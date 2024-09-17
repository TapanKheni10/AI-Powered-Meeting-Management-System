from MeetingManagement.servies.agenda_service import agenda_generation
import streamlit as st
import os
import json

def run():
    
    st.header("Agenda Creater")
    st.write("This tool will create an agenda for the meeting based on the discussion points and the documents provided.")

    b = st.button("Create Agenda")
    
    if b:
        agenda_text = agenda_generation()
        
        st.write("Here is the agenda of the meeting:")
        st.write(agenda_text)
        st.success("Agenda created successfully.")

    else:
        st.info("Please click the button to create the agenda.")

    


    