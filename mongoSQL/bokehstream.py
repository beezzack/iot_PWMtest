from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import Figure
import Adafruit_DHT
import threading

sensor = Adafruit_DHT.DHT11
GPIO = 2

source = ColumnDataSource(dict(x=[], humi=[], temp=[]))

fig = Figure(width=1000, height=800)
fig.line(source=source, x='x', y='humi', line_width=2, alpha = .85, color='blue')
fig.line(source=source, x='x', y='temp', line_width=2, alpha = .85, color='red')
fig.xaxis.axis_label = "Millionsecon"
fig.yaxis.axis_label = "。C/RH"
ct = 0
humidity = 0
temperature = 0

def getTempAndHumi():
    global humidity, temperature
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(seneor, GPIO)

def update_data():
    global ct, humidity, temperature
    ct += 1
    new_data = dict(x=[ct], humi = [humidity], temp=[temperature])
    source.stream(new_data, 10)

threading.Thread(target = getTempAndHumi).start()
curdoc().add_root(fig)
curdoc().add_periodic_callback(update_data, 500)
