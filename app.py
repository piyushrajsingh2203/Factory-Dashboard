# import streamlit as st
# from sections import production_output, revenue, margin

# st.set_page_config(page_title="Factory Dashboard", layout="centered")
# st.title("📱 Factory Dashboard")

# section = st.selectbox("🔍 Select Report", [
#     "Production Output",
#     "Revenue",
#     "Margin"
# ])

# if section == "Production Output":
#     production_output.display()
# elif section == "Revenue":
#     revenue.display()
# elif section == "Margin":
#     margin.display()












# import streamlit as st
# from sections.production_output import show_production_output
# from sections.revenue import show_revenue
# from sections.margin import show_margin

# st.set_page_config(page_title="Factory Dashboard", layout="wide")

# st.markdown("<h1 style='text-align: center;'>📊 Factory Dashboard</h1>", unsafe_allow_html=True)

# # Mobile-style main menu
# page = st.selectbox("📌 Select Report", ["-- Select --", "Production Output", "Revenue", "Margin"])

# # Show only selected section
# if page == "Production Output":
#     show_production_output()

# elif page == "Revenue":
#     show_revenue()

# elif page == "Margin":
#     show_margin()

# else:
#     st.info("👆 Please select a report to view the dashboard.")




















# import streamlit as st
# import pandas as pd
# from streamlit_option_menu import option_menu
# from datetime import datetime

# # -------------------------------
# # Load Static Sample Data
# # -------------------------------
# def load_production_output():
#     return pd.DataFrame([
#         {"Date": "2025-06-19", "MWC": 0.011, "Metal": 0.005, "Total": 0.017},
#         {"Date": "2025-05-19", "MWC": 0.026, "Metal": 0.011, "Total": 0.037},
#     ])

# def load_stagewise_today():
#     return pd.DataFrame([
#         {"Process": "Machining", "Output (pcs)": 14054, "Labor Hours": 975},
#         {"Process": "Assembly", "Output (pcs)": 139, "Labor Hours": 282},
#         {"Process": "Sanding", "Output (pcs)": 177, "Labor Hours": 63},
#         {"Process": "Polishing", "Output (pcs)": 239, "Labor Hours": 307},
#         {"Process": "Upholstery", "Output (pcs)": 218, "Labor Hours": 525},
#         {"Process": "Fitting", "Output (pcs)": 128, "Labor Hours": 72},
#         {"Process": "FG", "Output (pcs)": 255, "Labor Hours": 152},
#     ])

# def load_cumulative_output():
#     return pd.DataFrame([
#         {"Process": "Machining", "This Month Output": 124504, "This Month Labor": 8212, "Last Month Output": 95408, "Last Month Labor": 17942},
#         {"Process": "Assembly", "This Month Output": 2676, "This Month Labor": 5859, "Last Month Output": 4221, "Last Month Labor": 4691},
#         {"Process": "Sanding", "This Month Output": 2603, "This Month Labor": 1063, "Last Month Output": 2285, "Last Month Labor": 1299},
#         {"Process": "Polishing", "This Month Output": 2958, "This Month Labor": 2755, "Last Month Output": 2380, "Last Month Labor": 1929},
#         {"Process": "Upholstery", "This Month Output": 2069, "This Month Labor": 5725, "Last Month Output": 1582, "Last Month Labor": 1474},
#         {"Process": "Fitting", "This Month Output": 1789, "This Month Labor": 787, "Last Month Output": 1434, "Last Month Labor": 874},
#         {"Process": "FG", "This Month Output": 3099, "This Month Labor": 2031, "Last Month Output": 2584, "Last Month Labor": 1815},
#     ])

# def load_revenue_data():
#     return {
#         "Billing": {"Today": 0.06, "Same Day Last Month": 0.03, "Month Till Date": 0.32, "Last Month Till Date": 0.48},
#         "Order In Hand": {"Month Till Date": 2.67, "Last Month": 3.00},
#         "Order Received": {"Month Till Date": 0.36, "Last Month": 0.10}
#     }

# def load_margin_data():
#     return pd.DataFrame({
#         "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#         "Margin %": [18.2, 19.1, 17.5, 18.9, 20.1, 19.6]
#     })

