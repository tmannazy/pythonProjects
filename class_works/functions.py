import string

abc = string.ascii_lowercase
#
# def celsius_to_fahrenheit(celsius: float) -> float:
#     """
# converts celsius to fahrenheit
# :return  fahrenheit float
# """
#     return celsius * 1.8 + 32
#
#
# fahrenheit: float = celsius_to_fahrenheit(100)
# print(fahrenheit, "F")
# help(celsius_to_fahrenheit)

get_user_response = input("Enter the word to decode: ")
while not get_user_response.isalpha():
    print("Kindly enter correct word")
    get_user_response = input("Enter the word to decode: ")

user_key = input("Enter the key to decode your word: ")
while not user_key.isdigit():
    print("Kindly enter correct key")
    user_key = input("Enter the key to decode your word: ")

key_from = int(user_key)


def encode_word_and_decode_word(response: string, key: int):
    if 0 < key <= 26:
        rotated_word = response.lower().translate(str.maketrans(abc, abc[key:] + abc[:key]))
        decoded_word = rotated_word.translate(str.maketrans(abc[key:] + abc[:key], abc))
        print("Your encoded word is:", rotated_word)
        print("The decoded word is:", decoded_word)
    else:
        print("The key must be between 1 and 26")


encode_word_and_decode_word(get_user_response, key_from)
