import streamlit as st
from MeetingManagement.servies.summary_service import get_summary

def run():

    st.header("Summary Generator")

    st.write('This is a summary generator tool that generates a summary of the meeting. You can use this tool to generate a summary of the meeting and share it with your team members who have not attended the meeting.')

    is_clicked = st.button("Get Summary")

    if is_clicked:
        summary_text = get_summary()
        st.write(summary_text)
    else:
        st.info("Click the button to generate the summary.")