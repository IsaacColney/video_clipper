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

def main():
    print("**********  Video trimmer  ********")
    trim_time_sec : str = str(input("Enter trim time (sec) : "))
    video_list = scan_file()
    video_clipper_from_end(video_list , trim_time_sec)
    print("********* Video clip complete ***********")

#Programm entry point:
if __name__ == "__main__":
    main()

