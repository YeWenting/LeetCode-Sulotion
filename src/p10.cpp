#include <iostream>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int n = s.length();
        int m = p.length();
        bool **f = new bool*[n + 1];
        for (int i = 0; i < n + 1; i++)
        {
            f[i] = new bool[m + 1];
            f[i][m] = false;
        }
        for (int j = 0; j < m; j++)
            f[n][j] = false;
        f[n][m] = true;

        for (int j = m - 1; j >= 0; j--)
            for (int i = n; i >= 0; i--)
            {
                if (p[j] == '*') f[i][j] = false;
                else if (j < m - 1 && p[j + 1] == '*')
                {
                    int r_most;     // the new start
                    if (p[j] == '.') r_most = n;
                    else
                    {
                        r_most = i;
                        while (r_most < n && s[r_most]==p[j]) r_most++;
                    }
                    f[i][j] = false;
                    for (int k = i; k <= r_most; k++)
                        if (f[k][j + 2] == true)
                        {
                            f[i][j] = true;
                            break;
                        }
                }
                else if (p[j] != '.' && s[i] != p[j]) f[i][j] = false;
                else f[i][j] = (i < n) && f[i + 1][j + 1];
            }

        return f[0][0];

    }
};

int main(int argc, char const *argv[])
{
    Solution *my_solution = new Solution();
    cout << my_solution->isMatch("baba", "b*.*") << endl;
    return 0;
}