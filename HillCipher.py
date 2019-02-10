from typing import Any, Union
from numpy import *
from numpy import matrix
from numpy.core.multiarray import ndarray
from numpy.linalg import inv

hkey = matrix('9 7 11 13 ; 4 7 5 6 ; 2 21 14 9 ; 3 23 21 8')

def encrypt(msg):
    mylist = []
    result=""

    for i in msg:
        mylist.append(ord(i)-65)

    plain = matrix(array(mylist).reshape(3,4))
    cipher = plain*hkey
    division = cipher/26
    division = division.astype(int)
    cipher%=26

    for i in range(3):
        for j in range(4):
            result+=chr(cipher.item(i,j)+65)
    return (result,cipher,division)

def decrypt(result,cipher,division):
    mainmsg=""

    cipher = division*26+cipher
    plain = cipher*inv(hkey)

    for i in range(3):
        for j in range(4):
            mainmsg += chr(round(plain.item(i, j)) + 65)
    return mainmsg

msg="THISISMYTEXT"

result,cipher,division = encrypt(msg)

print("Plain text : "+msg)
print("Encrypted text : "+result)
print("Decrypted text : "+decrypt(result,cipher,division))