import os
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

from .features import add_features

data_path = Path('../data/NILU_Dataset_Trondheim_2014-2019.csv')
cache_path = Path('./features.csv')

## Prepare data
def preprocess(config):
  pred_var = config['pred_var']
  stations = config['stations']
  test_size = config['test_size']
  val_size = config['val_size']
  shuffle = config['shuffle']
  window = config['window']

  if (os.path.exists(cache_path)):
    df = pd.read_csv(cache_path)
    df = df.set_index(pd.to_datetime(df['timestamp'])).drop(columns=['timestamp']).sort_index()
  else:
    df = pd.read_csv(data_path, index_col=[0], header=[0, 1])
    df.index.name = 'timestamp'
    df.index = pd.to_datetime(df.index)
    print(df.columns)
    df = df[[*stations, 'weather']]
    print(df.columns)
    df.columns = [' '.join(col).strip() for col in df.columns.values]
    print(df.columns)

    df = handle_missing(df, strategy='mean')
    df = add_features(df, labels=['Bakke kirke PM10', 'Bakke kirke PM2.5'])

    df.to_csv(cache_path)

  y = get_targets(df, pred_var, window)
  X = df
  data_dict = split_data(X, y, val_size=val_size, test_size=test_size, shuffle=shuffle)
  return data_dict

## Filler
def handle_missing(df, strategy):
  if strategy == 'mean':
    df = df.fillna(df.groupby([df.index.month, df.index.hour]).transform('mean'))
    df = df.fillna(df.mean())
  if strategy == 'drop':
    df.dropna(inplace=True)
  return df

## Add target values
def get_targets(df, pred_var, window):
  temp = pd.DataFrame(index=df.index)
  for x in range(1, window + 1):
    new_label = 'target_{}_t+{}h'.format(pred_var, x)
    temp[new_label] = df[pred_var].shift(-x)
  temp = temp.fillna(method='ffill')
  return temp

## Split
def split_data(X, y, test_size, val_size, shuffle):
  # Improve
  XX, X_test, yy, y_test = train_test_split(X, y, test_size=test_size, shuffle=False)
  X_train, X_val, y_train, y_val = train_test_split(XX, yy, test_size=val_size, shuffle=shuffle)
  keys = ['X_train', 'X_val', 'X_test', 'y_train', 'y_val', 'y_test']
  values = [X_train, X_val, X_test, y_train, y_val, y_test]
  return dict(zip(keys, values))
