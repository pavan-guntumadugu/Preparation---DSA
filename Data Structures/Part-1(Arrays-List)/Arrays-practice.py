#this covers all 16 operations that we can do on the arrays
import array as arr
array2 = arr.array('i', [3,5,8,9,0,21,34,56]) # declaration
# for i in array2:                 #traversing
#     print(i) 
print(f'initial array: {array2}')
array2.append(28) #appending command
array2.insert(2,39) #insertion
array2.remove(56)
print(f'updated array after append, insertion, remove: {array2}') 
array2.pop()
print(f'poped array: {array2}')
array3 = arr.array('i', [8,9,3,4,5])
array2.extend(array3) #extending the array
print(f'extended array: {array2}')
list1 = [9,0,1]
array2.fromlist(list1) #updated array generated from list
print(f'updated list: {array2}')
print(f'count of occurances: {array2.count(8)}') #counting no of occurances
print(f'accessing the index of particular value is: {array2.index(8)}') # accessing index 
# we can use tostring, to list  but it we cant see the string converted characters since it is non readable
#slicing
print(f'conversion to list {array2.tolist()}')
print(f'slicing   {array2[0:5]}')