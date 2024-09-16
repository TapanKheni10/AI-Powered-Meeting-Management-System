import google.generativeai as genai
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from docx import Document
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
from MeetingManagement import logger

load_dotenv()

genai.configure(api_key = os.getenv('GEMINI_API_KEY'))
genai_model = genai.GenerativeModel('gemini-pro')

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_text_from_documents(document_path_list):

    text = ""

    for file in document_path_list:
        file_path = os.path.join("database/documents", file)

        if file.endswith('.pdf'):
            with open(file_path, 'rb') as f:
                pdf = PdfReader(f)
                for page in pdf.pages:
                    text += page.extract_text() + '\n'
        
        elif file.endswith('.docx'):
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text + '\n'

        elif file.endswith('.txt'):
            with open(file_path, 'r') as f:
                text += f.read()

        else:
            raise ValueError("Unsupported file format")
        
    return text

def create_embeddings(chunk_size=50):

    text = get_text_from_documents(os.listdir("database/documents/original")[1:])

    if not os.path.exists("database/documents/processed"):
        os.makedirs("database/documents/processed")

    with open("database/documents/processed/preprocessed.txt", 'w') as f:
        f.write(text)

    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    embeddings = model.encode(chunks)
    
    return chunks, embeddings

def find_most_similar_text(discussion_point, chunks, embeddings):

    dp_embedding = model.encode([discussion_point])

    similarities = cosine_similarity(dp_embedding, embeddings)[0]

    max_index = np.argmax(similarities)

    return chunks[max_index]   
    
def create_agenda():

    with open("database/discussion_points/discussion_points.json", 'r') as f:
        discussion_points = json.load(f)

    agenda_items = []
    chunks, embeddings = create_embeddings()

    for point in discussion_points:
        relevant_text = find_most_similar_text(point, chunks, embeddings)

        if relevant_text:
            prompt = f"""
            Create an agenda item based on the following discussion point and relevant document excerpts:
            
            Discussion Point: {point}
            
            Relevant Document Excerpts:
            {relevant_text}
            
            Please provide:
            1. A clear title for this agenda item
            2. Key points to be discussed
            """

            response = genai_model.generate_content(prompt)
            agenda_items.append(response.text)

    full_agenda_prompt = f"""
    Create a comprehensive meeting agenda using the following agenda items:
    
    {' '.join(agenda_items)}
    
    Please organize the agenda by linking related topics and provide a streamlined meeting flow.
    Include a brief introduction and conclusion section.
    """

    response = genai_model.generate_content(full_agenda_prompt)

    logger.info(f"Full agenda created successfully.\n")
    logger.info(f"Full agenda: {response.text}\n")
    logger.info(f"Agenda items: {agenda_items}\n")

    return response.text, agenda_items