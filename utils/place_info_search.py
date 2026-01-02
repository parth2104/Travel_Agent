from langchain_tavily import tavily_search
from dotenv import load_dotenv



class TavilyPlaceSearch:
    def __init__(self):
        load_dotenv()
        self.tavily_tools=tavily_search(topic="general",include_answer="advanced")

  

    def tavily_search_attraction(self,place):
        """
        search for the attraction place 
        """
        result=self.tavily_tools.invoke({"query":f"top attractive places in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def taavil_search_restaurant(self,place):
        """ search  the restaurant """
        result=self.tavily_tools.invoke({"query":f"what are the top 10 restaurants and eateries in and around {place}"})
        if isinstance(result,dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def taavil_search_activity(self,place):
        """ search activity near the place """
        result=self.tavily_tools.invoke({"query":f"activities in and around {place}"})
        if isinstance(result,dict)  and  result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_transportation(self,place):
        """ search the transportatin option near the place"""
        result=self.tavily_tools.invoke({"query":f"search the transportation option near the {place}"})
        if isinstance(result,dict)  and result.get("answer"):
            return["answer"]
        return result
    


 