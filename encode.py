#! /usr/bin/env python3
# encode.py
# By Eddie
# project started 20/02/2020

import os

# Definging functions and classes


class tap:
    needs_data = False
    matrix = {
        1: {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'},
        2: {1: 'f', 2: 'g', 3: 'h', 4: 'ij', 5: 'k'},
        3: {1: 'l', 2: 'm', 3: 'n', 4: 'o', 5: 'p'},
        4: {1: 'q', 2: 'r', 3: 's', 4: 't', 5: 'u'},
        5: {1: 'v', 2: 'w', 3: 'x', 4: 'y', 5: 'z'}
    }

    def crack(string):
        return 'This method is incompatible with cracking'

    def enc(string):
        lc = []
        for char in string:
            char_row_colum = []
            for row, row_value in tap.matrix.items():
                for colum, colum_value in row_value.items():
                    if char in colum_value:
                        char_row_colum.append(str(row))
                        char_row_colum.append(str(colum))
            lc.append('-'.join(char_row_colum))
        return ' '.join(lc)

    def dec(string):
        lc = []
        l = string.split()
        for char_id in l:
            char = tap.matrix[int(char_id[0])][int(char_id[1])]
            if char == 'ij':
                lc.append('_i/j_')
            else:
                lc.append(char)
        return ''.join(lc)


class base_x:
    needs_data = True
    data_prompt = ('What is the base you would like to '
                   'encode/decode in (eg 16 for hex or '
                   '2 for binary) must be 1 < base < 37: ')

    def data_valid(data):
        valid = True
        try:
            data_int = int(data)
        except:
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
            if char in base_x.lib:
                current_val = base_x.lib.index(char)
            if highest_val < current_val:
                highest_val = current_val

        minimum_base = highest_val + 1
        for base in range(minimum_base, 37):
            lc = []
            l = string.split()
            for character in l:
                lc.append(chr(int(character, base)))
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
            base = base_x.get_base()
        else:
            global extra_data
            base = int(extra_data)
        l = list(text)
        lc = []
        for char in l:
            char_num = ord(char)
            num = []
            while char_num:
                char_num, r = divmod(char_num, base)
                if r > 9:
                    num.append(base_x.lib[r])
                else:
                    num.append(str(r))
            lc.append(''.join(reversed(num)))
        return ' '.join(lc)

    def dec(string):
        if term:
            base = base_x.get_base()
        else:
            global extra_data
            base = int(extra_data)
        lc = []
        l = string.split()
        for character in l:
            lc.append(chr(int(character, base)))
        return ''.join(lc)


class phonetic:
    needs_data = False

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

    def crack(string):
        return 'This method is incompatible with cracking'

    def enc(phrase):
        phrase = phrase
        phonetic_phrase = []
        for char in phrase:
            if char in phonetic.phonetic_dict:
                phonetic_phrase.append(phonetic.phonetic_dict[char])
            else:
                phonetic_phrase.append(char)
        return " ".join(phonetic_phrase)

    def dec(phonetic_phrase):
        phonetic_phrase_list = phonetic_phrase.split()
        phrase = []
        for phrase_letter in phonetic_phrase_list:
            if phrase_letter in phonetic.phonetic_dict.values():
                for char, phonetic_letter in phonetic.phonetic_dict.items():
                    if phrase_letter == phonetic_letter:
                        phrase.append(char)
                        break
            else:
                phrase.append(phrase_letter)
        return "".join(phrase)


class hexi_decimal:
    needs_data = False

    def crack(string):
        return 'This method is incompatible with cracking'

    def enc(string):
        l = list(string)
        lc = []
        for char in l:
            lc.append(hex(ord(char)).strip('0x'))
        string = ' '.join(lc)
        return string

    def dec(string):
        l = string.split(' ')
        lc = []
        for char in l:
            lc.append(chr(int(char, 16)))
        string = ''.join(lc)
        return string


class ascii_id:
    needs_data = False

    def crack(string):
        return 'This method is incompatible with cracking'

    def dec(string):
        l = string.split(' ')
        lc = []
        for char in l:
            lc.append(chr(int(char)))
        string = ''.join(lc)
        return string

    def enc(string):
        l = list(ascii(string))
        lc = []
        for char in l:
            lc.append(str(ord(char)))
        string = ' '.join(lc)
        return string


class binary:
    needs_data = False

    def crack(string):
        return 'This method is incompatible with cracking'

    def dec(string):
        lc = []
        coded = True
        l = string.split()
        while coded:
            for character in l:
                lc.append(chr(int(character, 2)))
            string = ''.join(lc)
            coded = False
        return string

    def enc(string):
        l = list(string)
        lc = []
        for character in l:
            binary = bin(ord(character))[2:]
            binary = (8-len(binary))*'0'+binary
            lc.append(binary)
        string = ' '.join(lc)
        return string


class morse:
    needs_data = False
    lib = [
            '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..',
            '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
            '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----',
            '..---', '...--', '....-', '.....', '-....', '--...', '---..',
            '----.', '-----'
    ]

    def crack(string):
        return 'This method is incompatible with cracking'

    def dec(string):
        l = string.split(" ")
        lc = []
        for character in l:
            lc.append(General.eng[morse.lib.index(character)])
        string = ''.join(lc)
        return string

    def enc(string):
        l = list(string.lower())
        lc = []
        for character in l:
            if character == ' ':
                lc.append('')
            else:
                lc.append(morse.lib[General.eng.index(character)] + ' ')
        string = ''.join(lc)
        return string


class ceaser:
    needs_data = True
    data_prompt = 'What is the offset: '

    def data_valid(data):
        valid = True
        try:
            int(data)
        except:
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
        l = list(string.lower())
        lc = []
        if term:
            offset = ceaser.get_offset("dec")
        else:
            global extra_data
            offset = int(extra_data)
        for character in l:
            char_id = ((-offset + 26 + General.eng.index(character) + 26) % 26)
            lc.append(ceaser.ceaser_lib[char_id])
        string = ''.join(lc)
        return string

    def enc(string):
        l = list(string.lower())
        lc = []
        global term
        if term:
            offset = ceaser.get_offset()
        else:
            global extra_data
            offset = int(extra_data)
        for character in l:
            if character in ceaser.ceaser_lib:
                char_id = ((offset + General.eng.index(character) + 26) % 26)
                lc.append(ceaser.ceaser_lib[char_id])
            else:
                lc.append(character)
        string = ''.join(lc)
        return string


class General:
    cyphs = {
        'binary': binary, 'morse': morse, 'ceaser': ceaser,
        'hex': hexi_decimal, 'ascii': ascii_id, 'phonetic': phonetic,
        'base-x': base_x, 'tap': tap # add more here all strings must be
        # full lower case
    }
    list_of_methods = '\n'.join([
        'Binary', 'Morse', 'Ceaser', 'Hex', 'Ascii', 'Phonetic', 'Base-X',
        'Tap' # add more here formating doesn't matter
    ])
    eng = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    ]


