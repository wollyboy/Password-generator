
import random
import string 
chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
all = chars + chars1 + numbers
password = ''.join(random.choice(all)for i in range(8))
print (password)