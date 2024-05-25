import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector
from Models.DbModel import DbModel
from Views.Sigin.Sigin import Sigin

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('src/qt/login_window.ui', self)
        self.LoginButton.clicked.connect(self.login_clicked)

    def login_clicked(self):
        username = self.NameEdit.text()
        password = self.PswdEdit.text()

        # Підключення до бази даних MySQL
        try:
            db=DbModel()
            user=db.checkUser(username,password)
            msg=db.statusUser(username,password)

            if user:
                QMessageBox.information(self, msg["head"],msg["body"])
                # Додайте код для відкриття головного вікна програми або виконайте інші дії для авторизованого користувача
            else:
                QMessageBox.warning(self, msg["head"],msg["body"])
                self.NameEdit.clear()
                self.PswdEdit.clear()
                self.open_register_window()
            db.closeCon()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to connect to the database: {e}")

    def open_register_window(self):
        self.register_window = Sigin()
        self.register_window.show()