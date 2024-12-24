from operator import truediv
import re
#import pandas as pd
import os
import stat
#from networkx import difference

def part1(reports): 
    #Determine how many reports are safe if:
    #The levels are either all increasing or all decreasing.
    #Any two adjacent levels differ by at least one and at most three.
    #print(reports)
    safeReports = 0
    delta = 0
    for report in reports:
        status = "First"
        for level in range(len(report)-1):
            delta = int(report[level+1])-int(report[level])
            if delta > 0 and delta <= 3 and (status in ("First","Ascending")):
                status = "Ascending"
            elif delta < 0 and delta >= -3 and (status in ("First","Descending")):
                status = "Descending"
            else:
                #print("unsafe")
                status = "Unsafe"
                break
            if level == len(report)-2:
                #print("safe!")
                safeReports += 1
    return safeReports

def part2(reports):
    #Find simmilarity score
    pass

def parse_input(file_path):
    #Read File into a list, one item per line
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