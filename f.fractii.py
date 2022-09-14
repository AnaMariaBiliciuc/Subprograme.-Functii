a1= int(input("a1= "))
b1= int(input("b1="))
a2= int(input("a2= "))
b2= int(input("b2= "))
def adunare_fractii(x,y,z,t) :
    s=((x*t)+(y*z))/(y*t)
    return (s)
print("Suma fractiilor= ", adunare_fractii(a1,b1,a2,b2))

a1= int(input("a1= "))
b1= int(input("b1="))
a2= int(input("a2= "))
b2= int(input("b2= "))
def inmultire_fractii(x,y,z,t) :
    p= (x*z)/(y*t)
    return p
print("Produsul inmultirii= ", inmultire_fractii(a1,b1,a2,b2))


