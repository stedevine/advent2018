def add(key, map):
    if key in map:
        map[key] = 1 + map[key]
    else:
        map[key] = 1

def get_checksum(boxes):
    m = 0
    n = 0
    for line in boxes:
        map = {}
        for letter in line:
            add(letter,map)
        if (2 in map.itervalues()):
            m += 1
        if (3 in map.itervalues()):
            n += 1

    print m
    print n
    print n * m

get_checksum([
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab"])

with open('2-1-input.txt') as fp:
    lines = fp.readlines()
    get_checksum(lines)
