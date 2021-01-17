import random

chars = "abcdefghijklmnopqrstwxyzABCDRFGHIJKLMNOPQRSTWXVY!@#$%()"

while 1:
    password_len = int(input("what is lenght of password you like to generte:"))
    password_count = int(input("how many passwords would you like:"))
    for x in range(0,password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("here i your password : ", password)