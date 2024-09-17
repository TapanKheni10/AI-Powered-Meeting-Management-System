import streamlit as st

def run():

    st.title("MeetMind AI: Streamline Your Meetings 📝")

    st.header("Optimize Your Meeting Experience", divider = "rainbow")
    st.write("""
    MeetMind helps you streamline the process of managing meetings by organizing pre-meeting documents, generating agendas from key discussion points, and providing a summary of your meeting for easy reference. 
    Our system aims to save time and enhance productivity, ensuring meetings are efficient and well-structured.
    """)

    st.subheader("Key Features")
    st.write("""
    - **Pre-Meeting Document Uploads**: Upload relevant documents in formats like PDF, TXT, and DOCX.
    - **Agenda Creation**: Automatically generate a structured agenda based on uploaded documents and discussion points.
    - **Meeting Recording Analysis**: Analyze meeting recordings to identify covered and uncovered points.
    - **Summary Generation**: Generate concise and professional summaries from meeting video.
    """)

    st.header("How It Works", divider = "rainbow")
    st.write("""
    - **Step 1**: Upload pre-meeting documents and discussion points.
    - **Step 2**: Our system automatically generates a well-organized agenda for the meeting.
    - **Step 3**: Post-meeting, upload the meeting recording for analysis of covered and uncovered discussion points.
    - **Step 4**: Receive a summary highlighting key decisions and action items, if applicable.
    """)

    st.header("Why Use MeetMind?", divider = 'rainbow')
    st.write("""
    - Streamline your meeting process with a simple, easy-to-use interface.
    - Save time by automating agenda creation and meeting analysis.
    - Ensure no discussion points are missed with comprehensive post-meeting reports.
    """)

    st.write("""
    Improve your meeting efficiency with MeetMind. Start optimizing your meetings today! 🚀
    """)

