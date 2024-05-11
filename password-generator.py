# Author: Danny Nguyen
# Password Generator
import string
import secrets
from os.path import exists

# List of Letters uppercase and lowercase
uppercase_letters = list(string.ascii_uppercase)
lowercase_letters = list(string.ascii_lowercase)

# list of Numbers between 0 to 9
number_list = list(range(0,10))

# Turns numbers into a string
for i in range(len(number_list)):
    number_list[i] = str(number_list[i])

# list of Punctuation
punctuation = list(string.punctuation)

# Generate Password with only letters Function
def password_choice1(length, save_input, filename):
    # create password
    password = ''
    letters = uppercase_letters + lowercase_letters
    for number in range(length):
        parts = secrets.choice(letters)
        password += parts
    print('Here is your password:')
    print(password)

    # saves password
    save_input = save_input.lower()
    if save_input == 'yes':
        with open(filename, "w", encoding='utf-8') as file:
            file.write(password)

# Generate Password with letters and numbers Function
def password_choice2(length, save_input, filename):
    # Create Password
    password = ''
    letters_numbers = uppercase_letters + lowercase_letters + number_list
    for number in range(length):
        parts = secrets.choice(letters_numbers)
        password += parts
    print('Here is your password:')
    print(password)

    # saves password
    save_input = save_input.lower()
    if save_input == 'yes':
        with open(filename, "w", encoding='utf-8') as file:
            file.write(password)

# Generate Password with letters, numbers, and punctuation
def password_choice3(length, save_input, filename):
    # Create Password
    password = ''
    letters_num_punc = uppercase_letters + lowercase_letters + number_list + punctuation
    for number in range(length):
        parts = secrets.choice(letters_num_punc)
        password += parts
    print('Here is your password:')
    print(password)

    # saves password
    save_input = save_input.lower()
    if save_input == 'yes':
        with open(filename, "w", encoding='utf-8') as file:
            file.write(password)

# Divider Function
def divider():
    x ='--------------------------------------------'
    print(x)

# Tie it all up and make it user friendly
print("Welcome to Danny's Password Generator!")
divider()
print('Which of the following choices would you like?')
print('(1) Generate password with letters')
print('(2) Generate password with letters and numbers')
print('(3) Generate password with letters, numbers, and punctuations')
print('(4) Read Saved Password File')
divider()

while True:
    choice = input('CHOICE> ')

    if choice == '1':
        print('What is the length of the password?')
        length = input('Length: ')
        # Make sure length is a number
        if length.isalpha() == True:
            print('This is not a integer!')
        elif length.isnumeric() == True:
            length = int(length)
            print('Do you want to save the password?')
            save_input =(input('Yes/No: '))
            save_input = save_input.lower()
            if save_input == 'yes':
                print('What will be the name of the file the password is saved to?')
                filename = input('Name: ')
                print(f'Password is saved to a file named "{filename}".')
                # Make it so that the user does not need to type in .txt to create a file
                filename = filename + '.txt'
            else:
                print('Password not saved!')
                filename = "no"
            # OUTPUT
            password_choice1(length, save_input, filename)
        divider()

    elif choice == '2':
        print('What is the length of the password?')
        length = input('Length: ')
        # Make sure length is a number
        if length.isalpha() == True:
            print('This is not a integer!')
        elif length.isnumeric() == True:
            length = int(length)
            print('Do you want to save the password?')
            save_input =(input('Yes/No: '))
            save_input = save_input.lower()
            if save_input == 'yes':
                print('What will be the name of the file the password is saved to?')
                filename = input('Name: ')
                print(f'Password is saved to a file named "{filename}".')
                # Make it so that the user does not need to type in .txt to create a file
                filename = filename + '.txt'
            else:
                print('Password not saved!')
                filename = "no"
            # OUTPUT
            password_choice2(length, save_input, filename)
        divider()

    elif choice == '3':
        print('What is the length of the password?')
        length = input('Length: ')
        # Make sure length is a number
        if length.isalpha() == True:
            print('This is not a integer!')
        elif length.isnumeric() == True:
            length = int(length)
            print('Do you want to save the password?')
            save_input =(input('Yes/No: '))
            save_input = save_input.lower()
            if save_input == 'yes':
                print('What will be the name of the file the password is saved to?')
                filename = input('Name: ')
                print(f'Password is saved to a file named "{filename}".')
                # Make it so that the user does not need to type in .txt to create a file
                filename = filename + '.txt'
            else:
                print('Password not saved!')
                filename = "no"
            # OUTPUT
            password_choice3(length, save_input, filename)
        divider()

    elif choice == '4':
        print('What saved password file do you want to read?')
        name_file = input('File Name: ')
        # Make it so that the user does not need to type in .txt to look for a file
        name_file = name_file + '.txt'
        
        # Make sure that file exist
        file_exists = exists(name_file)
        if file_exists != True:
            print("This file does not exists!")
        else:
            with open(name_file, "r", encoding='utf-8') as file:
                line = file.readline()
                print(f'The password for {name_file[:-4]} is:')
                print(line)
        divider()

    else:
        if choice.isnumeric() == True:
            print("This is not a choice.")
            divider()
        elif choice.isalnum() == True:
            print("Thank you for using Danny's Password Generator!")
            print("Goodbye!")
            break
