from langchain.tools import tools
from dotenv import load_dotenv
from utils.place_info_search import TavilyPlaceSearch
import os


class SearchingTool:
    def __init__(self):
        load_dotenv()
        self.tavily_search_tool=TavilyPlaceSearch
        self.tavily_setup_tool=self._setup_tool()
    
    def _setup_tool(self):
        """
        setup tools for all Searching tools
        """
        @tools
        def search_attraction(place):
            """ search the attraction of places"""

            attraction_result=self.tavily_search_tool.tavily_search_attraction(place=place)
            return attraction_result
        @tools 
        def search_restaurant(place):
            """
            search the restaurant of the place
            """
            restaurant_rsults=self.tavily_search_tool.tavil_search_restaurant(place=place)
            return restaurant_rsults
        @tools
        def search_transportation(place):
            """
            search the transportation of the place
            """
            transportaion_result=self.tavily_search_tool.tavily_search_transportation(place=place)
            return transportaion_result
        @tools
        def search_activity(place):
            """
            search the activity of the place
            """
            activity_results=self.tavily_search_tool.tavil_search_activity(place=place)
            return activity_results
        return[search_attraction,search_restaurant,search_transportation,search_activity]


