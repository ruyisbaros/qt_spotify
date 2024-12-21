# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QVBoxLayout, QWidget)
import res_rc

class Ui_Music_App(object):
    def setupUi(self, Music_App):
        if not Music_App.objectName():
            Music_App.setObjectName(u"Music_App")
        Music_App.resize(880, 550)
        Music_App.setMinimumSize(QSize(880, 550))
        Music_App.setMaximumSize(QSize(880, 550))
        icon = QIcon()
        icon.addFile(u":/utils/MusicListItem.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Music_App.setWindowIcon(icon)
        self.actionPlay = QAction(Music_App)
        self.actionPlay.setObjectName(u"actionPlay")
        self.actionPlay.setCheckable(True)
        icon1 = QIcon()
        icon1.addFile(u":/utils/images/pase.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPlay.setIcon(icon1)
        self.actionPause_Unpause = QAction(Music_App)
        self.actionPause_Unpause.setObjectName(u"actionPause_Unpause")
        self.actionPause_Unpause.setCheckable(True)
        icon2 = QIcon()
        icon2.addFile(u":/utils/images/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPause_Unpause.setIcon(icon2)
        self.actionNext = QAction(Music_App)
        self.actionNext.setObjectName(u"actionNext")
        self.actionNext.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/utils/images/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionNext.setIcon(icon3)
        self.actionPrev = QAction(Music_App)
        self.actionPrev.setObjectName(u"actionPrev")
        self.actionPrev.setCheckable(True)
        icon4 = QIcon()
        icon4.addFile(u":/utils/images/pre.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionPrev.setIcon(icon4)
        self.actionStop = QAction(Music_App)
        self.actionStop.setObjectName(u"actionStop")
        self.actionStop.setCheckable(True)
        icon5 = QIcon()
        icon5.addFile(u":/utils/images/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionStop.setIcon(icon5)
        self.Main_body = QWidget(Music_App)
        self.Main_body.setObjectName(u"Main_body")
        self.Main_body.setMinimumSize(QSize(880, 550))
        self.Main_body.setMaximumSize(QSize(880, 550))
        self.bg_Image = QLabel(self.Main_body)
        self.bg_Image.setObjectName(u"bg_Image")
        self.bg_Image.setGeometry(QRect(0, -1, 881, 551))
        self.bg_Image.setPixmap(QPixmap(u"utils/bg_imgs/bg_0002_11.jpg"))
        self.bg_Image.setScaledContents(True)
        self.bg_overlay = QLabel(self.Main_body)
        self.bg_overlay.setObjectName(u"bg_overlay")
        self.bg_overlay.setGeometry(QRect(0, 0, 881, 561))
        self.bg_overlay.setStyleSheet(u"QLabel{\n"
"border:none;\n"
"}")
        self.bg_overlay.setPixmap(QPixmap(u"utils/bg_imgs/bg_overlay.png"))
        self.bg_overlay.setScaledContents(True)
        self.title_frame = QFrame(self.Main_body)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setGeometry(QRect(0, 0, 881, 51))
        self.title_frame.setFrameShape(QFrame.NoFrame)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 41, 31))
        self.label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.label.setPixmap(QPixmap(u":/utils/images/app_icon.png"))
        self.label_2 = QLabel(self.title_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 6, 171, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(79,208,178);\n"
"padding-left:3px;")
        self.minimize_btn = QPushButton(self.title_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setGeometry(QRect(780, 20, 41, 25))
        self.minimize_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,130);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(188, 188, 188);\n"
"border-style:inset;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/utils/images/min.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimize_btn.setIcon(icon6)
        self.minimize_btn.setIconSize(QSize(24, 24))
        self.close_btn = QPushButton(self.title_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(830, 20, 41, 25))
        self.close_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255,255,255,0);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,20,12,200);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,20,12,200);\n"
