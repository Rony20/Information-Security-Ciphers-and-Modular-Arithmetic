def encrypt(msg,k,t):
    result = ""
    for i in msg:
        if i == ' ' or i == '\n' or i == '!':
            result = result + i
        else:
            result = result + chr(((((ord(i) - 65) * k) + t) % 26) + 65)
    return result

def decrypt(result,k1,t):
    mainmsg = ""
    for i in result:
        if i == ' ' or i == '\n' or i == '!':
            mainmsg = mainmsg + i
        else:
            mainmsg = mainmsg + chr(((((ord(i) - 65) - 2) * k1) % 26) + 65)
    return mainmsg


k = int(input("Enter k : "))
t = int(input("Enter t : "))

for i in range(1,26):
    if ((k*i)%26)==1:
        k1=i
        break

message = "HELLO THERE I AM HERE!"

print("Plain text            : " + message)
result = encrypt(message,k,t)
print("Encrypted  text : " + result)
print("Again msg          :"+decrypt(result,k1,t))

3