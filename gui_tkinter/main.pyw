import time
from tkinter import *
from tkinter import ttk
from turtle import title
from threading import Thread
from asyncio import subprocess
import glob
from importlib.resources import path
import os
import sys
import subprocess
from time import time

#Video trimmer functions/Methods
def scan_file() -> list:
    if getattr(sys, 'frozen', False):
        path = os.path.dirname(sys.executable)
# or a script file (e.g. `.py` / `.pyw`)
    elif __file__:
        path = os.path.dirname(__file__)
    clip_list = []
    for file in glob.glob(path+"\\*.mp4"):
        clip_list.append(file)
    return clip_list

def output_path_generator(output_name : str , input_path : str) -> str:
    path_in_list : list = input_path.split("\\")
    path_in_list.pop()
    path_in_list.append(output_name)
    output_path : str = "\\".join(path_in_list)
    return output_path

def video_clipper_from_end(video_list : list[str] , trim_time : str):
    for video in video_list:
        output_name : str = trim_time+"_clipped_"+ video.split("\\")[-1]
        output_path : str = output_path_generator(output_name , video)
        command = f'ffmpeg -sseof -{trim_time} -i "{video}" -c copy "{output_path}"'
        subprocess.run(command)

def main_trimmer(trim_time : int) -> int:
    print("**********  Video trimmer  ********")
    trim_time_sec : str = str(trim_time)
    video_list = scan_file()
    if(len(video_list) == 0):
        print("No video found !")
        time_elapse = 0
    else:
        start_time = time()
        video_clipper_from_end(video_list , trim_time_sec)
        stop_time = time()
        time_elapse = round(stop_time - start_time,2)
        print("********* Video clip complete ***********")
        print(f"Time elapsed : {time_elapse} seconds")
    return time_elapse
#Tkinter GUI for python code
#setup
root = Tk()

#window dimension
root.title("Video clipper : End of frame Method")
root.geometry("400x150")
root.resizable(False , False)

#function
def trim_file():
    input_trim_time = time_trim_input.get()
    if(len(input_trim_time) != 0):
        trimming.grid(column=1 , row = 2)
        trim_time = int(input_trim_time)
        time_elapse : int = main_trimmer(trim_time)
        trimming.destroy()
        if(time_elapse == 0):
            no_video_found_text.grid(column=1 , row=2)
        else:
            time_elapse_text = Label(root , text = f"Time elapsed : {time_elapse} seconds")
            file_trim_complete_text.grid(column=1 , row = 2)
            time_elapse_text.grid(column=1,row=3)
    else:
        error_label = Label(root, text= "Enter a valid input")
        error_label.grid(column=1 , row = 2)
    button.destroy()
    quit_button.grid(row=1 , column= 1 , padx=10 ,pady=10)

#widget
title_text = Label(root ,text="Enter time(second) :" ,pady=15 , padx=15)
button = Button(root , text = "Trim file" , padx=20 , command=Thread(target = trim_file).start)
quit_button = Button(root , text = "Quit" , padx=20 , command=root.destroy)
time_trim_input = Entry(root ,)
trimming = Label(root , text="Trimming progress...........")
file_trim_complete_text = Label(text="File trim complete..")
no_video_found_text = Label(root , text= "No video found!")

#layout
title_text.grid(row=0,column=0 ,padx=10 , pady=10)
button.grid(row=1 , column= 1 , padx=10 ,pady=10)
time_trim_input.grid(row=0 , column= 1 , padx=10 ,pady=10)

root.mainloop()
