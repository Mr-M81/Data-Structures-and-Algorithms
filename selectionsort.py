# Problem Statement:

# Write a function that takes an unsorted array of integers and sorts it in ascending order using Selection Sort.

# You must:
# 	•	Find the minimum element in the unsorted part
# 	•	Swap it with the first unsorted index
# 	•	Repeat until the array is fully sorted

## Pseudcode:
# for i from 0 to n-1:
#     min_index = i
#     for j from i+1 to n:
#         if arr[j] < arr[min_index]:
#             min_index = j
#     swap arr[i] and arr[min_index]

my_array = [2, 6, 3, 5, 7, 9, 1]
n = len(my_array)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]

print(my_array)
