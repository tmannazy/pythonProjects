a = 6
b = 8


# def add(a, b):
#     import pdb;
#     pdb.set_trace()
#     c = a - b
#     return c
#
# add(a, b)

# assert 4 == 3, "4 must be equal to 3"

def tell_me_more_about(a_language: str) -> str:
    languages = ("Java", "Python", "JavaScript")

    assert a_language in languages, f"{a_language} is not found"

    return a_language


print(tell_me_more_about("Kotlin"))
