from pymongo import MongoClient
from bson.code import Code

client = MongoClient('localhost', 27017)
db = client['temp_hum_database']
collection = db['temp_hum_collection']

mapfun = Code("""
                function(){
                    emit(this,=.location, this.temperature);
                }
                """)

reducefun = Code("""
                function(key, values){
                    var total = 0
                    for (var i = 0;i<values.lenth; i++){
                        total += values[i];
                    }
                    return total/values.length;
                }
                """)

result = db.temp_hum_collection.map_reduce(mapfun, reducefun, "results")
for doc in result.find():
    print(doc)
