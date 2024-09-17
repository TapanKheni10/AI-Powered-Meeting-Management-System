from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

prompt = """You are a project manager at a company. You have a meeting with your team to discuss the some of the important points. Now your task is to create a summary to give it to your other team members who haven't attended the meeting. Write a summary based on the transcript given to you. The summary should include the main points like: 
- What was discussed during the meeting.
- Key decisions made during the meeting if it's available directly in the transcript otherwise just avoid it instead of fabricating it.
- Any action items assigned to the team members based on the transcript but if it's not available then leave it.

If any of the above points are not mentioned in the transcript, you are not required to include them in the summary. never give a wrong answer.
Summary should be concise and clear in a professional manner.

Only include information directly mentioned in the transcript. Do not add any details that weren't explicitly discussed.

Keep the summary concise and focused. It should be informative but not overly long.
Ensure clarity by using bullet points or short paragraphs for easy reading.

Here is the transcript: 
"""

transcript_file_path = "database/meeting_tracking/transcript.txt"

def get_summary():

    with open(transcript_file_path, 'r') as file:
        transcript = file.read()

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(prompt + transcript)

    return response.text
    