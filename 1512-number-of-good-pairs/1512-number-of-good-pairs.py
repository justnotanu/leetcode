class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = {}
        for n in nums:
            if n in count:
                res += count[n]
                count[n] += 1
            else:
                count[n] = 1
        return res
        