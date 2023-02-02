from pytube import YouTube, Channel
import os


class Video:
    def __init__(self, link, progress, complete):
        self.yt = YouTube(link, on_progress_callback=progress,
                          on_complete_callback=complete)
        self.channel = Channel(self.yt.channel_url)
        if not os.path.exists(f'./Download'):
            os.makedirs("Download")

    def download_video(self,):
        vid = self.yt.streams.get_highest_resolution()
        vid.download("./Download")
