# Search for Words in a Text File

import WordFinder

# Begin Main Program

file_i = open('theMessage.txt', 'r')  # Open Input file for reading
my_text = list(file_i)  # Read file into string myText
file_i.close()  # Close input file


# Print lines that contain the selected word
lineCnt = 0
for line in my_text:
    lineCnt += 1
    the_result = WordFinder.find_word(line)
    if the_result is not None:  # Word Found
        output = "'{}' found on line {}:\n{}\n".format(the_result.title(), lineCnt, line.strip())
        print(output)
