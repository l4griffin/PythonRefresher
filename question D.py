def is_uppercase(char):
    return char.isupper()

def is_lowercase(char):
    return char.islower()

def main():
    user_input = input("Enter a single character: ")
    if len(user_input) != 1:
        print("Please enter exactly one character.")
        return

    if is_uppercase(user_input):
        print("The character is uppercase.")
    elif is_lowercase(user_input):
        print("The character is lowercase.")
    else:
        print("The character is neither uppercase nor lowercase.")

if __name__ == "__main__":
    main()