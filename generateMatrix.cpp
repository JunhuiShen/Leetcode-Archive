// Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

// Example 1:


// Input: n = 3
// Output: [[1,2,3],[8,9,4],[7,6,5]]
// Example 2:

// Input: n = 1
// Output: [[1]]
 

// Constraints:

// 1 <= n <= 20

#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n));

        int num = 1;
        int start = 0;   // top-left corner of current layer
        int len = n;     // side length of current layer

        while (len > 0){
            if (len == 1){
                ans[start][start] = num;
                break;
            }

            // top row: left to right
            for (int j = start; j < start + len - 1; j++) {
                ans[start][j] = num++;
            }

            // right column: top to down
            for (int i = start; i < start + len - 1; i++){
                ans[i][start + len - 1] = num++;
            }

            // bottom row: right to left
            for (int j = start + len - 1; j > start; j--){
                ans[start + len - 1][j] = num++;
            }

            // left column: down to top
            for (int i = start + len - 1; i > start; i--){
                ans[i][start] = num++;
            }

            start++;
            len -= 2;
        }

        return ans;
            
    }
};