# Python writing files (txt, csv, json)

# txt_data = "I like pizzaaaaaaaaaaa"
#
# # file_path = "text.txt" #relative will be saved withnin the same directory im working on
#
# file_path = "C:\\Users\\Maryam M\\Desktop\\text.txt" #abolsute
#
#
# try:
#     with open(file = file_path, mode = "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file {file_path} was created")
#
# except FileExistsError:
#     print("File already exists")
#
# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
#
# file_path = "C:\\Users\\Maryam M\\Desktop\\text.txt" #abolsute
#
#
# try:
#     with open(file = file_path, mode= "w") as file:
#
#         for employee in employees:
#             file.write(employee + " ")
#         print(f'Txt file {file_path} was created')
# except FileExistsError:
#     print("File already exists")

# import json # amything with with key values
#
# employee = {
#
#     "name" : "Spongebob",
#     "age" : 11,
#     "job" : "cook"
# }
#
# file_path = "C:\\Users\\Maryam M\\Desktop\\text.json" #abolsute
#
#
# try:
#     with open(file = file_path, mode= "w") as file:
#         json.dump(employee, file, indent = 4) # indent arg to create spaces
#         print(f'json file {file_path} was created')
#
# except FileExistsError:
#     print("File already exists")


import csv
employees = [["Name", "Age", "Job"],
             ["Spongebob", 21, "Cook"],
             ["Patrick", 22, "Waiter"],
             ["Eugene", 25, "Boss"]]

file_path = "C:\\Users\\Maryam M\\Desktop\\text.csv" #abolsute

try:
    with open(file = file_path, mode= "w") as file:
        writer = csv.writer(file)

        for row in employees:
            writer.writerow(row)
        print(f'csv file {file_path} was created')
except FileExistsError:
    print("File already exists")