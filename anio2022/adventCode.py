from commons import *
from collections import defaultdict

def puzzle1_1(input, days):
    input = ",".join(input)
    input = input.split(",,")

    max_val = -1
    for v in input:
        sigma = sum([int(x) for x in v.split(',')])
        if max_val < sigma:
            max_val = sigma

    print("The solution of puzzle {} is: {}".format(days, max_val) )

def puzzle1_2(input, days):
    input = ",".join(input)
    input = input.split(",,")

    total_list = []
    for v in input:
        total_list.append(sum([int(x) for x in v.split(',')]))
    
    print("The solution of puzzle {} is: {}".format(days, sum(sorted(total_list)[-3:])))


def puzzle2_1(input, days):
    # A=Rock, B=Paper, C=Scissors
    # X=Rock, Y=Paper, Z=Scissors
    # Points X:1, Y:2, Z:3
    # Points lose:0, draw:3, win:6

    moves = {"A X":4, "A Y":8, "A Z":3,
            "B X":1, "B Y":5, "B Z":9,
            "C X":7, "C Y":2, "C Z":6}

    result = 0
    for i in input:
        result += moves[i]    

    print("The solution of puzzle {} is: {}".format(days, result))

def puzzle2_2(input, days):
    # A=Rock, B=Paper, C=Scissors
    # X=Lose, Y=Draw, Z=Win
    # Points Rock:1, Paper:2, Scissors:3
    # Points X:0, Y:3, Z:6

    moves = {"A X":3, "A Y":4, "A Z":8,
         "B X":1, "B Y":5, "B Z":9,
         "C X":2, "C Y":6, "C Z":7}

    result = 0
    for i in input:
        result += moves[i]    

    print("The solution of puzzle {} is: {}".format(days, result))


def puzzle3_1(input, days):
    alph_priority = getPoint()

    result = 0
    for i in input:
        lenght = int(len(i)/2)
        value = set(list(i[:lenght])).intersection(set(list(i[lenght:])))
        result += alph_priority[list(value)[0]]

    print("The solution of puzzle {} is: {}".format(days, result))

def puzzle3_2(input, days):
    alph_priority = getPoint()

    index = 0
    result = 0
    while index < len(input):
        group = input[index:index+3]
        group = [set(list(x)) for x in group]
        result += alph_priority[list(
                                (group[0].intersection(group[1])).intersection(group[2])
                                )[0]]
        index += 3

    print("The solution of puzzle {} is: {}".format(days, result))


def puzzle4_1(input, days):
    result = 0
    for i in input:
        pairs = i.split(',')
        
        pair1 = pairs[0].split('-')
        pair2 = pairs[1].split('-')

        condition1 = int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1])
        condition2 = int(pair2[0]) <= int(pair1[0]) and int(pair2[1]) >= int(pair1[1])
        
        if condition1 or condition2:
            result += 1
    
    print("The solution of puzzle {} is: {}".format(days, result))

def puzzle4_2(input, days):
    result = 0
    for i in input:
        pairs = i.split(',')
        pair1 = pairs[0].split('-')
        pair2 = pairs[1].split('-')

        rango1 = set([x for x in range(int(pair1[0]),int(pair1[1])+1)])
        rango2 = set([x for x in range(int(pair2[0]),int(pair2[1])+1)])
        
        if len(rango1.intersection(rango2)) > 0:
            result += 1

    print("The solution of puzzle {} is: {}".format(days, result))


def puzzle5_1(input, days):
    stacks, moves = getClearStructure(input)
    
    for i in moves:
        boxes = stacks[int(i[1])][-int(i[0]):]
        boxes = boxes[::-1]

        stacks[int(i[1])] = stacks[int(i[1])][:-int(i[0])]

        stack_simple = stacks[int(i[2])]
        stack_simple += boxes
        
        stacks[int(i[2])] = stack_simple

    result = ''.join([x[-1] for x in stacks.values()])

    print("The solution of puzzle {} is: {}".format(days, result))


