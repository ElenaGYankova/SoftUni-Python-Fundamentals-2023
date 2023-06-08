def password_validator(secret):
    character_counter = 0

    if len(secret) < 6 or len(secret) > 10:
        print("Password must be between 6 and 10 characters")

    if not secret.isalnum():
        print("Password must consist only of letters and digits")

    for character in secret:
        if character.isdigit():
            character_counter += 1

    if character_counter < 2:
        print("Password must have at least 2 digits")

    if 6 <= len(secret) <= 10 and secret.isalnum() and character_counter >= 2:
        print("Password is valid")


password = input()
password_validator(password)


# def password_validator(password):
#     password_is_valid = True
#     if not 6 <= len(password) <= 10:
#         password_is_valid = False
#         print("Password must be between 6 and 10 characters")
#     for symbol in password:
#         # following line can be replaced with: <if password.isalnum():>
#         if (48 <= ord(symbol) <= 57) or (65 <= ord(symbol) <= 90) or (97 <= ord(symbol) <= 122):
#             continue
#         else:
#             password_is_valid = False
#             print("Password must consist only of letters and digits")
#             break
#     digit_counter = 0
#     for symbol in password:
#         if 48 <= ord(symbol) <= 57: # can be replaced with <if symbol.isdigit():>
#             digit_counter += 1
#     if digit_counter < 2:
#         password_is_valid = False
#         print("Password must have at least 2 digits")
#     if password_is_valid:
#         print("Password is valid")
#
#
# user_password = input()
# password_validator(user_password)


# def length_validation(password):
#     if len(password) < 6 or len(password) > 10:
#         print("Password must be between 6 and 10 characters")
#         return False
#     return True
#
#
# def symbols_validation(password):
#     if not password.isalnum():
#         print("Password must consist only of letters and digits")
#         return False
#     return True
#
#
# def two_digits_validation(password):
#     counter_of_digits = 0
#     for character in password:
#         if character.isdigit():
#             counter_of_digits += 1
#     if counter_of_digits < 2:
#         print("Password must have at least 2 digits")
#         return False
#     return True
#
#
# some_password = input()
# password_is_valid = [length_validation(some_password),
#                      symbols_validation(some_password),
#                      two_digits_validation(some_password)]
#
# if all(password_is_valid):
#     print("Password is valid")
