# Part 2 - track which squares you've visited.
import operator
import sys

def vist(x, y, dir, visited):
    coords = [x, y]
    print str(coords) + " " + dir
    if coords in visited:
        print "Revisiting " + str(coords)
        print "Distance: " + str(abs(coords[0]) + abs(coords[1]))
        return True
    else:
        visited.append(coords)
        return False

if __name__ == '__main__':
    # Read the input and split it out.
    input = open('input.txt', 'r')
    directions = [x.strip() for x in input.read().split(',')]
    print directions

    # Initialize our state
    facing = 0;
    x = 0;
    y = 0;
    visited = []
    
    # Convert into instructions
    for dir in directions:
        old_x = x
        old_y = y
        if dir[0] is 'R':
            print "Right: " + dir[1:]
            facing = (facing + 90) % 360
        else:
            print "Left: " + dir[1:]
            facing = (facing - 90) % 360
        print "Facing: " + str(facing)

        print "Old coords: " + str(x) + "," + str(y)

        inc = int(dir[1:])
        if facing == 0:
            for d in range(1,inc+1):
                if (vist(x, y+d, dir, visited)):
                    sys.exit();
            y += inc
        elif facing == 90:
            for d in range(1,inc+1):
                if (vist(x+d, y, dir, visited)):
                    sys.exit();
            x += inc
        elif facing == 180:
            for d in range(1,inc+1):
                if (vist(x, y-d, dir, visited)):
                    sys.exit();
            y -= inc
        elif facing == 270:
            for d in range(1,inc+1):
                if (vist(x-d, y, dir, visited)):
                    sys.exit();
            x -= inc

    print "Hmm, no dupes"
    for v in visited:
        print v
    print "Damn!"
    
    
    
