#Developed by FRAPS200 (t.me/SickName404)
#GUI made with QT Design.

#Sviluppato da FRAPS200 (t.me/SickName404)
#GUI realizzata con QT Design.


import threading
import psutil
import time
from PyQt5 import QtCore, QtGui, QtWidgets

def cpu_check(self, cpu):
	time.sleep(2)
	_translate = QtCore.QCoreApplication.translate
	self.label.setText(_translate("cpu", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ce5c00;\">CPU STATUS</span></p></body></html>"))
	self.label_2.setText(_translate("cpu", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#008080;\">Loading...</span></p></body></html>"))
	while True:
		time.sleep(1)
		cpustatus = psutil.cpu_percent()
		if float(cpustatus) <= 39.9:
			color = "#4e9a06"
		elif float(cpustatus) <= 69.9:
			color = "DodgerBlue"
		elif float(cpustatus) <= 89.9:
			color = "Tomato"
		self.label_2.setText(_translate("cpu", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:" + color + ";\">" + str(cpustatus) + "%</span></p></body></html>"))


class Ui_cpu(object):
    def setupUi(self, cpu):
        cpu.setObjectName("cpu")
        cpu.resize(402, 181)
        cpu.setFixedSize(402, 181)
        self.label = QtWidgets.QLabel(cpu)
        self.label.setGeometry(QtCore.QRect(10, 40, 371, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(cpu)
        self.label_2.setGeometry(QtCore.QRect(0, 90, 400, 41))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(cpu)
        QtCore.QMetaObject.connectSlotsByName(cpu)



    def retranslateUi(self, cpu):
        _translate = QtCore.QCoreApplication.translate
        cpu.setWindowTitle(_translate("cpu", "CPU Status [by. FRAPS200]"))
        self.label_2.setText(_translate("cpu", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#0000ff;\"></span></p></body></html>"))
        self.label.setText(_translate("cpu", "<html><head/><body><p align=\"center\"><span style=\" font-size:25pt; font-weight:600; color:#0000ff;\">Developed by FRAPS200</span></p></body></html>"))
        threading.Thread(target=cpu_check, args=(self, cpu),).start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cpu = QtWidgets.QDialog()
    ui = Ui_cpu()
    ui.setupUi(cpu)
    cpu.show()
    sys.exit(app.exec_())