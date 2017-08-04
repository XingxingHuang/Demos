from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.examples    # creat database "examples" if not exist

db.cities.insert_one({"name" : "Chicago"})  # insert a dict to table "cities"
print db.cities.find_one() # note each dict has an id No.


tesla_s = {
    "manufacturer": "Tesla Motors",
    "class": "full-size",
    "body style" : "5-door liftback",
    "production":[2012,2013],
    "model years" : [2013],
    "layout" : ["Rear-motor", "rear-wheel drive"],
    "designer" : {
        "firstname" : "Franz",
        "surname" : "von Holzhausen"
    }
}

car = {
    "layout" : "rear mid-engine rear-wheel-drive layout",
    "name" : "Porsche Boxster",
    "productionYears" : [ ],
    "modelYears" : [ ],
    "bodyStyle" : "roadster",
    "assembly" : [
        "Finland",
        "Germany",
        "Stuttgart",
        "Uusikaupunki"
    ],
    "class" : "sports car",
    "manufacturer" : "Porsche"
}

db.autos.insert_one(tesla_s)  # insert a dict to table "autos"
db.autos.insert_one(car)  


def find():
    autos = db.autos.find({"manufacturer" : "Toyota"})
    for a in autos:
        pprint.pprint(a)
        
if __name__ == '__main__':
    find()