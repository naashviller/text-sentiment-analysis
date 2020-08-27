
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui  # works for pyqt5

import helper
import inference


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(1200, 600)
        self.button = QPushButton('Show sentence polarity', self)
        self.button.move(20, 640)
        self.button.resize(200, 40)
        self.sent_analysator = inference.SentimentAnalysis()
        # connect button to function on_click
        self.button.clicked.connect(self.get_text_sentiment)

        self.button = QPushButton("Load text from file", self)
        self.button.move(20, 700)
        self.button.resize(200, 40)
        self.sent_analysator = inference.SentimentAnalysis()
        # connect button to function on_click
        self.button.clicked.connect(self.openFileDialog)

        self.show()




    def get_text_sentiment(self):
        textboxValue = self.textbox.text()
        print(textboxValue)
        sentiment = self.sent_analysator.make_prediction([textboxValue])
        print(sentiment)
        if sentiment[0] == -1:
            polarity = "negative"
        elif sentiment[0] == 0:
            polarity = "neutral"
        elif sentiment[0] == 1:
            polarity = "positive"
        else:
            polarity = "neutral"

        QMessageBox.question(self, 'Text sentimental', "Text Polarity is " + polarity, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")

    def openFileDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')

        if filename[0]:
            f = open(filename[0], 'r',  encoding='utf-8')

            with f:
                data = f.read()
                self.textbox.setText(data)