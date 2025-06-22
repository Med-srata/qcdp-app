import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="QCDP Table Editor", layout="wide")
st.title("📋 QCDP Inline Table Editor")

# Initialize session data
if "topics" not in st.session_state:
    st.session_state.topics = []

# Add Topic Button
if st.button("➕ Add Topic"):
    new_topic = {
        "ID": f"AT-{len(st.session_state.topics)+1:03}",
        "Type": "",
        "Q": "", "Q_desc": "",
        "C": "", "C_desc": "",
        "D": "", "D_desc": "",
        "P": "", "P_desc": "",
        "ISS": "",
        "ECR": "", "APQP": "", "DEC": "", "FETE": "",
        "Desc": "", "Com": f"{datetime.today().strftime('%Y-%m-%d')}: ",
        "Action": "", "Status": "", "DocInfo": ""
    }
    st.session_state.topics.append(new_topic)

# Header row (table-like)
header_cols = st.columns([
    1.2, 2, 1, 1, 1, 1, 1.5, 1.5, 1.5, 1.5, 1.5, 2, 1.5, 1.5, 1.5
])
headers = ["ID", "Type", "Q", "C", "D", "P", "ISS", "ECR", "APQP", "DEC", "FETE", "Desc", "Action", "Status", "DocInfo"]
for col, text in zip(header_cols, headers):
    col.markdown(f"**{text}**")

# Rows: simulate editable table
for i, topic in enumerate(st.session_state.topics):
    cols = st.columns([
        1.2, 2, 1, 1, 1, 1, 1.5, 1.5, 1.5, 1.5, 1.5, 2, 1.5, 1.5, 1.5
    ])
    topic["ID"] = cols[0].text_input("ID", value=topic.get("ID", ""), key=f"id_{i}", disabled=True)
    topic["Type"] = cols[1].text_input("", value=topic.get("Type", ""), key=f"type_{i}")

    # QCDP dropdowns
    topic["Q"] = cols[2].selectbox("", ["", "Green", "Yellow", "Red"], index=["", "Green", "Yellow", "Red"].index(topic.get("Q", "")), key=f"q_{i}")
    topic["C"] = cols[3].selectbox("", ["", "Green", "Yellow", "Red"], index=["", "Green", "Yellow", "Red"].index(topic.get("C", "")), key=f"c_{i}")
    topic["D"] = cols[4].selectbox("", ["", "Green", "Yellow", "Red"], index=["", "Green", "Yellow", "Red"].index(topic.get("D", "")), key=f"d_{i}")
    topic["P"] = cols[5].selectbox("", ["", "Green", "Yellow", "Red"], index=["", "Green", "Yellow", "Red"].index(topic.get("P", "")), key=f"p_{i}")

    topic["ISS"] = cols[6].text_input("", value=topic.get("ISS", ""), key=f"iss_{i}")
    topic["ECR"] = cols[7].text_input("", value=topic.get("ECR", ""), key=f"ecr_{i}")
    topic["APQP"] = cols[8].text_input("", value=topic.get("APQP", ""), key=f"apqp_{i}")
    topic["DEC"] = cols[9].text_input("", value=topic.get("DEC", ""), key=f"dec_{i}")
    topic["FETE"] = cols[10].text_input("", value=topic.get("FETE", ""), key=f"fete_{i}")

    topic["Desc"] = cols[11].text_input("", value=topic.get("Desc", ""), key=f"desc_{i}")
    topic["Action"] = cols[12].text_input("", value=topic.get("Action", ""), key=f"action_{i}")
    topic["Status"] = cols[13].text_input("", value=topic.get("Status", ""), key=f"status_{i}")
    topic["DocInfo"] = cols[14].text_input("", value=topic.get("DocInfo", ""), key=f"docinfo_{i}")

# Optionally, show all in dataframe
if st.checkbox("📋 Show data as table (read-only)"):
    st.dataframe(pd.DataFrame(st.session_state.topics))
