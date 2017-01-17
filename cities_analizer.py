import pymysql
from external_cities_data import CitiesData
import urllib, json
import urllib.request

class Analizer():
    def __init__(self):
        data = CitiesData.all() # gets all the information from de database
        cities_dict = {}
        for city in data:
            cities_dict.update({city[1] : city[4]}) #filters only the city name and the population
        print(cities_dict)

    def api_request(self, city_name):
        url = "https://maps.googleapis.com/maps/api/geocode/json?address="+city_name+"&key=AIzaSyBXfOCtBnfej52I7UrZfCxninpHgo5Pcpk"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data

    def LatAndLongDict(self, dict_):
        aux = dict_['results'].pop()
        return aux['geometry']['location']

runner = Analizer()
req = runner.api_request("Balcarce")
lat_long = runner.LatAndLongDict(req)

# print(req['results'])
