import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# define functions that can be called on 

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_farenheit = float(temp_in_farenheit)
    celcius = (temp_in_farenheit - 32) * 5.0/9.0
    return round(celcius, 1)


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = (total/num_items)
    return round(mean, 1)


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)      

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# get values into lists
    date_list = []
    min_list = []
    max_list = []
    day_longphrase_list = []
    day_chanceofrain_list = []
    night_longphrase_list = []
    night_chanceofrain_list = []

    weather_list = []
    
    for day in json_data['DailyForecasts']:
       
        date_list.append(convert_date(day["Date"]))
        # date_list.append(day['key']['for']['date'])
        # print(date_list)

        max_list.append(convert_f_to_c(day["Temperature"]["Maximum"]["Value"]))
        # print(max_list)

        min_list.append(convert_f_to_c(day["Temperature"]["Minimum"]["Value"]))
        # print(min_list)
        
        day_longphrase_list.append((day["Day"]["LongPhrase"]))
        # print(day_longphrase_list)
        
        night_longphrase_list.append((day["Night"]["LongPhrase"]))
        # print(night_longphrase_list)

        # weather_list.append(date_list, min_list, max_list)
        # print(weather_list)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# daytime / nightime > initialised the two variables and used them as lists

    print()

    # calculate min, max, mean & update lists
    lowest_temp = format_temperature(min(min_list))
    # print(f"This is the lowest temp print out: {lowest_temp}")
    
    highest_temp = format_temperature(max(max_list))
    # print(f"This is the highest temp print out: {highest_temp}")
    
    total = sum(min_list)
    num_items = len(min_list)
    mean_min = format_temperature(convert_f_to_c(calculate_mean(total, num_items)))
    # print(f"This is the mean min print out: {mean_min}")

    total = sum(max_list)
    num_items = len(max_list)
    mean_max = format_temperature(convert_f_to_c(calculate_mean(total, num_items)))
    # print(f"This is the mean max print out: {mean_max}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    print()
    # format output into print statements to start

    print("5 Day Overview")
    print()
    print(f"    The lowest temperature will be {lowest_temp}, and will occur on <INSERT DATE WITH FUNCTION / FOR LOOP>.\n")
    print(f"    The highest temperature will be {highest_temp}, and will occur on <INSERT DATE WITH FUNCTION / FOR LOOP>.\n")
    print(f"    The average low this week is {mean_min}.\n")
    print(f"    The average high this week is {mean_max}.\n\n\n")
    print("test string")
    # add while loops for the day by day summaries. 



    for day in json_data['DailyForecasts']:
       
        date_list.append(convert_date(day["Date"]))
        # date_list.append(day['key']['for']['date'])
        # print(date_list)

        max_list.append(convert_f_to_c(day["Temperature"]["Maximum"]["Value"]))
        # print(max_list)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # now, format output message into a string
    output = """
    output goes here
    """

    return output
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print()




    # if using a while loop set i to 0, and add 1 each time it iterates, then stop the loop after 5
    