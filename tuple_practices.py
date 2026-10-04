#Here we are going to see a tuple functions

#Tuple syntax
tup = (10,20,30,40,50)
print(tup)

#Print indexing based output
print(tup[2])

#Print indexing, range and step based output
print(tup[0:2])    #Starting : Ending
print(tup[0:4:2])  #Starting : Ending : Step
print(tup[::2])    #Default starting : Default Ending : Step
print('Reverse tuple: ',tup[4:0:-1]) # reverse Indexing - Ending : Starting : step (negative value)

#Print length of tuple
print("Length of tuple is: ",len(tup))

#Store full length of String in Tuple
st_tup = tuple('Fantastic life ahead')
print(st_tup)
print('Length of the string tuple: ', len(st_tup))

#Reverser string
print('Reverse string: ', st_tup[20:0:-1])