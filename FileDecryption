#import needed codes from previous exercises
with open('info_security.txt','r') as t:
    text_data=t.read()
    t.close()
print(text_data)
import string 
original_characters=[i for i in string.ascii_lowercase]
encrypted_characters=original_characters[::-1]
encryption_dict=dict(list(zip(original_characters,encrypted_characters)))
encrypted_data=""

for i in text_data:
    if i in encryption_dict.keys():
        encrypted_data +=encryption_dict[i]
    else:
        encrypted_data +=i
print(encrypted_data)


# Create a decryption_dict
decryption_dict=dict(map(reversed, encryption_dict.items()))
print(decryption_dict)

# Time to decrypt
decrypted_data=""

for i in encrypted_data:
    if i in decryption_dict:
        decrypted_data += decryption_dict[i]
    else:
        decrypted_data +=i

print(decrypted_data)

#Compare the decrypted text with the original text
decrypted_data==text_data


