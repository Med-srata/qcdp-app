import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="QCDP Tracker", layout="wide")
st.title("📋 QCDP Inline Table Editor (with Gravity & Impact Description)")

# Initialize topics list
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

# Gravity dropdown options
gravity_options = ["", "A", "B", "C"]

# Header row
st.markdown("#### 🧩 Editable QCDP Table")
headers = [
    "ID", "Type",
    "Q Gravity", "Q Impact",
    "C Gravity", "C Impact",
    "D Gravity", "D Impact",
    "P Gravity", "P Impact",
    "ISS", "ECR", "APQP", "DEC", "FETE",
    "Desc", "Com", "Action", "Status", "DocInfo"
]

col_widths = [1, 2] + [1, 2]*4 + [1]*6 + [2, 2, 2, 2, 2]
cols = st.columns(col_widths[:len(headers)])
for col, header in zip(cols, headers):
    col.markdown(f"**{header}**")

# Each topic as row
for i, topic in enumerate(st.session_state.topics):
    cols = st.columns(col_widths[:len(headers)])

    topic["ID"] = cols[0].text_input("ID", value=topic.get("ID", ""), key=f"id_{i}", disabled=True)
    topic["Type"] = cols[1].text_input("", value=topic.get("Type", ""), key=f"type_{i}")

    # Q
    q_val = topic.get("Q", "")
    q_idx = gravity_options.index(q_val) if q_val in gravity_options else 0
    topic["Q"] = cols[2].selectbox("", gravity_options, index=q_idx, key=f"q_{i}")
    topic["Q_desc"] = cols[3].text_input("", value=topic.get("Q_desc", ""), key=f"qdesc_{i}")

    # C
    c_val = topic.get("C", "")
    c_idx = gravity_options.index(c_val) if c_val in gravity_options else 0
    topic["C"] = cols[4].selectbox("", gravity_options, index=c_idx, key=f"c_{i}")
    topic["C_desc"] = cols[5].text_input("", value=topic.get("C_desc", ""), key=f"cdesc_{i}")

    # D
    d_val = topic.get("D", "")
    d_idx = gravity_options.index(d_val) if d_val in gravity_options else 0
    topic["D"] = cols[6].selectbox("", gravity_options, index=d_idx, key=f"d_{i}")
    topic["D_desc"] = cols[7].text_input("", value=topic.get("D_desc", ""), key=f"ddesc_{i}")

    # P
    p_val = topic.get("P", "")
    p_idx = gravity_options.index(p_val) if p_val in gravity_options else 0
    topic["P"] = cols[8].selectbox("", gravity_options, index=p_idx, key=f"p_{i}")
    topic["P_desc"] = cols[9].text_input("", value=topic.get("P_desc", ""), key=f"pdesc_{i}")

    topic["ISS"] = cols[10].text_input("", value=topic.get("ISS", ""), key=f"iss_{i}")
    topic["ECR"] = cols[11].text_input("", value=topic.get("ECR", ""), key=f"ecr_{i}")
    topic["APQP"] = cols[12].text_input("", value=topic.get("APQP", ""), key=f"apqp_{i}")
    topic["DEC"] = cols[13].text_input("", value=topic.get("DEC", ""), key=f"dec_{i}")
    topic["FETE"] = cols[14].text_input("", value=topic.get("FETE", ""), key=f"fete_{i}")

    topic["Desc"] = cols[15].text_input("", value=topic.get("Desc", ""), key=f"desc_{i}")
    topic["Com"] = cols[16].text_input("", value=topic.get("Com", ""), key=f"com_{i}")
    topic["Action"] = cols[17].text_input("", value=topic.get("Action", ""), key=f"action_{i}")
    topic["Status"] = cols[18].text_input("", value=topic.get("Status", ""), key=f"status_{i}")
    topic["DocInfo"] = cols[19].text_input("", value=topic.get("DocInfo", ""), key=f"docinfo_{i}")

# Optional summary
if st.checkbox("📊 Show full data as table"):
    st.dataframe(pd.DataFrame(st.session_state.topics))
