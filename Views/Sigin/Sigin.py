import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from Models.DbModel import DbModel
class Sigin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('src/qt/sigin_window.ui', self)
        self.SiginButton.clicked.connect(self.register_clicked)

    def register_clicked(self):
        db=DbModel()
        username = self.NameEdit.text()
        if self.PswdEdit.text() == self.PswdEdit2.text():
            password = self.PswdEdit.text()

            existing_user = db.addUser(username,password)

            QMessageBox.information(self, existing_user["head"], existing_user["body"])
            self.close()  # Закриття вікна реєстрації після успішної реєстрації
            db.closeCon()

