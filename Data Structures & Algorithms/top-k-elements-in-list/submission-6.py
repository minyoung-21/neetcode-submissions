class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        res = []

        for n in nums:
            if n in hm:
                hm[n] += 1
            else:
                hm[n] = 0

        for j, v in sorted(hm.items(), key = lambda item : item[1]):
            res.append(j)

        return res[-k:]