"""VL-C feature-space measurement (axis-2 foundation build, CC 2026-07-03).

Read-only. Decides, BY MEASUREMENT (spec cowork_voiceleading_axis_design.md §5.3,
knowledge-based coding), which feature space the dormant VL-C texture classifier
implements. Three named candidates (§5.3; raw concatenation A+B is rejected a priori
for the measured motion-signal dilution, findings v2.0):

    (1) motion-only        = View B (4-d parallel/similar/contrary/oblique)
    (2) two-stage          = motion super-split (B) then melodic refinement (A)
    (3) z-scored concat    = View ABz (20-d, per-dim z-scored)

Criterion (§10(b)): reproduce the RATIFIED cluster memberships. The ratified table is
the four-class taxonomy fitted on the concatenated space at the study's confound cap
(idiom_table(recs,'AB',K=4,cap_n=80,seed=0) in run_vl_discovery.py). VL-C classifies by
NEAREST-CENTROID against a shipped reference set, so the decisive metric is how well
nearest-centroid IN EACH CANDIDATE SPACE reproduces that ratified partition (ARI +
label-aligned accuracy). Free-clustering recovery is reported as supporting evidence.

Usage:  .venv/Scripts/python.exe idiom_discovery/run_vl_feature_space.py
        (reads the study's cached records $TEMP/vl_records.pkl; VL_RELOAD=1 re-parses)
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score as ARI
import run_vl_discovery as rd   # reuse load_all / cap / matrix VERBATIM (identical construction)

SEED = 0
K = 4
CAP = 80


def nearest_centroid(X, ref_labels):
    """Fit per-class centroids from ref_labels, assign each row to its nearest centroid.
    Labels are the reference labels themselves (centroid k <-> class k), so the returned
    prediction is directly label-comparable to ref_labels (no Hungarian needed)."""
    ks = sorted(set(ref_labels))
    C = np.array([X[ref_labels == k].mean(0) for k in ks])
    d = ((X[:, None, :] - C[None, :, :]) ** 2).sum(2)   # (n, K) squared euclidean
    idx = d.argmin(1)
    return np.array([ks[i] for i in idx])


def two_stage_predict(X_A, X_B, ref_labels):
    """Two-stage nearest-centroid (declared build-time formulation):
      Stage 1 — a 2-way motion super-split. Super-groups are DATA-DERIVED: KMeans(2,seed)
        on the B features; each reference class maps to its majority super. Two super-
        centroids are the mean B over each super-group. A piece's super = nearest super-
        centroid in B-space.
      Stage 2 — within the assigned super, nearest sub-centroid in A-space among that
        super's reference classes.
    Returns the predicted reference-class label per piece."""
    ks = sorted(set(ref_labels))
    super_lab = KMeans(2, random_state=SEED, n_init=10).fit_predict(X_B)   # 0/1 per piece
    # each reference class -> its majority super
    cls_super = {}
    for k in ks:
        m = ref_labels == k
        cls_super[k] = int(round(super_lab[m].mean()))   # majority (0/1)
    supers = sorted(set(cls_super.values()))
    # super-centroids in B (mean B over the classes assigned to that super)
    superC = {}
    for s in supers:
        m = np.isin(ref_labels, [k for k in ks if cls_super[k] == s])
        superC[s] = X_B[m].mean(0)
    # sub-centroids in A, per reference class
    subC = {k: X_A[ref_labels == k].mean(0) for k in ks}
    pred = np.empty(len(ref_labels), dtype=int)
    for i in range(len(ref_labels)):
        ds = {s: ((X_B[i] - superC[s]) ** 2).sum() for s in supers}
        s = min(ds, key=ds.get)
        cand = [k for k in ks if cls_super[k] == s]
        da = {k: ((X_A[i] - subC[k]) ** 2).sum() for k in cand}
        pred[i] = min(da, key=da.get)
    return pred


def acc(ref, pred):
    return float((ref == pred).mean())


def main():
    recs = rd.load_all()
    capped = rd.cap(recs, CAP)
    X_AB, keep = rd.matrix(capped, 'AB')      # the ratified table's exact matrix
    L = KMeans(K, random_state=SEED, n_init=10).fit_predict(X_AB)
    n = len(keep)
    sizes = [int((L == k).sum()) for k in sorted(set(L))]
    print("=== VL-C feature-space measurement ===")
    print("reference = ratified AB K=%d clustering, cap=%d, seed=%d  (n=%d pieces)" % (K, CAP, SEED, n))
    print("reference class sizes: %s   (study idiom_table AB expected 360/329/395/325)" % sizes)

    X_A = np.array([r['A'] for r in keep])
    X_B = np.array([r['B'] for r in keep])
    X_ABz = (X_AB - X_AB.mean(0)) / (X_AB.std(0) + 1e-9)

    print("\n--- DECISIVE metric: nearest-centroid reproduction of the ratified partition ---")
    print("  space            nc-ARI   nc-accuracy")
    rows = {}
    for name, X in [("motion-only(B)", X_B), ("z-concat(ABz)", X_ABz)]:
        pred = nearest_centroid(X, L)
        rows[name] = (ARI(L, pred), acc(L, pred))
        print("  %-16s %.3f    %.3f" % (name, rows[name][0], rows[name][1]))
    ts_pred = two_stage_predict(X_A, X_B, L)
    rows["two-stage(B->A)"] = (ARI(L, ts_pred), acc(L, ts_pred))
    print("  %-16s %.3f    %.3f" % ("two-stage(B->A)", rows["two-stage(B->A)"][0], rows["two-stage(B->A)"][1]))

    print("\n--- SUPPORTING: free re-clustering recovery of the ratified partition (ARI) ---")
    for name, X in [("motion-only(B)", X_B), ("z-concat(ABz)", X_ABz)]:
        km = KMeans(K, random_state=SEED, n_init=10).fit_predict(X)
        print("  %-16s free-KMeans4 ARI=%.3f" % (name, ARI(L, km)))

    winner = max(rows, key=lambda k: rows[k][0])
    print("\nWINNER (highest nearest-centroid ARI): %s   ARI=%.3f acc=%.3f"
          % (winner, rows[winner][0], rows[winner][1]))
    # cross-check nc-ARI ordering is not a knife-edge tie
    ordered = sorted(rows.items(), key=lambda kv: -kv[1][0])
    print("ranking: " + " > ".join("%s(%.3f)" % (k, v[0]) for k, v in ordered))

    assert winner == "z-concat(ABz)", "winner changed — re-derive the C++ reference/export"

    # === reference-set export for the C++ VL-C classifier (winning space = ABz) ===
    import sklearn
    mean = X_AB.mean(0)
    std = X_AB.std(0)                       # population std (ddof=0) — matches run_vl_discovery ABz
    Xz = (X_AB - mean) / (std + 1e-9)
    centroidZ = np.array([Xz[L == k].mean(0) for k in sorted(set(L))])   # (4,20) in z-space

    # per-class RAW signatures (for deterministic, index-independent naming)
    FEAT = (["P|iv|=%d" % k for k in range(12)] + ["P|iv|>=12", "repeat", "step", "leap",
            "parallel", "similar", "contrary", "oblique"])
    rawC = np.array([X_AB[L == k].mean(0) for k in sorted(set(L))])
    iPar, iSim, iCon, iObl = 16, 17, 18, 19
    iStep, iLeap = 14, 15
    print("\n--- per-class RAW signatures (naming basis) ---")
    for k in range(K):
        print("  class%d n=%3d  step=%.2f leap=%.2f par=%.2f sim=%.2f con=%.2f obl=%.2f"
              % (k, int((L == k).sum()), rawC[k, iStep], rawC[k, iLeap],
                 rawC[k, iPar], rawC[k, iSim], rawC[k, iCon], rawC[k, iObl]))
    # signature-based greedy naming (index-independent, reproducible)
    remaining = set(range(K))
    contrapuntal = max(remaining, key=lambda k: rawC[k, iCon] + rawC[k, iSim] - rawC[k, iObl] - rawC[k, iLeap])
    remaining.discard(contrapuntal)
    pianistic = max(remaining, key=lambda k: rawC[k, iLeap]); remaining.discard(pianistic)
    classical = max(remaining, key=lambda k: rawC[k, iObl]); remaining.discard(classical)
    moderate = remaining.pop()
    name = {contrapuntal: "Contrapuntal", pianistic: "HomophonicPianistic",
            classical: "HomophonicClassical", moderate: "ModerateMixed"}
    print("  naming: c%d=Contrapuntal  c%d=HomophonicPianistic  c%d=HomophonicClassical  c%d=ModerateMixed"
          % (contrapuntal, pianistic, classical, moderate))

    # fit distribution (euclidean nearest-centroid distance in z-space) -> floor defaults
    d = np.sqrt(((Xz[:, None, :] - centroidZ[None, :, :]) ** 2).sum(2))   # (n,4)
    dsort = np.sort(d, 1)
    dBest = dsort[:, 0]
    fitScale = float(np.median(dBest))                                    # median best-distance
    fitBest = np.exp(-dBest / fitScale)
    fitSecond = np.exp(-dsort[:, 1] / fitScale)
    margin = fitBest - fitSecond
    print("\n--- fit distribution (z-space euclidean nearest-centroid) ---")
    print("  dBest: median=%.3f p90=%.3f  fitScale(default)=%.3f" % (np.median(dBest), np.percentile(dBest, 90), fitScale))
    print("  fitBest:  p05=%.3f p10=%.3f median=%.3f" % (np.percentile(fitBest, 5), np.percentile(fitBest, 10), np.median(fitBest)))
    print("  margin :  p05=%.3f p10=%.3f median=%.3f" % (np.percentile(margin, 5), np.percentile(margin, 10), np.median(margin)))

    def fmt(a):
        return ", ".join("%.9g" % x for x in a)

    hdr = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "src", "composing", "analysis", "voiceleading", "textureclassifierreference.h")
    order = [contrapuntal, classical, pianistic, moderate]   # stable emit order: Con, Class, Pian, Mod
    enumname = {contrapuntal: "Contrapuntal", classical: "HomophonicClassical",
                pianistic: "HomophonicPianistic", moderate: "ModerateMixed"}
    lines = []
    lines.append("// GENERATED by idiom_discovery/run_vl_feature_space.py — DO NOT EDIT BY HAND.")
    lines.append("// VL-C texture-classifier reference set (spec cowork_voiceleading_axis_design.md §5.3).")
    lines.append("//")
    lines.append("// PROVENANCE (the shipped-parameter contract, §5.3):")
    lines.append("//   run          : run_vl_feature_space.py feature-space measurement, CC 2026-07-03")
    lines.append("//   corpus state : study cache vl_records.pkl — 2102 pieces / 45 note-level sources")
    lines.append("//                  (findings v2.0; cc_vl_idiom_discovery_report.md)")
    lines.append("//   feature space: WINNER = z-scored concatenation (ABz); nearest-centroid reproduces")
    lines.append("//                  the ratified AB K=4 partition at ARI=%.3f accuracy=%.3f" % (rows["z-concat(ABz)"][0], rows["z-concat(ABz)"][1]))
    lines.append("//                  (two-stage %.3f, motion-only %.3f — §5.3 candidates)." % (rows["two-stage(B->A)"][0], rows["motion-only(B)"][0]))
    lines.append("//   clustering   : KMeans(K=4, random_state=0, n_init=10), sklearn %s; cap=80/source" % sklearn.__version__)
    lines.append("//   fit space    : mean/std over the cap=80 fit set (n=%d); z-space euclidean nearest-centroid." % n)
    lines.append("//   feature order (20-d): A[0..11]=P(|iv|=k) k0..11, A[12]=P(|iv|>=12), A[13]=repeat,")
    lines.append("//                  A[14]=step, A[15]=leap, B[16]=parallel, B[17]=similar, B[18]=contrary, B[19]=oblique.")
    lines.append("#pragma once")
    lines.append("#include <array>")
    lines.append("")
    lines.append("namespace mu::composing::analysis::voiceleading {")
    lines.append("")
    lines.append("inline constexpr int kVlFeatureDim = 20;")
    lines.append("inline constexpr int kVlTextureClassCount = 4;")
    lines.append("")
    lines.append("// Raw-feature normalization (subtract mean, divide by std+1e-9) then nearest-centroid in z-space.")
    lines.append("inline constexpr std::array<double, 20> kVlRefMean = { %s };" % fmt(mean))
    lines.append("inline constexpr std::array<double, 20> kVlRefStd  = { %s };" % fmt(std))
    lines.append("")
    lines.append("// Class centroids in z-space, in enum order (Contrapuntal, HomophonicClassical, HomophonicPianistic, ModerateMixed).")
    lines.append("inline constexpr std::array<std::array<double, 20>, 4> kVlRefCentroidZ = {{")
    for k in order:
        lines.append("    {{ %s }},  // %s (n=%d)" % (fmt(centroidZ[k]), enumname[k], int((L == k).sum())))
    lines.append("}};")
    lines.append("")
    lines.append("// Precision-phase floor DEFAULTS derived from the fit distribution over the fit set (documented, NOT tuned).")
    lines.append("inline constexpr double kVlFitScaleDefault  = %.9g;  // median best-distance" % fitScale)
    lines.append("inline constexpr double kVlFitFloorDefault  = %.9g;  // ~p05 of best-fit exp(-dBest/scale)" % float(np.percentile(fitBest, 5)))
    lines.append("inline constexpr double kVlMarginFloorDefault = %.9g;  // ~p05 of best-vs-second fit margin" % float(np.percentile(margin, 5)))
    lines.append("")
    lines.append("} // namespace mu::composing::analysis::voiceleading")
    lines.append("")
    os.makedirs(os.path.dirname(hdr), exist_ok=True)
    open(hdr, "w", encoding="utf-8").write("\n".join(lines))
    print("\nwrote reference header -> %s" % hdr)


if __name__ == "__main__":
    main()
