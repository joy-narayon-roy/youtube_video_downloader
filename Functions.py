from pytube import YouTube, Playlist, Channel
import os


class Downloader:
    def __init__(self, save_path) -> None:
        self.yt_v = ""
        self.yt_p = ""
        self.path = save_path

    def progress(self, r):
        print('s')
        print(r)

    def done(self, d):
        print(d)

    def set_video_link(self, link):
        self.yt_v = YouTube(link, on_complete_callback=self.done,
                            on_progress_callback=self.progress)
        return self.yt_v

    def set_playlist_link(self, link):
        self.yt_p = Playlist(link)
        return self.yt_p

    def get_channel(self):
        self.channel = Channel(self.yt_v.channel_url)
        return self.channel

    def download(self):
        self.yt_v.streams.filter(progressive=True)[0].download(self.path)
