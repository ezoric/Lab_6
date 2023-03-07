def encode(password):
    tracker_num = ""
    for num in password:
        num = int(num)
        if 0 <= num <= 6:
            num += 3
            tracker_num = tracker_num + str(num)
        else:
            num -= 7
            tracker_num = tracker_num + str(num)
    return tracker_num


if __name__ == "__main__":
    run_program = True
    while run_program:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = int(input("Please enter an option: "))
        if option == 3:
            break
        pass_word = input("Please enter your password to encode: ")

        if option == 1:
            encoded_password = encode(pass_word)
            print("Your password has been encoded and stored!")
        elif option == 2:
            pass
        print()



