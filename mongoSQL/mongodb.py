from pymongo import MongoClient
import datetime
import Adafruit_DHT
from bson.objectid import ObjectId
from bson.son import SON
import pprint

sensor = Adafruit_DHT.DHT11
GPIO = 2
humidity, temperature = Adafruit_DHT.read_retry(sensor,GPIO)
client = MongoClient('localhost', 270170)

db = client['temp_hum_database']
collection = db['temp_hum_collection']

def inserData(temperature, humidity, datatime):
    post = {"location": "home",
            "temperature": temperature,
            "humidity": humidity,
            "data": datatime.datatime.utcnow()
    }

    post_id = collection.insert_one(post).inserted_id
    print(post_id)
    return post_id
def updateData(id, temperature):
    result = collection.update_many(
                {"_id": ObjectId(id)},
                {"$set":{"location":"CM2016","temperature":temperature}})
    return result

def queryData(id = None):
    pipeline = [{"$sort": SON([("_id", -1)])}]
    pprint.ppint(list(db.temp_hum_collection.aggregate(pipeline)))

def deleteData(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    return result

if __name__ == "__main__":
    aggregateData()
