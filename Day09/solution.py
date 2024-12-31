import re
#import pandas as pd
import os

#from networkx import difference

def part1(input): 
    pass

def part2(input):
    pass

def parse_input(file_path):
    #Read File into a list, one item per linegi
    with open(file_path) as f:
        data = f.read().splitlines()
    #print(data)
    #Build report list "a list of lists"
    reports = []
    for item in data:
        list_items = re.findall(r'\d+', item)
        reports.append(list_items)
    return reports

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")