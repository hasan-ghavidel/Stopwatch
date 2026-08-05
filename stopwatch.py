import tkinter as tk
import time

running = False
start_time = 0
elapsed = 0


def update():
    global elapsed

    if running:
        elapsed = time.time() - start_time

        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed * 100) % 100)

        timer.config(text=f"{minutes:02}:{seconds:02}:{milliseconds:02}")

    root.after(10, update)


def start():
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - elapsed

def stop():
    global running
    running = False


def reset():
    global running, elapsed
    running = False
    elapsed = 0
    timer.config(text="00:00:00")


root = tk.Tk()
root.title("Stylish Stopwatch")
root.geometry("500x280")
root.configure(bg="#181818")

timer = tk.Label(
    root,
    text="00:00:00",
    font=("Consolas", 42, "bold"),
    fg="#00FF99",
    bg="#181818"
)
timer.pack(pady=30)

frame = tk.Frame(root, bg="#181818")
frame.pack()

btn_style = {
    "font": ("Arial", 14, "bold"),
    "width": 10,
    "height": 2,
    "bd": 0,
}

start_btn = tk.Button(
    frame,
    text="Start",
    bg="#27AE60",
    fg="white",
    command=start,
    **btn_style
)

stop_btn = tk.Button(
    frame,
    text="Stop",
    bg="#E74C3C",
    fg="white",
    command=stop,
    **btn_style
)

reset_btn = tk.Button(
    frame,
    text="Reset",
    bg="#3498DB",
    fg="white",
    command=reset,
    **btn_style
)

start_btn.grid(row=0, column=0, padx=10)
stop_btn.grid(row=0, column=1, padx=10)
reset_btn.grid(row=0, column=2, padx=10)

update()

root.mainloop()
