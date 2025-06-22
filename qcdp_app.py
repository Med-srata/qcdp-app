import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Smart QCDP Editor", layout="wide")
st.title("📋 QCDP Table with Smart Dropdown Panels")

# Initialize state
if "topics" not in st.session_state:
    st.session_state.topics = []

if "edit_q_index" not in st.session_state:
    st.session_state.edit_q_index = None

# Add a topic
if st.button("➕ Add Topic"):
    new_topic = {
        "ID": f"AT-{len(st.session_state.topics)+1:03}",
        "Type": "",
        "Q": "", "Q_desc": "",
        "C": "", "C_desc": "",
        "D": "", "D_desc": "",
        "P": "", "P_desc": "",
        "ISS": "", "ECR": "", "APQP": "", "DEC": "", "FETE": "",
        "Desc": "", "Com": f"{datetime.today().strftime('%Y-%m-%d')}: ",
        "Action": "", "Status": "", "DocInfo": ""
    }
    st.session_state.topics.append(new_topic)

# Display table headers
st.markdown("### Topics Table (Click Q to Edit)")
cols = st.columns([1, 2, 2, 2, 2])
for col, header in zip(cols, ["ID", "Type", "Q", "Desc", "Status"]):
    col.markdown(f"**{header}**")

# Display each topic row
for i, topic in enumerate(st.session_state.topics):
    cols = st.columns([1, 2, 2, 2, 2])
    cols[0].text_input("ID", value=topic["ID"], key=f"id_{i}", disabled=True)
    topic["Type"] = cols[1].text_input("", value=topic.get("Type", ""), key=f"type_{i}")

    # Q column as a clickable button
    if st.session_state.edit_q_index == i:
        with cols[2]:
            topic["Q"] = st.selectbox("Gravity", ["", "A", "B", "C"], index=["", "A", "B", "C"].index(topic.get("Q", "")), key=f"qval_{i}")
            topic["Q_desc"] = st.text_input("Impact Description", value=topic.get("Q_desc", ""), key=f"qdesc_{i}")
            if st.button("✅ Save Q", key=f"qsave_{i}"):
                st.session_state.edit_q_index = None
    else:
        q_summary = topic["Q"]
        if topic["Q_desc"]:
            q_summary += f": {topic['Q_desc'][:20]}"
        if cols[2].button(q_summary or "Q", key=f"qbtn_{i}"):
            st.session_state.edit_q_index = i

    topic["Desc"] = cols[3].text_input("", value=topic.get("Desc", ""), key=f"desc_{i}")
    topic["Status"] = cols[4].text_input("", value=topic.get("Status", ""), key=f"status_{i}")
