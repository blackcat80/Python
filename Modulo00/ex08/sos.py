import sys

morse_dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
                   '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def morse_encode(str):
    encoded_chars = []
    for char in str:
        if char == ' ':
            encoded_chars.append('/')
        elif not str.isalnum():
            print("ERROR")
            exit()
        elif char.upper() in morse_dictionary:
            encoded_chars.append(morse_dictionary[char.upper()])
    return ' '.join(encoded_chars)

def main():    
    if len(sys.argv) == 1:
        return
    str = ' '.join(sys.argv[1:])
    
    encoded_str = morse_encode(str)
   
    print(encoded_str)

if __name__ == '__main__':
    main()

