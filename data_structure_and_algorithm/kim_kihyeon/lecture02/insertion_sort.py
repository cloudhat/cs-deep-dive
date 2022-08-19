# 삽입정렬
def insertion_sorting(list):
    for i in range(len(list)):
        # max_index로 for문을 돌리기 위함
        max_index = i
        
        for j in range(max_index):
            # 우측 인덱스가 만약 크다면 좌측으로 변경
            if list[max_index] < list[j]:
                # 좌 우 값 변경
                temp = list[j]
                list[j] = list[max_index]
                list[max_index] = temp

    return list

            
print(insertion_sorting([4, 2, 7, 1, 9, 3]))
print(insertion_sorting([1, 5, 4, 10, 98, 77]))


        
         