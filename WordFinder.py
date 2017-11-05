def findWord(iLine):  # Function to find a word within a string
    """Return first word in sentence matching a word in the searchWords tuple"""

    # Define the words to search for the tuple searchWords
    searchWords = ("c++", "basic", "java", "python")

    result = None  # Pre-set result to None in case loop falls through
    try:
        iLine = iLine.lower()  # Convert string to lower case for searching

        # Loop through words in seachWords and try to find in string s
        for searchWord in searchWords:
            position = iLine.find(searchWord)  # Get postion of word in iLine
            if position != -1:
                result = searchWord  # Set result to value of found searchWord
                break

        # None will be returned if no search words found in string iLine
        return result

    except:
        # Fall through on any error
        return None
