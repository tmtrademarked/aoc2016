import md5

if __name__ == '__main__':
    input = open('input.txt', 'r').read().strip()
    print input

    count = 0
    password = ''
    while len(password) < 8:
        m = md5.new()
        attempt = input + str(count)
        m.update(attempt)
        guess = m.hexdigest()
        if guess[0:5] == '00000':
            password += guess[5]
            print "Current password: " + password
        count += 1

    # Now print the password
    print "Count: " + str(count)
    print "FINAL PASSWORD: " + password
        

