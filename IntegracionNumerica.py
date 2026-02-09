import math

def Integracion_Numerica(f, a, b, n):
    """
    f: Función a integrar
    a: Límite inferior
    b: Límite superior
    n: Número de intervalos (debe ser par)
    """
    if n % 2 != 0:
        print("Error: El número de intervalos debe ser par")
        return None

    h = (b - a) / n
    suma_par = 0
    suma_impar = 0
    
    # Encabezado 
    print(f"\n{'Punto (i)':^10} | {'x_i':^15} | {'f(x_i)':^15} | {'Peso':^8}")
    print("-" * 55)

    for i in range(n + 1):
        xi = a + i * h
        fi = f(xi)
        
        # Determinar el coeficiente
        if i == 0 or i == n:
            peso = 1
        elif i % 2 == 0:
            peso = 2
            suma_par += fi
        else:
            peso = 4
            suma_impar += fi
        
        print(f"{i:^10} | {xi:15.5f} | {fi:15.5f} | {peso:^8}")

    # Formula
    resultado = (h / 3) * (f(a) + f(b) + 4 * suma_impar + 2 * suma_par)
    return resultado

if __name__ == "__main__":
    # Ejemplo: Integrar f(x) = sin(x) desde 0 hasta pi
    f = lambda x: math.sin(x)
    
    limite_a = 0
    limite_b = math.pi
    intervalos = 6 # Debe ser par
    
    print(f"Calculando la integral de sin(x) de {limite_a} a {limite_b:.4f}...")
    
    integral = Integracion_Numerica(f, limite_a, limite_b, intervalos)
    
    if integral is not None:
        print("-" * 55)
        print(f"El valor aproximado de la integral es: {integral:.8f}")
        # El valor exacto de la integral de sin(x) de 0 a pi es 2.0
        error_abs = abs(2.0 - integral)
        print(f"Error absoluto estimado: {error_abs:.8f}")