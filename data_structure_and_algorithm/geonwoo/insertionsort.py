list = [6, 5, 9, 7, 3, 1, 6, 2, 4, 8]

for i in range(1, len(list)):
    for j in range(i, 0, -1): 
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break
            
print(list)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
