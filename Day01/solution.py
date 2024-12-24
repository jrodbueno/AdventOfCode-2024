import re
#import pandas as pd
import os

#from networkx import difference

def part1(data): 
    #define lists
    list1 = []
    list2 = []  
    #build lists
    for item in data:
        list_items = re.findall(r'\d+', item)
        list1.append(list_items[0])
        list2.append(list_items[1])
    #Sort lists smallest to largest
    list1.sort()
    list2.sort()
    #Calculate accumulated difference
    difference = 0
    for i in range(len(list1)):
        difference += abs(int(list1[i])-int(list2[i]))
    return difference

def part2(data):
    # Your solution for part 2
    pass

def parse_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

if __name__ == "__main__":
    #print(f"Current working directory: {os.getcwd()}")
    input_data = parse_input("Input.txt")
    print(f"Part 1: {part1(input_data)}")
    #print(f"Part 2: {part2(input_data)}")