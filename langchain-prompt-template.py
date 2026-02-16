from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template= "Tell me the key achievements of {name} in 1 line",
    input_variables=["name"]
)

llm = ChatOllama(
    model ="phi4-mini:latest" 
)

chain =prompt | llm    #LCEL

username =  input("whose achievements you would like to know?")


response =chain.invoke({"name":username})

#response =llm.invoke(prompt.format(name ="Virat Kohli"))

print(response.content)
