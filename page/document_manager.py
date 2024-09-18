import os
import json
import streamlit as st

from MeetingManagement import logger
from MeetingManagement.constants import DOCUMENTS_DIR, DISCUSSION_POINTS_DIR

# main function to run the streamlit code for document manager page
def run():
    
    # Create directories if they do not exist
    os.makedirs(DOCUMENTS_DIR, exist_ok = True)

    os.makedirs(DISCUSSION_POINTS_DIR, exist_ok = True)

    def save_uploaded_file_and_discussion_points(uploaded_file, discussion_point):
        """
        Save uploaded files and discussion points to specified directories.

        Args:
            uploaded_files (list): List of uploaded file objects.
            discussion_points (str): Discussion points entered by the user.
        """
        logger.info("Document and discussion points saving started")

        # path for saving original uploaded files
        original_file_path = os.path.join(DOCUMENTS_DIR, "original")
        os.makedirs(original_file_path, exist_ok = True)
       
        # save each uploaded file to the designated location
        for file in uploaded_file:
            
            with open(os.path.join(original_file_path, file.name), 'wb') as f:
                f.write(file.getbuffer())

            logger.info(f"Document {file.name} saved successfully")
        
        # notify the user about the files upload status
        if len(uploaded_file) > 1:
            st.success(f'All of your files uploaded successfully') 
        else:
            st.success(f'Your file uploaded successfully')

        # process discussion points and saving as JSON
        discussion_points_list = [point.strip() for point in discussion_point.split('\n')]

        with open(os.path.join(DISCUSSION_POINTS_DIR, 'discussion_points.json'), 'w') as f:
            json.dump(discussion_points_list, f)

        st.success('Discussion points saved successfully')

        logger.info("Document and discussion points saving completed")


    # title and description of the document manager page
    st.header('Pre-Meeting Document & Discussion Points Manager')
    st.write("""
    This is the document manager. Here you can upload documents and discussion points.
    """)

    # creating a form for uploading files and entering discussion points
    with st.form(key = 'upload_form'):

        uploaded_files = st.file_uploader('Upload Document', type = ['pdf', 'docx', 'txt'], accept_multiple_files = True)

        discussion_points = st.text_area('Enter your discussion points here (Each in new line)', height = 200)

        submitted = st.form_submit_button('Submit')

        # Check if the user has uploaded files and entered discussion points before submission
        if submitted:
            if uploaded_files and discussion_points:
                save_uploaded_file_and_discussion_points(uploaded_files, discussion_points)
            else:
                st.warning('Please upload a document and enter discussion points before submitting.')



    


    