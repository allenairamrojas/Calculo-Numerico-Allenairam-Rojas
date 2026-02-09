import math

def signo(f,a,b):
    return (f(a)*f(b))

def Biseccion(f, a, b, Es, NI):
    #f funcion
    #a limite inferior
    #b limite superior
    #Es error relativo deseado
    #NI numero maximo de iteraciones
    Ea = 100.0  # Error aproximado relativo
    I = 1       # Contador del número de iteraciones
    M_Actual = 0.0 # Punto medio actual
    M_Previa = 0.0 # Punto medio anterior
    
    # Imprimir encabezado de la tabla
    print("----------------------------------------------------------------------")
    print("| I |     a     |     b     | Punto Medio | Error Relativo (Ea) |")
    print("----------------------------------------------------------------------")
    
    if (signo(f,a,b) < 0):

        while (I < NI) & (Ea > Es):
            
            # Almacena el punto medio anterior 
            M_Previa = M_Actual
            M_Actual = (a + b) / 2
            
            # Determina el nuevo subintervalo
            if (f(M_Actual) * f(b) < 0):
                a_print = M_Actual # Usamos M_Actual como el nuevo límite a para la siguiente iteración
                b_print = b
                a = M_Actual # Actualizamos a
            else:
                a_print = a
                b_print = M_Actual # Usamos M_Actual como el nuevo límite b para la siguiente iteración
                b = M_Actual # Actualizamos b
            
            #calcula el error relativo aprox
            if I > 1:
                Ea = math.fabs(((M_Actual - M_Previa) / M_Actual))
                print(f"|{I:2d} | {a_print:9.6f} | {b_print:9.6f} |   {M_Actual:9.6f} |     {Ea:10.6f}      |")
            else:
                # La primera iteración no tiene error relativo para calcular
                print(f"|{I:2d} | {a:9.6f} | {b:9.6f} |   {M_Actual:9.6f} |      (No aplica)    |")
                
            I += 1

        print("----------------------------------------------------------------------")
        if Ea <= Es:
            print(f"Raíz aproximada: {M_Actual:.6f}. Error final: {Ea:.6f}.")
        elif I == NI:
            print(f"Máximo de iteraciones ({NI}) alcanzado. Raíz: {M_Actual:.6f}.")
        
        return M_Actual
        
    else:
        print("********")
        print("No existe el intervalo. La función tiene el mismo signo en los límites.")
        print("********")
        return None
        
if __name__ == '__main__':
    f = lambda x: math.sin(x)-math.exp(-x)
    
    # Ejecutamos con los parametros 
    Biseccion(f, -5, 2, 0.04, 20)