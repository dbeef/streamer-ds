import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import numpy as np

username = "put_your_plotly_username_here"
api_key = "put_your_plotly_api_key_here"

plotly.tools.set_credentials_file(username=username, api_key=api_key)

packet_times = np.fromfile("packet_times")
decompress_times = np.fromfile("decompress_times")
screenshot_times = np.fromfile("screenshot_times")

# Create a trace
trace = go.Scatter(
    y=screenshot_times
)
data = [trace]
py.plot(data, filename='screenshot_times')

trace = go.Scatter(
    y=decompress_times
)
data = [trace]
py.plot(data, filename='decompress_times')

trace = go.Scatter(
    y=packet_times
)
data = [trace]
py.plot(data, filename='packet_times')

trace = go.Scatter3d(
    x=packet_times,
    y=decompress_times,
    z=screenshot_times,
    showlegend=True
)
data = [trace]
py.plot(data, filename='all_3')
