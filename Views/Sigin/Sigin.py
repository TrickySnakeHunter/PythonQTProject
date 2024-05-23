import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector

class Sigin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('src/qt/sigin_window.ui', self)
        self.SiginButton.clicked.connect(self.register_clicked)

    def register_clicked(self):
        username = self.NameEdit.text()
        if self.PswdEdit.text() == self.PswdEdit2.text():
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

            # Перевірка, чи існує вже користувач з таким же ім'ям користувача
            query = "SELECT * FROM userdolonka WHERE name = %s"
            cursor.execute(query, (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                QMessageBox.warning(self, "Registration Failed", "Username already exists. Please choose a different username.")
            else:
                # Додавання нового користувача до бази даних
                insert_query = "INSERT INTO userdolonka (name, pswd) VALUES (%s, %s)"
                cursor.execute(insert_query, (username, password))
                db_connection.commit()
                QMessageBox.information(self, "Registration Successful", "You have been successfully registered.")
                self.close()  # Закриття вікна реєстрації після успішної реєстрації

            cursor.close()
            db_connection.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to connect to the database: {e}")

