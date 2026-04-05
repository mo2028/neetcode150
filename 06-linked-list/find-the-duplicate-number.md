# Find the Duplicate Number

## Problem
- **Link**: https://leetcode.com/problems/find-the-duplicate-number/
- **Description**: Given an array of n+1 integers where each integer is in the range [1, n], find the duplicate number. Must not modify the array and use O(1) extra space.

## Difficulty
Medium

## Approach
Floyd's Cycle Detection (tortoise and hare) — treat array values as pointers to the next index.

**Phase 1**: Find the meeting point inside the cycle.
- slow starts at `nums[0]` (1 step from index 0)
- fast starts at `nums[nums[0]]` (2 steps from index 0)
- Move slow 1 step, fast 2 steps until they meet

**Phase 2**: Find the cycle entry point (= duplicate).
- Reset one pointer (`pointer`) to index `0` (the true start)
- Keep `slow` at the meeting point
- Move both 1 step at a time until they meet
- Where they meet = the duplicate

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        pointer = 0
        while pointer != slow:
            pointer = nums[pointer]
            slow = nums[slow]

        return slow
```

## Key Pattern
- **Floyd's Cycle Detection** applied to an array treated as a linked list
- Each index has exactly one value = one outgoing edge, just like a linked list node's `next` pointer
- Array values as next pointers: `nums[i]` = next index to visit
- Duplicate creates a cycle because two indices point to the same next node
- Cycle entry point = duplicate number

## Complexity
- **Time**: O(n)
- **Space**: O(1)

## Mistakes / Learnings

**1. Confused why a duplicate creates a cycle**
Initially thought a cycle needed bidirectional movement ("in and out"). Clarified: in a directed traversal, a cycle just means you revisit a node. The duplicate value `d` causes two different indices to both point to index `d`, creating two incoming paths into `d`. Since each index has exactly one value (one outgoing edge), `d`'s only outgoing path eventually loops back to `d` — forming a cycle.

**2. Phase 1 initialization — used `slow = 0, fast = nums[0]`**
Tried starting slow at index 0 and fast at `nums[0]`, thinking they just needed to be offset by one. But this is asymmetric — slow has taken 0 steps, fast has taken 1. Floyd's requires fast to be exactly 2x the steps of slow from the same conceptual start. The fix: `slow = nums[0]` (1 step in), `fast = nums[nums[0]]` (2 steps in). Both have started from index 0 and taken the correct ratio of steps.

**3. Phase 2 reset — used `pointer = nums[0]` instead of `pointer = 0`**
Reset the pointer to `nums[0]` thinking that was the start. But `nums[0]` is already 1 step into the traversal. The traversal starts at index `0`, so phase 2 must reset to `0`. Using `nums[0]` causes the two pointers to be offset and they loop past each other indefinitely (infinite loop).

**4. Returned `nums[slow]` instead of `slow`**
After phase 2, `slow` (and `pointer`) are sitting at the duplicate index — that index value IS the duplicate. `nums[slow]` would be the next step beyond it. Return `slow` directly.

**5. Used `while i < len(nums)` for phase 1**
Early attempt looped based on array length rather than the cycle detection condition `slow != fast`. Phase 1 should loop until the two pointers meet, not a fixed number of times.

## Revisit
- **Struggle level**: struggled
- **Intervals**: 1d → 3d → 7d
- **Current interval**: 1
- **Date to revisit**: 2026-03-30
- **Revisit history**:
