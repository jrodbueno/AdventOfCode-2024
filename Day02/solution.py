import re
#import pandas as pd
import os
#from networkx import difference

def part1(reports): 
    #Calculate accumulated difference
    print(reports)
    pass

def part2(reports):
    #Find simmilarity score
    pass

def parse_input(file_path):
    with open(file_path) as f:
        data = f.read().splitlines()
    #define lists
    #print(data)
    reports = []
    #build lists
    for item in data:
        list_items = re.findall(r'\d+', item)
        reports.append(list_items)
    return reports

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")