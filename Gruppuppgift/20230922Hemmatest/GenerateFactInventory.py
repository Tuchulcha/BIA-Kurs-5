from datetime import datetime

def get_meteorological_season(date):
    """
    Determine the meteorological season based on the date.

    Parameters:
        date (datetime): The date for which to determine the season.

    Returns:
        str: The meteorological season ("Spring", "Summer", "Autumn", "Winter").
    """
    month = date.month

    if month >= 3 and month <= 5:
        return "Spring"
    elif month >= 6 and month <= 8:
        return "Summer"
    elif month >= 9 and month <= 11:
        return "Fall"
    else:
        return "Winter"
# Test the function
test_dates = [
    datetime(2023, 1, 15),  # Winter
    datetime(2023, 4, 15),  # Spring
    datetime(2023, 7, 15),  # Summer
    datetime(2023, 10, 15)  # Fall
]
#seasons = [get_meteorological_season(date) for date in test_dates]
#print(seasons)