def puzzle5_2(input, days):
    stacks, moves = getClearStructure(input)

    for i in moves:
        boxes = stacks[int(i[1])][-int(i[0]):]

        stacks[int(i[1])] = stacks[int(i[1])][:-int(i[0])]

        stack_simple = stacks[int(i[2])]
        stack_simple += boxes
        
        stacks[int(i[2])] = stack_simple

    result = ''.join([x[-1] for x in stacks.values()])

    print("The solution of puzzle {} is: {}".format(days, result))


def puzzle6_1(input, days):
    input = list(input[0])
    result = 0
    while True:
        if len(set(input[result:result+4])) == 4:
            break
        result += 1
    
    print("The solution of puzzle {} is: {}".format(days, result+4))

def puzzle6_2(input, days):
    input = list(input[0])
    result = 0
    while True:
        if len(set(input[result:result+14])) == 14:
            break
        result += 1
    
    print("The solution of puzzle {} is: {}".format(days, result+14))


def puzzle7_1(input, days):
    max_size = 100000
    prefix = ""
    roots = []
    sizes = {}
    tree = defaultdict(list)
    for i in input:
        if i[0] == '$': #and i != '$ ls':
            if i != '$ ls':
                head = i.replace('$ cd ', '')

                if i == '$ cd ..': 
                    roots.pop()
                    prefix = "".join(roots)
                else:
                    roots.append(head)
                    prefix += head
                    tree[prefix] = []
        else:
            content = tree[prefix]
            content.append(prefix+i.split(' ')[1])
            tree[prefix] = content
            if i[:3] != 'dir':
                sizes[prefix+i.split(' ')[1]] = int(i.split(' ')[0])

    treeSizes = defaultdict(list)
    def sizeCalculation(size, head):
        if head in sizes.keys():
            return sizes[head]
        
        for i in tree[head]:
            size += sizeCalculation(0, i)
            treeSizes[head] = size
        
        return size

    sizeCalculation(0, '/')

    result = 0
    for i in treeSizes.values():
        if i <= max_size:
            result += i

    print("The solution of puzzle {} is: {}".format(days, result))

def puzzle7_2(input, days):
    print(input[:10])


def error(input):
    print("Error en el llamado de la función")


def launch_puzzle(days, input):
    switch_puzzle = {
        "1-1":puzzle1_1, "1-2":puzzle1_2,
        "2-1":puzzle2_1, "2-2":puzzle2_2,
        "3-1":puzzle3_1, "3-2":puzzle3_2,
        "4-1":puzzle4_1, "4-2":puzzle4_2,
        "5-1":puzzle5_1, "5-2":puzzle5_2,
        "6-1":puzzle6_1, "6-2":puzzle6_2,
        "7-1":puzzle7_1, "7-2":puzzle7_2,
        # "8-1":puzzle8_1, "8-2":puzzle8_2,
        # "9-1":puzzle9_1, "9-2":puzzle9_2,
        # "10-1":puzzle10_1, "10-2":puzzle10_2,
        # "11-1":puzzle11_1, "11-2":puzzle11_2,
        # "12-1":puzzle12_1, "12-2":puzzle12_2,
        # "13-1":puzzle13_1, "13-2":puzzle13_2,
        # "14-1":puzzle14_1, "14-2":puzzle14_2,
        # "15-1":puzzle15_1, "15-2":puzzle15_2,
        # "16-1":puzzle16_1, "16-2":puzzle16_2,
        # "17-1":puzzle17_1, "17-2":puzzle17_2,
        # "18-1":puzzle18_1, "18-2":puzzle18_2,
        # "19-1":puzzle19_1, "19-2":puzzle19_2,
        # "20-1":puzzle20_1, "20-2":puzzle20_2,
        # "21-1":puzzle21_1, "21-2":puzzle21_2,
        # "22-1":puzzle22_1, "22-2":puzzle22_2,
        # "23-1":puzzle23_1, "23-2":puzzle23_2,
        # "24-1":puzzle24_1, "24-2":puzzle24_2,
        # "25-1":puzzle25_1, "25-2":puzzle25_2,
    }
    
    switch_puzzle.get(days, error)(input, days)

def solutions2022(year, days, path):
    day, nro = days.split('-')[0], days.split('-')[1]
    getInput(year, day, path, nro)
    
    input = inputList(year, day, path, nro)
    launch_puzzle(days, input)
