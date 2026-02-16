from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


prompt  = ChatPromptTemplate.from_messages([
   ("system", "You are a helpful AI assistant that provides information about the achievements of famous personalities."),
   ("human", "Tell me the key achievements of {name} in 3 bullet points."),
])


llm = ChatOllama(
    model ="phi4-mini:latest" 
)

chain =prompt | llm    #LCEL

username =  input("whose achievements you would like to know?")


response =chain.invoke({"name":username})

#response =llm.invoke(prompt.format(name ="Virat Kohli"))

print(response.content)
