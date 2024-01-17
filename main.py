import tkinter as tk
import tkinter.filedialog as fd
import os, subprocess

try:
    import ffmpeg
except ImportError:
    os.system("pip install ffmpeg")
    import ffmpeg

### Queue ###

file_queue = []

#### Commands ####

def select_files():
    for pathname in fd.askopenfilenames(parent=root, title="Choose Videos to DeFlicker"):
        file_queue.append(pathname)
    print(file_queue)

def start_queue():
    pass

#### GUI ####

root = tk.Tk()
root.title("Video DeFlickerer")

instruction = tk.Label(root, text = "Please select the videos you want to deflicker.")
instruction.grid(row = 0, columnspan = 2)

select_btn = tk.Button(root, text = "Select Files", command = select_files)
select_btn.grid(row = 1, column = 0)

start_btn = tk.Button(root, text = "Start Queue", command = start_queue)
start_btn.grid(row = 1, column = 1)

queue_label = tk.Label(root)
queue_label.grid(row = 1, columnspan = 2)

root.mainloop()