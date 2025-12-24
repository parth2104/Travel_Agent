from utils.config_loader import load_config
from pydantic import BaseModel,Field
from typing import Literal,Optional,Any
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os



class ConfigLoader:

    def __init__(self):
        print("Loaded config")
        self.config=load_config()
    
    def __getitem__(self,key):
        return self.config[key]
    

class ModelLoader(BaseModel):
    model_provider:Literal["openai","groq"]="openai"
    config:Optional[ConfigLoader] =  Field(default=None,exclude=True)

    def model_post_init(self, __context: Any) :
        self.config = ConfigLoader()
    

    class Config:
         arbitrary_types_allowed=True
        
    def load_llm(self):

            """
            load and return the llm model
            """
            print(f"loading model from provider {self.model_provider}")
            if self.model_provider == "openai":
                 print("Loading LLM model..") 
                 openai_api_key=os.getenv("openai_api_key")
                 openai_api_base=os.getenv("endpoint")
                 model_name=self.config["llm"]["openai"]["model_name"]
                 llm=ChatOpenAI(model=model_name,api_key=openai_api_key,openai_api_base=openai_api_base)
            elif self.model_provider == "groq":
                 print("Loading LLM model")
                 groq_api_key=os.getenv("groq_api_key")
                 model_name=self.config["llm"]["groq"]["model_name"]
                 llm=ChatGroq(model=model_name,api_key=groq_api_key)
            
            return llm

