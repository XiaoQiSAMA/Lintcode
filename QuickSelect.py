import random
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # rea = heapq.nlargest(n, nums)
        middle = random.randint(0, len(nums)-1)
        A_big = []
        A_small = []
        num = 0

        for i in range(len(nums)):
            if nums[middle]<nums[i]:
                A_big.append(nums[i])
            elif nums[middle]==nums[i]:
                num += 1
            elif nums[middle]>nums[i]:
                A_small.append(nums[i])
        if len(A_big)==n-1:
            return nums[middle]
        elif len(A_big)>n-1:
            return self.kthLargestElement(n, A_big)
        elif len(A_big)<n-1:
            return self.kthLargestElement(n-num-len(A_big), A_small)