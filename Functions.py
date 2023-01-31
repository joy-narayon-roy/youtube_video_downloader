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


class Video:
    def __init__(self, link):
        self.yt = YouTube(link)
        self.channel = Channel(self.yt.channel_url)


class Play_list:
    def __init__(self, link) -> Playlist:
        self.save_path = "./"
        self.playlist = Playlist(link)
        self.data = {
            "title": self.playlist.title,
            "channel":self.playlist.owner,
            "channel_url":self.playlist.owner_url,
            # "last_updated":self.playlist.last_updated,
            "playlist_url":self.playlist.playlist_url,
            "videos":[]
            # "description":self.playlist.description
        }

        # i = 0
        # for video in self.playlist.videos:
        #     self.data["videos"].append({
        #         "description":video.description
        #     })
        
        # # # print(self.data)
        folder = os.path.exists(f'{self.data["title"]}')
        # f = open("demofile2.txt", "r")
        if folder:
            self.save_path = f'./{self.data["title"]}'
            data_file = open(f"{self.save_path}/demofile2.txt", "w")
        else:
            os.makedirs(self.data["title"])

        print(dir(self.playlist.videos[0]))
        print(folder)

    def videos(self):
        l=0
        # print(dir(self.playlist))
        # print(self.playlist.videos)
        # for video in self.playlist.videos:
        #     pass
        #     print(i, ".", video.title)
        #     i += 1
