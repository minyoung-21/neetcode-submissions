class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                new_node = TrieNode()
                curr.children[c] = new_node
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        l = len(word)
        def recurse(node: TrieNode, j:int) -> bool:
            if j < l:
                if word[j] in node.children:
                    return recurse(node.children[word[j]], j+1)
                elif word[j] == '.':
                    if node.children:
                        for c in node.children:
                            if recurse(node.children[c],j+1):
                                return True
                        # this line is so important
                        # we return false after trying all the chars
                        return False
                    return False
                else:
                    return False
            else:
                return node.end

        curr = self.root
        return recurse(curr, 0)