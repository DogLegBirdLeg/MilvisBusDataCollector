import requests
from datetime import datetime, timedelta
import time
from logic.bus_finder import producer

url = 'http://apis.data.go.kr/1613000/BusLcInfoInqireService/getRouteAcctoBusLcList?serviceKey={key}&pageNo=1&numOfRows=100&_type=json&cityCode=38080&routeId={line_id}'
key = 'JYTc85AfEjOQLSqYvU4HB9tRgdy%2BiL1gZjJ0yuo9phMmyvotaPHrrghXzLfCEOLcTTR8WxvVPolqaxmWKX89aA%3D%3D'
station = ['MYB2', 'MYB3']


def find_bus(start_point, line_id):
    request_url = url.format(key=key, line_id=line_id)

    timeout = datetime.now() + timedelta(minutes=5)
    while datetime.now() <= timeout:
        res = requests.get(request_url)
        json = res.json()
        items = json['response']['body']['items']
        if items == "":
            continue

        items = items['item']
        if isinstance(items, dict):
            items = [items]

        print(f"=========finding bus...(in {line_id})=============")
        for item in items:
            if item['nodeid'] in station:
                print(f"===========bus find {item['vehicleno']}===========")
                producer.call_producer(item['vehicleno'], line_id)
                return
        time.sleep(60)
