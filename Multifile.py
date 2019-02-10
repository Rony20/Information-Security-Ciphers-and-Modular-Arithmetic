import os

path = 'D:\CP-SEM_6\IS\Programs\Try'
msg=""
result=""
for root,dir,files in os.walk(path):
    print("Root : ",root)
    print("Directory : ",dir)
    print("File : ",files)

    for file in files:
        os.chdir(root)
        with open(file,'r') as f1:
            msg=f1.read()

            for i in msg:
                if i == ' ' or i == '\n':
                    result = result + i
                else:
                    result = result + chr(((ord(i) - 65 + 3) % 26) + 65)

            newfile=file.split('.')
            myfile=newfile[0]+"_copy."+newfile[1]
            with open(myfile,'w') as f2:
                for j in result:
                    f2.write(j)
