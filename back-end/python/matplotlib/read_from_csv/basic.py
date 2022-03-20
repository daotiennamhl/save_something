import csv
with open('test.csv') as csv_file:
    # csv_reader = csv.reader(csv_file)
    csv_reader = csv.DictReader(csv_file)
    [print(row) for row in csv_reader]