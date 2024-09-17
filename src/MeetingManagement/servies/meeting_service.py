from moviepy.editor import VideoFileClip
import os
from transformers import pipeline
from MeetingManagement import logger
import soundfile as sf 

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
        
    except Exception as e:
        logger.info("Error in extracting text from audio: ", e)
        raise e

