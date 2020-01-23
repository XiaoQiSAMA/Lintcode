def loop(n-1):
    if n <= 4:
        return n
    a = n - 4
    for i in range(1,a+1):
        # print("loop's num is ",i)
        n += loop(i)
    return n

data = []    
while True:
    n = eval(input())
    if n == 0:
        break
    data.append(n)


for i in data:
    print(loop(i))