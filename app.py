import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()



# LangSmith tracking (optional)
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with OpenAI"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "question: {question}")
    ]
)

# Streamlit UI
st.title("Enhanced Q&A Chatbot with OpenAI")


api_key = os.getenv("ROUTER_API_KEY")
# Sidebar
st.sidebar.title("Settings")
# api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
selected_model = st.sidebar.selectbox("Select an OpenAI Model", ["openai/gpt-4o-mini","gpt-4o", "openai/gpt-3.5-turbo-0613","openai/gpt-4.1"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=1000, value=500)

# User input
st.write("Go ahead and ask any question")
user_input = st.text_input("Enter you query here")

# Response generation
def generate_response(question, model, temperature, max_tokens):
    llm = ChatOpenAI(
        model=model,
        openai_api_key= api_key,
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=temperature,
        max_tokens=max_tokens
    )
    parser = StrOutputParser()
    chain = prompt | llm | parser
    return chain.invoke({"question": question})

# Show result
if user_input:
    response = generate_response(user_input,selected_model, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide a query.")
