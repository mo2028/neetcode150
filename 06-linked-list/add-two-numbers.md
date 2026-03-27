# Add Two Numbers

## Problem
- **Link**: https://leetcode.com/problems/add-two-numbers/
- **Description**: Given two non-empty linked lists representing two non-negative integers stored in reverse order, add the two numbers and return the sum as a linked list in reverse order.

## Difficulty
Medium

## Approach
- Use a dummy node and `curr` pointer to build the result list
- Track `carry` (starts at 0)
- Loop `while l1 or l2 or carry` — handles different length lists AND leftover carry in one condition
- Each iteration:
  1. Safely get values: `l1Val = l1.val if l1 else 0` (same for l2)
  2. `addedNum = l1Val + l2Val + carry`
  3. `carry = addedNum // 10`
  4. Create node with `addedNum % 10` (ones digit only)
  5. Advance `curr`, then safely advance `l1` and `l2`
- Return `dummy.next`

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            addedNum = l1Val + l2Val + carry
            carry = addedNum // 10
            curr.next = ListNode(addedNum % 10)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
```

## Key Pattern
Dummy node + digit-by-digit addition with carry. The `while l1 or l2 or carry` condition elegantly handles unequal list lengths and leftover carry without any special cases after the loop.

## Complexity
- **Time**: O(max(n, m))
- **Space**: O(max(n, m))

## Mistakes / Learnings
- **Conditional carry update**: Used `if addedNum % 10 != 0: carry = addedNum // 10` — this skips resetting carry to 0 when there's no overflow. Always do `carry = addedNum // 10` unconditionally.
- **Storing full sum in node**: Used `ListNode(addedNum)` instead of `ListNode(addedNum % 10)`. Each node holds only the ones digit.
- **Wrong while condition**: Started with `while l1 and l2`, then `while l1 or l2`. The correct condition is `while l1 or l2 or carry` — adding `or carry` handles the case where both lists are exhausted but a carry remains (e.g. 99 + 1 = 100).
- **Unsafe list advancement**: `l1 = l1.next` crashes if `l1` is already `None`. Use `l1 = l1.next if l1 else None`.
- **No need for special carry handling after loop**: Because `or carry` is in the while condition, when carry=1 and both lists are None, the loop runs once more with `l1Val=0, l2Val=0`, naturally creating the carry node.

## Revisit
- **Struggle level**: hints
- **Intervals**: 3d → 7d → 14d
- **Current interval**: 1
- **Date to revisit**: 2026-03-27
- **Revisit history**:
