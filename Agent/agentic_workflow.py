from prompt_lib.prompt import system_prompt
from langgraph.graph import StateGraph,START,END,MessagesState
from langgraph.prebuilt import ToolNode,tools_condition
from utils.model_loader  import ModelLoader
from Tools.calculate import Expense
from Tools.currency_conversion_tool import CurrencyExchange
from Tools.place_search_tool import SearchingTool
from Tools.weather_info import WeatherTool





class GraphBuilder:

    def __init__(self,model_provider: str ="openai"):
        self.model_loder=ModelLoader(model_provider=model_provider)
        self.llm=self.model_loder.load_llm()
        self.tools=[]
        self.expense=Expense()
        self.currency_exchange=CurrencyExchange()
        self.searching_tool=SearchingTool()
        self.weather=WeatherTool()

        self.tools.extend([
            * self.expense.calculate_setup_tools,
            * self.currency_exchange.currency_convert_setup_tools,
            * self.searching_tool.tavily_setup_tool,
            * self.weather.weather_setup_tools
        ])
        self.llm_with_tools=self.llm.bind_tools(tools=self.tools)

        self.graph=None
    

        self.system_prompt=system_prompt
    def agent_function(self,state:MessagesState):
        """
        Main Agent function
        """
        user_input=state["messages"]
        input_question= state[self.system_prompt] + user_input
        response=self.llm_with_tools.invoke(input_question)
        return {"messages":[response]}
    
    def build_graph(self):

        graph_builder=StateGraph(MessagesState)
        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=self.tools))
        graph_builder.add_node(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph= graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()