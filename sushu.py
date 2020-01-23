n = eval(input())
nums = [i for i in range(2,n+1)]
# print(nums)
# nums1 = deepcopy(nums)
for i in range(n // 2):
    # print('i = ',i)
    for j in range(i+1,len(nums)):
        # print('j = ',j)
        try:
            if (nums[j] % nums[i] == 0):
                nums[j] = 0
                
        except ZeroDivisionError:
            continue
for x in nums:
    if x != 0:
        print(x)