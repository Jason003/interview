# Python code to demonstrate copy operations

# importing "copy" for copy operations
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using deepcopy to deep copy
li2 = copy.copy(li1)

# original elements of list
print("The original elements before deep copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

print("\r")

# adding and element to new list
li2[2][0] = 7

# Change is reflected in l2
print("The new list of elements after deep copying ")
for i in range(0, len(li1)):
    print(li2[i], end=" ")

print("\r")

# Change is NOT reflected in original list
# as it is a deep copy
print("The original elements after deep copying")
for i in range(0, len(li1)):
    print(li1[i], end=" ")

A = [(1,2,3),(1,2,3)]
B = copy.copy(A)
B[0] = (1,2,3,4)
print(A)