# # -------------------------------
# # Streamlit Page Config
# # -------------------------------
# st.set_page_config(page_title="Factory Dashboard", layout="centered", page_icon="📈")
# st.markdown("""
#     <style>
#         .block-container {
#             padding-top: 1rem;
#             padding-bottom: 2rem;
#         }
#         .report-card {
#             background-color: #f9f9f9;
#             padding: 1rem;
#             border-radius: 1rem;
#             box-shadow: 0 0 8px rgba(0,0,0,0.05);
#             margin-bottom: 1rem;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.title("📊 Factory Dashboard")


# selected = option_menu(
#     menu_title="Select Report",
#     options=["Production Output", "Revenue", "Margin"],
#     icons=["box", "currency-dollar", "percent"],
#     orientation="horizontal"
# )

# # -------------------------------
# # Report Logic
# # -------------------------------
# if selected == "Production Output":
#     st.header("🎁 Production Output")

#     st.subheader("📊 FOB Value (Today vs Same Day Last Month)")
#     st.dataframe(load_production_output(), use_container_width=True)

#     st.subheader("🕒 Today's Stage-wise Output")
#     for _, row in load_stagewise_today().iterrows():
#         with st.container():
#             st.markdown(f"<div class='report-card'>⛏️ <b>{row['Process']}</b>: {row['Output (pcs)']} pcs | {row['Labor Hours']} hrs</div>", unsafe_allow_html=True)

#     st.subheader("📊 Cumulative Output (Month vs Last Month)")
#     for _, row in load_cumulative_output().iterrows():
#         with st.container():
#             st.markdown(f"""
#                 <div class='report-card'>
#                     <b>{row['Process']}</b><br>
#                     📅 <b>This Month:</b> {row['This Month Output']} pcs | {row['This Month Labor']} hrs<br>
#                     ⏲️ <b>Last Month:</b> {row['Last Month Output']} pcs | {row['Last Month Labor']} hrs
#                 </div>
#             """, unsafe_allow_html=True)

# elif selected == "Revenue":
#     st.header("💰 Revenue")
#     data = load_revenue_data()

#     st.subheader("📆 Billing")
#     for k, v in data["Billing"].items():
#         st.markdown(f"<div class='report-card'>📅 <b>{k}</b>: ${v:.2f}M</div>", unsafe_allow_html=True)

#     st.subheader("📦 Order In Hand")
#     for k, v in data["Order In Hand"].items():
#         st.markdown(f"<div class='report-card'>📊 <b>{k}</b>: {v:.2f}M</div>", unsafe_allow_html=True)

#     st.subheader("✉️ Order Received")
#     for k, v in data["Order Received"].items():
#         st.markdown(f"<div class='report-card'>📦 <b>{k}</b>: {v:.2f}M</div>", unsafe_allow_html=True)

# elif selected == "Margin":
#     st.header("🔢 Rolling Margin - 6 Months")
#     df = load_margin_data()
#     st.line_chart(df.set_index("Month"))






















# import streamlit as st
# import pandas as pd
# from streamlit_option_menu import option_menu
# from datetime import datetime

# # -------------------------------
# # Load Static Sample Data
# # -------------------------------
# def load_production_output():
#     return pd.DataFrame([
#         {"Date": "2025-06-19", "MWC": 0.011, "Metal": 0.005, "Total": 0.017},
#         {"Date": "2025-05-19", "MWC": 0.026, "Metal": 0.011, "Total": 0.037},
#     ])

# def load_stagewise_today():
#     return pd.DataFrame([
#         {"Process": "Machining", "Output (pcs)": 14054, "Labor Hours": 975},
#         {"Process": "Assembly", "Output (pcs)": 139, "Labor Hours": 282},
#         {"Process": "Sanding", "Output (pcs)": 177, "Labor Hours": 63},
#         {"Process": "Polishing", "Output (pcs)": 239, "Labor Hours": 307},
#         {"Process": "Upholstery", "Output (pcs)": 218, "Labor Hours": 525},
#         {"Process": "Fitting", "Output (pcs)": 128, "Labor Hours": 72},
#         {"Process": "FG", "Output (pcs)": 255, "Labor Hours": 152},
#     ])

