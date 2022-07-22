# print(isinstance(4, int | str | float)) # EAFP
# print(type(4) == int or type(4) == str or type(4) == int) # Easier to ask forgiveness than permission


lst = [1, 2, 3, 4]


def simulate():
    try:
        # d = 4 + "I "
        # s = lst[9]
        # print(raise_exception(9))
        print(square([9]))
        print("I did well")
    except IndexError as e:
        print(f"Index out of bounds: {e}")
    except (TypeError, ValueError) as e:
        print(f"Error of no type: {e}")
    else:
        print("I am a happy dude")
    finally:
        print("I am from finally")


# print(simulate())


# def raise_exception(s: int | float) -> int | float:
def square(s: int | float) -> int | float:
    if isinstance(s, int | float):
        return s * s
    # raise ValueError("This is just whining you with exception")
    raise ValueError("I can only square an integer or float")


# print(simulate())

import json
import pathlib

file_path = pathlib.Path("./json/twitter_users.json").resolve()
# file_path.mkdir(parents=True, exist_ok=True)
twitter_users = []
username = input("Enter username: ")
is_married = input("Enter married: ")
age = input("Enter age: ")
data = dict(name=username, is_married=is_married, age=age)
# twitter_users = [{"name": "John Doe", "is_married": True, "age": 29},
#                  {"name": "Omosetan Omorele", "is_married": False, "age": 18}]
twitter_users2 = {"name": "bles you", "is_married": True, "age": 41}
twitter_users3 = {"name": "favour", "is_married": False, "age": 24}

with file_path.open(mode="w", encoding="utf-8") as file:
    twitter_users = twitter_users.copy()
    # twitter_users.append(twitter_users2)
    # twitter_users.append(twitter_users3)
    twitter_users.append(data)

    # json.dump(twitter_users2, file, indent=4)
    json.dump(twitter_users, file, indent=4)

print(file_path)
