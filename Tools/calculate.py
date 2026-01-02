from langchain.tools import tolls   
from utils.calculater import CalculateExpese


class Expense:
    def __init__(self):
        self.caculate=CalculateExpese()
        self.calculate_setup_tools=self._setup_tools()

    def _setup_tools(self):
        "setup tools for all expanse tools"

        def estimated_cost_of_hotel(total_days:int,night:int):
            """
            estimated cost of hotels
            """
            return self.caculate.multipy(total_days,night)
        
        def estimated_total_expanse(*cost):
            """
            total estimated cost of the trip
            """
            return self.caculate.calculate_total(*cost)
        
        def estimated_per_day_cost(total_cost:float,per_day:int):
            """
             estimatedd  per day cost of the trip
            """
            return self.caculate.calculate_daily_budget(total_cost,per_day)
        
        return[estimated_cost_of_hotel,estimated_total_expanse,estimated_per_day_cost]
