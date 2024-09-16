import streamlit as st
import os
from MeetingManagement.servies.meeting_service import extract_audio_from_video, get_text_from_audio

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

        get_text_from_audio(os.path.join(VIDEO_DIR, "audio.mp3"))

        if is_audio_available:
            st.success("Video file uploaded successfully")
        else:
            st.warning("Audio is not available in the video file")

    else:
        st.info("Please upload a video file")