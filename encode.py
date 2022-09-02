#! /usr/bin/env python3
# encode.py
# By MR-Spagetty
# project started 20/02/2020

import os
from typing import Protocol

# Defining functions and classes


class CodingMethod(Protocol):
    needs_data = False

    def data_valid(data) -> bool:
        return True

    def crack(string: str) -> str:
        return 'This method is incompatible with cracking'

    def enc(string: str) -> str:
        pass

    def dec(string: str) -> str:
        pass


class RailFence(CodingMethod):
    needs_data = True
    data_prompt = 'How many rails would you like to encode/decode with: '


class Tap(CodingMethod):
    matrix = {
        1: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'},
        2: {1: 'f', 2: 'g', 3: 'h', 4: 'ij', 5: 'k'},
        3: {1: 'l', 2: 'm', 3: 'n', 4: 'o', 5: 'p'},
        4: {1: 'q', 2: 'r', 3: 's', 4: 't', 5: 'u'},
        5: {1: 'v', 2: 'w', 3: 'x', 4: 'y', 5: 'z'}
    }

    def enc(string):
        lc = []
        for char in string:
            char_row_colum = []
            for row, row_value in Tap.matrix.items():
                for colum, colum_value in row_value.items():
                    if char in colum_value:
                        char_row_colum.append(str(row))
                        char_row_colum.append(str(colum))
            lc.append('-'.join(char_row_colum))
        return ' '.join(lc)

    def dec(string):
        lc = []
        string_list = string.split()
        for char_id in string_list:
            char = Tap.matrix[int(char_id[0])][int(char_id[1])]
            if char == 'ij':
                lc.append('_i/j_')
            else:
                lc.append(char)
        return ''.join(lc)


class BaseX(CodingMethod):
    needs_data = True
    data_prompt = ('What is the base you would like to '
                   'encode/decode in (eg 16 for hex or '
                   '2 for binary) must be 1 < base < 37: ')

    def data_valid(data):
        valid = True
        try:
            data_int = int(data)
        except ValueError:
            valid = False
        finally:
            if valid:
                valid = data_int in range(2, 37)
        return valid

    lib = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    ]

    def crack(string):

        highest_val = 0
        for char in string:
            if char in BaseX.lib:
                current_val = BaseX.lib.index(char)
            highest_val = max(highest_val, current_val)
        minimum_base = highest_val + 1
        for base in range(minimum_base, 37):
            string_list = string.split()
            lc = [chr(int(character, base)) for character in string_list]
            print(f'{base}: {"".join(lc)}')

    def get_base():
        not_valid = True
        while not_valid:
            not_valid = False
            base = 0
            try:
                base = int(input(
                                'What is the base you would like to '
                                'encode/decode in (eg 16 for hex or '
                                '2 for binary) must be 1 < base < 37: '
                                ))
            finally:
                if base < 2 or base > 37:
                    print('invalid input\n'
                          'valid inputs are intigers 1 < base < 37')
                    not_valid = True
        return base

    def enc(text):
        if term:
            base = BaseX.get_base()
        else:
            global extra_data
            base = int(extra_data)
        string_list = list(text)
        lc = []
        for char in string_list:
            char_num = ord(char)
            num = []
            while char_num:
                char_num, r = divmod(char_num, base)
                if r > 9:
                    num.append(BaseX.lib[r])
                else:
                    num.append(str(r))
            lc.append(''.join(reversed(num)))
        return ' '.join(lc)

    def dec(string):
        if term:
            base = BaseX.get_base()
        else:
            global extra_data
            base = int(extra_data)
        string_list = string.split()
        lc = [chr(int(character, base)) for character in string_list]
        return ''.join(lc)


