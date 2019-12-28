#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef struct Kakao_{
    int row;
    int col;
    int color;
}Kakao;

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int island = 0;
    vector<int> arealist;
    for (int i = 0; i < m; i++){
        for (int j = 0; j < n; j++){
            if (picture[i][j]){
                island+=1;
                int area = 0;

                queue<Kakao > q;
                Kakao kakao = {i, j, picture[i][j]};

                picture[i][j] = 0; // 방문했으면 지워버려용
                area+=1; // 방문했다는 표시로 카운트를 올려용

                q.push(kakao);
                while (q.size()){
                    Kakao prev = q.front();
                    q.pop();
                    
                    // up
                    if (prev.row -1 >= 0){
                        if (picture[prev.row-1][prev.col] == prev.color){
                            Kakao temp={prev.row-1,prev.col, picture[prev.row-1][prev.col]};
                            q.push(temp);
                            picture[prev.row-1][prev.col] = 0; // 방문했으면 지워버려용
                            area+=1; // 방문했다는 표시로 카운트를 올려용
                        }
                    }
                    // left
                    if (prev.col - 1 >= 0){
                        if (picture[prev.row][prev.col-1] ==  prev.color){
                            Kakao temp={prev.row,prev.col-1,picture[prev.row][prev.col-1] };
                            q.push(temp);
                            picture[prev.row][prev.col-1] = 0; // 방문했으면 지워버려용
                            area+=1; // 방문했다는 표시로 카운트를 올려용
                        }
                    }
                   // down
                    if (prev.row +1 < m){
                        if (picture[prev.row+1][prev.col] ==  prev.color){
                            Kakao temp={prev.row+1,prev.col,picture[prev.row+1][prev.col]};
                            q.push(temp);
                            picture[prev.row+1][prev.col] = 0; // 방문했으면 지워버려용
                            area+=1; // 방문했다는 표시로 카운트를 올려용
                        }
                    }
                   // right
                    if (prev.col +1 <  n){
                        if (picture[prev.row][prev.col+1] ==  prev.color){
                            Kakao temp={prev.row, prev.col+1, picture[prev.row][prev.col+1]};
                            q.push(temp);
                            picture[prev.row][prev.col+1] = 0; // 방문했으면 지워버려용
                            area+=1; // 방문했다는 표시로 카운트를 올려용
                        }
                    }
                }//while loop end
                arealist.push_back(area);
            }
        }
    }
    vector<int> answer(2);
    answer[0] = island;
    answer[1] = *max_element(arealist.begin(), arealist.end());
    return answer;
}