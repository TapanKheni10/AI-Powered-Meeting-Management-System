import os
from dotenv import load_dotenv

import google.generativeai as genai

from MeetingManagement import logger
from MeetingManagement.constants import TRANSCRIPT_PATH

load_dotenv()

# Configure the API key
genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

# Prompt for the summary generation
prompt = """You are a project manager at a company. You have a meeting with your team to discuss the some of the important points. Now your task is to create a summary to give it to your other team members who haven't attended the meeting. Write a summary based on the transcript given to you. The summary should include the main points like: 
- What was discussed during the meeting.
- Key decisions made during the meeting if it's available directly in the transcript otherwise just avoid it instead of fabricating it.
- Any action items assigned to the team members based on the transcript but if it's not available then leave it.

If any of the above points are not mentioned in the transcript, you are not required to include them in the summary. never give a wrong answer instead say not discussed during the meeting or anything similar to this.
Summary should be concise and clear in a professional manner.

Only include information directly mentioned in the transcript. Do not add any details that weren't explicitly discussed.

Keep the summary concise and focused. It should be informative but not overly long.
Ensure clarity by using bullet points or short paragraphs for easy reading.

format should be like this:
brief summary of the entire meeting.
- relevant text for the brief summary.

key decisions made during the meeting.
- relevant text for the key decisions.

assignment of action items to team members.
- relevant text for the action items.

Here is the transcript: 
"""


def get_summary() -> str:
    """
    Generate a summary of the meeting using the transcript.

    Returns:
        str: Summary of the meeting.
    """

    logger.info("Generating summary of the meeting from the transcript...")

    # Read the transcript from the file
    with open(TRANSCRIPT_PATH, 'r') as file:
        transcript = file.read()

    # Generate the summary using the Gemini Pro model
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(prompt + transcript)

    logger.info("Summary generated successfully.")

    return response.text
    