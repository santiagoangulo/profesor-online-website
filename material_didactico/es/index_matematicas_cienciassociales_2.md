# Matemáticas Aplicadas a las Ciencias Sociales II
## 2.º Bachillerato — Comunidad de Madrid
### Currículo: Decreto 64/2022 (LOMLOE)

**Descripción:** Índice temático completo organizado en capítulos didácticos con numeración de tres niveles. Cada subapartado incluye la referencia al bloque oficial de saberes básicos del Decreto 64/2022. Los ejemplos y aplicaciones están orientados al contexto de las Ciencias Sociales (economía, ciencias políticas, sociología, demografía). Este curso consolida y amplía los contenidos de CCSS I, con especial peso en el álgebra matricial, el análisis matemático (derivadas e integrales) y la inferencia estadística.

---

## ÍNDICE GENERAL

1. [Matrices](#cap1)
2. [Determinantes](#cap2)
3. [Sistemas de Ecuaciones Lineales](#cap3)
4. [Programación Lineal](#cap4)
5. [Límites, Continuidad y Derivabilidad](#cap5)
6. [Derivadas y Aplicaciones](#cap6)
7. [Representación de Funciones](#cap7)
8. [Integrales](#cap8)
9. [Probabilidad](#cap9)
10. [Distribuciones de Probabilidad](#cap10)
11. [Inferencia Estadística](#cap11)

---

## Capítulo 1. Matrices {#cap1}

### 1.1 Concepto y tipos de matrices

#### 1.1.1 Definición de matriz: elementos, filas, columnas y orden
`[Bloque: Álgebra (1.ª evaluación) > Matrices para sistemas de ecuaciones lineales y grafos; Bloque: Números y Operaciones > Adición y producto de matrices]`
Definición formal $A = (a_{ij})$ de orden $m \times n$. Notación. Matrices cuadradas, rectangulares, fila, columna. Aplicaciones: representación de datos tabulares en CCSS (tablas de contingencia, matrices de input-output).

#### 1.1.2 Tipos especiales de matrices: identidad, nula, diagonal, triangular, simétrica
`[Bloque: Números y Operaciones > Adición y producto de matrices, propiedades]`
Caracterización de cada tipo. Propiedades relevantes. La matriz identidad $I_n$ y su papel en el álgebra matricial.

#### 1.1.3 Traspuesta de una matriz: definición y propiedades
`[Bloque: Números y Operaciones > Adición y producto de matrices, propiedades]`
Definición $A^T = (a_{ji})$. Propiedades: $(A^T)^T = A$, $(A+B)^T = A^T + B^T$, $(AB)^T = B^T A^T$. Matrices simétricas y antisimétricas.

### 1.2 Operaciones con matrices

#### 1.2.1 Suma y diferencia de matrices: definición y propiedades
`[Bloque: Números y Operaciones > Adición y producto de matrices, propiedades]`
Condición de conformidad (mismo orden). Conmutatividad, asociatividad, elemento neutro (matriz nula), opuesta. Aplicaciones: suma de datos estadísticos matriciales.

#### 1.2.2 Producto de un escalar por una matriz
`[Bloque: Números y Operaciones > Adición y producto de matrices, propiedades]`
Definición. Propiedades distributivas. Aplicaciones: escalado de datos, modelos de precios con parámetro.

#### 1.2.3 Producto de matrices: condición de conformidad, definición y cálculo
`[Bloque: Números y Operaciones > Adición y producto de matrices, propiedades]`
Condición: número de columnas de $A$ = número de filas de $B$. Definición $c_{ij} = \sum_k a_{ik} b_{kj}$. Cálculo paso a paso. Orden del producto resultante.

#### 1.2.4 Propiedades del producto de matrices: asociatividad, distributividad y NO conmutatividad
`[Bloque: Números y Operaciones > Adición y producto de matrices, propiedades]`
Demostración con contraejemplos de la no conmutatividad. Propiedades que sí se cumplen. Consecuencias algebraicas: $AB = 0 \not\Rightarrow A = 0$ o $B = 0$.

#### 1.2.5 Potencias de matrices cuadradas
`[Bloque: Números y Operaciones > Adición y producto de matrices, propiedades]`
Definición de $A^k$ para $k \in \mathbb{N}$. $A^0 = I$. Cálculo de potencias. Aplicaciones: cadenas de Markov, modelos de transición de estados (demografía, comportamiento electoral).

#### 1.2.6 Matrices y grafos: matriz de adyacencia
`[Bloque: Álgebra (1.ª evaluación) > Matrices para sistemas de ecuaciones lineales y grafos]`
Representación de un grafo mediante su matriz de adyacencia. Relación entre $A^k$ y caminos de longitud $k$. Aplicaciones: redes de contactos sociales, análisis de influencia en redes.

### 1.3 Pensamiento computacional con matrices

#### 1.3.1 Uso de tecnología (hoja de cálculo, GeoGebra) para operar con matrices
`[Bloque: Álgebra (1.ª evaluación) > Pensamiento computacional con matrices/sistemas]`
Introducción de matrices en hoja de cálculo. Funciones de multiplicación matricial (MMULT), transposición (TRANSPONER) e inversa (MINVERSA). Verificación automática de resultados.

---

## Capítulo 2. Determinantes {#cap2}

### 2.1 Determinante de orden 2 y orden 3

#### 2.1.1 Determinante de una matriz 2×2: definición y cálculo
`[Bloque: Números y Operaciones > Determinantes: regla de Sarrus]`
Fórmula $\det A = a_{11}a_{22} - a_{12}a_{21}$. Interpretación geométrica (área del paralelogramo). Aplicaciones: comprobación de independencia lineal.

#### 2.1.2 Determinante de una matriz 3×3: Regla de Sarrus
`[Bloque: Números y Operaciones > Determinantes: regla de Sarrus]`
Regla de Sarrus: desarrollo diagonal. Cálculo sistemático paso a paso. Ejemplos con matrices de coeficientes de sistemas económicos.

#### 2.1.3 Desarrollo por adjuntos (cofactores): cualquier orden
`[Bloque: Números y Operaciones > Determinantes: regla de Sarrus]`
Menor complementario $M_{ij}$. Cofactor $A_{ij} = (-1)^{i+j} M_{ij}$. Desarrollo por una fila o columna. Estrategia de elección de la fila/columna más conveniente.

### 2.2 Propiedades de los determinantes

#### 2.2.1 Propiedades elementales: fila nula, filas iguales, cambio de fila, factor común
`[Bloque: Números y Operaciones > Determinantes: regla de Sarrus; Bloque: Álgebra > Conjuntos de matrices, determinantes, matriz inversa]`
Las propiedades fundamentales de los determinantes. Uso estratégico para simplificar cálculos. Consecuencias sobre la invertibilidad de la matriz.

#### 2.2.2 Propiedad multiplicativa: det(AB) = det(A)·det(B)
`[Bloque: Álgebra (1.ª evaluación) > Conjuntos de matrices, determinantes, matriz inversa]`
Demostración intuitiva. Consecuencias: $\det(A^k) = [\det(A)]^k$, $\det(A^{-1}) = 1/\det(A)$. Aplicaciones en verificación de cálculos.

### 2.3 Matriz inversa mediante determinantes

#### 2.3.1 Concepto de matriz inversa: condición de existencia y unicidad
`[Bloque: Números y Operaciones > Inversa de una matriz cuadrada mediante determinantes]`
Definición: $A \cdot A^{-1} = A^{-1} \cdot A = I$. Condición necesaria y suficiente: $\det(A) \neq 0$. Matriz regular vs. singular.

#### 2.3.2 Cálculo de la matriz inversa mediante la matriz adjunta
`[Bloque: Números y Operaciones > Inversa de una matriz cuadrada mediante determinantes]`
Matriz de cofactores. Matriz adjunta $\text{adj}(A)$. Fórmula $A^{-1} = \frac{1}{\det A} \cdot \text{adj}(A)^T$. Cálculo completo para matrices 2×2 y 3×3.

#### 2.3.3 Verificación de la inversa y propiedades
`[Bloque: Álgebra (1.ª evaluación) > Conjuntos de matrices, determinantes, matriz inversa]`
Comprobación: $A \cdot A^{-1} = I$. Propiedades: $(AB)^{-1} = B^{-1}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$. Cálculo con herramientas tecnológicas.

---

## Capítulo 3. Sistemas de Ecuaciones Lineales {#cap3}

### 3.1 Representación matricial y rango

#### 3.1.1 Sistema lineal en forma matricial: $Ax = b$ y matriz ampliada
`[Bloque: Álgebra (1.ª evaluación) > Matrices para sistemas de ecuaciones lineales; Bloque: Álgebra > Sistemas de ecuaciones: modelización]`
Escritura matricial de sistemas de ecuaciones. Matriz de coeficientes $A$, vector de incógnitas $x$, vector de términos independientes $b$. Matriz ampliada $(A|b)$.

#### 3.1.2 Rango de una matriz: definición mediante determinantes
`[Bloque: Álgebra (1.ª evaluación) > Rango de una matriz con parámetros (determinantes, orden ≤3)]`
Definición de rango como el orden del mayor menor no nulo. Cálculo del rango para matrices de orden ≤ 3 mediante determinantes. Relación con la independencia lineal de filas/columnas.

#### 3.1.3 Rango de una matriz con parámetros: discusión según el valor del parámetro
`[Bloque: Álgebra (1.ª evaluación) > Rango de una matriz con parámetros (determinantes, orden ≤3)]`
Cálculo del rango en función de un parámetro $\lambda$. Valores del parámetro que anulan determinantes. Tabla de casos. Aplicaciones: modelos con parámetro libre (política económica, planificación).

### 3.2 Teorema de Rouché-Frobenius

#### 3.2.1 Enunciado del Teorema de Rouché-Frobenius
`[Bloque: Álgebra (1.ª evaluación) > Teorema de Rouché-Frobenius con parámetro]`
Enunciado completo: el sistema es compatible si y solo si $\text{rg}(A) = \text{rg}(A|b)$. Clasificación: SCD (rango = número de incógnitas), SCI (rango < número de incógnitas), SI (rangos distintos).

#### 3.2.2 Discusión de sistemas con parámetro mediante Rouché-Frobenius
`[Bloque: Álgebra (1.ª evaluación) > Teorema de Rouché-Frobenius con parámetro]`
Metodología completa: calcular $\det(A)$, analizar los casos, calcular $\text{rg}(A|b)$ para cada caso, clasificar el sistema. Ejemplos con parámetro $\lambda$ en matrices 3×3. Aplicaciones: modelización de equilibrios económicos bajo incertidumbre paramétrica.

### 3.3 Métodos de resolución

#### 3.3.1 Método de Gauss: escalonamiento de la matriz ampliada
`[Bloque: Álgebra (1.ª evaluación) > Matrices para sistemas de ecuaciones lineales]`
Operaciones elementales de fila. Reducción a forma escalonada. Resolución por sustitución regresiva. Aplicaciones: distribución de flujos en modelos input-output.

#### 3.3.2 Regla de Cramer para sistemas 2×2 y 3×3
`[Bloque: Álgebra (1.ª evaluación) > Regla de Cramer (hasta 3×3)]`
Enunciado de la Regla de Cramer. Fórmula $x_i = \det(A_i)/\det(A)$. Construcción de las matrices $A_i$. Limitaciones (solo SCD, computacionalmente costosa para órdenes altos). Ejemplos prácticos.

#### 3.3.3 Resolución mediante la matriz inversa: $x = A^{-1}b$
`[Bloque: Álgebra (1.ª evaluación) > Ecuaciones matriciales]`
Condición: $\det(A) \neq 0$. Proceso de cálculo. Ventaja para múltiples sistemas con la misma matriz de coeficientes. Aplicaciones: resolución de modelos económicos lineales.

#### 3.3.4 Ecuaciones matriciales: resolución de $AX = B$, $XA = B$, $AXB = C$
`[Bloque: Álgebra (1.ª evaluación) > Ecuaciones matriciales]`
Multiplicación por la inversa por la izquierda o por la derecha. Importancia del orden (no conmutatividad). Ejercicios de determinación de matrices desconocidas.

---

## Capítulo 4. Programación Lineal {#cap4}

### 4.1 Modelización de problemas lineales

#### 4.1.1 Variables de decisión, función objetivo y restricciones
`[Bloque: Álgebra (1.ª evaluación) > Programación lineal: modelización, región factible, vértices, solución óptima]`
Identificación de las variables de decisión en un problema de CCSS. Función objetivo (maximización de beneficio/minimización de coste). Formulación de restricciones como inecuaciones lineales. Restricciones de no negatividad.

#### 4.1.2 Ejemplos de modelización en contextos de CCSS
`[Bloque: Álgebra (1.ª evaluación) > Programación lineal: modelización]`
Problemas de producción, asignación de presupuesto, planificación de campañas publicitarias, distribución de recursos públicos. Traducción del enunciado verbal al modelo matemático.

### 4.2 Resolución gráfica

#### 4.2.1 Representación de restricciones: semiplanos y región factible
`[Bloque: Álgebra (1.ª evaluación) > Programación lineal: modelización, región factible, vértices, solución óptima]`
Representación gráfica de cada inecuación lineal. Intersección de semiplanos: polígono convexo de la región factible. Región factible acotada e ilimitada. Caso de región factible vacía.

#### 4.2.2 Cálculo de los vértices de la región factible
`[Bloque: Álgebra (1.ª evaluación) > Programación lineal: modelización, región factible, vértices, solución óptima]`
Intersección de pares de rectas frontera. Resolución algebraica. Verificación de que el vértice pertenece a la región factible.

#### 4.2.3 Teorema del vértice: enunciado y justificación intuitiva
`[Bloque: Álgebra (1.ª evaluación) > Programación lineal: modelización, región factible, vértices, solución óptima]`
Enunciado: el óptimo de una función lineal sobre una región factible convexa se alcanza en un vértice. Justificación mediante rectas de nivel (isocostes/isobeneficio).

#### 4.2.4 Determinación de la solución óptima: evaluación en vértices
`[Bloque: Álgebra (1.ª evaluación) > Programación lineal: modelización, región factible, vértices, solución óptima]`
Evaluación de la función objetivo en todos los vértices. Selección del máximo o mínimo. Casos especiales: solución infinita (región ilimitada) y solución no única (función objetivo paralela a una arista).

#### 4.2.5 Análisis de sensibilidad elemental: variación de los coeficientes
`[Bloque: Álgebra (1.ª evaluación) > Programación lineal: modelización]`
Efecto de cambios en los coeficientes de la función objetivo o en los valores del lado derecho de las restricciones. Interpretación económica: precio sombra, cuellos de botella.

---

## Capítulo 5. Límites, Continuidad y Derivabilidad {#cap5}

### 5.1 Límites: repaso y profundización

#### 5.1.1 Límite en un punto: cálculo y límites laterales (repaso CCSS I)
`[Bloque: Medida y Geometría (Cambio) > Límite en un punto: indeterminaciones (0/0, k/0, ∞–∞, 1∞)]`
Repaso del concepto de límite. Límites laterales y existencia del límite bilateral. Funciones a trozos y funciones con valor absoluto.

#### 5.1.2 Indeterminaciones en límites finitos: 0/0, k/0, ∞–∞, 1^∞
`[Bloque: Medida y Geometría (Cambio) > Límite en un punto: indeterminaciones (0/0, k/0, ∞–∞, 1∞)]`
Resolución de la indeterminación 0/0 por factorización y simplificación. Indeterminación k/0: límites infinitos. Indeterminación ∞–∞: racionalización. Indeterminación $1^\infty$: forma exponencial y número $e$.

#### 5.1.3 Límites en el infinito: jerarquía de infinitos y asíntotas
`[Bloque: Medida y Geometría (Cambio) > Límite en infinito, asíntotas (racionales y a trozos)]`
Comportamiento asintótico de polinomios, racionales, exponenciales y logarítmicos. Asíntotas horizontales, verticales y oblicuas de funciones racionales y a trozos. Cálculo completo.

#### 5.1.4 Regla de L'Hôpital: enunciado, condiciones y aplicación
`[Bloque: Medida y Geometría (Cambio) > Derivadas: interpretación, cálculo de límites, L'Hôpital]`
Condiciones de aplicación: forma 0/0 o ∞/∞. Enunciado del teorema. Aplicación iterada cuando persiste la indeterminación. Formas reducibles a 0/0 o ∞/∞ (0·∞, ∞–∞, 0^0, ∞^0, 1^∞). Ejemplos en análisis de modelos de crecimiento económico.

### 5.2 Continuidad

#### 5.2.1 Definición de continuidad: repaso, verificación y tipos de discontinuidades
`[Bloque: Medida y Geometría (Cambio) > Continuidad, discontinuidades]`
Condiciones de continuidad. Tipos de discontinuidades: evitable, salto finito, salto infinito. Representación gráfica. Ejemplos con funciones económicas a trozos.

#### 5.2.2 Continuidad de funciones a trozos: determinación de parámetros
`[Bloque: Medida y Geometría (Cambio) > Continuidad, discontinuidades]`
Proceso de estudio en los puntos de cambio de definición. Determinación de constantes para garantizar la continuidad. Ejemplos: funciones de coste, tarifa progresiva del IRPF.

#### 5.2.3 Teoremas sobre funciones continuas: Bolzano, Rolle y Valor Medio
`[Bloque: Medida y Geometría (Cambio) > Teoremas de Bolzano, Rolle, Valor Medio]`
Enunciado e hipótesis de cada teorema. Teorema de Bolzano (TVI): existencia de raíces. Teorema de Rolle: condiciones para $f'(c) = 0$. Teorema del Valor Medio de Lagrange: $f'(c) = [f(b)-f(a)]/(b-a)$. Aplicaciones en economía: existencia de puntos de equilibrio, tasa de cambio media.

### 5.3 Derivabilidad

#### 5.3.1 Definición de derivada: repaso del cociente incremental y la tasa instantánea
`[Bloque: Medida y Geometría (Cambio) > Derivadas: interpretación, cálculo de límites, L'Hôpital]`
Revisión de la definición por límite. Interpretación como pendiente de la tangente y como tasa de cambio instantánea en modelos económicos.

#### 5.3.2 Derivabilidad: derivadas laterales y condición de derivabilidad
`[Bloque: Medida y Geometría (Cambio) > Derivabilidad, relación derivabilidad-continuidad]`
Derivada por la derecha y por la izquierda. Condición: igualdad de derivadas laterales. Estudio en puntos angulosos (funciones a trozos, valor absoluto). Ejemplos detallados.

#### 5.3.3 Relación derivabilidad-continuidad: implicación y no reciprocidad
`[Bloque: Medida y Geometría (Cambio) > Derivabilidad, relación derivabilidad-continuidad]`
Derivabilidad $\Rightarrow$ continuidad. Contraejemplos de continuidad sin derivabilidad. Función de módulo en $x = 0$.

---

## Capítulo 6. Derivadas y Aplicaciones {#cap6}

### 6.1 Reglas de derivación

#### 6.1.1 Tabla de derivadas de funciones elementales: repaso completo
`[Bloque: Medida y Geometría (Cambio) > Derivación de funciones (todas las reglas + cadena)]`
Tabla exhaustiva: potencias, exponencial ($e^x$, $a^x$), logarítmica ($\ln x$, $\log_a x$), trigonométricas (introducción). Aplicación directa.

#### 6.1.2 Reglas algebraicas: derivada de suma, diferencia, producto y cociente
`[Bloque: Medida y Geometría (Cambio) > Derivación de funciones (todas las reglas + cadena)]`
Todas las reglas con demostraciones breves. Práctica intensiva con funciones complejas. Aplicaciones: funciones de coste total, ingreso, beneficio y sus marginales.

#### 6.1.3 Regla de la cadena: derivada de funciones compuestas
`[Bloque: Medida y Geometría (Cambio) > Derivación de funciones (todas las reglas + cadena)]`
$(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$. Casos frecuentes: $e^{g(x)}$, $\ln(g(x))$, $[g(x)]^n$, $a^{g(x)}$, $\log_a(g(x))$. Cadenas múltiples.

#### 6.1.4 Derivadas de orden superior: segunda derivada y concavidad
`[Bloque: Medida y Geometría (Cambio) > Extremos, puntos de inflexión, crecimiento/decrecimiento, concavidad/convexidad]`
Definición de $f''$, $f'''$, etc. Interpretación de $f''$: concavidad hacia arriba ($f'' > 0$) y hacia abajo ($f'' < 0$). Relación con la velocidad de cambio marginal en economía.

### 6.2 Recta tangente y normal

#### 6.2.1 Ecuación de la recta tangente en un punto
`[Bloque: Medida y Geometría (Cambio) > Recta tangente, cálculo de coeficientes]`
$y - f(x_0) = f'(x_0)(x - x_0)$. Cálculo de $f'(x_0)$ y construcción de la ecuación. Interpretación como aproximación lineal local.

#### 6.2.2 Ecuación de la recta normal y cálculo de coeficientes
`[Bloque: Medida y Geometría (Cambio) > Recta tangente, cálculo de coeficientes]`
Pendiente de la normal: $-1/f'(x_0)$. Ecuación de la recta normal. Aplicaciones: análisis de curvas de nivel en economía.

#### 6.2.3 Determinación de puntos de una curva con tangente dada
`[Bloque: Medida y Geometría (Cambio) > Recta tangente, cálculo de coeficientes]`
Búsqueda de $x_0$ tal que $f'(x_0) = m$ (pendiente dada) o que la tangente pase por un punto exterior. Resolución de la ecuación resultante.

### 6.3 Análisis de funciones con derivadas

#### 6.3.1 Monotonía: intervalos de crecimiento y decrecimiento mediante $f'$
`[Bloque: Medida y Geometría (Cambio) > Extremos, puntos de inflexión, crecimiento/decrecimiento, concavidad/convexidad]`
Criterio: $f'(x) > 0 \Rightarrow$ creciente; $f'(x) < 0 \Rightarrow$ decreciente. Tabla de signos de $f'$. Interpretación en modelos económicos: fases de crecimiento y decrecimiento.

#### 6.3.2 Extremos relativos: criterio de la primera derivada (cambio de signo)
`[Bloque: Medida y Geometría (Cambio) > Extremos, puntos de inflexión, crecimiento/decrecimiento, concavidad/convexidad]`
Puntos críticos ($f' = 0$, $f'$ no existe). Clasificación por el cambio de signo de $f'$: máximo relativo ($+ \to -$), mínimo relativo ($- \to +$), ni máximo ni mínimo.

#### 6.3.3 Extremos relativos: criterio de la segunda derivada
`[Bloque: Medida y Geometría (Cambio) > Extremos, puntos de inflexión, crecimiento/decrecimiento, concavidad/convexidad]`
$f''(x_0) < 0$: máximo; $f''(x_0) > 0$: mínimo; $f''(x_0) = 0$: inconcluso. Ventajas y limitaciones del criterio. Aplicaciones: función de beneficio.

#### 6.3.4 Concavidad, convexidad y puntos de inflexión
`[Bloque: Medida y Geometría (Cambio) > Extremos, puntos de inflexión, crecimiento/decrecimiento, concavidad/convexidad]`
Concavidad hacia arriba ($f'' > 0$) y hacia abajo ($f'' < 0$). Punto de inflexión: cambio de concavidad donde $f'' = 0$ (con verificación). Aplicaciones: punto de inflexión en la curva de Laffer, análisis de rendimientos decrecientes.

### 6.4 Optimización

#### 6.4.1 Optimización sin restricciones: máximos y mínimos absolutos
`[Bloque: Medida y Geometría (Cambio) > Optimización]`
Extremos absolutos en $\mathbb{R}$: solo extremos relativos + comportamiento en $\pm\infty$. Extremos absolutos en $[a, b]$: extremos relativos interiores + valores en los extremos del intervalo.

#### 6.4.2 Modelización y resolución de problemas de optimización en CCSS
`[Bloque: Medida y Geometría (Cambio) > Optimización]`
Método: definir variable, expresar la magnitud a optimizar como función de una variable, derivar e igualar a cero, verificar con $f''$ o tabla de signos. Aplicaciones: maximización del beneficio económico, minimización del coste de producción, maximización de ingresos fiscales (Laffer), precio óptimo de un bien.

#### 6.4.3 Elasticidad de la demanda: interpretación mediante derivadas
`[Bloque: Medida y Geometría (Cambio) > Derivadas: interpretación]`
Definición de elasticidad precio de la demanda $\varepsilon = (dQ/dp) \cdot (p/Q)$. Demanda elástica, inelástica y unitaria. Relación con el ingreso marginal. Aplicación de la derivada en análisis económico avanzado.

---

## Capítulo 7. Representación de Funciones {#cap7}

### 7.1 Estudio analítico completo de funciones

#### 7.1.1 Dominio: cálculo para funciones polinómicas, racionales, irracionales, exponenciales, logarítmicas y a trozos
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones (polinómicas, racionales, exponenciales, logarítmicas, a trozos)]`
Método sistemático para cada tipo de función. Dominio de funciones a trozos. Expresión en notación de intervalos.

#### 7.1.2 Simetría: funciones pares, impares y sin simetría
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones]`
Verificación algebraica: $f(-x) = f(x)$ (par), $f(-x) = -f(x)$ (impar). Implicaciones gráficas.

#### 7.1.3 Puntos de corte con los ejes
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones]`
Corte con OY: $f(0)$. Cortes con OX: raíces de $f(x) = 0$. Resolución de ecuaciones asociadas.

#### 7.1.4 Asíntotas: verticales, horizontales y oblicuas
`[Bloque: Medida y Geometría (Cambio) > Límite en infinito, asíntotas (racionales y a trozos)]`
Cálculo sistemático de todos los tipos de asíntotas. Funciones racionales y funciones a trozos. Representación en el esquema de la función.

#### 7.1.5 Monotonía y extremos relativos mediante la primera derivada
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones; Medida y Geometría (Cambio) > Extremos, crecimiento/decrecimiento]`
Tabla de signos de $f'$. Puntos críticos. Clasificación de extremos. Intervalos de crecimiento y decrecimiento.

#### 7.1.6 Concavidad, convexidad y puntos de inflexión mediante la segunda derivada
`[Bloque: Medida y Geometría (Cambio) > Extremos, puntos de inflexión, concavidad/convexidad]`
Tabla de signos de $f''$. Puntos de inflexión. Intervalos de concavidad y convexidad.

#### 7.1.7 Representación gráfica: síntesis y boceto final
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones]`
Integración de todos los elementos del estudio. Construcción del boceto con escala adecuada. Coherencia entre el análisis analítico y la gráfica obtenida.

### 7.2 Tipos de funciones — estudio completo

#### 7.2.1 Funciones polinómicas de grado 3 y superior: estudio analítico completo
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones (polinómicas)]`
Dominio $\mathbb{R}$, sin asíntotas. Análisis completo con derivadas. Aplicaciones: curvas de beneficio cúbicas, funciones de coste total.

#### 7.2.2 Funciones racionales: estudio analítico completo
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones (racionales)]`
Dominio, puntos de corte, asíntotas verticales y horizontales/oblicuas, monotonía y extremos, concavidad. Ejemplos: productividad media, coste medio.

#### 7.2.3 Funciones exponenciales y logarítmicas: estudio analítico completo
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones (exponenciales, logarítmicas)]`
Estudio de $f(x) = e^{g(x)}$ y $f(x) = \ln(g(x))$ con $g$ polinómica. Asíntota horizontal. Aplicaciones: modelos de crecimiento económico.

#### 7.2.4 Funciones a trozos: estudio analítico completo (continuidad, derivabilidad, representación)
`[Bloque: Álgebra (1.ª evaluación) > Representación y estudio de funciones (a trozos)]`
Análisis en cada tramo. Continuidad y derivabilidad en los puntos de cambio. Representación global. Aplicaciones: funciones de coste con economías de escala, tarifa progresiva.

---

## Capítulo 8. Integrales {#cap8}

### 8.1 Primitivas e integración indefinida

#### 8.1.1 Concepto de primitiva: definición y no unicidad
`[Bloque: Medida y Geometría (Cambio) > Primitivas inmediatas simples y compuestas, Regla de Barrow]`
Definición: $F$ es primitiva de $f$ si $F' = f$. Familia de primitivas $F(x) + C$. Unicidad salvo constante de integración. Significado en contextos de CCSS: función de coste total a partir del coste marginal.

#### 8.1.2 Tabla de primitivas inmediatas básicas
`[Bloque: Medida y Geometría (Cambio) > Primitivas inmediatas simples y compuestas]`
Tabla completa: potencias $x^n$ ($n \neq -1$), $1/x$, $e^x$, $a^x$, $\ln|x|$, funciones trigonométricas básicas. Aplicación directa de la tabla.

#### 8.1.3 Primitivas inmediatas compuestas: regla de la cadena inversa
`[Bloque: Medida y Geometría (Cambio) > Primitivas inmediatas simples y compuestas]`
Integración de $f(ax+b)$: corrección por el factor $1/a$. Casos: $[g(x)]^n g'(x)$, $e^{g(x)} g'(x)$, $g'(x)/g(x)$. Ejemplos prácticos con funciones compuestas.

#### 8.1.4 Integración por partes: $\int u\, dv = uv - \int v\, du$ (introducción)
`[Bloque: Medida y Geometría (Cambio) > Primitivas inmediatas simples y compuestas]`
Fórmula de integración por partes. Elección de $u$ y $dv$ (regla ILATE). Aplicación a $\int x e^x dx$, $\int x \ln x\, dx$, etc. Casos relevantes en CCSS.

### 8.2 Integral definida

#### 8.2.1 Integral definida como límite de sumas: sumas de Riemann (introducción intuitiva)
`[Bloque: Medida y Geometría (Cambio) > Integral definida como área bajo curva]`
Motivación: área bajo una curva como suma de rectángulos. Partición del intervalo. Suma de Riemann. Paso al límite. Aplicaciones: área entre curvas de oferta y demanda (excedente del consumidor/productor).

#### 8.2.2 Integral definida como área bajo la curva: interpretación geométrica
`[Bloque: Medida y Geometría (Cambio) > Integral definida como área bajo curva]`
$\int_a^b f(x)\, dx$ como área con signo. Área positiva (función positiva) y negativa (función negativa). Área entre dos curvas. Aplicaciones: excedente del consumidor y del productor.

#### 8.2.3 Regla de Barrow: Teorema Fundamental del Cálculo
`[Bloque: Medida y Geometría (Cambio) > Primitivas inmediatas simples y compuestas, Regla de Barrow]`
Enunciado del Teorema Fundamental del Cálculo. Regla de Barrow: $\int_a^b f(x)\, dx = F(b) - F(a)$. Condición: $f$ continua en $[a, b]$. Proceso de cálculo.

#### 8.2.4 Propiedades de la integral definida
`[Bloque: Medida y Geometría (Cambio) > Integral definida como área bajo curva]`
Linealidad. Aditividad respecto al intervalo. Cambio de signo al invertir los límites. Valor cero cuando $a = b$. Comparación de integrales. Aplicaciones a problemas de CCSS.

### 8.3 Aplicaciones de la integral definida

#### 8.3.1 Cálculo de áreas bajo una curva (función positiva en $[a,b]$)
`[Bloque: Medida y Geometría (Cambio) > Integral definida como área bajo curva]`
Método sistemático: determinar raíces, calcular integral con signo adecuado para cada tramo. Ejemplos con funciones polinómicas y racionales.

#### 8.3.2 Área entre dos curvas: intersección, cálculo y aplicaciones
`[Bloque: Medida y Geometría (Cambio) > Integral definida como área bajo curva]`
$A = \int_a^b [f(x) - g(x)]\, dx$ con $f \geq g$ en $[a,b]$. Localización de los puntos de intersección. Aplicaciones: excedente del consumidor (área entre curva de demanda y precio de mercado) y excedente del productor.

#### 8.3.3 Excedente del consumidor y del productor: aplicación económica
`[Bloque: Medida y Geometría (Cambio) > Integral definida como área bajo curva]`
Definición económica del excedente del consumidor y del productor. Modelo de oferta y demanda. Cálculo mediante integrales definidas. Interpretación del área como bienestar.

---

## Capítulo 9. Probabilidad {#cap9}

### 9.1 Fundamentos de probabilidad

#### 9.1.1 Revisión de las interpretaciones de la probabilidad: clásica, frecuentista y subjetiva
`[Bloque: Medida y Geometría (Cambio) > Probabilidad: interpretaciones subjetiva, clásica, frecuentista]`
Repaso de las tres perspectivas. Aplicaciones: probabilidad frecuentista en estudios de mercado, clásica en sorteos, subjetiva en predicciones electorales (modelos bayesianos).

#### 9.1.2 Repaso del álgebra de sucesos, Laplace y axiomas de Kolmogorov
`[Bloque: Estadística (2.ª evaluación) > Probabilidad condicionada e independencia]`
Consolidación de los fundamentos de CCSS I. Verificación de coherencia axiomática. Propiedades derivadas.

### 9.2 Probabilidad condicionada e independencia

#### 9.2.1 Probabilidad condicionada: definición, cálculo y actualización
`[Bloque: Estadística (2.ª evaluación) > Probabilidad condicionada e independencia]`
$P(A|B) = P(A \cap B)/P(B)$. Reducción del espacio muestral. Actualización de probabilidades con información. Tablas de contingencia para calcular probabilidades condicionadas.

#### 9.2.2 Tablas de contingencia: lectura e interpretación probabilística
`[Bloque: Estadística (2.ª evaluación) > Diagramas de árbol, tablas de contingencia]`
Construcción e interpretación de tablas de doble entrada. Probabilidades marginales, conjuntas y condicionadas a partir de la tabla. Aplicaciones: estudios de opinión, encuestas de salud.

#### 9.2.3 Independencia estadística: definición, criterio y verificación
`[Bloque: Estadística (2.ª evaluación) > Probabilidad condicionada e independencia]`
Criterio: $P(A|B) = P(A)$ o equivalentemente $P(A \cap B) = P(A) \cdot P(B)$. Verificación con tablas de contingencia. Importancia en el diseño de encuestas y experimentos.

#### 9.2.4 Diagramas de árbol para experimentos compuestos
`[Bloque: Estadística (2.ª evaluación) > Diagramas de árbol, tablas de contingencia]`
Construcción de árboles de dos y tres etapas. Regla del producto en cada rama. Suma de probabilidades de los sucesos favorables (caminos del árbol). Aplicaciones: muestreo con y sin reposición.

### 9.3 Probabilidad total y Bayes

#### 9.3.1 Partición del espacio muestral y sistema completo de sucesos
`[Bloque: Estadística (2.ª evaluación) > Probabilidad total y Bayes]`
Definición de sistema de partición $\{H_1, \ldots, H_k\}$. Condiciones de exhaustividad e incompatibilidad mutua. Ejemplos: segmentos de la población.

#### 9.3.2 Teorema de la probabilidad total: fórmula y aplicaciones
`[Bloque: Estadística (2.ª evaluación) > Probabilidad total y Bayes]`
$P(A) = \sum_i P(A|H_i) \cdot P(H_i)$. Proceso de cálculo con árbol o tabla. Aplicaciones: tasa global de desempleo a partir de tasas por sector, análisis de riesgo de crédito estratificado.

#### 9.3.3 Teorema de Bayes: inversión de la probabilidad condicionada
`[Bloque: Estadística (2.ª evaluación) > Probabilidad total y Bayes]`
$P(H_i|A) = \frac{P(A|H_i) \cdot P(H_i)}{P(A)}$. Probabilidades a priori y a posteriori. Interpretación bayesiana. Aplicaciones: diagnóstico epidemiológico, fiabilidad de encuestas estratificadas, análisis de sondeos electorales.

---

## Capítulo 10. Distribuciones de Probabilidad {#cap10}

### 10.1 Variable aleatoria: repaso y profundización

#### 10.1.1 Variables aleatorias discretas: función de masa, distribución acumulada, esperanza y varianza
`[Bloque: Estadística (2.ª evaluación) > Distribuciones binomial y normal]`
Repaso de los conceptos de CCSS I. Cálculo de $E(X)$ y $Var(X)$. Propiedades de la esperanza y la varianza.

#### 10.1.2 Variables aleatorias continuas: función de densidad y distribución acumulada
`[Bloque: Estadística (2.ª evaluación) > Distribuciones binomial y normal]`
Concepto de función de densidad $f(x) \geq 0$ con $\int_{-\infty}^{+\infty} f(x)\, dx = 1$. Probabilidad como área. Función de distribución $F(x) = P(X \leq x)$.

### 10.2 Distribución binomial

#### 10.2.1 Distribución binomial $B(n, p)$: condiciones, función de masa y parámetros
`[Bloque: Estadística (2.ª evaluación) > Distribuciones binomial y normal]`
Condiciones del modelo de Bernoulli. Función de masa $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$. Parámetros $n$ y $p$. Aplicaciones: modelización de proporciones muestrales (intención de voto, aceptación de producto).

#### 10.2.2 Esperanza y varianza de la binomial: $E(X) = np$, $Var(X) = np(1-p)$
`[Bloque: Estadística (2.ª evaluación) > Distribuciones binomial y normal]`
Fórmulas. Interpretación. Cálculo de probabilidades exactas y acumuladas con calculadora o tabla. Ejercicios con contextos de CCSS.

#### 10.2.3 Cálculo de probabilidades acumuladas con la binomial
`[Bloque: Estadística (2.ª evaluación) > Distribuciones binomial y normal]`
$P(X \leq k)$, $P(X \geq k)$, $P(X = k)$ con herramientas tecnológicas. Uso de tablas de la binomial. Ejercicios: probabilidad de que en una muestra electoral haya al menos $k$ personas a favor de un candidato.

### 10.3 Distribución normal

#### 10.3.1 Distribución normal $N(\mu, \sigma)$: parámetros, campana de Gauss y propiedades
`[Bloque: Estadística (2.ª evaluación) > Distribuciones binomial y normal]`
Función de densidad (forma analítica). Campana de Gauss: simetría respecto a $\mu$, puntos de inflexión en $\mu \pm \sigma$. Regla empírica 68-95-99.7. Aplicaciones: distribución de rentas, errores de muestreo.

#### 10.3.2 Tipificación: transformación a $N(0,1)$ y uso de tablas
`[Bloque: Estadística (2.ª evaluación) > Distribuciones binomial y normal]`
$Z = (X - \mu)/\sigma$. Interpretación de $Z$. Uso de la tabla $\Phi(z)$. Cálculo de probabilidades: $P(X < a)$, $P(X > a)$, $P(a < X < b)$. Cálculo inverso: dado $p$, encontrar $x$.

#### 10.3.3 Cálculo de probabilidades con la normal: ejercicios completos
`[Bloque: Estadística (2.ª evaluación) > Distribuciones binomial y normal]`
Serie de ejercicios de aplicación en contextos de CCSS: distribución de salarios, notas de exámenes, tiempos de espera en servicios públicos. Uso de calculadora científica.

### 10.4 Aproximación de la binomial a la normal

#### 10.4.1 Condiciones de la aproximación: $np \geq 5$ y $n(1-p) \geq 5$
`[Bloque: Estadística (2.ª evaluación) > Aproximación binomial a normal]`
Justificación del teorema central del límite (intuitivo). Condiciones suficientes para la aproximación. Parámetros de la normal aproximante: $\mu = np$, $\sigma = \sqrt{np(1-p)}$.

#### 10.4.2 Corrección de continuidad en la aproximación
`[Bloque: Estadística (2.ª evaluación) > Aproximación binomial a normal]`
Justificación de la corrección $\pm 0.5$. Aplicación en el cálculo de $P(X = k)$, $P(X \leq k)$, $P(X \geq k)$. Comparación con el resultado exacto de la binomial.

#### 10.4.3 Problemas de aproximación binomial-normal en contextos electorales y sociales
`[Bloque: Estadística (2.ª evaluación) > Aproximación binomial a normal]`
Ejercicios completos: en una muestra de 1000 votantes donde el 42% apoya al partido A, ¿cuál es la probabilidad de que haya entre 400 y 440 simpatizantes en la muestra? Otros contextos sociales.

---

## Capítulo 11. Inferencia Estadística {#cap11}

### 11.1 Fundamentos de inferencia

#### 11.1.1 Población y muestra: parámetros poblacionales y estadísticos muestrales
`[Bloque: Estadística (2.ª evaluación) > Inferencia: población y muestra, parámetros poblacionales/muestrales]`
Distinción entre parámetros ($\mu, \sigma, p$) y sus estimadores ($\bar{x}, s, \hat{p}$). Importancia de la inferencia cuando no se puede estudiar la población completa. Aplicaciones: encuestas electorales, estudios de mercado.

#### 11.1.2 Técnicas de muestreo: aleatorio simple, sistemático, estratificado y por conglomerados
`[Bloque: Estadística (2.ª evaluación) > Técnicas de muestreo, representatividad]`
Descripción detallada de cada método. Criterios para elegir el tipo de muestreo. Representatividad y posibles sesgos. Ficha técnica de una encuesta: qué debe incluir.

#### 11.1.3 Ficha técnica de encuesta: elementos y lectura crítica
`[Bloque: Estadística (2.ª evaluación) > Ficha técnica de encuesta]`
Elementos de la ficha técnica: universo, tamaño muestral, método de muestreo, margen de error, nivel de confianza, fecha y organismo. Lectura e interpretación crítica de fichas técnicas de encuestas reales (CIS, Metroscopia, etc.).

### 11.2 Distribuciones muestrales

#### 11.2.1 Distribución de la media muestral $\bar{X}$: Teorema Central del Límite
`[Bloque: Estadística (2.ª evaluación) > Distribución de la media y proporción muestrales]`
Enunciado del TCL: si $n$ es suficientemente grande, $\bar{X} \sim N(\mu, \sigma/\sqrt{n})$ aproximadamente, independientemente de la distribución de la población. Error típico $\sigma/\sqrt{n}$. Implicaciones para la estimación.

#### 11.2.2 Distribución de la proporción muestral $\hat{P}$
`[Bloque: Estadística (2.ª evaluación) > Distribución de la media y proporción muestrales]`
Si $X \sim B(n, p)$ con $n$ grande, $\hat{P} = X/n \sim N(p, \sqrt{p(1-p)/n})$ aproximadamente. Condiciones de aplicación. Interpretación del error típico de la proporción.

### 11.3 Estimación puntual

#### 11.3.1 Concepto de estimador y propiedades deseables: insesgadez y eficiencia
`[Bloque: Estadística (2.ª evaluación) > Estimación puntual y por intervalo]`
Definición de estimador puntual. Insesgadez: $E(\hat{\theta}) = \theta$. Eficiencia: menor varianza entre los insesgados. $\bar{x}$ como estimador insesgado de $\mu$. $\hat{p}$ como estimador insesgado de $p$.

#### 11.3.2 Estimación puntual de la media y de la proporción
`[Bloque: Estadística (2.ª evaluación) > Estimación puntual y por intervalo]`
Cálculo de $\bar{x}$ y $\hat{p}$ a partir de datos muestrales. Interpretación. Limitación de la estimación puntual: no cuantifica la incertidumbre.

### 11.4 Estimación por intervalos de confianza

#### 11.4.1 Concepto de intervalo de confianza: nivel de confianza y nivel de significación
`[Bloque: Estadística (2.ª evaluación) > Intervalos de confianza (distribución normal): construcción, análisis]`
Definición: el IC es aleatorio; el parámetro es fijo. Interpretación frecuentista: el $(1-\alpha) \cdot 100\%$ de los intervalos construidos en repetidas muestras contendrán al parámetro. Nivel de confianza habituales: 90%, 95%, 99%.

#### 11.4.2 Valor crítico $z_{\alpha/2}$: obtención de la tabla de la normal
`[Bloque: Estadística (2.ª evaluación) > Intervalos de confianza (distribución normal): construcción, análisis]`
Definición de $z_{\alpha/2}$ como cuantil de la normal estándar. Valores habituales: $z_{0.025} = 1.96$ (95%), $z_{0.05} = 1.645$ (90%), $z_{0.005} = 2.576$ (99%). Obtención a partir de la tabla.

#### 11.4.3 Intervalo de confianza para la media con $\sigma$ conocida
`[Bloque: Estadística (2.ª evaluación) > Intervalo de confianza para la media (desviación típica conocida)]`
$IC_{1-\alpha}(\mu) = \left(\bar{x} - z_{\alpha/2} \dfrac{\sigma}{\sqrt{n}},\; \bar{x} + z_{\alpha/2} \dfrac{\sigma}{\sqrt{n}}\right)$. Condición: $\sigma$ conocida o $n$ grande. Construcción paso a paso. Interpretación del resultado. Aplicaciones: estimación del ingreso medio de una población.

#### 11.4.4 Intervalo de confianza para una proporción poblacional
`[Bloque: Estadística (2.ª evaluación) > Intervalos de confianza (distribución normal): construcción, análisis]`
$IC_{1-\alpha}(p) = \left(\hat{p} - z_{\alpha/2} \sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}},\; \hat{p} + z_{\alpha/2} \sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}\right)$. Condiciones de aplicación ($n$ grande, $n\hat{p} \geq 5$). Aplicaciones: estimación de la intención de voto, proporción de usuarios satisfechos.

#### 11.4.5 Margen de error de una estimación
`[Bloque: Estadística (2.ª evaluación) > Relación confianza-error-tamaño muestral]`
Definición: $E = z_{\alpha/2} \cdot \sigma/\sqrt{n}$ (para la media) o $E = z_{\alpha/2} \cdot \sqrt{\hat{p}(1-\hat{p})/n}$ (para la proporción). Lectura del margen de error en informes de encuestas. Relación entre el margen de error, el nivel de confianza y el tamaño muestral.

### 11.5 Tamaño muestral

#### 11.5.1 Tamaño muestral mínimo para una media con error máximo admisible
`[Bloque: Estadística (2.ª evaluación) > Tamaño muestral mínimo]`
Despeje de $n$ en la fórmula del margen de error: $n \geq \left(\dfrac{z_{\alpha/2} \cdot \sigma}{E}\right)^2$. Redondeo siempre hacia arriba. Aplicaciones: determinación del tamaño de muestra en estudios de CCSS.

#### 11.5.2 Tamaño muestral mínimo para una proporción con error máximo admisible
`[Bloque: Estadística (2.ª evaluación) > Tamaño muestral mínimo]`
$n \geq \left(\dfrac{z_{\alpha/2}}{E}\right)^2 p(1-p)$. Caso más desfavorable $p = 0.5$: $n \geq \left(\dfrac{z_{\alpha/2}}{2E}\right)^2$. Aplicaciones: encuestas electorales, estudios de satisfacción ciudadana.

#### 11.5.3 Relación confianza-error-tamaño muestral: análisis e interpretación
`[Bloque: Estadística (2.ª evaluación) > Relación confianza-error-tamaño muestral]`
Efectos de aumentar el nivel de confianza (aumenta $n$ o aumenta el error). Efecto de reducir el margen de error (aumenta $n$ o disminuye el nivel de confianza). Análisis coste-precisión en el diseño de encuestas. Lectura crítica de fichas técnicas reales.

### 11.6 Regresión lineal (en el contexto de inferencia)

#### 11.6.1 Repaso de la regresión lineal: rectas de regresión y coeficiente de determinación
`[Bloque: Estadística (2.ª evaluación) > Regresión lineal]`
Consolidación de los contenidos de CCSS I sobre regresión lineal. Rectas de regresión de $Y/X$ y de $X/Y$. Coeficiente de determinación $R^2$ y su interpretación como bondad del ajuste.

#### 11.6.2 Predicción e interpolación a partir del modelo de regresión
`[Bloque: Estadística (2.ª evaluación) > Regresión lineal]`
Uso de la recta de regresión para predecir valores. Extrapolación y sus riesgos. Interpretación de los coeficientes de regresión en términos sustantivos de CCSS. Aplicaciones: predicción del consumo a partir del ingreso, estimación de la participación electoral.

---

*Fin del índice — Matemáticas Aplicadas a las Ciencias Sociales II (2.º Bachillerato)*
*Comunidad de Madrid — Decreto 64/2022 (LOMLOE)*
