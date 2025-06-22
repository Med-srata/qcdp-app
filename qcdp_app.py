import streamlit as st
from datetime import datetime

st.set_page_config(page_title="QCDP Tracker", layout="wide")
st.title("📋 QCDP Interactive Table")

# Initialize topics state
if "topics" not in st.session_state:
    st.session_state.topics = []

# Initialize edit states for dynamic columns
editable_cols = ["q", "c", "d", "p", "iss", "ecr", "apqp", "dec", "fete"]
for col in editable_cols:
    st.session_state.setdefault(f"edit_{col}_index", None)

# Add new topic row
if st.button("➕ Add Topic"):
    st.session_state.topics.append({
        "ID": f"T-{len(st.session_state.topics)+1:03}",
        "Type": "",
        "Q": "", "Q_desc": "",
        "C": "", "C_desc": "",
        "D": "", "D_desc": "",
        "P": "", "P_desc": "",
        "ISS": "", "ISS_status": "", "ISS_title": "", "ISS_target": "",
        "ECR_type": "", "ECR_status": "", "ECR_instance": "", "ECR_title": "",
        "ECR_instruction": None, "ECR_conception": None, "ECR_official": None,
        "ECR_start": None, "ECR_solde": None, "ECR_ready": False,
        "APQP_ref": "", "APQP_status": "", "APQP_comment": "",
        "DEC_ref": "", "DEC_status": "", "DEC_comment": "",
        "FETE_ref": "", "FETE_status": "", "FETE_comment": "",
        "Desc": "", "Status": "", "Com": "", "Action": "", "DocInfo": ""
    })

# Dropdown levels for Gravity
gravity_levels = ["", "A", "B", "C"]

# Table headers
headers = ["ID", "Type", "Q", "C", "D", "P", "ISS", "ECR", "APQP", "DEC", "FETE", "Desc", "Status"]
st.columns([1] * len(headers))
for i, label in enumerate(headers):
    st.columns(len(headers))[i].markdown(f"**{label}**")

# Function to handle Q/C/D/P cells
def qcdp_cell(label, prefix, col, i, topic):
    if st.session_state[f"edit_{prefix}_index"] == i:
        topic[label] = col.selectbox("Gravity", gravity_levels, index=gravity_levels.index(topic[label]), key=f"{prefix}_val_{i}")
        topic[f"{label}_desc"] = col.text_input("Impact Description", value=topic[f"{label}_desc"], key=f"{prefix}_desc_{i}")
        if col.button("✅", key=f"{prefix}_save_{i}"):
            st.session_state[f"edit_{prefix}_index"] = None
    else:
        display = f"{topic[label]}: {topic[f'{label}_desc'][:8]}" if topic[label] else label
        if col.button(display, key=f"{prefix}_btn_{i}"):
            st.session_state[f"edit_{prefix}_index"] = i

# Function for short 3-field boxes like APQP, DEC, FETE
def short_edit(prefix, col, i, topic):
    if st.session_state[f"edit_{prefix}_index"] == i:
        topic[f"{prefix}_ref"] = col.text_input("Reference", value=topic[f"{prefix}_ref"], key=f"{prefix}_ref_{i}")
        topic[f"{prefix}_status"] = col.text_input("Status", value=topic[f"{prefix}_status"], key=f"{prefix}_status_{i}")
        topic[f"{prefix}_comment"] = col.text_input("Comment", value=topic[f"{prefix}_comment"], key=f"{prefix}_comment_{i}")
        if col.button("✅", key=f"{prefix}_save_{i}"):
            st.session_state[f"edit_{prefix}_index"] = None
    else:
        s = f"{topic[f'{prefix}_ref']} | {topic[f'{prefix}_status']} | {topic[f'{prefix}_comment']}"
        if col.button(s or prefix.upper(), key=f"{prefix}_btn_{i}"):
            st.session_state[f"edit_{prefix}_index"] = i

# Main table rows
for i, topic in enumerate(st.session_state.topics):
    cols = st.columns(len(headers))
    topic["ID"] = cols[0].text_input("", topic["ID"], key=f"id_{i}", disabled=True)
    topic["Type"] = cols[1].text_input("", topic["Type"], key=f"type_{i}")

    qcdp_cell("Q", "q", cols[2], i, topic)
    qcdp_cell("C", "c", cols[3], i, topic)
    qcdp_cell("D", "d", cols[4], i, topic)
    qcdp_cell("P", "p", cols[5], i, topic)

    # ISS
    if st.session_state.edit_iss_index == i:
        with cols[6]:
            topic["ISS"] = st.selectbox("Gravity", gravity_levels, index=gravity_levels.index(topic["ISS"]), key=f"iss_grav_{i}")
            topic["ISS_status"] = st.text_input("Status", value=topic["ISS_status"], key=f"iss_status_{i}")
            topic["ISS_title"] = st.text_input("Title", value=topic["ISS_title"], key=f"iss_title_{i}")
            topic["ISS_target"] = st.text_input("Target", value=topic["ISS_target"], key=f"iss_target_{i}")
            if st.button("✅", key=f"iss_save_{i}"):
                st.session_state.edit_iss_index = None
    else:
        summary = f"{topic['ISS']} | {topic['ISS_status']}" or "ISS"
        if cols[6].button(summary, key=f"iss_btn_{i}"):
            st.session_state.edit_iss_index = i

    # ECR
    if st.session_state.edit_ecr_index == i:
        with cols[7]:
            topic["ECR_type"] = st.text_input("Type", topic["ECR_type"], key=f"ecr_type_{i}")
            topic["ECR_status"] = st.text_input("Status", topic["ECR_status"], key=f"ecr_status_{i}")
            topic["ECR_instance"] = st.text_input("Instance", topic["ECR_instance"], key=f"ecr_instance_{i}")
            topic["ECR_title"] = st.text_input("Title", topic["ECR_title"], key=f"ecr_title_{i}")
            topic["ECR_instruction"] = st.date_input("Instruction Date", topic["ECR_instruction"] or datetime.today(), key=f"instr_{i}")
            topic["ECR_conception"] = st.date_input("Conception Date", topic["ECR_conception"] or datetime.today(), key=f"concep_{i}")
            topic["ECR_official"] = st.date_input("Officialisation Date", topic["ECR_official"] or datetime.today(), key=f"offic_{i}")
            topic["ECR_start"] = st.date_input("Demarrage Date", topic["ECR_start"] or datetime.today(), key=f"start_{i}")
            topic["ECR_solde"] = st.date_input("Solde Date", topic["ECR_solde"] or datetime.today(), key=f"solde_{i}")
            topic["ECR_ready"] = st.checkbox("Ready", topic["ECR_ready"], key=f"ready_{i}")
            if st.button("✅", key=f"ecr_save_{i}"):
                st.session_state.edit_ecr_index = None
    else:
        s = f"{topic['ECR_type']} | {topic['ECR_status']} | {topic['ECR_instance']}"
        if cols[7].button(s or "ECR", key=f"ecr_btn_{i}"):
            st.session_state.edit_ecr_index = i

    short_edit("apqp", cols[8], i, topic)
    short_edit("dec", cols[9], i, topic)
    short_edit("fete", cols[10], i, topic)

    topic["Desc"] = cols[11].text_input("", topic["Desc"], key=f"desc_{i}")
    topic["Status"] = cols[12].text_input("", topic["Status"], key=f"status_{i}")
