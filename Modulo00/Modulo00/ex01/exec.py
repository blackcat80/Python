import sys
string = " ".join(sys.argv[1:])
inverted_string = string[::-1]
inverted_string_swapcase = inverted_string.swapcase()
print(inverted_string_swapcase)
