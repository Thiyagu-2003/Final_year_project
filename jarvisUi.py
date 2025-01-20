from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class JarvisUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jarvis UI")
        self.setFixedSize(984, 572)  # Maintain fixed size
        self.setStyleSheet("background-color: #1e1e1e;")  # Set black background for all widgets
        self.setup_ui()

    def setup_ui(self):
        # Central Widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Background Label
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setStyleSheet("background-color: black;")
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 984, 572))

        # Path Gif Label
        self.pathGifLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathGif = QtGui.QMovie(".\\Material/path.gif")
        self.pathGifLabel.setMovie(self.pathGif)
        self.pathGifLabel.setScaledContents(True)
        self.pathGifLabel.setGeometry(QtCore.QRect(290, 330, 391, 201))

        # Logo Gif Label
        self.logoGifLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoGif = QtGui.QMovie(".\\Material/logo.gif")
        self.logoGifLabel.setMovie(self.logoGif)
        self.logoGifLabel.setScaledContents(True)
        self.logoGifLabel.setGeometry(QtCore.QRect(720, 20, 261, 221))

        # New Gif Label
        self.newGifLabel = QtWidgets.QLabel(self.centralwidget)
        self.newGif = QtGui.QMovie(".\\Material/new.gif")
        self.newGifLabel.setMovie(self.newGif)
        self.newGifLabel.setScaledContents(True)
        self.newGifLabel.setGeometry(QtCore.QRect(10, 10, 411, 301))

        # Buttons
        self.startButton = QtWidgets.QPushButton("Start", self.centralwidget)
        self.startButton.setFont(QtGui.QFont("Segoe Print", 8))
        self.startButton.setStyleSheet("""
            QPushButton {
               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4CAF50, stop: 1 #388E3C);
               border-radius: 5px;
               color: white;
               padding: 8px;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #66BB6A, stop: 1 #43A047);
            }
            QPushButton:pressed {
              background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #388E3C, stop: 1 #2E7D32);
            }
        """)
        self.startButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
        self.startButton.clicked.connect(self.start_button_clicked)

        self.stopButton = QtWidgets.QPushButton("Stop", self.centralwidget)
        self.stopButton.setFont(QtGui.QFont("Verdana", 8))
        self.stopButton.setStyleSheet("""
            QPushButton {
              background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f44336, stop: 1 #d32f2f);
              border-radius: 5px;
              color: white;
              padding: 8px;
            }
            QPushButton:hover {
              background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ef5350, stop: 1 #c62828);
            }
            QPushButton:pressed {
              background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d32f2f, stop: 1 #b71c1c);
            }
        """)
        self.stopButton.setGeometry(QtCore.QRect(840, 510, 81, 31))
        self.stopButton.clicked.connect(self.stop_button_clicked)

    def start_button_clicked(self):
        """Start the main code and play GIFs."""
        self.pathGif.start()
        self.logoGif.start()
        self.newGif.start()
        print("Start button clicked - Main code is running...")

        # Add your main logic here
        # For example, start a thread to run background tasks if needed.

    def stop_button_clicked(self):
        """Exit the application."""
        print("Stop button clicked - Exiting...")
        QtWidgets.QApplication.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Set the style to dark
    app.setStyle("Fusion")
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    jarvis_ui = JarvisUI()
    jarvis_ui.show()
    sys.exit(app.exec_())


# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys

# class JarvisUI(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Jarvis UI")
#         self.setFixedSize(984, 572)  # Maintain fixed size
#         self.setStyleSheet("background-color: rgb(0, 0, 0);")  # Set black background for all widgets
#         self.setup_ui()

#     def setup_ui(self):
#         # Central Widget
#         self.centralwidget = QtWidgets.QWidget(self)
#         self.setCentralWidget(self.centralwidget)

#         # Background Label
#         self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
#         self.backgroundLabel.setStyleSheet("background-color: rgb(0, 0, 0);")
#         self.backgroundLabel.setScaledContents(True)
#         self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 984, 572))

