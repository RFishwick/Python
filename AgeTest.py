print ('Hi!')
myAgeInt = int(input("Please enter your age:"))
message = 'My Age is %d' %(myAgeInt)
print (message)
if myAgeInt > 50:
    print ("You're old!")
else:
    print ("Cool")

deathAgeInt = int(input("At what age will you die?:"))
message = 'You will die at %d' %(deathAgeInt)
print (message)

yearsLeft = deathAgeInt - myAgeInt
message = "That's in %d years" %(yearsLeft)
print (message)

for i in range(yearsLeft):
    print ('Yo %d!' %(i+1))
