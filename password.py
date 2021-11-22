# Concepts: Random module, strings

import random

passlen = int(input('Enter the desired length of the password: '))

s = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
p = ''.join(random.sample(s, passlen))

print('Your password is:',p)