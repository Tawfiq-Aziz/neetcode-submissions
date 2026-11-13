class Solution:
    def hasDuplicate(self, nums):
        flag = False
        count = 0
        ar = []
        for i in nums:
            if i not in ar:
                ar.append(i)
        print(ar)
        if len(ar)==len(nums):
            flag = False
        else:
            flag = True
        return flag
    

   

        