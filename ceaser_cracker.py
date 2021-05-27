##
# ceaser_cracker.py
# program to crack a cesarian shift


def crack(string):
    eng = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]

    for offset in range(0, 26):
        l = list(string.lower())
        lc = []

        for character in l:
            if character in eng:
                char_id = ((-offset + 26 + eng.index(character) + 26) % 26)
                lc.append(eng[char_id])
            else:
                lc.append(character)
        string = ''.join(lc)
        print(f'{offset}: {string}')

if __name__ == '__main__':
    crack(input('What is the phrase you would like to crack:\n'))