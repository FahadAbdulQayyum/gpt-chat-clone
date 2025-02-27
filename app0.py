import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time  

# Load environment variables
load_dotenv()
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Create dummy sales data
data = {
    "date": pd.date_range(start="2023-01-01", periods=12, freq="M"),
    "revenue": [1000, 1200, 1500, 1400, 1800, 1600, 2000, 2200, 2100, 2300, 2500, 2700]
}
df = pd.DataFrame(data)

# Streamlit UI
st.title("📊 Sales Data Visualization & AI Insights")

# Plot the sales trend
st.write("### Sales Trend Over Time")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=df["date"], y=df["revenue"], marker="o", ax=ax)
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
st.pyplot(fig)

# AI Analysis
st.write("### AI-Generated Insights")

# Show loading effect before displaying AI response
with st.spinner("🔄 Analyzing data..."):
    time.sleep(2)  # Simulate processing time
    prompt = "Analyze this sales trend graph. Identify trends, anomalies, and predict future revenue growth."
    response = model.generate_content(prompt)
    insight = response.text if response.text else "AI couldn't generate insights."

st.write(insight)
