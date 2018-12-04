def add(key, map):
    if key in map:
        map[key] = 1 + map[key]
    else:
        map[key] = 1


with open('2-1-input.txt') as fp:
    #lines = fp.readlines()
    lines = [
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab"]
    for line in lines:
        map = {}
        print line
        for letter in line:
            #print letter
            add(letter,map)
        for key in map:
            print map[key]
