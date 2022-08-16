from asyncio import subprocess
import glob
import sys
import subprocess

def scan_file() -> list:
    path = sys.path[0]
    clip_list = []
    for file in glob.glob(path+"\\*.mp4"):
        clip_list.append(file)
    return clip_list

def video_clipper_from_end(video_list : list , trim_time : str):
    for video in video_list:
        input_video : str = "video"
        output_name : str = "./clipped"+ video.split("\\")[-1]
        command = f'ffmpeg -sseof -{trim_time} -i "{video}" -c copy "{output_name}"'
        subprocess.run(command)

def main():
    print("**********  Video trimmer  ********")
    trim_time_sec : str = str(input("Enter trim time (sec) : "))
    video_list = scan_file()
    video_clipper_from_end(video_list , trim_time_sec)
    print("********* Video clip complete ***********")

#Programm entry point:
main()
