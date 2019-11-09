import mysql.connector
from mysql.connector import Error


class Mysql:
    def __init__(self, mysql_user, mysql_password, mysql_database, mysql_host, mysql_port):
        connection = None
        try:
            connection = mysql.connector.connect(host=mysql_host,
                                                 database=mysql_database,
                                                 user=mysql_user,
                                                 password=mysql_password)
        except Error as e:
            raise Exception(e)

        self.connection = connection

    def close_connection(self):
        self.connection.close()

    def insert_tweet(self, id, text):
        query = "INSERT INTO tweet(id, text) VALUES(%s, %s)"

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (id, text))
            self.connection.commit()
        except Error as e:
            raise Exception(e)
        finally:
            cursor.close()
