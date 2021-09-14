def update_cipher_msg(msg):
    # change all the letters of the text message to uppercase
    msg = msg.upper()
    new_msg = ''
    for char in msg:
        # Update the code point of the character to the next level
        code = ord(char) + 1
        new_char = chr(code)
        # remove the white spaces from the text message
        if char.isspace():  # skip the white spaces if they have in any message
            continue
        # change the code point to the code point of A if the letter is Z and more
        if code > ord('Z'):
            new_char = 'A'
        new_msg = new_msg + new_char
    return new_msg


def decrypt_msg(crypted_msg):
    encrypted_msg = ''
    for char in crypted_msg:
        code = ord(char)-1
        new_char = chr(code)
        if code < ord('A'):
            new_char = 'Z'
        encrypted_msg = encrypted_msg + new_char
    return encrypted_msg


# The message should not contain digits
#  user_msg = ''
# while not user_msg.isalpha():  # it is same as user_msg.isalpha() == False
# user_msg = input("Enter a text message(no digits please): ")
#  if user_msg.isalpha():
#     crypt_msg = update_cipher_msg(user_msg)
#    print(crypt_msg)

if __name__ == '__main__':
    # Create an exception when user tries to enter digits and repeated ask for input
    while True:
        try:
            user_msg = input('Enter a text message: ')
            if user_msg.isalpha():
                crypt_msg = update_cipher_msg(user_msg)
                print(crypt_msg)
                break
            else:
                raise TypeError
        except TypeError:
            print('Please do not enter digits')
        finally:
            print("End of the program")
    print(decrypt_msg(crypt_msg))
