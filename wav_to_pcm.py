import os
import numpy as np
from subprocess import Popen

def main():
    files = os.listdir(".\\video")
    for i in files:
        Popen("ffmpeg -y  -i ./video/" + i + " -acodec pcm_s16le -f s16le -ac 1 -ar 16000 ./output/" + i[:-4] + ".pcm")
    """
    f = open(".\\video\\" + i, "rb")
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype=np.int16)
    data.tofile(".\\output\\" + i[:-4] + ".pcm")
    """
if __name__ == "__main__":
    main()
