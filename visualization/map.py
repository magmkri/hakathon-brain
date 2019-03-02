import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

def getPositionCSV(string):
    df = pd.read_csv("NILU_Dataset_Trondheim_2014-2019.csv", index_col=[0], header=[0, 1])
    df.index.name = 'timestamp'
    df.index = pd.to_datetime(df.index)
    return df[string]
# Add data
Bakke = getPositionCSV("Bakke kirke")
Tiller = getPositionCSV("E6-Tiller")
Elgeseter = getPositionCSV("Elgeseter")
Torvet = getPositionCSV("Torvet")
print(Bakke.head())
pos = [Bakke, Tiller, Elgeseter, Torvet]
names = ["Bakke Kirke", "E6-Tiller", "Elgeseter", "Torvet"]

print(list(Torvet.columns.values))


fig = go.Figure()
lay = go.Layout(title="PM10")
x_values = Bakke.index
for i in range(len(pos)):
    y_values = pos[i].NO
    fig.add_scatter(
        x=x_values,
        y=y_values,
        name=names[i]
    )

py.plot(fig)