# def load_cumulative_output():
#     return pd.DataFrame([
#         {"Process": "Machining", "This Month Output": 124504, "This Month Labor": 8212, "Last Month Output": 95408, "Last Month Labor": 17942},
#         {"Process": "Assembly", "This Month Output": 2676, "This Month Labor": 5859, "Last Month Output": 4221, "Last Month Labor": 4691},
#         {"Process": "Sanding", "This Month Output": 2603, "This Month Labor": 1063, "Last Month Output": 2285, "Last Month Labor": 1299},
#         {"Process": "Polishing", "This Month Output": 2958, "This Month Labor": 2755, "Last Month Output": 2380, "Last Month Labor": 1929},
#         {"Process": "Upholstery", "This Month Output": 2069, "This Month Labor": 5725, "Last Month Output": 1582, "Last Month Labor": 1474},
#         {"Process": "Fitting", "This Month Output": 1789, "This Month Labor": 787, "Last Month Output": 1434, "Last Month Labor": 874},
#         {"Process": "FG", "This Month Output": 3099, "This Month Labor": 2031, "Last Month Output": 2584, "Last Month Labor": 1815},
#     ])

# def load_revenue_data():
#     return {
#         "Billing": {"Today": 0.06, "Same Day Last Month": 0.03, "Month Till Date": 0.32, "Last Month Till Date": 0.48},
#         "Order In Hand": {"Month Till Date": 2.67, "Last Month": 3.00},
#         "Order Received": {"Month Till Date": 0.36, "Last Month": 0.10}
#     }

# def load_margin_data():
#     return pd.DataFrame({
#         "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#         "Margin %": [18.2, 19.1, 17.5, 18.9, 20.1, 19.6]
#     })

