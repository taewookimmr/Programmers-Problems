#include <iostream>
#include <vector>
using namespace std;
long long MAX = 10000;
long long solution(vector<vector<int> > recs)
{   
    vector<vector<int> > check(MAX, vector<int>(MAX, 0));
    int n=recs.size();
    int xmax=0;
    int ymax=0;
    for(int i = 0; i < n; i++){
        int x1=recs[i][0];
        int y1=recs[i][1];
        int x2=recs[i][2];
        int y2=recs[i][3];
    }
    long long answer = -1;
    return answer;
}