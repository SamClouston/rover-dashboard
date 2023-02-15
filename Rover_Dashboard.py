# the aim of this code is to input two sets of coords and animate a point traveling from one to another

#imports
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import datetime

#mapbox token to insert maps
mapbox_token = 'pk.eyJ1IjoiYm93bG9mcGFzdGEiLCJhIjoiY2xhZzY5ZDlkMHZwazNvbnVhZnFmdHB3MCJ9.pVbukiheiGZP0_71ZSTdyg'

#create app
app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
app.layout = html.Div(children=[
    html.H1(children="Map for tracking a point across greytown",
            style={'padding-bottom':'10px','padding-left':'10px'}),
    html.P(children="This is a map that shows the animation of a point moving across the main road of greytown",
           style={'padding-bottom':'5px','padding-left':'20px'}),
    dcc.Graph(id='graph', config={'displayModeBar': False, 'scrollZoom': True},
                style={'padding-top':'4px', 'padding-bottom':'2px','padding-left':'2px','height':'100vh'}), #wont redraw points, does detect change in file
    dcc.Interval(id='interval-component', interval=500, n_intervals=0) #500 millisecond interval
])
@app.callback(Output('graph', 'figure'),
              Input('interval-component', 'n_intervals'))

def update_figure(interval):
    #read csv file
    file = pd.read_csv("F:\Program Files (x86)\Research Practice\Tracking.csv")

    locations = [go.Scattermapbox(
                    lat=file['latitude'],
                    lon=file['longitude'],
                    mode='markers',
                    marker={'color' : 'Black'},
                    hoverinfo='text',
                    hovertext="%s\n Last updated: %s" %(file['hover text'], datetime.datetime.now())
    )]

    # Return figure
    return {
        'data': locations,
        'layout': go.Layout(
            uirevision='foo',  # preserves state of figure/map after callback activated
            clickmode='event+select',
            hovermode='closest',
            hoverdistance=2,
            mapbox=dict(
                accesstoken=mapbox_token,
                bearing=25,
                style='light',
                center=dict(
                    lat=-41.077935,
                    lon=175.462831
                ),
                pitch=40,
                zoom=11.5
            ),
        )
    }
if __name__ == "__main__":
    app.run_server(debug=True, port=8054)