"border-style:inset;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/utils/images/quit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_btn.setIcon(icon7)
        self.close_btn.setIconSize(QSize(24, 24))
        self.summary_box = QFrame(self.Main_body)
        self.summary_box.setObjectName(u"summary_box")
        self.summary_box.setGeometry(QRect(10, 60, 239, 275))
        self.summary_box.setStyleSheet(u"background-color: rgba(0, 0, 0, 150);\n"
"border-radius:10px;")
        self.summary_box.setFrameShape(QFrame.StyledPanel)
        self.summary_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.summary_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.summary_box)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(31, 21))
        self.label_3.setMaximumSize(QSize(31, 21))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_3.setPixmap(QPixmap(u":/utils/images/current-music.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(79,208,178);\n"
"")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.summary_box)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(191, 31))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(79,208,178);\n"
"")

        self.verticalLayout.addWidget(self.label_5)

        self.current_song_name = QLabel(self.frame_3)
        self.current_song_name.setObjectName(u"current_song_name")
        self.current_song_name.setMaximumSize(QSize(231, 31))
        self.current_song_name.setFont(font1)
        self.current_song_name.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:white;\n"
"")

        self.verticalLayout.addWidget(self.current_song_name)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(91, 31))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:rgb(79,208,178);\n"
"")

        self.verticalLayout.addWidget(self.label_6)

        self.current_song_path = QLabel(self.frame_3)
        self.current_song_path.setObjectName(u"current_song_path")
        self.current_song_path.setMaximumSize(QSize(231, 31))
        self.current_song_path.setFont(font1)
        self.current_song_path.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color:white;\n"
"")

        self.verticalLayout.addWidget(self.current_song_path)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.summary_box)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.add_to_fav_btn = QPushButton(self.frame_4)
        self.add_to_fav_btn.setObjectName(u"add_to_fav_btn")
        self.add_to_fav_btn.setMinimumSize(QSize(0, 27))
        self.add_to_fav_btn.setMaximumSize(QSize(250, 27))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.add_to_fav_btn.setFont(font2)
        self.add_to_fav_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_to_fav_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:rgb(255,140,64)")
        icon8 = QIcon()
        icon8.addFile(u":/utils/images/like.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_to_fav_btn.setIcon(icon8)
        self.add_to_fav_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.add_to_fav_btn)

        self.add_to_playlist_btn = QPushButton(self.frame_4)
        self.add_to_playlist_btn.setObjectName(u"add_to_playlist_btn")
        self.add_to_playlist_btn.setMinimumSize(QSize(0, 27))
        self.add_to_playlist_btn.setMaximumSize(QSize(251, 27))
        self.add_to_playlist_btn.setFont(font2)
        self.add_to_playlist_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_to_playlist_btn.setStyleSheet(u"background-color: rgb(255, 140,64);\n"
"color:rgb(255,255,255);")
        icon9 = QIcon()
        icon9.addFile(u":/utils/images/music_list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_to_playlist_btn.setIcon(icon9)
        self.add_to_playlist_btn.setIconSize(QSize(22, 22))

        self.verticalLayout_2.addWidget(self.add_to_playlist_btn)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.valume_dial = QDial(self.Main_body)
        self.valume_dial.setObjectName(u"valume_dial")
        self.valume_dial.setGeometry(QRect(60, 340, 121, 111))
        self.valume_dial.setCursor(QCursor(Qt.CursorShape.ClosedHandCursor))
        self.valume_dial.setMinimum(1)
        self.valume_dial.setMaximum(100)
        self.valume_dial.setValue(20)
        self.valume_dial.setNotchesVisible(True)
        self.volume_label = QLabel(self.Main_body)
        self.volume_label.setObjectName(u"volume_label")
        self.volume_label.setGeometry(QRect(110, 385, 31, 21))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        self.volume_label.setFont(font3)
        self.volume_label.setAlignment(Qt.AlignCenter)
        self.control_panel_main = QFrame(self.Main_body)
        self.control_panel_main.setObjectName(u"control_panel_main")
        self.control_panel_main.setGeometry(QRect(10, 480, 861, 70))
        self.control_panel_main.setStyleSheet(u"")
        self.control_panel_main.setFrameShape(QFrame.NoFrame)
        self.control_panel_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.control_panel_main)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.music_control = QFrame(self.control_panel_main)
        self.music_control.setObjectName(u"music_control")
        self.music_control.setStyleSheet(u"QFrame{\n"
"border:1px solid gray;\n"
"border-radius:20px;\n"
"}")
        self.music_control.setFrameShape(QFrame.StyledPanel)
        self.music_control.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.music_control)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.play_btn = QPushButton(self.music_control)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setMinimumSize(QSize(35, 30))
        self.play_btn.setMaximumSize(QSize(35, 30))
        self.play_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.play_btn.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,100);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(188, 188, 188);\n"
