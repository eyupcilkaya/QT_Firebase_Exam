import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame
from PyQt5.uic import loadUi
import read_firebase
import variables


class MainWindow(QMainWindow, QFrame):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)

        self.answer = ""
        self.variablesObject = variables.Variables()
        self.refresh.clicked.connect(self.refreshClicked)
        self.submit.clicked.connect(self.submitClicked)
        self.option_a.clicked.connect(lambda: self.save("a"))
        self.option_b.clicked.connect(lambda: self.save("b"))
        self.option_c.clicked.connect(lambda: self.save("c"))
        self.option_d.clicked.connect(lambda: self.save("d"))
        self.option_e.clicked.connect(lambda: self.save("e"))
        self.widget.setEnabled(False)
        self.show()

    def save(self, answer):
        self.answer = answer

    def submitClicked(self):
        print("submit")
        self.widget.setEnabled(False)
        self.refresh.setEnabled(True)
        read_firebase.writeFirebase(self.answer)
        self.info.setText("BİLGİ: Cevap Gönderildi.")

    def refreshClicked(self):
        self.state = read_firebase.readFirebase(self.variablesObject)
        if self.state == 1:
            self.widget.setEnabled(True)
            self.refresh.setEnabled(False)
            self.clear()
            quest, a, b, c, d, e = self.variablesObject.getQuestion()
            self.question.setText(quest)
            self.option_a.setText(a)
            self.option_b.setText(b)
            self.option_c.setText(c)
            self.option_d.setText(d)
            self.option_e.setText(e)
            self.frame.setStyleSheet(f'background-image : url({"1.jpg"})')
            self.info.setText("BİLGİ: Gönderme işleminden sonra değişiklik yapılamaz.")

        elif self.state == 0:
            self.info.setText("BİLGİ: Henüz soru mevcut değil.")

    def clear(self):
        self.option_a.setAutoExclusive(False)
        self.option_b.setAutoExclusive(False)
        self.option_c.setAutoExclusive(False)
        self.option_d.setAutoExclusive(False)
        self.option_e.setAutoExclusive(False)
        self.option_a.setChecked(False)
        self.option_b.setChecked(False)
        self.option_c.setChecked(False)
        self.option_d.setChecked(False)
        self.option_e.setChecked(False)
        self.option_a.setAutoExclusive(True)
        self.option_b.setAutoExclusive(True)
        self.option_c.setAutoExclusive(True)
        self.option_d.setAutoExclusive(True)
        self.option_e.setAutoExclusive(True)


app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
