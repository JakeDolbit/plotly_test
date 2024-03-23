import numpy as np
import plotly.graph_objs as go
import dash
from dash import dcc, html, Input, Output, State

# Function to generate sine wave data
def generate_sine_wave(freq):
    x = np.linspace(0, 10, 1000)
    y = np.sin(2 * np.pi * freq * x)
    return x, y

# Standard frequency value
standard_freq = 1.0

# Generate initial sine wave data
x_init, y_init = generate_sine_wave(standard_freq)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Sine Wave with Frequency Slider'),

    dcc.Graph(
        id='sine-wave-graph',
        figure={
            'data': [go.Scatter(x=x_init, y=y_init, mode='lines')],
            'layout': go.Layout(
                title='Sine Wave',
                xaxis={'title': 'Time'},
                yaxis={'title': 'Amplitude'}
            )
        }
    ),

    html.Label('Frequency:'),
    dcc.Slider(
        id='freq-slider',
        min=0.1,
        max=2.0,
        step=0.1,
        value=standard_freq,
        marks={i: str(i) for i in np.arange(0.1, 2.1, 0.1)},
    ),

    html.Button('Reset Frequency', id='reset-button', n_clicks=0),

    html.Div(id='output-container-button', children='')
])

# Callback to update the graph when the frequency slider is changed
@app.callback(
    Output('sine-wave-graph', 'figure'),
    [Input('freq-slider', 'value')]
)
def update_graph(freq):
    x, y = generate_sine_wave(freq)
    return {
        'data': [go.Scatter(x=x, y=y, mode='lines')],
        'layout': go.Layout(
            title='Sine Wave',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Amplitude'}
        )
    }

# Callback to reset the frequency when the reset button is clicked
@app.callback(
    Output('freq-slider', 'value'),
    [Input('reset-button', 'n_clicks')]
)
def reset_frequency(n_clicks):
    # Reset frequency to standard value
    return standard_freq

# Generate standalone HTML file
with open('index.html', 'w') as f:
    f.write(app.index())

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
