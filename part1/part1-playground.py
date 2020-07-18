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
    celcius = (round((temp_in_farenheit - 32) * 5.0/9.0))
    return(celcius)

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
    return(mean)

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
        for key1,key2 in json_data.items():    # .items accesses or prints out values and keys
            print(key1)

        # for temp in json_data:
        #     print()
   
    # print(type(json_data))
    return 

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))
    # iso_string = "2020-06-19T07:00:00+08:00"
    # print(convert_date(iso_string))

# print daily forcaset @ 93


#  },
#   "DailyForecasts": [
#     {
#       "Date": "2020-06-19T07:00:00+08:00",
#       "EpochDate": 1592521200,
#       "Sun": {
#         "Rise": "2020-06-19T07:16:00+08:00",
#         "EpochRise": 1592522160,
#         "Set": "2020-06-19T17:20:00+08:00",
#         "EpochSet": 1592558400
#       },
#       "Temperature": {
#         "Minimum": {
#           "Value": 47,
#           "Unit": "F",
#           "UnitType": 18
#         },




