import pymysql
from config import mysql
from datetime import datetime


def get_connection():
    return pymysql.connect(host=mysql.host, port=mysql.port, user=mysql.user, password=mysql.passwd, db=mysql.db, charset='utf8')


line_id = 'MYB1'
station_id = 'MYB1'
station_name = '밀양역'
lat = 127.35555
lon = 35.123444
station_order = 1
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
sql = f'''
    INSERT INTO bus_position(line_id, station_id, station_name, latitude, longitude, order_number, datetime)
    VALUE("{line_id}", "{station_id}", "{station_name}", {lat}, {lon}, {station_order}, "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    '''

db = get_connection()
db.cursor().execute(sql)
db.commit()
db.close()