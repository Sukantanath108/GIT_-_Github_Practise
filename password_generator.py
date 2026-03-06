# an interface
# password must have a range( minimum word limit )
# should contain upper,lower,special,numbers,symbols and other alphanumeric
# create all types of combination possible
# get all available characters ( a-z , A-Z , 0-9 , !@#$% )
# randomly select characters ( must have atleast one of the desired characters )


import random
import string # gives access to every desired chars

def get_length():
    while True:
        user_input = input("Enter character length: ").strip() # strip removes extra whitespace
        if not user_input.isdigit():
            print("Invalid number entered. try again!")
            continue
        length = int(user_input)
        if length<6:
            print("Number must be greater than 6!")
            continue
        return length

def generate():

    length = get_length()
    upper_case = input("Enter uppercase letters (Yes/No): ").lower().strip()
    digits = input("Enter digits (Yes/NO): ").lower().strip()
    special_case = input('Enter special case (Yes/NO) : ').lower().strip()

    lower = string.ascii_lowercase # a-z
    upper = string.ascii_uppercase if upper_case == 'yes' else "" # A-Z
    special = string.punctuation if special_case == 'yes' else ""
    digits_ = string.digits if digits == 'yes' else ""
    all_char = lower + upper + special + digits_
    # the digits/upper/lower == yes means, the user will input only yes no to store the value in all_char. its about whether to include what
    # print(all_char)

    required_char = []
    if upper_case == "yes":
        required_char.append(random.choice(upper)) # randomly picks one character from string
    if digits == "yes":
        required_char.append(random.choice(digits_))
    if special_case == "yes":
        required_char.append(random.choice(special))
    remaining_length = length - len(required_char)
    password = required_char

    for _ in range(remaining_length): # _ works as a unannouned variable
        password.append(random.choice(all_char)) # the password is a list and we need to make it a string later

    random.shuffle(password)
    print(password)
    str_password = "".join(password)
    return str_password

password = generate()
print(password)

# if somwone decides to keep it simple and dont include any uppercase/digits/special characters, it will be only lowercase


