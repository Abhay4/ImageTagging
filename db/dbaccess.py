import sqlite3

from config import Config

#conn = sqlite3.connect('SQLite_Python.db')
#Todo Need to check how to maintain single instance of DB connection - Need to do

#Todo add logger
#Todo Add authentication
#Todo add unit tests
#Todo error handling - Done


class dbAccess():
    def row_to_dict(self,cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
        data = {}
        for idx, col in enumerate(cursor.description):
            data[col[0]] = row[idx]
        return data

    def __init__(self):
        self.conn = sqlite3.connect(Config.DB_NAME,check_same_thread=False)
        self.conn.row_factory = self.row_to_dict
        #self.cursor = self.conn.cursor()

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     # make sure the dbconnection gets closed
    #     self.conn.close()
    #     self.cursor.close()

    @staticmethod
    def convert_to_binary_data(filename):
        # Convert digital data to binary format
        print(filename)
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def insert_blob(self, id, name, photo):
        try:
            cursor = self.conn.cursor()
            sqlite_insert_blob_query = """ INSERT INTO IMAGE1
                                      (ID, NAME, PHOTO) VALUES (?, ?, ?)"""

            photo = dbAccess.convert_to_binary_data(photo)

            data_tuple = (id, name, photo)
            cursor.execute(sqlite_insert_blob_query, data_tuple)
            self.conn.commit()
            print("Image and file inserted successfully as a BLOB into a table")
            #self.cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
                print("the sqlite connection is closed")

    def get_by_id(self,_id):
        try:
            _id = str(_id)
            cursor = self.conn.cursor()
            print("Connected to SQLite")
            sqlite_get_by_id_query = f"select ID,NAME,tags from image1 where ID='{_id}'"
            print(sqlite_get_by_id_query)
            cursor.execute(sqlite_get_by_id_query)
            res = cursor.fetchall()
            self.conn.commit()
            print("Retrieved item successfully from db")
            cursor.close()
            return res
        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
                print("the sqlite connection is closed")

    def get_all(self):
        try:
            cursor = self.conn.cursor()
            print("Connected to SQLite")
            sqlite_get_all_query = f"select id,name,tags from image1"
            print(sqlite_get_all_query)
            cursor.execute(sqlite_get_all_query)
            res = cursor.fetchall()
            self.conn.commit()
            print("Retrieved item successfully from db")
            return res

        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
                print("the sqlite connection is closed")

    def update_tags(self,_id,tags):
        #get the image if it does not exist - raise an exception
        try:
            cursor = self.conn.cursor()
            update_query = f"update image1 set tags = '{tags}' where ID='{_id}'"
            cursor.execute(update_query)
            get_query = f"select ID,NAME,tags from image1 where ID='{_id}'"
            cursor.execute(get_query)
            res = cursor.fetchall()
            self.conn.commit()
            return res
        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
                print("the sqlite connection is closed")





