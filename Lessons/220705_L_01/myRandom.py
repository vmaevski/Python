import datetime

def myRandomInt(min, max):  # возвращает случайное целое число N, min <= N <= max
    return min + round((max - min) * datetime.datetime.now().microsecond / 1000000)
