a=int(input("Enter number : "))
b=int(input("Enter mod : "))

r1=b;r2=a
if(r1<r2):
    (r1,r2)=(r2,r1)
t1=0;t2=1

while(r1>1):
    r=r1%r2
    q=r1//r2
    r1=r2
    r2=r
    t=t1-(q*t2)
    t1=t2
    t2=t

if(r1!=1):
    print("Invers of ",a," in mod ",b," does not exist.")
else:
    print("Invers of ",a," in mod ",b," is",t1,".")

