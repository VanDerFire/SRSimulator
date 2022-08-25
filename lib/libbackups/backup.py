import os
import time
from tkinter import W

class savebackup:

    def saveTimeTrial(times, track):

        timestr = time.strftime("%Y%m%d-%H%M%S")
        
        tname = track.trackName

        with open(f'{os.getcwd()}\\backups\\{tname}\\{timestr}.txt', 'w+') as f:

            f.write(str(times))