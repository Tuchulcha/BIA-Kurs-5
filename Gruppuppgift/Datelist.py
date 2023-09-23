from datetime import datetime, timedelta
# Define the start and end dates
start_date = datetime(2017, 1, 1)
end_date = datetime(2022, 12, 31)
# Create an empty list to store the dates
date_list = []
# Generate the date range
current_date = start_date
while current_date <= end_date:
    date_list.append(current_date)
    current_date += timedelta(days=1)
# Print the list of dates
for date in date_list:
    print(date)