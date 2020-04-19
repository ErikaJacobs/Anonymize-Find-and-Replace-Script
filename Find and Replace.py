# The purpose of this Python script is to find and replace text in 
# multiple text-based files without having to open them and physically
# find and replace. While simple, this code can be very powerful!

# The files that need words replaced
files = ["C:/folder/folder/folder/filename1.py", 
         "C:/folder/folder/folder/filename2.py"]

# The words being replaced
# Example: "Cat" is before, "turtle" is after
words = [('Cat', 'turtle'), ('meow', 'moo'), ('dog', 'turnip')]

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