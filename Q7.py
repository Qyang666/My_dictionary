#Prepare 
import os
os.getcwd()

#open file "sometext", lower all the characteristics and plit the text by words
with open('sometext.txt','r') as t:
    text_data=t.read().lower().split(" ")
    t.close()
print(text_data)

#import Counter function from the collection package and get the word frequency dictionary 
from collections import Counter
word_frequency_dict= Counter(text_data)
print(word_frequency_dict)

