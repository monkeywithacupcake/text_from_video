# text_from_video

supply a video file path and get a transcribed text

## How to use

1. fork and clone this repo, cd into this repo `cd text_from_video`
2. `uv sync`
3. many ways to actually use, here are two
    a. locally in your copy of repo using shell

```sh
uv run main.py "path/to/video.mp4" "path/to/save.txt"
```
    b. in a separate python project/folder

```python
import os
import sys

tfv_path = os.path.abspath('/your_path/text_from_video/src/text_from_video') 
sys.path.append(tfv_path)

from text_from_video import get_transcript_save_to_text

this_dir = os.path.dirname(__file__)
this_in_path = os.path.join(this_dir, "your_video_file.mp4")
this_out_path = os.path.join(this_dir, "your_text_choice.txt")

get_transcript_save_to_text(this_in_path, this_out_path)
```



## Prerequisites

1. know path to video
2. pick a path where you want to save the transcript



You may need to install whisper and moviepy

```sh
pip install whisper moviepy
```

This function depends on ffmpeg. On a mac, you can install easily with homebrew.

```sh
brew install ffmpeg
```

