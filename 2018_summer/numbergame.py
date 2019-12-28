def solution(A, B):
    answer= 0
    A.sort()
    B.sort()
    n = len(B)
    for i in range(n):
        for j in range(len(B)):
            if B[j] > A[i]:
                answer += 1
                B.remove(B[j])
                break

    return answer 