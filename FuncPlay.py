# Define Functions
def findPython(s):
    try:
        if s[s.index("Python"):s.index("Python")+6] == "Python":
            result = s.strip()
            return result
    except:
        return ""

# Begin Main Program
# Open Input file for reading
fileI = open('theMessage.txt', 'r')
myText = list(fileI)
fileI.close # Close input file

cnt = 0
for line in myText:
    cnt += 1
    if findPython(line) != "":
        output = 'Line {}: {}'.format(cnt, findPython(line))
        print(output)



