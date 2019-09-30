import os
os.system('clear')
n=1
fc=0
bc=0
fbc=0
while (n<=100):
    if(n%3==0)and(n%5==0):
        print(str(n)+".Fizzbuzz")
        fbc+=1
    elif (n%3==0):
        print(str(n)+"fizz")
        fc+=1
    elif (n%5==0):
        print(str(n)+".buzz")
        bc+=1

    n+=1
print("________________________________________")
print("Fizz\tBuzz\tFiizBuzz")
print ( str(fc) + '\t' + str(bc)+ '\t' + str(fbc) )