import requests

class CityWeather:
    def __init__(self, name, region, current, feels_like, condition):
        self.city = name
        self.region = region
        self.current = current
        self.feels_like = feels_like
        self.condition = condition
        
    def __str__(self):
        return f"It is currently {self.condition} and {self.current} in {self.city}, {self.region}. It feels like {self.feels_like}."


class CityAstronomy:
    def __init__(self, name, region, sunrise, sunset, moonrise, moonset, moon_phase):
        self.city = name
        self.region = region
        self.sunrise = sunrise
        self.sunset = sunset
        self.moonrise = moonrise
        self.moonset = moonset
        self.moon_phase = moon_phase
        
    def __str__(self):
        return f"City: {self.city}\nSunrise: {self.sunrise}\nSunset: {self.sunset}"


class WeatherAPI:
    base_url = 'http://api.weatherapi.com/v1'
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    # Private method that will set up the request url, make the request, return the response data
    # The __ before the function name is a naming convention for making a private method
    def __get(self, city, api_method):
        request_url = f"{self.base_url}{api_method}?key={self.api_key}&q={city}"
        response = requests.get(request_url)
        if response.ok:
            data = response.json()
            return data
        else:
            return None
        
    # Public method that will call the private method to get the data and create a weather object
    def get_current_weather(self, city):
        # Make the API get request to get back data
        weather_data = self.__get(city, '/current.json')
        # If there is data
        if weather_data:
            # Pull the specific info from the data
            city = weather_data['location']['name']
            region = weather_data['location']['region']
            current_temp = weather_data['current']['temp_f']
            feels_like = weather_data['current']['feelslike_f']
            condition = weather_data['current']['condition']['text']
            # Create a City Object out of that info
            city_obj = CityWeather(city, region, current_temp, feels_like, condition)
            return city_obj
        else:
            print('Something went wrong')
            return None
        
    def get_astronomy(self, city):
        astronomy_data = self.__get(city, '/astronomy.json')
        if astronomy_data:
            city = astronomy_data['location']['name']
            region = astronomy_data['location']['region']
            sunrise = astronomy_data['astronomy']['astro']['sunrise']
            sunset = astronomy_data['astronomy']['astro']['sunset']
            moonrise = astronomy_data['astronomy']['astro']['moonrise']
            moonset = astronomy_data['astronomy']['astro']['moonset']
            moon_phase = astronomy_data['astronomy']['astro']['moon_phase']
            astro_obj = CityAstronomy(city, region, sunrise, sunset, moonrise, moonset, moon_phase)
            return astro_obj
        else:
            print('Something went wrong')
            return None
