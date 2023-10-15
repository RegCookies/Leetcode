import collections
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        w = collections.Counter(filter(lambda x: x.isalpha(), licensePlate.lower()))
        return min([word for word in words if collections.Counter(word) & w == w], key = len)
