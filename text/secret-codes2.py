# Copyright 2016, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General 
# Public License

letters_in =  'aeiou bcdfghjklmnpqrstvwxyz'
letters_out = 'iouea bcdzgfjxlnmpqrtsvxwyz'
encode_trans = str.maketrans( letters_in, letters_out )
decode_trans = str.maketrans( letters_out, letters_in )

def encode(s):
    return s.lower().translate(encode_trans)

def decode(s):
    return s.lower().translate(decode_trans)

print("Welcome to the secret code generator!")

while True:
    
    i = input("Do you want to (e)ncode or (d)ecode? ")
    if i.lower() == 'e':
        a = input("Enter your text to encode: ")
        print(encode(a))
    else:
        a = input("Enter your text to decode: ")
        print(decode(a))

