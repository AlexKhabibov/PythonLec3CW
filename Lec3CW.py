# Функция Фибоначи
# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib (n-1) + fib(n-2)

# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)

# Быстрая сортировка:

# def quick_sort (array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     left_part_elem = [i for i in array[1:] if <= pivot]
#     right_part_elem = [i for i in array[1:] if > pivot]
#     return quick_sort(left_part_elem) + [pivot] + quick_sort(right_part_elem)

# print (quick_sort([12, 3, 4, 56, 34, 12, 3 ]))

# Сортировка слиянием:

# def merge_sort(nums): 
#     if len(nums) > 1:
#         mid = len(nums) // 2 
#         left = nums[:mid] 
#         right = nums[mid:] 
#         merge_sort(left) 
#         merge_sort(right) 
#         i=j=k=0
#         while i < len(left) and j < len(right): 
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1 
#             else:
#                 nums[k] = right[j]
#                 j += 1 
#             k += 1
#         while i < len(left): 
#             nums[k] = left[i] 
#             i += 1
#             k += 1
#         while j < len(right): 
#             nums[k] = right[j] 
#             j += 1
#             k += 1

# nums = [38, 27, 43, 3, 9, 82, 10] 
# merge_sort(nums)
# print(nums)