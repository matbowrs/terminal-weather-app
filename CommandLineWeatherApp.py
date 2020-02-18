
import requests
import json
import datetime


# input starts as 'y' so it can loop while user wants to input
# new values
newValue = 'y'

while newValue == 'y' :
    zipCode = input('Enter a US zip code: ')

    # Send request to API with user inputted zip code
    api_request = 'http://api.openweathermap.org/data/2.5/weather?zip='+zipCode+',us&appid=13a48991a81e7847db265b9cd773ae18'
    response = requests.get(api_request)
    # Turn response into JSON object
    json_data = response.json()

    # Parse JSON
    try:
        name = json_data['name']
        tempKelvin = json_data['main']['temp']

        # Formatted AND converted from tempKelvin at the same time
        tempFahrenheit ='{0:.3g}'.format( (tempKelvin - 273.15) * (9/5) + 32 )
        atmosphericPressure = json_data['main']['pressure'] 
        windSpeed = json_data['wind']['speed']
        weatherMain = json_data['weather'][0]['main']
        timeOfReport = datetime.datetime.now().strftime('%c')
        # Output
        print('\nName: {:>25}'.format(name))
        print('Current Temperature: {:>8} degrees Fahrenheit'.format(tempFahrenheit))
        print('Atmospheric Pressure: {:>7} hPa'.format(atmosphericPressure))
        print('Wind Speed: {:>16} mph'.format(windSpeed))
        print('Weather Description: {:>8}'.format(weatherMain))
        print('Time of Report: {:>33}'.format(timeOfReport))
        newValue = input('Search for a new zip code? [y/n] ')
    
    # Catch possible KeyError if 'name' cannot be parsed from JSON, i.e. zip code does not exist
    except KeyError as err:
        print('Error! Zip code not recognized.')
        