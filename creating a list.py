mylist=[]
print("initial blank list:")
print(mylist)

# addition of elements in the list
mylist.append(1)
mylist.append(2)
mylist.append(4)
print("\nlist after addition of three elements:")
print(mylist)

# adding elements to the list using iterator
for i in range (1,4):
    mylist.append (i)
print("\nlist after addition of elements from 1-3:")
print(mylist)

mylist.append((5,6))
print("\nlist after addition of tupple:")
print(mylist)


list2=['car','cat']
mylist.append(list2)
print(mylist)
