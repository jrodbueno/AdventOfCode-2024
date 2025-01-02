import re
#import pandas as pd
import os
import csv

#from networkx import difference

def part1(diskmap): 
    #set ID
    IDs = range(len(diskmap))
    compact = []
    #print(list(IDs))
    k=0
    #Find files and blanks
    for i, ch in enumerate(diskmap):
        if i % 2 == 0 or i == 0: 
            for j in range(int(ch)):
                compact.append(IDs[k])
            k +=1
            continue
        else:
            for j in range(int(ch)):
                compact.append('.')
            continue
    #Reduce
    ##find last number
    last = len(compact)-1
    for i, ch in enumerate(compact):
        while compact[last] == '.':
            last += -1
        if last == i:
            break
        if ch == '.':
            compact[i] = compact[last]
            compact[last] = '.'
        if i +1 == last: 
            break
    #Checksum
    checksum = 0
    with open('output.txt', 'w') as f:
        f.write(str(compact))
    i = 0
    print(len(compact),len(IDs))
    while compact[i] != '.':
        checksum += compact[i] * i
        i += 1
    return checksum

def part2(diskmap):
        #set ID
    compact = []
    #print(list(IDs))
    k=0
    #Find files and blanks
    for i, ch in enumerate(diskmap):
        if i % 2 == 0 or i == 0: 
            for j in range(int(ch)):
                compact.append(k)
            k +=1
            continue
        else:
            for j in range(int(ch)):
                compact.append('.')
            continue
    #Reduce
    ##find last number
    last = len(compact)-1
    for i, ch in enumerate(compact):
        while compact[last] == '.':
            last += -1
        block = [0,0]
        if compact[last] != compact[last-1]:
            block = [last,last]
        else:
            while compact[last] == compact[last-1]:
                if block[1] == 0:
                    block[1] = last 
                last += -1
                if compact[last] != compact[last-1]:
                    block[0] = last+1
                    print(compact[block[0]],compact[block[1]])

        if last == i:
            break
        if ch == '.':
            compact[i] = compact[last]
            compact[last] = '.'
        if i +1 == last: 
            break
    #Checksum
    checksum = 0
    with open('output.txt', 'w') as f:
        f.write(str(compact))
    i = 0
    print(len(compact),len(IDs))
    while compact[i] != '.':
        checksum += compact[i] * i
        i += 1
    return checksum

def parse_input(file_path):
    #Read File into a list, one item per linegi
    with open(file_path) as f:
        data = f.read()
    #print(data)
    #Build report list "a list of lists"
    reports = list(data)
    return reports

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")