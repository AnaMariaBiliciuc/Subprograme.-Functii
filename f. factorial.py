n= int(input("Nr n= "))
m= int(input("Nr m= "))
def factorial(x):
    fact=1
    for i in range (1,x+1) :
        fact=fact*i
    return fact
if n>m: 
    print("C=", (factorial(n))/ (factorial(m))*(factorial(n-m)))
else :
    print("Introduceti alte valori!")