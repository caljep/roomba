def clean_room(file) :
    #deserialize input into dimensions, position, dirt, moves etc
    lines = open(file,'r').readlines()
    dimensions = lines[0][0:-1].split(' ')
    width = int(dimensions[0])
    height = int(dimensions[1])
    position = lines[1][0:-1].split(' ')
    position = [int(position[0]), int(position[1])]
    dirty_bits = lines[2:-1]
    moves = lines[-1]

    #setup the board, could do without this step but it should
    #save compute time in the long run
    room = setup_room(width, height, dirty_bits)

    #move the roomba and clean that dirty floor!
    cleaned = 0
    for move in moves:
        position = move_roomba(position, width, height, move)
        
        #check if it was cleaned!
        if room[position[0]][position[1]] == 1:
            cleaned += 1
        
        room[position[0]][position[1]] = 0
    
    #print the results
    print(position[0],position[1])
    print(cleaned)


def move_roomba(position, width, height, move):
    #simply translate the cardinal directions into vector and make
    #roomba does not go out of bounds
    if move == 'N' and position[1] < height:
        position[1] += 1
    elif move == 'S' and position[1] > 0:
        position[1] -= 1
    elif move == 'E' and position[0] < width:
        position[0] += 1
    elif move == 'W' and position[0] > 0:
        position[0] -= 1

    return position

def setup_room(width, height, dirty_bits):
    #initialize the coordinates
    coordinates = {}
    for x in range(width):
        coordinates[x] = {}
        for y in range(height):
            coordinates[x][y] = 0

    #making the dirty coordinates 1, eveything else 0
    for dirt in dirty_bits:
        dirt_coords = dirt[0:-1].split(' ')
        coordinates[int(dirt_coords[0])][int(dirt_coords[1])] = 1
    return coordinates


#Using sys so you can specify the filename in the command line
#when you are executing this code. For example 'python roomba_simulator.py input.txt'
#If the file will always be 'input.txt' then uncomment the next line
#clean_room('input.txt')
import sys
clean_room(sys.argv[-1])