import csv


file = open("data/ex9_cities.csv","r")


try:
    print("yes")
    csv_reader = csv.DictReader(file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Column names: ", row)
        else:
            print("rank: ", row[0], "City: ", row[1], "State: ", row[2], "Population: ", row[3])
        line_count += 1
finally:
    file.close()
# Using dictionary read function ther ewe can use coulme name as a keys like row["rank"]

# Using dictionary read function ther ewe can use coulme name as a keys like row["rank"]
