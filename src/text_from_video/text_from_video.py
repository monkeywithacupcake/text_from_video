from moviepy import VideoFileClip
import os
import whisper
import tempfile
import argparse


def get_transcript_from_video(video_path, model_select = "tiny"):
    # prepare to use model
    model = whisper.load_model(model_select)
    try: 
        result = model.transcribe(video_path, verbose=True)  
    except: 
    # we could not get direct from video, so create audio
        with tempfile.TemporaryDirectory() as temp_dir:
            audio_path = os.path.join(temp_dir, "extracted_audio.mp3")
            video = VideoFileClip(video_path)
            video.audio.write_audiofile(audio_path)
            result = model.transcribe(audio_path, verbose=True)
    return(result)

def save_text_to_path(fpath, ftext):
    with open(fpath, "w") as file:
      file.write(ftext)

def get_transcript_save_to_text(the_video_path, the_text_path):
    the_result = get_transcript_from_video(the_video_path, model_select="small")
    transcribed_text = the_result["text"]
    save_text_to_path(fpath = the_text_path, ftext = transcribed_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="text_from_video.")
    parser.add_argument("video_path", type=str, help="Full path to video file")
    parser.add_argument("--text_path", type=str, default="video_transcript.txt", help="Full path to save text")

    args = parser.parse_args()
    get_transcript_save_to_text(args.video_path, args.text_path)