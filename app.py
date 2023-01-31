from PyQt5 import QtWidgets, QtGui
from MainWindow import Ui_MainWindow
from Functions import Downloader
import sys,subprocess,os
import requests

from pytube import Channel


if __name__ == "__main__":

    SAVE_PATH = os.path.join(os.path.expanduser("~"), "Downloads")
    download = Downloader(SAVE_PATH)

    # https://youtu.be/xaSFoi3Vfsc

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # print(dir(ui))
    # Add Functionality
    ui.input_link.setText("https://youtu.be/xaSFoi3Vfsc")
    ui.progressBar.hide()
    ui.progressBar_2.hide()
    # ui.progressBar.hide()

    def find_video():
        vid = download.set_video_link(ui.input_link.text())
        thumbnail_url = vid.thumbnail_url
        image_data = requests.get(thumbnail_url).content
        image = QtGui.QImage.fromData(image_data)
        pixmap = QtGui.QPixmap(image)
        ui.thum_img.setPixmap(pixmap)

        info_name = ui.info_table.item(0,1)
        info_name.setText(vid.title)
        ui.info_table.item(1,1).setText(download.get_channel().channel_name)
        ui.info_table.item(2,1).setText("780p")
        ui.info_table.item(3,1).setText(SAVE_PATH)

        # ui.download_btn.clicked.connect(lambda a:download.download())


    ui.find_btn.clicked.connect(find_video)

    MainWindow.show()
    sys.exit(app.exec_())
