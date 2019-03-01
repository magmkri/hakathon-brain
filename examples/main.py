from examples.process import *
from examples.GBM import *
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode, plot


config = {
  'pred_var': 'Bakke kirke PM10', # Must include station and pollutants name (column name)
  'stations': ['Bakke kirke'], # Stations to use in feature extraction
  'window': 6,
  'test_size': 0.3,
  'val_size': 0.1,
  'shuffle': True
}


processed_data = preprocess(config)
train(config, processed_data)

gbm_results, rmse, r2 = predict(config, processed_data)

y_values_predict = []
x_values = []
y_values_true = []
for index, row in gbm_results.iterrows():
  x_values.append(index)
  y_values_predict.append(row["GBM"])
  y_values_true.append(row["True"])

fig = go.Figure()
fig.add_scatter(
  x=x_values,
  y=y_values_predict,
  name= "Predicted"
)

fig.add_scatter(
  x=x_values,
  y=y_values_true,
  name = "True value "
)

plot(fig)
