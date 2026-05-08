"""Check what notes corelli has near tick 27360."""
import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\s\MS\tools\dcml\corelli\MS3\op01n08a.mscx')
root = tree.getroot()

# Find all measures and their notes, accumulate ticks
# Notes: look at tick positions
TARGET_TICKS = {27360, 27840}
TPQ = 480  # ticks per quarter, standard

# Walk through all parts to find notes around the target ticks
# We need to track cumulative ticks
print("Scanning corelli for notes near tick 27360 and 27840...")

for part in root.findall('.//Part'):
    part_name = part.find('trackName')
    part_label = part_name.text if part_name is not None else 'unknown'

    cum_tick = 0
    for measure in part.findall('.//Measure'):
        # Check if there's an explicit tick (irregular measure)
        tick_elem = measure.get('len')

        for elem in measure:
            if elem.tag == 'voice':
                local_tick = 0
                for child in elem:
                    if child.tag == 'Rest':
                        dur = child.find('duration')
                        if dur is None:
                            dur = child.find('durationType')
                        # Skip complex duration parsing
                        # Just check if notes are at target ticks
                    elif child.tag == 'Chord':
                        global_tick = cum_tick  # approximate
                        if abs(global_tick - 27360) < 600 or abs(global_tick - 27840) < 600:
                            notes = child.findall('.//Note')
                            pitches = []
                            for note in notes:
                                pitch_elem = note.find('pitch')
                                tpc_elem = note.find('tpc')
                                if pitch_elem is not None:
                                    pitches.append(int(pitch_elem.text))
                            if pitches:
                                pcs = sorted(set(p % 12 for p in pitches))
                                print(f"  part={part_label:10} ~tick={global_tick} pitches={pitches} pcs={pcs}")
        # Rough measure length increment
        cum_tick += 1920  # 4/4 measure at 480ppq = 1920 ticks; may vary

print("\nNote: tick calculations are approximate. Check DCML annotation files for exact analysis.")
