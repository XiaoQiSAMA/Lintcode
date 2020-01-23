# def choose(up, down):
#     temp = 1
#     reault = 1
#     for i in range(1,up+1):
#         temp *= i
#         reault *= down
#         down -= 1
#     return int(reault/temp)
# k,w = input().split()
# k,w = int(k),int(w)

# if w % k:
#     high_bit = w % k
# else: high_bit = k    
# print('high_bit:',high_bit)
# bit1 = int((w - high_bit)/k+1) #数字位数
# print('bit1:',bit1)
# num1 = 0
# for num in range(2**k-1):
#     num1 += num
# print('num1:',num1)
# bit_max = 2**k
# num2 = choose(bit1,bit_max-1)
# print('num2:',num2)
# last_num = 2**k - 2**high_bit
# print('last_num:',last_num)
# temp = 1
# if high_bit != 1:    
#     temp = choose(bit1,last_num)
# else: temp = choose(bit1-1,last_num)
# print('temp:',temp)
# reault = num2 - temp + num1
# print(reault,end='')

