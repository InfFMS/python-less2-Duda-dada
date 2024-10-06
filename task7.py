n = int(input())
if n == 1:
    print('None')
else:
    res = []
    for i in range(2, n + 1):
        is_prime = 1
        for j in res:
            if i % j == 0:
                is_prime = 0
                break
        if is_prime == 1:
            res.append(i)
        is_prime = 1
    print(*res)
