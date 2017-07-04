# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from cube import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1136, 895)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 31, 21))
        self.label.setObjectName("label")
        self.openGLWidget =Cube(Form)
        self.openGLWidget.setGeometry(QtCore.QRect(20, 90, 581, 791))
        self.openGLWidget.setObjectName("openGLWidget")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(340, 40, 121, 20))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(504, 40, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(620, 40, 481, 51))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(630, 360, 481, 51))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(630, 560, 481, 51))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(Form)
        self.openGLWidget_2.setGeometry(QtCore.QRect(640, 670, 231, 211))
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.openGLWidget_3 = QtWidgets.QOpenGLWidget(Form)
        self.openGLWidget_3.setGeometry(QtCore.QRect(890, 670, 231, 211))
        self.openGLWidget_3.setObjectName("openGLWidget_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(730, 640, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(980, 640, 56, 12))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "메뉴"))
        self.checkBox.setText(_translate("Form", "Overlap"))
        self.pushButton.setText(_translate("Form", "Update"))
        self.label_2.setText(_translate("Form", "Data Server"))
        self.label_3.setText(_translate("Form", "Volumes"))
        self.label_4.setText(_translate("Form", "DataServer 들의 성능 그래프"))
        self.label_5.setText(_translate("Form", "BW Graph (MB/s)"))
        self.label_6.setText(_translate("Form", "IOPS Graph"))


if __name__ == '__main__':
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

