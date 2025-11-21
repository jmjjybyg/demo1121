import streamlit as st
import time

st.title("Business Performance Dashboard")
st.write("Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard.")

st.subheader("Quarterly Revenue Overview")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Q1 2024")
    st.write("Revenue: $1.2M")
with col2:
    st.header("Q2 2024")
    st.write("Revenue: $1.5M")
with col3:
    st.header("Q3 2024")
    st.write("Revenue: $1.3M")

tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])
with tab1:
    st.write("### Sales Data")
    sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")
    st.bar_chart({"Revenue (in M$)": [1.2, 1.5, 1.3, 1.6]}, height=200)
with tab2:
    st.write("### Customer Insights")
    customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for feedback in customer_feedback:
        st.write(f"- {feedback}")
with tab3:
    st.write("### Market Trends")
    market_trends = {
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
    }
    for trend, status in market_trends.items():
        st.write(f"{trend}: {status}")
  
with st.expander("More Information"):
    st.write("Data collected via surveys and reports.")

st.subheader("Interactive Revenue Checker")
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
selected_quarter = st.selectbox("Select a quarter:", quarters)

st.write(f"Revenue for {selected_quarter}: {sales_data[selected_quarter]}")

growth = st.slider("Adjust growth percentage:", 0, 50, 10)
base_revenue = float(sales_data[selected_quarter].strip("$M"))
adjusted_revenue = base_revenue * (1 + growth / 100)
st.write(f"Adjusted Revenue for {selected_quarter}: ${adjusted_revenue:.2f}M")

if st.button("Show Motivation"):
    st.success("Keep pushing for growth! 🚀")



