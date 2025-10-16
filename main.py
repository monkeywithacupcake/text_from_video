import argparse
import text_from_video.text_from_video as tfv

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="text_from_video.")
    parser.add_argument("video_path", type=str, help="Full path to video file")
    parser.add_argument("--text_path", type=str, default="video_transcript.txt", help="Full path to save text")
    parser.add_argument("--model", type=str, default="tiny", help="whisper model size")

    args = parser.parse_args()
    tfv.get_transcript_save_to_text(args.video_path, args.text_path, args.model)
