import os
import json
import time

class savebackup:

    def saveTimeTrial(times, track):

        timestr = time.strftime("%Y%m%d-%H%M%S")
        
        tname = track.trackName

        with open(f'{os.getcwd()}\\backups\\{tname}\\{timestr}.txt', 'w+') as f:

            f.write(str(times))

    def saveRace(times, track):

        timestr = time.strftime("%Y%m%d-%H%M%S")
        
        tname = track.trackName

        with open(f'{os.getcwd()}\\backups\\{tname}\\Race\\{timestr}.txt', 'w+') as f:

            f.write(str(times))

    def saveRaceRecord(times, track):

        timestr = time.strftime("%Y%m%d-%H%M%S")
        
        tname = track.trackName

        with open('...\\...\\...\\currentData\\race.json', 'w+') as f:

            json.dump(times, f, indent=4)