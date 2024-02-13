def is_palindrome(input_str):

    return input_str == input_str[::-1]

user_input = input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome!')
else:
    print(f'"{user_input}" is not a palindrome.')

