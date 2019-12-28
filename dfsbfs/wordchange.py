
def similarity(w1, w2):
    count = 0
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            count +=1
    return count

def getCandidate(p_word, words):
    candidate = []
    for w in words:
        if similarity(p_word, w) == len(p_word)-1:
            candidate.append(words.index(w))
    return candidate

def matmul(mat1, mat2):
    n = len(mat1)
    m = len(mat2[0])
    l = len(mat1[0])
    result = [[0 for x in range(m)] for y in range(n)]

    for i in range(n):
        for j in range(m):
            sum = 0
            for k in range(l):
                sum += mat1[i][k] *mat2[k][j]
            result[i][j] = sum
    return result


def solution(begin, target, words):
    try :
        target_index = words.index(target)
    except :
        return 0

    p_word = begin
    candi = getCandidate(p_word, words)

    if len(candi) == 0:
        return 0

    n = len(words)
    g = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if similarity(words[i], words[j]) >= len(words[0])-1:
                g[i][j] = 1
                g[j][i] = 1

    answer = []
    for c in candi:
        count = 2
        temp_mat = g
        while True:
            if temp_mat[c][target_index] !=0 :
                break
            else : 
                temp_mat = matmul(temp_mat, g)
                count += 1
        answer.append(count)
    return min(answer)
   


         
            

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# begin = "hit"
# target = "hhh"
# words = ["hhh","hht"]
result = solution(begin, target, words)
print(result)