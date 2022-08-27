def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		left_array = arr[:mid]
		right_array = arr[mid:]
		merge_sort(left_array)
		merge_sort(right_array)

		i = j = k = 0

		while i < len(left_array) and j < len(right_array):
			if left_array[i] < right_array[j]:
				arr[k] = left_array[i]
				i += 1
			else:
				arr[k] = right_array[j]
				j += 1
			k += 1

		while i < len(left_array):
			arr[k] = left_array[i]
			i += 1
			k += 1

		while j < len(right_array):
			arr[k] = right_array[j]
			j += 1
			k += 1

arr = [42, 12, 11, 13, 5, 6, 7, 188, 43, 1, 79]
merge_sort(arr)
print(arr)