class Phonetic(CodingMethod):
    phonetic_dict = {
            'a': 'alfa',
            'b': 'bravo',
            'c': 'charlie',
            'd': 'delta',
            'e': 'echo',
            'f': 'foxtrot',
            'g': 'golf',
            'h': 'hotel',
            'i': 'india',
            'j': 'juliett',
            'k': 'kilo',
            'l': 'lima',
            'm': 'mike',
            'n': 'november',
            'o': 'oscar',
            'p': 'papa',
            'r': 'romeo',
            't': 'tango',
            'v': 'victor',
            'x': 'x-ray',
            'z': 'zulu',
            ' ': 'space'
            }

    def enc(phrase):
        phrase = phrase
        phonetic_phrase = []
        for char in phrase:
            if char in Phonetic.phonetic_dict:
                phonetic_phrase.append(Phonetic.phonetic_dict[char])
            else:
                phonetic_phrase.append(char)
        return " ".join(phonetic_phrase)

    def dec(phonetic_phrase):
        phonetic_phrase_list = phonetic_phrase.split()
        phrase = []
        for phrase_letter in phonetic_phrase_list:
            if phrase_letter in Phonetic.phonetic_dict.values():
                for char, phonetic_letter in Phonetic.phonetic_dict.items():
                    if phrase_letter == phonetic_letter:
                        phrase.append(char)
                        break
            else:
                phrase.append(phrase_letter)
        return "".join(phrase)


class HexiDecimal(CodingMethod):
    def enc(string):
        string_list = list(string)
        lc = [hex(ord(char)).strip('0x') for char in string_list]
        string = ' '.join(lc)
        return string

    def dec(string):
        string_list = string.split(' ')
        lc = [chr(int(char, 16)) for char in string_list]
        string = ''.join(lc)
        return string


class AsciiID(CodingMethod):
    def dec(string):
        string_list = string.split(' ')
        lc = [chr(int(char)) for char in string_list]
        string = ''.join(lc)
        return string

    def enc(string):
        string_list = list(ascii(string))
        lc = [str(ord(char)) for char in string_list]
        string = ' '.join(lc)
        return string


class Binary(CodingMethod):
    def dec(string):
        lc = []
        coded = True
        string_list = string.split()
        while coded:
            for character in string_list:
                lc.append(chr(int(character, 2)))
            string = ''.join(lc)
            coded = False
        return string

    def enc(string):
        string_list = list(string)
        lc = []
        for character in string_list:
            binary = bin(ord(character))[2:]
            binary = (8-len(binary))*'0'+binary
            lc.append(binary)
        string = ' '.join(lc)
        return string


class Morse(CodingMethod):
    lib = [
            '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
            '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
            '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----',
            '..---', '...--', '....-', '.....', '-....', '--...', '---..',
            '----.', '-----'
    ]

    def dec(string):
        string_list = string.split(" ")
        lc = [General.eng[Morse.lib.index(character)]
              for character in string_list]
        string = ''.join(lc)
        return string

    def enc(string):
        string_list = list(string.lower())
        lc = []
        for character in string_list:
            if character == ' ':
                lc.append('')
            else:
                lc.append(Morse.lib[General.eng.index(character)] + ' ')
        string = ''.join(lc)
        return string


class Ceaser(CodingMethod):
    needs_data = True
    data_prompt = 'What is the offset: '

    def data_valid(data):
        valid = True
        try:
            int(data)
        except ValueError:
            valid = FALSE
        return valid

    ceaser_lib = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z'
    ]

    def crack(string):
        eng = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z'
        ]

        for offset in range(26):
            string_list = list(string.lower())
            lc = []

            for character in string_list:
                if character in eng:
                    char_id = ((-offset + 26 + eng.index(character) + 26) % 26)
                    lc.append(eng[char_id])
                else:
                    lc.append(character)
            string = ''.join(lc)
            print(f'{offset}: {string}')

    def get_offset(enc_dec=""):
        not_valid = True
        offset = 0
        while not_valid:
            not_valid = False
            try:
                if enc_dec == "dec":
                    print('What is the offset the string was codded to:')
                else:
                    print('What is the offset you would like to '
                          'code your string to:')
                offset = int(input())
            finally:
                if offset == 0:
                    print("Error invalid input")
                    print('\nvalid inputs are intigers > or < 0')
                    not_valid = True
        return offset

    def dec(string):
        string_list = list(string.lower())
        lc = []
        global term
        if term:
            offset = Ceaser.get_offset("dec")
        else:
            global extra_data
            offset = int(extra_data)
        for character in string_list:
            if character in Ceaser.ceaser_lib:
                char_id = ((-offset + 26 + General.eng.index(character) + 26)
                           % 26)
                lc.append(Ceaser.ceaser_lib[char_id])
            else:
                lc.append(character)
        string = ''.join(lc)
        return string

    def enc(string):
        string_list = list(string.lower())
        lc = []
        global term
        if term:
            offset = Ceaser.get_offset()
        else:
            global extra_data
            offset = int(extra_data)
        for character in string_list:
            if character in Ceaser.ceaser_lib:
                char_id = ((offset + General.eng.index(character) + 26) % 26)
                lc.append(Ceaser.ceaser_lib[char_id])
            else:
                lc.append(character)
        string = ''.join(lc)
        return string


