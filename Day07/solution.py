import re
#import pandas as pd
import os
import operator

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

def part1(input): 
    operations = ['*', '+']
    print(input)
    pass

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