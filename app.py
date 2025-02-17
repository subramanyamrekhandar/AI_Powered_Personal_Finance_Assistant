import streamlit as st
import requests
import os
from dotenv import load_dotenv
import groq  # Import Groq API SDK

# Load environment variables
load_dotenv()

# Initialize Groq Client
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = groq.Client(api_key=GROQ_API_KEY)

# Set API key for Financial Modeling Prep (FMP)
FMP_API_KEY = "9oIC7Pv2OyjTcw2QarsR71Ct8D053ced"

# Function to fetch stock data from Financial Modeling Prep API
def get_stock_data(symbol):
    url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={FMP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200 and response.json():
        return response.json()[0]
    return None

# Function to generate AI response using Groq
def get_ai_response(prompt):
    model_name = "llama-3.3-70b-versatile"  # More stable model
    messages = [{"role": "user", "content": prompt}]

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            stream=False  # Using non-streaming for reliability
        )
        return response.choices[0].message.content if response.choices else "No response received."
    except Exception as exc:
        return f"❌ Error: {exc}"

# Streamlit UI
st.set_page_config(page_title="AI Financial Assistant", page_icon="💰", layout="centered")

# Sidebar Navigation
st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Home", "AI Assistant"])
page = st.sidebar.selectbox('Select a page:', 
                               ['Home', 'AI Assistant'])

if page == "Home":
    
    st.title("Welcome to AI Financial Assistant 💰")
    st.write("This tool helps you with stock market insights and financial advice.")
    st.write("Navigate to 'AI Assistant' to get started.")
    st.markdown("---")
    st.write("Developed by **Subramanyam Rekhandar**")
    st.image("banner.jpeg", use_container_width=True)  # Add banner image

elif page == "AI Assistant":
    st.title("💰 AI Financial Assistant")
    st.write("Ask me about stock prices, market trends, or investment advice!")

    query = st.text_input("Enter a stock symbol (e.g., AAPL) or a financial question:")

    if st.button("Get Insights"):
        if query.upper().isalpha():  # Check if input is a stock symbol
            data = get_stock_data(query.upper())
            if data:
                st.write(f"### {data['name']} ({data['symbol']})")
                st.write(f"📈 Price: ${data['price']}")
                st.write(f"📊 Change: {data['change']} ({data['changesPercentage']}%)")
            else:
                st.write("⚠️ Stock data not found. Try a different symbol.")
        else:  # Treat input as a general finance query
            with st.spinner("💬 Thinking..."):
                response = get_ai_response(query)
            st.write(response)

    st.markdown("---")
    st.write("🔍 Data sourced from Financial Modeling Prep & Groq AI.")
