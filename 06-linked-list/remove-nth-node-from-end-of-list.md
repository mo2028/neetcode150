# Remove Nth Node From End of List

## Problem
- **Link**: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- **Description**: Given the head of a linked list, remove the nth node from the end and return the head.

## Difficulty
Medium

## Approach
Two-pass approach:
1. First pass: count the total length of the list
2. Compute `nodeToRemove = length - n` (0-indexed position from dummy)
3. Use a dummy node prepended before head, start `curr` at dummy
4. Walk until `counter == nodeToRemove`, then do `curr.next = curr.next.next` to skip the target node
5. Return `dummy.next` (handles head removal cleanly)

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        nodeToRemove = length - n
        counter = 0
        while curr:
            if counter == nodeToRemove:
                curr.next = curr.next.next
                break
            counter += 1
            curr = curr.next
        return dummy.next
```

## Key Pattern
- **Dummy node** to avoid edge cases when removing the head
- Two-pass: count length, then walk to `length - n`

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Mistakes / Learnings

**1. Tried to manually handle edge cases instead of using a dummy node**
First attempt had conditions like `if length >= 3` and `elif length == 1: head = None`. This came from trying to handle "remove the head" as a special case. Realized this was a sign of missing the dummy node pattern — the dummy node makes all removals uniform, including head removal.

**2. Confused `dummy = curr` with `dummy.next = head`**
When asked how to set up a dummy node, wrote `dummy = curr` — thinking of dummy as just another pointer alias. The dummy node needs to be a *new* node that points to head: `dummy.next = head`. Then later wrote `dummy = head` which throws away the dummy node entirely and just makes dummy an alias for head. The key insight: dummy is a sentinel node *before* the list, not a pointer *into* the list.

**3. Was moving dummy inside the loop**
In an early version, wrote `dummy = curr` inside the traversal loop, thinking dummy needed to follow curr. This destroys the whole point of the dummy node — it's a fixed anchor. Only `curr` should move. The removal always happens via `curr.next = curr.next.next` where `curr` is at the right position.

**4. Forgot to reset `curr` before the second loop**
After the first loop (counting length), `curr` ends up as `None`. Started the second loop with `while curr:` without reassigning `curr = dummy`, so the second loop never ran at all. Always reset traversal pointers before a new loop.

**5. Returned `head` instead of `dummy.next`**
Returned `head` at the end, which seems right — until you remove the head node. In that case `head` still points to the old removed node, and the new head is `dummy.next`. Always return `dummy.next` when using this pattern.

**6. Counter offset confusion**
Initially used `counter == nodeToRemove - 1` (leftover from the version without dummy). Once `curr` starts at `dummy` (index 0), `counter == nodeToRemove` lands you exactly at the node *before* the one to remove, which is what you want for `curr.next = curr.next.next`.

## Revisit
- **Struggle level**: hints
- **Intervals**: 3d → 7d → 14d
- **Current interval**: 1
- **Date to revisit**: 2026-04-01
- **Revisit history**:
