# Python reading files (txt, json, csv
from importlib.resources import contents
import json
import csv

file_path = "C:\\Users\\Maryam M\\Desktop\\text.csv"

try:
    with open(file_path, "r") as file:
        # content = file.read() # for txxt
        # content = json.load(file)  # for json
        content = csv.reader(file)  # for csv

        # print(content["name"]) # for json

        for line in content:
            if line: # cehcks if the row isnt empty
                print(line[2])

except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print('You do not have permsission to read that file')