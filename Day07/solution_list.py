import re
#import pandas as pd
import os
import operator
from copy import copy, deepcopy
import csv

ops = {
    '*': operator.mul,
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '||': operator.concat
}

def determine_operator_part2 (row,col,row_size,col_size):
    #recibir una columna para saber cuántas veces tiene que haber cierto signo
    #recibir una fila para saber cuántas veces más tiene que ir un signo
    exponent = col_size-2
    repeats = []
    for i in range(exponent,0,-1):
        repeats.append(3**i)
    repeats.append(1)
    if (row//repeats[col] % 3 == 0):
        return "+"
    if (row//repeats[col] % 3 == 1):
        return "*"
    else:
        return "||"
    
def determine_operator (row,col,row_size,col_size):
    #recibir una columna para saber cuántas veces tiene que haber cierto signo
    #recibir una fila para saber cuántas veces más tiene que ir un signo
    exponent = col_size-2
    repeats = []
    for i in range(exponent,0,-1):
        repeats.append(2**i)
    repeats.append(1)
    if (row//repeats[col] % 2 == 0):
        return "+"
    else:
        return "*"

def part1(input): 
    operations = ['*', '+']
    sum = 0
    for row in input:
        result = row[0]
        list = row[1]
        #print(list)
        solutions = deepcopy([list])
        i = 0
        duplicate = len(list)-1
        #get all the possibilities
        while i < duplicate:
            solutions.extend(deepcopy(solutions))
            i += 1
        size = len(solutions)
        #insert the operation (+/*) in the correct place
        for i, solution in enumerate(solutions):
            col = 0
            for j,item in enumerate (solution):
                if(j%2 == 1):
                    col = int(j/2)
                    oper = determine_operator(i,col,size,len(list))
                    solution.insert(j,oper)  
        #print(f"{size},{len(list)}")
        #print('\n'.join(map(str,solutions)))
        for i,solution in enumerate(solutions):
            total = 0
            j =0
            while j < len(solution) - 1:
                if j == 0:
                    total = int(solution[j])
                total = ops[solution[j+1]](total,int(solution[j+2]))
                j += 2
            if total == int(result):
                sum += total
                break     
    return sum

def part2(input):
    operations = ['+', '*','||']
    sum = 0
    for row in input:
        result = row[0]
        list = row[1]
        #print(list)
        solutions = deepcopy([list])
        intermediate = deepcopy([list])
        i = 0
        duplicate = len(list)
        #get all the possibilities
        while i < duplicate:
            intermediate.extend(deepcopy(solutions))
            solutions.extend(deepcopy(intermediate))
            i += 1
        size = len(solutions)
        #insert the operation (+/*) in the correct place
        for i, solution in enumerate(solutions):
            col = 0
            for j,item in enumerate (solution):
                if(j%2 == 1):
                    col = int(j/2)
                    oper = determine_operator_part2(i,col,size,len(list))
                    solution.insert(j,oper)  
        #print(f"{size},{len(list)}")
        #print('\n'.join(map(str,solutions)))
        for i,solution in enumerate(solutions):
            total = 0
            j =0
            #print(i)
            while j < len(solution) - 1:
                if j == 0:
                    total = int(solution[j])
                if solution[j+1] == '||':
                    total = int(ops[solution[j+1]](str(total),solution[j+2]))
                else:
                    total = ops[solution[j+1]](total,int(solution[j+2]))
                j += 2
            if total == int(result):
                sum += total
                break     
        with open('path.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(solutions)
    return sum

def parse_input(file_path):
    with open(file_path) as f:
        data = f.read().splitlines()
    records = []
    for item in data:
        list_items = item.split(":")
        list_items[1] = list_items[1].split(" ") # type: ignore
        for number in list_items[1]:
            if len(number) == 0:
                list_items[1].pop(list_items[1].index(number))
        records.append(list_items)
    return records

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    #print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")




