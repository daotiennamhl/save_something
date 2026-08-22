import json
from datetime import datetime
from collections import defaultdict

# Load data from a.json
with open('json_file/acb.json', 'r') as f:
    data = json.load(f)

# Get date range from user
print("Enter date range to filter (or press Enter to skip):")
date_from_input = input("From date (YYYY-MM-DD): ").strip()
date_to_input = input("To date (YYYY-MM-DD): ").strip()

# Filter data by date range if provided
if date_from_input or date_to_input:
    filtered_data = []
    for item in data:
        item_date = datetime.fromisoformat(item['date'].replace('Z', '+00:00')).date()
        
        if date_from_input:
            date_from = datetime.strptime(date_from_input, '%Y-%m-%d').date()
        else:
            date_from = None
            
        if date_to_input:
            date_to = datetime.strptime(date_to_input, '%Y-%m-%d').date()
        else:
            date_to = None
        
        if (date_from is None or item_date >= date_from) and (date_to is None or item_date <= date_to):
            filtered_data.append(item)
    
    data = filtered_data
    if date_from_input and date_to_input:
        print(f"\nFiltering data from {date_from_input} to {date_to_input}\n")
    elif date_from_input:
        print(f"\nFiltering data from {date_from_input}\n")
    else:
        print(f"\nFiltering data to {date_to_input}\n")

# Group data by year
yearly_data = defaultdict(list)
for item in data:
    year = datetime.fromisoformat(item['date'].replace('Z', '+00:00')).year
    yearly_data[year].append(item)

# Calculate totals for each year
print("Results by Year:\n")
for year in sorted(yearly_data.keys()):
    items = yearly_data[year]
    value_diff = sum(item['buyForeignValue'] - item['sellForeignValue'] for item in items)
    quantity_diff = sum(item['buyForeignQuantity'] - item['sellForeignQuantity'] for item in items)
    
    print(f"Year {year}:")
    print(f"  buyForeignValue - sellForeignValue: {value_diff:,.2f}")
    print(f"  buyForeignQuantity - sellForeignQuantity: {quantity_diff:,.2f}")
    if quantity_diff != 0:
        print(f"  Average price difference per unit: {value_diff / quantity_diff:,.2f}")
    print()

# Calculate overall totals
print("Overall Total:")
total_difference = sum(item['buyForeignValue'] - item['sellForeignValue'] for item in data)
total_quantity_difference = sum(item['buyForeignQuantity'] - item['sellForeignQuantity'] for item in data)

print(f"Total (buyForeignValue - sellForeignValue): {total_difference:,.2f}")
print(f"Total (buyForeignQuantity - sellForeignQuantity): {total_quantity_difference:,.2f}")
if total_quantity_difference != 0:
    print(f"Average price difference per unit: {total_difference / total_quantity_difference:,.2f}")