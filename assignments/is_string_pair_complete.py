open_char_lst = ['[', '{', '(', '<']
close_char_lst = [']', '}', ')', '>']

#
# def is_char_complete(str_to_check):
#     lst = []
#     for x in str_to_check:
#         if x in open_char_lst:
#             lst.append(x)
#         elif x in close_char_lst:
#             get_index = close_char_lst.index(x)
#             if len(lst) > 0:
#                 if open_char_lst[get_index] == lst[len(lst) - 1]:
#                     lst.pop()
#     if len(lst) == 0:
#         return True
#     else:
#         return False
#
#
# print(is_char_complete("[{()}]"))


def bracket_pair(brackets: str) -> bool:
    if len(brackets) < 2 or len(brackets) % 2 != 0:
        return False
    stack = []

    for bracket in brackets:
        if bracket in "{([":
            stack.append(bracket)
        elif bracket in "])}":
            peeked = stack[- 1]
            if bracket == ")" and peeked == "(":
                stack.pop()
            elif bracket == "}" and peeked == "{":
                stack.pop()
            elif bracket == "]" and peeked == "[":
                stack.pop()
            return True
        else:
            return False
    else:
        return False



print(bracket_pair("{}{(([]))}"))