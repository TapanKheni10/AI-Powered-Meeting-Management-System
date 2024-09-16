from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

# prompt = """You are a project manager at a company. You have a meeting with your team to discuss the some of the important points. you want to create a summary to give it to your other team members who haven't attended the meeting. Write a summary based on the transcript given to you. The summary should include the main points like: 
# - What was discussed.
# - Key decisions made during the meeting.
# - Assigned action items and responsible participants.
# If any of the above points are not mentioned in the transcript, you are not required to include them in the summary. never give a wrong answer.

# Here is the transcript: 
# """

prompt = """You are a summarizer of the discussion / meeting. You are in a discussion with some other people to discuss the some of the important points. you want to create a summary to give it to others who haven't attended the meeting. Write a summary based on the transcript given to you.
Here is the transcript: 
"""

transcript_file_path = "database/meeting_tracking/transcript.txt"

def get_summary():

    with open(transcript_file_path, 'r') as file:
        transcript = file.read()

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(prompt + transcript)

    return response.text
    