# Definición de una función llamada fib que genera la serie de Fibonacci hasta el número n
def fib(n):
    # Inicialización de los dos primeros números de la serie
    a, b = 0, 1
    
    # Bucle que se ejecuta mientras el valor de a sea menor que n
    while a < n:
        # Imprime el valor actual de a sin un salto de línea al final
        print(a, end=' ')
        
        # Actualiza los valores de a y b para calcular el siguiente número de Fibonacci
        a, b = b, a+b
    
    # Imprime una nueva línea para separar la serie de Fibonacci del resto de la salida
    print()

# Llamada a la función fib con el argumento 1000 para generar la serie de Fibonacci hasta 1000
fib(1000)