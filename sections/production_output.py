# import streamlit as st
# from data_loader import get_fob_data, get_today_stage_output, get_cumulative_output

# def display():
#     st.subheader("📦 Production Output")

#     # 📊 FOB Date Comparison
#     st.markdown("### 🔁 FOB Value (Today vs Same Day Last Month)")
#     data = get_fob_data()
#     col1, col2 = st.columns(2)
#     with col1:
#         st.metric("19-06-2025 (Total)", f"${data['Total'][0]:.3f}M")
#         st.metric("MWC", f"{data['MWC'][0]:.3f}")
#         st.metric("Metal", f"{data['Metal'][0]:.3f}")
#     with col2:
#         st.metric("19-05-2025 (Total)", f"${data['Total'][1]:.3f}M")
#         st.metric("MWC", f"{data['MWC'][1]:.3f}")
#         st.metric("Metal", f"{data['Metal'][1]:.3f}")
        
#     # 🔩 Today's Production
#     st.markdown("### 🔧 Today's Stage-wise Output")
#     today = get_today_stage_output()
#     for _, row in today.iterrows():
#         st.success(f"🛠️ {row['Process']}: {row['Output (pcs)']} pcs, {row['Labor Hours']} hrs")

#     # 📆 Monthly Summary
#     st.markdown("### 📈 Cumulative Output (Month vs Last Month)")
#     summary = get_cumulative_output()
#     for _, row in summary.iterrows():
#         st.info(
#             f"🔧 {row['Process']}\n"
#             f"- 📅 This Month: {row['Current Month Output']} pcs | {row['Current Month Labor']} hrs\n"
#             f"- 📆 Last Month: {row['Last Month Output']} pcs | {row['Last Month Labor']} hrs"
#         )











import streamlit as st
import pandas as pd
from data_loader import get_production_output_data, get_hourly_output_data, get_cumulative_output_data

def show_production_output():
    st.subheader("📦 Production Output")

    # FOB
    st.markdown("### 📅 FOB Value (Today vs Same Day Last Month)")
    fob_df = get_production_output_data()
    st.dataframe(fob_df, use_container_width=True)

    # Hourly output
    st.markdown("### 🕒 Today's Stage-wise Output")
    hourly_df = get_hourly_output_data()
    st.dataframe(hourly_df, use_container_width=True)

    # Cumulative
    st.markdown("### 📊 Cumulative Output (Month vs Last Month)")
    cumulative_df = get_cumulative_output_data()
    st.dataframe(cumulative_df, use_container_width=True)
