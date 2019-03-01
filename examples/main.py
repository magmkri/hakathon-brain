from examples.process import *
from examples.GBM import *


config = {
  'pred_var': 'Torvet PM10', # Must include station and pollutants name (column name)
  'stations': ['Torvet'], # Stations to use in feature extraction
  'window': 6,
}


processed_data = preprocess()

train(config, processed_data)
print(processed_data)

result = predict(config, processed_data)
print(result[2])
