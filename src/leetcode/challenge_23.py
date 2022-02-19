# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from utils import ListNode, generate_linked_list, linked_list_iterator
from typing import List, Optional
from collections import defaultdict


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # final_lst = ListNode()
        vals = defaultdict(list)

        min_val = 10 ** 4

        for node in lists:
            if node is None:
                continue

            min_val = min_val if min_val <= node.val else node.val
            vals[node.val].append(node)

        try:
            first = vals[min_val].pop()
        except IndexError:
            return None

        if first.next is not None:
            vals[first.next.val].append(first.next)
            first.next = None

        node = first

        while vals:
            node, vals = self.construct_merge(vals, min_val, prev=node)
            min_val = None

        return first


    def construct_merge(self, vals, min_val=None, prev=None):
        min_val = min_val if min_val is not None else min(vals)

        if prev is None:
            node, *nodes = vals.pop(min_val)
            prev = node
        else:
            nodes = vals.pop(min_val)

        for node in nodes:
            prev.next = node
            prev = node

            if not node.next:
                continue

            next_ = node.next
            node.next = None # reset the value
            vals[next_.val].append(next_)

        return prev, vals


def run_tests():
    s = Solution()
    n = len(tests)

    for i, (case, result) in enumerate(tests, start=1):
        ll = [generate_linked_list(lst) for lst in case]
        output = s.mergeKLists(ll)
        formatted = list(linked_list_iterator(output))
        try:
            assert formatted == result
        except:
            raise RuntimeError(
                f"Bad result for the test case {i}:"
                "\n"
                f" case: {case}"
                "\n"
                f"Expected {result} but got {formatted}"
            )
        else:
            print(f"Passed case {i} of {n}")

    print('All test cases passed')


tests = [
    ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
    ([], []),
    ([[]], []),
    ([[1]], [1])
]

if __name__ == "__main__":
    run_tests()
