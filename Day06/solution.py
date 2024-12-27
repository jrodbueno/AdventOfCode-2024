from pickle import APPEND
import re
import csv
#import pandas as pd
import os
import sys
from xml.sax.saxutils import prepare_input_source
sys.setrecursionlimit(15000)

#otro enfoque es poner los # para crear el loop
# y leer si el guardia ya estuvo allí 
#¿cómo saber si el guardia ya estuvo allí? 
#probablemente leyendo los dos siguientes movimientos para saber que en el siguiente, estaría repitiendo posición
#Crea una lista de los obstáculos, para no repetir
#Revisa la lista antes de poner uno  

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
        return "Out",loc, count, map
    if map[loc[0] + dir[0]][loc[1] + dir[1]] == 'X':
        count += 1
        #print(count)
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
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(map)
    for row in map:
        for cell in row:
            if cell == 'X':
                count +=1
    return count, map

def part2(map,path):
    #Declarations
    guard = '^'
    obstacle = '#'
    count = 1
    obstacles = []
    successful = []
    direction = [-1,0]
    bounds = [len(map)-1,len(map[1])-1]
    loc = find_guard(map,guard)
    #loop setup
    obstacle_location = []
    #Me falta un loop para saber si ya acabamos
    loopmap = map.copy()
    while count > 0:
        count = 0
        firstCrash = False
        loop = False
        placed = False
        loopCount = 0
        #RESOLVER EL LABERINTO
        while (loc[0]+direction[0]) <= bounds[0] and (loc[1] + direction[1]) <= bounds[1] and not loop:
            #Si ya chocó, podemos poner obstáculo, siempre y cuando no lo hayamos intentado antes
            if firstCrash == True and [loc[0]+direction[0],loc[1] + direction[1]] not in obstacles and not placed:
                #Escoger la siguiente posición posible
                loopmap[loc[0]+direction[0]][loc[1] + direction[1]] = obstacle
                #Guarda la posición en una lista de intentos
                obstacle_location = [loc[0]+direction[0],loc[1] + direction[1]]
                obstacles.append([loc[0]+direction[0],loc[1] + direction[1]])
                placed = True
            #Si no ha tenido el primer contacto, no podemos poner obstáculo
            if firstCrash == False:
                path[loc[0]][loc[1]] = 'Y'
            loopmap[loc[0]][loc[1]] = 'X'
            if loopmap[loc[0]+direction[0]][loc[1] + direction[1]] == obstacle:
                #Si choca con un obstaculo, puede ser el que pusimos
                if [loc[0]+direction[0],loc[1] + direction[1]] == obstacle_location:
                    #La primera vez que se pone el obstaculo, rebota y no genera un loop
                    print("choque con obstaculo externo")
                    loopCount += 1
                    if loopCount > 1:
                        print("Loop!")
                        loop = True
                        break
                #Si no, hay que cambiar la dirección y actuar normal
                direction = turn_right(direction)
                firstCrash = True   
            else:
                loc = [loc[0]+direction[0],loc[1]+direction[1]]
                if firstCrash == True:
                    breakpoint()
                    path[loc[0]][loc[1]] = 'Y'
                #print(f"{loc[0]},{loc[1]} | {direction[0],direction[1]} | {bounds}")
                loopmap[loc[0]][loc[1]] = 'X'
                if firstCrash == True:
                    path[loc[0]][loc[1]] = 'Y'
        if loop:
            successful.append(obstacle_location)
        for row in path:
            for cell in row:
                if cell == 'X':
                    count +=1
        #print(count)
        print(obstacles)
        with open('output3.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(path)


            
    #change direction
    #check if we can place obstacle
    #place obstacle
    #walk & change direction until out or loop
    return count

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
    result1 = part1(input_data)
    print(f"Part 1: {result1[0]}")
    input_data = parse_input("Input.txt")
    print(f"Part 2: {part2(input_data,result1[1])}")