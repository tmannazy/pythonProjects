import string
# file = 'hello'
# b = file[0:2] + file[2:]
# print(b)
#
abc = string.ascii_lowercase
# key = 5
#
# a = file.translate(str.maketrans(abc, abc[key:] + abc[:key]))
# print("rotated 'hello' word in ceasar cipher:", a)
# b = a.translate(str.maketrans(abc[key:] + abc[:key], abc))
# print(b)

user_response = input("Enter the word to decode: ")
while not user_response.isalpha():
    print("Kindly correct word")
    user_response = input("Enter the word to decode: ")
    # get_user_response.upper()

user_key = input("Enter the key to decode your word: ")
while not user_key.isdigit():
    print("Kindly correct key")
    user_key = input("Enter the key to decode your word: ")

key_from = int(user_key)
if 0 < key_from <= 26:
    rotated_word = user_response.translate(str.maketrans(abc, abc[key_from:] + abc[:key_from]))
    word_entered = user_response.translate(str.maketrans(abc[:key_from] + abc[key_from:], abc))
    print("Your rotated word is:", rotated_word)
    print("The word you entered is", word_entered)
else:
    print("The key must be between 1 and 26")


# fn = "Road to Aso Rock"
# # print(fn.partition("k"))
# print(fn.split("o"))


