# A Python Program to sort lines in a file

s1 = "" # Clear List Variable (prob not needed)

# Open Input file for reading
fileI = open('FileIn.txt', 'r')

s1 = list(fileI) # Copy file contents into a list (array)
fileI.close # Close input file

s1.sort() # Sort List s1

cnt = 0 # Clear Count Variable
fileO = open('FileOut.txt', 'w') # Open Output file for writing
for line in s1: # Begin For Loop
    lineO = line.rstrip() + "\n" # Format line and store in lineO variable
    fileO.write(lineO) # Write Line
    cnt += 1 # Increment Count Variable

print(cnt, "records") # Print Record Count
fileO.close() # Close File
