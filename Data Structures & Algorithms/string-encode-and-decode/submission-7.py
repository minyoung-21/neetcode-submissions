class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#"
            res += word
        
        return res

    def decode(self, s: str) -> List[str]:
        
        res = []
        count = ""
        i = 0
        while i < len(s):
            count += s[i]
            print(count)
            word = ""
            if s[i] == "#":
                
                res.append(word.join(s[i+1:i+1+int(count[:len(count)-1])]))
                
                i = i+int(count[:len(count)-1])
                count = ""
            i += 1
        return res