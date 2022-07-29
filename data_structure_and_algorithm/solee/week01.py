# 1.2-3
# What is the smallest value of n such that an algorithm whose running time is 100n2
# runs faster than an algorithm whose running time is 2n on the same machine?

n = 0
while True:
    n += 1
    if 100*(n**2) < 2**n :
        print(n)
        break


# 100*n제곱인 알고리즘과 2의 n제곱인 알고리즘보다 더 빨리 실행되는 가장 작은 n값은?
# == 100n2 < 2n