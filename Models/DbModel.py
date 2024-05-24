import mysql.connector
class DbModel:
    def __init__(self):
        self.db_connection=self.connect()
        
    def connect(self):
        return  mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="dolonka"
            )
        
    def checkUser(self,username,password):
        cursor = self.db_connection.cursor()

            # Перевірка існування користувача в базі даних
        query = "SELECT * FROM userdolonka WHERE name = %s AND pswd = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()
        return user
    def statusUser(self,username,password):
        user=self.checkUser(username,password)
        outMsg={}
        if user:
            outMsg={"head":"Login Successful",
                    "body":f"Welcome {username}"}
        else:
            outMsg={"head":"Login Failed",
                    "body":"Invalid username or password."}
        return outMsg   
    def addUser(self,username,password):
        outMsg={}
        cursor = self.db_connection.cursor()

        
        existing_user = self.checkUser(username,password)

        if existing_user:
            outMsg={"head":"Registration Failed ",
                    "body":"Username already exists. Please choose a different username."}
        else:
                # Додавання нового користувача до бази даних
            insert_query = "INSERT INTO userdolonka (name, pswd) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, password))
            self.db_connection.commit()
            outMsg={"head":"Registration Successful ",
                    "body":f"You:{username} have been successfully registered."}
            cursor.close()
            return outMsg
    
    def closeCon(self):
        self.db_connection.close()