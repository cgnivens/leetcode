# https://leetcode.com/problems/sum-of-two-integers/

# The cheap answer would be
# sum((a, b))
# but that doesn't seem to be the spirit of the problem
class Solution:
    @staticmethod
    def add(a, b):
        """Use bit shifting to increment a and decrement b until b is 0
        """
        while b:
            c = a & b
            a = a ^ b
            b = c << 1

        return a

    @staticmethod
    def subtract(a, b):
        """If either number is negative, then we should do a subtract.

        Negate the add operation via the ~a
        """
        while b:
            c = (~a) & b
            a = a ^ b
            b = c << 1

        return a



    def getSum(self, a: int, b: int) -> int:
        """Add two numbers without arithmetic operators
        """
        if a < 0 and b < 0:
            return -1 * self.add(-a, -b)
        elif a < 0 or b < 0:
            a, b = sorted((a, b))
            return self.subtract(a, -b)
        else:
            return self.add(a, b)


def run_tests():
    s = Solution()
    n = len(tests)

    for i, (a, b, result) in enumerate(tests, start=1):
        tot = s.getSum(a, b)
        try:
            assert tot == result
        except:
            raise RuntimeError(
                f"Bad result for the test case {i}:"
                "\n"
                f" s1: {a}"
                "\n"
                f" s2: {b}"
                "\n"
                f"Expected {result} but got {tot}"
            )
        else:
            print(f"Passed case {i} of {n}")

    print('All test cases passed')


tests = [
    (2, 3, 5),
    (1, 9, 10),
    (10000000000, 1, 10000000001),
    (9999999, 9999999, 19999998),
    (-1, 1, 0),
    (-14, 16, 2)
]
