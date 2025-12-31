import requests

class CurrencyConverter:

    def __init__(self,exchange_rate_api_key:str):

      self.base_url= f"https://v6.exchangerate-api.com/v6/{exchange_rate_api_key}/latest"


    def currency_exchange(self,from_currency:str,to_currency:str,amount:float):
       """
       convert the amount from one currency to other currency
       """

       url=f"{self.base_url}/{from_currency}"

       response=requests.get(url=url)
       if response.status_code !=200:
          raise Exception("Api is not hited",response.json())
       rate=response.json()["conversion_rate"]
       if to_currency  not in rate :
          raise ValueError(f"{to_currency} not found in exchange rate")
       return amount* rate[to_currency]



