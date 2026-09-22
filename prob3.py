# ===================================================================================================
# AUTHOR: Panopio, Saguil, Fernando
# Activity 7: Input Validation
# ===============================================================================================

accepted_grade = [7, 8, 9, 10, 11, 12]
try:
    grade_level = int(input("Enter grade level: "))
    if grade_level in accepted_grade:
        print("Valid Grade.")
    else:
        print("Invalid Grade.")
except ValueError:
    print("Input Invalid. Please enter a whole number.")