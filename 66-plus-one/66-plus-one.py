class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int("".join(map(str, digits)))
        return list(map(int, str(res+1)))