"border-style:inset;\n"
"}")
        self.play_btn.setIcon(icon1)
        self.play_btn.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.play_btn)

        self.pause_btn = QPushButton(self.music_control)
        self.pause_btn.setObjectName(u"pause_btn")
        self.pause_btn.setMinimumSize(QSize(35, 30))
        self.pause_btn.setMaximumSize(QSize(35, 30))
        self.pause_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pause_btn.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,100);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(188, 188, 188);\n"
"border-style:inset;\n"
"}")
        self.pause_btn.setIcon(icon2)
        self.pause_btn.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.pause_btn)

        self.stop_btn = QPushButton(self.music_control)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setMinimumSize(QSize(35, 30))
        self.stop_btn.setMaximumSize(QSize(35, 30))
        self.stop_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.stop_btn.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,100);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(188, 188, 188);\n"
"border-style:inset;\n"
"}")
        self.stop_btn.setIcon(icon5)
        self.stop_btn.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.stop_btn)

        self.previous_btn = QPushButton(self.music_control)
        self.previous_btn.setObjectName(u"previous_btn")
        self.previous_btn.setMinimumSize(QSize(35, 30))
        self.previous_btn.setMaximumSize(QSize(35, 30))
        self.previous_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.previous_btn.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,100);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(188, 188, 188);\n"
"border-style:inset;\n"
"}")
        self.previous_btn.setIcon(icon4)
        self.previous_btn.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.previous_btn)

        self.next_btn = QPushButton(self.music_control)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(35, 30))
        self.next_btn.setMaximumSize(QSize(35, 30))
        self.next_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.next_btn.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,100);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(188, 188, 188);\n"
"border-style:inset;\n"
"}")
        self.next_btn.setIcon(icon3)
        self.next_btn.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.next_btn)

        self.loop_one_btn = QPushButton(self.music_control)
        self.loop_one_btn.setObjectName(u"loop_one_btn")
        self.loop_one_btn.setMinimumSize(QSize(35, 30))
        self.loop_one_btn.setMaximumSize(QSize(35, 30))
        self.loop_one_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.loop_one_btn.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,100);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(188, 188, 188);\n"
"border-style:inset;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/utils/images/loop-one.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.loop_one_btn.setIcon(icon10)
        self.loop_one_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.loop_one_btn)

        self.shufle_songs_btn = QPushButton(self.music_control)
        self.shufle_songs_btn.setObjectName(u"shufle_songs_btn")
        self.shufle_songs_btn.setMinimumSize(QSize(35, 30))
        self.shufle_songs_btn.setMaximumSize(QSize(35, 30))
        self.shufle_songs_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shufle_songs_btn.setStyleSheet(u"QPushButton{\n"
"background: transparent;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,100);\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(188, 188, 188);\n"
"border-style:inset;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/utils/images/play-random.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shufle_songs_btn.setIcon(icon11)
        self.shufle_songs_btn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.shufle_songs_btn)


        self.horizontalLayout_5.addWidget(self.music_control)

        self.play_control_frame = QFrame(self.control_panel_main)
        self.play_control_frame.setObjectName(u"play_control_frame")
        self.play_control_frame.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.play_control_frame.setFrameShape(QFrame.NoFrame)
        self.play_control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.play_control_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.music_slider = QSlider(self.play_control_frame)
        self.music_slider.setObjectName(u"music_slider")
        self.music_slider.setMinimumSize(QSize(311, 20))
        self.music_slider.setMaximumSize(QSize(311, 20))
        self.music_slider.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.music_slider.setStyleSheet(u"QSlider::groove:horizontal{\n"
"border:1px solid #999999;\n"
"height:15px;\n"
"padding:3px;\n"
"background:rgba(0,255,127,150);\n"
"border-radius:11px;\n"
"margin:2px 0px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal{\n"
"background:rgb(255,200,50);\n"
"border:1px solid #5c5c5c;\n"
"width:18px;\n"
"border-radius:9px;\n"
"margin:-2px 0px;\n"
"}")
        self.music_slider.setMaximum(100)
        self.music_slider.setValue(30)
        self.music_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.music_slider)


        self.horizontalLayout_5.addWidget(self.play_control_frame)

        self.timing_frame = QFrame(self.control_panel_main)
        self.timing_frame.setObjectName(u"timing_frame")
        self.timing_frame.setFrameShape(QFrame.NoFrame)
        self.timing_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.timing_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.time_label = QLabel(self.timing_frame)
        self.time_label.setObjectName(u"time_label")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.time_label.setFont(font4)
        self.time_label.setStyleSheet(u"color:white;")

        self.horizontalLayout_4.addWidget(self.time_label)


        self.horizontalLayout_5.addWidget(self.timing_frame)

        self.stackedWidget = QStackedWidget(self.Main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(270, 60, 601, 301))
        self.stackedWidget.setStyleSheet(u"background-color: rgba(0,0,0,50);\n"
"border-radius:12px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.loaded_song_listWidget = QListWidget(self.page)
        self.loaded_song_listWidget.setObjectName(u"loaded_song_listWidget")
        self.loaded_song_listWidget.setGeometry(QRect(10, 90, 581, 192))
        font5 = QFont()
        font5.setPointSize(15)
        self.loaded_song_listWidget.setFont(font5)
        self.loaded_song_listWidget.setStyleSheet(u"QListWidget{\n"
"color:rgb(86, 227,194);\n"
"selection-background-color: rgb(255, 140, 64);\n"
"selection-color: #fff;\n"
"background-color:rgba(0,0,0,100);\n"
"padding:10px;\n"
"}")
        self.loaded_song_listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 591, 66))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(151, 41))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color:#fff;\n"
