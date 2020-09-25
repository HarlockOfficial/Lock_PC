import tkinter
import datetime
from tkinter import messagebox
from LockPC import LockPC
from threading import Thread


def unlock(lock, hh, mm, ss, btn):
    lock.join()
    hh.delete(0, "end")
    hh.insert(0, "hh")
    mm.delete(0, "end")
    mm.insert(0, "mm")
    ss.delete(0, "end")
    ss.insert(0, "ss")
    hh.configure(state="normal")
    mm.configure(state="normal")
    ss.configure(state="normal")
    btn.configure(state="normal")


def lock_computer(btn, hh, mm, ss):
    hour = hh.get()
    min = mm.get()
    sec = ss.get()
    error = False
    if hour.isdigit():
        if min.isdigit() and 0 <= int(min) < 60:
            if sec.isdigit() and 0 < int(sec) < 60:
                lock = LockPC((int(hour) * 60 + int(min)) * 60 + int(sec))
                hh.configure(state="disabled")
                mm.configure(state="disabled")
                ss.configure(state="disabled")
                btn.configure(state="disabled")
                lock.start()
                messagebox.showinfo("Information Message", "Computer Locked")
                Thread(target=unlock, args=(lock, hh, mm, ss, btn)).start()
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
        messagebox.showinfo("Invalid Data", "Please put a correct time")


def init_content(w):
    label = tkinter.Label(w, text="How Long you want to Lock your computer for?")
    label.grid(column=0, row=0, columnspan=5)
    hh = tkinter.Entry(w, width=10)
    hh.insert(0, "hh")
    hh.bind("<FocusIn>", lambda args: hh.delete(0, "end"))
    hh.grid(column=0, row=1)
    col1 = tkinter.Label(window, text=":")
    col1.grid(column=1, row=1)
    mm = tkinter.Entry(w, width=10)
    mm.insert(0, "mm")
    mm.bind("<FocusIn>", lambda args: mm.delete(0, "end"))
    mm.grid(column=2, row=1)
    col2 = tkinter.Label(window, text=":")
    col2.grid(column=3, row=1)
    ss = tkinter.Entry(w, width=10)
    ss.insert(0, "ss")
    ss.bind("<FocusIn>", lambda args: ss.delete(0, "end"))
    ss.grid(column=4, row=1)
    btn = tkinter.Button(w, text="Start Lock", command=lambda: lock_computer(btn, hh, mm, ss))
    btn.grid(column=0, row=3, columnspan=5)


window = tkinter.Tk()
window.title("Pc Locker")
init_content(window)
window.mainloop()
