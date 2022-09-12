#import the data
with open('info_security.txt','r') as t:
    text_data=t.read()
    t.close()
print(text_data)

# get the coding dictionary from the previous exercise
import string 
original_characters=[i for i in string.ascii_lowercase]
# use the reversed alphabet as our encryption: a is encrypted to z, b is encrypted to y...etc.
encrypted_characters=original_characters[::-1]
# combine the two lists of characters into a coding dictionary 
encryption_dict=dict(list(zip(original_characters,encrypted_characters)))

# encrypt text_data
encrypted_data=""

for i in text_data:
    if i in encryption_dict:
        encrypted_data +=encryption_dict[i]
    else:
        encrypted_data +=i

print(encrypted_data)