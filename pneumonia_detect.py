import os
import warnings
from PIL import Image, ImageEnhance
warnings.filterwarnings('ignore')
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np

from keras_preprocessing.image import load_img, img_to_array
from keras.preprocessing import image

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMessageBox
import pyttsx3
#from win32com.client import Dispatch


def speak(str1):
    engine = pyttsx3.init()

    # rate
    #engine.setProperty('rate', 160)

    # voice
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)

    speech= str1
    engine.say(speech)
    engine.runAndWait()
    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 609)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 701, 611))
        self.frame.setStyleSheet("background-color: #035874;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, -60, 541, 561))
        self.label.setText("")
        self.gif=QMovie("picturelungs.gif")
        self.label.setMovie(self.gif)
        self.gif.start()
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 430, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("patient.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
" background-color:#DF582C;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: #7D93E0;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 530, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
" background-color:#DF582C;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
" background-color: #7D93E0;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.upload_image)
        self.pushButton_2.clicked.connect(self.predict_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PNEUMONIA Detection Apps"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/picturelungs.gif\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", " PNEUMONIA Detection"))
        self.pushButton.setText(_translate("MainWindow", "Upload Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Prediction"))


    def upload_image(self):
        filename=QFileDialog.getOpenFileName()
        path=filename[0]
        path=str(path)
        print(path)
        model=load_model('Resnetmodel.h5')
        img_file=load_img(path,target_size=(224,224))
        x=img_to_array(img_file)
        x=np.expand_dims(x, axis=0)
        img_data=preprocess_input(x)
        classes=model.predict(img_data)
        global result
        result=classes

    def predict_result(self):
        print(result)
        if result[0][0]>0.5:
            print("Result is Normal")
            speak("Person Results are Normal")
        else:
            print("Affected By PNEUMONIA")
            speak("Person is Affected By PNEUMONIA")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    # app exit only when window is closed
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()

    #sys.exit(app.exec_())
