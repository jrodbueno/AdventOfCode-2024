import re
import os

#from networkx import difference

def part1(list1, list2): 
    #Calculate accumulated difference
    difference = 0
    for i in range(len(list1)):
        difference += abs(int(list1[i])-int(list2[i]))
    return difference

def part2(list1, list2):
    #Find simmilarity score
    sim = 0
    for item1 in list1:
        count = 0
        for item2 in list2:
            if item1 == item2:
                count +=1
        sim += int(item1)*count
    return sim

def parse_input(file_path):
    with open(file_path) as f:
        data = f.read().splitlines()
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
    return [list1,list2]

if __name__ == "__main__":
    input_data = parse_input("Input.txt")
    print(f"Part 1: {part1(input_data[0],input_data[1])}")
    print(f"Part 2: {part2(input_data[0],input_data[1])}")