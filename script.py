import moviepy.editor
from os import listdir
from os.path import isfile, join

def write_mp3(source:str,destination:str):
    file_names = [f for f in listdir(source) if isfile(join(source, f))]
    for file in file_names: 
        video = moviepy.editor.VideoFileClip(source+file)
        audio = video.audio
        file = file.replace("4","3")
        write_path = destination+file
        audio.write_audiofile(write_path)

def user_input():
    source = input("Please input a source folder: ")
    destination = input("Please input a destination folder: ")
    return source,destination

if __name__ == "__main__":
    source,destination = user_input()
    write_mp3(source,destination)
    print("Done")
