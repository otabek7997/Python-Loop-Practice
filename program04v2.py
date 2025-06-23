from random import randint
from time import sleep

secret_code = randint(10, 99)

attempts = 0
max_attempts = 5


while attempts < max_attempts:
    guess = int(input(f'{attempts + 1} urinish, kodni toping '))
    if guess < secret_code:
        print('Kattaroq son ')
        
    elif guess > secret_code:
        print('Kichikroq son ')
        
    elif guess == secret_code:
        print("Malades ukam , topog'on ekansanu , topib qo'ydin gap yo'  ")    
        break

    attempts += 1

    if guess != secret_code and attempts == max_attempts:
        print("Sandan vanga chiqmekanu , kutginde kn yana harakat qilgin xoxlasen ")    
        sleep(15)
            
     

