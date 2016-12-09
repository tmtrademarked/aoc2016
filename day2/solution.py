if __name__ == '__main__':
    # Read the input and split it out.
    input = open('input.txt', 'r')
    lines = [x.strip() for x in input.readlines()]
    print lines

    # Set up the dial pad and initial state
    n = 3
    pad = [[x+n*y for x in range(1,n+1)] for y in range(n)]
    print pad
    x = 1
    y = 1

    # Convert into instructions
    for line in lines:
        print "Start: " + str(pad[y][x])
        for dir in line:
            if dir == 'U':
                y = max(0, y-1)
            elif dir == 'D':
                y = min(n-1, y+1)
            elif dir == 'L':
                x = max(0, x-1)
            elif dir == 'R':
                x = min(n-1, x+1)
        print "End: " + str(pad[y][x])
