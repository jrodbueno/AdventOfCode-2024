import re
#import pandas as pd
import os

#from networkx import difference

def part1(instructions):
    total = 0
    for instruction in instructions:
        multiples = re.findall(r'\d+',instruction)
        total += int(multiples[0]) * int(multiples[1])
    return total

def part2(instructions):
    total = 0
    multiply = True
    for instruction in instructions:
        #print(instruction)
        if instruction == "do()":
            multiply = True
            continue
        elif instruction == "don't()":  
            multiply = False  
            continue
        if multiply == True:
            multiples = re.findall(r'\d+',instruction)
            total += int(multiples[0]) * int(multiples[1])  
    return total

def parse_input_part1(file_path):
    #Read File into a list, one item per linegi
    with open(file_path) as f:
        data = f.read()
    list_items = re.findall(r'mul\([0-9]+,[0-9]+\)', data)
    return list_items

def parse_input_part2(file_path):
    #Read File into a list, one item per linegi
    with open(file_path) as f:
        data = f.read()
    #print(data)
    #Build report list "a list of lists"
    pattern = r"(?:do\(\))|(?:don't\(\))|(?:mul\([0-9]+,[0-9]+\))"
    list_items = re.findall(pattern, data)
    return list_items

if __name__ == "__main__":
    input_data = parse_input_part1("Input.txt")
    print(f"Part 1: {part1(input_data)}")
    input_data2 = parse_input_part2("Input.txt")
    print(f"Part 2: {part2(input_data2)}")