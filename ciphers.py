# Ceaser Cipher

# In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher.
# Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# Program:-

def encypt_func(txt, s):  
    result = ""  
  
  
# transverse the plain txt  
    for i in range(len(txt)):  
        char = txt[i]  
        # encypt_func uppercase characters in plain txt  
  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        # encypt_func lowercase characters in plain txt  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  
# check the above function  
txt = "SKKZ NKXK"  
s = 4  
  
print("Plain txt : " + txt)  
print("Shift pattern : " + str(s))  
print("Cipher: " + encypt_func(txt, s))



# Diffie Hellman Cipher

# The Diffie–Hellman (DH) Algorithm is a key-exchange protocol that enables two parties communicating over public channel to establish a mutual secret without 
# it being transmitted over the Internet.

# Program:-

from random import randint
 
if __name__ == '__main__':
 
    # Both the persons will be agreed upon the
    # public keys G and P
    # A prime number P is taken
    P = 23
     
    # A primitive root for P, G is taken
    G = 9
     
      
    print('The Value of P is :%d'%(P))
    print('The Value of G is :%d'%(G))
     
    # Alice will choose the private key a
    a = 4
    print('The Private Key a for Alice is :%d'%(a))
     
    # gets the generated key
    x = int(pow(G,a,P)) 
     
    # Bob will choose the private key b
    b = 3
    print('The Private Key b for Bob is :%d'%(b))
    
    # gets the generated key
    y = int(pow(G,b,P)) 
     
     
    # Secret key for Alice
    ka = int(pow(y,a,P))
     
    # Secret key for Bob
    kb = int(pow(x,b,P))
     
    print('Secret key for the Alice is : %d'%(ka))
    print('Secret Key for the Bob is : %d'%(kb))
    
    
# Hill Cipher
    
# In classical cryptography, the Hill cipher is a polygraphic substitution cipher based on linear algebra. Invented by Lester S. Hill in 1929, 
# it was the first polygraphic cipher in which it was practical to operate on more than three symbols at once.
    
# Program:-
    
keyMatrix = [[0] * 3 for i in range(3)]
 
messageVector = [[0] for i in range(3)]
 
cipherMatrix = [[0] for i in range(3)]
 
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
 
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
 
def HillCipher(message, key):
 
    getKeyMatrix(key)
 
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 
    encrypt(messageVector)
 
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
 
    print("Ciphertext: ", "".join(CipherText))
 
# Driver Code
def main():
 
    message = "ACT"
 
    key = "GYBNQKURP"
 
    HillCipher(message, key)
 
if __name__ == "__main__":
    main()
    
    
    
    
# PlayFair Cipher
    
# The Playfair cipher or Playfair square or Wheatstone–Playfair cipher is a manual symmetric encryption technique and was the first literal digram substitution cipher.
    
# Program:-
    
key=input("Enter key")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for c in key: #storing key
    if c not in result:
        if c=='J':
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): #storing other character
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
k=0
my_matrix=matrix(5,5,0) #initialize matrix
for i in range(0,5): #making matrix
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():  #Encryption
    msg=str(input("ENTER MSG:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decrypt():  #decryption
    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")
        
        
# Vegenere Cipher

# The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. 
# It employs a form of polyalphabetic substitution.

# Program:-

def generateKey(string, key): 
  key = list(key) 
  if len(string) == len(key): 
    return(key) 
  else: 
    for i in range(len(string) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 
  
def encryption(string, key): 
  encrypt_text = [] 
  for i in range(len(string)): 
    x = (ord(string[i]) +ord(key[i])) % 26
    x += ord('A') 
    encrypt_text.append(chr(x)) 
  return("" . join(encrypt_text)) 
def decryption(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('A') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 
if __name__ == "__main__": 
  string = input("Enter the message: ")
  keyword = input("Enter the keyword: ")
  key = generateKey(string, keyword) 
  encrypt_text = encryption(string,key) 
  print("Encrypted message:", encrypt_text) 
  print("Decrypted message:", decryption(encrypt_text, key))
