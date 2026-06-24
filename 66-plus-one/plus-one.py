class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        for i in digits:
            a += str(i)
        a = int(a) + 1
        o = []
        o = [int(j) for j in str(a)]
        return o
        