import csv
with open('demo.csv', encoding='utf8') as file:
  reader = csv.reader(file, delimiter = ",")
  line_count = 0
  for row in reader:
      print(row)