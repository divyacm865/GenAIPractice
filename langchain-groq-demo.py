from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
)

response =llm.invoke("Write about easy food list indian after vomit")
print(response.content)