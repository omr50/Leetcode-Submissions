class WordDictionary:

    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        curr = self.dictionary
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['*'] = {}

    def search(self, word: str) -> bool:
        def search2(word, curr):
            if not word:  # base case
                if '*' in curr:
                    return True
                return False
            elif word[0] == '.':
                if curr:
                    for i in curr:
                        if search2(word[1:], curr[i]):
                            return True
            else:
                if word[0] not in curr:
                    return False
                return search2(word[1:], curr[word[0]])
        return search2(word, self.dictionary)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)