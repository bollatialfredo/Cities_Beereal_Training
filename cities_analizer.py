from external_cities_data import CitiesDataExt
from internal_cities_data import CitiesDataInter
import json
import urllib.request

KEY_API = "AIzaSyBXfOCtBnfej52I7UrZfCxninpHgo5Pcpk"

class Analyzer():

    def get_external_data(self):
        data = CitiesDataExt.all() # gets all the information from de database
        cities_dict = {}
        for city in data:
            if " " in city[1]:
                cities_dict.update({city[1].replace(" ", "") : {'Population':city[4]}})#replace spaces
            else:
                cities_dict.update({city[1] : {'Population' :city[4]}}) #filters only the city name and the population
        return cities_dict

    def api_request(self, city_name):
        url = "https://maps.googleapis.com/maps/api/geocode/json?address="+city_name+"&key="+KEY_API
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data

    def lat_and_long_dict(self, dict_):
        aux = dict_['results'].pop()
        return aux['geometry']['location']

    def analize(self):
        ext_data = self.get_external_data()
        list_city = ext_data.keys()
        for city in list_city:
            request = self.api_request(city)
            lat_long = self.lat_and_long_dict(request)
            ext_data[city]['lat'] = lat_long['lat']
            ext_data[city]['lng'] = lat_long['lng']

        return ext_data

if __name__ == '__main__':
    runner = Analyzer()
    print(runner.analize())
    # saver = CitiesDataInter()



# req = runner.api_request("newyork")
# lat_long = runner.lat_and_long_dict(req)
# print(lat_long)
