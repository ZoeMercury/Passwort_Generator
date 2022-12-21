import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
random_order = input("Do you want the characters in your password in a randomized order? Yes or no?\n").lower()

rand_letters = random.choices(letters, weights=None, cum_weights=None, k=nr_letters)
rand_symbols = random.choices(symbols, weights=None, cum_weights=None, k=nr_symbols)
rand_numbers = random.choices(numbers, weights=None, cum_weights=None, k=nr_numbers)

if random_order == "no":
    password_letters = ""
    for string_letters in rand_letters:
        password_letters += string_letters
    password_symbols = ""
    for string_symbols in rand_symbols:
        password_symbols += string_symbols
    password_numbers = ""
    for string_numbers in rand_numbers:
        password_numbers += string_numbers  # advanced: making loop out of all
    print(f"Your password will be: {password_letters}{password_symbols}{password_numbers}")

elif random_order == "yes":
    rand_letters.extend(rand_symbols)
    rand_letters.extend(rand_numbers)
    password = random.sample(rand_letters, k=len(rand_letters))
    password_letters = ""
    for string_letters in password:
        password_letters += string_letters
    print(f"Your password will be: {password_letters}")
