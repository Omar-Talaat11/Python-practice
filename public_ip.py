import requests

def get_ip():
    url ='https://api.ipify.org/?format=json'
    response_json =requests.get(url).json()
    return (response_json['ip'])
    

def get_loc(ip):
    url=f'https://ipinfo.io/{ip}/geo'
    response_json =requests.get(url).json()
    return (response_json)
    



print(f'you public id is {get_ip()}')
x= input('please enter 1 if you want to also get your location or 0 if not\n')

if x=='1':
    loc=get_loc(get_ip())
    country=loc['country']
    city = loc['city']
    time_zone =loc['timezone']
    coords=loc['loc']
    print(f'Your country is {country} and your city is {city}')
    print(f'Your timezone is {time_zone}')
    print(f'Your exact coordinates are {coords}')