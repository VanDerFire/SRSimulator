

baseChassisWeight = 450
chassisMaterialPrice = 5000
minimumChassisWeight = 250

baseEnginePower = 100

baseTyreDurability = 120000 #Tyre durability in meters at 0.5

class tyre:

    def __init__(self, name, hardness):

        self.name = name

        self.hardness = hardness

        self.durability = self.durabilityCalc

        self.performance = self.durability / 100000

    def durabilityCalc(self):

        #0 es duro y 1 es blando, si el numero esta mas cerca de 1,
        #el neumatico va a ser mas blando y tambien al contrario

        if self.hardness == 0:

            durability = baseTyreDurability

        else:

            hardness = self.hardness * 100000

            durability = baseTyreDurability - hardness

        return durability 

class chassis:

    def __init__(self, name, price):
        
        self.name = name

        self.weight = baseChassisWeight - (price / 1000)

        self.aero = price - chassisMaterialPrice

        self.rating = self.chassisRating()

    def chassisRating(self):

        rating = round((self.aero + self.weight) / 1000)

        if rating > 100:

            rating = 100

        elif rating <= 0:

            rating = 1

        return rating

class engine:

    def __init__(self, name, endurance, power, weight):
        
        self.name = name
        self.endurance = endurance
        self.power = power
        self.weight = weight

        self.unreliability = round((self.power / 10) / self.endurance)
        self.rating = round(self.power - self.unreliability)

class car:

    def __init__(self, team, engine, chassis):

        self.team = team
        self.engine = engine
        self.chassis = chassis
        
        self.weigth = round(baseChassisWeight + self.engine.weight + self.chassis.weight)
        self.rating = round((self.engine.rating + self.chassis.rating) - (self.weigth / 100))

    def showInfo(self):

        print(f'{self.team} {self.chassis.name}\nEngine: {self.engine.name} \nChassis Rating: {self.chassis.rating} \nEngine Rating: {self.engine.rating} \nGlobal Rating: {self.rating}')

#Tyre compounds

soft = tyre('Soft', 0.70)

medium = tyre('Medium', 0.50)

hard = tyre('Hard', 0.35)

defaulTyre = tyre('Default', 0)