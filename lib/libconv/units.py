''''
Units Converter
'''
from textwrap import wrap

#Convertir Metros a Kilometros

def meterKm(meters):

    km = meters / 1000
    
    return km 

#Convertir unidades de tiempo

#Convertir segundos a minutos

def secondsMin(seconds):

    minutes = seconds / 60

    return minutes

#convertir minutos a segundos

def minutesSec(minutes):

    seconds = minutes * 60

    return seconds

#convertir minutos a horas

def minutesHrs(minutes):

    hours = minutes / 60

    return hours

#convertir horas a minutos

def hoursMinutes(hours):

    minutes = hours * 60

    return minutes

#convertir segundos a horas

def secondsHrs(seconds):

    hours = seconds / 3600

    return seconds

#convertir horas a segundos

def hoursSec(hours):

    seconds = hours * 3600

    return seconds

#convertir decimal a mm:ss

def decimalMinutesConverter(time):

    converted = str(time).split('.')

    minutes = int(converted[0])

    seconds = int(converted[1])

    seconds = round(int(seconds * 60 / 100))

    converted = f"{minutes}:{seconds}"

    return converted