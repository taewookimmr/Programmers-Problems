def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    for i in range(n):
        m = len(phone_book[i])
        for j in range(i+1, n):
            if phone_book[i] == phone_book[j][:m]:
                return False

    return True



pb = ["119", "97674223", "1195524421"]
print(solution(pb))