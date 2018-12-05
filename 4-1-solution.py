# For the input find the ID of the guard with the largest number of minutes of sleep
# and the minute at which they are asleep the most.

# There is  only one guard every day, shifts do not overlap
# Only care about sleep times in the midnight hour
# For each new gaurd create an array of 60 zeros
# For each sleeping minute increase the value of the array by 1

log = [
"[1518-11-01 00:00] Guard #10 begins shift"
"[1518-11-01 00:05] falls asleep"
"[1518-11-01 00:25] wakes up"
"[1518-11-01 00:30] falls asleep"
"[1518-11-01 00:55] wakes up"
"[1518-11-01 23:58] Guard #99 begins shift"
"[1518-11-02 00:40] falls asleep"
"[1518-11-02 00:50] wakes up"
"[1518-11-03 00:05] Guard #10 begins shift"
"[1518-11-03 00:24] falls asleep"
"[1518-11-03 00:29] wakes up"
"[1518-11-04 00:02] Guard #99 begins shift"
"[1518-11-04 00:36] falls asleep"
"[1518-11-04 00:46] wakes up"
"[1518-11-05 00:03] Guard #99 begins shift"
"[1518-11-05 00:45] falls asleep"
"[1518-11-05 00:55] wakes up"
]

with open('4-1-input.txt') as fp:
    # The file input is unsorted
    lines = sorted(fp.readlines())
    #print lines
    #apply_to_board(lines, get_board(lines))
