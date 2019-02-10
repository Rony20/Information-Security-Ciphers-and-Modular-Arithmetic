from numpy import matrix
f=open('abc.txt','r')
msg=f.read()

msg+='\0'
result=""
m =matrix(" 'A' 'B' 'C' 'D' 'E' ;  'F' 'G' 'H' 'I' 'J' ; 'K' 'L' 'M' 'N' 'O' ; 'P' 'Q' 'R' 'S' 'T' ; 'U' 'V' 'W' 'X' 'Y' ")
print(m)
P=''
q=''
fi=0;fj=0;si=0;sj=0
k=0
while(k<len(msg)):
    p=msg[k]
    if p=='\0':
        break
    q=msg[k+1]

    if q=='\0':
        q='X'

    if p==q:
        q='X'
        k+=1
    else:
        k+=2

    for i in range(5):
        for j in range(5):
            if(m.item(i,j)==p):
                fi=i
                fj=j
            if(m.item(i,j)==q):
                si=i
                sj=j

    if fi==si:
        result += m.item(fi%5,(fj+1)%5) + m.item(si%5,(sj+1)%5)
    elif fj==sj:
        result += m.item((fi+1)% 5,fj%5) + m.item((si+1)%5,sj% 5)
    else:
        result+= m.item(fi,sj) + m.item(si,fj)

f1=open('abc_copy.txt','w')
for char in result:
    f1.write(char)

print("Ans : "+result)