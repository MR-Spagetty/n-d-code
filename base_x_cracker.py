##
# base_x_cracker.py


def crack(string):
    lib = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]
    highest_val = 0
    for char in string:
        if char in lib:
            current_val = lib.index(char)
        if highest_val < current_val:
            highest_val = current_val

    minimum_base = highest_val + 1
    possibilities = []
    for base in range(minimum_base, 37):
        lc = []
        l = string.split()
        for character in l:
            lc.append(chr(int(character, base)))
        print(f'{base}: {"".join(lc)}')


if __name__ == '__main__':

    crack(input('What is the phrase you would like to crack:\n').lower())