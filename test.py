# O(n) = m*n 超时
# n,m = input().split(' ')
# stu = [0 for i in range(int(n))]
# for i in range(int(m)):
#     l,r,c = input().split(' ')
#     stu[int(l)-1:int(r)] = [j+int(c) for j in stu[int(l)-1:int(r)]]
# for i in stu: print(i,end=' ')

#构建线段树
class duanTree:
    def __init__(self,stu_num):
        self.stu_num = stu_num
        