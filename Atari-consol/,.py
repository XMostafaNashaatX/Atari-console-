k=int(input('please enter the number of integration'))
n=str(input('please enter cofecciants seperating them using space:')).split()
while len(n)!=k:
    print('error the number dont match')
    n = str (input ('please re-enter numbers cofecciants them using space:')).split ()
print(n)
b=[]
for i in n:
    a = int(i)
    b.append(a)

c=str(input('please enter the power of the numbers')).split()
while len(c)!=k:
    print ('error the number dont match')
    c = str (input ('please re-enter the power of the numbers')).split()

