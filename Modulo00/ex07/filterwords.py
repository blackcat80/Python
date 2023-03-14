import string
import sys

def main():
    if len(sys.argv) != 3:
        print("ERROR: Two arguments are required: a text string and an integer.")
        return
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("ERROR: Second argument must be an integer.")
        return

    s = sys.argv[1].translate(str.maketrans('', '', string.punctuation))

    palabras = [palabra for palabra in s.split() if len(palabra) > n and not palabra.isdigit()]

    print(palabras)

if __name__ == '__main__':
    main()
