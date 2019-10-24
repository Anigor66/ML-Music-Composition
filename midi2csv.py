import  py_midicsv
import pandas as pd

# Load the MIDI file and parse it into CSV format
csv_string = py_midicsv.midi_to_csv("Beethoven_Sonate_Op2_Scherzo.mid")
print(csv_string)
df=pd.DataFrame(csv_string)
df.to_csv("BT1.txt")
