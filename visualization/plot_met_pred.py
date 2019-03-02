import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

df = pd.read_csv("../data/WeatherPredictionData/Weather_prediction.csv", index_col=[1], header=[0])
df.index.name = 'timestamp'
df.index = pd.to_datetime(df.index)

names = ["no2_concentration","pm25_concentration","pm10_concentration"]

fig = go.Figure()
x_values = df.index
for c in names:
    y_values = df[c]
    print(y_values)
    fig.add_scatter(
        x=x_values,
        y=y_values,
        name=c
    )
plot(fig)



