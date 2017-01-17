import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', db='external_cities_example')
cur = conn.cursor()

qs = 'SELECT * from `city`'
row_count = cur.execute(qs)

print('rows: {}'.format(row_count))
data = cur.fetchall()
print(data)
