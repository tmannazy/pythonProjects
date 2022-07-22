# dict_ = []
#
# for x in word:
#     dict_.append(x)
#     for y in dict_:
#         if y == x:
#             s = y.count(x) + y.count(x)
#             dict_.append(s)
# return dict_

#
# def letters_count(word: str) -> dict[str, int]:
#     import string
#     abc = string.ascii_lowercase
#     map_ = {}
#
#     # for char in abc:
#     #     # map_[char] = word.lower().count(char)
#     #     map_ = {char: word.lower().count(char)}
#     # return map_
#     return {char: word.lower().count(char) for char in abc}
#
#
# print(letters_count("Alabama is Nigeria"))


def narcissistic(value):
    # Code away

    b = list(map(int, str(value)))
    length = len(b)
    sum = 0
    for x in b:
        sum += x ** length
    if sum == value:
        return True
    else:
        return False


print(narcissistic(153))
print(narcissistic(7))
