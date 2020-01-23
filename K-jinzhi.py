# def loop1(N,K):
#     num = ''
#     while N != 0:
#         for k in range(K):
#             num += str(loop1(N-1,K))
#             print(num)
#             return num
           
# L = []
# loop1(3,10)
# print(L)


# def loop(K):
#     data = []
#     for j in range(1,K):
#         for i in range(K):
#             num = str(j)+str(i)
#             if not check(num):
#                 data.append(num)
#     return data

# def check(num):
#     zeros = []
#     num = list(num)
#     while '0' in num:
#         zeros.append(num.index('0'))
#         num[num.index('0')]=None
#     temp = -1
#     for i in zeros:
#         if i == temp + 1:
#             return False
#         temp = i
#     return num

# N,K = int(input()),int(input())

# # if N > 2:
# # test = check('100')
# # print(test)
# data = loop(K)

# # print(len(data)*len(data[0]))
n=int(input())
k=int(input())
re=0
def loop(c,m):
    global n,k,re
    if c==1:
        if m==0:
            re+=k-1
        else:
            re+=k
    if c==n:
        for i in range(1,k):
            loop(c-1,i)
    else:
        if m==0:
            for i in range(1,k):
                loop(c-1,i)
        else:
            for i in range(0,k):
                loop(c-1,i)
loop(n,1)
print(re)