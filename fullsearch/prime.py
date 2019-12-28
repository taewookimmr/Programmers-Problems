# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
import math

def is_prime(number):
	if number == 0 or number == 1:
		return False
	sq = int(math.sqrt(number))
	for i in range(2, sq+1, 1):
		if number % i == 0:
			return False
	return True 

def p_sieve(n):
    a = [False, False] + [True]*(n-1)
    primes = []
    for i in range(2, n):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

def solution(numbers):
    a = " ".join(numbers)
    b = a.split()  
    b.sort(reverse = True)
    d = "".join(b)
    e = int(d)

    answer=[]
  
    for i in p_sieve(e+1):

        count = 0
        copied = []
        copied += b
        # print(copied)
        chars = " ".join(str(i))
        chars = chars.split()
        for c in chars:
            try :
                copied.remove(c)
            except :
                count += 1
                break
        if count == 0:
            answer.append(i)
        
    print(answer)
    return len(answer)
    # return (answer)

from itertools import permutations

def best_solution(n):
    a = set()

    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    # print(a)
    a -= set(range(0, 2))
    # print(a)
    # 아래에서부터는 소수가 아닌 것을 제거하는 과정 
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

numbers = "177"
print(best_solution(numbers))




    
