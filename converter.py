import sys
from urllib.request import urlopen

from lxml import etree
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QDoubleSpinBox, QPushButton,
    QVBoxLayout
)


class Course(QObject):
    CBR_URL = 'http://www.cbr.ru/scripts/XML_daily.asp'

    def get(self):
        """
        with urlopen(self.CBR_URL) as r:
            tree = etree.parse(r)
            value = tree.xpath('*[@ID="R01235"]/Value')[0].text
            return float(value.replace(',', '.'))
            """
        return 30


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initSignals()
        self._initLayouts()

    def _initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLabel = QLabel('Сумма в рублях', self)
        self.resultLabel = QLabel('Сумма в долларах', self)

        self.srcAmountEdit = QDoubleSpinBox(self)
        self.srcAmountEdit.setMaximum(999999999)
        self.resultAmountEdit = QDoubleSpinBox(self)
        self.resultAmountEdit.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)
        self.resetBtn = QPushButton('Сброс', self)

    def _initSignals(self):
        self.convertBtn.clicked.connect(self.onClickConvertBtn)
        self.resetBtn.clicked.connect(self.onClickResetBtn)

    def _initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)

        self.mainLayout.addWidget(self.srcLabel)
        self.mainLayout.addWidget(self.srcAmountEdit)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmountEdit)
        self.mainLayout.addWidget(self.convertBtn)
        self.mainLayout.addWidget(self.resetBtn)

        self.setCentralWidget(w)

    def onClickConvertBtn(self):
        RUR = self.srcAmountEdit.value()
        USD = self.resultAmountEdit.value()

        if RUR:
            self.resultAmountEdit.setValue(
                RUR / Course().get()
            )
        else:
            self.srcAmountEdit.setValue(
                USD * Course().get()
            )

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
                self.onClickConvertBtn()

    def onClickResetBtn(self):
        self.srcAmountEdit.setValue(0)
        self.resultAmountEdit.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    converter = MainWindow()
    converter.show()

    sys.exit(app.exec_())
