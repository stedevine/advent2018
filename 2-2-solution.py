import itertools

def get_common_letters(lines):
    # The input has exactly one pair of lines
    # with exactly 1 letter difference
    # All the lines are the same length
    result = ""
    for a,b in itertools.combinations(lines,2):
        diff = 0
        # Find the pair for which the difference is one
        for i in range(len(a)):
            if (a[i] != b[i]):
                diff += 1
            if (diff > 1):
                break
        if (diff == 1):
            # Collect the letters the two lines have in common
            for i in range(len(a)):
                if (a[i] == b[i]):
                    result += a[i]
            return result

# Test input
print get_common_letters([
"abcde",
"fghij",
"klmno",
"pqrst",
"fguij",
"axcye",
"wvxyz"])

# Problem input
with open('2-1-input.txt') as fp:
    lines = fp.readlines()
    print get_common_letters(lines)
