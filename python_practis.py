import string
import time
import random

def total_length():

    user_input = input("Enter Number : \n").strip()
    if not user_input.isdigit():
        print("Dont enter anything else besides number!")
        return None
    
    user = int(user_input)

    if user < 8:
        print("Too small password. Suggested length to be more than 8")
    else:
        print("Ok!")
    return user

def pp_gen():

    length = total_length()
    print("Total [password] length is",length)

    upper = input("Want upper? (yes/no)").lower().strip()
    digits = input("Want digits? (yes/no)").lower().strip()
    special = input("Want special characters? (yes/no)").lower().strip()

    chars = []
    lower = string.ascii_lowercase
    up = string.ascii_uppercase if upper == "yes" else ""
    dig = string.digits if digits == "yes" else ""
    sp = string.punctuation if special == "yes" else ""
    all_chars = lower + sp + dig + up

    if upper == "yes":
        chars.append(random.choice(up))
    if digits == "yes":
        chars.append(random.choice(dig))
    if special == "yes":
        chars.append(random.choice(sp))
    else:
        pass

    remaining_length = length - len(chars)

    password = chars.copy()

    for i in range(remaining_length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    str_pass = "".join(password)
    print(str_pass)

pas = pp_gen()
