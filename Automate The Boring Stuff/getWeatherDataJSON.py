#! python3
# This program uses API from OpenWeather.org formatted as JSON data to show the weather details
import json, sys, logging, pprint, time
from ModuleImporter import module_importer
pyip = module_importer('pyinputplus', 'pyinputplus')
requests = module_importer('requests', 'requests')

# filename = 'weatherData.log'
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s', 
                    datefmt = '%d/%m/%Y - %I:%M:%S %p', filemode = 'w')
logging.disable(logging.CRITICAL)

def timezone(sec: int) -> str:
    '''Return a given timezone in seconds in a formatted string'''
    hours = sec / 3600
    minutes = (hours - int(hours)) * 60
    return "%+d:%.2d hour(s)" % (hours, minutes)

def printDegree(value: int or float) -> str:
    '''Return a degree sign at the end of the given value'''
    return str(value) + u"\N{DEGREE SIGN}"

def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: getWeatherDataJSON.py <city_name>, <2-letter country code>')
    # Get location from command line 
    app_id = pyip.inputPassword(prompt = 'Enter your APP ID: ', blank = True);                           logging.info(f"API KEY Entered: {app_id != ''}")
    if not app_id:
        sys.exit('Unable to request OpenWeather server without an API key')
    location = ' '.join(sys.argv[1:]);                                                                   logging.info(f"{location = }")

    # Download the json data from the website
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={app_id}';   logging.debug(f"{url = }")
    try:
        response = requests.get(url);                                                                    logging.critical(f"{response.status_code = }")
        response.raise_for_status()
    except Exception as err:
        sys.exit(str(err))
    
    # Format and read the json data
    weather_data = json.loads(response.text);                                                            logging.debug(f"Weather Data received:\n{pprint.pformat(weather_data)}")
    print(f"\nDisplaying current weather data for {weather_data['name']} (Lat:{printDegree(weather_data['coord']['lat'])} Long:{printDegree(weather_data['coord']['lon'])})")
    print(f"Timezone: {timezone(weather_data['timezone'])}")
    print(f"Date: {time.ctime(weather_data['dt'])}")

    print(f"Sunrise: {time.ctime(weather_data['sys']['sunrise'])}, Sunset: {time.ctime(weather_data['sys']['sunset'])}")
    print(f"Cloudiness: {weather_data['clouds']['all']}%, Visibility: {weather_data['visibility']} metre")

    print(f"Temperature: Feels like: {printDegree(weather_data['main']['feels_like'])}C, "
    f"Humidity: {weather_data['main']['humidity']}%, Pressure: {weather_data['main']['pressure']} hPa, "
    f"Temp: {printDegree(weather_data['main']['temp'])}C (Max {printDegree(weather_data['main']['temp_max'])}C, Min {printDegree(weather_data['main']['temp_min'])}C)")

    print(f"Overall weather condition is {weather_data['weather'][0]['description']}")
    print(f"Wind: Blowing at {printDegree(weather_data['wind']['deg'])}, with speed {weather_data['wind']['speed']} meter/s")


if __name__ == '__main__':
    main()
