# https://leetcode.com/problems/permutation-in-string/


from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force way would be to check all permutations
        # of s1 and see if each is in s2. Let's start there
        for permute in permutations(s1):
            if ''.join(permute) in s2:
                return True

        return False


def run_tests():
    s = Solution()
    n = len(tests)

    for i, (s1, s2, result) in enumerate(tests, start=1):
        try:
            assert s.checkInclusion(s1, s2) is result
        except:
            raise RuntimeError(
                f"Bad result for the test case {i}:"
                "\n"
                f" s1: {s1}"
                "\n"
                f" s2: {s2}"
                "\n"
                f"Expected {result} but got {not result}"
            )
        else:
            print(f"Passed case {i} of {n}")

    print('All test cases passed')


tests = [
    ("ab", "eidbaooo", True),
    ("dinitrophenylhydrazine", "acetylphenylhydrazine", False)
]
