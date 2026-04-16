class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictionary = {} 
        dictionary1 = {}
        for char1, char2 in zip(s, t):
            dictionary[char1] = dictionary.get(char1, 0) + 1
            dictionary1[char2] = dictionary1.get(char2, 0) + 1

        for k, v in dictionary.items():
            if k not in dictionary1 or dictionary1[k] != v:
                return False
        

        return True