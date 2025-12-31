class CalculateExpese:

    @staticmethod
    def multipy(a:int,b:int):
        """
         multipy two int 
        
        :param a: Description
        :type a: int
        :param b: Description
        :type b: int
        """
        return a*b
    
    @staticmethod
    def calculate_total(*x:float):
        """
        Docstring for calculate_total
        
        :param x: add  all list of numeber 
    
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total:float,day:int):
        """
        Docstring for calculate_daily_budget
        
        :param total: total cost
        :type total: float
        :param day: number of days
        :type day: int
        """
        return total/day if day>0 else 0