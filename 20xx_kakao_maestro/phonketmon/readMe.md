## 폰켓몬

### [문제](https://www.welcomekakao.com/learn/courses/30/lessons/1845)

### 접근법

* pool에 있는 폰켓몬 종류의 수를 구하기 위해 set을 사용한다. 

```python
def solution(nums):
    myset = set(nums)
    m = len(nums)//2
    if len(myset) >= m :
        return m
    else : 
        return len(myset)
```

