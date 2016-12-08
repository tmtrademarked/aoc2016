if __name__ == '__main__':
    # Read the input and split it out.
    input = open('input.txt', 'r')
    directions = [x.strip() for x in input.read().split(',')]
    print directions

    # Initialize our state
    facing = 0;
    x = 0;
    y = 0;
    
    # Convert into instructions
    for dir in directions:
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
            y += inc
        elif facing == 90:
            x += inc
        elif facing == 180:
            y -= inc
        elif facing == 270:
            x -= inc

        print "New coords: " + str(x) + "," + str(y)
        print "Distance: " + str(abs(x) + abs(y))

    
    