"text-align:center;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.add_songs_btn = QPushButton(self.frame_5)
        self.add_songs_btn.setObjectName(u"add_songs_btn")
        self.add_songs_btn.setMinimumSize(QSize(30, 30))
        self.add_songs_btn.setMaximumSize(QSize(30, 30))
        self.add_songs_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_songs_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
"border-radius:5px;\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/utils/images/addFromLocal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_songs_btn.setIcon(icon12)
        self.add_songs_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.add_songs_btn)

        self.deleteselected_btn = QPushButton(self.frame_5)
        self.deleteselected_btn.setObjectName(u"deleteselected_btn")
        self.deleteselected_btn.setMinimumSize(QSize(30, 30))
        self.deleteselected_btn.setMaximumSize(QSize(30, 30))
        self.deleteselected_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.deleteselected_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
"border-radius:5px;\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/utils/images/clear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteselected_btn.setIcon(icon13)
        self.deleteselected_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.deleteselected_btn)

        self.delete_all_songs_btn = QPushButton(self.frame_5)
        self.delete_all_songs_btn.setObjectName(u"delete_all_songs_btn")
        self.delete_all_songs_btn.setMinimumSize(QSize(30, 30))
        self.delete_all_songs_btn.setMaximumSize(QSize(30, 30))
        self.delete_all_songs_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_all_songs_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
"border-radius:5px;\n"
"}\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/utils/images/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_all_songs_btn.setIcon(icon14)
        self.delete_all_songs_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.delete_all_songs_btn)


        self.horizontalLayout_7.addWidget(self.frame_5, 0, Qt.AlignRight)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 10, 591, 66))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(151, 41))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color:#fff;\n"
"text-align:center;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(200, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.add_songs_btn_2 = QPushButton(self.frame_8)
        self.add_songs_btn_2.setObjectName(u"add_songs_btn_2")
        self.add_songs_btn_2.setMinimumSize(QSize(120, 30))
        self.add_songs_btn_2.setMaximumSize(QSize(120, 30))
        self.add_songs_btn_2.setFont(font2)
        self.add_songs_btn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.add_songs_btn_2.setStyleSheet(u"QPushButton{\n"
"background-color:#55ff7f;\n"
"border-radius:8px;\n"
"}\n"
"")
        self.add_songs_btn_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.add_songs_btn_2)


        self.horizontalLayout_9.addWidget(self.frame_8, 0, Qt.AlignRight)

        self.play_list_listWidget = QListWidget(self.page_2)
        self.play_list_listWidget.setObjectName(u"play_list_listWidget")
        self.play_list_listWidget.setGeometry(QRect(10, 90, 591, 192))
        self.play_list_listWidget.setFont(font5)
        self.play_list_listWidget.setStyleSheet(u"QListWidget{\n"
"color:rgb(86, 227,194);\n"
"selection-background-color: rgb(255, 140, 64);\n"
"selection-color: #fff;\n"
"background-color:rgba(0,0,0,100);\n"
"padding:10px;\n"
"}")
        self.play_list_listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.frame_9 = QFrame(self.page_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 10, 591, 66))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(151, 41))
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color:#fff;\n"
"text-align:center;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_9)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(100, 0))
        self.frame_10.setMaximumSize(QSize(100, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.delete_a_favorite_btn = QPushButton(self.frame_10)
        self.delete_a_favorite_btn.setObjectName(u"delete_a_favorite_btn")
        self.delete_a_favorite_btn.setMinimumSize(QSize(30, 30))
        self.delete_a_favorite_btn.setMaximumSize(QSize(30, 30))
        self.delete_a_favorite_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_a_favorite_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
"border-radius:5px;\n"
"}\n"
"")
        self.delete_a_favorite_btn.setIcon(icon13)
        self.delete_a_favorite_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.delete_a_favorite_btn)

        self.delete_all_fav_btn = QPushButton(self.frame_10)
        self.delete_all_fav_btn.setObjectName(u"delete_all_fav_btn")
        self.delete_all_fav_btn.setMinimumSize(QSize(30, 30))
        self.delete_all_fav_btn.setMaximumSize(QSize(30, 30))
        self.delete_all_fav_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.delete_all_fav_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#fff;\n"
