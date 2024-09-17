import streamlit as st
import os
from MeetingManagement.servies.meeting_service import extract_audio_from_video, analyze_meeting

def run():

    st.header("Video Tracker Tool")

    VIDEO_DIR = "database/meeting_tracking"

    if not os.path.exists(VIDEO_DIR):
        os.makedirs(VIDEO_DIR)

    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:

        ## save the video file to the database
        video_file_path = os.path.join(VIDEO_DIR, uploaded_file.name)

        with open(video_file_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        is_audio_available = extract_audio_from_video(video_file_path)

        if is_audio_available:
            st.success("Video file uploaded successfully")

            clicked = st.button("Analyze Meeting")

            if clicked:

                response = analyze_meeting()

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