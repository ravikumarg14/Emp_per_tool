import streamlit as st  # pip install streamlit
from deta import Deta  # pip install deta


# Load the environment variables
DETA_KEY = "d0sas5umwhg_9N2kpDnHvw2jiWRg3XfddCniXjNCoan4"
# st.secrets["DETA_KEY"]

# Initialize with a project key
deta = Deta(DETA_KEY)

# This is how to create/connect a database
db = deta.Base("employee_data")


def insert_period(teamname, reviwername, doctype, number,rev,pages,description,startdate,enddate,hours):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"teamname": teamname, "reviwername": reviwername, "doctype": doctype, "number": number, "rev": rev, "pages": pages, "description": description, "startdate": startdate, "enddate": enddate,"hours": hours})


def fetch_all_periods():
    """Returns a dict of all periods"""
    res = db.fetch()
    return res.items


def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)

