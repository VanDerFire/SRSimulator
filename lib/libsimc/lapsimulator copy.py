
import random
import json

from lib.libconv.units import decimalMinutesConverter, hoursSec, meterKm, secondsHrs, secondsMin
from ..libconv import *
from lib.libbackups import backup
from lib.libcars.carCompts import hard, soft, medium, defaulTyre

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

    vehicleFire = 0.0040

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

    elif percentage < vehicleFire:

        return 'Vehicle Fire'

    elif percentage < seriousAccident:

        return 'Serious Accident'

    elif percentage < outOfFuel:

        return 'Vehicle out of fuel'

    elif percentage < fatalAccident:

        return 'Fatal Accident. RIP'

    else:

        return 0

def tyreSelector():

    percentage = random.random()

    if percentage <= 0.33:

        tyre = hard

    elif percentage <= 0.66:

        tyre = medium

    elif percentage <= 0.99:

        tyre = soft

    return tyre

class simmodes:

    def timeTrialSimulator(track, drivers):          #Modo Simulacion de FP y Clasificacion

        laptimes = {}

        for driver in drivers:

            dname = driver.name

            dteam = driver.car.team

            avgSpeed = lapSpeedSim(track, driver)

            laptime = float(lapTimeSim(track, avgSpeed))

            laptime = secondsMin(laptime)

            laptime = decimalMinutesConverter(laptime)

            laptimes[f'{dname} | {dteam}'] = laptime


        results = dict(sorted(laptimes.items(), key=lambda item: item[1]))   #Clear Camel

        for driver, time in results.items():

            print(f'\n{str(driver)} | ({str(time)})')

        backup.savebackup.saveTimeTrial(laptimes, track)

    def raceSimulator(track, drivers):

        fullracetimes = []

        totalracetimes = {}
        
        for driver in drivers:

            dname = driver.name

            dteam = driver.car.team

            fId = random.random()

            cId = retirementChances(fId)

            if cId == 0:
                
                racetime = fullRaceSim(track, driver)

                racetime = secondsMin(racetime)

                racetime = decimalMinutesConverter(racetime)            

                totalracetimes[f'{dname} | {dteam}'] = racetime

            else:
                
                totalracetimes[f'{dname} | {dteam}'] = f'DNF - {cId}'

        #Sort the dictionary

        results = dict(sorted(totalracetimes.items(), key=lambda item: item[1]))   #Clear Camel

        #Print

        for driver, time in results.items():

            print(f'\n{str(driver)} | ({str(time)})')


        backup.savebackup.saveRace(fullracetimes, track=track)





