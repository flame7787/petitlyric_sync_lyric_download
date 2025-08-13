from petitlyrics import find_lyric_folder, find_lyric_file
from tkinter import filedialog
from tkinter import *

import sys
import os
import time

def main():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    find_lyric_folder(folder_selected)

if __name__ == '__main__':
    dropped_paths = sys.argv[1:]
    
    if dropped_paths:
        for path in dropped_paths:
            if os.path.isdir(path):
                print(f"Dropped folder: {path}")
                find_lyric_folder(path)
            else:
                print(f"Dropped file: {path}")
                find_lyric_file(path)
        print("\nFiles/folders processed. Exiting in 1 second...")
        time.sleep(1)
    else:
        main()