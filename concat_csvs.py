
from pandas import read_csv
import pandas as pd
import datetime
import numpy as np

data_path = 'data/NILU_Dataset_Trondheim_2014-2019.csv'
metro_path = 'data/weather/weather_elgeseter'
traffic_path = "data/TrafikkData/Elgeseter Gate_cleaned.csv"

def concat(path_1, path_2, path_3):
  df = pd.read_csv(path_1, index_col=[0], header=[0, 1])
  df.index.name = 'timestamp'
  df.index = pd.to_datetime(df.index)
  df_1 = pd.merge(df["Elgeseter"], df["weather"], on="timestamp")

  df_2 = read_csv(path_2, index_col=[1])
  df_2.index.name = 'timestamp'
  df_2.index = pd.to_datetime(df_2.index)
  df_1 = pd.merge(df_1, df_2, on="timestamp", how="inner")
  df_1 = df_1.drop("Unnamed: 0", axis=1)

  df_3 = read_csv(path_3, index_col=[2])
  df_3.index.name = 'timestamp'
  df_3.index = pd.to_datetime(df_3.index)
  print(df_3)
  df_1 = pd.merge(df_1, df_3, on="timestamp", how="inner")
  df_1 = df_1.drop("Unnamed: 0", axis=1)

  print(df_1)

  df_1.to_csv("Elgeseter_super", sep=';')

#concat(data_path, metro_path, traffic_path)



#def concat(path_1, path_2):
#  df_1 = read_csv(path_1, delimiter=",", index_col=[0], header=[0, 1])
#  df_1.index.name = 'timestamp'
#  df_1.index = pd.to_datetime(df_1.index)
#  df_1 = df_1["Bakke kirke"].assign(traffic=0)
#  print(df_1)
#
#  df_2 = read_csv(path_2, index_col=[2])
#  df_2.index.name = 'timestamp'
#  df_2.index = pd.to_datetime(df_2.index)
#
#  intersection = df_1.index.intersection(df_2.index)
#  print(intersection)
#
#  counter = 0
#  for index in intersection:
#    df_1["traffic"][str(index)] = df_2["Bakke Kirke"][str(index)]
#    counter += 1
#    print(index)
#    print(counter)
#
#  print(df_1)
#  df_1.to_csv("all_data", sep=';')
#
#  return df_1

def fix_comma(df):
  res = df
# creating a list of dataframe columns
  columns = ["pressure", "rain", "temperature", "wind_speed"]
  counter = 0
  for j in df.index:
    counter += 1
    print(counter)
    try:
      df["pressure"][j] = float(df["pressure"][j].replace(',', '.'))
    except:
      pass
  print(res)

  counter = 0
  for j in df.index:
    counter += 1
    print(counter)
    try:
      df["rain"][j] = float(df["rain"][j].replace(',', '.'))
    except:
      pass
  print(res)

  counter = 0
  for j in df.index:
    counter += 1
    print(counter)
    try:
      df["temperature"][j] = float(df["temperature"][j].replace(',', '.'))
    except:
      pass
  print(res)
  counter = 0
  for j in df.index:
    counter += 1
    print(counter)
    try:
      df["wind_speed"][j] = float(df["wind_speed"][j].replace(',', '.'))

    except:
      pass
  print(res)
  return res
