''''
INDEX OF CARS
FORMULA WAVE Monocar
'''

from lib.libcars.carCompts import *

#Engines

ford = engine('Ford Ecoboost E-22001', 3, 50, 75)

volkswagen = engine('VW das.22 metro', 3, 52, 80)

honda = engine('Honda RA-322WJ', 2, 45, 70)

#ZEEPHYR by EXTMotorsport

zchassis = chassis("ZEEPHYR w1fp", 20000)

extcar = car('ZEEPHYR Caracas Racing', volkswagen, zchassis)

#NAOGP

naochassis = chassis('Nao N22jr', 20000)

naocar = car('Dataperro NAO GP', ford, naochassis)

#SUNSET RACING BLUE FORD

sunsetchassis = chassis("Sunset BR22fvj", 20000)

sunsetcar = car('Sunset Racing Blue by Ford', ford, sunsetchassis)



