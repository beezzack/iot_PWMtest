from pymongo import MongoClient
import datetime
import Adafruit_DHT
from bson.objectid import ObjectId
from bson.son import SON
import pprint
import time
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource,CDSView, BooleanFilter
from bokeh.plotting import Figure
import threading

sensor = Adafruit_DHT.DHT11
GPIO = 2
humidity, temperature = Adafruit_DHT.read_retry(sensor,GPIO)
ct = 0
client = MongoClient('localhost',27017)
source = ColumnDataSource(data = dict(x=[], temp=[]))
fig = Figure(width=1000, height=800)

db = client['temp_hum_database']
collection = db['temp_hum_collection']
collection.stats

def insertData(temperature, humidity, datatime):
    post = {"location": "home",
            "temperature": temperature,
            "humidity": humidity,
            "data": datetime.datetime.utcnow()}

    post_id = collection.insert_one(post).inserted_id
    print(post_id)
    return post_id

def queryData(id = None):
    for posts in collection.find():
        print(posts)
        update_data(temperature)
        if temperature > 30:
            red()
        else:
            blue()
def red():
    fig.circle(source = source, x='x', y = 'temp',size = 10, color = 'red')

def blue():
    fig.circle(source = source, x='x', y = 'temp',size = 20, color = 'blue')

def update_data(temperature):
    global ct
    ct += 1
    new_data = dict(x=[ct], temp=[temperature])
    source.stream(new_data, 10)

if __name__ == "__main__":
    fig.line(source=source, x='x', y='temp', line_width=2, alpha = .85, color='blue')
    fig.xaxis.axis_label = "Millionsecon"
    fig.yaxis.axis_label = "。C"

    curdoc().add_root(fig)
    curdoc().add_periodic_callback(update_data, 1000)
    while True:
        time.sleep(3)
        now = datetime.datetime.utcnow()
        insertData(temperature,humidity,now)
        queryData();
