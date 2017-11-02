# Search for Words in a String

# Define the words to search for
seachWords = ("java", "python")


# Define Functions
def findWords(s):  # Function to find a word within a string
    """Return first instance of word found"""
    result = -1  # Pre-set result to -1
    try:
        s = s.lower();  # Convert string to lower case for searching

        # Loop through words in seachWords and try to find in string s
        for searchWord in seachWords:
            result = s.find(searchWord)
            if result != -1:
                result = searchWord
                break

        # -1 will be returned if no search words found in string s
        return result

    except:
        # Fall through on errors
        return result


# Begin Main Program

fileI = open('theMessage.txt', 'r')  # Open Input file for reading
myText = list(fileI)  # Read file into string myText
fileI.close()  # Close input file

# Print lines that contain the selected word
lineCnt = 0
for line in myText:
    lineCnt += 1
    theResult = findWords(line)
    if theResult != -1:
        output = 'Line {}: {}'.format(lineCnt, line)
        print(output)