# # -------------------------------
# # Streamlit Page Config
# # -------------------------------
# st.set_page_config(page_title="Factory Dashboard", layout="centered", page_icon="📈")
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(120deg, #f6f9fc 0%, #eef3f8 100%) !important;
#             font-family: 'Segoe UI', sans-serif;
#         }
#         .block-container {
#             padding-top: 1rem;
#             padding-bottom: 2rem;
#         }
#         .report-card {
#             background-color: #ffffff;
#             padding: 1rem 1.5rem;
#             border-radius: 1.2rem;
#             box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
#             margin-bottom: 1rem;
#             border-left: 6px solid #4A90E2;
#         }
#         .report-header {
#             color: #4A90E2;
#             font-weight: 600;
#             font-size: 1.2rem;
#             margin-bottom: 0.5rem;
#         }
#     </style>
# """, unsafe_allow_html=True)

# st.title("📊 Factory Dashboard")

# selected = option_menu(
#     menu_title="Select Report",
#     options=["Production Output", "Revenue", "Margin"],
#     icons=["box", "currency-dollar", "percent"],
#     orientation="horizontal"
# )

# # -------------------------------
# # Report Logic
# # -------------------------------
# if selected == "Production Output":
#     st.header("🎁 Production Output")

#     st.markdown("<div class='report-header'>📊 FOB Value (Today vs Same Day Last Month)</div>", unsafe_allow_html=True)
#     st.dataframe(load_production_output(), use_container_width=True)

#     st.markdown("<div class='report-header'>🕒 Today's Stage-wise Output</div>", unsafe_allow_html=True)
#     for _, row in load_stagewise_today().iterrows():
#         with st.container():
#             st.markdown(f"<div class='report-card'>⛏️ <b>{row['Process']}</b>: {row['Output (pcs)']} pcs | {row['Labor Hours']} hrs</div>", unsafe_allow_html=True)

#     st.markdown("<div class='report-header'>📊 Cumulative Output (Month vs Last Month)</div>", unsafe_allow_html=True)
#     for _, row in load_cumulative_output().iterrows():
#         with st.container():
#             st.markdown(f"""
#                 <div class='report-card'>
#                     <b>{row['Process']}</b><br>
#                     📅 <b>This Month:</b> {row['This Month Output']} pcs | {row['This Month Labor']} hrs<br>
#                     ⏲️ <b>Last Month:</b> {row['Last Month Output']} pcs | {row['Last Month Labor']} hrs
#                 </div>
#             """, unsafe_allow_html=True)

# elif selected == "Revenue":
#     st.header("💰 Revenue")
#     data = load_revenue_data()

#     st.markdown("<div class='report-header'>📆 Billing</div>", unsafe_allow_html=True)
#     for k, v in data["Billing"].items():
#         st.markdown(f"<div class='report-card'>📅 <b>{k}</b>: ${v:.2f}M</div>", unsafe_allow_html=True)

#     st.markdown("<div class='report-header'>📦 Order In Hand</div>", unsafe_allow_html=True)
#     for k, v in data["Order In Hand"].items():
#         st.markdown(f"<div class='report-card'>📊 <b>{k}</b>: {v:.2f}M</div>", unsafe_allow_html=True)

#     st.markdown("<div class='report-header'>✉️ Order Received</div>", unsafe_allow_html=True)
#     for k, v in data["Order Received"].items():
#         st.markdown(f"<div class='report-card'>📦 <b>{k}</b>: {v:.2f}M</div>", unsafe_allow_html=True)

# elif selected == "Margin":
#     st.header("🔢 Rolling Margin - 6 Months")
#     df = load_margin_data()
#     st.line_chart(df.set_index("Month"))















import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from datetime import datetime

# -------------------------------
# Load Static Sample Data
# -------------------------------
def load_production_output():
    return pd.DataFrame([
        {"Date": "2025-06-19", "MWC": 0.011, "Metal": 0.005, "Total": 0.017},
        {"Date": "2025-05-19", "MWC": 0.026, "Metal": 0.011, "Total": 0.037},
    ])

def load_stagewise_today():
    return pd.DataFrame([
        {"Process": "Machining", "Output (pcs)": 14054, "Labor Hours": 975},
        {"Process": "Assembly", "Output (pcs)": 139, "Labor Hours": 282},
        {"Process": "Sanding", "Output (pcs)": 177, "Labor Hours": 63},
        {"Process": "Polishing", "Output (pcs)": 239, "Labor Hours": 307},
        {"Process": "Upholstery", "Output (pcs)": 218, "Labor Hours": 525},
        {"Process": "Fitting", "Output (pcs)": 128, "Labor Hours": 72},
        {"Process": "FG", "Output (pcs)": 255, "Labor Hours": 152},
    ])

def load_cumulative_output():
    return pd.DataFrame([
        {"Process": "Machining", "This Month Output": 124504, "This Month Labor": 8212, "Last Month Output": 95408, "Last Month Labor": 17942},
        {"Process": "Assembly", "This Month Output": 2676, "This Month Labor": 5859, "Last Month Output": 4221, "Last Month Labor": 4691},
        {"Process": "Sanding", "This Month Output": 2603, "This Month Labor": 1063, "Last Month Output": 2285, "Last Month Labor": 1299},
        {"Process": "Polishing", "This Month Output": 2958, "This Month Labor": 2755, "Last Month Output": 2380, "Last Month Labor": 1929},
        {"Process": "Upholstery", "This Month Output": 2069, "This Month Labor": 5725, "Last Month Output": 1582, "Last Month Labor": 1474},
        {"Process": "Fitting", "This Month Output": 1789, "This Month Labor": 787, "Last Month Output": 1434, "Last Month Labor": 874},
        {"Process": "FG", "This Month Output": 3099, "This Month Labor": 2031, "Last Month Output": 2584, "Last Month Labor": 1815},
    ])

def load_revenue_data():
    return {
        "Billing": {"Today": 0.06, "Same Day Last Month": 0.03, "Month Till Date": 0.32, "Last Month Till Date": 0.48},
        "Order In Hand": {"Month Till Date": 2.67, "Last Month": 3.00},
        "Order Received": {"Month Till Date": 0.36, "Last Month": 0.10}
    }

def load_margin_data():
    return pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Margin %": [18.2, 19.1, 17.5, 18.9, 20.1, 19.6]
    })

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(page_title="Factory Dashboard", layout="centered", page_icon="📊")
# st.markdown("""
#     <style>
#         body {
#             background: linear-gradient(135deg, #e3f2fd 0%, #fce4ec 100%) !important;
#             font-family: 'Segoe UI', sans-serif;
#         }
#         .block-container {
#             padding-top: 1rem;
#             padding-bottom: 2rem;
#         }
#         .report-card {
#             background-color: #ffffff;
#             padding: 1rem 1.5rem;
#             border-radius: 1.2rem;
#             box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
#             margin-bottom: 1rem;
#             border-left: 6px solid #42a5f5;
#         }
#         .report-header {
#             color: #1e88e5;
#             font-weight: 600;
#             font-size: 1.2rem;
#             margin-bottom: 0.5rem;
#         }
#     </style>
# """, unsafe_allow_html=True)


