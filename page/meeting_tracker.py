import streamlit as st
import os
from MeetingManagement.servies.meeting_service import extract_audio_from_video, analyze_meeting

# main function to run the streamlit code for meeting tracker page
def run():

    # title and description of the page
    st.header("Video Analyzer")
    st.write("Upload a video file to analyze the meeting and check if all the points are covered or not.")

    VIDEO_DIR = "database/meeting_tracking"

    os.makedirs(VIDEO_DIR, exist_ok = True)

    # upload the video file
    uploaded_file = st.file_uploader(label = 'Upload a video', type=["mp4", "avi", "mov"], label_visibility = 'hidden')

    # check if the video file is uploaded or not
    if uploaded_file is not None:

        ## save the video file to the database
        video_file_path = os.path.join(VIDEO_DIR, uploaded_file.name)

        with open(video_file_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        # extract audio from the video file
        is_audio_available = extract_audio_from_video(video_file_path)

        # check if audio is available in the video file
        if is_audio_available:
            st.success("Video file uploaded successfully")

            clicked = st.button("Analyze Meeting")

            # check if the button is clicked or not
            if clicked:

                # analyze the meeting
                response = analyze_meeting()

                # check if the response is empty or not
                if len(response) == 0:
                    st.markdown(
                        """
                        <div style='background-color:#f8d7da;padding:10px;border-radius:5px;'>
                            <strong style='color:#721c24;'>All the points are covered in the meeting.</strong>
                        </div>
                        """, unsafe_allow_html=True
                    )

                else:
                    st.markdown(
                        """
                        <div style='background-color:#fff3cd;padding:10px;border-radius:5px;'>
                            <strong style='color:#856404;'>The following points are not covered in the meeting:</strong>
                        </div>
                        """, unsafe_allow_html=True
                    )
                    
                    # display the points which are not covered in the meeting
                    for point in response:
                        st.markdown(
                            f"""
                            <div style='background-color:#e2e3e5;padding:10px;margin-top:5px;border-radius:5px;'>
                                <span style='color:#383d41;'>{point}</span>
                            </div>
                            """, unsafe_allow_html=True
                        )
            else:
                st.info("Click on the 'Analyze Meeting' button to analyze the meeting")

        else:
            st.warning("Audio is not available in the video file")

    else:
        st.info("Please upload a video file")