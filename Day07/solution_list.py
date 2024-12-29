import re
#import pandas as pd
import os
import operator
from copy import copy, deepcopy

ops = {
    '*': operator.mul,
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv
}
"""
# Parse string manually
num1, op, num2 = string[0], string[1], string[2]
result = ops[op](int(num1), int(num2))
print(result)  # 9
"""
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
        #Create Tree
        print(list)
        solutions = deepcopy([list])
        i = 0
        duplicate = len(list)-1
        #get all the possibilities
        while i < duplicate:
            solutions.extend(deepcopy(solutions))
            i += 1
        size = len(solutions)
        #insert the operation in the correct place
        for i, solution in enumerate(solutions):
            col = 0
            for j,item in enumerate (solution):
                if(j%2 == 1):
                    col = int(j/2)
                    oper = determine_operator(i,col,size,len(list))
                    solution.insert(j,oper)  
            #insert on 1,3,5... len-2
            #insert with an exponencial iterative pattern
        print(f"{size},{len(list)}")
        print('\n'.join(map(str,solutions)))
        
        """
            if len(solutions) == 0:
                solution.append(item)
                solutions.append(solution.copy())
                OperatorSet = False
            elif OperatorSet:
                for solution in solutions:
                    solution.append(item)
                OperatorSet = False
            else:
                solutions = deepcopy(solutions)
                solutions.extend(deepcopy(solutions))
                len(operations)
                i=0
                for index, sol in enumerate(deepcopy(solutions)):
                    solutions[index].append(operations[i])

                    i = (i + 1) % len(operations)
                OperatorSet = True

        solutions = list.copy()
        last_index = (len(solutions)-1)
        i = 0
        while i < last_index and i<= 10:
            last_index = (len(solutions)-1)
            item = solutions[i]
            #print(item)
            if item in operations:
                continue
            for operation in operations:
                solution = list.copy()
                solution.insert(i+1,operation)
                solutions.append(solution)
            i += 1
        """

                    
                    
    return sum

def part2(input):
    pass

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
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")




