# Implementation of caesar cipher in python
from art import logo


# Get the alphabet
def get_alphabet(case='upper'):
    start = 65  # A
    end = 91    # Z
    if case == 'lower':
        start = 97  # a
        end = 122   # z

    alphabet = []
    for i in range(start, end):
        alphabet.append(chr(i))     # Get char from ascii no and save it in a list

    return alphabet


# Create caesar cipher
def caesar(start_message, cipher_direction, shift_amount):
    # Direction left if decoding
    if cipher_direction == 'de':
        shift_amount *= -1

    alphabet_upper = get_alphabet(case='upper')
    alphabet_lower = get_alphabet(case='lower')

    caesar_list = []
    for idx in range(0, len(start_message)):
        if start_message[idx] in alphabet_upper:
            index = alphabet_upper.index(start_message[idx])
            index += shift_amount
            caesar_list.append(alphabet_upper[index])
        elif start_message[idx] in alphabet_lower:
            index = alphabet_lower.index(start_message[idx])
            index += shift_amount
            caesar_list.append(alphabet_lower[index])
        else:
            caesar_list.append(start_message[idx])

    return ''.join(caesar_list)


''' +++ Start +++ '''
print(logo)

continue_cipher = True
while continue_cipher:
    direction_type = input(f"Type 'A' to encrypt, type 'B' to decrypt:\n").upper()

    direction = 'no'    # Do nothing
    if direction_type == 'A':
        direction = 'en'    # Direction right (encoding)
    elif direction_type == 'B':
        direction = 'de'    # Direction left (decoding)

    if direction != 'no':
        message = input(f"Type your message:\n")
        caesar_message = message
        shift = int(input(f"Type the shift number:\n"))
        if shift != 0:
            shift = shift % 26
            caesar_message = caesar(start_message=message, cipher_direction=direction, shift_amount=shift)
        print(f"\nThe {direction}coded message is '{caesar_message}'\n")

    run_again = input(f"If you want to run again type 'yes'. Otherwise type 'no':\n").lower()
    if run_again == 'no':
        continue_cipher = False
        print("\nCaesar will be back :)")
