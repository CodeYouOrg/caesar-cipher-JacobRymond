unencrypted_text = input("What is your unencrypted text? \n")
encrypted_text = ""

for textChar in unencrypted_text:
    if 'a' <= textChar <= 'z':
        if ord(textChar) < 118:
            encrypted_text += str(chr(ord(textChar) + 5))
        else: 
            encrypted_text += (chr(97 + 4  - (122 - ord(textChar))))
    elif 'A' <= textChar <= 'Z':
         if ord(textChar) < 86:
            encrypted_text += str(chr(ord(textChar) + 5))
         else: 
            encrypted_text += (chr(65 + 4  - (90 - ord(textChar))))
    else:
        encrypted_text += textChar
        
print("The encrypted sentence is: " + encrypted_text)

