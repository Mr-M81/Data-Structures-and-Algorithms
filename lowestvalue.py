#in this code, you are required to find the lowest value of the array. 

mylist = [3,5,21,6,7,3] #i have created a list
# minval = mylist[0]
# for i in mylist:
#     if i > minval:
#         minval = i
# print(minval)

# bubble sort 
# n = len(mylist)
# for i in range (n - 1):
#     for j in range(n - i - 1):
#         if(mylist [j] > mylist[j + 1]):
#             mylist [j], mylist[j+1] = mylist[j+1], mylist[j]
# print(mylist)

mylist = [5,2,9,1,6]
n = len(mylist)

for i in range(n -1):
     for j in range(n-i-1):
        if(mylist[j] < mylist[j+1] ):
              mylist[j], mylist[j+1] = mylist [j+1], mylist[j]
print(mylist)