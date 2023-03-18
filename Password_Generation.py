import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRESTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*/,.[]{}_-;'()"
all = lower + upper + numbers + symbols
length = 15
password = "".join(random.sample(all,length))
print(password)