class Solution:
    def twoSum(self, nums, target):
        lst = []
        for i in range(len(nums)):
            for j in range(len(nums)-1,0,-1):
                if nums[i]+nums[j] ==target and i!=j and i not in lst and j not in lst:
                    lst.append(i)
                    lst.append(j)
        return lst