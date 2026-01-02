from dotenv import load_dotenv
import os
from utils.weather import WeatherForCast as WeatherAPI
from langchain.tools import tool


class WeatherTool:

    def __init__(self):
        load_dotenv()
        self.api_key=os.environ.get("openweather_map_api_key")
        self.weather_service=WeatherAPI(self.api_key)
        self.weather_setup_tools=self._setup_tool()

    def _setup_tool(self):
        "stup  for all tools for weather forcast"

        def current_wether(city):
            """
            fetch the  current weather for  the city
            """
            weather_data=self.weather_service.cuurent_weather(city)

            if weather_data:
                temp= weather_data.get('main',{}).get('temp','N/A')
                desc=weather_data.get('weather',[{}])[0].get('description','N/A')
                return f'current weather of {city} : {temp} C , {desc}'
            return f"could not find the current temp of {city}"
        
        def weather_forcast(city):
            "weather forcast for the city"

            weather_forcast_data=self.weather_service.forcasting(city)

            if weather_forcast_data and 'list' in weather_forcast_data:
                forcast_list=[]
                for item in weather_forcast_data['list']:
                    date=item['dt_txt'].split('')[0]
                    temp=item['main']['temp']
                    des=item['weather'][0]['description']

                    forcast_list.append(f"{date}: {temp} : deg celcius {des}")
                return f"weather forcast for {city} /n  {forcast_list}"
            return f"weather is not found for the {city}"
        return[current_wether,weather_forcast]
                

        