# 삽입정렬

def insertion_sort(num_list : list) -> list:
    key = 1
    for i in range(key, len(num_list)):
        for j in range(i, 1, -1):
            if num_list[j] < num_list[j-1]:
                num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
                continue
            else :
                break
        key += 1
                     
    return num_list

print(insertion_sort([1,3,4,2,7,5,6]))