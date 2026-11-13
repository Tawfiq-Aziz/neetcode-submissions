class Solution:
    def hasDuplicate(self, nums):
        flag = False
        arr = []
        for i in nums:
            if i not in arr:
                arr.append(i)
            else:
                flag = True
        return flag