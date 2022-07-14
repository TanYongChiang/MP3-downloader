from pytube import YouTube
import os
from moviepy.editor import *

#ask for the link from user
links = ["https://www.youtube.com/watch?v=ozH28qYrMy4",
"https://www.youtube.com/watch?v=wZGLkYVwcCs"]

for link in links:
    yt = YouTube(link)
    ys = yt.streams.get_audio_only()
    out_file = ys.download()

    base, ext = os.path.splitext(out_file)
    # new_file = base + '.mp3'
    # os.rename(out_file, new_file)

    def mp4_to_mp3(mp4, mp3):     
        mp4_without_frames = AudioFileClip(mp4)
        mp4_without_frames.write_audiofile(mp3)
        mp4_without_frames.close() # function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3")

    mp4_to_mp3(f"{base}.mp4", f"{base}.mp3")

    print("Downloaded {} [{}], from link {}".format(yt.title,yt.length,link))

    os.remove(f"{base}.mp4")