def term_start():
    global term
    term = True
    """Function to run the program in terminal mode"""

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
        global gui
        gui = Tk()
        gui.title('Menu')

        global in_out_gui
        in_out_gui = Toplevel()
        in_out_gui.title('Input/Output')
        input_label = Label(
                            in_out_gui, text='Input', font=('Comic Sans MS', 12))
        input_label.pack(pady=5)
        string_textvar = StringVar(in_out_gui)
        input_entry = Entry(in_out_gui, textvariable=string_textvar, width=50)
        input_entry.pack()
        output_label = Label(
                            in_out_gui, text='Output', font=('Comic Sans MS', 12))
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
                    data_prompt_label.config(textvariable=StringVar(gui, prompt))
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
                try:
                    output_textvar.set(
                        General.cyphs[str_code_type].dec(StringVar.get(string_textvar))
                        )
                except:
                    print('errored')
            else:
                mode = 'Encode'
                try:
                    output_textvar.set(
                        General.cyphs[str_code_type].enc(StringVar.get(string_textvar))
                        )
                except:
                    print('errored')
            print(f'''
Mode: {mode}
Code method: {str_code_type}
Extra data: {extra_data}''')

        # Button to change mode between encode and decode
        on_enc_dec_button = Button(gui, textvariable=StringVar(gui,
                                                            value='Change mode'
                                                            ),
                                command=enc_dec_switch,
                                font=("Comic Sans MS", 12))
        on_enc_dec_button.pack(pady=10)

        # Label and text entry field for the code type
        code_entry_label = Label(gui,
                                text='How would you like to Decode your string:',
                                font=("Comic Sans MS", 12))
        code_entry_label.pack(pady=10)
        code_type = StringVar(gui, 'none')
        code_type.trace_add('write', update)
        code_menu_button = Menubutton(gui, textvariable=code_type, font=('Comic Sans MS', 10))
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
