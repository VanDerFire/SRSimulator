''''
INDEX OF DRIVERS
FORMULA WAVE Monocar
'''
from lib.libracingd.driverAttributes import *
from .cars import *


#ZEEPHYR by EXTMotorsport

jJorginhos = racedriver('Zeo Van Der Fire', extcar, 0, 0)

aBrooklyn = racedriver('Alex Brooklyn', extcar, 0, 0)

#NAOGP Chevy

eKael = racedriver('Ethan Kael', naocar, 0, 0)

#SRB Ford

sFernandez = racedriver('Sunshine Fernandez', sunsetcar, 0, 0)

sPerez = racedriver('Segrio Perez', sunsetcar, 0, 0)

drivers = [
    zVanDerFire,
    aBrooklyn,
    eKael,
    sFernandez,
    sPerez
]