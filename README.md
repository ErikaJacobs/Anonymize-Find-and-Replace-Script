# Anonymize Data in Multiple Files With a Click
This repository contains a simple script that finds and replaces text in multiple text-based files without having to physically open them. This script was developed as part of the [Excel Python SQL Migration](https://github.com/ErikaJacobs/Excel-Python-SQL-Migration) project, based on a need for anonymizing private data prior to sharing work on GitHub. While this script is not a large scale project, it is VERY powerful and useful if you find yourself needing to anonymize shared scripts.

## Methods Used
* Find and Replace

## Technologies Used
* Python
* Spyder

## Packages Used
* Pandas

## How To Run

##### Set-Up
The repository features a file called "changes.csv", which features two columns: BEFORE and AFTER. List words needing to be changed in the BEFORE column, and what the word should be changed to in the AFTER column. Please note that words are case sensitive.

File locations should be placed starting on line 14 of find_replace.py. File names should be entered as strings in the Python list on line 14.

##### Install Requirements and Run
On the command line of your operating system, navigate to the repository directory (ideally using a Python virtual environment).

Run the following code on the command line to install requirements:
```
pip install -r requirements.txt 
```

Run the following code on the command line to run this project:
```
Python find_replace.py
```

# Featured Scripts or Deliverables
* [Python Script](https://github.com/ErikaJacobs/Anonymize-Find-and-Replace-Script/blob/master/Find%20and%20Replace.pyy)

# Other Repository Contents
* No other repository contents at this time.

# Sources
* No sources
