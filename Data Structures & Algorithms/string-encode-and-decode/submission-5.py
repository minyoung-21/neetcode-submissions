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
        # print(len(s))
        while n < len(s):
            # print(n)
            
            if s[n] == "#":
                # print(numb)
                res.append(s[n+1:n+1+int(numb)]);
                n = n+1+int(numb)
                # print(n)
                numb = ""; #reset
            if n < len(s):
                numb += s[n];
            else:
                return res;
            print(numb)
            n += 1;
                
        return res;