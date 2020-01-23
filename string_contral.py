s = list('abcdefg')
# print(str(s))
offset = 3
# s = s[-offset:]+s[:-offset]
# new_s = ''.join(s).split(s[-offset])
# print(new_s)
# s = s[-offset]+new_s[1]+new_s[0]
new_s = ''
print(s)
for j in range(offset,0,-1):
    new_s += s[-j]
# print(new_s)
for i in range(offset+1):
    new_s += s[i]
s = new_s
print(new_s)
# print(s)