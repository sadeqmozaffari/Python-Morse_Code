# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

print("Welcom to Morse Code")

ENGLISH_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


#  morse to english
def decrypt(message):
    message += ' '
    text = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                text += ' '
            else:
                text += ENGLISH_CODE_DICT[citext]
                citext = ''
    return text


def encrypt(message):
    text = ''
    for item in message:
        if item != ' ':
            text += MORSE_CODE_DICT[item] + ' '
        else:
            text += " "
    return text


def get_message():
    return input("Please Enter Your Text: ").upper()


Continue = True
while Continue:
    con = input("for decrypt please enter the 'd' and for encrypt please enter 'e' \n"
                "and for terminate the program enter other keys: ").lower()

    if con == 'd':
        message = get_message()
        text = decrypt(message)
        print(f"message morse code: {message} \n translate to English: {text}")

    elif con == 'e':
        message = get_message()
        text = encrypt(message)
        print(f"message: {message} \n translate to morse code: {text}")
    else:
        Continue = False
        print("Good Luck \n Good Bye")
