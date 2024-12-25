from operator import truediv
import re
#import pandas as pd
import os
import stat
#from networkx import difference
def evaluate_report(report):
    #Determine if a report is safe if:
    #The levels are either all increasing or all decreasing.
    #Any two adjacent levels differ by at least one and at most three.
    status = "First"
    for level in range(len(report)-1):
        delta = int(report[level+1])-int(report[level])
        if delta > 0 and delta <= 3 and (status in ("First","Ascending")):
            status = "Ascending"
        elif delta < 0 and delta >= -3 and (status in ("First","Descending")):
            status = "Descending"
        else:
            #print("unsafe")
            status = level+1
            break
        if level == len(report)-2:
            status = "Safe"
    return status

def part1(reports): 
    #print(reports)
    safeReports = 0
    for report in reports:
        if evaluate_report(report) == "Safe":
            safeReports += 1
    return safeReports

def part2(reports):
    #Determine how many reports are safe if you can skip one level
    #print(reports)
    safeReports = 0
    for report in reports:
        eval = evaluate_report(report)
        if eval == "Safe":
            safeReports += 1
            continue
        else:
            for index in range(len(report)):
                newreport = report.copy()
                del newreport[index]
                eval = evaluate_report(newreport)
                if eval == "Safe":
                    safeReports += 1
                    break
    return safeReports

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