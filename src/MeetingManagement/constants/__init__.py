
import os

DISCUSSION_POINTS_DIR  = 'database/discussion_points'
DOCUMENTS_DIR = 'database/documents'
VIDEO_DIR = "database/meeting_tracking"

AUDIO_FILE_PATH = os.path.join(VIDEO_DIR, "audio.mp3")
DISCUSSION_POINTS_PATH = os.path.join(DISCUSSION_POINTS_DIR, "discussion_points.json")
TRANSCRIPT_PATH = os.path.join(VIDEO_DIR, "transcript.txt")
