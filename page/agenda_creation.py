from MeetingManagement.servies.agenda_service import agenda_generation
import streamlit as st

# main function to run the streamlit code for agenda creater page
def run():
    
    # title and description of the agenda creater page
    st.header("Agenda Creater")
    st.write("This tool will create an agenda for the meeting based on the discussion points and the documents provided.")

    clicked = st.button("Create Agenda")
    
    # check if the button is clicked or not
    if clicked:

        # calling the agenda_generation function to generate the agenda
        agenda_text = agenda_generation()
        
        st.write("Here is the agenda of the meeting:")
        st.write(agenda_text)
        st.success("Agenda created successfully.")

    else:
        st.info("Please click the button to create the agenda.")

    


    