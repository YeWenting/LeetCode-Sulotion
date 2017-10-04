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



### P32 Longest Valid Parentheses

- Solution I
  - f[i, j] denotes whether substring s[i: j] is legal
  - f[i, j] = true if (f[i+1, j-1]) or (f[i, k] and f[k, j] and s[k-1] == ')' and s[k] == '(')
  - Prerequisite
    - j - i % 2 == 0
    - s[i] == '(' and s[j-1] == ')'
  - TLE: Overall time complexity is O(n^3)
- Solution II
  - f[i] denotes the longest valid parenthese ending at index i
  - Prerequisite
    - s[i] == ')'
  - if s[i-1] == '('
    - f[i] = (f[i - 2] if i >= 2 else 0) + 2
  - if s[i-1] == ')'
    - Then we need a extra '(' to match s[i] (which is ')')
    - Before this extra '(', there may be a valid parenthese string before and after it
    - f[i] = 2 + f[i-1] + f[i - f[i - 1] - 2]
    - Why must be f[i -1], which means the extra '(' is right before the longest parenthesis?
      - It's clearly that there won't be any extra '(' in the longest valid string, so this '(' should only be before the longest valid string. But if it's not at i - f[i - 1] - i, then this string will be invalid.
  - Histroy
    - Attempt I: forget to check whether the index is valid
  - ​