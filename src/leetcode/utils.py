from typing import List, Optional
from itertools import zip_longest, tee


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generate_linked_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None

    last = ListNode(val=lst.pop())

    for val in reversed(lst):
        node = ListNode(val, next=last)
        last = node

    return last


def linked_list_iterator(node):
    while node is not None:
        yield node.val
        node = node.next
