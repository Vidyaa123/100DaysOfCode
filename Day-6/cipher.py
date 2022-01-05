import string
def encode_message(message, shift):
    encoded_message = ""
    
    for char in message:
        location = int(string.ascii_letters.index(char.lower()))
        new_location = location +shift
        new_char =string.ascii_letters[new_location]
        encoded_message += new_char
    return(encoded_message)

def decode_message(message, shift):
    decoded_message = ""
    for char in message:
        location = int(string.ascii_letters.index(char.lower()))
        new_location = location - shift
        new_char =string.ascii_letters[new_location]
        decoded_message += new_char
    return(decoded_message)
    
en_de = input("Enter 'encode' or 'decode' (press e of d):-")
message = str(input("Enter the message to encode or decode :-"))
shift = int(input("Enter the number to shift :-"))
print(string.ascii_letters)
if en_de == 'e':
    print("Encoded message:-" +encode_message(message, shift))
elif en_de == 'd':
    print("Decoded Message -"+adecode_message(message, shift))
else:
    print("Wrong input - Enter either e or d")

