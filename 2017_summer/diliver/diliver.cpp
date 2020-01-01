#include <iostream>
#include <stdlib.h>
#include <vector>
using namespace std;

int solution(int N, vector<vector<int> > road, int K) {
    long MAX = 100000000;
    int **graph;
    graph = (int**)malloc(sizeof(int*)*(N+1));

    for(int i = 0; i < N+1; i++){
        graph[i] = (int*)malloc(sizeof(int)*(N+1));
    }
    for(int i = 1; i < N+1;i++){
        for(int j = 1; j < N+1; j++){
            graph[i][j] = MAX;
            if (i == j)
                graph[i][j] = 0;
        }
    }

    int m = road.size();
    for(int i = 0; i < m; i ++){
        int n1 = road[i][0];
        int n2 = road[i][1];
        int w  = road[i][2];
        if (graph[n1][n2] > w){
            graph[n1][n2] = w;
            graph[n2][n1] = w;
        }
    }

    for (int x = 1; x < N+1; x++){
        for (int y = 1; y < N+1; y++){
            for (int i = 1; i < N+1; i++){
                if(graph[x][i] > graph[x][y] + graph[y][i]){
                    graph[x][i] = graph[x][y] + graph[y][i];
                }
            }
        }
    }
    int answer = 0;
    for(int i = 1; i < N+1; i++){
        if (graph[1][i] <= K){
            answer += 1;
        }
    }

    return answer;

}