st.markdown("""
    <style>
    /* Set gradient background */
    body {
        background: linear-gradient(145deg, #e8f0ff, #fef9f3);
        background-attachment: fixed;
        background-size: cover;
        font-family: 'Segoe UI', sans-serif;
        color: #333333;
    }

    /* App main container styling */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 800px;
        margin: auto;
    }

    /* Section headers */
    .report-header {
        font-size: 1.2rem;
        font-weight: bold;
        color: #3056d3;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        border-left: 4px solid #3056d3;
        padding-left: 0.6rem;
    }

    /* Card styles */
    .report-card {
        background-color: #ffffffcc;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
        border-radius: 1.2rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        border-left: 5px solid #4A90E2;
        transition: transform 0.2s;
    }

    .report-card:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    }

    /* Optional table tweaks */
    .stDataFrame, .stTable {
        background-color: #ffffffdd;
        border-radius: 0.5rem;
        padding: 0.5rem;
    }

    /* Dropdown styling */
    .st-emotion-cache-16txtl3 {
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1);
    }

    </style>
""", unsafe_allow_html=True)



st.title("📊 Factory Dashboard")

selected = option_menu(
    menu_title="Select Report",
    options=["Production Output", "Revenue", "Margin"],
    icons=["box", "currency-dollar", "percent"],
    orientation="horizontal"
)

# -------------------------------
# Report Logic
# -------------------------------
if selected == "Production Output":
    st.header("🎁 Production Output")

    st.markdown("<div class='report-header'>📊 FOB Value (Today vs Same Day Last Month)</div>", unsafe_allow_html=True)
    st.dataframe(load_production_output(), use_container_width=True)

    st.markdown("<div class='report-header'>⏰ Today's Stage-wise Output</div>", unsafe_allow_html=True)
    for _, row in load_stagewise_today().iterrows():
        with st.container():
            st.markdown(f"<div class='report-card'>🔧 <b>{row['Process']}</b>: {row['Output (pcs)']} pcs | {row['Labor Hours']} hrs</div>", unsafe_allow_html=True)

    st.markdown("<div class='report-header'>📊 Cumulative Output (Month vs Last Month)</div>", unsafe_allow_html=True)
    for _, row in load_cumulative_output().iterrows():
        with st.container():
            st.markdown(f"""
                <div class='report-card'>
                    <b>{row['Process']}</b><br>
                    📅 <b>This Month:</b> {row['This Month Output']} pcs | {row['This Month Labor']} hrs<br>
                    ⏲️ <b>Last Month:</b> {row['Last Month Output']} pcs | {row['Last Month Labor']} hrs
                </div>
            """, unsafe_allow_html=True)

elif selected == "Revenue":
    st.header("💰 Revenue")
    data = load_revenue_data()

    st.markdown("<div class='report-header'>📆 Billing</div>", unsafe_allow_html=True)
    for k, v in data["Billing"].items():
        st.markdown(f"<div class='report-card'>📅 <b>{k}</b>: ${v:.2f}M</div>", unsafe_allow_html=True)

    st.markdown("<div class='report-header'>📦 Order In Hand</div>", unsafe_allow_html=True)
    for k, v in data["Order In Hand"].items():
        st.markdown(f"<div class='report-card'>📊 <b>{k}</b>: {v:.2f}M</div>", unsafe_allow_html=True)

    st.markdown("<div class='report-header'>✉️ Order Received</div>", unsafe_allow_html=True)
    for k, v in data["Order Received"].items():
        st.markdown(f"<div class='report-card'>📦 <b>{k}</b>: {v:.2f}M</div>", unsafe_allow_html=True)

elif selected == "Margin":
    st.header("📈 Rolling Margin - 6 Months")
    df = load_margin_data()
    st.line_chart(df.set_index("Month"))
