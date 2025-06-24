# import streamlit as st
# from data_loader import get_margin_data

# def display():
#     st.subheader("📉 Rolling Margin - 6 Months")
#     data = get_margin_data()
#     st.line_chart(data.set_index("Month"))












import streamlit as st
import pandas as pd
import altair as alt
from data_loader import get_margin_data

def show_margin():
    st.subheader("📈 Rolling Margin - 6 Months")

    df = get_margin_data()

    chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X("Month", sort=["Jan", "Feb", "Mar", "Apr", "May", "Jun"]),
        y="Margin (%)"
    ).properties(height=300)

    st.altair_chart(chart, use_container_width=True)
