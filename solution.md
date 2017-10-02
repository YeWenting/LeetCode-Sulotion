# Leetcode Solution

### P4 Median of Two Sorted Arrays

Solution:

https://leetcode.com/problems/median-of-two-sorted-arrays/solution/

Histroy:

- Attempt I
  - BUG: the condition of "while" clause: while (min_l <**=** max_l)
- Attempt II
  - BUG: return **float**((lnum + rnum)) / 2

### P10 Regular Expression Matching

Sort of like search with a cache, of course you can call it DP...

At first, when I encounter the *, I will iterate which part it will replace. But actually you can just escape this by simply using: f[i,j] = (first_match and f[i+1, j]) or f[i, j+2]



