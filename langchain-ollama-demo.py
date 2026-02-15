from langchain_ollama import ChatOllama

llm = ChatOllama(
    model ="phi4-mini:latest",
    
)
response =llm.invoke("Tell me about bengaluru")

print(response.content)
