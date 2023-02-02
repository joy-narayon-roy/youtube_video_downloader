from Download_playlist import Play_list
from Download_Video import Video

menu = 2 or input("1. Download Video\n2. Download Playlist.\nEnter menu : ")
'''
input("Enter The Youtube Video Link :")
input("Enter The Youtube Playlist Link :")
'''


def progress(stream, chunk, bytes_remaining):
    print("Downloading...", "%.2f" %
          (((stream.filesize-bytes_remaining)/stream.filesize)*100), "%")


def complete(stream, file_path):
    print("Download Compleate.")


def video():
    try:
        link = input("Enter youtube link - ")
        yt = Video(link, progress=progress, complete=complete)

        yt.download_video()
    except Exception as err:
        print("Error")
        print(err)
        video()
    except KeyboardInterrupt:
        print("Exit")
        exit()


def playlist():
    try:
        link = input("Enter Playlsit URL - ")
        yt = Play_list(link)
        videos = yt.videos()
        # print(videos)

        def loading(index, title):
            print(f"\nDownloading - {index}")
            print(index, "-", title)

        yt.download_all_as_video(
            progress=progress, complete=complete, loading=loading)
    except Exception:
        print("Invalid URL")
        playlist()
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    print("-"*20, "Start", "-"*20)
    try:
        menu = int(
            input("1. Download Video\n2. Download Playlist\nEnter menu - "))
        if menu == 1:
            video()
        elif menu == 2:
            playlist()
    except KeyboardInterrupt as key:
        # print(key)
        exit()
