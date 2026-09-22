# ===============================================================================================
# AUTHORS: Fernando, Panopio, Saguil
# Activity 7: Input Validator
# ==============================================================================================

try:
    age = int(input("Enter your age:"))

    if age >= 12 and age <= 18:
        print("Valid age.")
    else:
        print("Invalid age. Age must be between 12 and 18")

except ValueError:
    print("Invalid input. Enter a whole number.")