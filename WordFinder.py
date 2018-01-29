# Functions for SearchText.py

def find_word(i_line):  # Function to find a word within a string
    """Return first word in a sentence matching a word in the search_words tuple"""

    # Define the words to search for the tuple search_words
    search_words = ("c++", "basic", "java", "python")

    result = None  # Pre-set result to None in case loop falls through
    try:
        i_line = i_line.lower()  # Convert string to lower case for searching

        # Loop through words in search_words and try to find in string s
        for search_word in search_words:
            position = i_line.find(search_word)  # Get position of word in i_line

            if position != -1:
                result = search_word  # Set result to value of found search_word
                break

        # None will be returned if no search words found in string i_line

        return result

    except:
        # Fall through on any error
        return None


def find_words(i_line: object) -> object:  # Function to find words within a string
    """Return words in a sentence matching a word in the search_words tuple"""

    # Define the words to search for the tuple search_words
    search_words = ("c++", "basic", "java", "python")
    found_words = []

    i_line = i_line.lower()  # Convert string to lower case for searching

    # Loop through words in search_words and try to find in string s
    for search_word in search_words:
        position = i_line.find(search_word)  # Get position of word in i_line

        if position != -1:
            found_words.append([search_word]) # Set result to value of found search_word
            # break

    return found_words
