a= int(input('Primer numero '))
b= int(input('segundo numero numero '))
c= int(input('tercer numero '))

x=min(a,b,c)
z=max(a,b,c)
y=(a+b+c)-x-z
print('los numeros de ordenados de mayor a menor {}, {} y {}'.format(z,y,x))