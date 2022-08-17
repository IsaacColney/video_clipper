from glob import glob
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from turtle import title
from threading import Thread
from asyncio import subprocess
import glob
from importlib.resources import path
import subprocess
from time import time

#Video clipper function
def scan_file(path : str) -> list:
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

def main(trim_time : int , path : str) -> int:
    print("**********  Video trimmer  ********")
    trim_time_sec : str = str(trim_time)
    video_list = scan_file(path)
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




#setup
root = Tk()

#window dimension
root.title("Video clipper : end of frame")
root.minsize(height=200, width=400)
root.resizable(False , False)

#global_variable
global_path : str = ""

#function
def trim_file():
    input_trim_time = time_trim_input.get()
    if(len(input_trim_time) != 0):
        trimming.grid(column=1 , row = 4)
        trim_time = int(input_trim_time)
        time_elapse : int = main(trim_time , global_path)
        trimming.destroy()
        if(time_elapse == 0):
            no_video_found_text = Label(root , text= "No video found!")
            no_video_found_text.grid(column=1 , row=4)
        else:
            time_elapse_text = Label(root , text = f"Time elapsed : {time_elapse} seconds")
            file_trim_complete_text.grid(column=1 , row = 4)
            time_elapse_text.grid(column=1,row=4)
    else:
        error_label = Label(root, text= "Enter a valid input")
        error_label.grid(column=1 , row = 4)
    button.destroy()
    quit_button.grid(row=3 , column= 1 , padx=10 ,pady=10)
    
def select_folder() -> str:
    global global_path 
    global_path = filedialog.askdirectory()
    working_path = Label(root ,text=f"Path : {global_path}")
    working_path.grid(row=1 , column= 1 , padx=10 ,pady=10)

#widget
title_text = Label(root ,text="Enter time(second) :")

button = Button(root , text = "Trim file" , padx=20 , command=Thread(target = trim_file).start)
path_button = Button(root , text = "Select folder" , padx=20 , command=select_folder)
quit_button = Button(root , text = "Quit" , padx=20 , command=root.destroy)
time_trim_input = Entry(root)
trimming = Label(root , text="Trimming progress...........")
file_trim_complete_text = Label(text="File trim complete..")


#layout
title_text.grid(row=2,column=0 ,padx=10 , pady=10)
button.grid(row=3 , column= 1 , padx=10 ,pady=10)
path_button.grid(column=1 , row=0 , padx=10 ,pady=10)
time_trim_input.grid(row=2 , column= 1 , padx=10 ,pady=10)


root.mainloop()
