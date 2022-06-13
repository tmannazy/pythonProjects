if __name__ == '__main__':
    userResponse = int(input("Enter your score: "))
    match userResponse/10:
        case 10, 9, 8, 7:
            print("A")
        case 6 | 6.9:
            print("B")
        case 5 | 5.9:
            print("C")
        case 4.5 | 4.9:
            print("D")
        case 4 | 4.4:
            print("E")
        case _:
            print("F")



