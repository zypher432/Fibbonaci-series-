fib=int(input('enter the number of terms'))
a,b = 0,1
count=0
if fib <= 0:
    print("enter the number")
elif fib == 1:
    print("fibonacci seq upto",fib,":")
    print(a)
else:
    print("fibonnci series:")
    while count<fib:
        print(a)
        c=a+b
        a=b
        b=c
        count+=1
    """print(b)
 
    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(c)
print('the number'fib)"""
