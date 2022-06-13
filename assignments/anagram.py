import math

print("THIS PROGRAM TESTS IF A GIVEN NUMBER IS AN ANAGRAM")
user_response = int(input("Enter a number: "))


def is_anagram(number):
    length_of_number = len(str(number)) * (-1)
    power_of_number_in_str = str(int(math.pow(number, 2)))
    get_value_of_power = power_of_number_in_str[length_of_number:]
    if str(number) == get_value_of_power:
        return True, str(number) + " is an Anagram"
    else:
        return False, str(number) + " is not an Anagram"


if __name__ == "__main__":
    print(is_anagram(user_response))
