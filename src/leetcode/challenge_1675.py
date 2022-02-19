# https://leetcode.com/problems/minimize-deviation-in-array/
from typing import List

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        return 256


def run_tests():
    s = Solution()
    n = len(tests)

    for i, (case, result) in enumerate(tests, start=1):
        solution = s.minimumDeviation(case)
        try:
            assert solution == result
        except:
            raise RuntimeError(
                f"Bad result for the test case {i}:"
                "\n"
                f" case: {case}"
                "\n"
                f"Expected {result} but got {solution}"
            )
        else:
            print(f"Passed case {i} of {n}")

    print('All test cases passed')


tests = [
    ([1,2,3,4], 1),
    ([4,1,5,20,3], 3),
    ([2,10,8], 3)
]

if __name__ == "__main__":
    run_tests()
