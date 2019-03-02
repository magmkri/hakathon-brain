import plotly.plotly as py
from plotly.grid_objs import Grid, Column
from plotly.tools import FigureFactory as FF
from plotly.offline import plot
import time
from datetime import datetime
import numpy as np
import pandas as pd

def getPositionCSV(string):
    df = pd.read_csv("../NILU_Dataset_Trondheim_2014-2019.csv", index_col=[0], header=[0, 1])
    df.index.name = 'timestamp'
    df.index = pd.to_datetime(df.index)
    return df[string]
# Add data
appl = getPositionCSV("Bakke kirke")
Tiller = getPositionCSV("E6-Tiller")
Elgeseter = getPositionCSV("Elgeseter")
Torvet = getPositionCSV("Torvet")

appl = appl.head(100)
print(appl)
def to_unix_time(dt):
    epoch =  datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

appl_price = list(appl['PM10'])

my_columns = []
for k in range(len(appl.index) - 1):
    my_columns.append(Column(list(appl.index)[:k + 1], 'x{}'.format(k + 1)))
    my_columns.append(Column(appl_price[:k + 1], 'y{}'.format(k + 1)))

grid = Grid(my_columns)
py.grid_ops.upload(grid, 'PM10 values' + str(time.time()), auto_open=False)

data=[dict(type='scatter',
           xsrc=grid.get_column_reference('x1'),
           ysrc= grid.get_column_reference('y1'),
           name='PM10',
           mode='lines',
           line=dict(color= 'rgb(114, 186, 59)'),
           fill='tozeroy',
           fillcolor='rgba(114, 186, 59, 0.5)')]

axis=dict(ticklen=4,
          mirror=True,
          zeroline=False,
          showline=True,
          autorange=False,
          showgrid=False)

layout = dict(title='AAPL Daily Stock Price',
              font=dict(family='Balto'),
              showlegend=False,
              autosize=False,
              width=800,
              height=400,
              xaxis=dict(axis, **{'nticks':12, 'tickangle':-45,
                                  'range': [to_unix_time(datetime(2013, 12, 31, 23)),
                                            to_unix_time(datetime(2014, 1, 5, 2))]}),
              yaxis=dict(axis, **{'title': 'μm', 'range':[0,170]}),
              updatemenus=[dict(type='buttons',
                                showactive=False,
                                y=1,
                                x=1.1,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, dict(frame=dict(duration=50, redraw=False),
                                                               transition=dict(duration=0),
                                                               fromcurrent=True,
                                                               mode='immediate')])])])

frames=[{'data':[{'xsrc': grid.get_column_reference('x{}'.format(k + 1)),
                  'ysrc': grid.get_column_reference('y{}'.format(k + 1))}],
         'traces': [0]
         } for k in range(len(appl.index) - 1)]

fig=dict(data=data, layout=layout, frames=frames)
py.create_animations(fig, 'PM10 Bakke Kirke' + str(time.time()))