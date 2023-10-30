#Tess Jaworski
def print_menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')

def encode(user_pass):
    new_list = []
    for x in user_pass:
        new = int(x) + 3
        new_list.append(new)
    string = ''.join((map(str, new_list)))
    return string


if __name__ == "__main__":
    while True:
        print_menu()
        user_input = input('Please enter an option:')
        if user_input == '1':
            user_pass = input('Please enter your password to encode:')
            encode(user_pass)

