'''
Venturi Pure League
Concept by VanDerFire
2022
'''

#Import libs
import os
from shlex import join
from lib.libconv.units import decimalMinutesConverter, secondsMin
from lib.libsimc import *
from lib.libcars.carCompts import *
from lib.libracingd.driverAttributes import racedriver
from lib.libsimc.lapsimulator import complexLapSim, fullRaceSim, lapSpeedSim, lapTimeSim, simmodes
from lib.libtrack.trackAttributes import *

#Import data from the season
#Formula pure prototype
from data.category.FPure22.drivers import *
from data.category.FPure22.cars import *
from data.category.FPure22.tracks import *

#simmodes.raceSimulator(chacaoUC, drivers=drivers)
#simmodes.timeTrialSimulator(chacaoUC, drivers=drivers)

def joinFolder():

    os.system(f'cd {os.getcwd()}')

def menu():

    print('Formula Pure Simulator')
    print('\n[1] Simulate Race')
    #print('\n[2] Simulate Time Sessions')

    sel = input('>: ')

    if sel == '1':

        os.system('cls')
        print('Select Circuit')
        print('\n[1]GP Chacao')
        print('[2]GP Cojedes')
        print('[3]GP Chile')
        print('[4]GP Mexico')
        print('[5]GP Puerto la cruz')
        print('[6]GP Brasil')

        sel = input('>: ')

        if sel == '1':

            simmodes.raceSimulator(chacaoUC, drivers)

        elif sel == '2':

            simmodes.raceSimulator(sancarlosIC, drivers)

        elif sel == '3':

            simmodes.raceSimulator(chileIC, drivers)

        elif sel == '4':

            simmodes.raceSimulator(mexicoIC, drivers)

        elif sel == '5':

            simmodes.raceSimulator(plcUC, drivers)

        elif sel == '6':

            simmodes.raceSimulator(brazilIC, drivers)

    elif sel == '2':

        os.system('cls')
        print('Select Circuit')
        print('\n[1]GP Chacao')
        print('[2]GP Cojedes')
        print('[3]GP Chile')
        print('[4]GP Mexico')
        print('[5]GP Puerto la cruz')
        print('[6]GP Brasil')

        sel = input('>: ')

        if sel == '1':

            simmodes.timeTrialSimulator(chacaoUC, drivers)

        elif sel == '2':

            simmodes.timeTrialSimulator(sancarlosIC, drivers)

        elif sel == '3':

            simmodes.timeTrialSimulator(chileIC, drivers)

        elif sel == '4':

            simmodes.timeTrialSimulator(mexicoIC, drivers)
            
        elif sel == '5':

            simmodes.timeTrialSimulator(plcUC, drivers)

        elif sel == '6':

            simmodes.timeTrialSimulator(brazilIC, drivers)
1
menu()
