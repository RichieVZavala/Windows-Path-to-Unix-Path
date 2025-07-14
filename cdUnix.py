# This is going to be a remake of my Unix path script 
import os

dir = os.getcwd()
dir = dir.replace("\\", "/")

os.popen(f"echo {dir} | clip")

