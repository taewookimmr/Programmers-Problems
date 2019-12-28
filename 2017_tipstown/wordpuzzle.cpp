#include <iostream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

typedef struct Chunk_{
    int level;
    string accum;
}Chunk;

int solution(vector<string> strs, string t){
    int answer = -1;
    queue<Chunk> q;
    int n = strs.size();
    for(int i = 0; i <n; i++){
        int m = strs[i].size();
        if (strs[i].compare(t.substr(0, m))==0){
            Chunk chunk = {1, strs[i]};
            q.push(chunk);
        }
    }
    while (q.size()){
        Chunk temp = q.front();
        q.pop();
        if (t.compare(temp.accum)==0){
            answer = temp.level;
            break;
        }else{
            for(int i=0; i<n; i++){
                int l = temp.accum.size();
                int k = strs[i].size();
                string remain = t.substr(l);
                if (strs[i].compare(remain.substr(0, k)) == 0){
                    Chunk chunk = {temp.level+1, temp.accum+strs[i]};
                    q.push(chunk);
                }
            }
        }
        
    }
    return answer;
}