import re
import csv
#import pandas as pd
import os
import sys
sys.setrecursionlimit(150000)

def find_guard(map,guard):
    ver,hor = 0,0
    for row in map:
        if guard in row:
            hor = row.index(guard)
            ver = map.index(row)
    return ver,hor

def move (map, loc = [0,0], dir = [1,0], obstacle = '#',count=0):
    hbound = len(map[1])-1
    vbound = len(map)-1
    if loc[0] + dir[0] > vbound or loc[1] + dir[1] > hbound:
        map[loc[0]][loc[1]] = "X"
        return "Out",loc, count
    if map[loc[0] + dir[0]][loc[1] + dir[1]] == 'X':
        count += 1
        print(count)
    if map[loc[0] + dir[0]][loc[1] + dir[1]] == obstacle:
        dir = turn_right(dir)
    else:
        map[loc[0]][loc[1]] = "X"
        loc = [loc[0] + dir[0],loc[1] + dir[1]]
       # print(f"{loc} | {dir} | {count}")
    return move(map,loc,dir,obstacle,count)

def turn_right(direction = [-1,0]):
    if direction == [-1,0]:
        return [0,1]
    if direction == [0,1]:
        return [1,0]
    if direction == [1,0]:
        return [0,-1]
    if direction == [0,-1]:
        return [-1,0]
    return direction

def part1(map): 
    count = 0
    guard = '^'
    obstacle = '#'
    direction = [-1,0]
    guard_loc = find_guard(map,guard)
    movement = move(map,guard_loc,direction,obstacle, count)
    print (movement[2])
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(map)
    for row in map:
        for cell in row:
            if cell == 'X':
                count +=1
    return count

def part2(input):
    pass

def parse_input(file_path):
    #Read File into a list, one item per linegi
    with open(file_path) as f:
        data = f.read().splitlines()
    #print(data)
    #Build report list "a list of lists"
    lines = []
    for item in data:
        lines.append(list(item))
    return lines

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")