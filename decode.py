def mod(a,b):
    if(a<b):
        return a
    else:
        return (a%b)

def decrip(cifra,n,d):
    msg = ''
    i = 0
    while i < len(cifra):
        msg += chr(mod( ord(cifra[i])**d , n))
        i += 1
    return msg

if __name__=='__main__':
    text = input("Encrypted Message: ")
    n = int(input("n value, private key: "))
    d = int(input("d value, private key: "))
    
    print('your original message:', decrip(text,n,d))