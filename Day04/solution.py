import re
#import pandas as pd
import os

#from networkx import difference
def find_paths (row,col,input,targetChar):
    directions = []
    for vertical in range(row - 1, row + 2):
        if(vertical < 0 or vertical >= len(input)):
            continue
        for horizontal in range(col - 1, col +2):
            if(horizontal < 0 or horizontal >= len(input[vertical])):
                continue
            if input[vertical][horizontal] == targetChar:
                directions.append([vertical,horizontal])
    return directions

def part1(input): 
    count = 0
    target = "XMAS"
    #print(len(target))
    for row in range(len(input)):
        for col in range(len(input[row])):
            cell = input[row][col]
            #find Xs
            if cell == target[0]:
                #find directions where to find the next character 'M'
                directions = find_paths(row,col,input,target[1])
                #evaluate for the whole word in each direction
                if len(directions) == 0:
                    continue
                for direction in directions:
                    vmove = direction[0] - row
                    hmove = direction[1] - col
                    word = [input[row][col],input[direction[0]][direction[1]]]
                    for i in range(2,len(target)):
                        #print(i)
                        if(row + (vmove * i) >= len(input) or row + (vmove * i) < 0):
                            continue
                        if(col + (hmove * i) >= len(input[row + (vmove*i)]) or col + (hmove * i) < 0):
                            continue
                        letter = input[row + (vmove * i)][col + (hmove * i)]
                        if(letter == target[i]):
                            word.append(letter)
                        else:
                            break
                        continue
                    if(len(word) == len(target)):
                        #print(f"{word} - [{row},{col}] - h: {hmove}  v: {vmove}")
                        count += 1
                        #print(count)
                    continue
            else:
                continue
    #print (sum)
    return count

def part2(input):
    count = 0
    for row in range(1,len(input)-1):
        for col in range(1,len(input[row])-1):
            cell = input[row][col]
            #find As
            if cell == "A":
                C1 = f"{input[row-1][col-1]}{input[row][col]}{input[row+1][col+1]}"
                C2 = f"{input[row+1][col-1]}{input[row][col]}{input[row-1][col+1]}"
                if C1 in ["SAM","MAS"] and C2 in ["SAM","MAS"]:
                    count+=1
    return count

def parse_input(file_path):
    #Read File into a list, one item per linegi
    with open(file_path) as f:
        lines = f.read().splitlines()
    #print(data)
    #Build report list "a list of lists"
    Characters = []
    pattern = r'(?:[XMAS])'
    for line in lines:
        list_items = re.findall(pattern, line)
        Characters.append(list_items)
    return Characters

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")