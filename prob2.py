# ===================================================================================================
# AUTHOR: Panopio, Saguil, Fernando
# Activity 7: Input Validation
# ===================================================================================================

valid_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "i", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
username = input("Please enter your username: ")

is_valid_length = bool(5 <= len(username) <= 10)

all_chars_valid = bool(all(char in valid_characters for char in username))

if is_valid_length and all_chars_valid:
    print("Valid username.")
else:
    print("Invalid username.")