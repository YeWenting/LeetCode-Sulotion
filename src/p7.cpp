//
// Created by YeWenting. on 18/10/2017.
//

#include <iostream>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int ans = 0;
        while (x) {
            int temp = ans * 10 + x % 10;
            if (temp / 10 != ans)
                return 0;
            ans = temp;
            x /= 10;
        }
        return ans;
    }
};

int main(void)
{
    return 0;
}