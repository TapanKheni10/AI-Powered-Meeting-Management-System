from src.MeetingManagement.servies.agenda_creation import create_agenda
import streamlit as st
import os
import json

def run():
    
    st.header("Agenda Creater")
    st.write("This tool will create an agenda for the meeting based on the discussion points and the documents provided.")

    b = st.button("Create Agenda")
    
    if b:
        with open("database/discussion_points/discussion_points.json", 'r') as f:
            discussion_points = json.load(f)

        full_agenda, agenda_items = create_agenda()
        
        st.write("Here is the agenda of the meeting:")
        st.write(full_agenda)
        st.success("Agenda created successfully.")

    else:
        st.warning("Please click the button to create the agenda.")

    


    