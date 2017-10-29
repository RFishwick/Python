# Find String Program

# Define the words to search for
WordTup = ('python', 'java')
print(WordTup.index('C++'))

# Define Functions
def findPython(s):
    try:
        result = s.find("Python")
        print(WordTup)
        if result != -1:
            result = s.strip()
            return result
        else:            
            return result
    except:
        return ""

# Begin Main Program

# Open Input file for reading
fileI = open('theMessage.txt', 'r')
myText = list(fileI)
fileI.close # Close input file

# Print lines that contain the selected word
cnt = 0
for line in myText:
    cnt += 1
    if findPython(line) != -1:
        output = 'Line {}: {}'.format(cnt, findPython(line))
        print(output)



