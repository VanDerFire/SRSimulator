''''
INDEX OF DRIVERS
FORMULA PURE 1.0 2022
'''
from lib.libracingd.driverAttributes import *
from .cars import *


#EXTMotorsport porsche

zVanDerFire = racedriver('Zeo Van Der Fire', extcar, 0, 0)

aBrooklyn = racedriver('Alex Brooklyn', extcar, 0, 0)

#Goldenfire Chevy

aGallo = racedriver('Aaron Gallo', gfcar, 0, 0)

ddAngel = racedriver('Daniel de Angel', gfcar, 0, 0)

#Junin Bull Racing Mercedes

n = racedriver('N', jbmCar, 0, 0)

alia = racedriver('Alia', jbmCar, 0, 0)

#NAOGP Chevy

eKael = racedriver('Ethan Kael', naocar, 0, 0)

#Nou Mercedes

jfFernandez = racedriver('Jose Fernandez Fernandez', noucar, 0, 0)

#SRB Ford

sFernandez = racedriver('Sunshine Fernandez', sunsetcar, 0, 0)

sPerez = racedriver('Segrio Perez', sunsetcar, 0, 0)

#PV Ford

dDanielsson = racedriver('Daniel Danielsson', pvcar, 0, 0)

gWynaut = racedriver('Guillermo Wynaut', pvcar, 0, 0)

#Tottus porsche

dFernandez = racedriver('Daniela Fernandez', tottuscar, 0, 0)

#USDLG Mercedes

jButifarra = racedriver('Juan Butifarra', usdlgcar, 0, 0)

#Team Yiff

yYulianus = racedriver('Yuri Yulianus', yiffcar, 0, 0)

drivers = [
    zVanDerFire,
    aBrooklyn,
    eKael,
    sFernandez,
    sPerez,
    dDanielsson,
    gWynaut,
    jButifarra,
    aGallo, 
    ddAngel,
    dFernandez,
    yYulianus,
    n,
    alia,
    jfFernandez
]