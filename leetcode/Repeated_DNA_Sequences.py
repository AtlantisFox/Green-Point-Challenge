class Solution:
    # @param s, a string
    # @return a string[]
    def findRepeatedDnaSequences(self, s):
        a = set()
        b = set()
        for i in range(len(s)-9):
            if s[i:i+10] not in a:
                a.add(s[i:i+10])
            else:
                b.add(s[i:i+10])
        c = list(b)
        return c
            
