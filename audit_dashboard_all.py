import streamlit as st
import pandas as pd

def main():
    st.title("Audit Dashboard")

    # Sample audit data simulation (can be replaced with real loading logic)
    audit_data = [
        {"Assistant": "A001", "Status": "PASS", "Runtime OK": True},
        {"Assistant": "A002", "Status": "FAIL", "Runtime OK": False},
    ]

    st.markdown("### Audit Results")
    st.dataframe(audit_data)

    if st.sidebar.button("Export as CSV"):
        df = pd.DataFrame(audit_data)
        df.to_csv("audit_summary_export.csv", index=False)
        st.success("Exported audit summary to audit_summary_export.csv")

    st.markdown("### Notes")
    st.write("This dashboard is running inside StreamlitAuditGuard.")

if __name__ == "__main__":
    main()