''''
INDEX OF DRIVERS
FORMULA PURE 1.0 2022
'''
from lib.libracingd.driverAttributes import *
from .cars import *


#EXTMotorsport porsche

zVanDerFire = racedriver('Zeo Van Der Fire', extcar, 6, 3)

aBrooklyn = racedriver('Alex Brooklyn', extcar, 4.8, 3)

#Goldenfire Chevy

aGallo = racedriver('Aaron Gallo', gfcar, 0.68, 3) 

ddAngel = racedriver('Daniel de Angel', gfcar, 0.3, 2)

#Junin Bull Racing Mercedes

n = racedriver('Natural Gropius', jbmCar, 2, 2)

alia = racedriver('Alia Rivera', jbmCar, 2.7, 2)

#NAOGP Chevy

eKael = racedriver('Ethan Kael', naocar, 1.04, 3)

#Nou Mercedes

jfFernandez = racedriver('Jose Fernandez Fernandez', noucar, 1.8, 3)

#SRB Ford

sFernandez = racedriver('Sunshine Fernandez', sunsetcar, 5.5, 3)

sPerez = racedriver('Segrio Perez', sunsetcar, 2.8, 2)

#PV Ford

dDanielsson = racedriver('Daniel Danielsson', pvcar, 0.16, 1)

#Tottus porsche

dFernandez = racedriver('Daniela Fernandez', tottuscar, 1.4, 3)

#USDLG Mercedes

jButifarra = racedriver('Juan Butifarra', usdlgcar, 0.18, 3)

jMcCarthy = racedriver('Jenny McCarty', usdlgcar, 0.04, 1)

#Team Yiff

yYulianus = racedriver('Yuri Yulianus', yiffcar, 1.5, 3)

drivers = [
    zVanDerFire,
    aBrooklyn,
    eKael,
    sFernandez,
    sPerez,
    #dDanielsson,
    jMcCarthy,
    jButifarra,
    aGallo, 
    ddAngel,
    dFernandez,
    yYulianus,
    n,
    alia,
    jfFernandez
]