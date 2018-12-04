frequencies = set([0])
current_frequency = 0
found_twice = False
with open('1-1-input.txt') as fp:
    lines = fp.readlines()
    while (not found_twice):
        for line in lines:
            current_frequency += int(line)
            if (current_frequency in frequencies):
                print "first match " + str(current_frequency)
                found_twice = True
                break
            frequencies.add(current_frequency)