class BasicKeyed(CodingMethod):
    needs_data = True
    data_prompt = 'What is the passphrase: '

    def data_valid(data):
        return True

    def get_keyed(passphrase):
        alphabet_list = []
        for char in passphrase:
            if char not in alphabet_list and char in General.eng:
                alphabet_list.append(char)
        for char in General.eng:
            if char not in alphabet_list:
                alphabet_list.append(char)
        return alphabet_list

    def enc(string):
        string_list = list(string)
        codded_list = []
        global term
        if term:
            passphrase = input('What is the passphrase: ').strip()
        else:
            global extra_data
            passphrase = extra_data
        keyed_alpha = BasicKeyed.get_keyed(passphrase)

        for char in string_list:
            if char in General.eng:
                codded_list.append(keyed_alpha[General.eng.index(char)])
            else:
                codded_list.append(char)
        string = ''.join(codded_list)

        return string

    def dec(string):
        string_list = list(string)
        codded_list = []
        global term
        if term:
            passphrase = input('What is the passphrase: ').strip()
        else:
            global extra_data
            passphrase = extra_data
        keyed_alpha = BasicKeyed.get_keyed(passphrase)

        for char in string_list:
            if char in General.eng:
                codded_list.append(General.eng[keyed_alpha.index(char)])
            else:
                codded_list.append(char)
        string = ''.join(codded_list)

        return string


class Vigenere(CodingMethod):
    needs_data = True
    data_prompt = 'What is the passphrase: '

    vigenere_lib = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z'
    ]

    def data_valid(data):
        return str.isalpha(data)

    def enc(string):
        string_list = list(string.lower())
        codded_list = []
        poly_matrix = []
        poly_matrix_ids = []
        global term
        if term:
            passphrase = input(Vigenere.data_prompt).strip()
        else:
            global extra_data
            passphrase = extra_data

        ids = range(len(passphrase))
        current_id = 0
        for char in string_list:
            if char in Vigenere.vigenere_lib:
                poly_matrix_ids.append(current_id)
                current_id += 1
                if current_id >= len(passphrase):
                    current_id = 0
            else:
                poly_matrix_ids.append(-1)

            poly_matrix.append(char)
        for char, id in zip(poly_matrix, poly_matrix_ids):
            if id == -1:
                codded_list.append(char)
            else:
                offset = Vigenere.vigenere_lib.index(passphrase[id])
                char_pos = Vigenere.vigenere_lib.index(char)
                new_char = Vigenere.vigenere_lib[
                    (char_pos + offset) % 26]
                codded_list.append(new_char)
        return ''.join(codded_list)

    def dec(string):
        string_list = list(string.lower())
        codded_list = []
        poly_matrix = []
        poly_matrix_ids = []
        global term
        if term:
            passphrase = input(Vigenere.data_prompt).strip()
        else:
            global extra_data
            passphrase = extra_data

        ids = range(len(passphrase))
        current_id = 0
        for char in string_list:
            if char in Vigenere.vigenere_lib:
                poly_matrix_ids.append(current_id)
                current_id += 1
                if current_id >= len(passphrase):
                    current_id = 0
            else:
                poly_matrix_ids.append(-1)

            poly_matrix.append(char)
        for char, id in zip(poly_matrix, poly_matrix_ids):
            if id == -1:
                codded_list.append(char)
            else:
                offset = Vigenere.vigenere_lib.index(passphrase[id])
                char_pos = Vigenere.vigenere_lib.index(char)
                new_char = Vigenere.vigenere_lib[
                    (char_pos + 26 - offset) % 26]
                codded_list.append(new_char)
        return ''.join(codded_list)


