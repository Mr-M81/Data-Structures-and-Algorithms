# ⚔️ INTERVIEW CHALLENGE: Return the Second Largest Number in an Array


# Write a function that returns the second largest number in a given list of integers.
# Don’t use built-in sort functions like .sort() or sorted().

# Input:  [12, 35, 1, 10, 34, 1]
# Output: 34

# Input:  [10, 10, 10]
# Output: No second largest found

input = [12, 38, 1, 10, 34, 1]
largest = input[0]
second_largest = input[1]

# for i in range (len(input)):
#     if input[i] > largest:
#         second_largest = largest[i]
#         largest = input[i]
#     elif input > second_largest[i] and input
# print(second_largest)

#this wont work 

# for num in input:
#     if num > input:
#         second_largest = input
#         input = num
#     elif num > second_largest:
#         second_largest = num 
# print(second_largest)


#Write a prgram that finds the second number in an array

# arr = [6,8,2,9,10]

# first = arr[0]
# second = arr[1]

# for num in arr:
#     if num > first:
#         second = first 
#         first = num
#     elif second < num and num != first:
#         second = num
# print(second)

# # time complexities 
# for i in range(1,3):
#     print i # this is more aligned to constant time which is O(1)

# for i in range(1,3):
#     for j in range(1,4):
#         print(i, j)
# #Quadratic time , nested for loops , 0 squared

# in an array, find the third largest number 

array = [0,4,8,2,1]
first = float('-inf')
second = float('-inf')
third = float('-inf')

for num in array:
    if (num > first):
        second = first
        first = num 
    elif (second < num and num != first):
        third = second
        second = num 
    elif (third < num and num != second):
        third = num 
print(third) 