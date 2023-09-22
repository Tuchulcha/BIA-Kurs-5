# Complete code to generate InventoryMovement.csv using lists of lists for rows

## !!! FUNKAR KANSKE !!!

# Import necessary modules
import random
import csv
from datetime import datetime, timedelta

# Generate a list of dates for the specified range
start_date = datetime.strptime('2017-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2022-12-31', '%Y-%m-%d')
date_list = [start_date + timedelta(days=x) for x in range(0, (end_date-start_date).days + 1)]

# Read the CSV file as a list of lists, each inner list representing a row
csv_list = []
with open('C:\\Users\\Tono\\BIA-Kurs-5\\Gruppuppgift\\DimProducts.csv', 'r', encoding='ISO-8859-1') as f:
    # Skip the header line
    next(f)
    for line in f:
        # Remove newline character and split by commas
        row = line.strip().split(',')
        csv_list.append(row)

# Initialize results list to hold the generated rows
results = []

# Initialize InventoryMovementKey
InventoryMovementKey = 0

# Loop through each row in csv_list
for row in csv_list:
    ProductKey = row[0]
    ProductName = row[1]
    ProductSeason = row[2]
    
    # Initialize BoxUnitsBalance
    BoxUnitsBalance = 100
    
    # Create initial row
    InventoryMovementKey += 1
    initial_row = {
        'InventoryMovementKey': InventoryMovementKey,
        'MovementDate': date_list[0].strftime('%Y-%m-%d'),
        'ProductKey': ProductKey,
        'ProductName': ProductName,
        'UnitsIn': 0,
        'UnitsOut': 0,
        'UnitsBalance': BoxUnitsBalance
    }
    results.append(initial_row)
    
    # Loop through each date in date_list
    for current_date in date_list:
        # 50% chance to add UnitsIn
        if random.random() < 0.5:
            UnitsIn = random.randint(10, 20)
            BoxUnitsBalance += UnitsIn
            InventoryMovementKey += 1
            row_units_in = {
                'InventoryMovementKey': InventoryMovementKey,
                'MovementDate': current_date.strftime('%Y-%m-%d'),
                'ProductKey': ProductKey,
                'ProductName': ProductName,
                'UnitsIn': UnitsIn,
                'UnitsOut': 0,
                'UnitsBalance': BoxUnitsBalance
            }
            results.append(row_units_in)
        
        # Determine UnitsOutRows based on ProductSeason
        if ProductSeason == 'General':
            UnitsOutRows = random.randint(1, 10)
        elif ProductSeason == 'Summer':  # Assuming "Summer" is the season in season
            UnitsOutRows = random.randint(2, 3)
        else:
            UnitsOutRows = random.randint(1, 2)
        
        # Loop through UnitsOutRows
        for _ in range(UnitsOutRows):
            # Determine BoxUnitsOut based on ProductSeason
            if ProductSeason == 'General':
                BoxUnitsOut = random.randint(1, 5)
            elif ProductSeason == 'Summer':
                BoxUnitsOut = random.randint(1, 4)
            else:
                BoxUnitsOut = random.randint(1, 3)
            
            # Check if BoxUnitsOut > BoxUnitsBalance
            if BoxUnitsOut > BoxUnitsBalance:
                BoxUnitsOut = BoxUnitsBalance
            
            # Update BoxUnitsBalance
            BoxUnitsBalance -= BoxUnitsOut
            
            # Create row for UnitsOut
            InventoryMovementKey += 1
            row_units_out = {
                'InventoryMovementKey': InventoryMovementKey,
                'MovementDate': current_date.strftime('%Y-%m-%d'),
                'ProductKey': ProductKey,
                'ProductName': ProductName,
                'UnitsIn': 0,
                'UnitsOut': BoxUnitsOut,
                'UnitsBalance': BoxUnitsBalance
            }
            results.append(row_units_out)

# Save the results to a CSV file
output_file_path = 'C:\\Users\\Tono\\BIA-Kurs-5\\Gruppuppgift\\FactInventoryWithList.csv'
keys = results[0].keys()

with open(output_file_path, 'w', newline='', encoding='ISO-8859-1') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(results)

output_file_path
