# Multiply each value in the radius column with 0.102763 to convert to solar radius.
# Multiply each value in the mass column with 0.000954588 to convert to solar mass.
# HOW TO DO THESE?
import csv
from unittest import skip

dataset_1 = []
dataset_2 = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("dwarf_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

header1 = dataset_1[0]
header2 = dataset_2[0]

planetdata1 = dataset_1[1:]
planetdata2 = dataset_2[1:]

headers = header1+header2
planetdata = []

for index, data in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("space_merged_stars_PRO-129.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)

with open("space_merged_stars_PRO-129.csv", "r") as input, open("PRO-129_stars_merged.csv", "w",newline = "") as output:
    csvwriter = csv.writer(output)

    for row in csv.reader(input):
        if any(field.strip() for field in row):
            csvwriter.writerow(row)

#with open("PRO-129_stars_merged.csv") as f:
#    csvreader = csv.reader(f)
#    for row in csvreader:
#        if row[10] == "":
#            skip
#        else:
#            row[10] = row[10]*0.102763 #row[10] is radius
#            print(row[10])