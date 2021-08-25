def main():
    # Escribe el código adecuado para completar el programa
    x=int(input('Ingresa el primer número: '))
    y=int(input('Ingresa el segundo número: '))
    z=int(input('Ingresa el tercer número: '))

    if x>y and y>z:
        print(z)
        print(y)
        print(x)
    elif x>z and z>y:
        print(y)
        print(z)
        print(x)
    elif y>x and x>z:
        print(z)
        print(x)
        print(y)
    elif y>z and z>x:
        print(x)
        print(z)
        print(y)
    elif z>x and x>y:
        print(y)
        print(x)
        print(z)
    elif z>y and y>x:            
        print(x)
        print(y)
        print(z) 
    pass


if __name__=='__main__':
    main()
