import re

f = open('4442.txt')
s = f.readline()
timecodes = re.findall(r"(([01][0-9])|(2[0123]))[0-5][0-9]", s)
max_timecodes = 0
count = 0
h = []
for i in timecodes:
    if len(i[0] + i[1]) == 4:
        h.append(i[0] + i[1])
    elif len(i[1] + i[2]) == 4:
        h.append(i[1] + i[2])

print(h)
for i in range(3, len(s) - 3, 4):
    if s[i - 3] + s[i - 2] + s[i - 1] + s[i] in h:
        count += 1
    else:
        max_timecodes = max(max_timecodes, count)
        count = 0
max_timecodes = max(max_timecodes, count)
print(max_timecodes)
#5261 5643 6185 6010