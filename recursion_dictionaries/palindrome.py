def isPalindrome(s):
    """
    Checks if a string is a palindrome.

    A palindrome is a word, phrase, or sequence that reads the same backward 
    as forward.
    For example, "racecar" and "madam" are palindromes. This function ignores 
    spaces and punctuation marks.

    Args:
      s (str): The string to check.

    Note:
      convert s to string.

    Returns:
      bool: True if s is a palindrome and False otherwise.

    Raises:
      TypeError: If s is None.
    """

    # if isinstance(s, None):
    #     raise TypeError("s must not be None")

    # convert s to string in order to convert to lowercase
    text = str(s).lower()

    # remove spaces and punctuation marks
    text = "".join(c for c in text if c.isalnum())
    # print(f'input : {text}')

    # compare s with its reversed version
    return text == text[::-1]
