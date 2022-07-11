baseChassisWeight = 450
baseEnginePower = 100
minimumChassisWeight = 250

class chassis:

    def __init__(self, name, weight, aero):
        
        self.name = name

        self.weight = weight

        self.aero = aero

        self.rating = self.chassisRating()

    def chassisRating(self):

        rating = round(self.aero + self.weight / 1000)

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

    def __init__(self, name, team, engine, chassis):

        self.name = name
        self.team = team
        self.engine = engine
        self.chassis = chassis
        
        self.weigth = round(baseChassisWeight + self.engine.weight + self.chassis.weight)
        self.rating = round((self.engine.rating + self.chassis.rating) - (self.weigth / 100))
