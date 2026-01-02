from dotenv import load_dotenv
from langchain.tools import tool
from utils.currency_converter import CurrencyConverter
import os




class CurrencyExchange:


    def __init__(self):
        load_dotenv()
        self.api_key=os.environ.get("exchange_rate_api_key")
        self.currency_exchange_service=CurrencyConverter(self.api_key)
        self.currency_convert_setup_tools=self._setup_tool()

    def _setup_tool(self):

        "setup all tools for currency currency exchange tool"
        @tool
        def currency_rate(amount,from_currency,to_currency):
            """
            convert amount from one currency to another
            """
            return self.currency_exchange_service(amount,from_currency,to_currency)
        return [currency_rate]