import pandas as pd
from datetime import datetime, timedelta

def change_wrongly_formatted_csv(input_file):
    with open(input_file) as file:
        data = file.read()
        data = data.replace(";", ",")
    with open(input_file, "w") as file:
        file.write(data)

# Converting datetime
def convert_timestamp_to_datetime(timestamp, before_or_after):
    date = timestamp.split("T")[0]
    splitted_date = date.split("-")
    time = timestamp.split("T")[1]
    splitted_time = time.split("+")[0].split(":")
    t = datetime(int(splitted_date[0]), int(splitted_date[1]), int(splitted_date[2]), int(splitted_time[0]), int(splitted_time[1]))
    data = {"Timestamp": t}
    data[before_or_after + "hour"] = t.hour
    data[before_or_after + "month"] = t.month
    data[before_or_after + "year"] = t.year
    data[before_or_after + "day_of_week"] = t.weekday()
    data[before_or_after + "day_of_month"] = t.day
    data[before_or_after + "day_of_year"] = t.timetuple().tm_yday
    return data

trafikk_data_path = "trafikk.csv"
# change_wrongly_formatted_csv(trafikk_data_path)
trafikk_data = pd.read_csv(trafikk_data_path)
trafikk_data["output_volum"] = 0

test_timestamp = "2019-02-27T01:00+01:00"
for i in trafikk_data.index:
    fra_time = trafikk_data.at[i, "Fra"]
    data_dict = convert_timestamp_to_datetime(fra_time, "fra_")
    for key, value in data_dict.items():
        trafikk_data.at[i, key] = value

trafikk_data = trafikk_data.drop(["Navn", "Vegreferanse", "Fra", "Til",
 "Ikke gyldig lengde", "Lengdedekningsgrad (%)", "Felt", "Felt gyldig fra",
 "Felt gyldig til", "< 5", "6m", "> 5", "6m.1", "5", "6m - 7", "6m.2", "7",
 "6m - 12", "5m", "12", "5m - 16", "0m", "16", "0m - 24", "0m.1", "> 24", "0m.2"], axis=1)

number_of_hours_to_subtract = 6

for i in trafikk_data.index:
    for j in trafikk_data.index:
        before_data = trafikk_data.at[i, "Timestamp"]
        after_data = trafikk_data.at[j, "Timestamp"]
        t= datetime()
        timedelta(hours=6)
        before_data

        all_match = True
        for column in trafikk_data.columns.values:
            if(column == "hour" and trafikk_data.at[i, column]  - 6 == trafikk_data.at[j, column]):
                pass
            elif(trafikk_data.at[i, column] == trafikk_data.at[j, column]):
                pass
