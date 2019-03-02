
from pandas import read_csv
import pandas as pd
import datetime
import numpy as np

data_path = 'data/NILU_Dataset_Trondheim_2014-2019.csv'
metro_path = 'data/weather/weather_bakke_kirke'
traffic_path = "data/TrafikkData/Bakke Kirke_cleaned.csv"

def concat(path_1, path_2, path_3):
  df = pd.read_csv(path_1, index_col=[0], header=[0, 1])
  df.index.name = 'timestamp'
  df.index = pd.to_datetime(df.index)
  df_1 = pd.merge(df["Bakke kirke"], df["weather"], on="timestamp")

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

  df_1.to_csv("Bakke_super", sep=';')

#concat(data_path, metro_path, traffic_path)
