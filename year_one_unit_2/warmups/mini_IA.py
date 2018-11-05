import requests, json

def weather(longitude, latitude):
    api_token = '627815be0f4884397b0ee70d873ab92b'

    url = "https://api.darksky.net/forecast/627815be0f4884397b0ee70d873ab92b/"+str(longitude)+","+str(latitude)


########## call data ###############################################
    data = requests.get(url).json()
    return data

def outputs(data):
    the_latitude=data['latitude']
    print(the_latitude, 'is the latitude of the location the weather is predicted for')
    the_temperature=data['currently']['temperature']
    print(the_temperature, 'in fahrenheit')
    temp_in_celcius=round((the_temperature - 32)*5/9, 2)
    print(temp_in_celcius, 'in celcius')
    chance_of_rain=data['currently']['precipProbability']
    print(chance_of_rain, '% chance of rain')
    summary_of_daily_weather=data['currently']['summary']
    print(summary_of_daily_weather)


    if temp_in_celcius >= 20:
        print('Wear a T-shirt')
    if 20 >= temp_in_celcius >= 12:
        print('Wear a hoodie')
    if 12 >= temp_in_celcius >= 0:
        print('Wear a jacket')
    if 0 >= temp_in_celcius:
        print('Stay home')


data = weather(-72.0034,34.0565)
outputs(data)
