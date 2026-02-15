#help me with the python code connecting to google model
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

# Configure API key
#genai.configure(api_key="AIzaSyDr9IkWhp2Rh0p9My5NHyUWYdCp-x9Ze6o")

genai.configure()

# Select model
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate content
response = model.generate_content("Explain sap in 1 line")

print(response.text)
