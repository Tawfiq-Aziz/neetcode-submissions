class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for elem in strs:
            key = ''.join(sorted(elem))
            if key not in dic:
                dic[key] = []
            dic[key].append(elem)
        res = list(dic.values())
        return res
            