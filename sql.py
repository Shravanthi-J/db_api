import mysql.connector


class MySql():
    """

    """

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def establishConnection(self):
        """To establist a connection to mySql DataBase """
        try:
            self.con = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
            self.cursor = self.con.cursor()

            self.cursor.execute(f"create database if not exists {self.db}")
            self.cursor.execute(f"use {self.db}")

        except mysql.connector.DatabaseError as e:
            print("There is a problem with sql: ", e)


    def createTable(self,table_name, columns):
        """
        This function used to create a new table
        :param table_name:  table name
        :param columns: column names
        """
        try:
            self.establishConnection()
            self.cursor.execute(f"create table {table_name}({columns})")
        except Exception as e:
            print('Table not created:', e)
        finally:
            self.cursor.close()
            self.con.close()
            #self.cursor.execute(f"create table {table_name}({columns})")


    def insert(self,table_name, data):
        """
        This function is used to insert data into table
        :param table_name: table name
        :param data: data
        """
        try:
            self.establishConnection()
            self.cursor.execute(f"insert into table {table_name} values {data}")
            self.con.commit()
        except Exception as e:
            print('Data not inserted into mysql DB table:', e)

            """
            def bulkInsertion(table_name,data):

                    #Function to insert multiple records or to insert data from a file


                createTable()

            """





