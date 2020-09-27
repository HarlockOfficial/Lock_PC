import tkinter
import datetime
from tkinter import messagebox
from LockPC import LockPC
from threading import Thread


class GUI:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Pc Locker")
        self.init_for_time()
        self.init_until_time()
        self.lock_until_key()
        self.window.mainloop()

    def lock_gui(self, lock):
        for panel in self.window.children.values():
            for child in panel.winfo_children():
                child.configure(state="disabled")
        lock.start()
        messagebox.showinfo("Information Message", "Computer Locked")
        Thread(target=self.unlock_gui, args=(lock,)).start()

    def unlock_gui(self, lock):
        lock.join()
        for panel in self.window.children.values():
            for child in panel.winfo_children():
                if isinstance(child, tkinter.Entry):
                    child.delete(0, "end")
                child.configure(state="normal")

    def lock_for_time(self, hh, mm, ss):
        hour = hh.get()
        minutes = mm.get()
        sec = ss.get()
        error = False
        if hour.isdigit() and int(hour) >= 0:
            if minutes.isdigit() and 0 <= int(minutes) < 60:
                if sec.isdigit() and 0 <= int(sec) < 60:
                    time = ((int(hour) * 60 + int(minutes)) * 60 + int(sec))
                    if time != 0:
                        lock = LockPC(for_time=time)
                        self.lock_gui(lock)
                    else:
                        error = True
                else:
                    ss.focus_set()
                    error = True
            else:
                mm.focus_set()
                error = True
        else:
            hh.focus_set()
            error = True
        if error:
            messagebox.showerror("Invalid Data", "Please put a correct time")

    def lock_until_time(self, hh, mm, ss):
        hour = hh.get()
        minutes = mm.get()
        sec = ss.get()
        error = False
        if hour.isdigit() and int(hour) >= 0:
            if minutes.isdigit() and 0 <= int(minutes) < 60:
                if sec.isdigit() and 0 <= int(sec) < 60:
                    time = datetime.datetime.now()
                    time = time.replace(hour=int(hour), minute=int(minutes), second=int(sec))
                    if time > datetime.datetime.now():
                        lock = LockPC(until_time=time)
                        self.lock_gui(lock)
                    else:
                        msg = messagebox.askquestion("Lock until tomorrow",
                                                     "Do you want to lock the computer until tomorrow?")
                        if msg == "yes":
                            time += datetime.timedelta(days=1)
                            lock = LockPC(until_time=time)
                            self.lock_gui(lock)
                else:
                    ss.focus_set()
                    error = True
            else:
                mm.focus_set()
                error = True
        else:
            hh.focus_set()
            error = True
        if error:
            messagebox.showerror("Invalid Data", "Please put a correct time")

    def init_for_time(self):
        panel = tkinter.PanedWindow(self.window)
        panel.grid(column=0, row=0)

        label = tkinter.Label(panel, text="Lock computer for: ")
        panel.add(label)

        hh = tkinter.Entry(panel, width=10)
        hh.insert(0, "hh")
        hh.bind("<FocusIn>", lambda args: hh.delete(0, "end"))
        panel.add(hh)

        col1 = tkinter.Label(panel, text=":")
        panel.add(col1)

        mm = tkinter.Entry(panel, width=10)
        mm.insert(0, "mm")
        mm.bind("<FocusIn>", lambda args: mm.delete(0, "end"))
        panel.add(mm)

        col2 = tkinter.Label(panel, text=":")
        panel.add(col2)

        ss = tkinter.Entry(panel, width=10)
        ss.insert(0, "ss")
        ss.bind("<FocusIn>", lambda args: ss.delete(0, "end"))
        panel.add(ss)

        btn = tkinter.Button(panel, text="Start Lock", command=lambda: self.lock_for_time(hh, mm, ss))
        panel.add(btn)

    def init_until_time(self):
        panel = tkinter.PanedWindow(self.window)
        panel.grid(column=0, row=1)

        label = tkinter.Label(panel, text="Lock computer until: ")
        panel.add(label)

        hh = tkinter.Entry(panel, width=10)
        hh.insert(0, "hh")
        hh.bind("<FocusIn>", lambda args: hh.delete(0, "end"))
        panel.add(hh)

        col1 = tkinter.Label(panel, text=":")
        panel.add(col1)

        mm = tkinter.Entry(panel, width=10)
        mm.insert(0, "mm")
        mm.bind("<FocusIn>", lambda args: mm.delete(0, "end"))
        panel.add(mm)

        col2 = tkinter.Label(panel, text=":")
        panel.add(col2)

        ss = tkinter.Entry(panel, width=10)
        ss.insert(0, "ss")
        ss.bind("<FocusIn>", lambda args: ss.delete(0, "end"))
        panel.add(ss)

        btn = tkinter.Button(panel, text="Start Lock", command=lambda: self.lock_until_time(hh, mm, ss))
        panel.add(btn)

    def lock_until_key(self):
        pass


if __name__ == "__main__":
    GUI()
