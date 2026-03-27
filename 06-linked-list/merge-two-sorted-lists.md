# Merge Two Sorted Lists

## Problem
- **Link**: https://leetcode.com/problems/merge-two-sorted-lists/
- **Description**: Given the heads of two sorted linked lists, merge them into one sorted linked list and return the head.

## Difficulty
Easy

## Approach
- Use a dummy node as a stable starting point to avoid special-casing the head
- Use `curr` to track the tail of the merged list
- While both lists have nodes, compare `list1.val` and `list2.val`, attach the smaller node to `curr`, advance `curr` and the chosen list pointer
- After the loop, attach whichever list still has remaining nodes (already sorted, no need to iterate)
- Return `dummy.next`

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next

        curr.next = list1 or list2
        return dummy.next
```

## Key Pattern
Dummy node + two-pointer merge. Reuse existing nodes by rewiring `.next` pointers — no new node creation needed. After the loop, attach the leftover list directly since it's already sorted.

## Complexity
- **Time**: O(n + m)
- **Space**: O(1)

## Mistakes / Learnings
- **Created new nodes**: Used `ListNode(list1.val)` instead of attaching `list1` directly. The existing nodes are reused — just rewire their `.next` pointers.
- **Wrong while condition**: Used `list1.next and list2.next` instead of `list1 and list2`. Using `.next` skips the last node of each list since its `.next` is `None`.
- **Leftover handling inside loop**: Placed the `if list1 / elif list2` block inside the while loop. It must be outside — you only attach the remainder once, after the loop ends.
- **Order of curr and list advancement**: Must do `curr.next = list1` → `curr = list1` → `list1 = list1.next` in that exact order. Move `curr` to the node you just attached, then advance the list pointer for the next comparison. If you advance `list1` first, `curr` ends up pointing to the wrong node.
  - *In my own words*: move the curr before list1 or list2 so that you can point curr to either list1 node or list2 node. Then you move list1 or list2 based on what curr pointed to so that you can compare between the updated list1 and list2.
- **Simplification**: `curr.next = list1 or list2` works cleanly since one will be `None` and the other won't.

## Revisit
- **Struggle level**: hints
- **Intervals**: 3d → 7d → 14d
- **Current interval**: 1
- **Date to revisit**: 2026-03-27
- **Revisit history**:
