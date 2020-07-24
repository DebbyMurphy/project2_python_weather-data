import json
import plotly.express as px
import pandas as pd
from datetime import datetime


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

# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lists and Variables 

    date_list = []
    min_list = []
    max_list = []
    min_realfeel_list = []
    min_realfeelshade_list = []

    for day in json_data['DailyForecasts']:
        date_list.append(convert_date(day["Date"]))
        max_list.append(convert_f_to_c(day["Temperature"]["Maximum"]["Value"]))
        min_list.append(convert_f_to_c(day["Temperature"]["Minimum"]["Value"]))
        min_realfeel_list.append(convert_f_to_c(day["RealFeelTemperature"]["Minimum"]["Value"]))
        min_realfeelshade_list.append(convert_f_to_c(day["RealFeelTemperatureShade"]["Minimum"]["Value"]))

   # define the number of days in the source file
    num_days = len(date_list)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Graphs

    # Graph 1: Min & Max Temps by Day                            
    df = {
        "Dates": date_list,        
        "Minimum": min_list,
        "Maximum": max_list,
        "Min Real Feel": min_realfeel_list,
        "Min Real Feel Shade": min_realfeelshade_list
    }

    fig = px.line(
        df,
        x="Dates",
        y=["Minimum", "Maximum"],
        title=f"Min & Max Temperatures Over {num_days} Days"
    )

    fig.update_layout(
        yaxis_title='Temperature (Celcius)',
        legend_title_text='Temperatures'
    )
    fig.write_html("first-graph.html")

    # Graph 2: Minimum Temperatures by Day
    fig = px.line(
        df,
        x="Dates",
        y=["Minimum", "Min Real Feel", "Min Real Feel Shade"]
    )

    fig.update_layout(
        title=f"Minimum Temperatures Over {num_days} Days",
        yaxis_title='Temperature (Celcius)',
        legend_title_text='Minimum Temperatures'
    )
    fig.write_html("second-graph.html")
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    # print(process_weather("data/forecast_5days_a.json"))    
    # print(process_weather("data/forecast_5days_b.json"))
    print(process_weather("data/forecast_10days.json"))
    print()
