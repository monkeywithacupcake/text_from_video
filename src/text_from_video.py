from moviepy import VideoFileClip
import os
import whisper
import tempfile


def get_transcript_from_video(video_path, model_select = "base"):
    # prepare to use model
    model = whisper.load_model(model_select)
    try: 
        result = model.transcribe(video_path)  
    except: 
    # we could not get direct from video, so create audio
        with tempfile.TemporaryDirectory() as temp_dir:
            audio_path = os.path.join(temp_dir, "extracted_audio.mp3")
            video = VideoFileClip(video_path)
            video.audio.write_audiofile(audio_path)
            result = model.transcribe(audio_path)
    return(result)

def save_text_to_path(fpath, ftext):
    with open(fpath, "w") as file:
      file.write(ftext)

def get_transcript_save_to_text(the_video_path, the_text_path):
    the_result = get_transcript_from_video(the_video_path, model_select="tiny")
    transcribed_text = the_result["text"]
    save_text_to_path(fpath = the_text_path, ftext = transcribed_text)