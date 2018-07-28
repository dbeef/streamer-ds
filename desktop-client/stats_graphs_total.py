# based on:
# https://plot.ly/python/line-charts/
import numpy as np
import plotly

frames = 500

plotly.tools.set_credentials_file(username='x', api_key='x')

packet_times = np.fromfile("packet_times")
decompress_times = np.fromfile("decompress_times")
screenshot_times = np.fromfile("screenshot_times")

import plotly.plotly as py
import plotly.graph_objs as go

y_temp = []
for i in range(0, frames):
    value = packet_times[i] + decompress_times[i] + screenshot_times[i]
    y_temp.append(value)

labels = ['Total frame time']

colors = ['rgb(0,255,0)']

mode_size = [8, 8, 12, 8]
line_size = [2, 2, 4, 2]

y_data = [packet_times[0:frames]]

x_temp = []
for i in range(0, frames):
    x_temp.append(i)

x_data = [x_temp]

traces = []

for i in range(0, 1):
    traces.append(go.Scatter(
        x=x_data[i],
        y=y_data[i],
        mode='lines',
        line=dict(color=colors[i], width=line_size[i]),
        connectgaps=True,
    ))

    traces.append(go.Scatter(
        x=[x_data[i][0], x_data[i][11]],
        y=[y_data[i][0], y_data[i][11]],
        mode='markers',
        marker=dict(color=colors[i], size=mode_size[i])
    ))

layout = go.Layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickcolor='rgb(204, 204, 204)',
        tickwidth=2,
        ticklen=5,
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    autosize=False,
    width=10000,
    height=800,
    # margin=dict(
    #     autoexpand=False,
    #     l=100,
    #     r=20,
    #     t=110,
    # ),
    showlegend=False
)

annotations = []

# Adding labels
for y_trace, label, color in zip(y_data, labels, colors):
    # labeling the left_side of the plot
    annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                            xanchor='right', yanchor='middle',
                            text=label,
                            font=dict(family='Arial',
                                      size=16),
                            showarrow=False))
    # labeling the right_side of the plot
    annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
                            xanchor='left', yanchor='middle',
                            text='',
                            font=dict(family='Arial',
                                      size=16),
                            showarrow=False))
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                        xanchor='left', yanchor='bottom',
                        text='Frame processing time on sample of ' + str(frames) + ' frames',
                        font=dict(family='Arial',
                                  size=30,
                                  color='rgb(37,37,37)'),
                        showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                        xanchor='center', yanchor='top',
                        text='Source: me',
                        font=dict(family='Arial',
                                  size=12,
                                  color='rgb(150,150,150)'),
                        showarrow=False))


layout['annotations'] = annotations

fig = go.Figure(data=traces, layout=layout)
py.plot(fig, filename='stats_time_total')
