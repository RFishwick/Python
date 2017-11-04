## A simple program to convert the Time/Date value in a Splunk extract
## to an Excel readable format

# Open Input file for reading
fileI = open('FileIn.txt', 'r')

s1 = list(fileI) # Read file contents into a list (array)
fileI.close # Close input file

cnt = 0 # Create and assign 0 to count variable
fileO = open('FileOut.txt', 'w') # Open Output file for writing
for line in s1: # Begin For loop
    lineO = line.rstrip() + "\n" # Strip off any trailing characters and replace with a LF as a data cleanup step
    lineO = lineO.replace("14T", "14 ") # Repace the "T" after the date with a single space
    lineO = lineO.replace(".000-0400", "") # Remove the extra time info
    fileO.write(lineO) # Write the line to the file
    cnt += 1 # Increment count variable
	# End of For loop

fileO.close() # Close file
print(cnt, "records") # Print record count on terminal
