def affine(msg,key):
    result = ""
    for i in range(len(msg)):
        if i == 0:
            result += chr(((ord(msg[i]) - 64) + key) % 26 + 64)
        else:
            result += chr(((ord(msg[i]) - 64) + (ord(msg[i - 1]) - 64)) % 26 + 64)
    return result

key = int(input("Enter key : "))
msg="THISISMYMESSAGE"

print("Plain text    : "+msg)
print("Cipher text : "+affine(msg,key))

"""
For printing charcters and their values
print("Characters in string : ")
for i in msg:
    print(i,end="    ")

print("\nValue for msg :")
for i in range(len(msg)):
    print(ord(msg[i])-64,end="   ")

print("\nAuto key values")
for i in range(len(msg)):
    if i==0:
        print("12",end="   ")
    else:
        print(ord(msg[i-1])-64,end="   ")

print("\nValues which we are getting : ")
for i in range(len(msg)):
    if i==0:
        print(((ord(msg[i])-64)+12)%26,end="   ")
    else:
        print(((ord(msg[i])-64) + (ord(msg[i-1])-64))%26,end="   ")

print("\nCipher characters")
for i in range(len(msg)):
    if i==0:
        print(chr(((ord(msg[i])-64)+12)%26+64),end="   ")
        result+=chr(((ord(msg[i])-64)+12)%26+64)
    else:
        print(chr(((ord(msg[i])-64) + (ord(msg[i-1])-64))%26+64),end="   ")
        result+=chr(((ord(msg[i])-64) + (ord(msg[i-1])-64))%26+64)
"""