class Gronsfeld(CodingMethod):
    needs_data = True
    data_prompt = 'What is the passnumber: '

    gronsfeld_lib = [
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z'
    ]

    def data_valid(data):
        return str.isnumeric(data)

    def enc(string):
        string_list = list(string.lower())
        codded_list = []
        poly_matrix = []
        poly_matrix_ids = []
        global term
        if term:
            passphrase = list(input(Gronsfeld.data_prompt).strip())
        else:
            global extra_data
            passphrase = extra_data

        ids = range(len(passphrase))
        current_id = 0
        for char in string_list:
            if char in Gronsfeld.gronsfeld_lib:
                poly_matrix_ids.append(current_id)
                current_id += 1
                if current_id >= len(passphrase):
                    current_id = 0
            else:
                poly_matrix_ids.append(-1)

            poly_matrix.append(char)
        for char, id in zip(poly_matrix, poly_matrix_ids):
            if id == -1:
                codded_list.append(char)
            else:
                offset = int(passphrase[id])
                char_pos = Gronsfeld.gronsfeld_lib.index(char)
                new_char = Gronsfeld.gronsfeld_lib[
                    (char_pos + offset) % 26]
                codded_list.append(new_char)
        return ''.join(codded_list)

    def dec(string):
        string_list = list(string.lower())
        codded_list = []
        poly_matrix = []
        poly_matrix_ids = []
        global term
        if term:
            passphrase = list(input(Gronsfeld.data_prompt).strip())
        else:
            global extra_data
            passphrase = extra_data

        ids = range(len(passphrase))
        current_id = 0
        for char in string_list:
            if char in Gronsfeld.gronsfeld_lib:
                poly_matrix_ids.append(current_id)
                current_id += 1
                if current_id >= len(passphrase):
                    current_id = 0
            else:
                poly_matrix_ids.append(-1)

            poly_matrix.append(char)
        for char, id in zip(poly_matrix, poly_matrix_ids):
            if id == -1:
                codded_list.append(char)
            else:
                offset = int(passphrase[id])
                char_pos = Gronsfeld.gronsfeld_lib.index(char)
                new_char = Gronsfeld.gronsfeld_lib[
                    (char_pos + 26 - offset) % 26]
                codded_list.append(new_char)
        return ''.join(codded_list)


class PlMi(CodingMethod):
    needs_data = True
    data_prompt = 'What is the password and sequenced seperated by ",": '

    def data_valid(data):
        return str.isascii(data) and len(data) > 2 and data.count(',') == 1

    def enc(string):
        global term
        if term:
            phrase, sequence = input(PlMi.data_prompt).strip().split(',')
        else:
            global extra_data
            phrase, sequence = extra_data.strip().split(',')
        point = 0
        phrase_letter = 0
        encrypted_message = []
        for char in string:
            match sequence[point]:
                case "+":
                    encrypted_message.append(chr(
                        (ord(char) + ord(phrase[phrase_letter])) % 257))

                case "-":
                    encrypted_message.append(chr(
                        (ord(char) - ord(phrase[phrase_letter]) + 256) % 257))
            point = (point + 1) % len(sequence)
            phrase_letter = (phrase_letter + 1) % len(phrase)
        return "".join(encrypted_message)

    def dec(string):
        global term
        if term:
            phrase, sequence = input(PlMi.data_prompt).strip().split(',')
        else:
            global extra_data
            phrase, sequence = extra_data.strip().split(',')
        point = 0
        phrase_letter = 0
        encrypted_message = []
        for char in string:
            match sequence[point]:
                case "-":
                    encrypted_message.append(chr(
                        (ord(char) + ord(phrase[phrase_letter]) + 1) % 257))

                case "+":
                    encrypted_message.append(chr(
                        (ord(char) - ord(phrase[phrase_letter]) + 257) % 257))
            point = (point + 1) % len(sequence)
            phrase_letter = (phrase_letter + 1) % len(phrase)
        return "".join(encrypted_message)


