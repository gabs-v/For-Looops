#for loop notes and practice :) 

#Note: for loops allows us to loop over diffrent collections
#  Kinda like while loops but more specific


#for loops with strings
for letter in "Coding Dojo": #prints out everty letter while it goes through the ideration
    print(letter)



#for loops in arrays
friends = ["Kevin", "Jim" , "Karen"] #defining the array
for friend in friends: #making the for loops
    print(friend)

#using range with arrays to figure out how many elements are inside
friends = ["Kevin", "Jim" , "Karen"] #defining the array
for index in range (len(friends)): #making the for loops.
    print(friends[index]) # allows us the access each individual friend in array


#for loops with number  
for index in range (10): #making the for loops; Will print out everythin until 10 but the number 10 
    print(index)

for index in range (4, 10): #print out numbers raning from 4-10; will print 3 but not 10 
    print(index)

for index in range (4, 10, 2 ): #print out numbers raning from 4-10; will print 3 but not 10; Will go up my 2
    print(index)
