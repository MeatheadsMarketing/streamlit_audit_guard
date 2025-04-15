import streamlit as st
import datetime
import importlib.util
import sys
from pathlib import Path

def render_header():
    st.markdown("# Streamlit Audit Guard")
    st.markdown("### Final Validation & Assistant Launch Gateway")
    st.info("Version: v1.3\nLast Updated: " + datetime.datetime.now().strftime("%Y-%m-%d") +
            "\nMaintained By: StreamlitAuditSystem\nStatus: Live")

# Tab names and their corresponding script files
tabs = {
    "Audit Dashboard": "audit_dashboard_all.py",
    "Recovery Tab": "recovery_tab.py",
    "Fix Summary": "fix_summary_tab.py",
    "Deployment Finalizer": "deploy_tab.py",
    "Assistant Explorer": "explorer_tab.py",
    "Validator Checkpoint UI": "validator_tab.py"
}

st.set_page_config(page_title="Streamlit Audit Guard Launcher", layout="wide")
render_header()

# Sidebar navigation
selected_tab = st.sidebar.radio("Select a Module", list(tabs.keys()))

# Dynamic module loading
tab_script = Path(__file__).parent / tabs[selected_tab]
spec = importlib.util.spec_from_file_location(selected_tab, tab_script)
module = importlib.util.module_from_spec(spec)
sys.modules[selected_tab] = module
spec.loader.exec_module(module)

# Run the selected module's `main()` function
if hasattr(module, "main"):
    module.main()
else:
    st.error(f"The script '{tabs[selected_tab]}' does not define a `main()` function.")