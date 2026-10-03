# Here we are going to see List
# List is mutable and Indexing

#Syntax for List
lst1 = [10,20,30,40]
print(lst1)

lst2 = [100,200,300,400]
print(lst2)

#print based on  positive  or forward indexing
print('Print value from index 1: ', lst1[1])  # it will print the value in 1 positive or forward indexing

#print based on negative or backward indexing
print('Print value in -2 index: ', lst2[-2])

#Append the list
lst1.append(50)
print('Appended list values: ', lst1)

#Indexing insert values in the list
lst2.insert(500,2)
print('Indexing insert values: ', lst2)

#Remove values from the list
lst1.remove(10)
print('Removed values from list: ', lst1)

#Extend values in the list
lst1.extend([60, 70,80])
print('Extend values in the list: ', lst1)

#Pop values from the list
lst1.pop()
print('pop return value: ', lst1.pop())
print('Pop value from the list: ', lst1)







