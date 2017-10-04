class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in range(len(s) + 1)]
        max_len = 0
        # dp[0] = 0
        for i in range(1, len(s)):
            if s[i] == '(':
                continue
            if i >= 1 and s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i > 1 else 0) + 2
            else:
                if i - dp[i - 1] >= 1 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = 2 + dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0)
            if dp[i] > max_len:
                max_len = dp[i]
        for i in dp:
            print i
        return max_len


class Solution1(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        f = [[None for i in range(len(s) + 2)] for j in range(len(s) + 2)]
        for k in range(2, len(s) + 1, 2):
            for i in range(len(s) - k + 1):
                j = i + k
                if k == 2:
                    if s[i:j] == '()':
                        # print i, j, f[i][j]
                        f[i][j] = True
                        # print i, j, f[2][4]
                    else:
                        f[i][j] = False
                elif s[i] == '(' and s[j - 1] == ')':
                    if f[i + 1][j - 1] is True:
                        f[i][j] = True
                    else:
                        f[i][j] = False
                        for m in range(i, j - 1):
                            # print i, j, m, s[m:m + 2], f[i][m + 1], f[m + 1][j]
                            if s[m:m + 2] == ')(' and f[i][m + 1] and f[m + 1][j]:
                                f[i][j] = True
                                break
                if f[i][j] and k > max_len:
                    max_len = k
        return max_len

def main():
    print Solution().longestValidParentheses("(()))())(")

if __name__ == '__main__':
    main()