#write a program to generate 6 character OTP.


import random
import string

id =''
characters_list = list(string.ascii_letters)
for i in range(6):
    id += random.choice(characters_list)
print(id)
