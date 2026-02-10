# Cálculo-Numérico-Allenairam-Rojas
Este repositorio contiene una colección de algoritmos fundamentales de análisis numérico para la resolución de ecuaciones no lineales, integración definida y aproximación de funciones.


## Contenido del Repositorio

### 1. Búsqueda de Raíces

#### **Método de Bisección (`Biseccion.py`)**
Es un método de "encerrado" basado en el Teorema del Valor Medio. 
* **Funcionamiento:** Divide un intervalo [a, b] a la mitad y selecciona el subintervalo donde existe un cambio de signo.
* **Control de errores:** El algoritmo calcula el error relativo aproximado (E_a) en cada iteración hasta cumplir la tolerancia deseada (E_s) o alcanzar el límite de iteraciones (NI).



#### **Método de Newton-Raphson (`NewtonRapshon.py`)**
Un algoritmo iterativo abierto que utiliza la derivada de la función para encontrar raíces rápidamente.
* **Fórmula:** Utiliza la relación x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}.
* **Derivación Numérica:** Calcula la derivada mediante diferencias finitas con un paso h ajustable.
* **Eficiencia:** Ofrece una convergencia más rápida que la bisección, aunque requiere una buena aproximación inicial para evitar divergencias.



### 2. Integración Numérica

#### **Regla de Simpson 1/3 (`IntegracionNumerica.py`)**
Aproxima el valor de una integral definida utilizando parábolas en lugar de líneas rectas.
* **Requisito:** El número de intervalos (n) debe ser obligatoriamente un número par.
* **Ponderación:** Aplica pesos de 1, 4, 2 a los puntos evaluados para mejorar la precisión del área bajo la curva.

#### **Riemman.py: **
  Cálculo de la integral definida mediante la Suma de Riemann por la izquierda, permitiendo aproximar el área bajo una curva dividiéndola en n rectángulos.



### 3. Aproximación de Funciones

#### **Polinomio de Taylor (`PolinomioTaylor.py`)**
Permite representar una función mediante una suma finita de sus derivadas calculadas en un punto específico (x_0).
* **Lógica:** Implementa derivación numérica recursiva para construir polinomios de grado $n$.
* **Análisis de Error:** El script entrega el Error Absoluto comparando el valor aproximado con el valor real de la función.
