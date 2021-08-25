
def main():
    #Escribe tu código debajo de esta línea
    
        e=int(input('Ingresa tu edad: '))
    if e>=18:
        io=str(input('¿Tienes identificación oficial? (s/n): '))
        if io==('s'):
            print('Trámite de licencia concedido')
        elif io==('n'):
            print('No cumples con los requisitos')
        elif io!=('s') or ('n'):
            print('Respuesta incorrecta')
    elif e<0:
        print('Respuesta incorrecta')
    elif e<18:
        print('No cumples requisitos')
    pass


if __name__ == '__main__':
    main()
