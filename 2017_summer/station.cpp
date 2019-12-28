#include <iostream>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int solution_old(int n, vector<int> stations, int w)
{
    int *reach = (int*) malloc(sizeof(int) * (n+1));
    for (int i = 1 ;i <= n; i++)
        reach[i] = 0;
    int m = stations.size();
    
    int start, end;
    for (int s : stations){
        start = max(s-w, 1);
        end = min(n, s+w);
        for (int i = start; i<=end; i++)
            reach[i] = 1;
    }

    
    int count = 0;
    int i = 1;
    while(i <= n){
        if (reach[i]== 0){
            count ++;
            i += (2*w +1);
        }else{
            i+= 1;
        }
    }
    return count;
        
}

int solution(int n, vector<int> stations, int w)
{
    queue<int> q;
    for (int s : stations){
        q.push(max(s-w, 1));
        q.push(min(n, s+w));
    }

    int count = 0;
    int i = 1;

    int onedex_s = n+1;
    int onedex_e = n+1; 
    if (q.size()){
        onedex_s = q.front(); q.pop();
        onedex_e = q.front(); q.pop();
    }

    while(i <= n){
        if (i < onedex_s){
            count ++;
            i += (2*w +1);
        }else{
            i = onedex_e+1;
            if (q.size()){
                onedex_s = q.front(); q.pop();
                onedex_e = q.front(); q.pop();
            }else{
                onedex_s = n+1;
                onedex_e = n+1;
            }
        }
    }
    return count;
        
}