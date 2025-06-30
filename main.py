from pynput import keyboard
import pyautogui
import threading
import time
import random

spamming = False


def bow_spam_loop(iterations=None):
    count = 0
    while True:
        if spamming:
            charge_time = random.uniform(0.005, 0.01)         # Random bow hold (charge) time
            delay_between_shots = random.uniform(0.005, 0.01) # Random delay between shots

            pyautogui.mouseDown(button='left')  # Hold left-click
            time.sleep(charge_time)              # Simulate charging
            pyautogui.mouseUp(button='left')    # Release to shoot
            time.sleep(delay_between_shots)     # Wait before next shot
        else:
            time.sleep(0.1)

        if iterations is not None:
            count += 1
            if count >= iterations:
                break


def on_press(key):
    global spamming
    try:
        if key.char == '`':  # Press '`' to toggle
            spamming = not spamming
            print("Bow spam:", "ON" if spamming else "OFF")
    except AttributeError:
        pass


if __name__ == "__main__":
    # Start spam thread running indefinitely
    threading.Thread(target=bow_spam_loop, daemon=True).start()

    # Start keyboard listener (blocking)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
