import tkinter as tk
import tkinter.filedialog as fd
import os, subprocess

# try:
#     import ffmpeg
# except ImportError:
#     os.system("pip install ffmpeg")
#     import ffmpeg

# if probe is needed (or input)

### Queue ###

file_queue = []

#### Commands ####

def append_to_filename(filepath, to_append):
    split_filepath = filepath.rsplit('.', 1)
    split_filepath.insert(1, to_append)
    return '.'.join([''.join(split_filepath[:1])] + split_filepath)

def get_frame_time():
    pass

def process(filepath):
    subprocess.run(["ffmpeg",
                    "-fflags", "+genpts",
                    "-i", f"{filepath}",
                    "-fflags", "+genpts",
                    "-i", f"{filepath}",
                    "-filter_complex", "[0:v]setpts=PTS-STARTPTS[top];",
                    "[1:v]setpts=PTS-STARTPTS+.033/TB,", "format=yuva420p,",
                    "colorchannelmixer=aa=0.5[bottom];", "[top][bottom]overlay=shortest=1",
                    "-c:v", "libx264",
                    "-crf", "26",
                    "-an" f"{append_to_filename(filepath, '_noflicker')}"])

def select_files():
    for pathname in fd.askopenfilenames(parent=root, title="Choose Videos to DeFlicker"):
        file_queue.append(pathname)

def start_queue():
    while file_queue:
        process(file_queue.pop())

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