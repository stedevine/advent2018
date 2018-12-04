result = 0
with open('1-1-input.txt') as fp:
  for line in fp:
      result += int(line)

print result
