# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:50:16 2018

@author: jimmybow
"""

from dash import Dash#, html, dcc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import visdcc

app = Dash(__name__)

app.layout = html.Div([
      visdcc.Network(id = 'net',
                     options = dict(height= '600px', width= '100%')),
      dcc.Input(id = 'label',
                placeholder = 'Enter a scale ...',
                type = 'text',
                value = ''  ),
      dcc.Input(id = 'labelx',
                placeholder = 'Enter x position ...',
                type = 'text',
                value = ''  ),
      dcc.Input(id = 'labely',
                placeholder = 'Enter y position ...',
                type = 'text',
                value = ''  ),
      dcc.Input(id = 'node',
                placeholder = 'Enter node id ...',
                type = 'text',
                value = ''  )
])

@app.callback(
    Output('net', 'moveTo'),
    [Input('label', 'value'),
     Input('labelx', 'value'),
     Input('labely', 'value')])
def myfun(z, x, y):
    if z == '': z = 1
    if x == '': x = 1
    if y == '': y = 1
    return {'position': {'x': int(x), 'y': int(y)}, 'scale': int(z)}

@app.callback(
    Output('net', 'fit'),
    [Input('node', 'value')])
def myfun(x):
    if x == '': return {'Is_used': False}
    else: return {'nodes': [x], 'animation': True}

if __name__ == '__main__':
    app.run_server(debug=True)