## 게임 맵 최단거리

### [문제](https://www.welcomekakao.com/learn/courses/30/lessons/1844)

### 접근법

* 이미 지나간 길은 다시 못가게 막는다. 
```python
map[r][c] = 0 
```

* BFS로 4방면에 대한 탐색을 시도한다. 자료구조는 당연히 Queue를 사용

```python
...
while len(queue):
    answer += 1
    n = len(queue)
    for j in range(n):
        r, c = queue.pop(0)
...        
```