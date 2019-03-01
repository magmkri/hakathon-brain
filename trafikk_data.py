import pandas as pd
from datetime import datetime, timedelta
desired_width=320


pd.set_option('display.width', desired_width)

pd.set_option('display.max_columns', 10)


def change_wrongly_formatted_csv(input_file):
    with open(input_file) as file:
        data = file.read()
        data = data.replace(";", ",")
    with open(input_file, "w") as file:
        file.write(data)

# Converting datetime
def convert_timestamp_to_datetime(timestamp):
    date = timestamp.split("T")[0]
    splitted_date = date.split("-")
    time = timestamp.split("T")[1]
    splitted_time = time.split("+")[0].split(":")
    t = datetime(int(splitted_date[0]), int(splitted_date[1]), int(splitted_date[2]), int(splitted_time[0]), int(splitted_time[1]))
    data = {"Timestamp": t}
    return data

#trafikk_data_path = "./data/TrafikkData/Elgeseter Gate.csv"
#change_wrongly_formatted_csv(trafikk_data_path)
#trafikk_data = pd.read_csv(trafikk_data_path)


#delete_these_indexes = []
#for i in range(0, len(trafikk_data)):
#    fra_time = trafikk_data.at[i, "Fra"]
#    data_dict = convert_timestamp_to_datetime(fra_time)
#    for key, value in data_dict.items():
#        trafikk_data.at[i, key] = value
#
#    if trafikk_data.at[i, "Felt"] != "Totalt":
#        delete_these_indexes.append(i)
#
#trafikk_data = trafikk_data.drop(delete_these_indexes)
#
#print(trafikk_data.columns.values)
#trafikk_data = trafikk_data.drop(["Navn", "Vegreferanse", "Fra", "Til", "Felt", "Trafikkregistreringspunkt",
# "Ikke gyldig lengde", "Lengdedekningsgrad (%)", "Felt gyldig fra",
# "Felt gyldig til", "< 5", "6m", "> 5", "6m.1", "5", "6m - 7", "6m.2", "7",
# "6m - 12", "5m", "12", "5m - 16", "0m", "16", "0m - 24", "0m.1", "> 24", "0m.2"], axis=1)

#trafikk_data = trafikk_data.drop(["Navn", "Vegreferanse", "Fra", "Felt", "Trafikkregistreringspunkt", "Til",
# "Ikke gyldig lengde", "Lengdedekningsgrad (%)", "Felt gyldig fra",
# "Felt gyldig til", "< 5", 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
 #'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17'], axis=1)

#trafikk_data = trafikk_data.rename(columns={'Volum': 'Elgeseter Gate'})
#print(trafikk_data.head())#



trafikk_data_path_1 = "./data/TrafikkData/Brattorbrua_cleaned.csv"
trafikk_data_1 = pd.read_csv(trafikk_data_path_1)

trafikk_data_path_2 = "./data/TrafikkData/Bakke Kirke_cleaned.csv"
trafikk_data_2 = pd.read_csv(trafikk_data_path_2)
trafikk_data_path_3 = "./data/TrafikkData/E6 Tiller_cleaned.csv"
trafikk_data_3 = pd.read_csv(trafikk_data_path_3)
trafikk_data_path_4 = "./data/TrafikkData/Elgeseter Gate_cleaned.csv"
trafikk_data_4 = pd.read_csv(trafikk_data_path_4)

trafikk_data_1 = pd.merge(trafikk_data_1, trafikk_data_2, on="Timestamp")
trafikk_data_1 = pd.merge(trafikk_data_1, trafikk_data_3, on="Timestamp")
trafikk_data_1 = pd.merge(trafikk_data_1, trafikk_data_4, on="Timestamp")
print(trafikk_data_1.columns.values)
trafikk_data_1 = trafikk_data_1.drop(['Unnamed: 0_x', 'Unnamed: 0_y', 'Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)

print(trafikk_data_1)
csv_file = trafikk_data_1.to_csv()

with open("./data/TrafikkData/final_traffic_data_cleaned.csv", "w") as file:
    file.write(csv_file)

