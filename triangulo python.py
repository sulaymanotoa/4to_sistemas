num1=int(input("ingrese el cateto opuesto"))
num2=int(input("ingrese  el cateto adyacente"))
num3=int(input("ingrese  la hipotenusa"))
hipo=num1+num2
per=num1+num2+num3
area=num1*num3/2

if num3< hipo:
   print("no es correcto la hipotenusa es menor")
else:
  print("el perimetro es ",per)
  print("el area es  ",area)
 print("la hipotenusa es ",hipo)
