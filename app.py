import calendar  # Core Python Module
import datetime  # Core Python Module
import plotly.graph_objects as go  # pip install plotly
import streamlit as st  # pip install streamlit
from streamlit_option_menu import option_menu  # pip install streamlit-option-menu
import pandas as pd

import database as db  # local import

# -------------- SETTINGS --------------
incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency = "USD"
page_title = "Employee Performance Tracker"
page_icon = ":globe_with_meridians:"  # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
teamnames = ["GE", "Quest"]
doctypes = ["DWG", "TechSpec","BOM"]


# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
# selected = option_menu(
#     menu_title=None,
#     options=["Data Entry", "Data Visualization"],
#     icons=["pencil-fill", "bar-chart-fill"],  # https://icons.getbootstrap.com/
#     orientation="horizontal",
# )

# --- INPUT & SAVE PERIODS ---
# if selected == "Data Entry":
# st.header(f"Data Entry in {currency}")
with st.form("entry_form", clear_on_submit=True):
    teamname=st.selectbox("Select Team Name:", teamnames, key="teamname")
    reviwername=st.text_input("Enter Reviwer Name",key="reviwername")
    doctype = st.selectbox("Select Doc Type:", doctypes, key="doctype")
    number=st.text_input("Enter Number",key="number")
    rev=st.text_input("Enter Rev Number",key="rev")
    # st.text_input("Enter Description Name",key="description")
    pages=st.number_input("Enter Number of Pages",min_value=0, format="%i", step=1,key="pages")
    description = st.text_area("Description", placeholder="Enter your Description here ...")
    startdate = st.date_input("Start Date", value=None, min_value=None, max_value=None, key="startdate", on_change=None, args=None, kwargs=None)
    enddate = st.date_input("End Date", value=None, min_value=startdate, max_value=None, key=None, on_change=None, args=None, kwargs=None)
    startdate=str(startdate)
    enddate=str(enddate)
    "---"
    submitted = st.form_submit_button("Save Data")
    if submitted:
        db.insert_period(teamname, reviwername, doctype, number,rev,pages,description,startdate,enddate)
        st.write(type(db.fetch_all_periods()))
        #df=pd.read_json(db.fetch_all_periods())
        st.write(db.fetch_all_periods())
        st.success("Data saved!")


# --- PLOT PERIODS ---
#if selected == "Data Visualization":
#st.header("Data Visualization")

# with st.form("saved_periods"):
#     period = st.selectbox("Select Period:", get_all_periods())
#     submitted = st.form_submit_button("Plot Period")
#     if submitted:
#         # Get data from database
#         period_data = db.get_period(period)
#         comment = period_data.get("comment")
#         expenses = period_data.get("expenses")
#         incomes = period_data.get("incomes")

#         # Create metrics
#         total_income = sum(incomes.values())
#         total_expense = sum(expenses.values())
#         remaining_budget = total_income - total_expense
#         col1, col2, col3 = st.columns(3)
#         col1.metric("Total Income", f"{total_income} {currency}")
#         col2.metric("Total Expense", f"{total_expense} {currency}")
#         col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
#         st.text(f"Comment: {comment}")

#         # Create sankey chart
#         label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
#         source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
#         target = [len(incomes)] * len(incomes) + [label.index(expense) for expense in expenses.keys()]
#         value = list(incomes.values()) + list(expenses.values())

#         # Data to dict, dict to sankey
#         link = dict(source=source, target=target, value=value)
#         node = dict(label=label, pad=20, thickness=30, color="#E694FF")
#         data = go.Sankey(link=link, node=node)

#         # Plot it!
#         fig = go.Figure(data)
#         fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
#         st.plotly_chart(fig, use_container_width=True)
