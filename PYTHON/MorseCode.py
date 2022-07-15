MORSE_DICT = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encode(message):
    cipher = ''
    for letter in message:
        if letter != '':
            cipher += MORSE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decode(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(citext)]
                citext = ''
    return decipher




def main():
    message = "Hello"
    result = encode(message.upper())
    print(result)

    message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
    result = decode(message)
    print(result)

if __name__ == '__main__':
    main()