''''
INDEX OF CARS
FORMULA PURE 1.0 2022
'''

from lib.libcars.carCompts import *

#Engines

chevy = engine('Chevy c7070p', 2, 70, 70)

ford = engine('Ford Ecoboost E-22001', 4, 71, 69)

porsche = engine('Porsche 9p21h', 3, 72, 70)

mercedes = engine('Mercedes-AMG PU2022', 4, 75, 80)

engines = [chevy, ford, porsche, mercedes]

#EXTMotorsport Porsche

extchassis = chassis("Extreme P1", 70000)

extcar = car('EXTMotorsport Porsche', porsche, extchassis, defaulTyre)

#GoldenFire Racing

gfchassis = chassis("golden Gf1", 27000)

gfcar = car('Pepsi GoldenFire Racing Team', chevy, gfchassis, defaulTyre)

#Junín Bull Racing Mercedes

jbmChassis = chassis('Junin Bull JB1', 65000)

jbmCar = car('Junin Bull Racing Mercedes', mercedes, jbmChassis, defaulTyre)

#NAOGP Chevy

naochassis = chassis('Nao N22ek', 25000)

naocar = car('Dataperro NAO GP Chevy', chevy, naochassis, defaulTyre)

#NOU Mercedes

nouchassis = chassis('Nou papu001', 45000)

noucar = car('Nou Mercedes', mercedes, nouchassis, defaulTyre)

#Pilotos Velocistas Ford

pvchassis = chassis('PV22', 20000)

pvcar = car('Pilotos Velocistas Racing Team', ford, pvchassis, defaulTyre)

#SUNSET RACING BLUE FORD

sunsetchassis = chassis("Sunset BR22", 70000)

sunsetcar = car('Sunset Racing Blue', ford, sunsetchassis, defaulTyre)

#TOTTUS Porsche

tottuschassis = chassis("TOTTUS t1", 30000)

tottuscar = car('Tottus Racing Porsche', porsche, tottuschassis, defaulTyre)

#Hydroeleky Mercedes (ex UNOVA SDLG Mercedes)

usdlgchassis = chassis('USDLG U-1', 10000)

usdlgcar = car('Hydroeleky Mercedes', mercedes, usdlgchassis, defaulTyre)

#Team Yiff

yiffChassis = chassis('Yiff Braixen 1', 25000)

yiffcar = car('E621.NET TEAM YIFF MERCEDES', mercedes, yiffChassis, defaulTyre)