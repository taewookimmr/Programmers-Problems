#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int solution(int n, vector<string> data) {
    map <char, int> dic;
    dic.insert(make_pair('A', 0));
    dic.insert(make_pair('C', 1));
    dic.insert(make_pair('F', 2));
    dic.insert(make_pair('J', 3));
    dic.insert(make_pair('M', 4));
    dic.insert(make_pair('N', 5));
    dic.insert(make_pair('R', 6));
    dic.insert(make_pair('T', 7));
    dic.insert(make_pair('<', -1));  
    dic.insert(make_pair('=', 0));
    dic.insert(make_pair('>', 1));
    
    vector<vector<int> > graph(8, vector<int>(8, 0));
    for (string info : data){
        int n1 = dic[info[0]];
        int n2 = dic[info[2]];
        int ineq = dic[info[3]];
        int dst = info[4]-48;
    }
         
    return 1;
}