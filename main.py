#Tess Jaworski
def print_menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')

def encode(user_pass):
    new_pass = ""
    for x in user_pass:
        shift = int(x) + 3
        new_shift = shift % 10
        new_pass += str(new_shift)
    return new_pass


def decode(password):
    final_password = ""
    for i in password:
        shifted_num = (int(i) + 7)  # add 7 to handle it wrapping around (same thing as -3 and +10)
        final_num = shifted_num % 10
        final_password += str(final_num)
    return final_password


if __name__ == "__main__":
    while True:
        print_menu()
        user_pass = 0
        user_input = input('Please enter an option: ')
        if user_input == '1':
            user_pass = input('Please enter your password to encode: ')
            final_pass = encode(user_pass)
            print("Your password has been encoded and stored!")
        if user_input == '2':
            print(f"The encoded password is {final_pass}, and the original password is {decode(final_pass)}.")
        if user_input == '3':
            break


