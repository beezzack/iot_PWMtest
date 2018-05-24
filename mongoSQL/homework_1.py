from bokeh.io import curdoc
from bokeh.models import ColumnDataSource,CDSView, BooleanFilter
from bokeh.plotting import Figure
import Adafruit_DHT
import threading

sensor = Adafruit_DHT.DHT11
GPIO = 2
humidity = 0
temperature = 0

source = ColumnDataSource(data = dict(x=[], temp=[]))
booleans = [True if temp_val > 30 else False for temp_val in source.data['temp']]
view = CDSView(source=source, filters = [BooleanFilter(booleans)])

fig = Figure(width=1000, height=800)
ct = 0
fig.line(source=source, x='x', y='temp', line_width=2, alpha = .85, color='blue')
fig.circle(source = source, x='x', y = 'temp',size = 10, color = 'blue')
fig.circle(source = source, x='x', y = 'temp',size = 10, color = 'red', view = view)

fig.xaxis.axis_label = "Millionsecon"
fig.yaxis.axis_label = "。C"

def getTemp():
    global temperature,humidity
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, GPIO)

def update_data():
    global ct, temperature
    ct += 1
    new_data = dict(x=[ct], temp=[temperature])
    source.stream(new_data, 10)

threading.Thread(target = getTemp).start()
curdoc().add_root(fig)
curdoc().add_periodic_callback(update_data, 500)
