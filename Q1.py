import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

print('*****  start section 1 - print dictionary ********')


print(phonebook)
print(len(phonebook))


mydictionary = dict(m=8,n=9)
print(mydictionary)

chris_phone = phonebook["Chris"]
print(chris_phone)

print(phonebook.items())



print()
print('*****  end section 1 ********')
print()


'''



print('*****  start section 2 - search dictionary ********')

name ='Chris'
if name in phonebook:
    print(phonebook[name])
else:
    print(name,"is not in phonebook")




print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()





print()
print('*****  end section 3 ********')
print()


print(phonebook)

phonebook["Joe"]='555-0123'
phonebook["Chris"]='555-4444'

print(phonebook)





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()






print()
print('*****  end section 4 ********')
print()


print(phonebook)
del phonebook['Chris']
print(phonebook)



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for k in phonebook:
    print(k)
    print(phonebook[k])
# print(phonebook.keys())




print()
print('*****  end section 5 ********')
print()

for v in phonebook.values():
    print("254"+v)



print()
print('*****  start section 6 - using get and clear ********')
print()






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

for key,value in phonebook.items():
    print(key)
    print(value)

for item in phonebook.items():
    print(item)

for key,value in enumerate(phonebook):
    print(key)
    print(value)





print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()


phone = phonebook.get('Chris','key not found')
print(phone)
phone2=phonebook.get("Mary",'key not found')
print(phone2)

remove = phonebook.pop('Chris','not found')
print(remove)
print(phonebook)



print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

random_list=list(phonebook)
print(random_list)
random_key =random.choice(random_list)
print(random_key)
print(phonebook[random_key])



print()
print('*****  end section 9 ********')
print()

print(phonebook[random.choice(list(phonebook))])
'''





