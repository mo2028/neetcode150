# Reverse Linked List

## Problem
- **Link**: https://leetcode.com/problems/reverse-linked-list/
- **Description**: Reverse a singly linked list. Return the new head.

## Difficulty
Easy

## Approach
Two approaches covered:

**Recursive:**
- Base case: if `head` is None or `head.next` is None, return `head`
- Recurse on `head.next` to get `newHead` (the last node, which becomes the new head)
- Reverse the link: `head.next.next = head`
- Cut forward link: `head.next = None`
- Return `newHead` unchanged all the way up

**Iterative:**
- Track `prev = None` and `curr = head`
- Each iteration: save `nextNode`, set `curr.next = prev`, advance `prev` and `curr`
- Return `prev` (new head)

## Key Pattern
Pointer reversal — save next, reverse link, advance both pointers.

## Complexity
- **Time**: O(n)
- **Space**: O(1) iterative, O(n) recursive (call stack)

## Mistakes / Learnings
- **Recursive — wrong reversal target**: Used `newHead.next = curr` instead of `curr.next.next = curr`. `newHead` is the final head (last node) and should never be modified — it just gets passed back up unchanged.
- **Recursive — forgot to cut forward link**: After reversing, must set `curr.next = None` or you get a cycle.
- **Recursive — missing null check**: `if not curr or not curr.next` — forgot the `not` before `curr.next`, which inverted the base case condition.
- **Iterative — wrong pointer direction**: Used `curr.next = None` instead of `curr.next = prev`. `None` is only correct for the very first node (original head), and that's handled naturally since `prev` starts as `None`.
- **Iterative — wrong order**: `prev = curr` must happen AFTER `curr.next = prev`, not before. Doing it before creates a self-loop (`curr.next = curr`).
- **Iterative — wrong return**: Return `prev`, not `curr`. After the loop, `curr` is `None`.
- **Key insight**: `newHead` in recursive is always the same node (the last node). It never changes as the recursion unwinds — each level just fixes its own pointer and passes `newHead` up.

## Revisit
- **Struggle level**: struggled
- **Intervals**: 1d → 3d → 7d
- **Current interval**: 1
- **Date to revisit**: 2026-03-23
- **Revisit history**:
