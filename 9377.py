f = open('9377.txt')
s = f.readline()
di = set('1234567890')
l = set(s) - di
for c in l:
    s = s.replace(c, 'A')
for d in di:
    s = s.replace('A'+d, 'A '+d).replace(d+'A', d+' A')
words = [x if x[0]=='A' or x[0]!='0' and x[-1] not in '13579' else ' ' for x in s.split()]
s = ''.join(words)
while 'A ' in s or ' A' in s:
    s = s.replace('A ', ' ').replace(' A', ' ')
print(max(map(len, s.split())))