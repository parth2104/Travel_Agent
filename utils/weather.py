import requests


class WeatherForCast:

    def __init__(self,api_key):
        
        self.api_key=api_key
        self.base_url="https://api.openweathermap.org/data/2.5"


    def cuurent_weather(self,place):

        """
        Get current weather of Place
        """
        try:
            url=f"{self.base_url}/weather"
            params={
                "q":place,
                "appid":self.api_key
            }
            respond=requests.get(url=url,params=params)
            return respond.json if respond.status_code ==200 else {}
        except Exception as e:
            raise e
    
    def forcasting(self,place):
        """
        Weather forcasting
        """
        try:
            url=f"{self.base_url}/forecast"
            params={
                "q":place,
                "appid": self.api_key,
                "cnt":10,
                "units": "metric"
            }
            respond=requests.get(url=url,params=params)
            return respond.json() if respond.status_code ==200 else {}
        except Exception as e:
            raise e  
        