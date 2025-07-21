# Morse code converter
# .... . .-.. .-.. ---

def morse_code_converter():
    morse_dict = {
        'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
        'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
        'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
        'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
        'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
        'z': '--..'
    }
    morse_to_letter = {v: k for k, v in morse_dict.items()}
    morse_code = input("Please enter morse code").strip()
    letters = morse_code.split(" ")
    word = []

    for letter in letters:
        if letter in morse_to_letter:
            value = morse_to_letter.get(letter)
            word.append(value)
        else:
            word.append("?")

    result = "".join(word)
    return result

def main():
    morse_code_converter()


