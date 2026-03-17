class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        sum = 0
        product = 1
        for i in s:
            d =int(i)
            sum += d
            product*=d
        return product - sum
        