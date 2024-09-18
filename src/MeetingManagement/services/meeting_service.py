import os
import json
from uuid import uuid4
from typing import List, Optional

import soundfile as sf 
from transformers import pipeline
from moviepy.editor import VideoFileClip
from langchain_core.documents import Document
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

from MeetingManagement import logger
from MeetingManagement.constants import AUDIO_FILE_PATH, DISCUSSION_POINTS_PATH, TRANSCRIPT_PATH

def extract_audio_from_video(video_file_path) -> bool:
    """
    Extract audio from a video file.

    Args:
        video_file_path (str): Path to the video file.

    Returns:
        bool: True if audio was successfully extracted, False otherwise.
    """

    try:
        logger.info("Extracting audio from video...")
        # Load the video file by creating a VideoFileClip object
        video_clip = VideoFileClip(video_file_path)

        # Extract the audio from the video
        audio_clip = video_clip.audio
        is_audio_available = audio_clip is not None

        # Write the audio to a file
        if is_audio_available:
            audio_clip.write_audiofile(AUDIO_FILE_PATH)
            audio_clip.close()
            video_clip.close()

            return is_audio_available  

        else:
            return is_audio_available
        
        
    except Exception as e:
        logger.error(f"Error extracting audio from video: {e}")
        raise e

def get_transcript_from_audio(audio_file_path) -> Optional[str]:
    """
    Generate transcript from an audio file using Whisper model.

    Args:
        audio_file_path (str): Path to the audio file.

    Returns:
        Optional[str]: Transcribed text if successful, None otherwise.
    """

    try:
        logger.info("Generating transcript from audio...")

        # Load the automatic speech recognition pipeline
        transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-small")
        audio_data, sample_rate = sf.read(audio_file_path)

        # If the audio has multiple channels, take the mean of all channels
        if len(audio_data.shape) > 1:
            audio_data = audio_data.mean(axis=1)

        # Transcribe the audio
        transcript = transcriber({"array": audio_data, "sampling_rate": sample_rate})
        text = transcript.get('text', None)

        # Save the transcript to a file
        if text is not None:
            with open(TRANSCRIPT_PATH, "w") as file:
                file.write(text)
            return text
        
        else:
            logger.warning("Transcript not generated.")
            return None
    
    except Exception as e:
        logger.error(f"Error in extracting text from audio: {e}")
        raise e

def get_documents(text, words_per_chunk = 100):
    """
    Split text into chunks and create Document objects.

    Args:
        text (str): Input text to be split.
        words_per_chunk (int): Number of words per chunk.

    Returns:
        List[Document]: List of Document objects.
    """

    logger.info("Creating Document objects...")

    # Split the text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = words_per_chunk, chunk_overlap = 30)
    text_chunks = text_splitter.split_text(text)

    # Create Document objects from the text chunks
    documents = [Document(page_content = content) for content in text_chunks]

    logger.info(f"Created {len(documents)} Document objects.")

    return documents


def get_vector_store(documents):
    """
    Create a vector store from the given documents.

    Args:
        documents (list): List of Document objects.

    Returns:
        Chroma (object): A Chroma vector store containing the document embeddings.
    """

    logger.info("Creating vector store...")

    # Initialize the Hugging Face embeddings
    embeddings = HuggingFaceEmbeddings()
    # Initialize the Chroma vector store
    chroma_db = Chroma(embedding_function = embeddings)

    # Add the documents to the vector store
    logger.info("Adding documents to the vector store...")
    uuids = [str(uuid4()) for _ in range(len(documents))]
    chroma_db.add_documents(documents, ids = uuids)

    logger.info("Documents added to the vector store.")

    return chroma_db

def get_undiscussed_points(discussion_point, vector_store) -> List[str]:
    """
    Identify undiscussed points based on similarity search.

    Args:
        discussion_points (List[str]): List of discussion points.
        vector_store (Chroma): Vector store containing the meeting transcript document objects.

    Returns:
        List[str]: List of undiscussed points.
    """

    logger.info("Identifying undiscussed points...")

    # Identify undiscussed points
    undiscussed_point = []
    for point in discussion_point:
        related_documents = vector_store.similarity_search_with_relevance_scores(point, score_threshold = 0.1)    

        if len(related_documents) == 0:
            undiscussed_point.append(point)

    logger.info

    return undiscussed_point
    
def analyze_meeting():
    """
    Analyze the meeting by processing audio, generating transcript,
    and identifying undiscussed points.

    Returns:
        List[str]: List of undiscussed points.
    """

    try:
        logger.info("Analyzing meeting...")

        with open(DISCUSSION_POINTS_PATH, "r") as file:
            discussion_points = json.load(file)

        transcript = get_transcript_from_audio(AUDIO_FILE_PATH)
        logger.info("Transcript generated successfully.")

        documents = get_documents(transcript)

        vector_store = get_vector_store(documents = documents)

        response = get_undiscussed_points(discussion_point = discussion_points, vector_store = vector_store)

        return response
    
    except Exception as e:
        logger.error(f"Error in analyzing meeting: {e}")
        raise e



