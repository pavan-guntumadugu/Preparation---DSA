# creation of array
import array as ar
array1 = ar.array('i',[1,21,3,4,5])
print(array1)

#inserion in array (need to specify index and value)
array1.insert(1, 6)
print(array1)

#traversal in array
for i in array1:
    print(i)

#Accesing element in array
def array_access(array1, index):
    return(print(array1[index]))
array_access(array1, 3)
print(f'array is: {array1}')

#linear searching in array
def linear_search(array,value):
    for index in range(len(array)):
        if array[index] == value:
            return(print(f'index of value is: {index}'))
        
linear_search(array1, 5)

#deletion in array
array1.remove(21)
print(f'array after deletion is: {array1}')

#rest of one dimensional array operations are there in the Arrays-practice.py
