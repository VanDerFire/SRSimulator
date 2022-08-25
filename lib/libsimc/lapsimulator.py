
from distutils.log import fatal
import random

from lib.libconv.units import decimalMinutesConverter, hoursSec, meterKm, secondsHrs, secondsMin
from ..libconv import *
from lib.libbackups import backup

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


def fullRaceSim(track, driver):

    totalRaceTime = []

    laps = track.laps

    trackDistance = track.trackDistance

    fullRaceDistance = trackDistance * laps

    #Do the simulation

    for i in range(laps):

        avgSpeed = lapSpeedSim(track, driver)

        lapTime = float(lapTimeSim(track, avgSpeed))

        #-+1

        totalRaceTime.append(lapTime)

    totalRaceTime = sum(totalRaceTime)

    return totalRaceTime


def retirementChances(percentage):
   
    #Chances

    accident = 0.09

    engineFailure = 0.050

    electricFailure = 0.045

    outOfFuel = 0.030

    brakesFailure = 0.025

    gearboxFailure = 0.022

    seriousAccident = 0.0020

    fatalAccident = 0.0015

    if percentage < accident:

        return 'Accident'

    elif percentage < engineFailure:

        return 'Engine Failure.'

    elif percentage < electricFailure:

        return 'Electric Failure.'

    elif percentage < brakesFailure:

        return 'Brakes Failure'

    elif percentage < gearboxFailure:

        return 'Gearbox Failure'

    elif percentage < seriousAccident:

        return 'Serious Accident'

    elif percentage < outOfFuel:

        return 'Vehicle out of fuel'

    elif percentage < fatalAccident:

        return 'Fatal Accident. RIP'

    else:

        return 0



class simmodes:

    def timeTrialSimulator(track, drivers):          #Modo Simulacion de FP y Clasificacion

        laptimes = []   #Crear lista con todos los tiempos para luego ordenarlos

        for driver in drivers:

            dname = driver.name

            avgSpeed = lapSpeedSim(track, driver)

            laptime = float(lapTimeSim(track, avgSpeed))

            laptime = secondsMin(laptime)

            laptime = decimalMinutesConverter(laptime)

            laptimes.append(laptime)

            print(dname + ': ' + str(laptime))

        laptimes.sort()

        backup.savebackup.saveTimeTrial(laptimes, track)

        print(f'Best lap: {laptimes[0]}' )

    def raceSimulator(track, drivers):

        fullracetimes = []
        
        for driver in drivers:

            dname = driver.name

            fId = random.random()

            cId = retirementChances(fId)

            if cId == 0:
                
                racetime = fullRaceSim(track, driver)

                racetime = secondsMin(racetime)

                racetime = decimalMinutesConverter(racetime)            

                fullracetimes.append(racetime)

                print(dname + ' : ' + str(racetime))

            else:

                print(dname + ' : ' + f'DNF - {cId}')

        fullracetimes.sort()

        print(f'\nWinner: {fullracetimes[0]}')




