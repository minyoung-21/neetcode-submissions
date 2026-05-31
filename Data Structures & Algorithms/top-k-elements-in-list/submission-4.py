class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [];
        m = {};
        for i in nums:
            if i not in m.keys():
                m[i] = 1;
            else:
                m[i] += 1;
        
        m = {k: v for k, v in sorted(m.items(), key=lambda item: item[1], reverse = True)}
        
        for keys in m.keys():
            res.append(keys);

        return res[0:k];