import pynput
from time import sleep
import datetime
from threading import Thread


class LockPC(Thread):
    def __init__(self, for_time=None, until_time=None, key_combination=None):
        Thread.__init__(self)
        if for_time is not None and isinstance(for_time, int):
            if for_time > 0:
                self.time = for_time
            else:
                raise Exception("Invalid Parameter Set")
        elif until_time is not None and isinstance(until_time, datetime.datetime):
            now = datetime.datetime.now()
            if now < until_time:
                self.time = (until_time - now).total_seconds()
            else:
                raise Exception("Invalid Parameter Set")
        elif key_combination is not None:
            pass
        else:
            raise Exception("No Parameters Set")

    def move(self, x, y):
        if x != 0 or y != 0:
            pynput.mouse.Controller().position = (0, 0)

    def scroll(self, x, y, dx, dy):
        pynput.mouse.Controller().scroll(-dx, -dy)

    def stop(self, key):
        if not hasattr(key, "char"):
            if key == pynput.keyboard.Key.cmd:
                pynput.keyboard.Controller().press('z')
                pynput.keyboard.Controller().release('z')
            else:
                pynput.keyboard.Controller().release(key)

    def run(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.stop)
        mouse_listener = pynput.mouse.Listener(on_move=self.move, on_scroll=self.scroll, suppress=True)
        keyboard_listener.start()
        mouse_listener.start()
        # --------
        sleep(self.time)
        # --------
        keyboard_listener.stop()
        mouse_listener.stop()
        exit(0)
