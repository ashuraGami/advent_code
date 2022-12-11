from commons import *


def solutions2021(year, days, path):
    day, nro = days.split('-')[0], days.split('-')[1]
    getInput(year, day, path, nro)

    input = inputList(year, day, path, nro)