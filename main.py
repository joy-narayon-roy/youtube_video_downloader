import os
from pytube import YouTube


class Youtube_Downloader:
    def __init__(self):
        self.video_url = input(
            "Enter the video URL : ")
        self.download_path = "./Download"

        current_dir = os.getcwd()
        download_folder = os.path.join(current_dir, "Download")
        if not os.path.exists(download_folder):
            os.mkdir(download_folder)
        try:
            self.yt = YouTube(self.video_url, on_complete_callback=self.on_complete_callback,
                              on_progress_callback=self.on_progress_callback)
        except Exception as err:
            print("URL Is Not Valid. Please Insert Youtube video link")
            self.video_url = input("Enter the video URL : ")
            self.yt = YouTube(self.video_url)
        finally:
            print("Loading.....")
            pass

    def on_progress_callback(self, stream, chunk, file_handle):
        print("Downloading....")

    def on_complete_callback(self, stream, path):
        print("Download Compleate.")

    def show_details(self):
        # print(dir(self.yt))
        self.details = f"\tName : {self.yt.title}\n\tChannel : {self.yt.channel_url}\n\tDate : {self.yt.publish_date}\n\tThumbnail : {self.yt.thumbnail_url}"
        print("-"*20, "Details", "-"*20)
        print(self.details)
        self.details = self.details + \
            f"\n\tDescription : {self.yt.description}"
        print("-"*20, "-------", "-"*20, "\n")

    def download_video(self):
        videos = self.yt.streams.filter(progressive=True)
        print("-"*10, "Download Resolution", "-"*10)
        i = 1
        for vid in videos:
            print(
                f"{i}. Download - {vid.resolution} - {(vid.filesize/1048576):0.2f}MB")
            i += 1
        res = int(input("Enter Resolution - "))
        if res > 0 and res <= len(videos):
            print(f"{videos[res-1].resolution} Downloading")
            self.download(videos[res-1])
        else:
            print(f"\nInvalid Input. Please input 1 to {len(videos)}.")
            self.download_video()

    def download_audio(self):
        videos = self.yt.streams.filter(only_audio=True)
        print("-"*10, "Download Size", "-"*10)
        i = 1
        for vid in videos:
            print(f"{i}. Download - {vid.abr} - {(vid.filesize/1048576):0.2f}MB ")
            i += 1
        res = int(input("Enter Resolution - "))
        if res > 0 and res <= len(videos):
            print(f"{videos[res-1].abr} Downloading")
            self.download(videos[res-1])
        else:
            print(f"\nInvalid Input. Please input 1 to {len(videos)}.")
            self.download_video()

    def download(self, file):
        print("Download Start")
        file.download(self.download_path)
        # f = open(f"{self.download_path}/{self.yt.title}.txt", "w")
        # f.write(self.details)
        # f.close()
        # print(dir(file))


def app():
    app = Youtube_Downloader()
    app.show_details()
    try:
        print("-"*10, "Download Type", "-"*10)
        print("  1. Video")
        print("  2. Audio")
        download = int(input("Enter [1/2] : "))
        if download == 1:
            print("Loading...")
            app.download_video()
        elif download == 2:
            print("Loading...")
            app.download_audio()
        else:
            raise Exception("Invalid")
    except KeyboardInterrupt:
        print("Exit")
    except Exception as err:
        print("Invalid Input")
        print(err)


app()
