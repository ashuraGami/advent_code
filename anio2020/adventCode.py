# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:27:29 2020

@author: Deibby
"""
import os, requests
from collections import Counter
import re
from math import floor,ceil
import memory_profiler as mem

path = 'D:\\ScripPython\\AdventCode'
os.chdir(path)

def getInput(day_):
    url = 'https://adventofcode.com/2020/day/{}/input'.format(day_)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
    cookies = {"Cookie": "_ga=GA1.2.681339401.1607403727; _gid=GA1.2.941494419.1616951001; _gat=1; session=53616c7465645f5f9572c22225a08201265e8bf8cc74f3d47a1fc3539fc220517fcdb6a53cbabf6e784f91abad4234ad"}
    r = requests.get(url, headers = headers, cookies = cookies)
    with open("input_day_{}.txt".format(day_),'w') as f:
        f.write(r.text)

def inputList(day_):
    f = open("input_day_{}.txt".format(day_),'r')
    _input = f.readlines()
    f.close()
    inputToList = []
    for e in _input:
        inputToList.append(e[:-1])
    return inputToList

def puzzle1(inputList):
    for e in inputList:
        complement = 2020-int(e)
        if str(complement) in inputList:
            return complement*int(e)

def puzzle2(inputList):
    for e in inputList:
        if int(e)>2020: continue
        complement1 = 2020-int(e)
        for v in inputList:
            if int(v)>complement1: continue
            complement2 = complement1-int(v)
            if str(complement2) in inputList:
                return complement2*int(v)*int(e)

def puzzle3(inputList):
    c = 0
    for e in inputList:
        e = e.split(" ")
        minMax, char, word = e[0].split("-"), e[1][:-1], Counter(e[2])
        if int(minMax[0]) <= word[char] <= int(minMax[1]):
            c += 1
    return c

def puzzle4(inputList):
    c = 0
    for e in inputList:
        e = e.split(" ")
        minMax, char, word = e[0].split("-"), e[1][:-1], e[2]
        if word[int(minMax[0])-1] == char and word[int(minMax[1])-1] != char:
            c += 1
        elif word[int(minMax[0])-1] != char and word[int(minMax[1])-1] == char:
            c += 1
    return c

def puzzle5(inputList):
    c,n = 0,0
    for i, v in enumerate(inputList):
        if i == 0: continue
        c += 3
        if v[c%31]=="#":
            n += 1
    return n

def puzzle6(inputList):
    steps = {"1":1,"3":1,"5":1,"7":1,"01":2}
    n = 1
    for step in steps:
        c,k = 0,0
        for i, v in enumerate(inputList):
            if i == 0: 
                continue
            elif i%steps[step]==0:
                c += int(step)
                if v[c%31]=="#":
                    k += 1
        n *= k
    return n

def puzzle7(inputList):
    # Nota: Se debe adicionar un salto de línea más, al final de fichero input
    needed = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    word = ''
    c = 0
    for e in inputList:
        word += e
        if e == '':
            flag = True
            for need in needed:
                if need in word:
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                c += 1
            word = ''
    return c

def validatePassportPuzzle8(word):
    passportData = {}
    # c = True
    for e in word:
        e = e.split(":")
        passportData[e[0]]=e[1]
    if  len(passportData['byr'])<4 or len(passportData['iyr'])<4 or len(passportData['eyr'])<4:
        return 0
    elif int(passportData['byr'])<1920 or int(passportData['byr'])>2002:
        return 0
    elif int(passportData['iyr'])<2010 or int(passportData['iyr'])>2020:
        return 0
    elif int(passportData['eyr'])<2020 or int(passportData['eyr'])>2030:
        return 0
    elif passportData['hgt'][-2:]!="cm" and passportData['hgt'][-2:]!="in":
        return 0
    elif passportData['hgt'][-2:]=="cm" and not(150<=int(passportData['hgt'][:-2])<=193):
        return 0
    elif passportData['hgt'][-2:]=="in" and not(59<=int(passportData['hgt'][:-2])<=76):
        return 0
    elif not(re.search('^#[a-f0-9]{6,6}', passportData['hcl'])):
        return 0
    elif passportData['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return 0
    elif not(re.search('[0-9]{9,9}', passportData['pid'])):
        return 0
    return 1

def puzzle8(inputList):
    # Note: One more line break should be added at the end of the input file
    # Note2: I get +1 result :c .
    needed = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    word = ''
    c = 0
    for e in inputList:
        word += " "+e
        if e == '':
            flag = True
            for need in needed:
                if need in word:
                    continue
                else:
                    flag = False
                    break
            if flag == True:
                word = (word.split(" "))[1:-1]
                j = validatePassportPuzzle8(word)
                if j == 1: print(word)
                c += j
                # print(word)
            word = ''
    return c

def puzzle9(inputList):
    ans = -1
    for code in inputList:
        rows,columns = [0,127],[0,7]
        for w in code:
            if w == "F":
                flr = floor((rows[0]+rows[1])/2)
                rows = [rows[0],flr]
            elif w == "B":
                cl = ceil((rows[0]+rows[1])/2)
                rows = [cl,rows[1]]
            elif w == "L":
                flr = floor((columns[0]+columns[1])/2)
                columns = [columns[0],flr]
            elif w == "R":
                cl = ceil((columns[0]+columns[1])/2)
                columns= [cl,columns[1]]
        rspns = rows[0]*8+columns[0]
        if rspns > ans:
            ans = rspns
    return ans

def puzzle10(inputList):
    seatsList = []
    for code in inputList:
        rows,columns = [0,127],[0,7]
        for w in code:
            if w == "F":
                flr = floor((rows[0]+rows[1])/2)
                rows = [rows[0],flr]
            elif w == "B":
                cl = ceil((rows[0]+rows[1])/2)
                rows = [cl,rows[1]]
            elif w == "L":
                flr = floor((columns[0]+columns[1])/2)
                columns = [columns[0],flr]
            elif w == "R":
                cl = ceil((columns[0]+columns[1])/2)
                columns= [cl,columns[1]]
        rspns = rows[0]*8+columns[0]
        seatsList.append(rspns)
    seatsList = sorted(seatsList)
    for i in range(len(seatsList)-1):
        remain = seatsList[i+1]-seatsList[i]
        if remain == 2:
            return seatsList[i+1]-1

def puzzle11(inputList):
    responses,count = "",0
    for group in inputList:
        if group == "":
            tupla = set(Counter(responses))
            count += len(tupla)
            responses = ""
            continue
        responses += group
    return count
        
def puzzle12(inputList):
    c,responses,count = 0,[],0
    # f = open("log.txt","w")
    for group in inputList:
        if group == "":
            if c == 1:
                counters = Counter(responses)
                # f.write("personas:{}\n".format(c))
                # f.write(str(counters)+"\n")
                count += sum(counters.values())
                # f.write("conteo:  {}\n".format(count))
            elif c>1:
                counters = Counter(responses)
                # f.write("personas:{}\n".format(c))
                # f.write(str(counters)+"\n")
                for e in counters.values():
                    if e==c:
                        e = 1
                    else:
                        continue
                    count += e
                # f.write("conteo:  {}\n".format(count))
            c,responses = 0,[]
            continue
        c += 1
        for response in group:
            responses.append(response)
    # f.close()
    return count

def puzzle13_(inputList):
    # No es la mejor lógica, creo que se puede hacer con arboles, pero no me salió :c
    print(str(mem.memory_usage()) + 'MB')
    containers = set()
    for bag in inputList:
        bag = (bag.replace(".","").replace(" bags","").replace(" bag","")).split(" contain ")
        bag[0] = bag[0].replace(" ","_")
        bag[1] = bag[1].split(", ")
        interior_bag = []
        for inBag in bag[1]:
            interior_bag.append(inBag[2:].replace(" ","_"))
        bag[1] = interior_bag
        if "shiny_gold" in bag[1]:
            containers.add(bag[0])
    flag, num = True, len(containers)
    while flag:
        cont = containers.copy()
        for container in cont:
            for bag in inputList:
                bag = (bag.replace(".","").replace(" bags","").replace(" bag","")).split(" contain ")
                bag[0] = bag[0].replace(" ","_")
                bag[1] = bag[1].split(", ")
                interior_bag = []
                for inBag in bag[1]:
                    interior_bag.append(inBag[2:].replace(" ","_"))
                bag[1] = interior_bag
                if container in bag[1]:
                    containers.add(bag[0])
        if len(containers) == num:
            flag = False
        else:
            num = len(containers)
    print(str(mem.memory_usage()) + 'MB')
    return (len(containers))

    
def puzzle13(inputList):
    print(str(mem.memory_usage()) + 'MB')
    bags_dict = {}
    def parentBag(childbag):
        for parent in bags_dict:
            content = bags_dict[parent]
            if childbag in content:
                parentBag(parent)
                bagset.add(parent)
        return
    for bag in inputList:
        bag = (bag.replace(".","").replace(" bags","").replace(" bag","")).split(" contain ")
        bag[0],bag[1] = bag[0].replace(" ","_"),bag[1].replace(", ",",").replace(" ","_")
        bags_dict[bag[0]] = bag[1]
    # print(len(bags_dict))
    bagset = set()
    parentBag("shiny_gold")
    print(str(mem.memory_usage()) + 'MB')
    return str(len(bagset))

def puzzle14(inputList):
    print(str(mem.memory_usage()) + 'MB')
    def add_children(parent_bag):
        parent_contents = bags_dict[parent_bag]
        if parent_contents[0] == "no_other":
            return
        else:
            for child in parent_contents:
                name = child[2:]
                count = int(child[0])
                if name in children_count:
                    children_count[name] += count
                else:
                    children_count[name] = count
                for x in range(count):
                    add_children(name)
            return
    bags_dict = {}
    for bag in inputList:
        bag = (bag.replace(".","").replace(" bags","").replace(" bag","")).split(" contain ")
        bag[0],bag[1] = bag[0].replace(" ","_"),(bag[1].replace(", ",",").replace(" ","_")).split(",")
        bags_dict[bag[0]] = bag[1]
    children_count = {}
    add_children("shiny_gold")
    print(str(mem.memory_usage()) + 'MB')
    return sum(children_count.values())

def puzzle15(inputList):
    commands = {'nxt_jmp':1, "acc":0, "steps": []}
    print(str(mem.memory_usage()) + 'MB')
    while True:
        inst = inputList[commands["nxt_jmp"]].split(' ')
        if commands["nxt_jmp"] in commands["steps"]:
            break
        commands["steps"].append(commands["nxt_jmp"])
        if inst[0] == 'acc':
            commands["nxt_jmp"] += 1
            commands["acc"] += int(inst[1])
        elif inst[0] == 'jmp':
            commands["nxt_jmp"] += int(inst[1])
        elif inst[0] == 'nop':
            commands["nxt_jmp"] += 1
    print(str(mem.memory_usage()) + 'MB')
    return commands["acc"]

def puzzle16(inputList):
    endLine = len(inputList) - 1
    
    def replaceInstruction(s):
        if s == 'jmp':
            return "nop"
        elif s == "nop":
            return "jmp"
    
    def runInstructions(inputListCopy):
        commands = {'nxt_jmp':1, "acc":0, "steps": []}
        while commands['nxt_jmp'] < endLine:
            inst = inputListCopy[commands["nxt_jmp"]].split(' ')
            if commands["nxt_jmp"] in commands["steps"]:
                return True, commands["acc"]
            commands["steps"].append(commands["nxt_jmp"])
            if inst[0] == 'acc':
                commands["nxt_jmp"] += 1
                commands["acc"] += int(inst[1])
            elif inst[0] == 'jmp':
                commands["nxt_jmp"] += int(inst[1])
            elif inst[0] == 'nop':
                commands["nxt_jmp"] += 1
        return False, commands["acc"]
    
    for idx,elm in enumerate(inputList):
        inputListCopy = inputList.copy()
        inst = elm.split(" ")
        if inst[0] == "jmp" or inst[0] == "nop":
            inst[0] = replaceInstruction(inst[0])
            inputListCopy[idx] = "{} {}".format(inst[0], inst[1])
            flag, acc = runInstructions(inputListCopy)
            if flag:
                continue
            else:
                print(str(mem.memory_usage()) + 'MB')
                return acc

def puzzle17(inputList):
    nPrmbl = 25
    for elm in range(nPrmbl,len(inputList)-1):
        preamble = inputList[elm-nPrmbl:elm]
        number = int(inputList[elm])
        flag = False
        for i in preamble:
            if int(i)*2 == number: continue
            elif str(abs(number - int(i))) in preamble:
                flag = False
                break
            flag = True
        if flag:
            return number

def puzzle18(inputList):
    return

if __name__=="__main__":
    nroPuzzle = 18
    day_ = ceil(nroPuzzle/2)
    getInput(day_)
    # print(str(mem.memory_usage()) + 'MB')
    # inputList = inputList(day_)
    # print(str(mem.memory_usage()) + 'MB')
    # ans = puzzle18(inputList)
    # print("The answer is:",ans)


