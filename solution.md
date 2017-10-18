## Tips

1. Don't have the idea? See **more examples**!
2. The first thing is to examine special case of input (e.g. **len** is too short)
3. Watch your **index** when using list!!

## Leetcode Solution

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

**Interesting finding**

During coding, I found out in the python, you cannot using *f = [[0] * 2] * 3* to initilaize a 2-d array. However, it's okay to use *f = [0] * 3*. The reason behind this is the **list** is *mutable variable*, while the **int** is *immutatble variable*. When applying a ***** operation to list, it will duplicate the list using the same refference. If the list contains int, assignment will create a new int and assign it. But if the element of list is list, it will not create a new list when assign one element. As a result, it modify all the value in one row

More reading see [here](https://rg03.wordpress.com/2007/04/21/semantics-of-python-variable-names-from-a-c-perspective/)



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



### P55 Jump Game

- Attempt I
  - Define a set *f* to be the set of reachable index, and iterate the array from start. If this index is in the *f*, then we can update the *f* since we can perform *jump* operation here.
  - This method TLE in the last data
- Attempt II
  - After a little consideration, I found out we don't need to maintain this *f* and just store the *farest* index we can arrive. It saves the operation of maintain *f*, and cut the time complexity from O(nm) to O(n) (m is the average of MAX_JUMP)
- This simple solution can even beat 89.5% solution… (
- The fastest solution search from the right to make it faster, it's smart.

### P141&P142

- Purpose: detect and identify the loop in linklist
- **BUG**
  - check if the head is nullptr
  - consider the boundry scenario (one node, no loop)

### P218 The Skyline Problem

- Kind of like simulation
- Maintain a heap, which stores the (height, x_covariate) of the upper-right node of building who we are examining
- We only care about the highest building at one time
- If the current new building is far from the highest, it means current highest building will not affect by the future high building, so add it to the result and delete it from the heap, and also delete the one that control by it.
- If the current new building is under the reach of highest
  - add it to the heap (add all the building starting at the same x-covariate)
  - if the new height is higher than the old maxinum, then add to the result

### P319 Bulb Switcher

- Oberser the data, if Bulb *i* is still open, *i* has odd number of factors.

### P7 Reverse Interger

- I found in the c++, the mod of a negtive is not like what I thought before. I thought the remainder is always a non-negative number, however it isn't. Let says -1 / 3 = -0.333… then the quoitent is -0, and the remainder is -1. So both *a* and *-a*, they will have the same quotient and the remainder.

### p42 Trapping rain water (*)

- This is quite a interesting problem.
- Attempt I:
  - I think the water could only be stored in the near neighboor, which is limited by the *peak point*
  - However, it's clearly wrong, like [5, 1, 2, 1, 2, 5]. The water can store in the two 5
- Attempt II:
  - I look the solution, find out for each bar, the maxinum of water is determined by the *min{l[i], r[i]}*, which l[i] is maxinum in 0..i, and r[i] is maxinum in i..n-1.
  - Easily accept by some preprocess
- Other solution:
  - Stack: Store all the *critical bar*
    - while the height[i] > stack_top
      - stack.pop()
      - add the answer (since the lower side has been determined)
    - push the height[i] to the stack
    - Only one loop
  - Two pointer
    - In Attempt II we know that the answer is determined by the *l, r*. Now we consider not to calculate all of the *l, r*
    - Initialize i = 0, j = -1
    - Update the l[i] and r[j]
    - if l[i] < r[j]
      - so l[i] **must** lower than the r[i], so the ans is determined by leftside
      - Add to the answer and l++
    - Same thing happens in another situation
    - Only one loop