## 배달, level 3

### [문제](https://www.welcomekakao.com/learn/courses/30/lessons/12978)

### 접근법

* floyd 알고리즘 사용, 3중 for문

```python
for y in range(1, N+1):
    for i in range(1, N+1):
        for x in range(1, N+1):
            graph[x][i] = min(graph[x][i], graph[x][y] + graph[y][i])
```