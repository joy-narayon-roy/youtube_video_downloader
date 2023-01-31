from Functions import Video, Play_list

menu = 2 or input("1. Download Video\n2. Download Playlist.\nEnter menu : ")
'''
input("Enter The Youtube Video Link :")
input("Enter The Youtube Playlist Link :")
'''


def video():
    link = "https://youtu.be/KZDGh6OtAqE"
    yt = Video(link)


def playlist():
    link = "https://youtube.com/playlist?list=PLORBXYLRQHK3mmBOVym4ut5Z_UaKXSqth"
    yt = Play_list(link)
    yt.videos()


# if(menu == "1"):
#     video()
# elif(menu == "2"):
#     playlist()

if __name__ == "__main__":
    playlist()