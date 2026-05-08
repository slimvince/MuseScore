"""Parse corelli MSCX to find note pitch classes near tick 27360."""
import xml.etree.ElementTree as ET
from fractions import Fraction

SCORE_FILE = r'C:\s\MS\tools\dcml\corelli\MS3\op01n08a.mscx'
TARGET_TICK = 27360
TOLERANCE = 480  # +/- one quarter note

DURATION_MAP = {
    'whole': 1920, 'half': 960, 'quarter': 480, 'eighth': 240,
    'sixteenth': 120, '32nd': 60, '64th': 30,
}

tree = ET.parse(SCORE_FILE)
root = tree.getroot()

PC_NAMES = ['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B']

results = []

for part_idx, staff in enumerate(root.findall('.//Staff')):
    cum_tick = 0
    for measure in staff.findall('Measure'):
        mlen = measure.get('len')
        measure_start = cum_tick
        voice_tick = cum_tick

        for elem in measure:
            if elem.tag == 'voice':
                voice_tick = measure_start
                for child in elem:
                    if child.tag in ('Chord', 'Rest'):
                        # Find duration
                        dur_type = child.find('durationType')
                        if dur_type is None:
                            dur_type = child.find('dots')
                        dots = len(child.findall('dots'))

                        dur_text = None
                        for dt in child.iter('durationType'):
                            dur_text = dt.text
                            break
                        base_dur = DURATION_MAP.get(dur_text, 480)
                        # Apply dots
                        total_dur = base_dur
                        for _ in range(dots):
                            total_dur += base_dur // (2 ** (_ + 1))

                        # Check tuplets (approximate)
                        tuplet = child.find('.//Tuplet')

                        tick_here = voice_tick

                        if child.tag == 'Chord':
                            if abs(tick_here - TARGET_TICK) <= TOLERANCE:
                                pitches = []
                                for note in child.findall('.//Note'):
                                    pitch_elem = note.find('pitch')
                                    if pitch_elem is not None:
                                        p = int(pitch_elem.text)
                                        pitches.append(p)
                                if pitches:
                                    pcs = sorted(set(p % 12 for p in pitches))
                                    pc_names = [PC_NAMES[pc] for pc in pcs]
                                    results.append((tick_here, part_idx+1, pitches, pcs, pc_names))

                        voice_tick += base_dur  # approximate (ignoring tuplets/dots for now)

        # Advance measure
        if mlen:
            # len attribute is a fraction like "4/4"
            num, den = mlen.split('/')
            cum_tick += 1920 * int(num) // int(den)
        else:
            cum_tick += 1920  # default 4/4

results.sort()
print(f"Notes near tick {TARGET_TICK} (±{TOLERANCE}):")
for tick, staff_id, pitches, pcs, pc_names in results:
    print(f"  tick={tick:6} staff={staff_id} pitches={pitches} pcs={pcs} names={pc_names}")
