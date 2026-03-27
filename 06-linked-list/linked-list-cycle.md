# Linked List Cycle

## Problem
- **Link**: https://leetcode.com/problems/linked-list-cycle/
- **Description**: Given the head of a linked list, return True if there is a cycle, False otherwise.

## Difficulty
Easy

## Approach
Floyd's Cycle Detection (tortoise and hare):
- `slow` moves 1 step at a time, `fast` moves 2 steps at a time
- If there's a cycle, fast will eventually lap slow and they'll meet
- If there's no cycle, fast will hit `None` and the loop exits

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None

        while fast and slow:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return False
```

## Key Pattern
Two pointers (slow/fast). If a cycle exists, fast laps slow and they meet. If no cycle, fast reaches `None` first.

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Mistakes / Learnings
- **`fast.next.next` can crash**: If `fast.next` is `None`, then `fast.next.next` throws `AttributeError: 'NoneType' object has no attribute 'next'`. Guard with `fast.next.next if fast.next else None`.
- **Two layers of safety**:
  1. `while fast and slow` — if `fast` is `None`, the loop exits before you ever touch `fast.next`
  2. `if fast.next else None` — inside the loop, guards against `fast.next` being `None` before doing `fast.next.next`
- **`fast.next` vs `fast.next.next`**: `fast.next` just reads the pointer value — safe even if it returns `None`. `fast.next.next` goes one level deeper — crashes if `fast.next` is `None`. Each extra `.something` requires the thing before it to not be `None`.
- **You cannot call `.next` on `None`**: `None` is not a `ListNode` — it has no attributes. This is the root cause of most linked list crashes.

## Revisit
- **Struggle level**: hints
- **Intervals**: 3d → 7d → 14d
- **Current interval**: 1
- **Date to revisit**: 2026-03-29
- **Revisit history**:
