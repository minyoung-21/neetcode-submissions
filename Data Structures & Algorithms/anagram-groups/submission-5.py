class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        pos = 0
        for word in strs:
            s = "".join(sorted(word))
            if s not in d:
                d[s] = pos
                res.append([word])
                pos += 1
            else:
                
                res[d[s]].append(word)
        
        return res