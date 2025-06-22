import streamlit as st
import pandas as pd
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="QCDP Tracker", layout="wide")
st.title("📋 QCDP Topic Management & KPI Tracker")

# Initialize topics list
if "topics" not in st.session_state:
    st.session_state.topics = []

# Add Topic
if st.button("➕ Add Topic"):
    new_topic = {
        "ID": f"AT-{len(st.session_state.topics)+1:03}",
        "Type": "",
        "Q": "", "Q_desc": "",
        "C": "", "C_desc": "",
        "D": "", "D_desc": "",
        "P": "", "P_desc": "",
        "ISS": "", "ISS_status": "", "ISS_title": "",
        "ECR": "", "APQP": "", "DEC": "", "FETE": "",
        "Desc": "",
        "Com": f"{datetime.today().strftime('%Y-%m-%d')}: ",
        "Status": "",
        "DocInfo": "",
        "Actions": []
    }
    st.session_state.topics.append(new_topic)

# Display and edit topics
for i, topic in enumerate(st.session_state.topics):
    with st.expander(f"🧩 Topic {topic.get('ID', f'AT-{i+1:03}')}"):
        topic["Type"] = st.text_input("📂 Type of Topic (e.g. ISS, HW evolution)", value=topic.get("Type", ""), key=f"type_{i}")

        st.markdown("### 🔍 QCDP Status Details")
        col_qcdp = st.columns(4)

        with col_qcdp[0].expander("Q - Quality"):
            topic["Q"] = st.selectbox("Gravity", ["", "Green", "Yellow", "Red"],
                                      index=["", "Green", "Yellow", "Red"].index(topic.get("Q", "")), key=f"q_{i}")
            topic["Q_desc"] = st.text_area("Impact Description", value=topic.get("Q_desc", ""), key=f"q_desc_{i}")

        with col_qcdp[1].expander("C - Cost"):
            topic["C"] = st.selectbox("Gravity", ["", "Green", "Yellow", "Red"],
                                      index=["", "Green", "Yellow", "Red"].index(topic.get("C", "")), key=f"c_{i}")
            topic["C_desc"] = st.text_area("Impact Description", value=topic.get("C_desc", ""), key=f"c_desc_{i}")

        with col_qcdp[2].expander("D - Delay"):
            topic["D"] = st.selectbox("Gravity", ["", "Green", "Yellow", "Red"],
                                      index=["", "Green", "Yellow", "Red"].index(topic.get("D", "")), key=f"d_{i}")
            topic["D_desc"] = st.text_area("Impact Description", value=topic.get("D_desc", ""), key=f"d_desc_{i}")

        with col_qcdp[3].expander("P - Performance"):
            topic["P"] = st.selectbox("Gravity", ["", "Green", "Yellow", "Red"],
                                      index=["", "Green", "Yellow", "Red"].index(topic.get("P", "")), key=f"p_{i}")
            topic["P_desc"] = st.text_area("Impact Description", value=topic.get("P_desc", ""), key=f"p_desc_{i}")

        st.markdown("### ⚙️ Project Fields (ISS, ECR, etc.)")
        col_proj = st.columns(4)

        with col_proj[0].expander("ISS - Issue"):
            topic["ISS"] = st.selectbox("Gravity", ["", "A", "B", "C"],
                                        index=["", "A", "B", "C"].index(topic.get("ISS", "")), key=f"iss_{i}")
            topic["ISS_status"] = st.text_input("Status", value=topic.get("ISS_status", ""), key=f"iss_status_{i}")
            topic["ISS_title"] = st.text_input("Title", value=topic.get("ISS_title", ""), key=f"iss_title_{i}")

        topic["ECR"] = col_proj[1].text_input("ECR", value=topic.get("ECR", ""), key=f"ecr_{i}")
        topic["APQP"] = col_proj[2].text_input("APQP", value=topic.get("APQP", ""), key=f"apqp_{i}")
        topic["DEC"] = col_proj[3].text_input("DEC", value=topic.get("DEC", ""), key=f"dec_{i}")

        topic["FETE"] = st.text_input("FETE", value=topic.get("FETE", ""), key=f"fete_{i}")
        topic["Desc"] = st.text_area("📝 Description of the topic", value=topic.get("Desc", ""), key=f"desc_{i}")
        topic["Com"] = st.text_area("💬 Comments (auto-date)", value=topic.get("Com", ""), key=f"com_{i}")
        topic["Status"] = st.text_input("📍 Topic Status", value=topic.get("Status", ""), key=f"status_{i}")
        topic["DocInfo"] = st.text_input("📎 Document Info or References", value=topic.get("DocInfo", ""), key=f"docinfo_{i}")

# Display Table
if st.session_state.topics:
    st.subheader("📊 Topics Overview Table")
    df = pd.DataFrame(st.session_state.topics)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No topics yet. Click '➕ Add Topic' to get started.")
