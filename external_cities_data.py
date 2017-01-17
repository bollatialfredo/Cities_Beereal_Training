import pymysql
MAX_POPULATION = 1000000

class CitiesData(object):

    def all():

        conn = pymysql.connect(host='localhost', user='root', password='', db='external_cities_example')
        cur = conn.cursor()

        qs = 'SELECT * FROM `City` WHERE `population` > ' + str(MAX_POPULATION)
        cur.execute(qs)
        data = cur.fetchall()

        return data


# print('cities retrieved: {}'.format(row_count))
# print(data)
