import operator

def comparator(a, b):
    if a[1] > b[1]:
        return -1;
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return 1

if __name__ == '__main__':
    # Read the input and split it out.
    input = open('input.txt', 'r')
    rooms = [x.strip() for x in input.readlines()]
    infos = [[x, x[: -11], x[-10:-7], x[-6:-1]] for x in rooms]

    # info[0] = original
    # info[1] = encrypted
    # info[2] = sector
    # info[3] = checksum

    sector_count = 0
    for info in infos:
        print info
        # Establish the count of each letter.
        counts = {}
        for x in info[1]:
            if x == '-':
                continue
            counts[x] = info[1].count(x)
        print counts

        # Sort first by the count. We then need to sort
        # alphabetically to break ties. Use our custom
        # comparator to achieve this.
        sorted_counts = sorted(counts.items(), cmp=comparator)
        print sorted_counts

        # Now look into the checksum and check to see that
        # the characters appear in order. Assume the room
        # is legit until proven otherwise.
        valid = True
        for x in info[3]:
            tuple = sorted_counts.pop(0)
            if tuple[0] != x:
                print "Wanted " + x + " but found " + tuple[0]
                valid = False
                break;

        # Now we know if the room is valid or not.
        print "Valid: " + str(valid)
        if valid:
            sector_count += int(info[2])
        print "Sector sum: " + str(sector_count)

