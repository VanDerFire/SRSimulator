'''
Venturi Pure League
Concept by VanDerFire
2022
'''

#Import libs
from lib.libsimc import *
from lib.libcars.carCompts import *
from lib.libracingd.driverAttributes import racedriver
from lib.libsimc.lapsimulator import complexLapSim, lapSpeedSim, lapTimeSim
from lib.libtrack.trackAttributes import *

#create test track

caracas = track(eventName='Lechosa Race', 
trackName='Lechosa International Raceway', 
trackDistance=4920,
laps=23,
avgTime=115,
avgSpeed=154.02)

#test car

testEngine = engine('MMC PU22TC', 3, 10, 250)

testChassis = chassis('MMC AeroX1', 300, 50)

testcar = car('MMC X22', 'Escuderia MMC', testEngine, testChassis)

#test driver

thestig = racedriver('The Stig', testcar, 270, 19)

print(complexLapSim(caracas, thestig))