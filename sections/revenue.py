# import streamlit as st
# from data_loader import get_billing_data, get_order_data

# def display():
#     st.subheader("💵 Revenue Summary")

#     billing = get_billing_data()
#     st.markdown("### Billing")
#     st.metric("Today", f"${billing['Today']:.2f}M")
#     st.metric("Same Day Last Month", f"${billing['Same Day Last Month']:.2f}M")
#     st.metric("Month Till Date", f"${billing['Month Till Date']:.2f}M")
#     st.metric("Same Month Last Year", f"${billing['Same Month Last Year']:.2f}M")

#     order = get_order_data()

#     st.markdown("### 📦 Order in Hand")
#     st.metric("Today", f"${order['Order in Hand']['Today']:.2f}M")
#     st.metric("Same Day Last Month", f"${order['Order in Hand']['Same Day Last Month']:.2f}M")

#     st.markdown("### ✅ Order Received")
#     st.metric("This Month", f"${order['Order Received']['Month Till Date']:.2f}M")
#     st.metric("Same Month Last Year", f"${order['Order Received']['Same Month Last Year']:.2f}M")













import streamlit as st
import pandas as pd
from data_loader import get_revenue_data

def show_revenue():
    st.subheader("💰 Revenue Overview")

    revenue = get_revenue_data()
    
    st.markdown("### Billing")
    st.dataframe(revenue["billing"], use_container_width=True)

    st.markdown("### Order in Hand")
    st.dataframe(revenue["order_in_hand"], use_container_width=True)

    st.markdown("### Order Received")
    st.dataframe(revenue["order_received"], use_container_width=True)
