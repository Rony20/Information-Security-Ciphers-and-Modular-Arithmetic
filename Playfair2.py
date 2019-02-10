#KEY IS MYCODE
m = [['M','Y','C','O','D'],['E','A','B','F','G'],['H','I','J','K','L'],['N','P','Q','R','S'],['T','U','V','W','X']]
for i in m:
    print(i)

def playfair(msg):
    msg+='\0'
    result=""
    P=''
    q=''
    fi=0;fj=0;si=0;sj=0
    k=0

    while(k<len(msg)):
        p = msg[k]
        if p == '\0':
            break
        q = msg[k + 1]

        if q == '\0':
            q = 'X'

        if p == q:
            q = 'X'
            k += 1
        else:
            k += 2

        for i in range(5):
            if p in m[i]:
                fi=i
                fj=m[i].index(p)
            if q in m[i]:
                si=i
                sj=m[i].index(q)

        if fi == si:
            result += m[fi % 5][(fj + 1) % 5] + m[si % 5][(sj + 1) % 5]
        elif fj == sj:
            result += m[(fi+1) % 5][fj % 5] + m[(si+1) % 5][sj % 5]
        else:
            result += m[fi][sj] + m[si][fj]
    return result

msg="SNIPERCANNON"
print("Plain text    : "+msg)
print("Cipher text : "+playfair(msg))
