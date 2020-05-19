# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIra.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import cv2
import numpy as np
import os
import sys
import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout

#sys.path.insert(0,'C:/Users/szymo/gitRepo/rehabAssistance/tf-pose-estimation/tf_pose/')
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh



class VideoThread(QThread):
    changePixmapSignal = pyqtSignal(np.ndarray)

    def run(self):
        model = 'mobilenet_thin'
        camera = 0
        """Parsing arguments to networks.py to get model"""
        parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
        parser.add_argument('--camera', type=int, default=0)

        parser.add_argument('--resize', type=str, default='432x368',
                            help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')

        parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')

        parser.add_argument('--model', type=str, default='mobilenet_thin',
                        help='cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small')
        parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')

        parser.add_argument('--tensorrt', type=str, default="False",
                        help='for tensorrt process.')

        args = parser.parse_args()

        cap = cv2.VideoCapture(0)
        w, h = model_wh(args.resize)
        e = TfPoseEstimator(get_graph_path(model), target_size=(w, h))
        while True:
            ret, cvImg = cap.read()
            humans = e.inference(cvImg, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)
            cvImg = TfPoseEstimator.draw_humans(cvImg, humans, imgcopy=False)
            self.changePixmapSignal.emit(cvImg)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._runFlag = False
        self.wait()

    def str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -10, 680, 471))
        self.stackedWidget.setStyleSheet("background-color:black")
        self.stackedWidget.setObjectName("stackedWidget")
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setObjectName("mainPage")
        self.buttonRecord = QtWidgets.QPushButton(self.mainPage)
        self.buttonRecord.setGeometry(QtCore.QRect(20, 240, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.buttonRecord.setFont(font)
        self.buttonRecord.setStyleSheet("background-color:#FFCC00;\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonRecord.setObjectName("buttonRecord")

        self.title = QtWidgets.QLabel(self.mainPage)
        self.title.setGeometry(QtCore.QRect(10, 20, 371, 61))
        self.title.setStyleSheet("color:#FFCC00; font-family: \'Helvetica Neue\', sans-serif; font-size: 30px; font-weight: bold; letter-spacing: -1px; line-height: 1; text-align: center;")
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.mainPage)
        self.label.setGeometry(QtCore.QRect(240, 150, 321, 221))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white; font-family: \'Helvetica Neue\', sans-serif; font-size: 14px; line-height: 24px; margin: 0 0 24px; text-align: justify; text-justify: inter-word; font: bold 14px;")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.buttonTrain = QtWidgets.QPushButton(self.mainPage)
        self.buttonTrain.setGeometry(QtCore.QRect(20, 190, 151, 41))
        self.buttonTrain.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonTrain.setAutoDefault(False)
        self.buttonTrain.setDefault(True)
        self.buttonTrain.setObjectName("buttonTrain")
        self.buttonAuthor = QtWidgets.QPushButton(self.mainPage)
        self.buttonAuthor.setGeometry(QtCore.QRect(20, 290, 151, 41))
        self.buttonAuthor.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonAuthor.setObjectName("buttonAuthor")
        self.label_2 = QtWidgets.QLabel(self.mainPage)
        self.label_2.setGeometry(QtCore.QRect(180, 110, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;font-size: 15px; font-weight: 300; line-height: 32px;font: bold 16px;")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.buttonExit = QtWidgets.QPushButton(self.mainPage)
        self.buttonExit.setGeometry(QtCore.QRect(20, 340, 151, 41))
        self.buttonExit.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonExit.setObjectName("buttonExit")
        self.stackedWidget.addWidget(self.mainPage)
        self.trainInfoPage = QtWidgets.QWidget()
        self.trainInfoPage.setObjectName("trainInfoPage")
        self.labelInfoTrainDescription = QtWidgets.QLabel(self.trainInfoPage)
        self.labelInfoTrainDescription.setGeometry(QtCore.QRect(10, 30, 381, 111))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelInfoTrainDescription.setFont(font)
        self.labelInfoTrainDescription.setStyleSheet("color: white; font-family: \'Helvetica Neue\', sans-serif; font-size: 14px; line-height: 24px; margin: 0 0 24px; text-align: justify; text-justify: inter-word; font: bold 14px;")
        self.labelInfoTrainDescription.setWordWrap(True)
        self.labelInfoTrainDescription.setObjectName("labelInfoTrainDescription")
        self.exerciseInfoList = QtWidgets.QListWidget(self.trainInfoPage)
        self.exerciseInfoList.setGeometry(QtCore.QRect(410, 20, 256, 381))
        self.exerciseInfoList.setStyleSheet("color: white; font-family: \'Helvetica Neue\', sans-serif; font-size: 14px; line-height: 24px; margin: 0 0 24px; text-align: justify; text-justify: inter-word; font: bold 14px;")
        self.exerciseInfoList.setObjectName("exerciseInfoList")
        item = QtWidgets.QListWidgetItem()
        self.exerciseInfoList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exerciseInfoList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exerciseInfoList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exerciseInfoList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.exerciseInfoList.addItem(item)
        self.previewLabel = QtWidgets.QLabel(self.trainInfoPage)
        self.previewLabel.setGeometry(QtCore.QRect(200, 130, 191, 141))
        self.previewLabel.setStyleSheet("color: white; font-family: \'Helvetica Neue\', sans-serif; font-size: 14px; line-height: 24px; margin: 0 0 24px; text-align: justify; text-justify: inter-word; font: bold 14px;")
        self.previewLabel.setWordWrap(True)
        self.previewLabel.setObjectName("previewLabel")
        self.buttonTrainInfoNow = QtWidgets.QPushButton(self.trainInfoPage)
        self.buttonTrainInfoNow.setGeometry(QtCore.QRect(20, 290, 151, 41))
        self.buttonTrainInfoNow.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonTrainInfoNow.setAutoDefault(False)
        self.buttonTrainInfoNow.setDefault(True)
        self.buttonTrainInfoNow.setObjectName("buttonTrainInfoNow")
        self.buttonTrainInfoBack = QtWidgets.QPushButton(self.trainInfoPage)
        self.buttonTrainInfoBack.setGeometry(QtCore.QRect(20, 340, 151, 41))
        self.buttonTrainInfoBack.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonTrainInfoBack.setObjectName("buttonTrainInfoBack")
        self.stackedWidget.addWidget(self.trainInfoPage)
        self.trainPage = QtWidgets.QWidget()
        self.trainPage.setObjectName("trainPage")
        self.buttonTrainStop = QtWidgets.QPushButton(self.trainPage)
        self.buttonTrainStop.setGeometry(QtCore.QRect(20, 240, 151, 41))
        self.buttonTrainStop.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonTrainStop.setObjectName("buttonTrainStop")
        self.buttonTrainFinish = QtWidgets.QPushButton(self.trainPage)
        self.buttonTrainFinish.setGeometry(QtCore.QRect(20, 290, 151, 41))
        self.buttonTrainFinish.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonTrainFinish.setObjectName("buttonTrainFinish")
        self.buttonTrainStart = QtWidgets.QPushButton(self.trainPage)
        self.buttonTrainStart.setGeometry(QtCore.QRect(20, 190, 151, 41))
        self.buttonTrainStart.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonTrainStart.setObjectName("buttonTrainStart")
        self.labelTrain = QtWidgets.QLabel(self.trainPage)
        self.labelTrain.setGeometry(QtCore.QRect(230, 20, 432, 368))
        self.labelTrain.setText("")
        self.labelTrain.setObjectName("labelTrain")
        self.labelTrainName = QtWidgets.QLabel(self.trainPage)
        self.labelTrainName.setGeometry(QtCore.QRect(10, 20, 151, 16))
        self.labelTrainName.setStyleSheet("color:white;font-size: 15px; font-weight: 300; line-height: 32px;font: bold 16px;")
        self.labelTrainName.setObjectName("labelTrainName")
        self.buttonTrainBack = QtWidgets.QPushButton(self.trainPage)
        self.buttonTrainBack.setGeometry(QtCore.QRect(20, 340, 151, 41))
        self.buttonTrainBack.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonTrainBack.setObjectName("buttonTrainBack")
        self.stackedWidget.addWidget(self.trainPage)
        self.recordInfoPage = QtWidgets.QWidget()
        self.recordInfoPage.setObjectName("recordInfoPage")
        self.labelRecordDescription = QtWidgets.QLabel(self.recordInfoPage)
        self.labelRecordDescription.setGeometry(QtCore.QRect(20, 20, 421, 101))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelRecordDescription.setFont(font)
        self.labelRecordDescription.setStyleSheet("color: white; font-family: \'Helvetica Neue\', sans-serif; font-size: 14px; line-height: 24px; margin: 0 0 24px; text-align: justify; text-justify: inter-word; font: bold 14px;")
        self.labelRecordDescription.setWordWrap(True)
        self.labelRecordDescription.setObjectName("labelRecordDescription")
        self.labelRecordName = QtWidgets.QLabel(self.recordInfoPage)
        self.labelRecordName.setGeometry(QtCore.QRect(60, 130, 151, 16))
        self.labelRecordName.setStyleSheet("color:white;font-size: 15px; font-weight: 300; line-height: 32px;font: bold 16px;")
        self.labelRecordName.setObjectName("labelRecordName")
        self.buttonRecordInfoBack = QtWidgets.QPushButton(self.recordInfoPage)
        self.buttonRecordInfoBack.setGeometry(QtCore.QRect(20, 340, 151, 41))
        self.buttonRecordInfoBack.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonRecordInfoBack.setObjectName("buttonRecordInfoBack")
        self.lineDescription = QtWidgets.QLineEdit(self.recordInfoPage)
        self.lineDescription.setGeometry(QtCore.QRect(230, 180, 181, 81))
        self.lineDescription.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.lineDescription.setMaxLength(2000)
        self.lineDescription.setObjectName("lineDescription")
        self.buttonRecordInfoNow = QtWidgets.QPushButton(self.recordInfoPage)
        self.buttonRecordInfoNow.setGeometry(QtCore.QRect(20, 290, 151, 41))
        self.buttonRecordInfoNow.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonRecordInfoNow.setAutoDefault(False)
        self.buttonRecordInfoNow.setDefault(True)
        self.buttonRecordInfoNow.setObjectName("buttonRecordInfoNow")
        self.lineName = QtWidgets.QLineEdit(self.recordInfoPage)
        self.lineName.setGeometry(QtCore.QRect(230, 130, 181, 31))
        self.lineName.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.lineName.setMaxLength(30)
        self.lineName.setObjectName("lineName")
        self.labelInfoRecord = QtWidgets.QLabel(self.recordInfoPage)
        self.labelInfoRecord.setGeometry(QtCore.QRect(60, 180, 151, 16))
        self.labelInfoRecord.setStyleSheet("color:white;font-size: 15px; font-weight: 300; line-height: 32px;font: bold 16px;")
        self.labelInfoRecord.setObjectName("labelInfoRecord")
        self.stackedWidget.addWidget(self.recordInfoPage)
        self.recordPage = QtWidgets.QWidget()
        self.recordPage.setObjectName("recordPage")
        self.buttonRecordFinish = QtWidgets.QPushButton(self.recordPage)
        self.buttonRecordFinish.setGeometry(QtCore.QRect(20, 290, 151, 41))
        self.buttonRecordFinish.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonRecordFinish.setObjectName("buttonRecordFinish")
        self.buttonRecordStop = QtWidgets.QPushButton(self.recordPage)
        self.buttonRecordStop.setGeometry(QtCore.QRect(20, 240, 151, 41))
        self.buttonRecordStop.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonRecordStop.setObjectName("buttonRecordStop")
        self.labelRecord = QtWidgets.QLabel(self.recordPage)
        self.labelRecord.setGeometry(QtCore.QRect(230, 20, 432, 368))
        self.labelRecord.setText("")
        self.labelRecord.setObjectName("labelRecord")
        self.buttonRecordStart = QtWidgets.QPushButton(self.recordPage)
        self.buttonRecordStart.setGeometry(QtCore.QRect(20, 190, 151, 41))
        self.buttonRecordStart.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonRecordStart.setObjectName("buttonRecordStart")
        self.buttonRecordBack = QtWidgets.QPushButton(self.recordPage)
        self.buttonRecordBack.setGeometry(QtCore.QRect(20, 340, 151, 41))
        self.buttonRecordBack.setStyleSheet("background-color:#FFCC00;\n"
"font: 8pt \"Tahoma\";\n"
"color:231900;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"font: bold 14px;\n"
"padding: 6px; \n"
"min-width:10px;\n"
"")
        self.buttonRecordBack.setObjectName("buttonRecordBack")
        self.labelRecordName_2 = QtWidgets.QLabel(self.recordPage)
        self.labelRecordName_2.setGeometry(QtCore.QRect(30, 30, 151, 16))
        self.labelRecordName_2.setStyleSheet("color:white;font-size: 15px; font-weight: 300; line-height: 32px;font: bold 16px;")
        self.labelRecordName_2.setObjectName("labelRecordName_2")
        self.stackedWidget.addWidget(self.recordPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        """Button functions """
        #menuPage
        self.buttonTrain.clicked.connect(self.nextPageTrainInfo)
        self.buttonRecord.clicked.connect(self.nextPageRecordInfo)
        self.buttonExit.clicked.connect(self.exit)
        #trainInfoPage
        self.buttonTrainInfoNow.clicked.connect(self.nextPageTrain)

        self.buttonTrainInfoBack.clicked.connect(self.backPageMenu)
        #trainpage
        self.buttonTrainBack.clicked.connect(self.backPageTrainInfo)

        #recordInfoPage
        self.buttonRecordInfoNow.clicked.connect(self.nextPageRecord)
        self.buttonRecordInfoBack.clicked.connect(self.backPageMenu)
        #trainpage
        self.buttonRecordBack.clicked.connect(self.backPageRecordInfo)

    """Menu"""
    def nextPageRecordInfo(self):
        self.stackedWidget.setCurrentIndex(3)

    def nextPageTrainInfo(self):
        self.stackedWidget.setCurrentIndex(1)

    def exit(self):
        SystemExit

        """Train Info"""
    def nextPageTrain(self):
        self.startRecordingTrain()
        self.stackedWidget.setCurrentIndex(2)

    def backPageMenu(self):
        self.stackedWidget.setCurrentIndex(0)
        """Train"""
    def backPageTrainInfo(self):
        self.stackedWidget.setCurrentIndex(1)

        """record info"""
    def nextPageRecord(self):
        self.startRecordingRecord()
        self.stackedWidget.setCurrentIndex(4)

        """record"""
    def backPageRecordInfo(self):
        self.stackedWidget.setCurrentIndex(3)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RehabAssistance"))
        self.buttonRecord.setText(_translate("MainWindow", "Nagraj ćwiczenie"))
        self.title.setText(_translate("MainWindow", "RehabAssistance"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Program ma na celu pomóc w trudnym procesie rehabilitacji za pomocą wykorzystania technologii (cos dopisac). </p><p>Dzięki pobraniu obrazu z kamery jest on w stanie stwierdzić czy dobrze czy źle wykonywane jest dane ćwiczenie na podstawie wcześniej zapisanych próbek.</p><p>Można również nagrywać nowe ćwiczenia co daje dodatkowe możliwości personalizacji.</p></body></html>"))
        self.buttonTrain.setText(_translate("MainWindow", "Wykonaj ćwiczenie"))
        self.buttonAuthor.setText(_translate("MainWindow", "Autor"))
        self.label_2.setText(_translate("MainWindow", "Streszczenie działania programu"))
        self.buttonExit.setText(_translate("MainWindow", "Wyjście"))
        self.labelInfoTrainDescription.setText(_translate("MainWindow", "<html><head/><body><p>Wybierz ćwiczenie, w oknie obok pojawi się jego opis. Wciśnij wykonaj ćwiczenie stań przed kamerą i ćwicz! </p></body></html>"))
        __sortingEnabled = self.exerciseInfoList.isSortingEnabled()
        self.exerciseInfoList.setSortingEnabled(False)
        item = self.exerciseInfoList.item(0)
        item.setText(_translate("MainWindow", "Ćwiczenie 1"))
        item = self.exerciseInfoList.item(1)
        item.setText(_translate("MainWindow", "Ćwiczenie 2"))
        item = self.exerciseInfoList.item(2)
        item.setText(_translate("MainWindow", "Ćwiczenie 3"))
        item = self.exerciseInfoList.item(3)
        item.setText(_translate("MainWindow", "Ćwiczenie 4"))
        self.exerciseInfoList.setSortingEnabled(__sortingEnabled)
        self.previewLabel.setText(_translate("MainWindow", "Opis ćwiczenia"))
        self.buttonTrainInfoNow.setText(_translate("MainWindow", "Wykonaj ćwiczenie"))
        self.buttonTrainInfoBack.setText(_translate("MainWindow", "Cofnij"))
        self.buttonTrainStop.setText(_translate("MainWindow", "Stop"))
        self.buttonTrainFinish.setText(_translate("MainWindow", "Zakończ i zapisz"))
        self.buttonTrainStart.setText(_translate("MainWindow", "Start"))
        self.labelTrainName.setText(_translate("MainWindow", "Nazwa ćwiczenia"))
        self.buttonTrainBack.setText(_translate("MainWindow", "Cofnij"))
        self.labelRecordDescription.setText(_translate("MainWindow", "<html><head/><body><p>Wypełnij nazwę i opis ćwiczenia następnie wciśnij wykonaj ćwiczenie stań przed kamerą i je wykonaj zostanie ono zapisane do folderu, w którym umieszczona jest aplikacja. </p></body></html>"))
        self.labelRecordName.setText(_translate("MainWindow", "Nazwa ćwiczenia"))
        self.buttonRecordInfoBack.setText(_translate("MainWindow", "Cofnij"))
        self.buttonRecordInfoNow.setText(_translate("MainWindow", "Wykonaj ćwiczenie"))
        self.labelInfoRecord.setText(_translate("MainWindow", "Opis ćwiczenia"))
        self.buttonRecordFinish.setText(_translate("MainWindow", "Zakończ i zapisz"))
        self.buttonRecordStop.setText(_translate("MainWindow", "Stop"))
        self.buttonRecordStart.setText(_translate("MainWindow", "Start"))
        self.buttonRecordBack.setText(_translate("MainWindow", "Cofnij"))
        self.labelRecordName_2.setText(_translate("MainWindow", "Nazwa ćwiczenia"))

    """webcam implementation"""
    def startRecordingRecord(self):
        self.thread = VideoThread()
        self.thread.changePixmapSignal.connect(self.updateImageRecord)
        self.thread.start()

    def startRecordingTrain(self):
        self.thread = VideoThread()
        self.thread.changePixmapSignal.connect(self.updateImageTrain)
        self.thread.start()

    def convertCvQt(self, cvImg):
        """Convert from an opencv image to QPixmap"""
        rgbImage = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB)
        h, w, ch = rgbImage.shape
        bytes_per_line = ch * w
        convertToQt = QtGui.QImage(rgbImage.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convertToQt.scaled(800, 600, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    def updateImageTrain(self, cvImg):
        """Updates the image_label with a new opencv image"""
        qtImg = self.convertCvQt(cvImg)
        self.labelTrain.setPixmap(qtImg)

    def updateImageRecord(self, cvImg):
        """Updates the image_label with a new opencv image"""
        qtImg = self.convertCvQt(cvImg)
        self.labelRecord.setPixmap(qtImg)