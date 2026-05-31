class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = [];
        hm = {};
        pos = 0;
        for word in strs:
            sorted_string = ''.join(sorted(word));
            if sorted_string not in hm.keys():
                hm[sorted_string] = pos;
                pos += 1;
                res.append([word]);
            else:
                res[hm[sorted_string]].append(word);
        return res;