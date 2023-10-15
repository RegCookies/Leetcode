import collections
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        pc = collections.Counter(filter(lambda x: x.isalpha(), licensePlate.lower()))
        print(pc)
        return min([w for w in words if collections.Counter(w) & pc == pc], key=len)
