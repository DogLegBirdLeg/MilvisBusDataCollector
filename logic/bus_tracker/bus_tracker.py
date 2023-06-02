import requests
from datetime import datetime, timedelta
from pymysql import connect
from config import mysql
import time

url = 'http://apis.data.go.kr/1613000/BusLcInfoInqireService/getRouteAcctoBusLcList?serviceKey={key}&pageNo=1&numOfRows=100&_type=json&cityCode=38080&routeId={line_id}'
key = 'JYTc85AfEjOQLSqYvU4HB9tRgdy%2BiL1gZjJ0yuo9phMmyvotaPHrrghXzLfCEOLcTTR8WxvVPolqaxmWKX89aA%3D%3D'
station = ['MYB2', 'MYB3']


def get_connection():
    return connect(host=mysql.host, port=mysql.port, user=mysql.user, password=mysql.passwd, db=mysql.db, charset='utf8')


def tracking_bus(bus_number, line_id):
    request_url = url.format(key=key, line_id=line_id)

    timeout = datetime.now() + timedelta(hours=1)
    while datetime.now() <= timeout:
        res = requests.get(request_url)
        json = res.json()
        items = json['response']['body']['items']
        if items == "":
            continue

        items = items['item']
        if isinstance(items, dict):
            items = [items]

        for item in items:
            if bus_number == item['vehicleno']:
                lat = item['gpslati']
                lon = item['gpslong']
                station_id = item['nodeid']
                station_name = item['nodenm']
                station_order = item['nodeord']

                db = get_connection()
                cursor = db.cursor()

                sql = f'''
                INSERT INTO bus_position(line_id, station_id, station_name, latitude, longitude, order_number, datetime)
                VALUE("{line_id}", "{station_id}", "{station_name}", {lat}, {lon}, {station_order}, "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                '''

                cursor.execute(sql)
                db.commit()
                db.close()

        time.sleep(60)
