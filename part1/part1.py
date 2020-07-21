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
    
    for day in json_data['DailyForecasts']:
        date_list.append(convert_date(day["Date"]))
        max_list.append(convert_f_to_c(day["Temperature"]["Maximum"]["Value"]))
        min_list.append(convert_f_to_c(day["Temperature"]["Minimum"]["Value"]))
        day_longphrase_list.append((day["Day"]["LongPhrase"]))
        day_chanceofrain_list.append((day["Day"]["RainProbability"]))
        night_longphrase_list.append((day["Night"]["LongPhrase"]))
        night_chanceofrain_list.append((day["Night"]["RainProbability"]))

    # append lists into the weather list
    weather_list = []

    weather_list.append(date_list)  #weather_list[0][<position of day here>]
    weather_list.append(min_list)   #weather_list[1][<position of day here>]
    weather_list.append(max_list)   #weather_list[2][<position of day here>]
    weather_list.append(day_longphrase_list)        #weather_list[3][<position of day here>]
    weather_list.append(day_chanceofrain_list)      #weather_list[4][<position of day here>]
    weather_list.append(night_longphrase_list)      #weather_list[5][<position of day here>]
    weather_list.append(night_chanceofrain_list)    #weather_list[6][<position of day here>]

    # calculate min, max, mean & update lists
    lowest_temp = min(min_list)
    index_min = min_list.index(lowest_temp)
    
    highest_temp = max(max_list)
    index_max = max_list.index(highest_temp)
    
    total = sum(min_list)
    num_items = len(min_list)
    mean_min = convert_f_to_c(calculate_mean(total, num_items))

    total = sum(max_list)
    num_items = len(max_list)
    mean_max = convert_f_to_c(calculate_mean(total, num_items))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # format output into print statements to start

    num_days = len(date_list)
    
    # print(f"{num_days} Day Overview\n")
    # print(f"    The lowest temperature will be {format_temperature(lowest_temp)}, and will occur on {date_list[index_min]}.\n")
    # print(f"    The highest temperature will be {format_temperature(highest_temp)}, and will occur on {date_list[index_max]}.\n")
    # print(f"    The average low this week is {mean_min}.\n")
    # print(f"    The average high this week is {mean_max}.\n\n\n")
    
    # # day by day summaries. 

    # for index in range(num_days):
    #     print(f"-------- {weather_list[0][index]} --------\n")
    #     print(f"Minimum Temperature: {format_temperature(weather_list[1][index])}\n")
    #     print(f"Maximum Temperature: {format_temperature(weather_list[2][index])}\n")
    #     print(f"Daytime: {weather_list[3][index]}\n")
    #     print(f"    Chance of rain: {weather_list[4][index]}%\n")
    #     print(f"Nighttime: {weather_list[5][index]}\n")
    #     print(f"    Chance of rain: {weather_list[6][index]}%\n\n")
        

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # now, format output message into a string
    output = ""
    output += (f"{num_days} Day Overview\n")
    output += (f"    The lowest temperature will be {format_temperature(lowest_temp)}, and will occur on {date_list[index_min]}.\n")
    output += (f"    The highest temperature will be {format_temperature(highest_temp)}, and will occur on {date_list[index_max]}.\n")
    output += (f"    The average low this week is {mean_min}.\n")
    output += (f"    The average high this week is {mean_max}.\n\n\n")
    
    # day by day summaries. 

    for index in range(num_days):
        output += (f"-------- {weather_list[0][index]} --------\n")
        output += (f"Minimum Temperature: {format_temperature(weather_list[1][index])}\n")
        output += (f"Maximum Temperature: {format_temperature(weather_list[2][index])}\n")
        output += (f"Daytime: {weather_list[3][index]}\n")
        output += (f"    Chance of rain:  {weather_list[4][index]}%\n")
        output += (f"Nighttime: {weather_list[5][index]}\n")
        output += (f"    Chance of rain:  {weather_list[6][index]}%\n\n")

        
    #     output += (f"5 Day Overview\n    The lowest temperature will be {format_temperature(lowest_temp)}, and will occur on {date_list[index_min]}.\n")

    return output
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    print()
