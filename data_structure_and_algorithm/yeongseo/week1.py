import math

# 1.2-2
n = 2

while 8 * (n**2) < 64 * n * math.log2(n): 
    # insertion이 merge보다 낫다면(연산수가 적다면)
    n += 1

print(n-1)

# 1.2-3
k = 1

while 100*(k**2) > 2**k:
    k += 1

print(k)