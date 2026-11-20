class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [item for item, frequency in count.most_common(k)]