"border-radius:5px;\n"
"}\n"
"")
        self.delete_all_fav_btn.setIcon(icon14)
        self.delete_all_fav_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.delete_all_fav_btn)


        self.horizontalLayout_11.addWidget(self.frame_10, 0, Qt.AlignRight)

        self.loaded_song_listWidget_2 = QListWidget(self.page_3)
        self.loaded_song_listWidget_2.setObjectName(u"loaded_song_listWidget_2")
        self.loaded_song_listWidget_2.setGeometry(QRect(10, 90, 581, 192))
        self.loaded_song_listWidget_2.setFont(font5)
        self.loaded_song_listWidget_2.setStyleSheet(u"QListWidget{\n"
"color:rgb(86, 227,194);\n"
"selection-background-color: rgb(255, 140, 64);\n"
"selection-color: #fff;\n"
"background-color:rgba(0,0,0,100);\n"
"padding:10px;\n"
"}")
        self.loaded_song_listWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.stackedWidget.addWidget(self.page_3)
        self.frame_6 = QFrame(self.Main_body)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(270, 380, 601, 61))
        self.frame_6.setStyleSheet(u"border-radius:5px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.song_list_btn = QPushButton(self.frame_6)
        self.song_list_btn.setObjectName(u"song_list_btn")
        self.song_list_btn.setMaximumSize(QSize(161, 30))
        self.song_list_btn.setFont(font2)
        self.song_list_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.song_list_btn.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"border-radius:10px;\n"
"color:#222;")

        self.horizontalLayout_8.addWidget(self.song_list_btn)

        self.play_list_btn = QPushButton(self.frame_6)
        self.play_list_btn.setObjectName(u"play_list_btn")
        self.play_list_btn.setMinimumSize(QSize(161, 30))
        self.play_list_btn.setMaximumSize(QSize(161, 30))
        self.play_list_btn.setFont(font2)
        self.play_list_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.play_list_btn.setStyleSheet(u"background-color: rgb(79,208,178);\n"
"border-radius:10px;\n"
"color:#222;")

        self.horizontalLayout_8.addWidget(self.play_list_btn)

        self.favorite_btn = QPushButton(self.frame_6)
        self.favorite_btn.setObjectName(u"favorite_btn")
        self.favorite_btn.setMinimumSize(QSize(161, 30))
        self.favorite_btn.setMaximumSize(QSize(161, 30))
        self.favorite_btn.setFont(font2)
        self.favorite_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.favorite_btn.setStyleSheet(u"background-color: rgb(255, 140, 64);\n"
"border-radius:10px;\n"
"color:#222;")

        self.horizontalLayout_8.addWidget(self.favorite_btn)

        Music_App.setCentralWidget(self.Main_body)
        self.bg_Image.raise_()
        self.bg_overlay.raise_()
        self.summary_box.raise_()
        self.valume_dial.raise_()
        self.volume_label.raise_()
        self.control_panel_main.raise_()
        self.title_frame.raise_()
        self.stackedWidget.raise_()
        self.frame_6.raise_()

        self.retranslateUi(Music_App)
        self.close_btn.clicked.connect(Music_App.close)
        self.minimize_btn.clicked.connect(Music_App.showMinimized)
        self.valume_dial.sliderMoved.connect(self.volume_label.setNum)

        QMetaObject.connectSlotsByName(Music_App)
    # setupUi

    def retranslateUi(self, Music_App):
        Music_App.setWindowTitle(QCoreApplication.translate("Music_App", u"Spotify_Clone", None))
        self.actionPlay.setText(QCoreApplication.translate("Music_App", u"Play", None))
        self.actionPause_Unpause.setText(QCoreApplication.translate("Music_App", u"Pause/Unpause", None))
        self.actionNext.setText(QCoreApplication.translate("Music_App", u"Next", None))
        self.actionPrev.setText(QCoreApplication.translate("Music_App", u"Prev", None))
        self.actionStop.setText(QCoreApplication.translate("Music_App", u"Stop", None))
        self.bg_Image.setText("")
        self.bg_overlay.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Music_App", u"Spotify", None))
        self.minimize_btn.setText("")
        self.close_btn.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Music_App", u"Currently Playing", None))
        self.label_5.setText(QCoreApplication.translate("Music_App", u"Name", None))
        self.current_song_name.setText(QCoreApplication.translate("Music_App", u"Song name here", None))
        self.label_6.setText(QCoreApplication.translate("Music_App", u"Path", None))
        self.current_song_path.setText(QCoreApplication.translate("Music_App", u"Song Path here", None))
        self.add_to_fav_btn.setText(QCoreApplication.translate("Music_App", u"  Add to Favorite", None))
        self.add_to_playlist_btn.setText(QCoreApplication.translate("Music_App", u"  Add to Favorite", None))
        self.volume_label.setText(QCoreApplication.translate("Music_App", u"20", None))
