import os
import shutil

def find_mp3_files(directory):
    files = []

    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            files.append(file)
    
    files.sort()
    return files

def copy_directory(in_dir, out_dir):
    shutil.copytree(in_dir, out_dir)
