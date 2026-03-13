import streamlit as st
import pandas as pd
from src.app.database.db import load_products

st.title("Ecommerce Price Dashboard")

df = load_products()

if df.empty:
    st.warning("No data found")
else:

    st.subheader("Product Table")
    st.dataframe(df)

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    st.subheader("Price Comparison by Platform")

    avg_price = df.groupby("platform")["price"].mean()

    st.bar_chart(avg_price)

    st.subheader("Price Distribution")

    st.line_chart(df["price"])

    st.subheader("Average Price by Platform")

    avg_price = df.groupby("platform")["price"].mean()

    st.bar_chart(avg_price)

    st.subheader("Top 10 Most Expensive Products")

    top = df.sort_values("price", ascending=False).head(10)

    st.dataframe(top)