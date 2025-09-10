import requests

# Edit here!
APIKEY = '12f43b161a6442a970b3d13cda7d9bd1'

response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={APIKEY}')

response = requests.get(f'http://api.exchangeratesapi.io/latest?access_key={APIKEY}')

if response.json()['success']:
    print('EURAUD rate is currently', response.json()['rates']['AUD'])
else:
    print('Error:', response.json()['error']['info'])