def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

print(is_palindrome("топот"))
print(is_palindrome("python"))
print(is_palindrome("Топот"))  
print(is_palindrome("А роза упала на лапу Азора"))
