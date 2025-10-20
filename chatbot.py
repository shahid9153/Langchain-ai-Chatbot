from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

#Loading environment variables
load_dotenv()

#Getting your Gemini API key
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
api_key = os.getenv("GOOGLE_API_KEY")

#Initialize the Gemini chat model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

#Simple console chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chat ended.")
        break
    
    # Send user input to Gemini model
    result = model.invoke(user_input)
    
    # Print model response
    print("AI:", result.content)
