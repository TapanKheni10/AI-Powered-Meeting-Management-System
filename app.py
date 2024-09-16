import streamlit as st
from page import home, document_manager, agenda_creation, meeting_tracker

PAGES = {
    "Home": {"page": home, "title": "Home Page", "icon": "🏠"},
    "Document Manager": {"page": document_manager, "title": "Document Manager", "icon": "📂"},
    "Agenda Creator": {"page": agenda_creation, "title": "Agenda Creator", "icon": "📝"},
    "Video Tracking": {"page": meeting_tracker, "title": "Video Tracking", "icon": "📹"},
}

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Home'

def update_page_config(page_name):
    st.set_page_config (
        page_title=PAGES[page_name]['title'],
        page_icon=PAGES[page_name]['icon'],
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'mailto: tapankheni10304@gmail.com',
            'about': 'This is an AI powered meeting management system which helps you to manage your meetings effectively while making the whole process automated and hassle free.'
        }
    )

update_page_config(st.session_state['current_page'])

with st.sidebar:
    st.write('## Navigation')
    selection = st.selectbox('Go to', list(PAGES.keys()), index=list(PAGES.keys()).index(st.session_state['current_page']))

if selection != st.session_state['current_page']:
    st.session_state['current_page'] = selection
    st.experimental_rerun()

page = PAGES[st.session_state['current_page']]['page']
page.run()

