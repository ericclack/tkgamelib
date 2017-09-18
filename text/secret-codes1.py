# Copyright 2016, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General 
# Public License

letters_in =  'aeiou bcdfghjklmnpqrstvwxyz'
letters_out = 'uoiea bcdzgfjxlmnpqrtsvwXyZ'
encode_trans = str.maketrans( letters_in, letters_out )
decode_trans = str.maketrans( letters_out, letters_in )

print("Welcome to the secret code generator!")

i = input("Do you want to (e)ncode or (d)ecode? ")
if i.lower() == 'e':

    while True:
        a = input("Enter your text to encode: ")
        print(a.lower().translate(encode_trans))

else:

    while True:
        a = input("Enter your text to decode: ")
        print(a.lower().translate(decode_trans))

