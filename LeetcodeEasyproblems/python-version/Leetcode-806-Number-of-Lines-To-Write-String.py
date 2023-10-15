class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        units, rows = 0, 0
        for s in S:
            unit = widths[ord(s) - ord('a')]
            if 100 - units >= unit:
                units += unit
            else:
                rows += 1
                units = 0
                units += unit
        return [rows + 1, units] if units != 0 else [rows, units]
