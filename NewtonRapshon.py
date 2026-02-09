import math

def derivada(f, h=0.8):
    return lambda x: (f(x + h) - f(x)) / h

def Newton_Rapshon(f, x, Er, N):
    Ea = Er + 1     # Error Relativo Actual
    i = 1           # Número de Iteración
    fd = derivada(f)
    
    # encabezado
    print(f"{'Iteración':^12} | {'Aproximación (xi)':^20} | {'Error (Ea)':^15}")
    print("-" * 53)
    
    while (Ea > Er) & (i < N):
        f_val = f(x)
        fd_val = fd(x)
        
        if fd_val == 0:
            print("Error: Derivada igual a cero.")
            break
            
        xi = x - (f_val / fd_val)
        Ea = abs((xi - x) / xi)
        
        # fila con celdas
        print(f"{i:^12} | {xi:20.8f} | {Ea:15.8f}")
        
        x = xi
        i += 1
        
    return xi

if __name__ == "__main__":
    # Función: f(x) = sin(x) - e^(-x)
    f = lambda x: math.sin(x) - math.exp(-x) 
    
    print("\nMETODO DE NEWTON RAPSHON")
    print("=" * 53)
    resultado = Newton_Rapshon(f, 0.5, 0.0001, 10)
    print("=" * 53)
    print(f"El valor aproximado de la raíz es: {resultado:.8f}\n")