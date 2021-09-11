import random
from math import sqrt

def prime(n): 
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False

def mdc(n1,n2):
    rest = 1
    while(n2 != 0):
        rest = n1%n2
        n1 = n2
        n2 = rest
    return n1

def generate_E(num): 
    while True:
        e = random.randrange(2,num) 
        if(mdc(num,e) == 1):
            return e
   
def numPrime():
    while True:
        x=random.randrange(1,100)
        if(prime(x)):
            return x

def mod(a,b):
    if(a<b):
        return a
    else:
        return (a%b)

def cipher(words,e,n):
    i = 0
    lista = ''
    while(i < len(words)):
        k = ord(words[i])
        k = k**e
        lista += chr(mod(k,n))
        i += 1
    return lista

def decrip(cifra,n,d):
    msg = ''
    i = 0
    while i < len(cifra):
        msg += chr(mod( ord(cifra[i])**d , n))
        i += 1
    return msg

def generate_D(toti,e):
    d = 0
    while(mod(d*e,toti)!=1):
        d += 1
    return d

## MAIN
if __name__=='__main__':
    text = input("Message encrypt: ")
    p = numPrime() 
    q = numPrime() 

    n = p*q 

    totiente_de_N = (p-1)*(q-1) 

    e = generate_E(totiente_de_N) 
    d = generate_D(totiente_de_N,e)

    print('Public key:', (n, e))
    print('Private key:', (n, d))

    text_cipher = cipher(text,e,n)
    print('Encrypted message:', text_cipher)

    resps = input('Gostaria de descriptar? (S/N)')    
    if(resps == 'S'):
        original_text = decrip(text_cipher,n,d)
        print('Original message:', original_text)