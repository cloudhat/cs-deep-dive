##1.2-2
#Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size n, insertion sort runs in 8n2 steps, while merge
#sort runs in 64n lg n steps. For which values of n does insertion sort beat merge sort?
#삽입 정렬이 병합 정렬을 능가하는 n 값은 무엇입니까?
import math

n = 2

while 8*(n**2) > 64*n*math.log2(n):
    n+=1

print(n-1)


##1.2-3
#What is the smallest value of n such that an algorithm whose running time is 100n2
#runs faster than an algorithm whose running time is 2n on the same machine?
#100n2 알고리즘이 실행시간2n인 알고리즘보다 빠르게 실행되는 가장 작은 n의 값은??

n = 1

while 100*(n**2) > 2**n:
    n+=1

    
print(n)


## 삽입정렬?
##삽입 정렬은 두 번째 자료부터 시작하여 그 앞(왼쪽)의 자료들과 비교하여 삽입할 위치를 지정한 후 자료를 뒤로 옮기고 지정한 자리에 자료를 삽입하여 정렬하는 알고리즘이다.
#두 번째 자료는 첫 번째 자료, 세 번째 자료는 두 번째와 첫 번째 자료, 네 번째 자료는 세 번째, 두 번째, 첫 번째 자료와 비교한 후 자료가 삽입될 위치를 찾는다. 자료가 삽입될 위치를 찾았다면 그 위치에 자료를 삽입하기 위해 자료를 한 칸씩 뒤로 이동시킨다.처음 Key 값은 두 번째 자료부터 시작한다.

## 병합정렬
#  간단히 말해 어떤 문제를 우선 작은 문제로 쪼개고 난 후 다시 조합하여 원래의 문제를 푸는 것