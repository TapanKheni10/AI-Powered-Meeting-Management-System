import streamlit as st
from MeetingManagement.servies.summary_service import get_summary

# main function to run the streamlit code for summary generator page
def run():

    # title and description of the page
    st.header("Summary Generator")
    st.write('This is a summary generator tool that generates a summary of the meeting. You can use this tool to generate a summary of the meeting and share it with your team members who have not attended the meeting.')

    is_clicked = st.button("Get Summary")

    # check if the button is clicked or not
    if is_clicked:
        # get the summary of the meeting
        summary_text = get_summary()
        st.write(summary_text)
    else:
        st.info("Click the button to generate the summary.")