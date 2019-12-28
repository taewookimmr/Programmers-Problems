#include <vector>
#include <algorithm>

using namespace std;

int n ;
int myP, myQ;
vector<int> myland;


long long func(long target){
    long long result = 0;
    for(int i = 0; i < n*n; i++){
         result += (long long)(target - myland[i]>= 0 ? (target-myland[i])*myP : (myland[i]-target)*myQ);
    }
    return result;
}
long long solution(vector<vector<int> > land, int P, int Q)
{
    myP = P;
    myQ = Q;
    n = land.size();
    vector<long long> answer;
    for(int i = 0; i < n; i++)
        for(int j =0; j<n; j++)
            myland.push_back(land[i][j]);
    sort(myland.begin(), myland.end());
    int maxh = myland[n*n-1];
    int minh = myland[0];

    int left = minh;
    int right = maxh;
    int x = (left+right)/2;
    while(left < right){

        if(func(x) < func(x+1)){
            right = x ;
        }else {
            left = x+1;
        }
        x = (left+ right)/2;
    }
    return func(x);


}