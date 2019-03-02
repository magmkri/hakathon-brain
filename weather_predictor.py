import requests
from trafikk_data import convert_timestamp_to_datetime, write_csv_to_file
import datetime
import pandas as pd

start_date = datetime.datetime(2018, 12, 12)
end_date = datetime.datetime(2019, 3, 1)

col_names = ['timestamp', 'no2_concentration', 'pm25_concentration', "pm10_concentration"]
df = pd.DataFrame(columns = col_names)

while start_date.date() != end_date.date():
    URL = "https://api.met.no/weatherapi/airqualityforecast/0.1/?station=NO0068A&reftime=" + str(start_date.date()) + "T12:00:00Z"
    r = requests.get(url=URL, params={})
    data = r.json()
    try:
        for element in data["data"]["time"]:
            date = convert_timestamp_to_datetime(element["to"])
            no2_concentration = element["variables"]["no2_concentration"]["value"]
            pm25_concentration = element["variables"]["pm25_concentration"]["value"]
            pm10_concentration = element["variables"]["pm10_concentration"]["value"]
            df.loc[len(df)] = [date, no2_concentration, pm25_concentration, pm10_concentration]
    except:
        pass
    start_date = start_date + datetime.timedelta(days=1)
df = df.set_index(pd.to_datetime(df['timestamp'])).drop(columns=['timestamp']).sort_index()
df = df[~df.index.duplicated(keep='first')]
write_csv_to_file(df, "./data/WeatherPredictionData/weather_prediction.csv")


