def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


res = []
for N in range(1, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R += convert(sum(map(int, R)), 3)
    R = int(R, 3)
    if R % 2 == 0 and R > 220:
        res.append(R)

print(min(res))
