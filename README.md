# AI Financial Assistant

## Overview
This AI-powered financial assistant allows users to retrieve real-time stock data and get AI-generated financial insights. It integrates the **Financial Modeling Prep API** for stock market data and **Groq's LLaMA model** for AI-based financial responses.

## Features
- 📈 Fetch real-time stock prices using **Financial Modeling Prep API**
- 🤖 Get AI-generated financial insights via **Groq AI**
- 🏦 Analyze market trends, investment strategies, and financial questions
- 🚀 Built using **Streamlit** for an interactive UI

## Technologies Used
- **Python** 🐍
- **Streamlit** 📊
- **Groq API** 🤖
- **Financial Modeling Prep API** 💹
- **Dotenv** for environment variable management

## Installation
### Prerequisites
Ensure you have Python installed (preferably 3.8+). Install required dependencies using:

```sh
pip install streamlit requests python-dotenv groq
```

## Environment Variables
Create a `.env` file in the project root and add the following:

```
GROQ_API_KEY=your_groq_api_key
FMP_API_KEY=your_fmp_api_key
```

Replace `your_groq_api_key` and `your_fmp_api_key` with your actual API keys.

## Usage
Run the Streamlit app with:

```sh
streamlit run app.py
```

## How It Works
1. **Enter a stock symbol** (e.g., AAPL) to fetch real-time stock data.
2. **Ask financial questions** (e.g., "Suggest a savings plan based on my ₹50,000 monthly income.")
3. **Receive AI-generated insights** for investment, savings, and financial planning.

## Sample Questions for Testing
### Stock Data Queries:
- "AAPL" (Fetch Apple Inc. stock data)
- "TSLA" (Fetch Tesla stock data)
- "GOOGL" (Fetch Alphabet stock data)

### Financial Advice Queries:
- "What are the best investment strategies for 2024?"
- "How to diversify my stock portfolio?"
- "Suggest a savings plan based on my ₹50,000 monthly income."
- "What are some good ETFs to invest in?"
- "Explain the difference between mutual funds and index funds."

## API References
- **Financial Modeling Prep API**: [https://financialmodelingprep.com/developer/docs/](https://financialmodelingprep.com/developer/docs/)
- **Groq AI API**: [https://groq.com/](https://groq.com/)

## Contributing
Pull requests are welcome! Open an issue for feature requests or bug reports.

## License
This project is licensed under the MIT License.

---

🚀 **Get Started & Make Smarter Financial Decisions!**

