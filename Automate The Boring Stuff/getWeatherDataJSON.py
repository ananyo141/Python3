#! python3
# This program uses API from OpenWeather.org formatted as JSON data to show the weather details
import json, requests, sys, pyinputplus as pyip, logging, pprint
logging.basicConfig(filename = 'weatherData.log', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(lineno)d - %(message)s', 
                    datefmt = '%d/%m/%Y - %I:%M:%S %p', filemode = 'w')
# from ModuleImporter import module_importer

def kelvinToCel(kelv_temp: float) -> float:
    '''Takes the temperature in Kelvin and returns the equivalent temperature in celcius'''
    return kelv_temp - 273.15

def main():
    if len(sys.argv) < 2:
        sys.exit('Usage: getWeatherDataJSON.py <city_name>, <2-letter country code>')
    # Get location from command line 
    app_id = pyip.inputPassword(prompt = 'Enter your APP ID: ', blank = True);      logging.info(f"API KEY Entered: {app_id != ''}")
    if not app_id:
        sys.exit('Unable to request OpenWeather server without an API key')
    location = ' '.join(sys.argv[1:]);                                              logging.debug(f"{location = }")

    # Download the json data from the website
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={app_id}';  logging.debug(f"{url = }")
    try:
        response = requests.get(url);                                                logging.debug(f"{response.status_code = }")
        response.raise_for_status()
    except Exception as err:
        sys.exit(str(err))
    
    weather_data = json.loads(response.text);                                        logging.debug(f"Weather Data received:\n{pprint.pformat(weather_data)}")



if __name__ == '__main__':
    main()
