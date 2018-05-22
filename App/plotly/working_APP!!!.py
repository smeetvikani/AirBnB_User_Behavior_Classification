import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import pickle

with open("pv.pkl",'rb') as picklefile:
    pv=pickle.load(picklefile)



trace1 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'AU')], name='AU')
trace2 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'CA')], name='CA')
trace3 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'DE')], name='DE')
trace4 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'ES')], name='ES')
trace5 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'FR')], name='FR')
trace6 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'GB')], name='GB')
trace7 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'IT')], name='IT')
trace8 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'NDF')], name='NDF')
trace9 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'NL')], name='NL')
trace10 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'PT')], name='PT')
trace11 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'US')], name='US')
trace12 = go.Bar(x=pv.index, y=pv[('secs_elapsed_mean', 'other')], name='other')



app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3, trace4,trace5,trace6,trace7,trace8
            ,trace9,trace10,trace11,trace12],
            'layout':
            go.Layout(title='Order Status by Customer', barmode='stack')
        })
])



if __name__ == '__main__':
    app.run_server(debug=True)
