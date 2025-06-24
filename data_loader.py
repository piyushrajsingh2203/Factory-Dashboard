# import pandas as pd

# # --- FOB Production Data ---
# def get_fob_data():
#     return pd.DataFrame({
#         "Date": ["19-06-2025", "19-05-2025"],
#         "MWC": [0.011, 0.026],
#         "Metal": [0.005, 0.011],
#         "Total": [0.017, 0.037]
#     })

# # --- Daily Output Summary (Stage-wise, Today) ---
# def get_today_stage_output():
#     return pd.DataFrame({
#         "Process": ["Machining", "Assembly", "Sanding", "Polishing", "Upholstery", "Fitting", "FG"],
#         "Output (pcs)": [14054, 139, 177, 239, 218, 128, 255],
#         "Labor Hours": [975, 282, 63, 307, 525, 72, 152]
#     })

# # --- Monthly Summary: Current vs Last ---
# def get_cumulative_output():
#     return pd.DataFrame({
#         "Process": ["Machining", "Assembly", "Sanding", "Polishing", "Upholstery", "Fitting", "FG"],
#         "Current Month Output": [124504, 2676, 2603, 2958, 2069, 1789, 3099],
#         "Current Month Labor": [8212, 5859, 1063, 2888, 5725, 787, 2031],
#         "Last Month Output": [95408, 2421, 2285, 2380, 1582, 1434, 2584],
#         "Last Month Labor": [17942, 4691, 1299, 1929, 1432, 874, 1815]
#     })

# # --- Revenue Section ---
# def get_billing_data():
#     return {
#         "Today": 0.06,
#         "Same Day Last Month": 0.03,
#         "Month Till Date": 0.32,
#         "Same Month Last Year": 0.48
#     }

# def get_order_data():
#     return {
#         "Order in Hand": {
#             "Today": 2.67,
#             "Same Day Last Month": 3.00
#         },
#         "Order Received": {
#             "Month Till Date": 0.36,
#             "Same Month Last Year": 0.10
#         }
#     }

# # --- Margin ---
# def get_margin_data():
#     return pd.DataFrame({
#         "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#         "Margin (%)": [18.2, 19.1, 17.5, 18.8, 20.0, 19.4]
#     })














import pandas as pd

def get_production_output_data():
    return pd.DataFrame([
        {"Date": "2025-06-19", "MWC": 0.011, "Metal": 0.005, "Total": 0.017},
        {"Date": "2025-05-19", "MWC": 0.026, "Metal": 0.011, "Total": 0.037}
    ])

def get_hourly_output_data():
    return pd.DataFrame([
        {"Hour": "08:00", "Process": "Machining", "Output (pcs)": 14054, "Labor Hours": 975},
        {"Hour": "10:00", "Process": "Assembly", "Output (pcs)": 139, "Labor Hours": 282},
        {"Hour": "12:00", "Process": "Sanding", "Output (pcs)": 177, "Labor Hours": 63},
        {"Hour": "14:00", "Process": "Polishing", "Output (pcs)": 239, "Labor Hours": 307},
        {"Hour": "16:00", "Process": "Upholstery", "Output (pcs)": 218, "Labor Hours": 525},
        {"Hour": "18:00", "Process": "Fitting", "Output (pcs)": 128, "Labor Hours": 72},
        {"Hour": "20:00", "Process": "FG", "Output (pcs)": 255, "Labor Hours": 152},
    ])

def get_cumulative_output_data():
    return pd.DataFrame([
        {"Process": "Machining", "Current Month Output": 124504, "Current Month Labor": 8212, "Last Month Output": 95408, "Last Month Labor": 17942},
        {"Process": "Assembly", "Current Month Output": 2676, "Current Month Labor": 5859, "Last Month Output": 4221, "Last Month Labor": 4691},
        {"Process": "Sanding", "Current Month Output": 2603, "Current Month Labor": 1063, "Last Month Output": 2285, "Last Month Labor": 1299},
        {"Process": "Polishing", "Current Month Output": 2958, "Current Month Labor": 2755, "Last Month Output": 2380, "Last Month Labor": 1929},
        {"Process": "Upholstery", "Current Month Output": 2069, "Current Month Labor": 5725, "Last Month Output": 1582, "Last Month Labor": 1474},
        {"Process": "Fitting", "Current Month Output": 1789, "Current Month Labor": 787, "Last Month Output": 1434, "Last Month Labor": 874},
        {"Process": "FG", "Current Month Output": 3099, "Current Month Labor": 2031, "Last Month Output": 2584, "Last Month Labor": 1815},
    ])

def get_revenue_data():
    return {
        "billing": pd.DataFrame([
            {"Current Date": 0.06, "Same Day Last Month": 0.03, "During Month": 0.32, "Same Date Last Month": 0.48}
        ]),
        "order_in_hand": pd.DataFrame([
            {"During Month": 2.67, "Same Date Last Month": 3.00}
        ]),
        "order_received": pd.DataFrame([
            {"During Month": 0.36, "Same Date Last Month": 0.10}
        ])
    }

def get_margin_data():
    df = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Margin (%)": [18.2, 19.1, 17.5, 18.8, 20.0, 19.4]
    })
    df["Month"] = pd.Categorical(df["Month"], categories=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], ordered=True)
    return df.sort_values("Month")