#if QT_CONFIG(tooltip)
        self.play_btn.setToolTip(QCoreApplication.translate("Music_App", u"play", None))
#endif // QT_CONFIG(tooltip)
        self.play_btn.setText("")
#if QT_CONFIG(tooltip)
        self.pause_btn.setToolTip(QCoreApplication.translate("Music_App", u"pause", None))
#endif // QT_CONFIG(tooltip)
        self.pause_btn.setText("")
#if QT_CONFIG(tooltip)
        self.stop_btn.setToolTip(QCoreApplication.translate("Music_App", u"stop", None))
#endif // QT_CONFIG(tooltip)
        self.stop_btn.setText("")
#if QT_CONFIG(tooltip)
        self.previous_btn.setToolTip(QCoreApplication.translate("Music_App", u"prev", None))
#endif // QT_CONFIG(tooltip)
        self.previous_btn.setText("")
#if QT_CONFIG(tooltip)
        self.next_btn.setToolTip(QCoreApplication.translate("Music_App", u"next", None))
#endif // QT_CONFIG(tooltip)
        self.next_btn.setText("")
#if QT_CONFIG(tooltip)
        self.loop_one_btn.setToolTip(QCoreApplication.translate("Music_App", u"loop", None))
#endif // QT_CONFIG(tooltip)
        self.loop_one_btn.setText("")
#if QT_CONFIG(tooltip)
        self.shufle_songs_btn.setToolTip(QCoreApplication.translate("Music_App", u"shuffle", None))
#endif // QT_CONFIG(tooltip)
        self.shufle_songs_btn.setText("")
        self.time_label.setText(QCoreApplication.translate("Music_App", u"00:00:00/00:00:00", None))
        self.label_7.setText(QCoreApplication.translate("Music_App", u"Song List", None))
        self.add_songs_btn.setText("")
        self.deleteselected_btn.setText("")
        self.delete_all_songs_btn.setText("")
        self.label_8.setText(QCoreApplication.translate("Music_App", u"Playlist", None))
        self.add_songs_btn_2.setText(QCoreApplication.translate("Music_App", u"Load Selected", None))
        self.label_9.setText(QCoreApplication.translate("Music_App", u"Favorites", None))
        self.delete_a_favorite_btn.setText("")
        self.delete_all_fav_btn.setText("")
        self.song_list_btn.setText(QCoreApplication.translate("Music_App", u"Song List", None))
        self.play_list_btn.setText(QCoreApplication.translate("Music_App", u"Play List", None))
        self.favorite_btn.setText(QCoreApplication.translate("Music_App", u"Favorite", None))
    # retranslateUi