class General:
    cyphs = {
        'binary': Binary, 'morse': Morse, 'ceaser': Ceaser,
        'hex': HexiDecimal, 'ascii': AsciiID, 'phonetic': Phonetic,
        'base-x': BaseX, 'tap': Tap, 'basic-keyed': BasicKeyed,
        'vigenere': Vigenere, 'gronsfeld': Gronsfeld, 'plus-minus': PlMi
        # add more here all strings must be full lower case
    }
    list_of_methods = '\n'.join([
        'Binary', 'Morse', 'Ceaser', 'Hex', 'Ascii', 'Phonetic', 'Base-X',
        'Tap', 'Basic-Keyed', 'Vigenere', 'Gronsfeld', 'Plus-Minus'
        # add more here must use "-" instead of " "
    ])
    eng = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    ]


def term_start():
    """Function to run the program in terminal mode"""
    global term
    term = True

    cont = "y"
    while cont == "y":
        cont = ''
        # finding what the user wants to encode/decode and how
        space_sererated = 'morse, hex, ascii ids, binary or base x'
        enc_dec = input('would you like to encode, decode or '
                        'crack your string? ').lower().strip()
        code_type = input(f'how would you like to {enc_dec}'
                          ' your string? ').lower().strip()
        string = input(f'What is the string you would like to {enc_dec}? '
                       f'(if you are decoding {space_sererated} '
                       'please separate letters with spaces) ')
        if enc_dec == "decode":
            if code_type in General.cyphs:
                print(General.cyphs[code_type].dec(string))
            else:
                print("ERROR CODE TYPE NOT FOUND")
        elif enc_dec == "encode":
            if code_type in General.cyphs:
                print(General.cyphs[code_type].enc(string))
            else:
                print("ERROR CODE TYPE NOT FOUND")
        elif enc_dec == 'crack':
            if code_type in General.cyphs:
                General.cyphs[code_type].crack(string)
            else:
                print('ERROR CODE TYPE NOT FOUND')
        while cont not in ['y', 'n']:
            cont = input('Would you like to continue (y|n) ')
    if cont == 'n':
        print('have a nice day')
        exit()


GUI_disabled = False
try:
    from tkinter import *
except ModuleNotFoundError:
    print('tkinter module not found GUI mode has been disabled\n'
          'automatically starting in terminal mode')
    GUI_disabled = True
    if __name__ == '__main__':
        term_start()

