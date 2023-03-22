"""
Author: Ciara O'Grady
Version: Version 1
Description: GitHub Lab
Date: March 7, 2023
"""


def encode(password):
    new_password = ""
    for char in password:
        new_char = (int(char) + 3) % 10
        new_password += str(new_char)
    return new_password


def decode(password):
    pass


def display_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


def main():
    display_menu()
    keep_playing = True
    password = ""
    choice = int(input("Please enter an option: "))
    while keep_playing:

        if choice == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!\n")
            display_menu()
            choice = int(input("Please enter an option: "))
        elif choice == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}.\n")
            display_menu()
            choice = int(input("Please enter an option: "))
        elif choice == 3:
            keep_playing = False
        else:
            print("Invalid input.\n")
            display_menu()
            choice = int(input("Please enter an option: "))


if __name__ == "__main__":
    main()