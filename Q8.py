# import the string function to create a list of alphabet characteristics from a-z 
import string 
original_characters=[i for i in string.ascii_lowercase]
print(original_characters)
# use the reversed alphabet as our encryption: a is encrypted to z, b is encrypted to y...etc.
encrypted_characters=original_characters[::-1]
print(encrypted_characters)
# combine the two lists of characters into a coding dictionary 
encryption_dict=dict(list(zip(original_characters,encrypted_characters)))
print(encryption_dict)