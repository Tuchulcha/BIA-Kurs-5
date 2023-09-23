from datetime import datetime, timedelta
import csv

# Read the CSV file as a list of tuples 
with open('C:\\Users\\Tono\\BIA-Kurs-5\\Gruppuppgift\\DimProducts.csv', 'r', encoding='ISO-8859-1') as f:
    # Read lines and split by commas
    lines = f.readlines()
    # Remove the header and strip newline characters
    lines = [line.strip() for line in lines[1:]]
    # Convert each line to a tuple
    tuple_data = [tuple(line.split(',')) for line in lines]

# Generate a list of dates for the specified range
start_date = datetime.strptime('2017-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2017-12-31', '%Y-%m-%d')
date_list = [start_date + timedelta(days=x) for x in range(0, (end_date-start_date).days + 1)]

# Function to loop through list of tuples row-by-row and a list of dates
def nested_loop_with_date_list(tuple_list, date_list):
    results = []
    
    for index, row_tuple in enumerate(tuple_list):
        for current_date in date_list:
            # Do something with each row and date here. For now, just collect some sample output.
            results.append(f"Row {index}: {row_tuple[1]} - Date: {current_date.strftime('%Y-%m-%d')}")
            
    return results[:10]  # Return the first 10 results as a sample

# Perform the nested loop
sample_results_with_date_list = nested_loop_with_date_list(tuple_data, date_list)

sample_results_with_date_list


