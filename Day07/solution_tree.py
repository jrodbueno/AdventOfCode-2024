import re
#import pandas as pd
import os
import operator

class OperationNode:
    def __init__(self, value):
        self.value = value        # Value in this node
        self.add = None          # Addition branch/child
        self.multiply = None 
        self.parent = None 

    def __str__(self):
        return ','.join(map(str, self.value))
    
    def add_child(self, value, branch="+"):
        # Create a new family member
        new_child = OperationNode(child_name)
        # Add them as left or right child
        if branch == "+" and self.add is None:
            self.add = new_child
        elif branch == "*" and self.multiply is None:
            self.add = new_child
        else:
            print(f"Can't add {child_name} as {branch} child - spot taken!")

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
    sum = 0
    for row in input:
        result = row[0]
        list = row[1]
        root = ''
        #Create Tree
        print(list)
        for i in range(len(list)-1):
            print(item)
            if i == 0:
                root = OperationNode(list[i]) 
                root.add_child(list[i+1],'+')
                root.add_child(list[i+1],'*')
            else:
                node = OperationNode(list[i]) 
                root.add_child(list[i+1],'+')
                root.add_child(list[i+1],'*')
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