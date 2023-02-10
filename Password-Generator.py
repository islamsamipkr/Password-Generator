#PASSWORD-GENERATOR
import random
letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']    

total=int(input("How many total characters do you want in the password?"))   
numbers=int(input("How many numbers do you want in the password?"))
letters=int(input("How many letters do you want in the password?"))
symbol=int(input("How many symbols do you want in the password?"))
password=[]
password_string = ""
for charac in range(total):
    password.append(random.choice(letter_list))

if total!=numbers+letters+symbol:
    print("Total does not match up to values provided for numbers, letters and symbol combined")
else:
    for charac in range(1,numbers+1):
        password.append(random.choice(number_list))
    for charac in range (numbers,(numbers+letters)):
        password.append((random.choice(letter_list)))
    for charac in range(numbers+letters-1,numbers+letters+symbol):
        password.append((random.choice(symbol_list)))
    for i in password:
        password_string = password_string+i
    print(password_string)
