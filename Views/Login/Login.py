import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector

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
            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="dolonka"
            )
            cursor = db_connection.cursor()

            # Перевірка існування користувача в базі даних
            query = "SELECT * FROM userdolonka WHERE name = %s AND pswd = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                QMessageBox.information(self, "Login Successful", "Welcome, " + username)
                # Додайте код для відкриття головного вікна програми або виконайте інші дії для авторизованого користувача
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
                self.NameEdit.clear()
                self.PswdEdit.clear()
                self.open_register_window()
            cursor.close()
            db_connection.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to connect to the database: {e}")

    def open_register_window(self):
        self.register_window = Sigin()
        self.register_window.show()