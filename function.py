def trial_func(*bob):
    num = bob + bob + bob
    return num
x = trial_func(10,20,30)
print(x)

def sum(*num):
    total = 0
    for i in num:
        total += i
    return total

y = sum(12,45,2)
print(y)

def min_value(*num):
    if num == 0:
        return None
    min_num = num[0]
    for i in num:
        if i <= min_num:
            min_num = i
    return min_num

print(f'The minimum among these  numbers are: {min_value(12,45,2,3,521,21,2)}')

def card_details(username, **detail):
    username = str(username.lower())
    print(username)
    for key, item in detail.items():
        print("  ", key + ":", item)

print(card_details('Sukanta', Birthday = 2002, balance = 100234, sex = "male"))

