from traceback import print_tb


class racedriver:

    def __init__(self, name, car, points, exp):
        
        self.name = name

        self.car = car

        self.points = points

        self.exp = exp

        #Driver rating formula

        self.rating = self.gdrTotalRating()

    def gdrPointsR(self):

        gdrRating = self.points / 10

        return gdrRating

    def gdrExpR(self):

        gdrRating = self.exp / 4

        return gdrRating

    def gdrCarR(self):

        gdrRating = round(self.car.rating / 10)

        return gdrRating

    def gdrTotalRating(self):

        gdrPointsR = self.gdrPointsR()

        gdrExpR = self.gdrExpR()

        gdrCarR = self.gdrCarR()

        totalR = round((gdrPointsR + gdrExpR + gdrCarR))

        return totalR


    def showDriverInfo(self):

        info = f"""
        Name: {self.name}
        Team: {self.car.team}
        Points: {self.points}
        Starts: {self.exp}
        Global Rating: {self.gdrTotalRating()}
        """

        return info
