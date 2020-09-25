import pynput
from time import sleep
from threading import Thread


class LockPC(Thread):
    def __init__(self, time):
        Thread.__init__(self)
        self.keyboard_listener = pynput.keyboard.Listener(on_press=self.stop)
        self.mouse_listener = pynput.mouse.Listener(on_move=self.move, on_scroll=self.scroll, suppress=True)
        self.time = time

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
        self.keyboard_listener.start()
        self.mouse_listener.start()
        sleep(self.time)
        self.keyboard_listener.stop()
        self.mouse_listener.stop()
        exit(0)
