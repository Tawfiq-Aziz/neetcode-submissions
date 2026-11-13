class Solution:
    def isAnagram(self, s, t):
        arr = {}
        arr1 = {}
        flag = False
        for key in s:
            if key not in arr:
                arr[key] = 1
            else:
                arr[key] += 1

        for key in t:
            if key not in arr1:
                arr1[key] = 1
            else:
                arr1[key] += 1
                
        if arr == arr1:
            flag = True
        return flag