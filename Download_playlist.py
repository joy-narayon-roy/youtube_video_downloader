from pytube import YouTube, Playlist
import os

class Play_list:
    def __init__(self, link) -> Playlist:
        # print("Initial Start")
        self.playlist = Playlist(link)
        self.data = {
            "title": self.playlist.title,
            "channel": self.playlist.owner,
            "channel_url": self.playlist.owner_url,
            "playlist_url": self.playlist.playlist_url,
            "folder_files": [],
            "videos": []
        }
        # print("error here")
        self.save_path = f'./Download/{self.data["title"]}'

        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # Get Folder Files Downloaded
        for file in os.listdir(self.save_path):
            self.data["folder_files"].append(file)

        for video in self.playlist.videos:
            self.data["videos"].append({
                "title": video.title.translate(str.maketrans("", "", "\\/:*?\"<>|#,")),
                "download": True,
                "video_url": video.watch_url,
                "exist": False,
            })

        # print("Initial Done")

    def videos(self):
        return self.data

    def download_all_as_video(self, loading, progress, complete):
        files = os.listdir(self.save_path)
        i = 0
        for video in self.data["videos"]:
            i += 1
            file_name = f'{video["title"]}.mp4'
            file_exist = file_name in files
            file_size = 0
            loading(i, video["title"])

            if file_exist:
                file_size = os.path.getsize(
                    f'./{self.save_path}/{file_name}')
                video["exist"] = True

            vid = YouTube(video["video_url"], on_progress_callback=progress, on_complete_callback=complete).streams.filter(
                progressive=True, file_extension='mp4').order_by('resolution').desc().first()

            if file_size == vid.filesize:
                complete(
                    "stream", f'./{self.data["title"]}/{video["title"]}.mp4')
                continue
            elif video["download"]:
                vid.download(self.save_path)

    def download_all_as_audio(self):
        print("Not create")
