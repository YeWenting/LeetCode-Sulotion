# Leetcode Solution

### P4 Median of Two Sorted Arrays

Solution:

https://leetcode.com/problems/median-of-two-sorted-arrays/solution/

Histroy:

- Attempt I
  - BUG: the condition of "while" clause: while (min_l <**=** max_l)
- Attempt II
  - BUG: return **float**((lnum + rnum)) / 2