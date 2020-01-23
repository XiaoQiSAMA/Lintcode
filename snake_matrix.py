num = eval(input())
string = ''
x = 1
for i in range(1,num+1): 
    print(x,end=' ')
    temp = x
    for j in range(i+1,num+1):
        temp += j
        string += str(temp) + ' '
    print(string.rstrip(' '))
    string = ''
    x += i

