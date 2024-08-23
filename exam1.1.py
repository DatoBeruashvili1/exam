# What's the real floor?

def get_real_floor(n):
    if n < 1 :
        return n
    elif n == 0:
        return "Ground"
    elif n < 13:
        return n - 1
    else:
        return n - 2


# Holiday VIII - Duty Free

def duty_free(price, discount, holiday_cost):
    saving_per_bottle = price * (discount / 100)
    return (holiday_cost // saving_per_bottle)

# Last Survivor
def last_survivor(letters, coords):
    letters = list(letters)
    for i in coords:
        letters.pop(i)
    return letters[0]

