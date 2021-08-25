def main():
    #escribe tu código abajo de esta línea
    
    p=float(input('Peso en kg: '))
    if p>0:
        a=float(input('Altura en m: '))
        if a>0:
            i=p/(a)**2
            if i<20:
                print('PESO BAJO')
            elif 20<=i<25:
                print('NORMAL')
            elif 25<=i<30:
                print('SOBREPESO')
            elif 30<=i<40:
                print('OBESIDAD')
            elif i>=40:
                print('OBESIDAD MORBIDA')
        elif a<=0:
            print('Revisa tus datos, alguno de ellos es erróneo')
    elif p<=0:
        print('Revisa tu dato, es erróneo')
    pass
if __name__=='__main__':
    main()
