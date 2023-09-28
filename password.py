import random
import string

print("cuantos caracteres desea")
print(jls_extract_var)
cant_caracteres = int(input())


if(cant_caracteres > 4):

    print("password:")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase 
    num = string.digits

    symbols = string.punctuation

    chars = lower+upper+num+symbols

    temp = random.sample(chars,cant_caracteres)

    print("".join(temp))


else:

    print("su contraseña debe tener mas de 4 caracteres")


