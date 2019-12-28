// 참고하고 공부하겠습니다!
// 파이썬으로 풀기 전에 cpp보고 공부
#include <vector>
using namespace std;
#define MIN_CORE_WORKTIME 10000

int solution(int n, vector<int> cores) {
    int size = cores.size();
    int mincore = MIN_CORE_WORKTIME + 1;
    int maxcore = 0;
    int left = 0;
    int right = 0;
    int mid = 0;

    if(n <= size) return n;

    for(int i  = 0; i < size; ++i){
        if(mincore > cores[i]) mincore = cores[i];
        if(maxcore < cores[i]) maxcore = cores[i];
    }

    left = (mincore * (n - size)) / size;
    right = (maxcore * (n - size)) / size;

    int corework ;
    int currentwork ;
    while(left <= right){
        corework= size; 
        currentwork = 0;
        mid = (left + right) / 2;
        for(int core : cores){
            corework += (mid / core); 
            if((mid % core) == 0) ++currentwork; 
        }
        if(n > corework) left = mid + 1;
        else if(n <= (corework - currentwork)) right = mid - 1;
        else {
            int tmpwork = corework - currentwork;
            for(int i = 0; i < size; ++i){
                if((mid % cores[i]) == 0) ++tmpwork;
                if(tmpwork == n) return (i + 1);
            }
        }
    }
    return 0;
}