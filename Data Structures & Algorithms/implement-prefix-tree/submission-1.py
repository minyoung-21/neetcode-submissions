class PrefixTree:
    
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                new_node = PrefixTree()
                curr.children[c] = new_node
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        i = 0
        curr = self
        while i < len(word):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
                i+=1
            else:
                return False
        
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        i = 0
        while i < len(prefix):
            if prefix[i] in curr.children:
                curr = curr.children[prefix[i]]
                i += 1
            else:
                return False
                
        return True
        
        