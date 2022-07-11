
import random

from lib.libconv.units import decimalMinutesConverter, hoursSec, meterKm, secondsMin
from ..libconv import *

class phy:

    def avgSpeed(distance, time):

        avgSpeed = distance / time

        return avgSpeed

def lapSpeedSim(track, driver):
    #get the distance in km

    trackAvgSpeed = round(track.avgSpeed)

    trackMaxAvgSpeed = round(trackAvgSpeed + (driver.rating / 10) * driver.car.rating / 10)

    speedRange = random.randint(trackAvgSpeed, trackMaxAvgSpeed)

    return speedRange

def lapTimeSim(track, avgSpeed):

    #convert laptime to km

    distance = meterKm(track.trackDistance)

    laptime = distance / avgSpeed

    #convert to seconds

    laptime = hoursSec(laptime)

    return laptime

def complexLapSim(track, driver):

    avgSpeed = lapSpeedSim(track, driver)

    lapTime = lapTimeSim(track, avgSpeed)

    #Convert to minutes

    lapTime = secondsMin(lapTime)

    #format

    lapTime = decimalMinutesConverter(lapTime)

    return lapTime



