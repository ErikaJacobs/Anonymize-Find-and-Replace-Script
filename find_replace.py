# The purpose of this Python script is to find and replace text in 
# multiple text-based files without having to open them and physically
# find and replace. While simple, this code can be very powerful!

import os
import pandas as pd

# The words being replaced
path = os.path.dirname(os.path.realpath(__file__)).replace('modules', '')
df = pd.read_csv(path + '/changes.csv')
words = [(x , y) for x, y in zip(df['BEFORE'], df['AFTER'])]

# The files that need words replaced
files = ["C:/folder/folder/folder/filename1.py", 
         "C:/folder/folder/folder/filename2.py"]

# Loop through all files and words
for file in files:
    for before, after in words:
        fin = open(file, "rt")
        data = fin.read()
        data = data.replace(before, after)
        fin.close()

        fin = open(file, "wt")
        fin.write(data)
        fin.close()
        
#%%