def findWord(i_line):  # Function to find a word within a string
    """Return first word in sentence matching a word in the searchWords tuple"""

    # Define the words to search for the tuple searchWords
    searchWords = ("c++", "basic", "java", "python")

    result = None  # Pre-set result to None in case loop falls through
    try:
        i_line = i_line.lower()  # Convert string to lower case for searching

        # Loop through words in seachWords and try to find in string s
        for searchWord in searchWords:
            position = i_line.find(searchWord)  # Get postion of word in i_line

            if position != -1:
                result = searchWord  # Set result to value of found searchWord
                break

        # None will be returned if no search words found in string i_line

        return result

    except:
        # Fall through on any error
        return None
