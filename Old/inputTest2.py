tName = ("Claire", "Corey", "Matthew", "Randy")

aName = input("Enter a Name: ")
print("Hi " + aName)

if aName in tName:
	print("I know ", aName)
	print("You're cool!")
else:
	print("Who the heck is", aName + "?")

