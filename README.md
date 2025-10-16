# text_from_video

supply a video file path and get a transcribed text

## How to use

1. know path to video
2. pick a path where you want to save the transcript

```sh
python text_from_video.py "path/to/video.mp4" "path/to/save.txt"
```


## Prerequisites

You may need to install whisper and moviepy

```sh
pip install whisper moviepy
```

This function depends on ffmpeg. On a mac, you can install easily with homebrew.

```sh
brew install ffmpeg
```

