#This is a protoype.
import random

# Enter a word that has at LEAST 4 letters
print('please enter your root word for password creation\n')
root = input()
# print(root)

# Truncates the root word to only the first 3 letters
root2 = root[0:3]
# print(root[0:3])

# Generates a random number value from 1-100
num = random.randint(1, 101)
# print(random.randint(1,101))
# converts the random number into a string format, since strings can
# not be concatenated with ints. Num value updated
num = str(num)

# RandomString Generation
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def string_gen(length):
    return ''.join([random.choice(letters) for x in range(0, length)])


# Limits the amount of characters in the mod portion of the password to 4 letters
# Creates mod for input of 4
mod = str(string_gen(4))
# print(mod)

# Output
print('Your password is')
print('\n')
password = (mod + root2 + num)
print(password)
print('\n')



