import  os, sys
import requests
import string

def get_current_path():
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    path = os.path.abspath(path)
    return path


def getInput(advent_year, advent_day, path, nro):
    url = 'https://adventofcode.com/{}/day/{}/input'.format(advent_year, advent_day)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    ## The cookies must be obtained from each account
    cookies = {"Cookie": "ru=53616c7465645f5f0365e106f769d80b8db299e55b1323b71af26e04e664a5a757e1f86a8e61a4511391701bdee6f0c6; session=53616c7465645f5fd6686a7fa1776fc22991f852d3c7daee1cceafc1e703633eebc83cec64219d5b05c4395b5f44d02482ecd2b8eb3200d5395eca0823d2c91c"}
    r = requests.get(url, headers = headers, cookies = cookies)
    with open("{}/anio{}/input_day_{}_{}.txt".format(path, advent_year, advent_day, nro),'w') as f:
        f.write(r.text)


def inputList(advent_year, advent_day, path, nro):
    inputToList = open("{}/anio{}/input_day_{}_{}.txt".format(path, advent_year, advent_day, nro),'r')\
                    .read()\
                    .splitlines()
    return inputToList


def getPoint():
    lowers = {}
    uppers = {}
    value = 1

    for i in list(string.ascii_lowercase):
        lowers[i]=value
        value += 1
    for i in list(string.ascii_uppercase):
        uppers[i]=value
        value += 1

    alph_priority = lowers.copy()
    alph_priority.update(uppers)

    return alph_priority

def getClearStructure(input):
    ## We separate the stacks of boxes from the movements
    for i, v in enumerate(input):
        if v == '': break

    boxOrder = input[:i]
    moves = input[i+1:]

    ## We clean the lines to obtain lists with which we can work better
    clear = lambda x: x.replace('    ','_')\
                        .replace('[','')\
                        .replace(']','')\
                        .replace(' ','')
    boxMatriz = []
    order = []
    for i in boxOrder:
        if '[' in i:
            if i[0] == '[':
                boxMatriz.append(list(clear(i)))
            else:
                boxMatriz.append(list(clear(i)))
        else:
            order = (list(i[1:-1].replace(' ','')))

    ## We create the structure of stacks of boxes
    stacks = {}
    for i in order:
        stacks[int(i)] = list()

    ## we fill the stacks
    for row in boxMatriz[::-1]:
        for i, v in enumerate(row):
            if v == '_': continue
            stack = stacks[i+1]
            stack.append(v)
            stacks[i+1] = stack

    ## We formatting the movements
    clear = lambda x: x.replace('move', '')\
                        .replace('from', '|')\
                        .replace('to', '|')\
                        .replace(' ', '')
    moves = [clear(x) for x in moves]
    moves = [x.split('|') for x in moves]

    return stacks, moves