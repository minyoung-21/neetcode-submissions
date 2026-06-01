class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word;
        return res

    def decode(self, s: str) -> List[str]:
        
        numb = "";
        start_pos = 0;
        res = [];
        faced_del = False;
        n = 0;
        while n < len(s):
            if s[n] == "#":
                res.append(s[n+1:n+1+int(numb)]);
                n = n+1+int(numb)
                numb = ""; #reset
            if n < len(s):
                numb += s[n];
            else:
                return res;
            n += 1;
                
        return res;