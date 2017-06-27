import requests
from pprint import pprint

url = 'http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'

response = requests.get(url)

data = response.json()

# pprint(data)
'''
+ aus der JSON response die temp ausgeben
'''
print(data['main']['temp'] - 273.15)

'''
{'base': 'stations',
 'clouds': {'all': 90},
 'cod': 200,
 'coord': {'lat': 51.51, 'lon': -0.13},
 'dt': 1485789600,
 'id': 2643743,
 'main': {'humidity': 81,
          'pressure': 1012,
          'temp': 280.32,
          'temp_max': 281.15,
          'temp_min': 279.15},
 'name': 'London',
 'sys': {'country': 'GB',
         'id': 5091,
         'message': 0.0103,
         'sunrise': 1485762037,
         'sunset': 1485794875,
         'type': 1},
 'visibility': 10000,
 'weather': [{'description': 'light intensity drizzle',
              'icon': '09d',
              'id': 300,
              'main': 'Drizzle'}],
 'wind': {'deg': 80, 'speed': 4.1}}

'''