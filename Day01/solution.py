import pandas as pd
import os

def part1(data): 
    pass

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
    print(f"Part 2: {part2(input_data)}")