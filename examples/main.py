from examples.process import *
import examples.GBM as gbm
import examples.MLP as mlp
import examples.RF as rf
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode, plot
from concat_csvs import *


config = {
  'pred_var': 'PM10', # Must include station and pollutants name (column name)
  'stations': ['Bakke kirke'], # Stations to use in feature extraction
  'window': 1,
  'test_size': 0.3,
  'val_size': 0.1,
  'shuffle': True
}

filename_benchmark = Path('./andreas_model.joblib')
filename_our = Path('./rai_model.joblib')

andreas_data = preprocess_andreas(config)
our_data = preprocess_ours(config)


#gbm.train(config, andreas_data, filename_benchmark)
#gbm.train(config, our_data, filename_our)
#
#gbm_results_andreas, rmse_andreas, r2_andreas = gbm.predict(config, andreas_data, filename_benchmark)
gbm_results_our, rmse_our, r2_our = gbm.predict(config, our_data, filename_our)

#print(gbm.get_feature_importance(config, processed_data))

#print("RMSE_andreas: " + str(rmse_andreas))
#print("r2_andreas: " + str(r2_andreas))
print("RMSE_rai: " + str(rmse_our))
print("r2_rai: " + str(r2_our))

y_values_predict_andreas = []
y_values_predict_our = []

x_values = []
y_values_true = []
#for index, row in gbm_results_andreas.iterrows():
#  x_values.append(index)
#  y_values_predict_andreas.append(row["GBM"])
#  y_values_true.append(row["True"])

for index, row in gbm_results_our.iterrows():
  x_values.append(index)
  y_values_predict_our.append(row["GBM"])
  y_values_true.append(row["True"])

fig = go.Figure()
y_values_metro = our_data["X_test"]["pm10_concentration"]

#fig.add_scatter(
#  x=x_values,
#  y=y_values_predict_andreas,
#  name= "Predicted benchmark"
#)
#fig.add_scatter(
#  x=x_values,
#  y=y_values_predict_our,
#  name= "Predicted sensorless"
#)
fig.add_scatter(
  x=x_values,
  y=y_values_true,
  name = "True value"
)
fig.add_scatter(
  x=x_values,
  y=y_values_metro,
  name = "Metro value"
)

plot(fig, filename="Metro_prediction")
