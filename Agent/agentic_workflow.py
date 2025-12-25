from prompt_lib.prompt import system_prompt
from langgraph.graph import StateGraph,START,END,MessagesState
from langgraph.prebuilt import ToolNode,tools_condition
from utils.model_loader  import ModelLoader







class GraphBuilder:

    def __init__(self,model_provider: str ="openai"):
        self.model_loder=ModelLoader(model_provider=model_provider)
        self.llm=self.model_loder.load_llm()

        





        self.system_prompt=system_prompt
    def agent_function(self,state:MessagesState):
        """
        Main Agent function
        """
        user_input=state["messages"]
        input_question= state[self.system_prompt] + user_input
        response=self.llm_with_tool.invoke(input_question)
        return {"messages":[response]}
    
    def build_graph(self):

        graph_builder=StateGraph(MessagesState)
        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=tools))
        graph_builder.add_node(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools",agent)
        graph_builder.add_edge("agent",END)
        self.graph= graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()