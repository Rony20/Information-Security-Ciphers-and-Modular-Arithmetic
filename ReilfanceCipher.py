def encryption(msg,key):
    inc = 1;row = 0;col = 0
    result=""

    matrix = [["" for i in range(len(msg))] for j in range(key)]
    for char in msg:
        if row + inc < 0 or row + inc >= len(matrix):
            inc *= -1
        matrix[row][col] = char
        row += inc
        col += 1

    for list in matrix:
        result += "".join(list)
    return result

def decryption(result,key):
    matrix1 = [["" for i in range(len(result))] for j in range(key)]
    inc = 1;row = 0;col = 0

    for char in result:
        if row + inc < 0 or row + inc >= len(matrix1):
            inc *= -1
        matrix1[row][col] = "*"
        row += inc
        col += 1

    index = 0
    for i in matrix1:
        for j in range(len(i)):
            if i[j] == "*":
                i[j] = result[index]
                index += 1

    inc = 1;row = 0;col = 0

    mainmsg = ""
    for char in result:
        if row + inc < 0 or row + inc >= len(matrix1):
            inc *= -1
        mainmsg += matrix1[row][col]
        row += inc
        col += 1
    return mainmsg

msg=input("Enter message : ")
key=int(input("Enter key : "))

print("Plain text : "+msg)
result=encryption(msg,key)
print("Cipher text : "+result)
print("Decrypted text : "+decryption(result,key))
