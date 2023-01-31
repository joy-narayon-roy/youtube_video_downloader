from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 730)
        MainWindow.setMaximumSize(QtCore.QSize(500, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("background:#fff;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabs = QtWidgets.QTabWidget(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabs.setFont(font)
        self.tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabs.setObjectName("tabs")
        self.video = QtWidgets.QWidget()
        self.video.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.video.setObjectName("video")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.video)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.video)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))

        # Font
        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("text-align:center;""padding:10px 0;")
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.line_4 = QtWidgets.QFrame(self.video)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 10, 0, 10)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.video)

        font = QtGui.QFont()
        font.setFamily("Less")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.input_link = QtWidgets.QLineEdit(self.video)

        font = QtGui.QFont()
        font.setFamily("Less")
        self.input_link.setFont(font)
        self.input_link.setTabletTracking(True)
        self.input_link.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.input_link.setStyleSheet(
            "padding:2px 5px;border:0px;border-bottom:1px solid #ccc;")
        self.input_link.setObjectName("input_link")
        self.horizontalLayout_4.addWidget(self.input_link)
        self.find_btn = QtWidgets.QPushButton(self.video)

        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(10)
        self.find_btn.setFont(font)
        self.find_btn.setStyleSheet("QPushButton{"
                                    "border-radius: 8px;"
                                    "padding:2px 15px;"
                                    "border:1px solid black;"
                                    "text-align:center;"
                                    "}")
        self.find_btn.setObjectName("find_btn")
        self.horizontalLayout_4.addWidget(self.find_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.frame = QtWidgets.QFrame(self.video)
        self.frame.setMinimumSize(QtCore.QSize(0, 200))
        self.frame.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("border:0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self._2 = QtWidgets.QHBoxLayout(self.frame)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(0)
        self._2.setObjectName("_2")
        self.thum_img = QtWidgets.QLabel(self.frame)
        self.thum_img.setMaximumSize(QtCore.QSize(300, 200))
        self.thum_img.setText("")
        # Thum_img
        # self.thum_img.setPixmap(QtGui.QPixmap(":/newPrefix/th.jpg"))
        self.thum_img.setScaledContents(True)
        self.thum_img.setAlignment(QtCore.Qt.AlignCenter)
        self.thum_img.setWordWrap(True)
        self.thum_img.setObjectName("thum_img")
        self._2.addWidget(self.thum_img)
        self.verticalLayout.addWidget(self.frame)


        self.info_table = QtWidgets.QTableWidget(self.video)
        self.info_table.setMaximumSize(QtCore.QSize(16777215, 150))

        font = QtGui.QFont()
        font.setFamily("Less")
        self.info_table.setFont(font)
        self.info_table.setAutoFillBackground(False)
        self.info_table.setStyleSheet("border:0;")
        self.info_table.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.info_table.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.info_table.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.info_table.setAutoScroll(False)
        self.info_table.setAlternatingRowColors(True)
        self.info_table.setShowGrid(True)
        self.info_table.setCornerButtonEnabled(True)
        self.info_table.setObjectName("info_table")
        self.info_table.setColumnCount(2)
        self.info_table.setRowCount(4)

        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("New Column")
        font = QtGui.QFont()
        font.setFamily("Less")
        item.setFont(font)

        self.info_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.info_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.info_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        
        self.info_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setItem(3, 1, item)

        item = QtWidgets.QTableWidgetItem()
        self.info_table.setItem(3, 0, item)
        self.info_table.horizontalHeader().setVisible(False)
        self.info_table.horizontalHeader().setHighlightSections(False)
        self.info_table.horizontalHeader().setStretchLastSection(True)
        self.info_table.verticalHeader().setVisible(False)
        self.info_table.verticalHeader().setHighlightSections(False)
        self.info_table.verticalHeader().setSortIndicatorShown(True)
        self.info_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.info_table)

        self.progressBar_2 = QtWidgets.QProgressBar(self.video)
        self.progressBar_2.setProperty("value",0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout.addWidget(self.progressBar_2)
        self.frame_2 = QtWidgets.QFrame(self.video)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reset_button = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(10)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("QPushButton{width: auto;padding: 10px;border: 1px solid #1d3557;border-radius: 8px;background: #1d3557;color: #fff;}"
                                        "QPushButton:focus{border: 1px solid #1d3557;border-radius: 8px;background: #fff;color: #1d3557;}")
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout.addWidget(self.reset_button)
        self.download_btn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(10)
        self.download_btn.setFont(font)
        self.download_btn.setStyleSheet("QPushButton{width: auto;padding: 10px;border: 1px solid #e63946;border-radius: 8px;background: #e63946;color: #fff;}"
                                        "QPushButton:focus{border: 1px solid #e63946;border-radius: 8px;background: #fff;color: #e63946;}")
        self.download_btn.setObjectName("download_btn")
        self.horizontalLayout.addWidget(self.download_btn)
        self.verticalLayout.addWidget(self.frame_2)
        self.label_7.raise_()
        self.line_4.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.info_table.raise_()
        self.progressBar_2.raise_()
        self.tabs.addTab(self.video, "")
        self.playlist = QtWidgets.QWidget()
        self.playlist.setObjectName("playlist")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.playlist)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_10 = QtWidgets.QLabel(self.playlist)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("text-align:center;""padding:10px 0;")
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.line_5 = QtWidgets.QFrame(self.playlist)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, 0, 10)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.playlist)
        font = QtGui.QFont()
        font.setFamily("Less")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.input_link_2 = QtWidgets.QLineEdit(self.playlist)
        font = QtGui.QFont()
        font.setFamily("Less")
        self.input_link_2.setFont(font)
        self.input_link_2.setTabletTracking(True)
        self.input_link_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.input_link_2.setStyleSheet(
            "padding:2px 5px;border:0px;border-bottom:1px solid #ccc;")
        self.input_link_2.setObjectName("input_link_2")
        self.horizontalLayout_5.addWidget(self.input_link_2)
        self.find_btn_2 = QtWidgets.QPushButton(self.playlist)
        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(10)
        self.find_btn_2.setFont(font)
        self.find_btn_2.setStyleSheet("QPushButton{"
                                      "border-radius: 8px;"
                                      "padding:2px 15px;"
                                      "border:1px solid black;"
                                      "text-align:center;"
                                      "}")
        self.find_btn_2.setObjectName("find_btn_2")
        self.horizontalLayout_5.addWidget(self.find_btn_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.frame_3 = QtWidgets.QFrame(self.playlist)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setStyleSheet("border:0px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self._3 = QtWidgets.QHBoxLayout(self.frame_3)
        self._3.setContentsMargins(0, 0, 0, 0)
        self._3.setSpacing(0)
        self._3.setObjectName("_3")
        self.thum_img_2 = QtWidgets.QLabel(self.frame_3)
        self.thum_img_2.setMaximumSize(QtCore.QSize(300, 200))
        self.thum_img_2.setText("")
        self.thum_img_2.setPixmap(QtGui.QPixmap(":/newPrefix/th.jpg"))
        self.thum_img_2.setScaledContents(True)
        self.thum_img_2.setAlignment(QtCore.Qt.AlignCenter)
        self.thum_img_2.setWordWrap(True)
        self.thum_img_2.setObjectName("thum_img_2")
        self._3.addWidget(self.thum_img_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.info_table_2 = QtWidgets.QTableWidget(self.playlist)
        self.info_table_2.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Less")
        self.info_table_2.setFont(font)
        self.info_table_2.setAutoFillBackground(False)
        self.info_table_2.setStyleSheet("border:0;")
        self.info_table_2.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.info_table_2.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.info_table_2.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.info_table_2.setAutoScroll(False)
        self.info_table_2.setAlternatingRowColors(True)
        self.info_table_2.setShowGrid(True)
        self.info_table_2.setCornerButtonEnabled(True)
        self.info_table_2.setObjectName("info_table_2")
        self.info_table_2.setColumnCount(2)
        self.info_table_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("New Column")
        font = QtGui.QFont()
        font.setFamily("Less")
        item.setFont(font)
        self.info_table_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table_2.setItem(3, 0, item)
        self.info_table_2.horizontalHeader().setVisible(False)
        self.info_table_2.horizontalHeader().setHighlightSections(False)
        self.info_table_2.horizontalHeader().setStretchLastSection(True)
        self.info_table_2.verticalHeader().setVisible(False)
        self.info_table_2.verticalHeader().setHighlightSections(False)
        self.info_table_2.verticalHeader().setSortIndicatorShown(True)
        self.info_table_2.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.info_table_2)
        self.progressBar = QtWidgets.QProgressBar(self.playlist)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_3.addWidget(self.progressBar)
        self.frame_4 = QtWidgets.QFrame(self.playlist)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.reset_button_2 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(10)
        self.reset_button_2.setFont(font)
        self.reset_button_2.setStyleSheet("QPushButton{width: auto;padding: 10px;border: 1px solid #1d3557;border-radius: 8px;background: #1d3557;color: #fff;}"
                                          "QPushButton:focus{border: 1px solid #1d3557;border-radius: 8px;background: #fff;color: #1d3557;}")
        self.reset_button_2.setObjectName("reset_button_2")
        self.horizontalLayout_2.addWidget(self.reset_button_2)
        self.download_btn_2 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Less")
        font.setPointSize(10)
        self.download_btn_2.setFont(font)
        self.download_btn_2.setStyleSheet("QPushButton{width: auto;padding: 10px;border: 1px solid #e63946;border-radius: 8px;background: #e63946;color: #fff;}"
                                          "QPushButton:focus{border: 1px solid #e63946;border-radius: 8px;background: #fff;color: #e63946;}")
        self.download_btn_2.setObjectName("download_btn_2")
        self.horizontalLayout_2.addWidget(self.download_btn_2)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.tabs.addTab(self.playlist, "")
        self.verticalLayout_2.addWidget(self.tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabs.setToolTip(_translate("MainWindow", "Download Single Video"
                                        ""))
        self.label_7.setText(_translate("MainWindow", "Download YoutubeVideo"))
        self.label_8.setText(_translate("MainWindow", "Link "))
        self.input_link.setPlaceholderText(
            _translate("MainWindow", "Enter Your Youtube Link"))
        self.find_btn.setText(_translate("MainWindow", "Enter"))
        self.info_table.setSortingEnabled(False)
        item = self.info_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.info_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.info_table.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.info_table.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.info_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        __sortingEnabled = self.info_table.isSortingEnabled()
        self.info_table.setSortingEnabled(False)
        item = self.info_table.item(0, 0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.info_table.item(0, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.info_table.item(1, 0)
        item.setText(_translate("MainWindow", "Chanel"))
        item = self.info_table.item(1, 1)
        item.setText(_translate("MainWindow", ""))
        item = self.info_table.item(2, 0)
        item.setText(_translate("MainWindow", "Resulution"))
        item = self.info_table.item(3, 0)
        item.setText(_translate("MainWindow", "Save in"))
        self.info_table.setSortingEnabled(__sortingEnabled)
        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.download_btn.setText(_translate("MainWindow", "Download"))
        self.tabs.setTabText(self.tabs.indexOf(self.video),
                             _translate("MainWindow", "Video"))
        self.label_10.setText(_translate(
            "MainWindow", "Download Youtube Play List"))
        self.label_9.setText(_translate("MainWindow", "Link "))
        self.input_link_2.setPlaceholderText(
            _translate("MainWindow", "Enter Your Youtube Link"))
        self.find_btn_2.setText(_translate("MainWindow", "Enter"))
        self.info_table_2.setSortingEnabled(False)
        item = self.info_table_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.info_table_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.info_table_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.info_table_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.info_table_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        __sortingEnabled = self.info_table_2.isSortingEnabled()
        self.info_table_2.setSortingEnabled(False)

        item = self.info_table_2.item(0, 0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.info_table_2.item(0, 1)
        item.setText(_translate("MainWindow", "Something.mp4"))
        item = self.info_table_2.item(1, 0)
        item.setText(_translate("MainWindow", "Chanel"))
        item = self.info_table_2.item(1, 1)
        item.setText(_translate("MainWindow", "Some Thing"))
        item = self.info_table_2.item(2, 0)
        item.setText(_translate("MainWindow", "Resulution"))
        item = self.info_table_2.item(3, 0)
        item.setText(_translate("MainWindow", "Save in"))
        self.info_table_2.setSortingEnabled(__sortingEnabled)
        self.reset_button_2.setText(_translate("MainWindow", "Reset"))
        self.download_btn_2.setText(_translate("MainWindow", "Download"))
        self.tabs.setTabText(self.tabs.indexOf(
            self.playlist), _translate("MainWindow", "Play List"))
