# Copy List with Random Pointer

## Problem
- **Link**: https://leetcode.com/problems/copy-list-with-random-pointer/
- **Description**: Deep copy a linked list where each node has a `next` and a `random` pointer.

## Difficulty
Medium

## Approach
- Two-pass with a hashmap (old node → new node).
- **Pass 1**: Create all new nodes (val only), store mapping in hashmap.
- **Pass 2**: Wire up `next` and `random` on each new node using the map.
- Seed the map with `{None: None}` so lookups for `None` pointers just work.

## Key Pattern
Hashmap for old→new node mapping (clone graph / deep copy pattern)

## Complexity
- **Time**: O(n)
- **Space**: O(n)

## Mistakes / Learnings
- **`new Node()` is not Python** — Python doesn't use `new`, just `Node(val)`.
- **Loop condition `while curr.next` skips the last node** — should be `while curr` since `curr` itself becomes `None` after the last node.
- **Forgot to advance `curr`** inside the loop on first attempt — infinite loop.
- **Tried to create a dummy node for `None`** (val 0) instead of just mapping `None → None` — the copy should point to `None`, not a fake node.
- **Returning the head**: forgot that `oldNewMap[head]` gives you the new head directly — no need for a separate variable.
- **Don't need to handle `next` and `random` separately from each other** — both have the same "node might not exist yet" problem, so both go in the second pass.

## Revisit
- **Struggle level**: hints
- **Intervals**: 3d → 7d → 14d
- **Current interval**: 1
- **Date to revisit**: 2026-03-08
- **Revisit history**:
