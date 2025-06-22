import streamlit as st
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(page_title="QCDP Tracker", layout="wide")

st.title("📋 QCDP Topic Management & KPI Tracker")

# Initialize topic list in session
if "topics" not in st.session_state:
    st.session_state.topics = []

# --- Add Topic Button ---
if st.button("➕ Add Topic"):
    new_topic = {
        "ID": f"AT-{len(st.session_state.topics)+1:03}",
        "Type": "",
        "Q": "",
        "C": "",
        "D": "",
        "P": "",
        "ISS": "",
        "ECR": "",
        "APQP": "",
        "DEC": "",
        "FETE": "",
        "Desc": "",
        "Com": f"{datetime.today().strftime('%Y-%m-%d')}: ",
        "Status": "",
        "DocInfo": "",
        "Actions": []
    }
    st.session_state.topics.append(new_topic)

# --- Display all topics ---
for i, topic in enumerate(st.session_state.topics):
    with st.expander(f"🧩 Topic {topic['ID']}"):
        col1, col2 = st.columns([2, 1])
        topic["Type"] = col1.text_input("Type of Topic", value=topic["Type"], key=f"type_{i}")

        col_qcdp = st.columns(4)
        topic["Q"] = col_qcdp[0].selectbox("Quality (Q)", ["", "Green", "Yellow", "Red"], index=["", "Green", "Yellow", "Red"].index(topic["Q"]), key=f"q_{i}")
        topic["C"] = col_qcdp[1].selectbox("Cost (C)", ["", "Green", "Yellow", "Red"], index=["", "Green", "Yellow", "Red"].index(topic["C"]), key=f"c_{i}")
        topic["D"] = col_qcdp[2].selectbox("Delay (D)", ["", "Green", "Yellow", "Red"], index=["", "Green", "Yellow", "Red"].index(topic["D"]), key=f"d_{i}")
        topic["P"] = col_qcdp[3].selectbox("Performance (P)", ["", "Green", "Yellow", "Red"], index=["", "Green", "Yellow", "Red"].index(topic["P"]), key=f"p_{i}")

        col_tags = st.columns(5)
        topic["ISS"] = col_tags[0].text_input("ISS", value=topic["ISS"], key=f"iss_{i}")
        topic["ECR"] = col_tags[1].text_input("ECR", value=topic["ECR"], key=f"ecr_{i}")
        topic["APQP"] = col_tags[2].text_input("APQP", value=topic["APQP"], key=f"apqp_{i}")
        topic["DEC"] = col_tags[3].text_input("DEC", value=topic["DEC"], key=f"dec_{i}")
        topic["FETE"] = col_tags[4].text_input("FETE", value=topic["FETE"], key=f"fete_{i}")

        topic["Desc"] = st.text_area("📝 Description", value=topic["Desc"], key=f"desc_{i}")
        topic["Com"] = st.text_area("💬 Comments", value=topic["Com"], key=f"com_{i}")
        topic["Status"] = st.text_input("📍 Status", value=topic["Status"], key=f"status_{i}")
        topic["DocInfo"] = st.text_input("📎 Document Info", value=topic["DocInfo"], key=f"docinfo_{i}")

# --- Table View ---
if st.session_state.topics:
    st.markdown("### 📊 Topics Table")
    df = pd.DataFrame(st.session_state.topics)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No topics yet. Click 'Add Topic' to get started.")

