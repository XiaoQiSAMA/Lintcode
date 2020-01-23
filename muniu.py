nums = []
for i in range(1,56):
    if i <= 4:
        nums.append(i)
    else:
        num = nums[i-2]+nums[i-4]
        nums.append(num)
years = []
while True:
    n = eval(input())
    if n == 0 or n > 55:
        break
    years.append(n)

for x in years:
    print(nums[x-1])
