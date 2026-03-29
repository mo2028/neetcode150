# Reorder List

## Problem
- **Link**: https://leetcode.com/problems/reorder-list/
- **Description**: Given the head of a singly linked list, reorder it in-place so that nodes alternate from the front and back: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

## Difficulty
Medium

## Approach
Three steps:

1. **Find the middle** using slow/fast pointers (`while fast and fast.next`)
2. **Cut and reverse the second half**: save `second = slow.next`, set `slow.next = None` to cut, then reverse from `second`
3. **Merge alternating**: take one node from first half, one from reversed second half, repeat

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        slow.next = None

        curr = head
        while curr and prev:
            nextCurrNode = curr.next
            nextPrevNode = prev.next
            curr.next = prev
            prev.next = nextCurrNode
            curr = nextCurrNode
            prev = nextPrevNode
```

## Key Pattern
Slow/fast to find middle → reverse second half → merge alternating. Classic three-step linked list restructure.

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Mistakes / Learnings
- **Start reversal from `slow.next`, not `slow`**: `slow` is the last node of the first half — it stays there. The second half begins at `slow.next`.
- **Must cut with `slow.next = None`**: After finding the middle, `slow` still points to the next node. Without cutting, the first half incorrectly connects into the second half. Cut severs the two halves cleanly.
- **Cut can happen after reversal here**: Since reversal starts from `slow.next`, the `slow` node is never touched during reversal — so `slow.next = None` works whether placed before or after the reversal loop.
- **Function modifies in-place**: Return type is `None` — do not `return head`.
- **Merge while condition**: `while curr and prev` — stops when the second half (shorter or equal) runs out.

## Revisit
- **Struggle level**: hints
- **Intervals**: 3d → 7d → 14d
- **Current interval**: 1
- **Date to revisit**: 2026-03-31
- **Revisit history**:
