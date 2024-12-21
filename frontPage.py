from PySide6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem
from PySide6.QtCore import Qt
from PyQt5.QtCore import QUrl
from PySide6.QtGui import QAction, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import os

from music import Ui_Music_App


class MyMainWindow(QMainWindow, Ui_Music_App):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_song_list = []
        self.favorite_songs_list = []
        self.play_list_songs_list = []
        # Remove initial title bar
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # set Initial position of the window
        self.initialPosition = self.pos()

        # Create actions
        self.add_songs_btn.clicked.connect(self.add_songs_func)
        self.play_btn.clicked.connect(self.play_song_func)

        # Add our app moveable properties
        def moveAPP(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() -
                          self.initialPosition)
                self.initialPosition = event.globalPos()
                event.accept()

        self.title_frame.mouseMoveEvent = moveAPP

        # Crate Music Player Plugin
        self.music_player = QMediaPlayer()

    def mousePressEvent(self, event):
        self.initialPosition = event.globalPos()

    # Add songs
    def add_songs_func(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, caption="Add songs", dir=':\\', filter='Supported Files (*.mp3 *.mpeg *.org *.m4a *.MP3 *.wma *.acc *.amr)'
        )
        if files:
            # print(files)

            for file in files:
                # self.loaded_song_listWidget.addItem(file.split('/')[-1])
                self.current_song_list.append(file)

                # Add to favorite songs list
                # favorite_songs_list.append(file)

                # Add to play list list
                # play_list_songs_list.append(file)
                self.loaded_song_listWidget.addItem(
                    QListWidgetItem(
                        QIcon(':/utils/images/MusicListItem.png'),
                        os.path.basename(file)
                    )
                )

    # Play song
    def play_song_func(self):
        # Get the selected song
        try:
            selected_song = self.loaded_song_listWidget.currentRow()
            current_song = self.current_song_list[selected_song]
            song_url = QMediaContent(QUrl.fromLocalFile(current_song))
            self.music_player.setMedia(song_url)
            self.music_player.play()
        except Exception as e:
            print("Play song error: ", e)
