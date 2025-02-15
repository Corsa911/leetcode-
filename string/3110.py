class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        You are given a string s. The score of a string
        is defined as the sum of the absolute difference 
        between the ASCII values of adjacent characters.
        Return the score of s.
        """
        x = 0
        for i in range(0,len(s)-1):
            x += abs(ord(s[i]) - ord(s[i+1]))
        return x