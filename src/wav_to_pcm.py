import os
from subprocess import Popen

import numpy as np

def main():
    files = os.listdir(".\\video")
    for i in files:
        Popen("ffmpeg -y  -i ./video/" + i + " -acodec pcm_s16le -f s16le -ac 1 -ar 16000 ./output/" + i[:-4] + ".pcm")

if __name__ == "__main__":
    main()
