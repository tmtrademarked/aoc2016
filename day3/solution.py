if __name__ == '__main__':
    # Read the input and split it out.
    input = open('input.txt', 'r')
    lines = [x.strip() for x in input.readlines()]
    tris = [[int(y) for y in x.split()] for x in lines]

    # Now check to see if a tri is valid.
    count = 0
    for tri in tris:
        print tri
        combo1 = (tri[0] + tri[1]) > tri[2]
        print combo1
        combo2 = (tri[0] + tri[2]) > tri[1]
        print combo2
        combo3 = (tri[1] + tri[2]) > tri[0]
        print combo3
        if (combo1 and combo2 and combo3):
            count += 1

    print "Valid triangles: " + str(count)
