import streamlit as st
from datetime import datetime

st.set_page_config(page_title="QCDP Interactive Table", layout="wide")
st.title("📋 QCDP Interactive Table")

# Initialize session state for topics
def initialize_topic(index):
    return {
        "ID": f"T-{index+1:03}",
        "Type": "",
        "Q": {"gravity": "", "desc": "", "expanded": False},
        "C": {"gravity": "", "desc": "", "expanded": False},
        "D": {"gravity": "", "desc": "", "expanded": False},
        "P": {"gravity": "", "desc": "", "expanded": False},
        "ISS": {"gravity": "", "status": "", "title": "", "target": "", "expanded": False},
        "ECR": {
            "type": "", "status": "", "instance": "", "title": "",
            "instruction_date": None, "conception_date": None,
            "officialisation_date": None, "demarrage_date": None,
            "solde_date": None, "ready": False, "expanded": False
        },
        "APQP": {"reference": "", "status": "", "comment": "", "expanded": False},
        "DEC": {"reference": "", "status": "", "comment": "", "expanded": False},
        "FETE": {"reference": "", "status": "", "comment": "", "expanded": False},
        "Desc": "",
        "Status": ""
    }

if "topics" not in st.session_state:
    st.session_state.topics = []

# Add topic
if st.button("➕ Add Topic"):
    st.session_state.topics.append(initialize_topic(len(st.session_state.topics)))

# Column headers
columns_labels = ["ID", "Type", "Q", "C", "D", "P", "ISS", "ECR", "APQP", "DEC", "FETE", "Desc", "Status"]
col_widths = [1] * len(columns_labels)
header_cols = st.columns(col_widths)
for i, label in enumerate(columns_labels):
    header_cols[i].markdown(f"**{label}**")

# Helper for dropdown panels

def gravity_dropdown(col, field, topic, key_prefix):
    if topic[field]["expanded"]:
        topic[field]["gravity"] = col.selectbox("Gravity", ["", "A", "B", "C"], key=f"{key_prefix}_grav")
        topic[field]["desc"] = col.text_area("Impact desc", key=f"{key_prefix}_desc")
    else:
        summary = topic[field]["gravity"] or ""
        if col.button(summary or field, key=f"btn_{key_prefix}"):
            topic[field]["expanded"] = True


def iss_dropdown(col, topic, key_prefix):
    if topic["ISS"]["expanded"]:
        topic["ISS"]["gravity"] = col.selectbox("Gravity", ["", "A", "B", "C"], key=f"{key_prefix}_grav")
        topic["ISS"]["status"] = col.text_input("Status", key=f"{key_prefix}_status")
        topic["ISS"]["title"] = col.text_input("Title", key=f"{key_prefix}_title")
        topic["ISS"]["target"] = col.text_input("Target", key=f"{key_prefix}_target")
    else:
        if col.button("ISS", key=f"btn_{key_prefix}"):
            topic["ISS"]["expanded"] = True


def ecr_dropdown(col, topic, key_prefix):
    if topic["ECR"]["expanded"]:
        for field in ["type", "status", "instance", "title"]:
            topic["ECR"][field] = col.text_input(field.capitalize(), key=f"{key_prefix}_{field}")
        for field in ["instruction_date", "conception_date", "officialisation_date", "demarrage_date", "solde_date"]:
            topic["ECR"][field] = col.date_input(field.replace("_", " ").capitalize(), key=f"{key_prefix}_{field}")
        topic["ECR"]["ready"] = col.checkbox("Ready", key=f"{key_prefix}_ready")
    else:
        if col.button("ECR", key=f"btn_{key_prefix}"):
            topic["ECR"]["expanded"] = True


def simple_block(col, topic, section, key_prefix):
    if topic[section]["expanded"]:
        topic[section]["reference"] = col.text_input("Reference", key=f"{key_prefix}_ref")
        topic[section]["status"] = col.text_input("Status", key=f"{key_prefix}_stat")
        topic[section]["comment"] = col.text_area("Comment", key=f"{key_prefix}_com")
    else:
        if col.button(section, key=f"btn_{key_prefix}"):
            topic[section]["expanded"] = True

# Render rows
for idx, topic in enumerate(st.session_state.topics):
    row_cols = st.columns(col_widths)

    # ID and Type
    row_cols[0].text_input("", value=topic["ID"], key=f"id_{idx}", disabled=True)
    topic["Type"] = row_cols[1].text_input("", value=topic["Type"], key=f"type_{idx}")

    gravity_dropdown(row_cols[2], "Q", topic, f"q_{idx}")
    gravity_dropdown(row_cols[3], "C", topic, f"c_{idx}")
    gravity_dropdown(row_cols[4], "D", topic, f"d_{idx}")
    gravity_dropdown(row_cols[5], "P", topic, f"p_{idx}")

    iss_dropdown(row_cols[6], topic, f"iss_{idx}")
    ecr_dropdown(row_cols[7], topic, f"ecr_{idx}")

    simple_block(row_cols[8], topic, "APQP", f"apqp_{idx}")
    simple_block(row_cols[9], topic, "DEC", f"dec_{idx}")
    simple_block(row_cols[10], topic, "FETE", f"fete_{idx}")

    topic["Desc"] = row_cols[11].text_input("", value=topic["Desc"], key=f"desc_{idx}")
    topic["Status"] = row_cols[12].text_input("", value=topic["Status"], key=f"status_{idx}")
