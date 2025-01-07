import re


def validate_credit_card(number):
    number = str(number).replace(" ", "")
    if not re.match(r"^\d{13,19}$", number):
        return False, "Invalid number length"

    if luhn_check(number):
        return True, get_card_brand(number)
    else:
        return False, "Invalid card number"

def luhn_check(number):
    total = 0
    reverse_digits = number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def get_card_brand(number):
    if re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", number):
        return "Visa"
    elif re.match(r"^5[1-5][0-9]{14}$", number):
        return "MasterCard"
    elif re.match(r"^3[47][0-9]{13}$", number):
        return "American Express"
    elif re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$", number):
        return "Discover"
    elif re.match(r"^(?:2131|1800|35\d{3})\d{11}$", number):
        return "JCB"
    elif re.match(r"^8699[0-9]{11}$", number):
        return "Voyager"
    elif re.match(r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$", number):
        return "Diners Club"
    elif re.match(r"^(2014|2149)\d{11}$", number):
        return "EnRoute"
    elif re.match(r"^(606282|3841)[0-9]{10,11,12}$", number):
        return "Hipercard"
    elif re.match(r"^50[0-9]{14,17}$", number):
        return "Aura"
    else:
        return "Unknown"

if __name__ == "__main__":
    card_number = input("Enter the credit card number: ")
    is_valid, result = validate_credit_card(card_number)
    if is_valid:
        print(f"Card is valid and belongs to {result}")
    else:
        print(f"Card is invalid: {result}")