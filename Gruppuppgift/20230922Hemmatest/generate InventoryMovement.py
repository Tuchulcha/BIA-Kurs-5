#generate InventoryMovement.csv using namedtuples

## !!! FUNKAR INTE !!!
# Import necessary modules
import random
import csv
from datetime import datetime, timedelta
from collections import namedtuple

# Generate a list of dates for just the year 2017
start_date = datetime.strptime('2017-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2017-12-31', '%Y-%m-%d')
date_list = [start_date + timedelta(days=x) for x in range(0, (end_date-start_date).days + 1)]

# Define a namedtuple for better readability and immutability
DimProduct = namedtuple('DimProduct', ['product_id', 'product_name', 'product_season'])

# Read the CSV file as a list of namedtuples
tuple_list = []
with open('C:\\Users\\Tono\\BIA-Kurs-5\\Gruppuppgift\\DimProducts.csv', 'r', encoding='ISO-8859-1') as f:
    next(f)  # Skip header line
    for line in f:
        product_id, product_name, product_season = line.strip().split(',')
        tuple_list.append(DimProduct(product_id, product_name, product_season))

# Initialize results list to hold the generated rows
results_tuples_complete = []

# Initialize InventoryMovementKey
InventoryMovementKey = 0

# Loop through each row in tuple_list
for row in tuple_list:
    ProductKey = row.product_id
    ProductName = row.product_name
    ProductSeason = row.product_season
    
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
    results_tuples_complete.append(initial_row)
    
    # Loop through each date in date_list
    for current_date in date_list:
        # Similar logic as before, but using namedtuples for readability
        
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
            results_tuples_complete.append(row_units_in)
        
        if ProductSeason == 'General':
            UnitsOutRows = random.randint(1, 10)
        elif ProductSeason == 'Summer':  # Assuming "Summer" is the season in season
            UnitsOutRows = random.randint(2, 3)
        else:
            UnitsOutRows = random.randint(1, 2)
        
        for _ in range(UnitsOutRows):
            if ProductSeason == 'General':
                BoxUnitsOut = random.randint(1, 5)
            elif ProductSeason == 'Summer':
                BoxUnitsOut = random.randint(1, 4)
            else:
                BoxUnitsOut = random.randint(1, 3)
            
            if BoxUnitsOut > BoxUnitsBalance:
                BoxUnitsOut = BoxUnitsBalance
            
            BoxUnitsBalance -= BoxUnitsOut
            
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
            results_tuples_complete.append(row_units_out)

# Save the results to a CSV file
output_file_path_tuples_complete = 'C:\\Users\\Tono\\BIA-Kurs-5\\Gruppuppgift\\FactInventoryWithTuples.csv'
keys = results_tuples_complete[0].keys()

with open(output_file_path_tuples_complete, 'w', newline='', encoding='ISO-8859-1') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(results_tuples_complete)

output_file_path_tuples_complete
