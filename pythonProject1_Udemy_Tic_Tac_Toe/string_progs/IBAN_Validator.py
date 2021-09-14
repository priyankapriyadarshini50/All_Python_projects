iban = input('Enter a valid IBAN, please: ')
iban = iban.replace(' ', '')
if not iban.isalnum():
    print("You have entered invalid character!")
elif len(iban) < 15:
    print('The IBAN is too short')
elif len(iban) > 31:
    print("The IBAN is too long ")
else:
    new_iban = iban[4:] + iban[:4]
    new_iban_upper = new_iban.upper()
    update_iban = ''
    for letter in new_iban_upper:
        if letter.isdigit():
            update_iban += letter
        else:
            double_digit = str(10 + ord(letter) - ord('A'))
            update_iban += double_digit
    print(update_iban)

    if int(update_iban) % 97 == 1:
        print("{} is a valid IBAN".format(iban))
    else:
        print('{} is an invalid IBAN'.format(iban))


