from pymongo import MongoClient

class CitiesDataInter():

    def __init__(self):
        client = MongoClient()
        db = client.city

    def add(self, cities):
