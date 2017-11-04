aList = ["All","Clear"]
numList = [1, 2, 3]
print(aList, numList)
bigList = [aList,numList]
print(bigList)
print(bigList[0][0])
print("\nbothList...")
bothList = aList + numList
print(bothList)
print(bothList[3])
for v1 in bothList:
	print(v1)
	if v1 == "Clear":
		print(" Yes!")
	
