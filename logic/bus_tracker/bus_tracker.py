import requests
from datetime import datetime, timedelta
from pymysql import connect
import time

url = 'http://apis.data.go.kr/1613000/BusLcInfoInqireService/getRouteAcctoBusLcList?serviceKey={key}&pageNo=1&numOfRows=100&_type=json&cityCode=38080&routeId={line_id}'
key = 'JYTc85AfEjOQLSqYvU4HB9tRgdy%2BiL1gZjJ0yuo9phMmyvotaPHrrghXzLfCEOLcTTR8WxvVPolqaxmWKX89aA%3D%3D'
station = ['MYB2', 'MYB3']


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
                line_id = item['routenm']
                print(datetime.now(), lat, lon, station_id, station_name, station_order, line_id, bus_number)

        time.sleep(60)
