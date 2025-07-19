import  string  
import random
chars = " " + string.ascii_letters + string.digits +string.punctuation # Generat randome chars 
chars= list(chars)
key=chars.copy()  
random.shuffle(key)     
# Encrypt 
user_cipher=input("Enter your message to encrypt : ")
encrypt_message=''
for  i in user_cipher :
    index = chars.index(i)
    encrypt_message += key[index]
print(f'the originale message is {user_cipher}')
print(f'the encrypt message is  {encrypt_message}')








