# Morse code converter
# .... . .-.. .-.. ---

MORSE_DICT = {
        'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',
        'f': '..-.',  'g': '--.',   'h': '....',  'i': '..',    'j': '.---',
        'k': '-.-',   'l': '.-..',  'm': '--',    'n': '-.',    'o': '---',
        'p': '.--.',  'q': '--.-',  'r': '.-.',   's': '...',   't': '-',
        'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',  'y': '-.--',
        'z': '--..'
    }
MORSE_TO_LETTER = {v: k for k, v in MORSE_DICT.items()}

def morse_code_converter(morse_code):
    decoded_letters = []
    for word in morse_code.split("/"):
        letter = word.split(" ")
        for l in letter:
            value = MORSE_TO_LETTER.get(l)
            if l in MORSE_TO_LETTER:
                decoded_letters.append(value)
        decoded_letters.append(" ")

    result = "".join(decoded_letters)
    return result

def main():
   end = False
   while not end:
       morse_code = input("Please enter morse code: ").strip()
       result =  morse_code_converter(morse_code=morse_code)
       print(result)
       end_program = input("Do you want to continue (y/n)")
       if end_program == "n":
           end = True

main()

