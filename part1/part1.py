import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    return f"{temp}{DEGREE_SYBMOL}"

# # ----------SIMPLE OUTPUT WORKING----------

# # temp = 34
# # temp = str(temp)                        # if temp needs to be a string, convert it like this before passing into the function.
# # print(format_temperature(temp))
# # print(type(temp))                       # class = interger prior to wrapping temp as a string
# # print(type(format_temperature))       # class = function

# # ----------SIMPLE OUTPUT WORKING----------

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

# ----------SIMPLE OUTPUT NOT WORKING ----------

# iso_string = "2020-06-19T07.00:00+8:00"
# print(convert_date(iso_string))

# ----------SIMPLE OUTPUT NOT WORKING ----------

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

# ----------SIMPLE OUTPUT WORKING----------
# temp_in_farenheit = 50
# print(convert_f_to_c(temp_in_farenheit))
# ----------SIMPLE OUTPUT WORKING----------

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

# ----------SIMPLE OUTPUT WORKING----------
# temp = [4, 3, 2, 6]

# total = sum(temp)
# num_items = len(temp)

# print(calculate_mean(total, num_items))
# ----------SIMPLE OUTPUT WORKING----------

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

    # get values into lists
    date_list = []
    min_list = []
    max_list = []
    day_longphrase_list = []
    day_chanceofrain_list = []
    night_longphrase_list = []
    night_chanceofrain_list = []
    
    for day in json_data['DailyForecasts']:
       
        date_list.append(convert_date(day["Date"]))
        # date_list.append(day['key']['for']['date'])
        print(date_list)

        max_list.append(convert_f_to_c(day["Temperature"]["Maximum"]["Value"]))
        print(max_list)

        min_list.append(convert_f_to_c(day["Temperature"]["Minimum"]["Value"]))
        print(min_list)
        
        day_longphrase_list.append((day["Day"]["LongPhrase"]))
        print(day_longphrase_list)
        
        night_longphrase_list.append((day["Night"]["LongPhrase"]))
        print(night_longphrase_list)



# daytime / nightime > initialised the two variables and used them as lists

    print()

    # calculate min, max, mean
    lowest_temp = min(min_list)
    print(f"This is the lowest temp print out: {lowest_temp}")
    
    highest_temp = max(max_list)
    print(f"This is the highest temp print out: {highest_temp}")
    
    total = sum(min_list)
    num_items = len(min_list)
    mean_min = convert_f_to_c(calculate_mean(total, num_items))
    print(f"This is the mean min print out: {mean_min}")

    total = sum(max_list)
    num_items = len(max_list)
    mean_max = convert_f_to_c(calculate_mean(total, num_items))
    print(f"This is the mean max print out: {mean_max}")

    # format output message
    output = """
    output goes here

    5 Day Overview
    The lowest temperature will be 8.3°C, and will occur on Friday 19 June 2020.
    The highest temperature will be 22.2°C, and will occur on Sunday 21 June 2020.
    The average low this week is 11.7°C.
    The average high this week is 20.1°C.

    -------- Friday 19 June 2020 --------
    Minimum Temperature: 8.3°C
    Maximum Temperature: 17.8°C
    Daytime: Sunshine mixing with some clouds
        Chance of rain:  1%
    Nighttime: Clear
        Chance of rain:  0%  
    """
    print()

    print("5 Day Overview")


    return output

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))




    # if using a while loop set i to 0, and add 1 each time it iterates, then stop the loop after 5
    