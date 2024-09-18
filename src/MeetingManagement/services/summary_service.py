import os
from dotenv import load_dotenv

import google.generativeai as genai

from MeetingManagement import logger
from MeetingManagement.constants import TRANSCRIPT_PATH

load_dotenv()

# Configure the API key
genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

# Prompt for the summary generation
prompt = """As a discussion summarizer, your role is to create concise, professional summaries of meetings or discussions for team members who were unable to attend. Follow these guidelines to produce clear and informative summaries:

Summary Content
Include the following main points in your summary:

Overview of topics discussed
Key decisions made (if explicitly stated in the transcript)
Action items assigned to specific team members (if mentioned)

Important Notes
Only include information directly stated in the transcript
If any main points are not covered in the transcript, omit them from the summary
Do not fabricate or infer information not explicitly discussed
If uncertain about a point, indicate it was not clearly addressed in the meeting

Summary Structure
Format your summary as follows:

1) Brief overview of the entire meeting (2-3 sentences)
   Support with relevant quotes or paraphrases from the transcript

2) Key decisions made during the meeting (if any)
   Include supporting evidence from the transcript

3) Action items assigned to team members (if any)
   Provide relevant quotes or paraphrases for each action item


Writing Style
Keep the summary concise and focused
Use clear, professional language
Employ bullet points or short paragraphs for readability
Ensure the summary is informative without being overly detailed

Remember, your goal is to provide an accurate, concise representation of the meeting's content to keep non-attendees informed of important developments and next steps.

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
    