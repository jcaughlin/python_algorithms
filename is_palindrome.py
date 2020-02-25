
def main():
    print(is_palindrome("xanax"))
    print(is_palindrome("Not Palindrome"))
    print(is_palindrome("a"))

    print(palindrome("madam"))


def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])


def palindrome(s):
    return len(s) < 2 or s[0] == s[-1] and palindrome(s[1:-1])


if __name__ == "__main__":
    main()