if not GUI_disabled:
    def gui_setup():
        """sets up the program gui
        """
        global gui
        gui = Tk()
        gui.title('Menu')

        global in_out_gui
        in_out_gui = Toplevel()
        in_out_gui.title('Input/Output')

        in_out_gui.protocol("WM_DELETE_WINDOW", lambda: False)

        input_label = Label(
                            in_out_gui, text='Input',
                            font=('Comic Sans MS', 12))
        input_label.pack(pady=5)
        string_textvar = StringVar(in_out_gui)
        input_entry = Entry(in_out_gui, textvariable=string_textvar, width=50)
        input_entry.pack()
        output_label = Label(
                            in_out_gui, text='Output',
                            font=('Comic Sans MS', 12))
        output_label.pack(pady=5)
        output_textvar = StringVar(in_out_gui)
        output_entry = Entry(in_out_gui, textvariable=output_textvar, width=50)
        output_entry.pack()

        global is_on
        is_on = True

        def enc_dec_switch():
            global is_on

            if is_on:
                code_entry_label.config(
                        text='How would you like to Encode your string:'
                        )
                is_on = False

            else:
                code_entry_label.config(
                        text='How would you like to Decode your string:'
                        )
                is_on = True

        def update(called_by, y, action):
            global str_code_type
            str_code_type = StringVar.get(code_type).lower()
            global extra_data
            extra_data = StringVar.get(data_stringvar)
            # print(f'"{called_by}" "{y}" "{action}"')
            if str_code_type in General.cyphs:
                if General.cyphs[str_code_type].needs_data:
                    prompt = General.cyphs[str_code_type].data_prompt
                    data_prompt_label.config(textvariable=StringVar(gui,
                                                                    prompt))
                    data_entry.config(state=NORMAL)
                    if General.cyphs[str_code_type].data_valid(extra_data):
                        go_button.config(state=ACTIVE)
                    else:
                        go_button.config(state=DISABLED)
                else:
                    data_prompt_label.config(textvariable=no_data)
                    data_stringvar.set('')
                    data_entry.config(state=DISABLED)
                    go_button.config(state=ACTIVE)

            else:
                go_button.config(state=DISABLED)
                data_prompt_label.config(textvariable=no_data)
                data_stringvar.set('')
                data_entry.config(state=DISABLED)

        def go():
            global extra_data
            global str_code_type
            global is_on
            if is_on:
                mode = 'Decode'
                output_textvar.set(
                    General.cyphs[str_code_type].dec(StringVar.get(
                        string_textvar))
                    )
            else:
                mode = 'Encode'
                output_textvar.set(
                    General.cyphs[str_code_type].enc(StringVar.get(
                        string_textvar))
                    )
            print(f'''
Mode: {mode}
Code method: {str_code_type}
Extra data: {extra_data}''')

        # Button to change mode between encode and decode
        on_enc_dec_button = Button(gui,
                                   textvariable=StringVar(gui,
                                                          value='Change mode'),
                                   command=enc_dec_switch,
                                   font=("Comic Sans MS", 12))
        on_enc_dec_button.pack(pady=10)

        # Label and text entry field for the code type
        code_entry_label = Label(
            gui,
            text='How would you like to Decode your string:',
            font=("Comic Sans MS", 12))
        code_entry_label.pack(pady=10)
        code_type = StringVar(gui, 'none')
        code_type.trace_add('write', update)
        code_menu_button = Menubutton(gui, textvariable=code_type,
                                      font=('Comic Sans MS', 10))
        code_menu_button.pack(pady=5)
        code_menu = Menu(code_menu_button, font=('Comic Sans MS', 10))
        code_menu_button['menu'] = code_menu
        for type in General.list_of_methods.split():
            code_menu.add_radiobutton(label=type.lower(), variable=code_type)

        # Label and entry box for inputing of any extra data required by the
        # specific method eg the offset of the ceaser cypher
        no_data = StringVar(gui, 'no extra data needed')
        data_prompt_label = Label(gui,
                                  textvariable=no_data,
                                  font=('Comic Sans MS', 12))
        data_prompt_label.pack(pady=10)
        data_stringvar = StringVar(gui)
        data_stringvar.trace_add('write', update)
        data_entry = Entry(gui, textvariable=data_stringvar, state=DISABLED)
        data_entry.pack(pady=5)

        # The infamos GO button
        go_button = Button(gui, text='GO', state=DISABLED, command=go)
        go_button.pack(pady=20)

    def gui_start():
        """starts up the gui
        """
        global term
        term = False
        gui_setup()
        gui.mainloop()

    def main():
        """Main program function"""
        # asking the user weather or no they want to run the program
        not_valid = True
        while not_valid:
            not_valid = False
            print('Launch Program (y|n)')
            launch = input('>> ').strip().lower()
            if launch not in ['y', 'n']:
                print('ERROR input invalid valid inputs are "y" and "n"')
                not_valid = True
            elif launch == 'n':
                print('Have a nice day')
                exit()
        # asking the user weather they would like to run the program in
        # terminal or GUI mode
        not_valid = True
        while not_valid:
            print('launch in terminal or GUI mode? ')
            mode = input('>> ').strip().lower()
            if mode in ['terminal', 'gui']:
                not_valid = False
            if mode == 'terminal':
                os.system('cls' if os.name == 'nt' else 'clear')
                term_start()
            elif mode == 'gui':
                os.system('cls' if os.name == 'nt' else 'clear')
                gui_start()

    if __name__ == '__main__':
        main()
