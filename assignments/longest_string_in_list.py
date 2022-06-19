def longest_string(string_of_letters) -> list:
    string_of_letters.sort(key=len, reverse=True)
    return string_of_letters[0]


print(longest_string(["I", "love", "You", "view", "greta"]))
