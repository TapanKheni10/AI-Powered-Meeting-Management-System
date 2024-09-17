from moviepy.editor import VideoFileClip
import os
from transformers import pipeline
from MeetingManagement import logger
import soundfile as sf 
from langchain_core.documents import Document
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from uuid import uuid4
import json

## Define the input video file path and output audio file path

def extract_audio_from_video(video_file_path):

    video_clip = VideoFileClip(video_file_path)

    audio_clip = video_clip.audio
    is_audio_available = audio_clip is not None
    
    audio_file_path = os.path.join("database/meeting_tracking", "audio.mp3")

    if is_audio_available:
        audio_clip.write_audiofile(audio_file_path)
        audio_clip.close()  

    video_clip.close()

    return is_audio_available

def get_text_from_audio(audio_file_path):

    transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-small")

    audio_data, sample_rate = sf.read(audio_file_path)

    if len(audio_data.shape) > 1:
        audio_data = audio_data.mean(axis=1)

    transcript = transcriber({"array": audio_data, "sampling_rate": sample_rate})

    text = transcript.get('text', None)

    transcript_path = os.path.join("database/meeting_tracking", "transcript.txt")

    try:
        if text is not None:
            with open(transcript_path, "w") as file:
                file.write(text)

        return text
        
    except Exception as e:
        logger.info("Error in extracting text from audio: ", e)
        raise e
    
def split_document_content(text, words_per_chunk = 50):

    words = text.split()

    text_chunks = []

    for i in range(0, len(text), words_per_chunk):
        text_chunks.append(' '.join(words[i:i+words_per_chunk]))

    documents = [Document(page_content = content) for content in text_chunks]

    return documents


def intialize_vector_stores(documents):
    
    embeddings = HuggingFaceEmbeddings()

    db = Chroma(embedding_function = embeddings)

    uuids = [str(uuid4()) for _ in range(len(documents))]
    db.add_documents(documents)

    return db

def get_undiscussed_point(discussion_point, vector_store):

    undiscussed_point = []

    for point in discussion_point:

        similar_docs = vector_store.similarity_search_with_relevance_scores(point, score_threshold = 0.2)    

        if len(similar_docs) == 0:
            undiscussed_point.append(point)

    return undiscussed_point
    
def analyze_meeting():

    audio_file_path = os.path.join("database/meeting_tracking", "audio.mp3")
    discussion_points_path = "database/discussion_points/discussion_points.json"

    with open(discussion_points_path, "r") as file:
        discussion_points = json.load(file)

    transcript = get_text_from_audio(audio_file_path)

    documents = split_document_content(transcript)

    vector_store = intialize_vector_stores(documents = documents)

    response = get_undiscussed_point(discussion_point = discussion_points, vector_store = vector_store)

    return response



