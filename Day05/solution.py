import re
#import pandas as pd
import os

def check_print (dict,printset):
    value = printset.pop(0)
    if value not in dict:
        #print("Value not in dictionary")
        return False
    if len(printset) == 0:
        #print(f"last item: {value}")
        return True
    for item in printset:
        if item in dict[value]:
            #print(f"Broken instruction: {printset},value: {value}, item: {item}")
            return False
    return check_print(dict,printset)

def part1(instructions,prints): 
    sum = 0
    inst_dict = build_instruction_dict(instructions)
    for printset in prints:
        #print(f"Starting validation: {printset}")
        if check_print (inst_dict,printset.copy()):
            #print(f"valid print set: {printset}")
            index = len(printset)
            if index%2 ==0:
                #print(printset)
                index = index/2
                sum += (printset[index] + printset[index-1])/2
            else:
                index = int(index/2)
                sum += int(printset[index])
    return sum

def part2(input):
    pass

def parse_input(file_path):
    #Read File into a list, one item per linegi
    with open(file_path) as f:
        data = f.read().splitlines()
    #print(data)
    #Build report list "a list of lists"
    return data
def get_instructions(data):
    instructions = []
    for item in data:
        if "|" in item:
            instructions.append(item.split('|'))
    return instructions

def get_prints(data):
    prints = []
    for item in data:
        if "|" not in item:
            if len(item) > 0:
                prints.append(item.split(','))
    return prints

def build_instruction_dict(instructions):
    #encontrar todas las páginas X que tienen que estar impresas antes que Y
    #[X,Y]
    dictionary = {}
    for instruction in instructions:
        if instruction[1] in dictionary:
            ls = []
            ls = dictionary[instruction[1]]
            ls.append(instruction[0])
            dictionary.update({instruction[1]:ls})
        else:
            dictionary[instruction[1]] = [instruction[0]]
    return dictionary

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    instructions = get_instructions(input_data)
    prints = get_prints(input_data)
    print(f"Part 1: {part1(instructions,prints)}")
    print(f"Part 2: {part2(input_data)}")