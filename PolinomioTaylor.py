import math

def Derivar(f, h = 0.01):
    def _(x):
        return (f(x + h) - f(x))/h
    return _

def Polinomio_Taylor(f, x0, n):
    def Polinomio(x):
        i=1
        p=f(x0)
        while (i!=n+1):
            if (i==1):
                d_Actual=Derivar(f)
                p+=d_Actual(x0) * (x-x0)
            else:
                d_Actual=Derivar(d_Actual)
                p+=( d_Actual(x0) * (x-x0)**i ) / math.factorial(i) 
            i+=1      
        return p
    return Polinomio

f=lambda x: x**2 + math.cos(x)

def Resul_Polinomio(f, x, x0, n):
    poli = Polinomio_Taylor(f, x0, n)
    valor_approx = poli(x)
    valor_real = f(x)
    error_rel = abs(valor_real - valor_approx)

    # Encabezado Organizado
    print("\n" + "="*70)
    print(f"{'RESULTADOS DEL POLINOMIO DE TAYLOR':^70}")
    print("="*70)
    
    # Definición de columnas: Concepto | Valor
    print(f"{'Concepto':<25} | {'Valor Calculado':<40}")
    print("-" * 70)
    
    print(f"{'Punto de evaluación (x)':<25} | {x:<40}")
    print(f"{'Centro (x0)':<25} | {x0:<40}")
    print(f"{'Grado del polinomio (n)':<25} | {n:<40}")
    print("-" * 70)
    
    # Resultados numéricos formateados a 6 decimales
    print(f"{'Valor Aproximado':<25} | {valor_approx:<40.6f}")
    print(f"{'Valor Real':<25} | {valor_real:<40.6f}")
    print(f"{'Error Absoluto':<25} | {error_rel:<40.6e}") # Notación científica para errores pequeños
    
    print("="*70 + "\n")
    
    return valor_approx

if __name__ == '__main__':
    Resul_Polinomio(f,0.3,0,3)