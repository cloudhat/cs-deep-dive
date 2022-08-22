# 삽입정렬

from array import array

def insertion_sort(numbers : array) -> array:
    key = 1
    for i in range(key, len(numbers)):
        for j in range(i, 0, -1):
            if numbers[j] < numbers[j-1]:
                numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
                continue
            else :
                break
        key += 1
                     
    return numbers

print(insertion_sort([3,4,2,7,5,6,1]))