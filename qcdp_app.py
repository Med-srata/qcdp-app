import streamlit as st
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="QCDP Interactive Table", layout="wide")
st.title("📋 QCDP Inline Table — Gravity + Impact (Click-to-Edit)")

# Initialize state
if "topics" not in st.session_state:
    st.session_state.topics = []

# Track open edit index per column
for col in ["q", "c", "d", "p"]:
    if f"edit_{col}_index" not in st.session_state:
        st.session_state[f"edit_{col}_index"] = None

# Add Topic
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

# Table headers
st.markdown("### 🧩 Topics Table (Click Q/C/D/P to Edit)")
header = st.columns([1, 2, 2, 2, 2, 2, 2, 2])
labels = ["ID", "Type", "Q", "C", "D", "P", "Desc", "Status"]
for col, label in zip(header, labels):
    col.markdown(f"**{label}**")

# Row renderer
gravity_levels = ["", "A", "B", "C"]

for i, topic in enumerate(st.session_state.topics):
    cols = st.columns([1, 2, 2, 2, 2, 2, 2, 2])

    cols[0].text_input("ID", value=topic["ID"], key=f"id_{i}", disabled=True)
    topic["Type"] = cols[1].text_input("", value=topic.get("Type", ""), key=f"type_{i}")

    # Smart editable cell function
    def editable_cell(label, key_prefix, col_num):
        col = cols[col_num]
        value = topic.get(label, "")
        desc = topic.get(f"{label}_desc", "")
        state_key = f"edit_{key_prefix}_index"

        if st.session_state[state_key] == i:
            topic[label] = col.selectbox("Gravity", gravity_levels,
                                         index=gravity_levels.index(value) if value in gravity_levels else 0,
                                         key=f"{key_prefix}_val_{i}")
            topic[f"{label}_desc"] = col.text_input("Impact Desc", value=desc, key=f"{key_prefix}_desc_{i}")
            if col.button("✅", key=f"{key_prefix}_save_{i}"):
                st.session_state[state_key] = None
        else:
            label_summary = f"{value}: {desc[:10]}" if value else label
            if col.button(label_summary, key=f"{key_prefix}_btn_{i}"):
                st.session_state[state_key] = i

    editable_cell("Q", "q", 2)
    editable_cell("C", "c", 3)
    editable_cell("D", "d", 4)
    editable_cell("P", "p", 5)

    topic["Desc"] = cols[6].text_input("", value=topic.get("Desc", ""), key=f"desc_{i}")
    topic["Status"] = cols[7].text_input("", value=topic.get("Status", ""), key=f"status_{i}")
