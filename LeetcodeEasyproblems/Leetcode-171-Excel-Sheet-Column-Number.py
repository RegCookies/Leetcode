class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for char in s: num = ord(char)-64 + num*26
        return num