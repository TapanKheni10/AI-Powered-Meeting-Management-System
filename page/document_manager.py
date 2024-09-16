import streamlit as st
import os
import json

def run():
    
    DISCUSSION_POINTS_DIR  = 'database/discussion_points'
    DOCUMENTS_DIR = 'database/documents'

    ## check if the directory exists, if not create it
    if not os.path.exists(DISCUSSION_POINTS_DIR):
        os.makedirs(DISCUSSION_POINTS_DIR)
                    
    if not os.path.exists(DOCUMENTS_DIR):
        os.makedirs(DOCUMENTS_DIR)

    def save_uploaded_file(uploaded_file):

        original_file_path = os.path.join(DOCUMENTS_DIR, "original")
        
        if not os.path.exists(original_file_path):
            os.makedirs(original_file_path)
       
        for file in uploaded_file:
            with open(os.path.join(original_file_path, file.name), 'wb') as f:
                f.write(file.getbuffer())
        
        if len(uploaded_file) > 1:
            st.success(f'All of your files uploaded successfully') 
        else:
            st.success(f'Your file uploaded successfully')

    def save_discussion_point(discussion_point):
        discussion_points_list = [point.strip() for point in discussion_point.split('\n')]

        with open(os.path.join(DISCUSSION_POINTS_DIR, 'discussion_points.json'), 'w') as f:
            json.dump(discussion_points_list, f)

        st.success('Discussion points saved successfully')

    st.header('Pre-Meeting Document & Discussion Points Manager')
    st.write("""
    This is the document manager. Here you can upload documents and discussion points.
    """)

    with st.form(key = 'upload_form'):

        uploaded_files = st.file_uploader('Upload Document', type = ['pdf', 'docx', 'txt'], accept_multiple_files = True)

        discussion_points = st.text_area('Enter your discussion points here (Each in new line)', height = 200)

        submitted = st.form_submit_button('Submit')

        if submitted:
            if uploaded_files and discussion_points:
                save_uploaded_file(uploaded_files)

                save_discussion_point(discussion_points)

            else:
                st.warning('Please upload a document and enter discussion points before submitting.')



    


    