import requests

url = 'http://apis.data.go.kr/1613000/BusSttnInfoInqireService/getCrdntPrxmtSttnList?serviceKey={key}&pageNo=1&numOfRows=50&_type=json&gpsLati={lat}&gpsLong={lon}'
key = 'JYTc85AfEjOQLSqYvU4HB9tRgdy%2BiL1gZjJ0yuo9phMmyvotaPHrrghXzLfCEOLcTTR8WxvVPolqaxmWKX89aA%3D%3D'

lat = 35.48403709331703
lon = 128.74843584478066

request_url = url.format(key=key, lon=lon, lat=lat)

res = requests.get(request_url)
json = res.json()

items = json['response']['body']['items']['item']

items = [((lat - item['gpslati']) ** 2 + (lon - item['gpslong']) ** 2) ** (1/2) for item in items]
items.sort()

for item in items:
    print(item)

print(request_url)
print(res.json())