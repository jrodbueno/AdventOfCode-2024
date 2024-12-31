from copy import deepcopy
from itertools import count
import re
#import pandas as pd
import os
import numpy as np

#from networkx import difference

def part1(input): 
    #get antennas
    count = 0
    antennas = {}
    bounds = (len(input)-1,len(input[1])-1)
    map = deepcopy(input)
    for i,row in enumerate(input):
        for j,item in enumerate(row):
            if item == ".":
                continue
            elif item in antennas:
                aux = []
                for antenna in antennas[item]:
                    aux.append(antenna)
                #print(aux)
                aux.append((i,j))
                antennas.update({item: aux})
                continue
            else:
                antennas[item] = [(i,j)]

    for antenna in antennas:
        total_positions = len(antennas[antenna])
        for i in range(total_positions):
                p1 = antennas[antenna][i]
                for j in range(i+1,total_positions):
                    p2 = antennas[antenna][j]
                    delta = (p2[0]-p1[0],p2[1]-p1[1])
                    an1 = (p1[0]-delta[0],p1[1]-delta[1]) 
                    if (an1[0] <= bounds[0] and an1[0] >= 0) and (an1[1] <= bounds[1] and an1[1] >= 0):
                        map[an1[0]][an1[1]] = '#'
                    an2 = (p2[0]+delta[0],p2[1]+delta[1])
                    if (an2[0] <= bounds[0] and an2[0] >= 0) and (an2[1] <= bounds[1] and an2[1] >= 0):
                        map[an2[0]][an2[1]] = '#'
                    continue
    for row in map:
        for cell in row:
            if cell == '#':
                count += 1
    return count

def part2(input):
    count = 0
    antennas = {}
    bounds = (len(input)-1,len(input[1])-1)
    map2 = deepcopy(input)
    for i,row in enumerate(input):
        for j,item in enumerate(row):
            if item == ".":
                continue
            elif item in antennas:
                aux = []
                for antenna in antennas[item]:
                    aux.append(antenna)
                #print(aux)
                aux.append((i,j))
                antennas.update({item: aux})
                continue
            else:
                antennas[item] = [(i,j)]

    for antenna in antennas:
        total_positions = len(antennas[antenna])
        if len(antennas[antenna]) == 1:
            continue
        for i in range(total_positions):
                p1 = antennas[antenna][i]
                map2[p1[0]][p1[1]] = '#'
                for j in range(i+1,total_positions):
                    p2 = antennas[antenna][j]
                    map2[p2[0]][p2[1]] = '#'
                    delta = (p2[0]-p1[0],p2[1]-p1[1])
                    an1 = (p1[0]-delta[0],p1[1]-delta[1]) 
                    while (an1[0] <= bounds[0] and an1[0] >= 0) and (an1[1] <= bounds[1] and an1[1] >= 0):
                        map2[an1[0]][an1[1]] = '#'
                        an1 = (an1[0]-delta[0],an1[1]-delta[1]) 
                    an2 = (p2[0]+delta[0],p2[1]+delta[1])
                    while (an2[0] <= bounds[0] and an2[0] >= 0) and (an2[1] <= bounds[1] and an2[1] >= 0):
                        map2[an2[0]][an2[1]] = '#'
                        an2 = (an2[0]+delta[0],an2[1]+delta[1]) 
                    continue
    for row in map2:
        for cell in row:
            if cell == '#':
                count += 1
    return count

def parse_input(file_path):
    #Read File into a list, one item per linegi
    with open(file_path) as f:
        data = f.read().splitlines()

    #print(data)
    #Build report list "a list of lists"
    reports = []
    for item in data:
        list_items = re.findall(r'.', item)
        reports.append(list_items)
    return reports

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")