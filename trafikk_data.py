import pandas as pd
from datetime import datetime, timedelta

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)


# Vegvesenet's csv are formatted with ; instead of ,
def change_wrongly_formatted_csv(input_file):
    with open(input_file) as file:
        data = file.read()
        data = data.replace(";", ",")
    with open(input_file, "w") as file:
        file.write(data)


# Converting timestamp for vegvesen-csv to standard datetime
def convert_timestamp_to_datetime(timestamp):
    date = timestamp.split("T")[0]
    splitted_date = date.split("-")
    time = timestamp.split("T")[1]
    splitted_time = time.split("+")[0].split(":")
    t = datetime(int(splitted_date[0]), int(splitted_date[1]), int(splitted_date[2]), int(splitted_time[0]), int(splitted_time[1]))
    return t


# Convert the data from timestamp to datetime
def update_data_with_datetime(df):
    for i in range(0, len(df)):
        til_timestamp = df.at[i, "Til"]
        til_datetime = convert_timestamp_to_datetime(til_timestamp)
        df.at[i, "Datetime"] = til_datetime
    return df

# Remove rows that does not use total volume
def update_with_total_volume(df):
    delete_these_indexes = []
    for i in range(0, len(df)):
        if df.at[i, "Felt"] != "Totalt":
            delete_these_indexes.append(i)
    df = df.drop(delete_these_indexes)
    return df


# Merge all different CSV-files on datetime
def merge_data_on_datetime(list_of_csv_files):
    first_filename = list_of_csv_files[0]
    df = pd.read_csv(first_filename)

    for index in range(1, len(list_of_csv_files)):
        next_filename = list_of_csv_files[1]
        next_df = pd.read_csv(next_filename)
        df = pd.merge(df, next_df, on="Timestamp")
    df = df.drop(['Unnamed: 0_x', 'Unnamed: 0_y', 'Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)
    return df


def write_csv_to_file(df, filepath):
    csv_file = df.to_csv()
    with open(filepath, "w") as file:
        file.write(csv_file)


def drop_columns_standard(df):
    df = df.drop(["Navn", "Vegreferanse", "Fra", "Til", "Felt", "Trafikkregistreringspunkt",
                  "Ikke gyldig lengde", "Lengdedekningsgrad (%)", "Felt gyldig fra",
                  "Felt gyldig til", "< 5", "6m", "> 5", "6m.1", "5", "6m - 7", "6m.2", "7",
                  "6m - 12", "5m", "12", "5m - 16", "0m", "16", "0m - 24", "0m.1", "> 24", "0m.2"], axis=1)
    return df


def drop_columns_unnamed(df):
    df= df.drop(["Navn", "Vegreferanse", "Fra", "Felt", "Trafikkregistreringspunkt", "Til",
                 "Ikke gyldig lengde", "Lengdedekningsgrad (%)", "Felt gyldig fra",
                 "Felt gyldig til", "< 5", 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14',
                 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17'], axis=1)
    return df

trafikk_data_path_1 = "./data/TrafikkData/Brattorbrua_cleaned.csv"
trafikk_data_path_2 = "./data/TrafikkData/Bakke Kirke.csv"
trafikk_data_path_3 = "./data/TrafikkData/E6 Tiller_cleaned.csv"
trafikk_data_path_4 = "./data/TrafikkData/Elgeseter Gate_cleaned.csv"


current_data_traffic_path = trafikk_data_path_2
change_wrongly_formatted_csv(current_data_traffic_path)

trafikk_data = pd.read_csv(current_data_traffic_path)
trafikk_data = update_data_with_datetime(trafikk_data)
trafikk_data = update_with_total_volume(trafikk_data)
trafikk_data = drop_columns_standard(trafikk_data)
trafikk_data = trafikk_data.rename(columns={'Volum': 'Elgeseter Gate'})

write_csv_to_file(trafikk_data, "./data/TrafikkData/Bakke Kirke_cleaned.csv")

print(trafikk_data.columns.values)
print(trafikk_data.head())#