#         # Path Gif Label
#         self.pathGifLabel = QtWidgets.QLabel(self.centralwidget)
#         self.pathGif = QtGui.QMovie(".\\Material/path.gif")
#         self.pathGifLabel.setMovie(self.pathGif)
#         self.pathGifLabel.setScaledContents(True)
#         self.pathGifLabel.setGeometry(QtCore.QRect(290, 330, 391, 201))

#         # Logo Gif Label
#         self.logoGifLabel = QtWidgets.QLabel(self.centralwidget)
#         self.logoGif = QtGui.QMovie(".\\Material/logo.gif")
#         self.logoGifLabel.setMovie(self.logoGif)
#         self.logoGifLabel.setScaledContents(True)
#         self.logoGifLabel.setGeometry(QtCore.QRect(720, 20, 261, 221))

#         # New Gif Label
#         self.newGifLabel = QtWidgets.QLabel(self.centralwidget)
#         self.newGif = QtGui.QMovie(".\\Material/new.gif")
#         self.newGifLabel.setMovie(self.newGif)
#         self.newGifLabel.setScaledContents(True)
#         self.newGifLabel.setGeometry(QtCore.QRect(10, 10, 411, 301))

#         # Text Browser for information
#         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser.setGeometry(QtCore.QRect(0, 510, 191, 41))
#         font = QtGui.QFont()
#         font.setFamily("Sitka Subheading")
#         font.setPointSize(16)
#         self.textBrowser.setFont(font)
#         self.textBrowser.setStyleSheet("background:transparent; border-radius:none;")
#         self.textBrowser.setObjectName("textBrowser")

#         self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         self.textBrowser_2.setFont(font)
#         self.textBrowser_2.setStyleSheet("background:transparent; border-radius:none;")
#         self.textBrowser_2.setObjectName("textBrowser_2")

#         # Buttons
#         self.startButton = QtWidgets.QPushButton("Start", self.centralwidget)
#         self.startButton.setFont(QtGui.QFont("Segoe Print", 8))
#         self.startButton.setStyleSheet("""
#             QPushButton {
#                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4CAF50, stop: 1 #388E3C);
#                border-radius: 5px;
#                color: white;
#                padding: 8px;
#             }
#             QPushButton:hover {
#                 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #66BB6A, stop: 1 #43A047);
#             }
#             QPushButton:pressed {
#               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #388E3C, stop: 1 #2E7D32);
#             }
#         """)
#         self.startButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
#         self.startButton.clicked.connect(self.start_button_clicked)

#         self.stopButton = QtWidgets.QPushButton("Stop", self.centralwidget)
#         self.stopButton.setFont(QtGui.QFont("Verdana", 8))
#         self.stopButton.setStyleSheet("""
#             QPushButton {
#               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f44336, stop: 1 #d32f2f);
#               border-radius: 5px;
#               color: white;
#               padding: 8px;
#             }
#             QPushButton:hover {
#               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ef5350, stop: 1 #c62828);
#             }
#             QPushButton:pressed {
#               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d32f2f, stop: 1 #b71c1c);
#             }
#         """)
#         self.stopButton.setGeometry(QtCore.QRect(840, 510, 81, 31))
#         self.stopButton.clicked.connect(self.stop_button_clicked)

#     def start_button_clicked(self):
#         """Start the main code and play GIFs."""
#         self.pathGif.start()
#         self.logoGif.start()
#         self.newGif.start()
#         print("Start button clicked - Main code is running...")

#         # Add your main logic here
#         # For example, start a thread to run background tasks if needed.

#     def stop_button_clicked(self):
#         """Exit the application."""
#         print("Stop button clicked - Exiting...")
#         QtWidgets.QApplication.quit()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     # Set the style to dark
#     app.setStyle("Fusion")
#     palette = QtGui.QPalette()
#     palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
#     palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
#     palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
#     palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
#     palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
#     palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
#     palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
#     palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
#     palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
#     palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
#     palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
#     palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
#     palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
#     app.setPalette(palette)

#     jarvis_ui = JarvisUI()
#     jarvis_ui.show()
#     sys.exit(app.exec_())
