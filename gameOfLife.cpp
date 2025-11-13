#include <vector>
#include <utility>

using namespace std;

class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int rows = board.size();
        int cols = board[0].size();

        vector<pair<int,int>> directions = {
            {-1, -1}, {-1, 0}, {-1, 1},
            {0, -1}, {0,1},
            {1,-1}, {1,0}, {1,1}
        };

        vector<vector<int>> oldBoard = board;

        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                int live_neighbors = 0;

                // Count live neighbors
                for (auto &d: directions){
                    int nr = r + d.first;
                    int nc = c + d.second;
                    if (nr >= 0 and nr < rows and nc >= 0 and nc < cols) {
                        if (oldBoard[nr][nc] == 1) {
                            live_neighbors++;
                        }
                    }
                }

                // Apply rules
                if (oldBoard[r][c] == 1) {
                    if (live_neighbors < 2 or live_neighbors > 3)
                        board[r][c] = 0;
                    else
                        board[r][c] = 1;
                } else {
                    if (live_neighbors == 3)
                        board[r][c] = 1;
                    else
                        board[r][c] = 0;
                }
            }
        }
    }
};
