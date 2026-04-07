# Ejercicios — Capítulos 6 y 7: Límites, Continuidad, Derivadas y Aplicaciones

**Asignatura:** Matemáticas II — 2.º Bachillerato (Ciencias y Tecnología)  
**Comunidad:** Comunidad de Madrid  
**Marco normativo:** Decreto 64/2022 (LOMLOE) / EVAU Madrid  
**Capítulos:** 6 (Límites y Continuidad) · 7 (Derivadas y Aplicaciones)

> **Estructura por subsección:** 1 Ejercicio Resuelto · 2 Nivel Básico · 2 Nivel Intermedio · 1 Nivel EVAU · 2 Test de Opción Múltiple

---

# Matemáticas II — Ejercicios Capítulos 6 y 7

**Curso:** 2.º Bachillerato — Ciencias y Tecnología  
**Comunidad:** Comunidad de Madrid  
**Capítulos:** 6 (Límites y Continuidad) · 7 (Derivadas y Aplicaciones)  
**Marco normativo:** Decreto 64/2022 (LOMLOE) / Programación FUHEM 2025-26

> **Estructura de cada subsección:** 1 Ejercicio Resuelto · 2 Nivel Básico · 2 Nivel Intermedio · 1 Nivel EVAU · 2 Test de Opción Múltiple

---

# CAPÍTULO 6. LÍMITES Y CONTINUIDAD

---

## 6.1 Límite de una función en un punto

---

#### 6.1.1 Concepto intuitivo de límite: aproximación gráfica y tabular

**Ejercicio Resuelto**

Estudia el límite de $f(x) = \dfrac{x^2 - 1}{x - 1}$ cuando $x \to 1$ mediante una tabla de valores.

**Solución:**

Observamos que $x = 1$ no pertenece al dominio de $f$ (el denominador se anula). Sin embargo, podemos aproximarnos a $x = 1$ por ambos lados:

| $x$ | $0{,}9$ | $0{,}99$ | $0{,}999$ | $\to 1 \leftarrow$ | $1{,}001$ | $1{,}01$ | $1{,}1$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $1{,}9$ | $1{,}99$ | $1{,}999$ | $\to ?$ | $2{,}001$ | $2{,}01$ | $2{,}1$ |

Los valores se acercan a $2$ por ambos lados. Podemos confirmar algebraicamente:

$$f(x) = \frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1} = x + 1 \quad (x \neq 1)$$

Por tanto: $\displaystyle\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1}(x+1) = 2$

La tabla confirma el resultado: conforme $x \to 1$, $f(x) \to 2$, aunque $f(1)$ no existe.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Completa la siguiente tabla para $f(x) = \dfrac{x^2 - 4}{x - 2}$ y determina $\displaystyle\lim_{x \to 2} f(x)$.

   | $x$ | $1{,}9$ | $1{,}99$ | $2{,}01$ | $2{,}1$ |
   |---|---|---|---|---|
   | $f(x)$ | ? | ? | ? | ? |

   > **Solución:** Simplificando: $\dfrac{x^2-4}{x-2} = \dfrac{(x-2)(x+2)}{x-2} = x+2$ para $x \neq 2$.  
   > $f(1{,}9)=3{,}9$; $f(1{,}99)=3{,}99$; $f(2{,}01)=4{,}01$; $f(2{,}1)=4{,}1$.  
   > $\displaystyle\lim_{x \to 2} f(x) = 4$

2. Observando la gráfica de $f(x) = x^2 - 3x + 2$, determina intuitivamente $\displaystyle\lim_{x \to 1} f(x)$ y compruébalo por sustitución directa.

   > **Solución:** Como $f$ es un polinomio (continua en todo $\mathbb{R}$), podemos sustituir directamente:  
   > $\displaystyle\lim_{x \to 1} (x^2 - 3x + 2) = 1 - 3 + 2 = 0$.  
   > Nótese que $f(1) = 0$, luego el límite coincide con el valor de la función.

**Nivel Intermedio:**

3. Construye una tabla de valores para $g(x) = \dfrac{\sin x}{x}$ con $x$ en radianes, aproximándote a $x = 0$. ¿Qué límite sugiere la tabla?

   > **Solución:** 
   >
   > | $x$ | $\pm 0{,}5$ | $\pm 0{,}1$ | $\pm 0{,}01$ | $\pm 0{,}001$ |
   > |---|---|---|---|---|
   > | $\sin(x)/x$ | $0{,}9589$ | $0{,}9983$ | $0{,}999983$ | $\approx 1$ |
   >
   > La tabla sugiere $\displaystyle\lim_{x \to 0} \dfrac{\sin x}{x} = 1$.  
   > Este es el límite trigonométrico fundamental, fundamental en el cálculo de derivadas.

4. Para $h(x) = \left(1 + \dfrac{1}{x}\right)^x$, aproxima $\displaystyle\lim_{x \to +\infty} h(x)$ tabulando valores $x = 10, 100, 1000, 10000$.

   > **Solución:**
   >
   > | $x$ | $10$ | $100$ | $1000$ | $10000$ |
   > |---|---|---|---|---|
   > | $h(x)$ | $2{,}5937$ | $2{,}7048$ | $2{,}7169$ | $2{,}7181$ |
   >
   > La tabla sugiere $\displaystyle\lim_{x \to +\infty}\left(1 + \frac{1}{x}\right)^x = e \approx 2{,}71828$.  
   > Este es el límite que define el número $e$ de Euler.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \dfrac{x^3 - 8}{x^2 - 4}$.

   a) Determina el dominio de $f$.  
   b) Construye una tabla de valores para $x \to 2$ e indica qué valor sugiere el límite.  
   c) Calcula $\displaystyle\lim_{x \to 2} f(x)$ algebraicamente y compara con la tabla.

   > **Solución:**
   >
   > **a)** El denominador se anula en $x^2 - 4 = 0 \Rightarrow x = \pm 2$.  
   > $\text{Dom}(f) = \mathbb{R} \setminus \{-2, 2\}$
   >
   > **b)** Tabla para $x \to 2$:
   >
   > | $x$ | $1{,}9$ | $1{,}99$ | $2{,}01$ | $2{,}1$ |
   > |---|---|---|---|---|
   > | $f(x)$ | $1{,}4262$ | $1{,}4925$ | $1{,}5075$ | $1{,}5732$ |
   >
   > La tabla sugiere $\displaystyle\lim_{x \to 2} f(x) \approx 1{,}5 = \dfrac{3}{2}$.
   >
   > **c)** Factorizando: $x^3 - 8 = (x-2)(x^2+2x+4)$ y $x^2 - 4 = (x-2)(x+2)$:
   >
   > $$\lim_{x \to 2} \frac{x^3 - 8}{x^2 - 4} = \lim_{x \to 2} \frac{(x-2)(x^2+2x+4)}{(x-2)(x+2)} = \lim_{x \to 2} \frac{x^2+2x+4}{x+2} = \frac{4+4+4}{4} = \frac{12}{4} = 3$$
   >
   > **Corrección:** La tabla da $\approx 1{,}5$ porque hay un error en el cálculo numérico; verifiquemos: $f(1{,}9) = \dfrac{1{,}9^3-8}{1{,}9^2-4} = \dfrac{6{,}859-8}{3{,}61-4} = \dfrac{-1{,}141}{-0{,}39} \approx 2{,}926$. La tabla corregida da valores $\to 3$, confirmando el resultado algebraico $\displaystyle\lim_{x \to 2} f(x) = 3$.

**Test de Opción Múltiple**

6. Para $f(x) = \dfrac{x^2 - 9}{x - 3}$, el valor de $\displaystyle\lim_{x \to 3} f(x)$ es:
   - a) $0$
   - b) $3$
   - c) $6$
   - d) No existe

   > **Respuesta correcta: c)** $\dfrac{x^2-9}{x-3} = \dfrac{(x-3)(x+3)}{x-3} = x+3 \to 3+3 = 6$ cuando $x \to 3$.

7. Una tabla de valores muestra que $f(x) \to 5$ cuando $x \to 2^-$ y $f(x) \to 5$ cuando $x \to 2^+$. Se puede concluir que:
   - a) $f(2) = 5$
   - b) $\displaystyle\lim_{x \to 2} f(x) = 5$
   - c) $f$ es continua en $x = 2$
   - d) $f$ es derivable en $x = 2$

   > **Respuesta correcta: b)** La igualdad de los límites laterales garantiza la existencia del límite global en $x = 2$. Sin información sobre $f(2)$, no podemos afirmar continuidad (opción c es incorrecta).

---

#### 6.1.2 Definición formal de límite (ε-δ, nivel introductorio)

**Ejercicio Resuelto**

Demuestra mediante la definición épsilon-delta que $\displaystyle\lim_{x \to 3}(2x - 1) = 5$.

**Solución:**

Queremos demostrar que dado $\varepsilon > 0$, existe $\delta > 0$ tal que:
$$0 < |x - 3| < \delta \Rightarrow |(2x-1) - 5| < \varepsilon$$

**Análisis previo:** Simplificamos la condición de llegada:
$$|(2x-1) - 5| = |2x - 6| = 2|x - 3|$$

Si exigimos $2|x-3| < \varepsilon$, entonces basta con que $|x-3| < \dfrac{\varepsilon}{2}$.

**Elección de $\delta$:** Tomamos $\delta = \dfrac{\varepsilon}{2}$.

**Verificación:** Si $0 < |x-3| < \delta = \dfrac{\varepsilon}{2}$, entonces:
$$|(2x-1)-5| = 2|x-3| < 2 \cdot \frac{\varepsilon}{2} = \varepsilon \checkmark$$

Por tanto, queda demostrado que $\displaystyle\lim_{x \to 3}(2x-1) = 5$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Usando la definición intuitiva, justifica que $\displaystyle\lim_{x \to 2}(3x + 1) = 7$.

   > **Solución:** Para $\varepsilon > 0$ dado, analizamos: $|(3x+1) - 7| = |3x - 6| = 3|x-2|$.  
   > Necesitamos $3|x-2| < \varepsilon$, es decir, $|x-2| < \dfrac{\varepsilon}{3}$.  
   > Tomamos $\delta = \dfrac{\varepsilon}{3}$. Entonces si $|x-2| < \delta$: $|(3x+1)-7| = 3|x-2| < 3\cdot\dfrac{\varepsilon}{3} = \varepsilon$. ✓

2. ¿Es correcto afirmar que $\displaystyle\lim_{x \to 0} x^2 = 0$? Justifica tomando $\varepsilon = 0{,}01$ y encontrando un $\delta$ apropiado.

   > **Solución:** Necesitamos $|x^2 - 0| = x^2 < 0{,}01$, lo que equivale a $|x| < \sqrt{0{,}01} = 0{,}1$.  
   > Tomando $\delta = 0{,}1$: si $|x| < 0{,}1$ entonces $x^2 < 0{,}01 = \varepsilon$. ✓  
   > En general $\delta = \sqrt{\varepsilon}$ funciona para cualquier $\varepsilon > 0$.

**Nivel Intermedio:**

3. Demuestra con la definición $\varepsilon$-$\delta$ que $\displaystyle\lim_{x \to 1}(x^2 + 2x) = 3$.

   > **Solución:** Analizamos: $|(x^2+2x) - 3| = |x^2+2x-3| = |(x-1)(x+3)| = |x-1|\cdot|x+3|$.  
   > Acotamos $|x+3|$: si restringimos $|x-1| < 1$, entonces $0 < x < 2$, por lo que $3 < x+3 < 5$, luego $|x+3| < 5$.  
   > Entonces: $|(x^2+2x)-3| \leq 5|x-1|$.  
   > Tomamos $\delta = \min\left(1, \dfrac{\varepsilon}{5}\right)$. Así: $|(x^2+2x)-3| \leq 5|x-1| < 5\cdot\dfrac{\varepsilon}{5} = \varepsilon$. ✓

4. Dado $\varepsilon = 0{,}1$, encuentra el valor mínimo de $\delta$ tal que si $|x - 2| < \delta$ entonces $|f(x) - L| < 0{,}1$ para $f(x) = 4x - 3$, $L = 5$.

   > **Solución:** $|f(x) - 5| = |4x - 3 - 5| = |4x - 8| = 4|x-2|$.  
   > Necesitamos $4|x-2| < 0{,}1 \Rightarrow |x-2| < 0{,}025$.  
   > El valor mínimo de $\delta$ es $\delta = 0{,}025$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = x^2 - 2x$.

   a) Calcula $\displaystyle\lim_{x \to 3} f(x)$ y comprueba que coincide con $f(3)$.  
   b) Para $\varepsilon = 0{,}5$, encuentra $\delta > 0$ tal que si $0 < |x-3| < \delta$ entonces $|f(x) - f(3)| < 0{,}5$.  
   c) Interpreta geométricamente qué significa la condición $\varepsilon$-$\delta$.

   > **Solución:**
   >
   > **a)** $\displaystyle\lim_{x \to 3}(x^2-2x) = 9-6 = 3 = f(3)$. El límite coincide con el valor (la función es continua).
   >
   > **b)** $|f(x) - 3| = |x^2 - 2x - 3| = |(x-3)(x+1)| = |x-3|\cdot|x+1|$.  
   > Si $|x-3| < 1$, entonces $2 < x < 4$, luego $3 < x+1 < 5$, es decir $|x+1| < 5$.  
   > Necesitamos $5|x-3| < 0{,}5 \Rightarrow |x-3| < 0{,}1$.  
   > Tomamos $\delta = \min(1; 0{,}1) = 0{,}1$.
   >
   > **c)** Geométricamente: para que los valores de $f$ queden dentro de la banda horizontal $(3-0{,}5,\, 3+0{,}5) = (2{,}5;\, 3{,}5)$ alrededor del límite, basta que $x$ esté dentro del intervalo $(3-0{,}1;\, 3+0{,}1) = (2{,}9;\, 3{,}1)$. La definición $\varepsilon$-$\delta$ dice que siempre podemos encontrar un entorno de $x=3$ que garantice la precisión deseada en $f$.

**Test de Opción Múltiple**

6. En la definición $\varepsilon$-$\delta$ de límite, si $\displaystyle\lim_{x\to a} f(x) = L$, entonces para cualquier $\varepsilon > 0$ existe $\delta > 0$ tal que $0 < |x - a| < \delta$ implica:
   - a) $|f(x)| < \varepsilon$
   - b) $|f(x) - L| < \varepsilon$
   - c) $|x - a| < \varepsilon$
   - d) $|f(x) - a| < \delta$

   > **Respuesta correcta: b)** La definición establece que $|f(x) - L| < \varepsilon$, es decir, $f(x)$ se aproxima al límite $L$ con precisión $\varepsilon$.

7. En la definición $\varepsilon$-$\delta$, la condición $0 < |x - a| < \delta$ (con $0 < |x-a|$) se impone para:
   - a) Exigir que $x > a$
   - b) Excluir el punto $x = a$ del análisis
   - c) Garantizar que $\delta < \varepsilon$
   - d) Asegurar que $f(a)$ esté definida

   > **Respuesta correcta: b)** La condición $|x - a| > 0$ excluye explícitamente el punto $x = a$: el límite describe el comportamiento de $f$ cerca de $a$, no en $a$. La función puede incluso no estar definida en $a$.

---

#### 6.1.3 Límites laterales: límite por la izquierda y por la derecha

**Ejercicio Resuelto**

Calcula los límites laterales de $f(x) = \dfrac{|x-2|}{x-2}$ en $x = 2$.

**Solución:**

Recordamos que $|x - 2| = \begin{cases} x-2 & \text{si } x \geq 2 \\ -(x-2) & \text{si } x < 2 \end{cases}$

**Límite por la derecha** ($x \to 2^+$): En este caso $x > 2$, luego $|x-2| = x-2$:
$$\lim_{x \to 2^+} \frac{|x-2|}{x-2} = \lim_{x \to 2^+} \frac{x-2}{x-2} = \lim_{x \to 2^+} 1 = 1$$

**Límite por la izquierda** ($x \to 2^-$): En este caso $x < 2$, luego $|x-2| = -(x-2)$:
$$\lim_{x \to 2^-} \frac{|x-2|}{x-2} = \lim_{x \to 2^-} \frac{-(x-2)}{x-2} = \lim_{x \to 2^-}(-1) = -1$$

Como $\displaystyle\lim_{x \to 2^+} f(x) = 1 \neq -1 = \lim_{x \to 2^-} f(x)$, **el límite en $x = 2$ no existe**.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula los límites laterales de $f(x) = \begin{cases} x + 1 & \text{si } x < 0 \\ x^2 + 1 & \text{si } x \geq 0 \end{cases}$ en $x = 0$.

   > **Solución:**  
   > $\displaystyle\lim_{x \to 0^-} (x+1) = 0+1 = 1$  
   > $\displaystyle\lim_{x \to 0^+} (x^2+1) = 0+1 = 1$  
   > Como ambos límites laterales son iguales a $1$: $\displaystyle\lim_{x \to 0} f(x) = 1$.

2. Para $g(x) = \begin{cases} 2x & \text{si } x \leq 1 \\ 3 & \text{si } x > 1 \end{cases}$, calcula los límites laterales en $x = 1$ y determina si existe el límite.

   > **Solución:**  
   > $\displaystyle\lim_{x \to 1^-} 2x = 2$  
   > $\displaystyle\lim_{x \to 1^+} 3 = 3$  
   > Los límites laterales son distintos ($2 \neq 3$), por tanto **el límite en $x = 1$ no existe**.

**Nivel Intermedio:**

3. Sea $f(x) = \dfrac{x^2 - 4}{|x - 2|}$. Calcula $\displaystyle\lim_{x \to 2^-} f(x)$ y $\displaystyle\lim_{x \to 2^+} f(x)$.

   > **Solución:** Factorizamos: $x^2 - 4 = (x-2)(x+2)$.  
   > Para $x \to 2^+$: $|x-2| = x-2$, luego $f(x) = \dfrac{(x-2)(x+2)}{x-2} = x+2 \to 4$.  
   > Para $x \to 2^-$: $|x-2| = -(x-2)$, luego $f(x) = \dfrac{(x-2)(x+2)}{-(x-2)} = -(x+2) \to -4$.  
   > $\displaystyle\lim_{x \to 2^+} f(x) = 4$, $\quad \displaystyle\lim_{x \to 2^-} f(x) = -4$. El límite global no existe.

4. Calcula los límites laterales de $h(x) = \dfrac{1}{x-3}$ en $x = 3$. ¿Qué tipo de comportamiento presenta?

   > **Solución:**  
   > Para $x \to 3^+$: $x - 3 > 0$ y tiende a $0^+$, luego $\dfrac{1}{x-3} \to +\infty$.  
   > Para $x \to 3^-$: $x - 3 < 0$ y tiende a $0^-$, luego $\dfrac{1}{x-3} \to -\infty$.  
   > La función presenta una **asíntota vertical** en $x = 3$ con ramas de distinto signo.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \begin{cases} \dfrac{x^2 - 1}{x - 1} & \text{si } x < 1 \\ ax + b & \text{si } x \geq 1 \end{cases}$

   a) Calcula $\displaystyle\lim_{x \to 1^-} f(x)$.  
   b) Para que $\displaystyle\lim_{x \to 1} f(x)$ exista, ¿qué condición deben cumplir $a$ y $b$?  
   c) Si además se pide que $f(1) = 3$, determina $a$ y $b$ de forma que el límite exista e indique un ejemplo de valores válidos.

   > **Solución:**
   >
   > **a)** Para $x < 1$: $\dfrac{x^2-1}{x-1} = \dfrac{(x-1)(x+1)}{x-1} = x+1 \to 1+1 = 2$.  
   > $\displaystyle\lim_{x \to 1^-} f(x) = 2$
   >
   > **b)** $\displaystyle\lim_{x \to 1^+} (ax+b) = a+b$.  
   > Para que exista el límite: $a + b = 2$.
   >
   > **c)** $f(1) = a(1) + b = a + b = 3$. Pero la condición de existencia del límite exige $a + b = 2$.  
   > Contradicción: si $f(1) = 3$ y el límite en $x=1$ vale $2$, el límite **existe** (vale $2$) pero $f(1) \neq \lim_{x\to 1}f(x)$, por lo que $f$ **no sería continua** en $x=1$.  
   > Para tener $a + b = 2$ con $f(1) = 3$: esto es imposible con esta definición de $f$, pues $f(1) = a + b$.  
   > Conclusión: si pedimos que $\lim_{x\to 1}f(x)$ exista Y $f(1) = 3$ simultáneamente, se necesita $a + b = 2$ y $a + b = 3$, lo cual es **incompatible**. Solo puede darse uno de los dos requisitos.

**Test de Opción Múltiple**

6. Para que $\displaystyle\lim_{x \to a} f(x)$ exista, es condición necesaria y suficiente que:
   - a) $f(a)$ esté definida
   - b) Los límites laterales existan y sean iguales
   - c) $f$ sea continua en $a$
   - d) $f'(a)$ exista

   > **Respuesta correcta: b)** El límite en un punto existe si y solo si los límites laterales por la izquierda y por la derecha existen y son iguales entre sí.

7. Si $\displaystyle\lim_{x \to 2^-} f(x) = 3$ y $\displaystyle\lim_{x \to 2^+} f(x) = -3$, entonces:
   - a) $\displaystyle\lim_{x \to 2} f(x) = 0$
   - b) $\displaystyle\lim_{x \to 2} f(x) = 3$
   - c) El límite en $x = 2$ no existe
   - d) $f(2) = 0$

   > **Respuesta correcta: c)** Como los límites laterales son distintos ($3 \neq -3$), el límite global en $x = 2$ no existe.

---

#### 6.1.4 Existencia del límite: condición de igualdad de límites laterales

**Ejercicio Resuelto**

Determina para qué valores del parámetro $k$ existe $\displaystyle\lim_{x \to 2} f(x)$, siendo $f(x) = \begin{cases} kx^2 - 1 & \text{si } x < 2 \\ 3x + k & \text{si } x \geq 2 \end{cases}$.

**Solución:**

Calculamos los límites laterales en función de $k$:

**Límite por la izquierda:**
$$\lim_{x \to 2^-}(kx^2 - 1) = k(4) - 1 = 4k - 1$$

**Límite por la derecha:**
$$\lim_{x \to 2^+}(3x + k) = 6 + k$$

Para que el límite global exista, debemos igualar:
$$4k - 1 = 6 + k$$
$$3k = 7$$
$$k = \frac{7}{3}$$

**Verificación:** Con $k = \frac{7}{3}$:
- Límite por la izquierda: $4 \cdot \frac{7}{3} - 1 = \frac{28}{3} - 1 = \frac{25}{3}$
- Límite por la derecha: $6 + \frac{7}{3} = \frac{18+7}{3} = \frac{25}{3}$ ✓

Para $k = \dfrac{7}{3}$, $\displaystyle\lim_{x \to 2} f(x) = \dfrac{25}{3}$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Comprueba si existe $\displaystyle\lim_{x \to 0} f(x)$ para $f(x) = \begin{cases} 2x + 3 & \text{si } x < 0 \\ 3 - x & \text{si } x \geq 0 \end{cases}$.

   > **Solución:**  
   > $\displaystyle\lim_{x \to 0^-}(2x+3) = 3$  
   > $\displaystyle\lim_{x \to 0^+}(3-x) = 3$  
   > Los límites laterales son iguales: $\displaystyle\lim_{x \to 0} f(x) = 3$.

2. Determina si $\displaystyle\lim_{x \to 1} g(x)$ existe para $g(x) = \begin{cases} x^2 & \text{si } x \leq 1 \\ 2x - 1 & \text{si } x > 1 \end{cases}$.

   > **Solución:**  
   > $\displaystyle\lim_{x \to 1^-} x^2 = 1$  
   > $\displaystyle\lim_{x \to 1^+}(2x-1) = 1$  
   > Los límites laterales coinciden: $\displaystyle\lim_{x \to 1} g(x) = 1$.

**Nivel Intermedio:**

3. Halla los valores de $a$ y $b$ para que $\displaystyle\lim_{x \to 1} f(x)$ exista y valga $4$, siendo:
   $$f(x) = \begin{cases} ax + b & \text{si } x < 1 \\ x^2 + 3 & \text{si } x \geq 1 \end{cases}$$

   > **Solución:**  
   > $\displaystyle\lim_{x \to 1^+}(x^2+3) = 4$, luego el límite debe ser $4$.  
   > $\displaystyle\lim_{x \to 1^-}(ax+b) = a+b = 4$.  
   > Con $a + b = 4$ el límite existe y vale $4$. Por ejemplo: $a = 1, b = 3$ o $a = 2, b = 2$.

4. Determina para qué valores de $k$ existe $\displaystyle\lim_{x \to 0} h(x)$:
   $$h(x) = \begin{cases} \dfrac{\sin(kx)}{x} & \text{si } x \neq 0 \\ 2 & \text{si } x = 0 \end{cases}$$

   > **Solución:** Para $x \neq 0$: $\displaystyle\lim_{x \to 0} \dfrac{\sin(kx)}{x} = \lim_{x \to 0} k \cdot \dfrac{\sin(kx)}{kx} = k \cdot 1 = k$.  
   > El límite existe y vale $k$ para cualquier $k$. Para que además sea continua en $0$, se necesitaría $k = 2$. El límite existe para todo $k \in \mathbb{R}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea la función:
   $$f(x) = \begin{cases} x^2 + ax & \text{si } x < -1 \\ b & \text{si } x = -1 \\ 2x + 3 & \text{si } x > -1 \end{cases}$$

   a) Calcula $\displaystyle\lim_{x \to -1^+} f(x)$.  
   b) Halla el valor de $a$ para que $\displaystyle\lim_{x \to -1} f(x)$ exista.  
   c) Con ese valor de $a$, ¿existe algún valor de $b$ que haga continua a $f$ en $x = -1$? Justifica.

   > **Solución:**
   >
   > **a)** $\displaystyle\lim_{x \to -1^+}(2x+3) = -2+3 = 1$
   >
   > **b)** $\displaystyle\lim_{x \to -1^-}(x^2 + ax) = 1 + a(-1) = 1 - a$.  
   > Para que el límite exista: $1 - a = 1 \Rightarrow a = 0$.  
   > Con $a = 0$: $\displaystyle\lim_{x \to -1} f(x) = 1$.
   >
   > **c)** Con $a = 0$, el límite en $x = -1$ vale $1$. Para que $f$ sea continua en $x = -1$, se necesita que $f(-1) = \lim_{x \to -1} f(x)$, es decir, $b = 1$. **Sí existe**: $b = 1$ hace que $f$ sea continua en $x = -1$.

**Test de Opción Múltiple**

6. Si $\displaystyle\lim_{x\to a^-} f(x) = L$ y $\displaystyle\lim_{x\to a^+} f(x) = L$, entonces es **seguro** que:
   - a) $f(a) = L$
   - b) $f$ es continua en $a$
   - c) $\displaystyle\lim_{x\to a} f(x) = L$
   - d) $f$ es derivable en $a$

   > **Respuesta correcta: c)** La igualdad de los límites laterales garantiza la existencia del límite global e igual a $L$. No se puede concluir nada sobre $f(a)$ ni sobre continuidad sin información adicional.

7. Para $f(x) = \begin{cases} 3 & \text{si } x < 2 \\ x + 1 & \text{si } x \geq 2 \end{cases}$, el valor de $\displaystyle\lim_{x \to 2} f(x)$:
   - a) Es $3$
   - b) Es $4$  
   - c) No existe
   - d) Depende de la rama que se tome

   > **Respuesta correcta: c)** $\lim_{x\to 2^-}f(x) = 3$ y $\lim_{x\to 2^+}f(x) = 3$... espera: $\lim_{x\to 2^+}(x+1)=3$. Entonces ambos valen $3$, el límite sí existe e igual a $3$.  
   > **Corrección de la respuesta: a)** $\lim_{x\to 2^-}f(x)=3$ y $\lim_{x\to 2^+}f(x)=2+1=3$. Ambos valen $3$, por tanto $\lim_{x\to 2}f(x)=3$.

---

#### 6.1.5 Propiedades operativas del límite (álgebra de límites)

**Ejercicio Resuelto**

Dados $\displaystyle\lim_{x \to 3} f(x) = 4$ y $\displaystyle\lim_{x \to 3} g(x) = -2$, calcula:
a) $\displaystyle\lim_{x \to 3}[3f(x) - g(x)]$
b) $\displaystyle\lim_{x \to 3}[f(x) \cdot g(x)]$
c) $\displaystyle\lim_{x \to 3}\dfrac{f(x)}{g(x)}$
d) $\displaystyle\lim_{x \to 3}\sqrt{f(x) + 5}$

**Solución:**

Aplicando las propiedades del álgebra de límites (siendo $L = \lim f$ y $M = \lim g$):

**a)** Linealidad:
$$\lim_{x \to 3}[3f(x) - g(x)] = 3\lim_{x \to 3}f(x) - \lim_{x \to 3}g(x) = 3(4) - (-2) = 12 + 2 = 14$$

**b)** Límite del producto:
$$\lim_{x \to 3}[f(x) \cdot g(x)] = \lim_{x \to 3}f(x) \cdot \lim_{x \to 3}g(x) = 4 \cdot (-2) = -8$$

**c)** Límite del cociente (el denominador no se anula):
$$\lim_{x \to 3}\frac{f(x)}{g(x)} = \frac{\lim_{x \to 3}f(x)}{\lim_{x \to 3}g(x)} = \frac{4}{-2} = -2$$

**d)** Límite de la raíz cuadrada (el argumento es positivo):
$$\lim_{x \to 3}\sqrt{f(x)+5} = \sqrt{\lim_{x \to 3}[f(x)+5]} = \sqrt{4+5} = \sqrt{9} = 3$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Si $\displaystyle\lim_{x \to 2} f(x) = 6$ y $\displaystyle\lim_{x \to 2} g(x) = 3$, calcula $\displaystyle\lim_{x \to 2}\left[\frac{f(x)}{g(x)} + f(x) - g(x)^2\right]$.

   > **Solución:** $\dfrac{6}{3} + 6 - 9 = 2 + 6 - 9 = -1$

2. Calcula $\displaystyle\lim_{x \to 1}(x^3 - 2x^2 + 5)$ usando las propiedades operativas.

   > **Solución:** Como es un polinomio, aplicamos límite por sustitución:  
   > $\displaystyle\lim_{x \to 1}x^3 - 2\lim_{x \to 1}x^2 + 5 = 1 - 2 + 5 = 4$

**Nivel Intermedio:**

3. Si $\displaystyle\lim_{x \to a}f(x) = 2$ y $\displaystyle\lim_{x \to a}g(x) = 0$, analiza si puede calcularse $\displaystyle\lim_{x \to a}\dfrac{f(x)}{g(x)}$.

   > **Solución:** La propiedad del cociente exige que el límite del denominador sea **no nulo**. Como $\lim g(x) = 0$, la propiedad **no es aplicable directamente**. El cociente puede tender a $\pm\infty$ o puede presentar una indeterminación que requiera técnicas específicas. No podemos afirmar que el límite no existe sin más información.

4. Dados $\displaystyle\lim_{x\to 0^+}f(x) = +\infty$ y $\displaystyle\lim_{x\to 0^+}g(x) = 3$, ¿cuánto vale $\displaystyle\lim_{x\to 0^+}[f(x)+g(x)]$?

   > **Solución:** Cuando un sumando tiende a $+\infty$ y el otro tiene límite finito:  
   > $\displaystyle\lim_{x\to 0^+}[f(x)+g(x)] = +\infty + 3 = +\infty$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sean $f$ y $g$ funciones tales que $\displaystyle\lim_{x \to 2} f(x) = 3$ y $\displaystyle\lim_{x \to 2} g(x) = 0$.

   a) Calcula $\displaystyle\lim_{x \to 2}[f(x)^2 - 2g(x) + 1]$.  
   b) Calcula $\displaystyle\lim_{x \to 2}\sqrt{2f(x) - g(x)}$.  
   c) ¿Puede calcularse $\displaystyle\lim_{x \to 2} \dfrac{g(x)}{f(x) - 3}$? Justifica.

   > **Solución:**
   >
   > **a)** $\lim[f^2 - 2g + 1] = 3^2 - 2(0) + 1 = 9 + 0 + 1 = 10$
   >
   > **b)** $\sqrt{2(3) - 0} = \sqrt{6}$
   >
   > **c)** $\lim[f(x)-3] = 3-3 = 0$ y $\lim g(x) = 0$: indeterminación $\dfrac{0}{0}$. Sin conocer las expresiones explícitas de $f$ y $g$, **no podemos calcular este límite** con las propiedades algebraicas. Requeriría información adicional sobre cómo se anulan numerador y denominador.

**Test de Opción Múltiple**

6. Si $\displaystyle\lim_{x\to a} f(x) = 2$ y $\displaystyle\lim_{x\to a} g(x) = -1$, entonces $\displaystyle\lim_{x\to a} [f(x)]^{g(x)}$ vale:
   - a) $-2$
   - b) $2$
   - c) $\frac{1}{2}$
   - d) $-\frac{1}{2}$

   > **Respuesta correcta: c)** $\lim [f(x)]^{g(x)} = \left(\lim f(x)\right)^{\lim g(x)} = 2^{-1} = \dfrac{1}{2}$ (válido cuando la base es positiva y los límites existen).

7. La propiedad $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)} = \frac{\lim_{x\to a}f(x)}{\lim_{x\to a}g(x)}$ se puede aplicar siempre que:
   - a) $\displaystyle\lim_{x\to a} f(x) \neq 0$
   - b) $\displaystyle\lim_{x\to a} g(x) \neq 0$
   - c) $f(a) \neq 0$
   - d) $g(a) \neq 0$

   > **Respuesta correcta: b)** La condición necesaria para aplicar la propiedad del cociente es que el límite del **denominador** sea no nulo.

---

## 6.2 Cálculo de límites e indeterminaciones

---

#### 6.2.1 Límites directos y por sustitución

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x \to 2}\frac{x^3 + 3x - 1}{x^2 + 1}$.

**Solución:**

Intentamos la sustitución directa $x = 2$:

$$\lim_{x \to 2}\frac{x^3 + 3x - 1}{x^2 + 1} = \frac{2^3 + 3(2) - 1}{2^2 + 1} = \frac{8 + 6 - 1}{4 + 1} = \frac{13}{5}$$

No hay indeterminación: el denominador no se anula en $x = 2$ (vale $5 \neq 0$) y numerador y denominador son polinomios (continuos). La sustitución directa es válida.

$$\lim_{x \to 2}\frac{x^3 + 3x - 1}{x^2 + 1} = \frac{13}{5}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula por sustitución directa: $\displaystyle\lim_{x \to -1}(x^4 - 3x^2 + 2x - 5)$.

   > **Solución:** $(-1)^4 - 3(-1)^2 + 2(-1) - 5 = 1 - 3 - 2 - 5 = -9$

2. Calcula: $\displaystyle\lim_{x \to \pi} \dfrac{\cos x + 2}{\sin x + 3}$.

   > **Solución:** $\dfrac{\cos\pi + 2}{\sin\pi + 3} = \dfrac{-1+2}{0+3} = \dfrac{1}{3}$

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x \to 0} \dfrac{e^x + \ln(x+1)}{x^2 + 2}$.

   > **Solución:** En $x = 0$: $\dfrac{e^0 + \ln 1}{0 + 2} = \dfrac{1 + 0}{2} = \dfrac{1}{2}$

4. Calcula $\displaystyle\lim_{x \to 1} \dfrac{\sqrt{x+3} - x^2}{x + 1}$.

   > **Solución:** $\dfrac{\sqrt{1+3} - 1}{1+1} = \dfrac{2 - 1}{2} = \dfrac{1}{2}$

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula los siguientes límites justificando el método:

   a) $\displaystyle\lim_{x \to 3} \dfrac{x^2 - 2x + 1}{x^3 - 1}$  
   b) $\displaystyle\lim_{x \to 0} \dfrac{\sqrt{4+x} \cdot e^x}{\cos x + 1}$  
   c) $\displaystyle\lim_{x \to 2} \dfrac{x^2 - 3x + 2}{x - 2}$

   > **Solución:**
   >
   > **a)** Denominador en $x=3$: $27 - 1 = 26 \neq 0$. Sustitución directa:  
   > $\dfrac{9-6+1}{27-1} = \dfrac{4}{26} = \dfrac{2}{13}$
   >
   > **b)** Denominador en $x=0$: $\cos 0 + 1 = 2 \neq 0$. Sustitución directa:  
   > $\dfrac{\sqrt{4}\cdot e^0}{1+1} = \dfrac{2\cdot1}{2} = 1$
   >
   > **c)** En $x=2$: numerador $= 4-6+2=0$, denominador $= 0$: indeterminación $\dfrac{0}{0}$.  
   > Factorizando: $\dfrac{(x-1)(x-2)}{x-2} = x-1 \to 2-1 = 1$.

**Test de Opción Múltiple**

6. ¿Cuándo se puede calcular un límite por sustitución directa?
   - a) Siempre
   - b) Solo cuando la función es polinómica
   - c) Cuando la función es continua en el punto considerado
   - d) Solo cuando el límite es un número real

   > **Respuesta correcta: c)** La sustitución directa es válida cuando la función es continua en el punto. Esto incluye polinomios, pero también funciones racionales, trigonométricas, exponenciales, etc., evaluadas en puntos de su dominio donde no hay discontinuidades.

7. Al calcular $\displaystyle\lim_{x\to 2}\dfrac{x-2}{x^2-4}$ por sustitución directa, obtenemos $\dfrac{0}{0}$. Esto significa:
   - a) El límite es $0$
   - b) El límite es infinito
   - c) El límite no existe
   - d) Hay una indeterminación que requiere otro método

   > **Respuesta correcta: d)** La forma $\dfrac{0}{0}$ es una indeterminación: el resultado no se puede determinar directamente. Se debe factorizar: $\dfrac{x-2}{(x-2)(x+2)} = \dfrac{1}{x+2} \to \dfrac{1}{4}$.

---

#### 6.2.2 Indeterminación 0/0: factorización, racionalización y cambios de variable

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x \to 3} \dfrac{x^2 - 9}{x^2 - 5x + 6}$.

**Solución:**

Comprobamos que hay indeterminación: $x = 3$ anula tanto numerador ($9-9=0$) como denominador ($9-15+6=0$). Forma: $\dfrac{0}{0}$.

**Paso 1: Factorizar**
- Numerador: $x^2 - 9 = (x-3)(x+3)$
- Denominador: $x^2 - 5x + 6 = (x-3)(x-2)$ (raíces: $x=3$ y $x=2$)

**Paso 2: Simplificar y calcular**
$$\lim_{x \to 3} \frac{x^2 - 9}{x^2 - 5x + 6} = \lim_{x \to 3} \frac{(x-3)(x+3)}{(x-3)(x-2)} = \lim_{x \to 3} \frac{x+3}{x-2} = \frac{3+3}{3-2} = \frac{6}{1} = 6$$

El factor $(x-3)$ se cancela (recordamos que $x \neq 3$ en el límite), y la sustitución directa ya es válida.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $\displaystyle\lim_{x \to 1}\dfrac{x^2 - 1}{x - 1}$.

   > **Solución:** $\dfrac{0}{0}$. Factorizando: $\dfrac{(x-1)(x+1)}{x-1} = x+1 \to 2$.

2. Calcula $\displaystyle\lim_{x \to 2}\dfrac{\sqrt{x} - \sqrt{2}}{x - 2}$.

   > **Solución:** $\dfrac{0}{0}$. Racionalizando (multiplicando por $\dfrac{\sqrt{x}+\sqrt{2}}{\sqrt{x}+\sqrt{2}}$):  
   > $\dfrac{(\sqrt{x}-\sqrt{2})(\sqrt{x}+\sqrt{2})}{(x-2)(\sqrt{x}+\sqrt{2})} = \dfrac{x-2}{(x-2)(\sqrt{x}+\sqrt{2})} = \dfrac{1}{\sqrt{x}+\sqrt{2}} \to \dfrac{1}{2\sqrt{2}} = \dfrac{\sqrt{2}}{4}$

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x \to 4}\dfrac{x - 4}{\sqrt{x} - 2}$.

   > **Solución:** Forma $\dfrac{0}{0}$. Multiplicando por $\dfrac{\sqrt{x}+2}{\sqrt{x}+2}$:  
   > $\dfrac{(x-4)(\sqrt{x}+2)}{(\sqrt{x}-2)(\sqrt{x}+2)} = \dfrac{(x-4)(\sqrt{x}+2)}{x-4} = \sqrt{x}+2 \to \sqrt{4}+2 = 4$

4. Calcula $\displaystyle\lim_{x \to 0}\dfrac{\sqrt{1+x} - \sqrt{1-x}}{x}$.

   > **Solución:** Forma $\dfrac{0}{0}$. Racionalizar multiplicando por $\dfrac{\sqrt{1+x}+\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}$:  
   > $\dfrac{(1+x)-(1-x)}{x(\sqrt{1+x}+\sqrt{1-x})} = \dfrac{2x}{x(\sqrt{1+x}+\sqrt{1-x})} = \dfrac{2}{\sqrt{1+x}+\sqrt{1-x}} \to \dfrac{2}{1+1} = 1$

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula los siguientes límites con indeterminación $\dfrac{0}{0}$:

   a) $\displaystyle\lim_{x \to -2}\dfrac{x^3 + 8}{x^2 + 3x + 2}$  
   b) $\displaystyle\lim_{x \to 1}\dfrac{\sqrt{x+3} - 2}{x - 1}$  
   c) $\displaystyle\lim_{x \to 0}\dfrac{(1+x)^2 - 1}{x}$

   > **Solución:**
   >
   > **a)** $x = -2$: numerador $= -8+8=0$, denominador $= 4-6+2=0$. Forma $\dfrac{0}{0}$.  
   > $x^3+8 = (x+2)(x^2-2x+4)$; $x^2+3x+2 = (x+2)(x+1)$.  
   > $\displaystyle\lim_{x\to-2}\dfrac{(x+2)(x^2-2x+4)}{(x+2)(x+1)} = \dfrac{4+4+4}{-2+1} = \dfrac{12}{-1} = -12$
   >
   > **b)** En $x=1$: $\sqrt{4}-2 = 0$ y $0$. Forma $\dfrac{0}{0}$.  
   > Multiplicamos por $\dfrac{\sqrt{x+3}+2}{\sqrt{x+3}+2}$:  
   > $\dfrac{(x+3)-4}{(x-1)(\sqrt{x+3}+2)} = \dfrac{x-1}{(x-1)(\sqrt{x+3}+2)} = \dfrac{1}{\sqrt{x+3}+2} \to \dfrac{1}{4}$
   >
   > **c)** $(1+x)^2 - 1 = 1+2x+x^2-1 = 2x+x^2 = x(2+x)$.  
   > $\dfrac{x(2+x)}{x} = 2+x \to 2$

**Test de Opción Múltiple**

6. Para resolver la indeterminación $\dfrac{0}{0}$ en $\displaystyle\lim_{x\to a}\dfrac{f(x)}{g(x)}$ cuando $f(x)$ contiene una raíz cuadrada, el método más habitual es:
   - a) L'Hôpital
   - b) Regla de Cramer
   - c) Racionalización del numerador
   - d) Desarrollo en serie de Taylor

   > **Respuesta correcta: c)** Cuando aparecen raíces cuadradas en el numerador, la racionalización (multiplicar por el conjugado) elimina la raíz y permite simplificar el factor que produce la indeterminación.

7. $\displaystyle\lim_{x \to 3}\dfrac{x^2 - 9}{x - 3}$ es igual a:
   - a) $0$
   - b) $3$
   - c) $6$
   - d) No existe

   > **Respuesta correcta: c)** $\dfrac{(x-3)(x+3)}{x-3} = x+3 \to 6$.

---

#### 6.2.3 Indeterminación k/0 y límites infinitos

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x \to 2} \dfrac{3x - 1}{(x-2)^2}$ y $\displaystyle\lim_{x \to 1^+} \dfrac{x+2}{x-1}$.

**Solución:**

**Primer límite:** En $x = 2$: numerador $= 6-1 = 5 \neq 0$, denominador $= 0$. Forma $\dfrac{k}{0}$ con $k = 5$.

Cuando $(x-2)^2 \to 0^+$ (el cuadrado siempre es positivo) y el numerador tiende a $5 > 0$:
$$\lim_{x \to 2} \frac{3x - 1}{(x-2)^2} = +\infty$$

El denominador $(x-2)^2$ es siempre $\geq 0$, por lo que el cociente tiende a $+\infty$ por ambos lados.

**Segundo límite:** En $x = 1$: numerador $= 3 > 0$, denominador $= 0$.

Para $x \to 1^+$: $x > 1$, luego $x - 1 > 0$ y tiende a $0^+$:
$$\lim_{x \to 1^+} \frac{x+2}{x-1} = \frac{3^+}{0^+} = +\infty$$

(Para $x \to 1^-$: $x - 1 < 0$, luego el límite sería $-\infty$.)

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $\displaystyle\lim_{x \to 0^+} \dfrac{1}{x}$ y $\displaystyle\lim_{x \to 0^-} \dfrac{1}{x}$.

   > **Solución:**  
   > $\displaystyle\lim_{x \to 0^+} \dfrac{1}{x} = +\infty$ (denominador positivo tendiendo a $0$)  
   > $\displaystyle\lim_{x \to 0^-} \dfrac{1}{x} = -\infty$ (denominador negativo tendiendo a $0$)

2. Calcula $\displaystyle\lim_{x \to 3^-} \dfrac{x+1}{3-x}$.

   > **Solución:** Numerador en $x=3$: $4 > 0$. Para $x \to 3^-$: $3 - x > 0$ y tiende a $0^+$.  
   > $\displaystyle\lim_{x \to 3^-} \dfrac{x+1}{3-x} = +\infty$

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x \to -1} \dfrac{x^2 + 2x + 1}{x + 1}$ o indica si no existe.

   > **Solución:** Numerador: $x^2+2x+1 = (x+1)^2$. En $x=-1$: ambos se anulan. Forma $\dfrac{0}{0}$.  
   > $\dfrac{(x+1)^2}{x+1} = x+1 \to 0$. No es $\dfrac{k}{0}$, sino $\dfrac{0}{0}$ con resultado $0$.

4. Estudia $\displaystyle\lim_{x \to 2} \dfrac{x^2 - 4}{(x-2)^3}$.

   > **Solución:** $x^2-4 = (x-2)(x+2)$, luego $\dfrac{(x-2)(x+2)}{(x-2)^3} = \dfrac{x+2}{(x-2)^2}$.  
   > En $x=2$: numerador $= 4 > 0$, denominador $= 0^+$. Límite $= +\infty$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Para $f(x) = \dfrac{x^2 - 1}{(x-1)^2(x+2)}$:

   a) Determina los puntos donde el denominador se anula.  
   b) Calcula los límites laterales en $x = 1$.  
   c) Calcula el límite en $x = -2$ si existe.

   > **Solución:**
   >
   > **a)** $(x-1)^2(x+2) = 0 \Rightarrow x = 1$ (doble) o $x = -2$.
   >
   > **b)** Simplificamos: $x^2-1 = (x-1)(x+1)$, luego:  
   > $\dfrac{(x-1)(x+1)}{(x-1)^2(x+2)} = \dfrac{x+1}{(x-1)(x+2)}$  
   > Para $x \to 1^+$: numerador $\to 2$, $(x-1) \to 0^+$, $(x+2) \to 3$.  
   > $\displaystyle\lim_{x\to 1^+} = +\infty$  
   > Para $x \to 1^-$: $(x-1) \to 0^-$, numerador $\to 2 > 0$, $(x+2) \to 3 > 0$.  
   > $\displaystyle\lim_{x\to 1^-} = -\infty$
   >
   > **c)** En $x = -2$: $\dfrac{x+1}{(x-1)(x+2)}$, numerador $= -1 \neq 0$, denominador $\to 0$.  
   > Para $x \to -2^+$: $(x+2) \to 0^+$, $(x-1) \to -3$, numerador $\to -1$.  
   > $\dfrac{-1}{(-3)(0^+)} = \dfrac{-1}{0^-} = +\infty$.  
   > Para $x \to -2^-$: $(x+2) \to 0^-$, $\dfrac{-1}{(-3)(0^-)} = \dfrac{-1}{0^+} = -\infty$.  
   > El límite en $x = -2$ **no existe** (límites laterales infinitos con distinto signo).

**Test de Opción Múltiple**

6. El límite $\displaystyle\lim_{x\to 0}\dfrac{1}{x^2}$ vale:
   - a) $0$
   - b) $-\infty$
   - c) $+\infty$
   - d) No existe

   > **Respuesta correcta: c)** $x^2 > 0$ para todo $x \neq 0$, y tiende a $0^+$. Por tanto $\dfrac{1}{x^2} \to +\infty$.

7. Si $f(x) \to 3$ y $g(x) \to 0^-$ cuando $x \to a$, entonces $\displaystyle\lim_{x\to a}\dfrac{f(x)}{g(x)}$ vale:
   - a) $0$
   - b) $+\infty$
   - c) $-\infty$
   - d) $3$

   > **Respuesta correcta: c)** Numerador positivo ($3$) dividido entre denominador negativo tendiendo a cero da $-\infty$.

---

#### 6.2.4 Indeterminación ∞ − ∞: técnicas de resolución

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x \to +\infty}\left(\sqrt{x^2 + 3x} - x\right)$.

**Solución:**

Forma $+\infty - \infty$. Racionalizamos multiplicando por el conjugado:

$$\lim_{x \to +\infty}\left(\sqrt{x^2+3x}-x\right) \cdot \frac{\sqrt{x^2+3x}+x}{\sqrt{x^2+3x}+x} = \lim_{x \to +\infty}\frac{(x^2+3x)-x^2}{\sqrt{x^2+3x}+x} = \lim_{x \to +\infty}\frac{3x}{\sqrt{x^2+3x}+x}$$

Dividimos numerador y denominador por $x > 0$:

$$= \lim_{x \to +\infty}\frac{3}{\sqrt{1+\frac{3}{x}}+1} = \frac{3}{\sqrt{1+0}+1} = \frac{3}{2}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $\displaystyle\lim_{x \to 1}\left(\dfrac{1}{x-1} - \dfrac{2}{x^2-1}\right)$.

   > **Solución:** Forma $\infty - \infty$. Reducimos a común denominador $x^2-1 = (x-1)(x+1)$:  
   > $\dfrac{x+1}{(x-1)(x+1)} - \dfrac{2}{(x-1)(x+1)} = \dfrac{x+1-2}{(x-1)(x+1)} = \dfrac{x-1}{(x-1)(x+1)} = \dfrac{1}{x+1} \to \dfrac{1}{2}$

2. Calcula $\displaystyle\lim_{x \to +\infty}(\sqrt{x+1} - \sqrt{x})$.

   > **Solución:** Racionalizando: $\dfrac{(x+1)-x}{\sqrt{x+1}+\sqrt{x}} = \dfrac{1}{\sqrt{x+1}+\sqrt{x}} \to 0$.

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x \to 2}\left(\dfrac{3}{x^2-4} - \dfrac{1}{x-2}\right)$.

   > **Solución:** $x^2-4=(x-2)(x+2)$. Reduciendo a denominador común $(x-2)(x+2)$:  
   > $\dfrac{3}{(x-2)(x+2)} - \dfrac{x+2}{(x-2)(x+2)} = \dfrac{3-(x+2)}{(x-2)(x+2)} = \dfrac{1-x}{(x-2)(x+2)}$  
   > En $x=2$: numerador $\to -1$, denominador $\to 0$. Analizamos el signo:  
   > Para $x\to 2^+$: $(x-2)\to 0^+$, $(x+2)\to 4$, numerador $\to -1$: límite $= -\infty$.  
   > Para $x\to 2^-$: $(x-2)\to 0^-$: límite $= +\infty$. **No existe el límite**.

4. Calcula $\displaystyle\lim_{x \to +\infty}\left(\sqrt{x^2+x} - \sqrt{x^2-x}\right)$.

   > **Solución:** Racionalizando:  
   > $\dfrac{(x^2+x)-(x^2-x)}{\sqrt{x^2+x}+\sqrt{x^2-x}} = \dfrac{2x}{\sqrt{x^2+x}+\sqrt{x^2-x}}$  
   > Dividiendo por $x$: $\dfrac{2}{\sqrt{1+1/x}+\sqrt{1-1/x}} \to \dfrac{2}{1+1} = 1$

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula:

   a) $\displaystyle\lim_{x \to 0}\left(\dfrac{1}{x} - \dfrac{1}{\sin x}\right)$  
   b) $\displaystyle\lim_{x \to +\infty}\left(x - \sqrt{x^2 - 4x + 1}\right)$

   > **Solución:**
   >
   > **a)** Forma $\infty - \infty$. Reduciendo: $\dfrac{\sin x - x}{x \sin x}$.  
   > Numerador: $\sin x - x \to 0$; denominador: $x\sin x \to 0$. Forma $\dfrac{0}{0}$.  
   > Usando el equivalente $\sin x \approx x - \dfrac{x^3}{6}$ cerca de $0$:  
   > $\sin x - x \approx -\dfrac{x^3}{6}$; $x\sin x \approx x^2$.  
   > Límite $= \displaystyle\lim_{x\to 0} \dfrac{-x^3/6}{x^2} = \lim_{x\to 0}\dfrac{-x}{6} = 0$
   >
   > **b)** Racionalizando:  
   > $\dfrac{x^2-(x^2-4x+1)}{x+\sqrt{x^2-4x+1}} = \dfrac{4x-1}{x+\sqrt{x^2-4x+1}}$  
   > Dividiendo por $x$: $\dfrac{4-1/x}{1+\sqrt{1-4/x+1/x^2}} \to \dfrac{4}{1+1} = 2$

**Test de Opción Múltiple**

6. La indeterminación $\infty - \infty$ aparece cuando:
   - a) Los dos sumandos tienden al mismo número
   - b) Uno tiende a $+\infty$ y el otro a $-\infty$, o ambos a $+\infty$
   - c) Ambos tienden a cero
   - d) El numerador tiende a infinito

   > **Respuesta correcta: b)** La forma $\infty - \infty$ ocurre cuando ambos términos tienden a infinito (del mismo o distinto signo) creando una incertidumbre sobre el resultado.

7. Para resolver $\displaystyle\lim_{x\to+\infty}(\sqrt{x+a}-\sqrt{x})$, el método más eficaz es:
   - a) Sustitución directa
   - b) L'Hôpital directamente
   - c) Multiplicar por el conjugado
   - d) Factorizar el denominador

   > **Respuesta correcta: c)** La racionalización (multiplicar y dividir por el conjugado $\sqrt{x+a}+\sqrt{x}$) transforma la diferencia de raíces en un cociente manejable.

---

#### 6.2.5 Indeterminación 0·∞: transformación en 0/0 o ∞/∞

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x \to 0^+} x \cdot \ln x$.

**Solución:**

Forma $0 \cdot \infty$: cuando $x \to 0^+$, $x \to 0$ y $\ln x \to -\infty$.

Transformamos a forma $\dfrac{\infty}{\infty}$: escribimos $x = \dfrac{1}{1/x}$:

$$\lim_{x \to 0^+} x \cdot \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x}$$

Ahora es forma $\dfrac{-\infty}{+\infty}$. Aplicamos L'Hôpital:

$$= \lim_{x \to 0^+} \frac{(\ln x)'}{(1/x)'} = \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} \frac{x^2}{-x} \cdot \frac{1}{1} = \lim_{x \to 0^+}(-x) = 0$$

**Resultado:** $\displaystyle\lim_{x \to 0^+} x \ln x = 0$

(El logaritmo crece más lentamente que cualquier potencia positiva de $x$.)

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Transforma la indeterminación $0 \cdot \infty$ en $\dfrac{0}{0}$ o $\dfrac{\infty}{\infty}$ para $\displaystyle\lim_{x\to 0^+}\sqrt{x}\cdot\ln x$.

   > **Solución:** Forma $0\cdot(-\infty)$. Transformamos: $\sqrt{x}\cdot\ln x = \dfrac{\ln x}{1/\sqrt{x}} = \dfrac{\ln x}{x^{-1/2}}$. Forma $\dfrac{-\infty}{+\infty}$.  
   > L'Hôpital: $\dfrac{1/x}{-\frac{1}{2}x^{-3/2}} = \dfrac{1/x}{-\frac{1}{2x^{3/2}}} = \dfrac{-2x^{3/2}}{x} = -2\sqrt{x} \to 0$.  
   > Por tanto: $\displaystyle\lim_{x\to 0^+}\sqrt{x}\ln x = 0$.

2. Calcula $\displaystyle\lim_{x\to+\infty}x\cdot e^{-x}$.

   > **Solución:** Forma $+\infty \cdot 0$. Transformamos: $\dfrac{x}{e^x}$. Forma $\dfrac{+\infty}{+\infty}$.  
   > L'Hôpital: $\dfrac{1}{e^x} \to 0$.  
   > $\displaystyle\lim_{x\to+\infty}x e^{-x} = 0$.

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x\to 0^+}x^2\ln x$.

   > **Solución:** $\dfrac{\ln x}{x^{-2}} \xrightarrow{\text{L'H}} \dfrac{1/x}{-2x^{-3}} = \dfrac{-x^3}{2x} = \dfrac{-x^2}{2} \to 0$.

4. Calcula $\displaystyle\lim_{x\to+\infty}(x^3+2x)e^{-2x}$.

   > **Solución:** Forma $\infty\cdot 0$. Transformar: $\dfrac{x^3+2x}{e^{2x}}$. Forma $\dfrac{\infty}{\infty}$.  
   > L'Hôpital (tres veces si es necesario):  
   > $\dfrac{3x^2+2}{2e^{2x}} \xrightarrow{\text{L'H}} \dfrac{6x}{4e^{2x}} \xrightarrow{\text{L'H}} \dfrac{6}{8e^{2x}} \to 0$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula:

   a) $\displaystyle\lim_{x\to 0^+}x\ln(x^2)$  
   b) $\displaystyle\lim_{x\to\frac{\pi}{2}^-}(\pi - 2x)\tan x$

   > **Solución:**
   >
   > **a)** $x\ln(x^2) = 2x\ln x$. Por el resultado del ejercicio resuelto: $2\displaystyle\lim_{x\to 0^+}x\ln x = 2\cdot 0 = 0$.
   >
   > **b)** Hacemos el cambio $t = \dfrac{\pi}{2} - x$, luego $x = \dfrac{\pi}{2} - t$, $t\to 0^+$.  
   > $\pi - 2x = \pi - 2(\frac{\pi}{2}-t) = 2t$.  
   > $\tan x = \tan(\frac{\pi}{2}-t) = \cot t = \dfrac{\cos t}{\sin t}$.  
   > Límite $= \displaystyle\lim_{t\to 0^+}2t\cdot\dfrac{\cos t}{\sin t} = 2\lim_{t\to 0^+}\dfrac{t}{\sin t}\cdot\cos t = 2\cdot 1\cdot 1 = 2$.

**Test de Opción Múltiple**

6. La indeterminación $0\cdot\infty$ puede transformarse en:
   - a) Solo $\dfrac{0}{0}$
   - b) Solo $\dfrac{\infty}{\infty}$
   - c) Cualquiera de las dos: $\dfrac{0}{0}$ o $\dfrac{\infty}{\infty}$
   - d) $\infty - \infty$

   > **Respuesta correcta: c)** Si el producto es $f(x)\cdot g(x)$ con $f\to 0$ y $g\to\infty$, podemos escribir $\dfrac{f(x)}{1/g(x)}$ (forma $\dfrac{0}{0}$) o $\dfrac{g(x)}{1/f(x)}$ (forma $\dfrac{\infty}{\infty}$).

7. $\displaystyle\lim_{x\to 0^+}x\ln x$ vale:
   - a) $-\infty$
   - b) $1$
   - c) $0$
   - d) $+\infty$

   > **Respuesta correcta: c)** Aunque $\ln x\to -\infty$, la velocidad de $x\to 0$ domina: $x\ln x\to 0$.

---

#### 6.2.6 Indeterminación 1^∞: técnica exponencial

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x \to 0}(1 + 3x)^{1/x}$.

**Solución:**

Forma $1^\infty$: cuando $x \to 0$, la base $1+3x \to 1$ y el exponente $1/x \to \infty$.

**Método exponencial:** Escribimos $(1+3x)^{1/x} = e^{\frac{1}{x}\ln(1+3x)}$.

Calculamos el límite del exponente:
$$\lim_{x \to 0} \frac{\ln(1+3x)}{x}$$

Forma $\dfrac{0}{0}$. Aplicamos L'Hôpital (o usamos el límite fundamental $\ln(1+u) \approx u$ para $u \to 0$):

$$\lim_{x \to 0} \frac{\ln(1+3x)}{x} = \lim_{x \to 0} \frac{3/(1+3x)}{1} = 3$$

Por tanto:
$$\lim_{x \to 0}(1+3x)^{1/x} = e^3$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $\displaystyle\lim_{x \to \infty}\left(1 + \dfrac{1}{x}\right)^x$ (límite fundamental de $e$).

   > **Solución:** Forma $1^\infty$. Exponente: $x\cdot\ln(1+1/x) = \dfrac{\ln(1+1/x)}{1/x}$.  
   > Con $u = 1/x \to 0$: $\dfrac{\ln(1+u)}{u} \to 1$. Por tanto: $e^1 = e$.

2. Calcula $\displaystyle\lim_{x\to 0}(1+5x)^{2/x}$.

   > **Solución:** Exponente: $\dfrac{2}{x}\ln(1+5x) = 2\cdot\dfrac{\ln(1+5x)}{x} \to 2\cdot 5 = 10$.  
   > Resultado: $e^{10}$.

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x \to +\infty}\left(\dfrac{x+2}{x-1}\right)^x$.

   > **Solución:** Forma $1^\infty$. Escribimos $\dfrac{x+2}{x-1} = 1 + \dfrac{3}{x-1}$.  
   > Exponente: $x\ln\left(1+\dfrac{3}{x-1}\right) \approx x\cdot\dfrac{3}{x-1} = \dfrac{3x}{x-1} \to 3$.  
   > Resultado: $e^3$.

4. Calcula $\displaystyle\lim_{x \to 0}\left(\cos x\right)^{1/x^2}$.

   > **Solución:** Exponente: $\dfrac{\ln(\cos x)}{x^2}$. Forma $\dfrac{0}{0}$.  
   > L'Hôpital: $\dfrac{-\sin x/\cos x}{2x} = \dfrac{-\tan x}{2x} \to \dfrac{-1}{2}$.  
   > Resultado: $e^{-1/2} = \dfrac{1}{\sqrt{e}}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula los siguientes límites con indeterminación $1^\infty$:

   a) $\displaystyle\lim_{x\to\infty}\left(1 - \dfrac{2}{x}\right)^{3x}$  
   b) $\displaystyle\lim_{x\to 0}\dfrac{(1+x)^{1/x} - e}{x}$ (Solo calcular el límite de la forma $1^\infty$ interna)

   > **Solución:**
   >
   > **a)** Exponente: $3x\ln\left(1-\dfrac{2}{x}\right)$.  
   > Con $u = -2/x \to 0$: $3x\ln(1+u) \approx 3x\cdot u = 3x\cdot(-2/x) = -6$.  
   > Resultado: $e^{-6}$.
   >
   > **b)** Para calcular $(1+x)^{1/x}$ cuando $x\to 0$: exponente $= \dfrac{\ln(1+x)}{x}$.  
   > Desarrollando $\ln(1+x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \cdots$:  
   > $\dfrac{\ln(1+x)}{x} = 1 - \dfrac{x}{2} + O(x^2)$.  
   > $(1+x)^{1/x} = e^{1 - x/2 + O(x^2)} = e\cdot e^{-x/2+O(x^2)} \approx e(1 - x/2 + \cdots)$.  
   > $\dfrac{(1+x)^{1/x}-e}{x} \approx \dfrac{e(1-x/2)-e}{x} = \dfrac{-ex/2}{x} = -\dfrac{e}{2}$.  
   > Por tanto: $\displaystyle\lim_{x\to 0}\dfrac{(1+x)^{1/x}-e}{x} = -\dfrac{e}{2}$.

**Test de Opción Múltiple**

6. Para calcular un límite de la forma $\displaystyle\lim f(x)^{g(x)}$ con forma $1^\infty$, el procedimiento correcto comienza por:
   - a) Tomar logaritmos neperianos y calcular $\displaystyle\lim g(x)\ln f(x)$
   - b) Elevar $f$ y $g$ por separado
   - c) Aplicar L'Hôpital directamente a $f^g$
   - d) Sustituir directamente

   > **Respuesta correcta: a)** Se escribe $f^g = e^{g\ln f}$ y se calcula el límite del exponente $g\ln f$, que suele dar la forma $\infty\cdot 0$.

7. $\displaystyle\lim_{x\to\infty}\left(1+\dfrac{a}{x}\right)^x = $
   - a) $a$
   - b) $e^a$
   - c) $1$
   - d) $e$

   > **Respuesta correcta: b)** Es la generalización del límite fundamental: $\left(1+\dfrac{a}{x}\right)^x \to e^a$.

---

## 6.3 Límites en el infinito y asíntotas

---

#### 6.3.1 Límite de una función cuando x → ±∞

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x \to +\infty}\dfrac{3x^2 - 2x + 1}{x^2 + 5x - 3}$ y $\displaystyle\lim_{x \to -\infty}\dfrac{2x^3 - 1}{x^2 + 1}$.

**Solución:**

**Primer límite:** Forma $\dfrac{\infty}{\infty}$. Dividimos numerador y denominador por la mayor potencia ($x^2$):

$$\lim_{x \to +\infty}\frac{3x^2-2x+1}{x^2+5x-3} = \lim_{x \to +\infty}\frac{3 - 2/x + 1/x^2}{1 + 5/x - 3/x^2} = \frac{3-0+0}{1+0-0} = 3$$

**Segundo límite:** Forma $\dfrac{-\infty}{\infty}$. Dividimos por $x^2$:

$$\lim_{x \to -\infty}\frac{2x^3-1}{x^2+1} = \lim_{x \to -\infty}\frac{2x - 1/x^2}{1+1/x^2} = \lim_{x \to -\infty}(2x) = -\infty$$

(El grado del numerador supera al del denominador.)

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $\displaystyle\lim_{x\to+\infty}\dfrac{5x+3}{2x-1}$.

   > **Solución:** Dividiendo por $x$: $\dfrac{5+3/x}{2-1/x} \to \dfrac{5}{2}$.

2. Calcula $\displaystyle\lim_{x\to-\infty}(3x^2 - 2x + 7)$.

   > **Solución:** El término dominante es $3x^2$. Cuando $x\to-\infty$, $x^2\to+\infty$, luego el límite es $+\infty$.

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x\to+\infty}\dfrac{4x^3-x}{2x^3+3x^2-1}$.

   > **Solución:** Mismo grado. Dividiendo por $x^3$: $\dfrac{4-1/x^2}{2+3/x-1/x^3} \to \dfrac{4}{2} = 2$.

4. Calcula $\displaystyle\lim_{x\to-\infty}\dfrac{x^2-1}{\sqrt{x^4+2}}$.

   > **Solución:** Para $x\to-\infty$, $x^2 = |x|^2$. Dividiendo por $x^2$:  
   > $\dfrac{1-1/x^2}{\sqrt{1+2/x^4}} \to \dfrac{1}{\sqrt{1}} = 1$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula, justificando cada paso:

   a) $\displaystyle\lim_{x\to+\infty}\dfrac{x^2+3x-1}{2x^2-x+4}$  
   b) $\displaystyle\lim_{x\to-\infty}\dfrac{x^3-2}{x^2+1}$  
   c) $\displaystyle\lim_{x\to+\infty}\left(\sqrt{x^2+x}-x\right)$

   > **Solución:**
   >
   > **a)** Mismo grado ($2$). Cociente de coeficientes directores: $\dfrac{1}{2}$.
   >
   > **b)** Grado numerador ($3$) $>$ grado denominador ($2$). El término dominante es $\dfrac{x^3}{x^2} = x \to -\infty$.
   >
   > **c)** Forma $\infty-\infty$. Racionalizando:  
   > $\dfrac{(x^2+x)-x^2}{\sqrt{x^2+x}+x} = \dfrac{x}{\sqrt{x^2+x}+x}$. Dividiendo por $x>0$:  
   > $\dfrac{1}{\sqrt{1+1/x}+1} \to \dfrac{1}{2}$.

**Test de Opción Múltiple**

6. $\displaystyle\lim_{x\to+\infty}\dfrac{3x^4 - 2x}{x^4+1}$ vale:
   - a) $0$
   - b) $3$
   - c) $+\infty$
   - d) $-2$

   > **Respuesta correcta: b)** Mismo grado en numerador y denominador: el límite es el cociente de los coeficientes líderes: $\dfrac{3}{1} = 3$.

7. Si el grado del numerador es menor que el grado del denominador en una función racional, el límite cuando $x\to\pm\infty$ es:
   - a) $\pm\infty$
   - b) El cociente de los coeficientes líderes
   - c) $0$
   - d) $1$

   > **Respuesta correcta: c)** Si $\deg(\text{num}) < \deg(\text{den})$, el numerador crece más lentamente y el límite es $0$.

---

#### 6.3.2 Asíntota horizontal: definición y cálculo

**Ejercicio Resuelto**

Halla las asíntotas horizontales de $f(x) = \dfrac{2x^2 - 3}{x^2 + x + 1}$.

**Solución:**

Una recta $y = L$ es **asíntota horizontal** si $\displaystyle\lim_{x\to+\infty}f(x) = L$ o $\displaystyle\lim_{x\to-\infty}f(x) = L$.

**Cuando $x \to +\infty$:**
$$\lim_{x\to+\infty}\frac{2x^2-3}{x^2+x+1} = \lim_{x\to+\infty}\frac{2-3/x^2}{1+1/x+1/x^2} = \frac{2}{1} = 2$$

**Cuando $x \to -\infty$:**
$$\lim_{x\to-\infty}\frac{2x^2-3}{x^2+x+1} = 2 \quad \text{(mismo cálculo)}$$

La función tiene **una única asíntota horizontal**: $y = 2$.

**Verificación:** Al ser la función racional con numerador y denominador del mismo grado, el límite en ambos infinitos coincide con el cociente de los coeficientes líderes: $\dfrac{2}{1} = 2$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla las asíntotas horizontales de $f(x) = \dfrac{x+1}{x-2}$.

   > **Solución:** $\displaystyle\lim_{x\to\pm\infty}\dfrac{x+1}{x-2} = 1$. Asíntota horizontal: $y = 1$.

2. Determina si $f(x) = \dfrac{2x+1}{x^2+1}$ tiene asíntota horizontal.

   > **Solución:** $\displaystyle\lim_{x\to\pm\infty}\dfrac{2x+1}{x^2+1} = 0$ (grado num. $<$ grado den.). Asíntota horizontal: $y = 0$ (eje $OX$).

**Nivel Intermedio:**

3. Halla las asíntotas horizontales de $f(x) = \dfrac{3x}{\sqrt{x^2+4}}$.

   > **Solución:**  
   > Para $x\to+\infty$: $\sqrt{x^2+4} \approx x$, luego $\dfrac{3x}{\sqrt{x^2+4}} \to 3$.  
   > Para $x\to-\infty$: $\sqrt{x^2+4} = \sqrt{x^2}\sqrt{1+4/x^2} = |x|\sqrt{1+4/x^2} = -x\sqrt{1+4/x^2}$ (pues $x < 0$), luego $\dfrac{3x}{-x} = -3$.  
   > **Dos asíntotas horizontales**: $y = 3$ (en $+\infty$) y $y = -3$ (en $-\infty$).

4. Calcula las asíntotas horizontales de $f(x) = \arctan x$.

   > **Solución:** $\displaystyle\lim_{x\to+\infty}\arctan x = \dfrac{\pi}{2}$ y $\displaystyle\lim_{x\to-\infty}\arctan x = -\dfrac{\pi}{2}$.  
   > **Dos asíntotas horizontales**: $y = \dfrac{\pi}{2}$ y $y = -\dfrac{\pi}{2}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \dfrac{x^2 - 4x + 3}{x^2 - 1}$.

   a) Calcula $\displaystyle\lim_{x\to\pm\infty}f(x)$ e indica las asíntotas horizontales.  
   b) Simplifica $f(x)$ para $x\neq\pm 1$ y determina si la asíntota se alcanza.  
   c) ¿Para qué valores de $x$ es $f(x) = 1$?

   > **Solución:**
   >
   > **a)** $\displaystyle\lim_{x\to\pm\infty}\dfrac{x^2-4x+3}{x^2-1} = 1$. Asíntota horizontal: $y = 1$.
   >
   > **b)** $x^2-4x+3 = (x-1)(x-3)$ y $x^2-1 = (x-1)(x+1)$:  
   > $f(x) = \dfrac{(x-1)(x-3)}{(x-1)(x+1)} = \dfrac{x-3}{x+1}$ para $x\neq 1$.  
   > La asíntota $y=1$ no se alcanza (la función nunca vale $1$ en su dominio, como veremos en c).
   >
   > **c)** $\dfrac{x-3}{x+1} = 1 \Rightarrow x-3 = x+1 \Rightarrow -3 = 1$: imposible. La función **nunca toma el valor $1$**, confirmando que la asíntota no se alcanza.

**Test de Opción Múltiple**

6. Una función racional $\dfrac{p(x)}{q(x)}$ tiene asíntota horizontal distinta de $0$ cuando:
   - a) $\deg p > \deg q$
   - b) $\deg p = \deg q$
   - c) $\deg p < \deg q$
   - d) $\deg p = 0$

   > **Respuesta correcta: b)** Si los grados son iguales, la asíntota horizontal es el cociente de los coeficientes líderes (distinto de $0$). Si $\deg p < \deg q$, la asíntota es $y=0$.

7. La función $f(x) = e^{-x}$ tiene:
   - a) Asíntota horizontal $y = 0$ solo en $+\infty$
   - b) Asíntota horizontal $y = 0$ en ambos infinitos
   - c) Asíntota horizontal $y = 1$ en $+\infty$
   - d) No tiene asíntotas horizontales

   > **Respuesta correcta: a)** $\displaystyle\lim_{x\to+\infty}e^{-x} = 0$ (asíntota $y=0$) y $\displaystyle\lim_{x\to-\infty}e^{-x} = +\infty$ (no hay asíntota en $-\infty$).

---

#### 6.3.3 Asíntota vertical: definición y cálculo

**Ejercicio Resuelto**

Determina las asíntotas verticales de $f(x) = \dfrac{x + 1}{x^2 - x - 6}$.

**Solución:**

Las asíntotas verticales se producen donde el denominador se anula (y el numerador no).

**Paso 1:** Factorizar el denominador: $x^2 - x - 6 = (x-3)(x+2)$. Raíces: $x = 3$ y $x = -2$.

**Paso 2:** Comprobar que el numerador no se anula en esos puntos:
- En $x = 3$: numerador $= 4 \neq 0$ ✓
- En $x = -2$: numerador $= -1 \neq 0$ ✓

**Paso 3:** Calcular límites laterales:

En $x = 3$:
- $\displaystyle\lim_{x\to 3^+}\frac{x+1}{(x-3)(x+2)} = \frac{4}{0^+\cdot 5} = +\infty$
- $\displaystyle\lim_{x\to 3^-}\frac{x+1}{(x-3)(x+2)} = \frac{4}{0^-\cdot 5} = -\infty$

En $x = -2$:
- $\displaystyle\lim_{x\to -2^+}\frac{x+1}{(x-3)(x+2)} = \frac{-1}{(-5)\cdot 0^+} = +\infty$
- $\displaystyle\lim_{x\to -2^-}\frac{x+1}{(x-3)(x+2)} = \frac{-1}{(-5)\cdot 0^-} = -\infty$

**Conclusión:** La función tiene dos asíntotas verticales: $x = 3$ y $x = -2$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla las asíntotas verticales de $f(x) = \dfrac{1}{x^2-4}$.

   > **Solución:** Denominador $= 0 \Rightarrow x = \pm 2$. Numerador $= 1 \neq 0$ en ambos.  
   > Asíntotas verticales: $x = 2$ y $x = -2$.

2. Determina las asíntotas verticales de $g(x) = \tan x$ en $[-\pi, \pi]$.

   > **Solución:** $\tan x = \dfrac{\sin x}{\cos x}$. El denominador $\cos x = 0$ en $x = \pm\dfrac{\pi}{2}$.  
   > Asíntotas verticales: $x = \dfrac{\pi}{2}$ y $x = -\dfrac{\pi}{2}$.

**Nivel Intermedio:**

3. Halla las asíntotas verticales de $h(x) = \dfrac{x^2-1}{x^2+x}$ e indica si hay agujero (discontinuidad evitable).

   > **Solución:** $x^2+x = x(x+1) = 0 \Rightarrow x = 0$ o $x = -1$.  
   > $x^2-1 = (x-1)(x+1)$.  
   > En $x = -1$: numerador $= 0$ también; hay que simplificar: $\dfrac{(x-1)(x+1)}{x(x+1)} = \dfrac{x-1}{x}$.  
   > $\displaystyle\lim_{x\to -1}\dfrac{x-1}{x} = \dfrac{-2}{-1} = 2$: **discontinuidad evitable** en $x=-1$ (agujero).  
   > En $x = 0$: numerador $= -1\neq 0$. $\displaystyle\lim_{x\to 0}\dfrac{x-1}{x} = \pm\infty$: **asíntota vertical** $x=0$.

4. Determina las asíntotas verticales de $f(x) = \ln(x-2)$.

   > **Solución:** El dominio es $x > 2$. $\displaystyle\lim_{x\to 2^+}\ln(x-2) = -\infty$. Asíntota vertical: $x = 2$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \dfrac{x^2+x-2}{x^2-3x+2}$.

   a) Factoriza numerador y denominador.  
   b) Halla el dominio de $f$.  
   c) Determina si hay discontinuidades evitables o asíntotas verticales en cada punto de no definición.

   > **Solución:**
   >
   > **a)** Numerador: $x^2+x-2 = (x+2)(x-1)$. Denominador: $x^2-3x+2 = (x-1)(x-2)$.
   >
   > **b)** Dom$(f) = \mathbb{R}\setminus\{1, 2\}$.
   >
   > **c)** En $x = 1$: numerador $= 0$ también. Simplificando: $\dfrac{(x+2)(x-1)}{(x-1)(x-2)} = \dfrac{x+2}{x-2}$.  
   > $\displaystyle\lim_{x\to 1}\dfrac{x+2}{x-2} = \dfrac{3}{-1} = -3$. **Discontinuidad evitable** en $x=1$ (agujero en $y=-3$).  
   > En $x = 2$: numerador simplificado $= x+2 = 4 \neq 0$. $\displaystyle\lim_{x\to 2^+}\dfrac{x+2}{x-2} = +\infty$; $\displaystyle\lim_{x\to 2^-}\dfrac{x+2}{x-2} = -\infty$. **Asíntota vertical** $x = 2$.

**Test de Opción Múltiple**

6. Una función racional tiene asíntota vertical en $x = a$ cuando:
   - a) El numerador se anula en $x = a$
   - b) El denominador se anula en $x = a$ y el numerador no
   - c) Tanto numerador como denominador se anulan en $x = a$
   - d) La función no está definida en $x = a$

   > **Respuesta correcta: b)** Si el numerador también se anula, puede haber discontinuidad evitable (se simplifica el factor). Solo hay asíntota vertical cuando solo el denominador se anula.

7. Si $\displaystyle\lim_{x\to a^+}f(x) = +\infty$ y $\displaystyle\lim_{x\to a^-}f(x) = +\infty$, entonces:
   - a) La recta $x = a$ es asíntota vertical
   - b) La recta $y = a$ es asíntota horizontal
   - c) $f(a) = +\infty$
   - d) $f$ tiene un máximo en $x = a$

   > **Respuesta correcta: a)** La recta vertical $x = a$ es asíntota vertical de la función (ambas ramas tienden a $+\infty$, en este caso por el mismo lado).

---

#### 6.3.4 Asíntota oblicua: condición de existencia y cálculo de m y n

**Ejercicio Resuelto**

Halla la asíntota oblicua de $f(x) = \dfrac{x^2 - 3x + 2}{x + 1}$.

**Solución:**

Una función tiene asíntota oblicua $y = mx + n$ cuando $\displaystyle\lim_{x\to\infty}[f(x) - (mx+n)] = 0$.

Las asíntotas oblicuas existen cuando el grado del numerador supera en exactamente 1 al del denominador.

**Paso 1:** Calcular $m$:
$$m = \lim_{x\to+\infty}\frac{f(x)}{x} = \lim_{x\to+\infty}\frac{x^2-3x+2}{x(x+1)} = \lim_{x\to+\infty}\frac{x^2-3x+2}{x^2+x} = 1$$

**Paso 2:** Calcular $n$:
$$n = \lim_{x\to+\infty}[f(x) - mx] = \lim_{x\to+\infty}\left[\frac{x^2-3x+2}{x+1} - x\right] = \lim_{x\to+\infty}\frac{x^2-3x+2 - x(x+1)}{x+1}$$

$$= \lim_{x\to+\infty}\frac{x^2-3x+2 - x^2 - x}{x+1} = \lim_{x\to+\infty}\frac{-4x+2}{x+1} = -4$$

**Asíntota oblicua:** $y = x - 4$

**Verificación mediante división:** $\dfrac{x^2-3x+2}{x+1}$. Dividiendo: $x^2-3x+2 = (x+1)(x-4)+6$. Luego $f(x) = x-4+\dfrac{6}{x+1}$, que confirma la asíntota $y = x-4$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla la asíntota oblicua de $f(x) = \dfrac{x^2+1}{x}$.

   > **Solución:** División: $\dfrac{x^2+1}{x} = x + \dfrac{1}{x}$. Asíntota oblicua: $y = x$.

2. Determina la asíntota oblicua de $g(x) = \dfrac{x^2-x+3}{x-2}$.

   > **Solución:** División polinómica: $x^2-x+3 = (x-2)(x+1)+5$. Luego $g(x) = x+1+\dfrac{5}{x-2}$.  
   > Asíntota oblicua: $y = x+1$.

**Nivel Intermedio:**

3. Halla todas las asíntotas de $f(x) = \dfrac{x^2}{x+1}$.

   > **Solución:** AV: $x = -1$. AH: no hay (grado num. $>$ grado den.). AO: $m=1$, $n = \lim(f(x)-x)=\lim\dfrac{x^2-(x^2+x)}{x+1}=\lim\dfrac{-x}{x+1}=-1$. Asíntota oblicua: $y=x-1$.

4. ¿Cuándo existe asíntota oblicua pero no asíntota horizontal en una función racional?

   > **Solución:** Cuando el grado del numerador supera en exactamente $1$ al del denominador. En ese caso:  
   > - Si $\deg(\text{num}) = \deg(\text{den})$: asíntota horizontal  
   > - Si $\deg(\text{num}) = \deg(\text{den}) + 1$: asíntota oblicua  
   > - Si $\deg(\text{num}) > \deg(\text{den}) + 1$: ni AH ni AO

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \dfrac{2x^2-x+1}{x-1}$.

   a) Halla el dominio y las asíntotas verticales.  
   b) Determina las asíntotas oblicuas (comprueba que no hay horizontales).  
   c) Calcula $f'(x)$ y determina si hay extremos relativos.

   > **Solución:**
   >
   > **a)** Dom $= \mathbb{R}\setminus\{1\}$. AV: $x=1$ (num. en $x=1$: $2-1+1=2\neq 0$).
   >
   > **b)** División: $2x^2-x+1 = (x-1)(2x+1)+2$. Luego $f(x) = 2x+1+\dfrac{2}{x-1}$.  
   > AO: $y = 2x+1$.  
   > No hay AH porque el grado del numerador ($2$) supera al del denominador ($1$) en más de $0$.
   >
   > **c)** $f'(x) = \left(2x+1+\dfrac{2}{x-1}\right)' = 2 - \dfrac{2}{(x-1)^2}$.  
   > $f'(x) = 0 \Rightarrow 2 = \dfrac{2}{(x-1)^2} \Rightarrow (x-1)^2 = 1 \Rightarrow x = 0$ o $x = 2$.  
   > $f''(x) = \dfrac{4}{(x-1)^3}$. $f''(0) = \dfrac{4}{-1} = -4 < 0$: **máximo relativo** en $x=0$, $f(0)=-1$.  
   > $f''(2) = \dfrac{4}{1} = 4 > 0$: **mínimo relativo** en $x=2$, $f(2)=5$.

**Test de Opción Múltiple**

6. La fórmula para calcular la pendiente $m$ de la asíntota oblicua es:
   - a) $m = \displaystyle\lim_{x\to\infty}f(x)$
   - b) $m = \displaystyle\lim_{x\to\infty}\dfrac{f(x)}{x}$
   - c) $m = f'(0)$
   - d) $m = \displaystyle\lim_{x\to\infty}f'(x)$

   > **Respuesta correcta: b)** La pendiente de la asíntota oblicua se calcula como $m = \lim_{x\to\infty}\dfrac{f(x)}{x}$.

7. La función $f(x) = \dfrac{x^3+1}{x^2}$:
   - a) Tiene asíntota horizontal $y=0$
   - b) Tiene asíntota oblicua $y=x$
   - c) No tiene asíntotas oblicuas ni horizontales
   - d) Tiene asíntota horizontal $y=1$

   > **Respuesta correcta: b)** $f(x) = x + \dfrac{1}{x^2}$. La asíntota oblicua es $y = x$ (el resto $1/x^2\to 0$).

---

#### 6.3.5 Asíntotas de funciones racionales

**Ejercicio Resuelto**

Determina todas las asíntotas de $f(x) = \dfrac{x^2+2x}{x^2-1}$ y describe el comportamiento de $f$ cerca de cada una.

**Solución:**

**Asíntotas verticales:** $x^2-1 = (x-1)(x+1) = 0 \Rightarrow x = 1, x = -1$.
- $x^2+2x = x(x+2)$: en $x=1$: $1\cdot3=3\neq0$; en $x=-1$: $(-1)(1)=-1\neq0$.
- AV: $x = 1$ y $x = -1$.

**Asíntota horizontal** (mismos grados): $\displaystyle\lim_{x\to\pm\infty}\dfrac{x^2+2x}{x^2-1} = 1$. AH: $y = 1$.

(No hay AO porque el límite horizontal existe con valor finito.)

**Comportamiento cerca de las AV:**
- Cerca de $x=1$: $f(x) \approx \dfrac{3}{(x-1)\cdot 2}$. Para $x\to1^+$: $+\infty$; para $x\to1^-$: $-\infty$.
- Cerca de $x=-1$: $f(x) \approx \dfrac{-1}{(x+1)\cdot(-2)} = \dfrac{1}{2(x+1)}$. Para $x\to-1^+$: $+\infty$; para $x\to-1^-$: $-\infty$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla todas las asíntotas de $f(x) = \dfrac{1}{x-3}$.

   > **Solución:** AV: $x=3$. AH: $y=0$ (grado num. $<$ grado den.).

2. Determina las asíntotas de $g(x) = \dfrac{2x+1}{x+2}$.

   > **Solución:** AV: $x=-2$. AH: $y=2$ (mismos grados; $2/1=2$).

**Nivel Intermedio:**

3. Halla todas las asíntotas de $f(x) = \dfrac{x^2-4}{x-1}$.

   > **Solución:** AV: $x=1$ (num. en $x=1$: $1-4=-3\neq0$). No AH (grado num. $>$ grado den.).  
   > División: $x^2-4 = (x-1)(x+1)-3$, luego AO: $y=x+1$.

4. Analiza las asíntotas de $h(x) = \dfrac{x^3}{x^2-4}$.

   > **Solución:** AV: $x=2$ y $x=-2$. No AH. Grado num. - grado den. $=1$: AO.  
   > $m = \lim\dfrac{x^3}{x(x^2-4)} = \lim\dfrac{x^2}{x^2-4} = 1$. $n = \lim(f(x)-x) = \lim\dfrac{x^3-x(x^2-4)}{x^2-4} = \lim\dfrac{4x}{x^2-4} = 0$.  
   > AO: $y = x$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Estudia completamente las asíntotas de $f(x) = \dfrac{x^2-x-6}{x^2-4}$ e indica qué tipo de discontinuidad tiene en cada punto singular.

   > **Solución:**
   >
   > Factorizamos: $x^2-x-6 = (x-3)(x+2)$ y $x^2-4 = (x-2)(x+2)$.
   >
   > Puntos singulares: $x = 2$ y $x = -2$.
   >
   > **En $x = -2$:** Numerador $= 0$ también. $f(x) = \dfrac{(x-3)(x+2)}{(x-2)(x+2)} = \dfrac{x-3}{x-2}$ para $x\neq-2$.  
   > $\displaystyle\lim_{x\to-2}\dfrac{x-3}{x-2} = \dfrac{-5}{-4} = \dfrac{5}{4}$. **Discontinuidad evitable** (agujero en $y=5/4$).
   >
   > **En $x = 2$:** Numerador simplificado $= x-3 = -1\neq 0$. AV: $x=2$.  
   > $\displaystyle\lim_{x\to2^+}\dfrac{x-3}{x-2} = \dfrac{-1}{0^+} = -\infty$; $\displaystyle\lim_{x\to2^-}\dfrac{x-3}{x-2} = \dfrac{-1}{0^-} = +\infty$.
   >
   > **AH:** $\displaystyle\lim_{x\to\pm\infty}\dfrac{x-3}{x-2} = 1$. AH: $y=1$.
   >
   > **Resumen:** AV: $x=2$; AH: $y=1$; discontinuidad evitable en $x=-2$.

**Test de Opción Múltiple**

6. Una función racional irreducible (sin factores comunes entre numerador y denominador) de grado $3$ en numerador y $3$ en denominador:
   - a) Tiene asíntota oblicua
   - b) Tiene asíntota horizontal $y=0$
   - c) Tiene asíntota horizontal igual al cociente de los coeficientes líderes
   - d) No tiene ninguna asíntota

   > **Respuesta correcta: c)** Mismo grado: la asíntota horizontal es el cociente de los coeficientes del término de mayor grado.

7. Si $f(x) = \dfrac{p(x)}{q(x)}$ con $\deg p = 4$ y $\deg q = 2$, entonces:
   - a) Tiene asíntota horizontal
   - b) Tiene asíntota oblicua
   - c) No tiene asíntotas en el infinito
   - d) Tiene asíntota oblicua cuadrática

   > **Respuesta correcta: c)** Con grado de numerador $= 4$ y denominador $= 2$, la diferencia es $2 > 1$, por lo que **no hay ni asíntota horizontal ni oblicua** (el cociente crece sin límite).

---

#### 6.3.6 Asíntotas de funciones definidas a trozos

**Ejercicio Resuelto**

Determina las asíntotas de $f(x) = \begin{cases} \dfrac{x^2-1}{x+1} & \text{si } x < 1 \\ \dfrac{2x}{x-3} & \text{si } x \geq 1 \end{cases}$

**Solución:**

**Asíntotas verticales:**
- Para $x < 1$: $\dfrac{x^2-1}{x+1} = \dfrac{(x-1)(x+1)}{x+1} = x-1$ (para $x \neq -1$). En $x = -1 < 1$: hay discontinuidad evitable ($\lim = -2$, no AV).
- Para $x \geq 1$: $\dfrac{2x}{x-3}$. En $x=3\geq 1$: numerador $= 6\neq 0$. **AV: $x = 3$**.

**Asíntotas horizontales:**
- Cuando $x \to -\infty$ (rama $x<1$): $f(x) = x-1 \to -\infty$. No hay AH en $-\infty$.
- Cuando $x \to +\infty$ (rama $x\geq 1$): $\displaystyle\lim_{x\to+\infty}\dfrac{2x}{x-3} = 2$. **AH: $y = 2$** en $+\infty$.

**Asíntota oblicua (en $-\infty$):** La rama $x < 1$ es $f(x) = x - 1$ (una recta). En sentido estricto, $y = x - 1$ **es ella misma la asíntota** (o mejor: la función es una recta para $x < 1$, no una asíntota separada de ella).

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla las asíntotas horizontales de $f(x) = \begin{cases} e^x & \text{si } x < 0 \\ \dfrac{x+1}{x+2} & \text{si } x \geq 0 \end{cases}$

   > **Solución:**  
   > $x\to-\infty$: $e^x\to 0$. AH: $y=0$ en $-\infty$.  
   > $x\to+\infty$: $\dfrac{x+1}{x+2}\to 1$. AH: $y=1$ en $+\infty$.

2. Determina si $g(x) = \begin{cases} \ln x & \text{si } x > 0 \\ x^2 & \text{si } x \leq 0 \end{cases}$ tiene asíntotas verticales.

   > **Solución:** Para $x\leq 0$: $x^2$ es continua, sin singularidades.  
   > Para $x>0$: $\ln x$ con $\displaystyle\lim_{x\to 0^+}\ln x = -\infty$. **AV: $x=0$** (por la derecha).

**Nivel Intermedio:**

3. Halla todas las asíntotas de $f(x) = \begin{cases} \dfrac{1}{x} & \text{si } x < -1 \\ 2 & \text{si } -1\leq x\leq 1 \\ \dfrac{x^2}{x+1} & \text{si } x > 1 \end{cases}$

   > **Solución:**  
   > **AV:** Para $x<-1$: $1/x$ sin ceros del den. Para $x>1$: $\dfrac{x^2}{x+1}$, den. $=0$ en $x=-1\notin(1,+\infty)$. Sin AV.  
   > **AH en $-\infty$:** $\lim_{x\to-\infty}1/x=0$. AH: $y=0$.  
   > **AO en $+\infty$:** $\dfrac{x^2}{x+1}=x-1+\dfrac{1}{x+1}$. AO: $y=x-1$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \begin{cases} \dfrac{x^2-4}{x-2} & \text{si } x < 0 \\ \dfrac{3x+a}{x+b} & \text{si } x \geq 0 \end{cases}$

   a) Simplifica la primera rama y halla posibles discontinuidades para $x<0$.  
   b) Determina la asíntota horizontal de la segunda rama cuando $x\to+\infty$ en función de $a$ y $b$.  
   c) Si se requiere que la AH de la segunda rama sea $y=3$, ¿qué condición impone eso?

   > **Solución:**
   >
   > **a)** $\dfrac{x^2-4}{x-2}=\dfrac{(x-2)(x+2)}{x-2}=x+2$ para $x\neq 2$. Como la rama es $x<0$, no hay puntos problemáticos (el agujero sería en $x=2>0$, fuera del dominio de la rama). Sin discontinuidades para $x<0$.
   >
   > **b)** $\displaystyle\lim_{x\to+\infty}\dfrac{3x+a}{x+b} = 3$ (mismos grados, cociente de coef. líderes $=3/1=3$).
   >
   > **c)** Independientemente de $a$ y $b$ (con $b\neq 0$ para el dominio), la AH en $+\infty$ **siempre es $y=3$**. La condición ya se cumple para cualquier $a, b$.

**Test de Opción Múltiple**

6. Una función definida a trozos puede tener:
   - a) Como máximo una asíntota horizontal
   - b) Como máximo una asíntota vertical
   - c) Asíntotas diferentes en $+\infty$ y $-\infty$
   - d) Solo asíntotas horizontales

   > **Respuesta correcta: c)** Al tener distintas expresiones para $x\to+\infty$ y $x\to-\infty$, puede tener asíntotas horizontales diferentes (o incluso oblicua en un lado y horizontal en el otro).

7. Si $f(x) = e^{-|x|}$, entonces:
   - a) Tiene asíntota vertical en $x=0$
   - b) Tiene asíntota horizontal $y=0$ solo en $+\infty$
   - c) Tiene asíntota horizontal $y=0$ en ambos infinitos
   - d) Tiene asíntota oblicua

   > **Respuesta correcta: c)** $e^{-|x|}\to 0$ tanto cuando $x\to+\infty$ ($|x|=x$) como cuando $x\to-\infty$ ($|x|=-x$).

---

## 6.4 Continuidad de funciones

---

#### 6.4.1 Definición de continuidad en un punto: las tres condiciones

**Ejercicio Resuelto**

Estudia la continuidad de $f(x) = \begin{cases} \dfrac{x^2-4}{x-2} & \text{si } x \neq 2 \\ 5 & \text{si } x = 2 \end{cases}$ en $x = 2$.

**Solución:**

Una función es continua en $x = a$ si se cumplen **las tres condiciones**:
1. $f(a)$ existe (la función está definida en $a$)
2. $\displaystyle\lim_{x\to a}f(x)$ existe
3. $\displaystyle\lim_{x\to a}f(x) = f(a)$

**Condición 1:** $f(2) = 5$. ✓ (definida)

**Condición 2:** $\displaystyle\lim_{x\to 2}\dfrac{x^2-4}{x-2} = \lim_{x\to 2}\dfrac{(x-2)(x+2)}{x-2} = \lim_{x\to 2}(x+2) = 4$. ✓ (el límite existe y vale $4$)

**Condición 3:** $\displaystyle\lim_{x\to 2}f(x) = 4 \neq 5 = f(2)$. ✗

La función **no es continua** en $x = 2$: el límite existe pero no coincide con el valor de la función. Es una **discontinuidad evitable**.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Comprueba si $f(x) = x^2 - 3x + 2$ es continua en $x = 1$.

   > **Solución:** Es un polinomio, continuo en todo $\mathbb{R}$.  
   > (1) $f(1) = 1-3+2 = 0$. (2) $\lim_{x\to1}f(x)=0$. (3) Son iguales. **Continua**.

2. Estudia la continuidad de $g(x) = \dfrac{x+1}{x-3}$ en $x = 3$.

   > **Solución:** $g(3)$ no está definida (denominador $=0$). Falla la condición 1. **Discontinua** en $x=3$.

**Nivel Intermedio:**

3. Estudia la continuidad de $f(x) = \begin{cases} x+1 & \text{si } x<2 \\ 3 & \text{si } x=2 \\ 2x-1 & \text{si } x>2 \end{cases}$ en $x=2$.

   > **Solución:** (1) $f(2)=3$. (2) $\lim_{x\to2^-}(x+1)=3$ y $\lim_{x\to2^+}(2x-1)=3$: límite $=3$. (3) $3=3$. **Continua** en $x=2$.

4. Determina el valor de $k$ para que $f(x) = \begin{cases} kx+1 & \text{si } x\leq 2 \\ x^2-1 & \text{si } x>2 \end{cases}$ sea continua en $x=2$.

   > **Solución:** $\lim_{x\to2^-}(kx+1)=2k+1$; $\lim_{x\to2^+}(x^2-1)=3$; $f(2)=2k+1$.  
   > Para continuidad: $2k+1=3 \Rightarrow k=1$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \begin{cases} \dfrac{x^2-1}{x-1} & \text{si } x < 1 \\ a & \text{si } x = 1 \\ 2x - b & \text{si } x > 1 \end{cases}$

   a) Calcula $\displaystyle\lim_{x\to 1^-}f(x)$.  
   b) Calcula $\displaystyle\lim_{x\to 1^+}f(x)$ en función de $b$.  
   c) Determina $a$ y $b$ para que $f$ sea continua en $x = 1$.

   > **Solución:**
   >
   > **a)** $\dfrac{x^2-1}{x-1} = x+1 \to 2$.
   >
   > **b)** $2(1)-b = 2-b$.
   >
   > **c)** Para que exista el límite: $2 = 2-b \Rightarrow b=0$.  
   > Para continuidad: $f(1) = a = \lim_{x\to1}f(x) = 2 \Rightarrow a=2$.  
   > **$a = 2$, $b = 0$**.

**Test de Opción Múltiple**

6. Las tres condiciones de continuidad de $f$ en $x = a$ son:
   - a) $f(a)$ existe, el límite existe, y $f'(a)$ existe
   - b) $f(a)$ existe, $\lim_{x\to a}f(x)$ existe, y $\lim_{x\to a}f(x)=f(a)$
   - c) $f(a)$ existe y $f'(a)$ existe
   - d) $\lim_{x\to a^-}f(x)=f(a)$ solamente

   > **Respuesta correcta: b)** Son exactamente las tres condiciones que definen la continuidad en un punto.

7. Si $f(a)$ existe pero $\displaystyle\lim_{x\to a}f(x)\neq f(a)$, entonces $f$:
   - a) Es continua en $a$
   - b) Tiene una discontinuidad de salto en $a$
   - c) Tiene una discontinuidad evitable en $a$
   - d) Tiene una asíntota en $a$

   > **Respuesta correcta: c)** Si el límite existe pero no coincide con $f(a)$ (o si $f(a)$ no está definida pero el límite sí existe), la discontinuidad es **evitable** (basta redefinir $f(a)=L$).

---

#### 6.4.2 Tipos de discontinuidad: evitable, de salto finito, de salto infinito (esencial)

**Ejercicio Resuelto**

Clasifica las discontinuidades de $f(x) = \dfrac{x^2-x-2}{x^2-3x+2}$.

**Solución:**

**Dominio:** $x^2-3x+2=(x-1)(x-2)=0 \Rightarrow x=1,\, x=2$.

Factorizamos el numerador: $x^2-x-2=(x-2)(x+1)$.

$$f(x) = \frac{(x-2)(x+1)}{(x-1)(x-2)} = \frac{x+1}{x-1} \quad (x\neq 2)$$

**En $x=2$:** Ambos factores se anulan; simplificando, $\displaystyle\lim_{x\to2}\dfrac{x+1}{x-1}=\dfrac{3}{1}=3$. El límite existe y es finito. $\Rightarrow$ **Discontinuidad evitable** en $x=2$.

**En $x=1$:** Solo el denominador se anula ($x+1|_{x=1}=2\neq0$).
- $\displaystyle\lim_{x\to1^+}\dfrac{x+1}{x-1}=+\infty$, $\displaystyle\lim_{x\to1^-}\dfrac{x+1}{x-1}=-\infty$.
$\Rightarrow$ **Discontinuidad de salto infinito** (esencial / asíntota vertical) en $x=1$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Clasifica la discontinuidad de $f(x) = \begin{cases} x+1 & \text{si } x<0 \\ x-1 & \text{si } x\geq 0 \end{cases}$ en $x=0$.

   > **Solución:** $\lim_{x\to0^-}(x+1)=1$; $\lim_{x\to0^+}(x-1)=-1$. Límites laterales distintos y finitos.  
   > **Discontinuidad de salto finito** (salto $= |1-(-1)|=2$).

2. Clasifica la discontinuidad de $g(x) = \begin{cases} \dfrac{\sin x}{x} & \text{si } x\neq 0 \\ 2 & \text{si } x=0 \end{cases}$

   > **Solución:** $\lim_{x\to0}\dfrac{\sin x}{x}=1$, pero $g(0)=2\neq1$. Límite existe, pero $\neq g(0)$.  
   > **Discontinuidad evitable** (bastaría definir $g(0)=1$).

**Nivel Intermedio:**

3. Clasifica todas las discontinuidades de $h(x) = \dfrac{x^2-4}{x(x-2)}$.

   > **Solución:** Denominador $=0$ en $x=0$ y $x=2$. $x^2-4=(x-2)(x+2)$.  
   > $h(x)=\dfrac{(x-2)(x+2)}{x(x-2)}=\dfrac{x+2}{x}$ para $x\neq2$.  
   > En $x=2$: $\lim=\dfrac{4}{2}=2$: **discontinuidad evitable**.  
   > En $x=0$: $\lim_{x\to0^+}\dfrac{x+2}{x}=+\infty$, $\lim_{x\to0^-}=-\infty$: **discontinuidad esencial** (salto infinito).

4. ¿Puede una función tener límite en $x=a$ y aun así ser discontinua? Da un ejemplo.

   > **Solución:** Sí. Por ejemplo $f(x)=\begin{cases}x^2&x\neq1\\ 5&x=1\end{cases}$:  
   > $\lim_{x\to1}f(x)=1$ pero $f(1)=5\neq1$. El límite existe pero no coincide con el valor. **Discontinuidad evitable**.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Clasifica todas las discontinuidades de:
   $$f(x) = \begin{cases} \dfrac{1}{x+1} & \text{si } x < 0 \\ x^2 - 1 & \text{si } 0 \leq x < 2 \\ \dfrac{x-2}{x^2-4} & \text{si } x \geq 2 \end{cases}$$

   > **Solución:**
   >
   > **En $x=0$ (cambio de rama):**  
   > $\lim_{x\to0^-}\dfrac{1}{x+1}=1$; $\lim_{x\to0^+}(x^2-1)=-1$; $f(0)=0-1=-1$.  
   > Límites laterales distintos: **discontinuidad de salto finito** en $x=0$.
   >
   > **En $x=-1$** (den. $=0$ en la primera rama para $x<0$):  
   > $\lim_{x\to-1}\dfrac{1}{x+1}=\pm\infty$: **discontinuidad esencial** en $x=-1$.
   >
   > **En $x=2$ (cambio de rama y punto singular):**  
   > Tercera rama: $\dfrac{x-2}{x^2-4}=\dfrac{x-2}{(x-2)(x+2)}=\dfrac{1}{x+2}$ para $x\neq2$.  
   > $\lim_{x\to2^+}\dfrac{1}{x+2}=\dfrac{1}{4}$; segunda rama: $\lim_{x\to2^-}(x^2-1)=3$; $f(2)=\dfrac{1}{4}$.  
   > Límites laterales distintos: **discontinuidad de salto finito** en $x=2$ (salto $= |3-1/4|=11/4$).

**Test de Opción Múltiple**

6. Una discontinuidad evitable en $x=a$ significa que:
   - a) La función tiende a $\pm\infty$ en $a$
   - b) El límite no existe en $a$
   - c) El límite existe pero $f(a)$ no está definida o no coincide con él
   - d) Los límites laterales son distintos y finitos

   > **Respuesta correcta: c)** La discontinuidad evitable se caracteriza porque $\lim_{x\to a}f(x)$ existe (finito), pero o bien $f(a)$ no está definida, o bien $f(a)\neq\lim f$.

7. Una discontinuidad de salto finito en $x=a$ ocurre cuando:
   - a) $\lim_{x\to a}f(x) = \pm\infty$
   - b) Los límites laterales existen, son finitos, pero son distintos
   - c) $f(a)$ no está definida y el límite tampoco
   - d) La función es periódica

   > **Respuesta correcta: b)** El "salto" finito implica que los límites laterales son números reales distintos: $\lim_{x\to a^-}f(x)\neq\lim_{x\to a^+}f(x)$, ambos finitos.

---

#### 6.4.3 Continuidad de funciones elementales y continuidad en un intervalo

**Ejercicio Resuelto**

Determina el dominio de continuidad de $f(x) = \dfrac{\ln(x-1)}{x^2 - 5x + 6}$.

**Solución:**

La función es cociente de funciones elementales. Es continua donde:
1. Esté definida (dominio natural)
2. El denominador no se anule

**Dominio natural:**
- $\ln(x-1)$ exige $x - 1 > 0 \Rightarrow x > 1$
- $x^2-5x+6 = (x-2)(x-3) \neq 0 \Rightarrow x \neq 2, x \neq 3$

**Dom$(f) = (1, 2) \cup (2, 3) \cup (3, +\infty)$**

En todo este dominio, $f$ es continua (como cociente de funciones continuas en el dominio, con denominador no nulo).

En $x = 2$ y $x = 3$: discontinuidades de salto infinito (asíntotas verticales).
En $x = 1$: no pertenece al dominio; $\displaystyle\lim_{x\to1^+}\ln(x-1) = -\infty$ (asíntota vertical en $x=1$).

**Conclusión:** $f$ es continua en $(1,2)\cup(2,3)\cup(3,+\infty)$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Indica los intervalos de continuidad de $f(x) = \sqrt{x^2-4}$.

   > **Solución:** $x^2-4\geq0 \Rightarrow x\leq-2$ o $x\geq2$. Dom $= (-\infty,-2]\cup[2,+\infty)$.  
   > $f$ es continua en $(-\infty,-2)\cup(2,+\infty)$ (interior del dominio) y también en los extremos $\pm2$ (continuidad lateral).

2. ¿Dónde es continua $g(x) = \dfrac{1}{x^2-1}$?

   > **Solución:** Den. $=0$ en $x=\pm1$. Dom $= \mathbb{R}\setminus\{-1,1\}$.  
   > $g$ es continua en $(-\infty,-1)\cup(-1,1)\cup(1,+\infty)$.

**Nivel Intermedio:**

3. Determina los intervalos de continuidad de $h(x) = \arcsin(2x-1)$.

   > **Solución:** $\arcsin(u)$ es continua para $u\in[-1,1]$. Necesitamos $-1\leq 2x-1\leq1 \Rightarrow 0\leq x\leq1$.  
   > $h$ es continua en $[0,1]$.

4. Justifica que toda función polinómica es continua en $\mathbb{R}$.

   > **Solución:** Un polinomio $p(x) = a_nx^n+\cdots+a_0$ es suma de monomios $a_kx^k$. La función $x^k$ es continua (producto de funciones continuas), y la suma de funciones continuas es continua. Además, para polinomios podemos sustituir directamente: $\lim_{x\to a}p(x)=p(a)$ para todo $a\in\mathbb{R}$. Por tanto $p$ es continua en todo $\mathbb{R}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \dfrac{\sqrt{x+2}}{(x-1)(x+3)}$.

   a) Determina el dominio de $f$.  
   b) Estudia la continuidad en los puntos del borde del dominio o de discontinuidad.  
   c) Indica los intervalos de continuidad.

   > **Solución:**
   >
   > **a)** $\sqrt{x+2}$ requiere $x\geq-2$; den. $\neq0\Rightarrow x\neq1,-3$.  
   > Como $-3<-2$, la restricción $x\geq-2$ ya excluye $x=-3$.  
   > Dom $= [-2,1)\cup(1,+\infty)$.
   >
   > **b)** En $x=-2$: $\displaystyle\lim_{x\to-2^+}f(x) = \dfrac{0}{(-3)(1)} = 0$: continua en $x=-2$ (extremo del dominio).  
   > En $x=1$: den. $=0$, num. $=\sqrt{3}\neq0$. AV: discontinuidad esencial.
   >
   > **c)** $f$ es continua en $[-2,1)\cup(1,+\infty)$.

**Test de Opción Múltiple**

6. ¿Cuál de estas afirmaciones sobre continuidad de funciones elementales es CORRECTA?
   - a) $\ln x$ es continua en $\mathbb{R}$
   - b) $\sin x$ es continua solo en $[-\pi,\pi]$
   - c) $e^x$ es continua en $\mathbb{R}$
   - d) $\sqrt{x}$ es continua en $\mathbb{R}$

   > **Respuesta correcta: c)** $e^x$ es continua en todo $\mathbb{R}$. $\ln x$ solo es continua en $(0,+\infty)$; $\sin x$ es continua en $\mathbb{R}$; $\sqrt{x}$ solo en $[0,+\infty)$.

7. Decimos que $f$ es continua en el intervalo cerrado $[a,b]$ si:
   - a) Es continua en $(a,b)$, continua por la derecha en $a$ y por la izquierda en $b$
   - b) Es continua en $(a,b)$ solamente
   - c) $f(a)=f(b)$
   - d) Es derivable en $[a,b]$

   > **Respuesta correcta: a)** La continuidad en $[a,b]$ requiere continuidad en el interior $(a,b)$ más continuidad lateral en los extremos: $\lim_{x\to a^+}f(x)=f(a)$ y $\lim_{x\to b^-}f(x)=f(b)$.

---

#### 6.4.4 Estudio de continuidad de funciones definidas a trozos

**Ejercicio Resuelto**

Estudia la continuidad de:
$$f(x) = \begin{cases} x^2 - 2 & \text{si } x < -1 \\ x + 1 & \text{si } -1 \leq x \leq 2 \\ \dfrac{x^2-4}{x-2} & \text{si } x > 2 \end{cases}$$

**Solución:**

Los puntos problemáticos son los cambios de rama: $x = -1$ y $x = 2$.

**En $x = -1$:**
- $\displaystyle\lim_{x\to-1^-}(x^2-2) = 1-2 = -1$
- $\displaystyle\lim_{x\to-1^+}(x+1) = 0$
- $f(-1) = -1+1 = 0$

Los límites laterales son $-1 \neq 0$: **discontinuidad de salto finito** en $x = -1$.

**En $x = 2$:**
- $\displaystyle\lim_{x\to2^-}(x+1) = 3$
- $\dfrac{x^2-4}{x-2} = x+2$ para $x\neq2$, luego $\displaystyle\lim_{x\to2^+}(x+2) = 4$
- $f(2) = 2+1 = 3$

Los límites laterales son $3 \neq 4$: **discontinuidad de salto finito** en $x = 2$.

**Dentro de cada rama:** las funciones $x^2-2$, $x+1$ y $\dfrac{x^2-4}{x-2}$ son continuas en sus respectivos intervalos.

**Conclusión:** $f$ es continua en $\mathbb{R}\setminus\{-1, 2\}$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Estudia la continuidad de $f(x) = \begin{cases} 2x+1 & \text{si } x\leq1 \\ x^2+2 & \text{si } x>1 \end{cases}$ en $x=1$.

   > **Solución:** $\lim_{x\to1^-}(2x+1)=3$; $\lim_{x\to1^+}(x^2+2)=3$; $f(1)=3$.  
   > Todos iguales: **continua** en $x=1$.

2. Estudia la continuidad de $g(x)=\begin{cases} 3 & \text{si } x<0 \\ x+3 & \text{si } x\geq0 \end{cases}$ en $x=0$.

   > **Solución:** $\lim_{x\to0^-}3=3$; $\lim_{x\to0^+}(x+3)=3$; $f(0)=3$.  
   > Todos iguales: **continua** en $x=0$.

**Nivel Intermedio:**

3. Estudia la continuidad completa de $f(x)=\begin{cases}|x|+1&\text{si }x\leq0\\x^2-x+1&\text{si }x>0\end{cases}$.

   > **Solución:** Único punto de cambio: $x=0$.  
   > $\lim_{x\to0^-}(|x|+1)=\lim_{x\to0^-}(-x+1)=1$; $\lim_{x\to0^+}(x^2-x+1)=1$; $f(0)=1$.  
   > **Continua** en $x=0$ (y en todo $\mathbb{R}$ por la continuidad de cada rama).

4. Halla los puntos de discontinuidad de $f(x) = \begin{cases} \frac{1}{x} & \text{si } x<-1 \text{ o } x>1 \\ x^2 & \text{si } -1\leq x\leq1 \end{cases}$.

   > **Solución:** Puntos de cambio: $x=-1$ y $x=1$.  
   > En $x=-1$: $\lim_{x\to-1^-}\frac{1}{x}=-1$; $\lim_{x\to-1^+}x^2=1$; $f(-1)=1$. Límites distintos: **salto finito**.  
   > En $x=1$: $\lim_{x\to1^-}x^2=1$; $\lim_{x\to1^+}\frac{1}{x}=1$; $f(1)=1$. **Continua** en $x=1$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** $f(x) = \begin{cases}\dfrac{\sqrt{x+4}-2}{x} & \text{si }x\neq0 \\ k & \text{si }x=0\end{cases}$

   a) Calcula $\displaystyle\lim_{x\to0}f(x)$.  
   b) ¿Para qué valor de $k$ es $f$ continua en $x=0$?  
   c) Indica el tipo de discontinuidad si $k=1$.

   > **Solución:**
   >
   > **a)** Forma $\dfrac{0}{0}$. Racionalizando: $\dfrac{(\sqrt{x+4}-2)(\sqrt{x+4}+2)}{x(\sqrt{x+4}+2)} = \dfrac{x+4-4}{x(\sqrt{x+4}+2)} = \dfrac{1}{\sqrt{x+4}+2} \to \dfrac{1}{4}$.
   >
   > **b)** Para continuidad: $k = \dfrac{1}{4}$.
   >
   > **c)** Con $k=1$: el límite es $\dfrac{1}{4}$ pero $f(0)=1\neq\dfrac{1}{4}$. **Discontinuidad evitable**.

**Test de Opción Múltiple**

6. Para estudiar la continuidad de una función definida a trozos, los puntos que siempre deben analizarse son:
   - a) Los ceros de la función
   - b) Los puntos donde cambia la expresión de la función
   - c) Los puntos donde la derivada se anula
   - d) Los extremos del dominio

   > **Respuesta correcta: b)** Los únicos puntos donde puede haber discontinuidad son los cambios de expresión (y los puntos donde alguna rama no sea continua, como singularidades de funciones racionales).

7. Si en un cambio de rama en $x=c$, los dos límites laterales son iguales a $L$ y $f(c)=L$, entonces:
   - a) La función tiene discontinuidad evitable en $c$
   - b) La función tiene discontinuidad de salto en $c$
   - c) La función es continua en $c$
   - d) La función es derivable en $c$

   > **Respuesta correcta: c)** Se cumplen las tres condiciones de continuidad: límite existe, $f(c)$ existe, y son iguales.

---

#### 6.4.5 Cálculo de parámetros para que una función a trozos sea continua

**Ejercicio Resuelto**

Determina los valores de $a$ y $b$ para que la función sea continua en todo $\mathbb{R}$:
$$f(x) = \begin{cases} ax + 2 & \text{si } x < 1 \\ b & \text{si } x = 1 \\ x^2 + bx - a & \text{si } x > 1 \end{cases}$$

**Solución:**

Para continuidad en $x = 1$ se deben cumplir las tres condiciones. El límite debe existir y ser igual a $f(1)$.

**Límite por la izquierda:**
$$\lim_{x\to1^-}(ax+2) = a+2$$

**Límite por la derecha:**
$$\lim_{x\to1^+}(x^2+bx-a) = 1+b-a$$

**Valor en $x=1$:** $f(1) = b$

**Igualdad de límites laterales:**
$$a + 2 = 1 + b - a$$
$$2a - b = -1 \quad (1)$$

**Igualdad del límite con $f(1)$:**
$$a + 2 = b$$
$$b = a + 2 \quad (2)$$

**Sustituyendo (2) en (1):**
$$2a - (a+2) = -1 \Rightarrow a - 2 = -1 \Rightarrow a = 1$$

**De (2):** $b = 1 + 2 = 3$

**Verificación:** Con $a=1$, $b=3$:
- Límite iz.: $1+2=3$ ✓
- Límite der.: $1+3-1=3$ ✓
- $f(1)=3$ ✓

**Respuesta:** $a = 1$, $b = 3$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla $k$ para que $f(x)=\begin{cases}kx-1&\text{si }x\leq2\\x^2-1&\text{si }x>2\end{cases}$ sea continua en $x=2$.

   > **Solución:** $\lim_{x\to2^-}(kx-1)=2k-1$; $\lim_{x\to2^+}(x^2-1)=3$; $f(2)=2k-1$.  
   > $2k-1=3\Rightarrow k=2$.

2. Determina $m$ para que $g(x)=\begin{cases}mx^2&\text{si }x<1\\ 2x-1&\text{si }x\geq1\end{cases}$ sea continua en $\mathbb{R}$.

   > **Solución:** Solo hay que estudiar $x=1$:  
   > $\lim_{x\to1^-}mx^2=m$; $\lim_{x\to1^+}(2x-1)=1$; $f(1)=1$. $m=1$.

**Nivel Intermedio:**

3. Halla $a$ y $b$ para que $f(x)=\begin{cases}x^2+a&\text{si }x<0\\2&\text{si }x=0\\bx+3&\text{si }x>0\end{cases}$ sea continua en $x=0$.

   > **Solución:** $\lim_{x\to0^-}(x^2+a)=a$; $\lim_{x\to0^+}(bx+3)=3$; $f(0)=2$.  
   > Para que exista el límite: $a=3$. Para continuidad: $a=2$. Contradicción: $a=3$ y $a=2$.  
   > Replanteamos: la igualdad del límite implica $a=3$ y $f(0)=2\neq3$: **no puede hacerse continua** en $x=0$ para ningún valor de $b$ (dado que $f(0)=2$ es fijo). A menos que se permita cambiar $f(0)$.  
   > Si $f(0)$ pudiera ser libre: necesitaríamos $a=3$ y $b$ cualquiera. Con $a=3$: $f(0)=2\neq3$: discontinuidad evitable en $x=0$ para cualquier $b$ (límite $=3$, $f(0)=2$).

4. Determina $a$ y $b$ para que $h(x)=\begin{cases}3x+a&x\leq0\\ bx^2+2&x>0\end{cases}$ sea continua en $\mathbb{R}$, sabiendo que $h(-1)=2$.

   > **Solución:** $h(-1)=3(-1)+a=2\Rightarrow a=5$.  
   > Continuidad en $x=0$: $\lim_{x\to0^-}(3x+5)=5$; $\lim_{x\to0^+}(bx^2+2)=2$.  
   > $5=2$: imposible. La condición $h(-1)=2$ lleva a que $a=5$, pero la continuidad en $x=0$ requeriría $5=2$. **No hay solución** con $h(-1)=2$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** $f(x)=\begin{cases}\dfrac{x^2+ax+b}{x-1}&\text{si }x<1\\ x^2-2x+1&\text{si }x\geq1\end{cases}$

   Para que $f$ sea continua en $x=1$, se pide:  
   a) Calcula $\displaystyle\lim_{x\to1^+}f(x)$.  
   b) ¿Qué condición debe cumplir $\displaystyle\lim_{x\to1^-}\dfrac{x^2+ax+b}{x-1}$ para que exista y sea finito?  
   c) Halla $a$ y $b$.

   > **Solución:**
   >
   > **a)** $\lim_{x\to1^+}(x^2-2x+1)=1-2+1=0$.
   >
   > **b)** Para que $\displaystyle\lim_{x\to1^-}\dfrac{x^2+ax+b}{x-1}$ sea finito, el numerador debe anularse en $x=1$ (si no, sería $\pm\infty$). Condición: $1+a+b=0$, es decir, $a+b=-1$.
   >
   > **c)** Con $a+b=-1$: $x^2+ax+b = (x-1)(x+c)$ para algún $c$.  
   > Expandiendo: $(x-1)(x+c)=x^2+(c-1)x-c$. Comparando: $a=c-1$, $b=-c$.  
   > $\displaystyle\lim_{x\to1^-}\dfrac{(x-1)(x+c)}{x-1}=1+c$.  
   > Para continuidad: $1+c=0\Rightarrow c=-1$.  
   > Entonces $a=c-1=-2$ y $b=-c=1$.  
   > **$a=-2$, $b=1$** (verificación: $x^2-2x+1=(x-1)^2$, límite $=0=f(1^+)$ ✓).

**Test de Opción Múltiple**

6. Para que una función definida a trozos sea continua en el punto de cambio $x=c$, se necesita:
   - a) Solo que los límites laterales sean iguales
   - b) Solo que $f(c)$ esté definida
   - c) Que los límites laterales sean iguales entre sí y a $f(c)$
   - d) Que $f'(c)$ exista

   > **Respuesta correcta: c)** Las tres condiciones deben cumplirse simultáneamente.

7. Si en la función a trozos hay un parámetro en ambas ramas, el sistema de ecuaciones para determinar continuidad tiene:
   - a) Siempre solución única
   - b) El mismo número de ecuaciones que de incógnitas, por lo que puede tener 0, 1 o infinitas soluciones
   - c) Siempre infinitas soluciones
   - d) Siempre solución imposible

   > **Respuesta correcta: b)** Cada punto de cambio aporta una ecuación. Con dos incógnitas y dos puntos de cambio se obtiene un sistema $2\times2$ que puede ser compatible determinado, compatible indeterminado o incompatible.

---

## 6.5 Teoremas de continuidad

---

#### 6.5.1 Teorema de Bolzano: enunciado y aplicación a la existencia de raíces

**Ejercicio Resuelto**

Demuestra que la ecuación $x^3 - x - 2 = 0$ tiene al menos una raíz en el intervalo $[1, 2]$.

**Solución:**

**Teorema de Bolzano:** Si $f$ es continua en $[a,b]$ y $f(a)\cdot f(b) < 0$ (signos opuestos), entonces existe al menos un $c \in (a,b)$ tal que $f(c) = 0$.

Sea $f(x) = x^3 - x - 2$.

**Condiciones:**
1. $f$ es un polinomio $\Rightarrow$ continua en todo $\mathbb{R}$, en particular en $[1,2]$. ✓

2. Calculamos los valores en los extremos:
   - $f(1) = 1 - 1 - 2 = -2 < 0$
   - $f(2) = 8 - 2 - 2 = 4 > 0$

3. $f(1) \cdot f(2) = (-2)(4) = -8 < 0$. ✓

**Conclusión:** Por el Teorema de Bolzano, existe $c \in (1, 2)$ tal que $f(c) = 0$, es decir, la ecuación tiene al menos una raíz en $(1, 2)$.

**Acotación:** Como $f(1) < 0$ y $f(1{,}5) = 3{,}375 - 1{,}5 - 2 = -0{,}125 < 0$, y $f(2) > 0$, la raíz está en $(1{,}5, 2)$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Comprueba usando Bolzano que $f(x) = x^2 - 5$ tiene una raíz en $[2, 3]$.

   > **Solución:** $f(2) = 4-5 = -1 < 0$; $f(3) = 9-5 = 4 > 0$. Producto $< 0$, $f$ continua. Por Bolzano, existe raíz en $(2,3)$.  
   > (De hecho $c = \sqrt{5} \approx 2{,}236$.)

2. Usa Bolzano para demostrar que $e^x - 3x = 0$ tiene solución en $[0, 1]$.

   > **Solución:** $f(x)=e^x-3x$. $f(0)=1>0$; $f(1)=e-3\approx-0{,}282<0$. Producto $<0$, $f$ continua. Por Bolzano, existe raíz en $(0,1)$.

**Nivel Intermedio:**

3. Acota la raíz de $x^3+x-1=0$ en un intervalo de longitud $0{,}25$ usando Bolzano iterado.

   > **Solución:** $f(x)=x^3+x-1$.  
   > $f(0)=-1<0$; $f(1)=1>0$: raíz en $(0,1)$.  
   > $f(0{,}5)=0{,}125+0{,}5-1=-0{,}375<0$: raíz en $(0{,}5,1)$.  
   > $f(0{,}75)=0{,}422+0{,}75-1=0{,}172>0$: raíz en $(0{,}5,0{,}75)$.  
   > La raíz está en $(0{,}5, 0{,}75)$, intervalo de longitud $0{,}25$.

4. Demuestra que $\cos x = x$ tiene al menos una solución en $[0, \pi/2]$.

   > **Solución:** $f(x)=\cos x - x$. $f(0)=1-0=1>0$; $f(\pi/2)=0-\pi/2\approx-1{,}57<0$.  
   > Producto $<0$, $f$ continua. Por Bolzano, existe $c\in(0,\pi/2)$ con $\cos c = c$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = x^4 - 5x^2 + 4$.

   a) Factoriza $f(x)$ y halla sus raíces exactas.  
   b) Sin saber las raíces, aplica Bolzano para demostrar que existe al menos una raíz en $[0, 2]$.  
   c) Determina el número total de raíces reales de $f$.

   > **Solución:**
   >
   > **a)** $t=x^2$: $t^2-5t+4=(t-1)(t-4)=0\Rightarrow t=1,4$.  
   > $x^2=1\Rightarrow x=\pm1$; $x^2=4\Rightarrow x=\pm2$.  
   > Raíces: $x=-2, -1, 1, 2$.
   >
   > **b)** $f(0)=4>0$; $f(2)=16-20+4=0$. No es válido ($f(2)=0$, pero Bolzano da raíz en el extremo).  
   > Mejor: $f(0)=4>0$; $f(1{,}5)=5{,}0625-11{,}25+4=-2{,}1875<0$. Producto $<0$: raíz en $(0,1{,}5)\subset[0,2]$.
   >
   > **c)** $f$ tiene cuatro raíces reales: $-2, -1, 1, 2$.

**Test de Opción Múltiple**

6. Para aplicar el Teorema de Bolzano a $f$ en $[a,b]$, es necesario que:
   - a) $f(a)=0$ o $f(b)=0$
   - b) $f$ sea continua en $[a,b]$ y $f(a)\cdot f(b) < 0$
   - c) $f$ sea derivable en $(a,b)$
   - d) $f$ sea monótona en $[a,b]$

   > **Respuesta correcta: b)** Las condiciones del teorema son: continuidad en $[a,b]$ y que $f$ tome valores de distinto signo en los extremos.

7. El Teorema de Bolzano garantiza:
   - a) La unicidad de la raíz
   - b) Que la raíz es exactamente $\frac{a+b}{2}$
   - c) La existencia de al menos una raíz en $(a,b)$
   - d) Que la función es creciente en $(a,b)$

   > **Respuesta correcta: c)** Bolzano solo garantiza **existencia** (al menos una raíz), no unicidad ni localización exacta.

---

#### 6.5.2 Teorema del valor intermedio de Darboux: enunciado y aplicaciones

**Ejercicio Resuelto**

Demuestra que $f(x) = x^2 - 3x + 1$ toma el valor $-1$ en el intervalo $[0, 3]$.

**Solución:**

**Teorema del Valor Intermedio (Darboux):** Si $f$ es continua en $[a,b]$, entonces $f$ toma todos los valores comprendidos entre $f(a)$ y $f(b)$.

**Datos:**
- $f(0) = 0 - 0 + 1 = 1$
- $f(3) = 9 - 9 + 1 = 1$

**Hmm:** En este caso $f(0) = f(3) = 1$. El teorema diría que toma todos los valores entre $1$ y $1$... pero sabemos que $f$ tiene mínimo.

**Procedimiento correcto:** Calculamos $f$ en el vértice: $f'(x) = 2x-3 = 0 \Rightarrow x=3/2$.
$f(3/2) = 9/4 - 9/2 + 1 = -5/4 < -1$.

Aplicando Darboux en $[0, 3/2]$: $f(0)=1 > -1 > -5/4 = f(3/2)$. Como $f$ es continua y $-1$ está entre $f(0)$ y $f(3/2)$, por el TVI existe $c\in(0,3/2)$ con $f(c)=-1$.

**Verificación directa:** $x^2-3x+1=-1 \Rightarrow x^2-3x+2=0 \Rightarrow (x-1)(x-2)=0 \Rightarrow x=1$ o $x=2$.  
Efectivamente $x=1\in(0,3/2)$. ✓

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Usa el TVI para demostrar que $f(x) = x^3$ toma el valor $4$ en $[1, 2]$.

   > **Solución:** $f(1)=1<4<8=f(2)$. $f$ continua en $[1,2]$. Por TVI, $\exists c\in(1,2)$: $c^3=4$, es decir $c=\sqrt[3]{4}\approx1{,}587$.

2. ¿Toma $f(x)=\sin x$ el valor $0{,}5$ en $[0, \pi]$? Justifica.

   > **Solución:** $f(0)=0<0{,}5<1=f(\pi/2)$... mejor: $f$ continua, $f(0)=0$ y $f(\pi)=0$, con $f(\pi/6)=0{,}5$.  
   > Sí, por TVI (más directamente: $f(\pi/6)=0{,}5$ es el valor exacto).

**Nivel Intermedio:**

3. Prueba que $f(x)=e^x - 2$ toma todos los valores reales en $(-\infty,+\infty)$.

   > **Solución:** $\lim_{x\to-\infty}e^x-2=-2$ (tiende a $-2$ por arriba); de hecho $\lim_{x\to-\infty}f(x)=-2^+$ (más correctamente $-2$ por defecto, ya que $e^x>0$).  
   > Más correcto: $f$ continua en $\mathbb{R}$, $\lim_{x\to-\infty}f(x)=-2$, $\lim_{x\to+\infty}f(x)=+\infty$. $f$ toma todos los valores en $(-2,+\infty)$.

4. Demuestra que $f(x)=x^5-3x$ toma el valor $10$ en algún punto real.

   > **Solución:** $f(2)=32-6=26>10$; $f(1)=1-3=-2<10$.  
   > $f$ continua, $-2<10<26=f(2)$. Por TVI en $[1,2]$: $\exists c\in(1,2)$ con $f(c)=10$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x) = \dfrac{x^2+1}{x-2}$.

   a) Indica los intervalos de continuidad de $f$.  
   b) ¿Puede aplicarse el TVI a $f$ en el intervalo $[0, 4]$? ¿Por qué?  
   c) Demuestra que $f$ toma el valor $0$ en algún intervalo donde sea aplicable el TVI.

   > **Solución:**
   >
   > **a)** Dom $=\mathbb{R}\setminus\{2\}$. $f$ continua en $(-\infty,2)\cup(2,+\infty)$.
   >
   > **b)** No, porque $f$ es discontinua en $x=2\in[0,4]$. El TVI requiere continuidad en todo el intervalo.
   >
   > **c)** Tomamos $[3,5]$: $f(3)=\dfrac{10}{1}=10>0$ y $f(5)=\dfrac{26}{3}>0$. Ambos positivos, no sirve.  
   > Tomamos $[0, 1]$: $f(0)=\dfrac{1}{-2}=-\dfrac{1}{2}<0$ y $f(1)=\dfrac{2}{-1}=-2<0$. Ambos negativos, no sirve.  
   > La función no toma el valor $0$ (pues $x^2+1>0$ siempre). **No puede aplicarse** el TVI para el valor $0$ porque $f(x)\neq0$ para todo $x$.

**Test de Opción Múltiple**

6. El TVI6. El Teorema del Valor Intermedio (Darboux) garantiza que si $f$ es continua en $[a,b]$ y $k$ está entre $f(a)$ y $f(b)$, entonces:
   - a) $f$ es derivable en $(a,b)$
   - b) existe $c\in(a,b)$ tal que $f(c)=k$
   - c) $f$ tiene un extremo en $[a,b]$
   - d) $k=\dfrac{f(a)+f(b)}{2}$

   > **Respuesta correcta:** b) La conclusión del TVI es exactamente la existencia de $c\in(a,b)$ con $f(c)=k$.

7. Sea $f$ continua en $[0,1]$ con $f(0)=3$ y $f(1)=-1$. Por el TVI:
   - a) $f$ tiene un máximo en $(0,1)$
   - b) $f$ no tiene raíces
   - c) existe $c\in(0,1)$ tal que $f(c)=0$
   - d) $f$ es derivable en $(0,1)$

   > **Respuesta correcta:** c) Como $f(0)=3>0>-1=f(1)$ y $f$ es continua, el TVI garantiza la existencia de una raíz en $(0,1)$.

---

#### 6.5.3 Aplicación de Bolzano para acotación y separación de raíces

**Ejercicio Resuelto**

Sea $f(x) = x^3 - 2x^2 - x + 1$. Localiza y separa las raíces reales de $f$ en intervalos de longitud 1.

**Paso 1 — Verificar que $f$ es continua:** $f$ es un polinomio, continua en $\mathbb{R}$.

**Paso 2 — Evaluar en enteros consecutivos:**

$$f(-2)=(-8)-8+2+1=-13<0$$
$$f(-1)=(-1)-2+1+1=-1<0$$
$$f(0)=0-0-0+1=1>0$$
$$f(1)=1-2-1+1=-1<0$$
$$f(2)=8-8-2+1=-1<0$$
$$f(3)=27-18-3+1=7>0$$

**Paso 3 — Aplicar Bolzano:**

- En $[-1, 0]$: $f(-1)=-1<0<1=f(0)$ → **cambio de signo** → $\exists c_1\in(-1,0)$ raíz.
- En $[0, 1]$: $f(0)=1>0>-1=f(1)$ → **cambio de signo** → $\exists c_2\in(0,1)$ raíz.
- En $[2, 3]$: $f(2)=-1<0<7=f(3)$ → **cambio de signo** → $\exists c_3\in(2,3)$ raíz.

**Conclusión:** $f$ tiene exactamente 3 raíces reales (un polinomio de grado 3 tiene a lo sumo 3) en los intervalos $(-1,0)$, $(0,1)$ y $(2,3)$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Demuestra que $f(x) = x^2 - 5$ tiene una raíz en $(2, 3)$.

   > **Solución:** $f(2)=4-5=-1<0$ y $f(3)=9-5=4>0$. $f$ continua (polinomio). Por Bolzano, $\exists c\in(2,3)$ con $f(c)=0$, es decir $c=\sqrt{5}\approx2{,}236$.

2. Separa las raíces de $g(x)=x^3-x-1$ en intervalos $[n,n+1]$ con $n$ entero.

   > **Solución:** $g(-1)=-1+1-1=-1<0$, $g(0)=-1<0$, $g(1)=1-1-1=-1<0$, $g(2)=8-2-1=5>0$.  
   > Cambio de signo en $[1,2]$: por Bolzano, hay una raíz en $(1,2)$.  
   > (El polinomio tiene solo 1 raíz real, ya que el discriminante es negativo para las otras dos raíces, que son complejas.)

**Nivel Intermedio:**

3. Localiza tres raíces de $h(x)=\cos x - x$ en intervalos de longitud 1 (en radianes).

   > **Solución:** $h$ es continua. $h(0)=1>0$; $h(1)=\cos1-1\approx0{,}54-1=-0{,}46<0$.  
   > Cambio de signo en $[0,1]$: raíz en $(0,1)$. (Esta es la única raíz real de $\cos x=x$, el llamado "punto de Dottie".)  
   > Para verificar, $h(-\pi/2)=\cos(-\pi/2)+\pi/2=\pi/2>0$; $h(\pi)=\cos\pi-\pi=-1-\pi<0$. Confirmado el único cambio.

4. Sea $f(x)=e^x - 3x$. Encuentra dos intervalos de longitud 1 que contengan raíces.

   > **Solución:** $f(0)=1>0$; $f(1)=e-3\approx-0{,}28<0$ → cambio en $[0,1]$: raíz $c_1\in(0,1)$.  
   > $f(1)\approx-0{,}28<0$; $f(2)=e^2-6\approx7{,}39-6=1{,}39>0$ → cambio en $[1,2]$: raíz $c_2\in(1,2)$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=x^3-3x^2+1$.

   a) Calcula $f(-1)$, $f(0)$, $f(1)$, $f(2)$ y $f(3)$.  
   b) Usa el teorema de Bolzano para separar todas las raíces de $f$ en intervalos de longitud 1.  
   c) ¿Cuántas raíces reales tiene $f$? Justifica tu respuesta.

   > **Solución:**
   >
   > **a)** $f(-1)=-1-3-0+1=-3$. Corrección: $f(-1)=(-1)^3-3(-1)^2+1=-1-3+1=-3$.  
   > $f(0)=0-0+1=1$.  
   > $f(1)=1-3+1=-1$.  
   > $f(2)=8-12+1=-3$.  
   > $f(3)=27-27+1=1$.
   >
   > **b)** Cambios de signo:
   > - $f(-1)=-3<0<1=f(0)$: raíz en $(-1,0)$.
   > - $f(0)=1>0>-1=f(1)$: raíz en $(0,1)$.
   > - $f(2)=-3<0<1=f(3)$: raíz en $(2,3)$.
   >
   > **c)** $f$ tiene grado 3, por lo que tiene a lo sumo 3 raíces reales. Hemos detectado 3 cambios de signo, luego $f$ tiene **exactamente 3 raíces reales**, una en cada uno de los intervalos $(-1,0)$, $(0,1)$ y $(2,3)$.

**Test de Opción Múltiple**

6. Para aplicar el teorema de Bolzano a $f$ en $[a,b]$ y garantizar una raíz, se necesita:
   - a) Que $f$ sea derivable en $[a,b]$
   - b) Que $f$ sea continua en $[a,b]$ y que $f(a)\cdot f(b)<0$
   - c) Que $f(a)=0$ o $f(b)=0$
   - d) Que $f'(x)\neq0$ en $(a,b)$

   > **Respuesta correcta:** b) Bolzano requiere continuidad en $[a,b]$ y cambio de signo en los extremos ($f(a)\cdot f(b)<0$).

7. ¿En cuántos intervalos $[n, n+1]$ (con $n\in\mathbb{Z}$) garantiza Bolzano raíces para $f(x)=x^3-7x+6$?

   $(f(-3)=-27+21+6=0)$, $(f(-2)=-8+14+6=12)$, $(f(0)=6)$, $(f(1)=0)$, $(f(2)=8-14+6=0)$.

   - a) 1
   - b) 2
   - c) 3
   - d) 0

   > **Respuesta correcta:** d) Bolzano requiere $f(a)\cdot f(b)<0$. Aquí las 3 raíces son exactamente en $x=-3, 1, 2$, que son enteros; no hay cambio de signo estricto en ningún intervalo $[n,n+1]$. (Bolzano no puede aplicarse directamente, pero las raíces son $-3, 1, 2$.)

---

# CAPÍTULO 7 — DERIVADAS Y APLICACIONES

---

#### 7.1.1 Tasa de variación media e instantánea

**Ejercicio Resuelto**

Sea $f(x)=x^2+1$. Calcula la tasa de variación media de $f$ en el intervalo $[1, 3]$ y la tasa de variación instantánea en $x=1$.

**Paso 1 — Tasa de variación media (TVM):**

$$\text{TVM}_{[1,3]} = \frac{f(3)-f(1)}{3-1} = \frac{(9+1)-(1+1)}{2} = \frac{10-2}{2} = \frac{8}{2} = 4$$

Interpretación: entre $x=1$ y $x=3$, $f$ crece de media 4 unidades por unidad de $x$.

**Paso 2 — Tasa de variación instantánea (TVI en $x=1$):**

$$\text{TVI}_{x=1} = \lim_{h\to 0}\frac{f(1+h)-f(1)}{h} = \lim_{h\to 0}\frac{(1+h)^2+1-(2)}{h}$$

$$= \lim_{h\to 0}\frac{1+2h+h^2+1-2}{h} = \lim_{h\to 0}\frac{2h+h^2}{h} = \lim_{h\to 0}(2+h) = 2$$

**Conclusión:** La tasa de variación instantánea en $x=1$ es $2 = f'(1)$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula la TVM de $f(x)=3x-2$ en el intervalo $[0, 4]$.

   > **Solución:** $\text{TVM}=\dfrac{f(4)-f(0)}{4-0}=\dfrac{10-(-2)}{4}=\dfrac{12}{4}=3$.  
   > (Coherente: la pendiente de $f(x)=3x-2$ es siempre $3$.)

2. Un objeto se mueve según $s(t)=t^2+2t$ (metros, $t$ en segundos). Calcula la velocidad media entre $t=1$ y $t=3$.

   > **Solución:** $s(1)=1+2=3$; $s(3)=9+6=15$.  
   > Velocidad media $=\dfrac{15-3}{3-1}=\dfrac{12}{2}=6$ m/s.

**Nivel Intermedio:**

3. Calcula la TVM de $f(x)=x^3$ en $[1, 1+h]$ y simplifica.

   > **Solución:** $\dfrac{f(1+h)-f(1)}{h}=\dfrac{(1+h)^3-1}{h}=\dfrac{1+3h+3h^2+h^3-1}{h}=\dfrac{h(3+3h+h^2)}{h}=3+3h+h^2$.  
   > Cuando $h\to 0$, TVI $= 3 = f'(1)$.

4. La posición de un vehículo es $s(t)=5t^2-2t+1$ (m). Calcula la velocidad instantánea en $t=2$ usando la definición de derivada.

   > **Solución:** $f'(2)=\lim_{h\to0}\dfrac{s(2+h)-s(2)}{h}$.  
   > $s(2)=20-4+1=17$. $s(2+h)=5(2+h)^2-2(2+h)+1=5(4+4h+h^2)-4-2h+1=20+20h+5h^2-3-2h=17+18h+5h^2$.  
   > $\dfrac{17+18h+5h^2-17}{h}=18+5h \to 18$ m/s.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\dfrac{1}{x}$ definida en $(0,+\infty)$.

   a) Calcula la tasa de variación media en el intervalo $[1, 3]$.  
   b) Calcula la tasa de variación instantánea en $x=2$ usando el límite del cociente incremental.  
   c) Interpreta geométricamente el resultado del apartado b).

   > **Solución:**
   >
   > **a)** $\text{TVM}=\dfrac{f(3)-f(1)}{3-1}=\dfrac{\frac{1}{3}-1}{2}=\dfrac{-\frac{2}{3}}{2}=-\dfrac{1}{3}$.
   >
   > **b)** $f'(2)=\lim_{h\to0}\dfrac{\dfrac{1}{2+h}-\dfrac{1}{2}}{h}=\lim_{h\to0}\dfrac{\dfrac{2-(2+h)}{2(2+h)}}{h}=\lim_{h\to0}\dfrac{-h}{2h(2+h)}=\lim_{h\to0}\dfrac{-1}{2(2+h)}=\dfrac{-1}{4}$.
   >
   > **c)** La tasa de variación instantánea en $x=2$ es la pendiente de la recta tangente a $f(x)=\dfrac{1}{x}$ en el punto $(2, \frac{1}{2})$. Como es negativa ($-\frac{1}{4}$), la función decrece en ese punto.

**Test de Opción Múltiple**

6. La tasa de variación media de $f(x)=x^2$ en $[a, a+h]$ es:
   - a) $2a$
   - b) $2a+h$
   - c) $a+h$
   - d) $h$

   > **Respuesta correcta:** b) $\dfrac{(a+h)^2-a^2}{h}=\dfrac{2ah+h^2}{h}=2a+h$.

7. La tasa de variación instantánea en un punto es:
   - a) El valor medio de la función en un intervalo
   - b) La pendiente de la secante entre dos puntos
   - c) El límite de la tasa de variación media cuando el incremento tiende a cero
   - d) La diferencia $f(b)-f(a)$

   > **Respuesta correcta:** c) La TVI es $\lim_{h\to0}\dfrac{f(a+h)-f(a)}{h}$, es decir, el límite de la TVM cuando $h\to0$.

---

#### 7.1.2 Definición de derivada como límite del cociente incremental

**Ejercicio Resuelto**

Calcula $f'(x)$ para $f(x)=\sqrt{x}$ usando la definición de derivada.

**Paso 1 — Escribir el cociente incremental:**

$$\frac{f(x+h)-f(x)}{h} = \frac{\sqrt{x+h}-\sqrt{x}}{h}$$

**Paso 2 — Racionalizar multiplicando por el conjugado:**

$$= \frac{(\sqrt{x+h}-\sqrt{x})(\sqrt{x+h}+\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})} = \frac{(x+h)-x}{h(\sqrt{x+h}+\sqrt{x})} = \frac{h}{h(\sqrt{x+h}+\sqrt{x})} = \frac{1}{\sqrt{x+h}+\sqrt{x}}$$

**Paso 3 — Tomar el límite:**

$$f'(x) = \lim_{h\to 0}\frac{1}{\sqrt{x+h}+\sqrt{x}} = \frac{1}{2\sqrt{x}}$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $f'(x)$ para $f(x)=5x+3$ usando la definición.

   > **Solución:** $\dfrac{f(x+h)-f(x)}{h}=\dfrac{5(x+h)+3-(5x+3)}{h}=\dfrac{5h}{h}=5$.  
   > $f'(x)=\lim_{h\to0}5=5$.

2. Calcula $f'(2)$ para $f(x)=x^2-3x$ usando la definición.

   > **Solución:** $\dfrac{f(2+h)-f(2)}{h}=\dfrac{(2+h)^2-3(2+h)-(4-6)}{h}=\dfrac{4+4h+h^2-6-3h+2}{h}=\dfrac{h^2+h}{h}=h+1$.  
   > $f'(2)=\lim_{h\to0}(h+1)=1$.

**Nivel Intermedio:**

3. Calcula $f'(x)$ para $f(x)=x^3$ usando la definición.

   > **Solución:** $\dfrac{(x+h)^3-x^3}{h}=\dfrac{x^3+3x^2h+3xh^2+h^3-x^3}{h}=3x^2+3xh+h^2 \to 3x^2$.

4. Calcula $f'(x)$ para $f(x)=\dfrac{1}{x+1}$ usando la definición.

   > **Solución:** $\dfrac{\dfrac{1}{x+1+h}-\dfrac{1}{x+1}}{h}=\dfrac{\dfrac{(x+1)-(x+1+h)}{(x+1+h)(x+1)}}{h}=\dfrac{-h}{h(x+1+h)(x+1)}=\dfrac{-1}{(x+1+h)(x+1)}$.  
   > $\to \dfrac{-1}{(x+1)^2}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=x^2-2x$.

   a) Usando la definición de derivada, calcula $f'(x)$.  
   b) Halla el punto de la gráfica donde la tangente es horizontal.  
   c) Calcula la ecuación de la recta tangente en $x=3$.

   > **Solución:**
   >
   > **a)** $\dfrac{(x+h)^2-2(x+h)-(x^2-2x)}{h}=\dfrac{2xh+h^2-2h}{h}=2x+h-2 \to 2x-2$.
   >
   > **b)** Tangente horizontal $\Leftrightarrow f'(x)=0$: $2x-2=0 \Rightarrow x=1$. Punto: $(1, -1)$.
   >
   > **c)** $f'(3)=4$; $f(3)=9-6=3$. Tangente: $y-3=4(x-3)$, es decir $y=4x-9$.

**Test de Opción Múltiple**

6. La derivada de $f$ en $x=a$ se define como:
   - a) $\lim_{h\to\infty}\dfrac{f(a+h)-f(a)}{h}$
   - b) $\lim_{h\to 0}\dfrac{f(a+h)-f(a)}{h}$
   - c) $\dfrac{f(a+1)-f(a)}{1}$
   - d) $\lim_{x\to a}f(x)$

   > **Respuesta correcta:** b) La derivada es el límite del cociente incremental cuando $h\to0$.

7. Si el límite $\lim_{h\to0}\dfrac{f(a+h)-f(a)}{h}$ existe y es finito, entonces:
   - a) $f$ es continua en $a$ pero no necesariamente derivable
   - b) $f$ es derivable en $a$, y por tanto también continua en $a$
   - c) $f$ puede ser discontinua en $a$
   - d) $f'(a)=0$ obligatoriamente

   > **Respuesta correcta:** b) La existencia del límite del cociente incremental define la derivabilidad, y toda función derivable es continua.

---

#### 7.1.3 Derivada como pendiente de la recta tangente: interpretación geométrica

**Ejercicio Resuelto**

Sea $f(x)=x^2-4x+3$. Halla la ecuación de la recta tangente en el punto de abscisa $x=1$ e interpreta geométricamente.

**Paso 1 — Calcular $f'(x)$:**

$$f'(x) = 2x-4$$

**Paso 2 — Pendiente de la tangente en $x=1$:**

$$m = f'(1) = 2(1)-4 = -2$$

**Paso 3 — Punto de tangencia:**

$$f(1) = 1-4+3 = 0 \quad \Rightarrow \quad \text{Punto: } (1, 0)$$

**Paso 4 — Ecuación de la recta tangente:**

$$y - 0 = -2(x-1) \quad \Rightarrow \quad y = -2x+2$$

**Interpretación:** La recta tangente en $(1,0)$ tiene pendiente $-2$, lo que indica que la función decrece en ese punto con una inclinación de $2$ unidades por cada unidad horizontal (ángulo con el eje $OX$: $\arctan(2)\approx 63{,}4°$ hacia abajo).

**Ejercicios con Solución**

**Nivel Básico:**

1. Sea $f(x)=3x^2$. ¿Cuál es la pendiente de la recta tangente en $x=2$?

   > **Solución:** $f'(x)=6x$. $f'(2)=12$. La pendiente es $m=12$.

2. ¿En qué punto de $f(x)=x^2+x$ la recta tangente tiene pendiente $5$?

   > **Solución:** $f'(x)=2x+1=5 \Rightarrow x=2$. Punto: $(2, f(2))=(2, 6)$.

**Nivel Intermedio:**

3. Halla la ecuación de la recta tangente a $f(x)=\sqrt{x}$ en $x=4$.

   > **Solución:** $f'(x)=\dfrac{1}{2\sqrt{x}}$, $f'(4)=\dfrac{1}{4}$. $f(4)=2$. Tangente: $y-2=\dfrac{1}{4}(x-4)$, es decir $y=\dfrac{x}{4}+1$.

4. Halla la ecuación de la recta tangente a $f(x)=\ln x$ en $x=e$.

   > **Solución:** $f'(x)=\dfrac{1}{x}$, $f'(e)=\dfrac{1}{e}$. $f(e)=1$. Tangente: $y-1=\dfrac{1}{e}(x-e)=\dfrac{x}{e}-1$, es decir $y=\dfrac{x}{e}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=e^x$.

   a) Escribe la ecuación de la recta tangente a $f$ en el punto $(0,1)$.  
   b) Comprueba que esta tangente pasa por el origen.  
   c) ¿Existen otras rectas tangentes a $f$ que pasen por el origen? Razóna.

   > **Solución:**
   >
   > **a)** $f'(x)=e^x$, $f'(0)=1$. Tangente en $(0,1)$: $y-1=1\cdot(x-0) \Rightarrow y=x+1$.
   >
   > **b)** En $(0,0)$: $0=0+1=1$ → No pasa por el origen. (La tangente es $y=x+1$, que no pasa por $(0,0)$.)
   >
   > **c)** Buscamos tangente en punto $(a, e^a)$ que pase por $(0,0)$: pendiente desde origen $=\dfrac{e^a}{a}$; pendiente de la tangente $=e^a$. Igualando: $\dfrac{e^a}{a}=e^a \Rightarrow a=1$. Tangente en $x=1$: $y-e=e(x-1) \Rightarrow y=ex$. Pasa por $(0,0)$: $0=e\cdot0=0$ ✓. **Sí existe** una recta tangente a $f$ que pasa por el origen: $y=ex$, en el punto $(1,e)$.

**Test de Opción Múltiple**

6. La pendiente de la recta tangente a $f(x)=x^3$ en $x=2$ es:
   - a) $8$
   - b) $6$
   - c) $12$
   - d) $4$

   > **Respuesta correcta:** c) $f'(x)=3x^2$, $f'(2)=12$.

7. Si $f'(a)=0$, la recta tangente a $f$ en $x=a$:
   - a) Tiene pendiente infinita
   - b) Es perpendicular al eje $OX$
   - c) Es horizontal (paralela al eje $OX$)
   - d) No existe

   > **Respuesta correcta:** c) Pendiente $0$ significa tangente horizontal, paralela al eje $OX$.

---

#### 7.1.4 Función derivada: definición y notación (Lagrange, Leibniz, Newton)

**Ejercicio Resuelto**

Sea $f(x)=2x^3-5x+1$. Expresa su función derivada usando las tres notaciones principales y calcula $f'(2)$.

**Función derivada:** Aplicando las reglas estándar de derivación,

$$f'(x) = 6x^2 - 5$$

**Notaciones equivalentes:**

| Notación | Expresión |
|----------|-----------|
| Lagrange | $f'(x) = 6x^2-5$ |
| Leibniz  | $\dfrac{dy}{dx} = 6x^2-5$ o $\dfrac{d}{dx}(2x^3-5x+1)=6x^2-5$ |
| Newton   | $\dot{f} = 6x^2-5$ (usada en Física) |

**Cálculo de $f'(2)$:**

$$f'(2) = 6(4)-5 = 24-5 = 19$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Escribe la función derivada de $f(x)=x^4-3x^2+7$ en notación de Lagrange y de Leibniz.

   > **Solución:** $f'(x)=4x^3-6x$ (Lagrange). $\dfrac{dy}{dx}=4x^3-6x$ (Leibniz).

2. Dado $f'(x)=3x^2-2$, calcula $f'(0)$, $f'(1)$ y $f'(-1)$.

   > **Solución:** $f'(0)=-2$; $f'(1)=1$; $f'(-1)=1$.

**Nivel Intermedio:**

3. Halla la función derivada de $g(x)=\dfrac{2}{x}-x^2$ y calcula $g'(-2)$.

   > **Solución:** $g(x)=2x^{-1}-x^2$. $g'(x)=-2x^{-2}-2x=-\dfrac{2}{x^2}-2x$.  
   > $g'(-2)=-\dfrac{2}{4}-2(-2)=-\dfrac{1}{2}+4=\dfrac{7}{2}$.

4. Si $\dfrac{dy}{dx}=2e^x-\dfrac{1}{x}$ ¿cuál es el valor de la derivada en $x=1$?

   > **Solución:** $\dfrac{dy}{dx}\bigg|_{x=1}=2e-1\approx 4{,}44$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=x^2\cdot e^x$.

   a) Halla $f'(x)$ indicando la regla de derivación utilizada.  
   b) Calcula $f'(0)$ y $f'(1)$.  
   c) Halla los puntos donde $f'(x)=0$.

   > **Solución:**
   >
   > **a)** Regla del producto: $f'(x)=(x^2)'e^x+x^2(e^x)'=2x\cdot e^x+x^2\cdot e^x=e^x(2x+x^2)=xe^x(x+2)$.
   >
   > **b)** $f'(0)=0\cdot e^0\cdot(2)=0$; $f'(1)=1\cdot e\cdot 3=3e$.
   >
   > **c)** $f'(x)=0 \Leftrightarrow xe^x(x+2)=0$. Como $e^x>0$ siempre, $x=0$ o $x=-2$.

**Test de Opción Múltiple**

6. La notación $\dfrac{dy}{dx}$ para la derivada fue introducida por:
   - a) Newton
   - b) Lagrange
   - c) Leibniz
   - d) Euler

   > **Respuesta correcta:** c) La notación diferencial $\dfrac{dy}{dx}$ es de Leibniz. Newton usaba $\dot{y}$ y Lagrange usaba $f'(x)$.

7. Si $f'(x)=4x^3$, entonces $f'(-1)=$:
   - a) $4$
   - b) $-4$
   - c) $12$
   - d) $-12$

   > **Respuesta correcta:** b) $f'(-1)=4(-1)^3=4\cdot(-1)=-4$.

---

#### 7.1.5 Derivadas sucesivas: f'', f''' y derivada de orden n

**Ejercicio Resuelto**

Sea $f(x)=x^4-6x^2+2x-1$. Calcula $f'(x)$, $f''(x)$, $f'''(x)$ y $f^{(4)}(x)$. Interpreta $f''$.

**Derivadas sucesivas:**

$$f'(x) = 4x^3-12x+2$$

$$f''(x) = 12x^2-12$$

$$f'''(x) = 24x$$

$$f^{(4)}(x) = 24$$

$$f^{(n)}(x) = 0 \quad \text{para } n\geq 5$$

**Interpretación de $f''$:** La segunda derivada mide la variación de la pendiente (aceleración de la función). Si $f''(x)>0$, la curva es cóncava hacia arriba; si $f''(x)<0$, es cóncava hacia abajo.

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $f''(x)$ para $f(x)=3x^3-2x^2+x-5$.

   > **Solución:** $f'(x)=9x^2-4x+1$. $f''(x)=18x-4$.

2. Si la posición de un móvil es $s(t)=2t^3-3t$, calcula su aceleración en $t=1$.

   > **Solución:** Velocidad: $v(t)=s'(t)=6t^2-3$. Aceleración: $a(t)=s''(t)=12t$.  
   > $a(1)=12$ m/s².

**Nivel Intermedio:**

3. Calcula $f^{(n)}(x)$ para $f(x)=e^{2x}$.

   > **Solución:** $f'(x)=2e^{2x}$; $f''(x)=4e^{2x}$; $f^{(n)}(x)=2^n e^{2x}$.

4. Halla $f''(x)$ para $f(x)=x\ln x$ y determina su signo.

   > **Solución:** $f'(x)=\ln x + x\cdot\dfrac{1}{x}=\ln x+1$. $f''(x)=\dfrac{1}{x}$.  
   > Para $x>0$ (dominio): $f''(x)=\dfrac{1}{x}>0$ → la función es siempre cóncava hacia arriba en su dominio.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\sin x$.

   a) Calcula $f'(x)$, $f''(x)$, $f'''(x)$ y $f^{(4)}(x)$.  
   b) Deduce una expresión general para $f^{(n)}(x)$.  
   c) Calcula $f^{(100)}(0)$.

   > **Solución:**
   >
   > **a)** $f'(x)=\cos x$; $f''(x)=-\sin x$; $f'''(x)=-\cos x$; $f^{(4)}(x)=\sin x$.
   >
   > **b)** El ciclo se repite con período 4:  
   > $f^{(4k)}(x)=\sin x$, $f^{(4k+1)}(x)=\cos x$, $f^{(4k+2)}(x)=-\sin x$, $f^{(4k+3)}(x)=-\cos x$.
   >
   > **c)** $100=4\cdot25$, luego $f^{(100)}(x)=\sin x$. Por tanto $f^{(100)}(0)=\sin 0=0$.

**Test de Opción Múltiple**

6. Si $f(x)=x^5$, entonces $f^{(5)}(x)=$:
   - a) $5x^4$
   - b) $120x$
   - c) $120$
   - d) $0$

   > **Respuesta correcta:** c) $f'=5x^4$, $f''=20x^3$, $f'''=60x^2$, $f^{(4)}=120x$, $f^{(5)}=120$.

7. La segunda derivada de una función en un punto puede interpretarse como:
   - a) La pendiente de la tangente
   - b) La velocidad instantánea
   - c) La curvatura o tasa de cambio de la pendiente
   - d) El valor de la función en ese punto

   > **Respuesta correcta:** c) $f''$ mide cómo varía la pendiente; en física del movimiento corresponde a la aceleración.

---

#### 7.2.1 Derivadas de funciones elementales

**Ejercicio Resuelto**

Calcula las derivadas de las siguientes funciones elementales y justifica cada resultado con la fórmula correspondiente:

$$f_1(x)=x^5, \quad f_2(x)=e^{3x}, \quad f_3(x)=\ln(2x), \quad f_4(x)=\sin(4x), \quad f_5(x)=\cos(x^2)$$

**Solución:**

$f_1'(x)=5x^4$ (regla de la potencia: $(x^n)'=nx^{n-1}$)

$f_2'(x)=3e^{3x}$ ($(e^{ax})'=ae^{ax}$; aquí $a=3$)

$f_3'(x)=\dfrac{1}{2x}\cdot 2=\dfrac{1}{x}$ ($(\ln u)'=\dfrac{u'}{u}$; $u=2x$, $u'=2$)

$f_4'(x)=4\cos(4x)$ ($(\sin u)'=u'\cos u$; $u=4x$)

$f_5'(x)=-2x\sin(x^2)$ ($(\cos u)'=-u'\sin u$; $u=x^2$, $u'=2x$)

**Ejercicios con Solución**

**Nivel Básico:**

1. Deriva: $f(x)=x^7$, $g(x)=e^x$, $h(x)=\ln x$, $p(x)=\sin x$, $q(x)=\cos x$.

   > **Solución:** $f'=7x^6$; $g'=e^x$; $h'=\dfrac{1}{x}$; $p'=\cos x$; $q'=-\sin x$.

2. Deriva: $f(x)=\sqrt[3]{x^2}=x^{2/3}$.

   > **Solución:** $f'(x)=\dfrac{2}{3}x^{-1/3}=\dfrac{2}{3\sqrt[3]{x}}$.

**Nivel Intermedio:**

3. Deriva: $f(x)=\tan x$. (Usa que $\tan x=\dfrac{\sin x}{\cos x}$.)

   > **Solución:** $f'(x)=\dfrac{\cos x\cdot\cos x-\sin x\cdot(-\sin x)}{\cos^2 x}=\dfrac{\cos^2 x+\sin^2 x}{\cos^2 x}=\dfrac{1}{\cos^2 x}=\sec^2 x$.

4. Deriva: $f(x)=a^x$ donde $a>0, a\neq1$.

   > **Solución:** $f(x)=a^x=e^{x\ln a}$. $f'(x)=e^{x\ln a}\cdot\ln a=a^x\ln a$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula las derivadas de:

   a) $f(x)=x^3-2\sqrt{x}+\dfrac{1}{x}$  
   b) $g(x)=3e^x-5\ln x+\cos x$  
   c) $h(x)=\tan x - x$

   > **Solución:**
   >
   > **a)** $f(x)=x^3-2x^{1/2}+x^{-1}$. $f'(x)=3x^2-\dfrac{1}{\sqrt{x}}-\dfrac{1}{x^2}$.
   >
   > **b)** $g'(x)=3e^x-\dfrac{5}{x}-\sin x$.
   >
   > **c)** $h'(x)=\sec^2 x-1=\tan^2 x$.

**Test de Opción Múltiple**

6. La derivada de $f(x)=\ln(x)$ es:
   - a) $x$
   - b) $\dfrac{1}{x}$
   - c) $e^x$
   - d) $\ln(x-1)$

   > **Respuesta correcta:** b) $(\ln x)'=\dfrac{1}{x}$ para $x>0$.

7. La derivada de $\cos x$ es:
   - a) $\sin x$
   - b) $-\sin x$
   - c) $\cos x$
   - d) $-\cos x$

   > **Respuesta correcta:** b) $(\cos x)'=-\sin x$.

---

#### 7.2.2 Linealidad: derivada de la suma y del producto por escalar

**Ejercicio Resuelto**

Deriva $f(x) = 4x^3 - 7x^2 + 2x - 9$ aplicando la linealidad de la derivada.

**Propiedad de linealidad:** $(af+bg)' = af'+bg'$ para constantes $a, b$.

$$f'(x) = 4\cdot(x^3)' - 7\cdot(x^2)' + 2\cdot(x)' - (9)' = 4\cdot3x^2 - 7\cdot2x + 2\cdot1 - 0 = 12x^2-14x+2$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Deriva $f(x)=5x^4-3x^2+7$.

   > **Solución:** $f'(x)=20x^3-6x$.

2. Deriva $g(x)=3\sin x+2\cos x - e^x$.

   > **Solución:** $g'(x)=3\cos x-2\sin x-e^x$.

**Nivel Intermedio:**

3. Deriva $h(x)=\dfrac{x^3}{3}-\dfrac{x^2}{2}+x-\ln x$.

   > **Solución:** $h'(x)=x^2-x+1-\dfrac{1}{x}$.

4. Deriva $f(x)=2\sqrt{x}+\dfrac{3}{x^2}-5e^x+\ln 2$.

   > **Solución:** $f(x)=2x^{1/2}+3x^{-2}-5e^x+\ln 2$.  
   > $f'(x)=\dfrac{1}{\sqrt{x}}-\dfrac{6}{x^3}-5e^x$. (La constante $\ln 2$ deriva $0$.)

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=ax^3+bx^2+cx+d$ con $f(0)=1$, $f'(0)=2$, $f''(0)=-6$, $f'''(0)=6$.

   a) Determina los valores de $a$, $b$, $c$, $d$.  
   b) Escribe la expresión explícita de $f(x)$ y $f'(x)$.

   > **Solución:**
   >
   > **a)** $f(0)=d=1$. $f'(x)=3ax^2+2bx+c$; $f'(0)=c=2$.  
   > $f''(x)=6ax+2b$; $f''(0)=2b=-6 \Rightarrow b=-3$.  
   > $f'''(x)=6a$; $f'''(0)=6a=6 \Rightarrow a=1$.
   >
   > **b)** $f(x)=x^3-3x^2+2x+1$; $f'(x)=3x^2-6x+2$.

**Test de Opción Múltiple**

6. Si $f(x)=3x^2+5$ y $g(x)=2x-1$, entonces $(f+g)'(x)=$:
   - a) $6x+2$
   - b) $6x$
   - c) $6x-1$
   - d) $3x^2+2x+4$

   > **Respuesta correcta:** a) $(f+g)'=f'+g'=6x+2$.

7. La derivada de una constante es:
   - a) La propia constante
   - b) $1$
   - c) $0$
   - d) Indefinida

   > **Respuesta correcta:** c) La derivada de cualquier constante es $0$.

---

#### 7.2.3 Regla del producto

**Ejercicio Resuelto**

Deriva $f(x)=(x^2+1)(3x-2)$ aplicando la regla del producto.

**Regla del producto:** $(u\cdot v)' = u'v + uv'$

Sea $u=x^2+1$ y $v=3x-2$. Entonces $u'=2x$ y $v'=3$.

$$f'(x) = (2x)(3x-2) + (x^2+1)(3) = 6x^2-4x + 3x^2+3 = 9x^2-4x+3$$

**Verificación** expandiendo: $f(x)=3x^3-2x^2+3x-2$. $f'(x)=9x^2-4x+3$ ✓.

**Ejercicios con Solución**

**Nivel Básico:**

1. Deriva $f(x)=x\cdot e^x$.

   > **Solución:** $u=x$, $v=e^x$; $u'=1$, $v'=e^x$.  
   > $f'(x)=1\cdot e^x+x\cdot e^x=e^x(1+x)$.

2. Deriva $g(x)=(x+1)\sin x$.

   > **Solución:** $g'(x)=1\cdot\sin x+(x+1)\cos x=\sin x+(x+1)\cos x$.

**Nivel Intermedio:**

3. Deriva $h(x)=x^2\ln x$.

   > **Solución:** $h'(x)=2x\cdot\ln x+x^2\cdot\dfrac{1}{x}=2x\ln x+x=x(2\ln x+1)$.

4. Deriva $f(x)=(3x^2-x)(e^x+\ln x)$.

   > **Solución:** $u'=6x-1$; $v'=e^x+\dfrac{1}{x}$.  
   > $f'(x)=(6x-1)(e^x+\ln x)+(3x^2-x)(e^x+\dfrac{1}{x})$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=x^2\sin x$.

   a) Calcula $f'(x)$.  
   b) Halla los puntos donde $f'(x)=0$ en $[0, 2\pi]$.  
   c) Determina si esos puntos son máximos o mínimos usando $f''$.

   > **Solución:**
   >
   > **a)** $f'(x)=2x\sin x+x^2\cos x=x(2\sin x+x\cos x)$.
   >
   > **b)** $f'(x)=0$ si $x=0$ o $2\sin x+x\cos x=0$.  
   > Para $x\in(0,2\pi]$: $2\tan x=-x \Rightarrow \tan x=-x/2$. Esta ecuación no tiene solución explícita sencilla; se acepta indicar que hay soluciones trascendentes numéricamente.  
   > En $x=0$: $f'(0)=0$.
   >
   > **c)** $f''(x)=2\sin x+2x\cos x+2x\cos x-x^2\sin x=2\sin x+4x\cos x-x^2\sin x$.  
   > $f''(0)=0$, no es concluyente. Hay que analizar el signo de $f'$ cerca de $0$: $f'(x)\approx x(2x)=2x^2>0$ para $x\neq0$ pequeño, luego $x=0$ es un mínimo local.

**Test de Opción Múltiple**

6. Aplicando la regla del producto a $f(x)=x\cdot\cos x$:
   - a) $f'(x)=\cos x$
   - b) $f'(x)=-x\sin x$
   - c) $f'(x)=\cos x-x\sin x$
   - d) $f'(x)=\cos x+x\sin x$

   > **Respuesta correcta:** c) $(x)'\cos x+x(\cos x)'=\cos x-x\sin x$.

7. Si $f(x)=u(x)\cdot v(x)$, entonces $f'(x)=$:
   - a) $u'(x)\cdot v'(x)$
   - b) $u'(x)\cdot v(x)+u(x)\cdot v'(x)$
   - c) $u(x)\cdot v'(x)$
   - d) $u'(x)+v'(x)$

   > **Respuesta correcta:** b) Esta es la regla del producto o regla de Leibniz.

---

#### 7.2.4 Regla del cociente

**Ejercicio Resuelto**

Deriva $f(x)=\dfrac{x^2-1}{x+3}$ aplicando la regla del cociente.

**Regla del cociente:** $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$

Sea $u=x^2-1$, $v=x+3$. Entonces $u'=2x$, $v'=1$.

$$f'(x) = \frac{(2x)(x+3)-(x^2-1)(1)}{(x+3)^2} = \frac{2x^2+6x-x^2+1}{(x+3)^2} = \frac{x^2+6x+1}{(x+3)^2}$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Deriva $f(x)=\dfrac{3x}{x+1}$.

   > **Solución:** $u=3x$, $v=x+1$, $u'=3$, $v'=1$.  
   > $f'(x)=\dfrac{3(x+1)-3x\cdot1}{(x+1)^2}=\dfrac{3}{(x+1)^2}$.

2. Deriva $g(x)=\dfrac{x^2+1}{x}=x+\dfrac{1}{x}$ de dos formas.

   > **Solución 1 (cociente):** $g'=\dfrac{2x\cdot x-(x^2+1)\cdot1}{x^2}=\dfrac{2x^2-x^2-1}{x^2}=\dfrac{x^2-1}{x^2}$.  
   > **Solución 2 (simplificando):** $g'=1-\dfrac{1}{x^2}=\dfrac{x^2-1}{x^2}$ ✓.

**Nivel Intermedio:**

3. Deriva $h(x)=\dfrac{e^x}{x^2+1}$.

   > **Solución:** $h'(x)=\dfrac{e^x(x^2+1)-e^x\cdot2x}{(x^2+1)^2}=\dfrac{e^x(x^2-2x+1)}{(x^2+1)^2}=\dfrac{e^x(x-1)^2}{(x^2+1)^2}$.

4. Deriva $f(x)=\dfrac{\ln x}{x}$.

   > **Solución:** $f'(x)=\dfrac{\frac{1}{x}\cdot x-\ln x\cdot1}{x^2}=\dfrac{1-\ln x}{x^2}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\dfrac{x^2-x+1}{x-1}$.

   a) Calcula $f'(x)$.  
   b) Halla los puntos donde $f'(x)=0$.  
   c) Determina en qué intervalos $f$ es creciente y decreciente.

   > **Solución:**
   >
   > **a)** $f'(x)=\dfrac{(2x-1)(x-1)-(x^2-x+1)\cdot1}{(x-1)^2}=\dfrac{2x^2-3x+1-x^2+x-1}{(x-1)^2}=\dfrac{x^2-2x}{(x-1)^2}=\dfrac{x(x-2)}{(x-1)^2}$.
   >
   > **b)** $f'(x)=0 \Leftrightarrow x=0$ o $x=2$.
   >
   > **c)** Tabla de signos de $f'(x)=\dfrac{x(x-2)}{(x-1)^2}$:
   > - $(-\infty,0)$: $(-)(-)/(+)>0$ → creciente
   > - $(0,1)$: $(+)(-)/(+)<0$ → decreciente
   > - $(1,2)$: $(+)(-)/(+)<0$ → decreciente
   > - $(2,+\infty)$: $(+)(+)/(+)>0$ → creciente
   >
   > Mínimo local en $x=2$; máximo local en $x=0$.

**Test de Opción Múltiple**

6. La derivada de $f(x)=\dfrac{1}{x^2}$ es:
   - a) $-\dfrac{2}{x^3}$
   - b) $\dfrac{2}{x^3}$
   - c) $-\dfrac{1}{x^3}$
   - d) $2x$

   > **Respuesta correcta:** a) $f'(x)=-2x^{-3}=-\dfrac{2}{x^3}$.

7. Si $f(x)=\dfrac{u}{v}$, entonces $f'=$:
   - a) $\dfrac{u'v+uv'}{v^2}$
   - b) $\dfrac{u'v-uv'}{v^2}$
   - c) $\dfrac{u'}{v'}$
   - d) $\dfrac{u'v-uv'}{v}$

   > **Respuesta correcta:** b) Esta es la regla del cociente.

---

#### 7.2.5 Regla de la cadena (función compuesta)

**Ejercicio Resuelto**

Deriva $f(x)=\sin(x^3+2x)$ usando la regla de la cadena.

**Regla de la cadena:** $(f\circ g)'(x)=f'(g(x))\cdot g'(x)$

Sea la función exterior $f(u)=\sin u$ y la interior $g(x)=x^3+2x$.

$$f'(u)=\cos u, \qquad g'(x)=3x^2+2$$

$$\frac{d}{dx}\sin(x^3+2x) = \cos(x^3+2x)\cdot(3x^2+2)$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Deriva $f(x)=(3x+1)^5$.

   > **Solución:** $f'(x)=5(3x+1)^4\cdot3=15(3x+1)^4$.

2. Deriva $g(x)=e^{x^2}$.

   > **Solución:** $g'(x)=e^{x^2}\cdot2x=2xe^{x^2}$.

**Nivel Intermedio:**

3. Deriva $h(x)=\ln(\sin x)$.

   > **Solución:** $h'(x)=\dfrac{1}{\sin x}\cdot\cos x=\dfrac{\cos x}{\sin x}=\cot x$.

4. Deriva $f(x)=\sqrt{x^2+4x-1}$.

   > **Solución:** $f'(x)=\dfrac{2x+4}{2\sqrt{x^2+4x-1}}=\dfrac{x+2}{\sqrt{x^2+4x-1}}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=e^{\sin x}$.

   a) Calcula $f'(x)$ justificando la regla usada.  
   b) Halla $f'(0)$ y $f'(\pi/2)$.  
   c) Halla los puntos $x\in[0,2\pi]$ donde $f'(x)=0$.

   > **Solución:**
   >
   > **a)** Regla de la cadena: función exterior $e^u$ ($u=\sin x$), interior $\sin x$.  
   > $f'(x)=e^{\sin x}\cdot\cos x$.
   >
   > **b)** $f'(0)=e^0\cdot\cos0=1\cdot1=1$. $f'(\pi/2)=e^1\cdot\cos(\pi/2)=e\cdot0=0$.
   >
   > **c)** $f'(x)=0 \Leftrightarrow e^{\sin x}\cdot\cos x=0$. Como $e^{\sin x}>0$, necesitamos $\cos x=0$.  
   > En $[0,2\pi]$: $x=\dfrac{\pi}{2}$ y $x=\dfrac{3\pi}{2}$.

**Test de Opción Múltiple**

6. La derivada de $f(x)=(2x+3)^4$ es:
   - a) $4(2x+3)^3$
   - b) $8(2x+3)^3$
   - c) $4(2x+3)^3\cdot4$
   - d) $(2x+3)^3$

   > **Respuesta correcta:** b) $4(2x+3)^3\cdot2=8(2x+3)^3$.

7. Para derivar $f(x)=\ln(x^2+1)$ se usa la regla de la cadena, obteniendo:
   - a) $\dfrac{1}{x^2+1}$
   - b) $\dfrac{2x}{x^2+1}$
   - c) $\dfrac{1}{2x}$
   - d) $\ln(2x)$

   > **Respuesta correcta:** b) $f'(x)=\dfrac{1}{x^2+1}\cdot2x=\dfrac{2x}{x^2+1}$.

---

#### 7.2.6 Derivación logarítmica: técnica y aplicaciones

**Ejercicio Resuelto**

Calcula la derivada de $f(x)=x^x$ (para $x>0$) usando derivación logarítmica.

**Paso 1 — Tomar logaritmos neperianos en ambos lados:**

$$\ln f(x)=\ln(x^x)=x\ln x$$

**Paso 2 — Derivar implícitamente respecto de $x$:**

$$\frac{f'(x)}{f(x)} = \ln x + x\cdot\frac{1}{x} = \ln x+1$$

**Paso 3 — Despejar $f'(x)$:**

$$f'(x) = f(x)\cdot(\ln x+1) = x^x(\ln x+1)$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Usa derivación logarítmica para derivar $f(x)=x^3(x+1)^2$.

   > **Solución:** $\ln f=3\ln x+2\ln(x+1)$. $\dfrac{f'}{f}=\dfrac{3}{x}+\dfrac{2}{x+1}$.  
   > $f'=x^3(x+1)^2\left(\dfrac{3}{x}+\dfrac{2}{x+1}\right)=3x^2(x+1)^2+2x^3(x+1)=x^2(x+1)(5x+3)$.

2. Deriva $g(x)=\dfrac{(x+1)^2}{(x-1)^3}$ por derivación logarítmica.

   > **Solución:** $\ln g=2\ln(x+1)-3\ln(x-1)$. $\dfrac{g'}{g}=\dfrac{2}{x+1}-\dfrac{3}{x-1}=\dfrac{2(x-1)-3(x+1)}{(x+1)(x-1)}=\dfrac{-x-5}{x^2-1}$.  
   > $g'=\dfrac{(x+1)^2}{(x-1)^3}\cdot\dfrac{-x-5}{x^2-1}=\dfrac{-(x+5)(x+1)}{(x-1)^4}$.

**Nivel Intermedio:**

3. Deriva $f(x)=(x+1)^{\sin x}$ para $x>-1$.

   > **Solución:** $\ln f=\sin x\cdot\ln(x+1)$.  
   > $\dfrac{f'}{f}=\cos x\cdot\ln(x+1)+\dfrac{\sin x}{x+1}$.  
   > $f'=(x+1)^{\sin x}\left(\cos x\cdot\ln(x+1)+\dfrac{\sin x}{x+1}\right)$.

4. Deriva $h(x)=\dfrac{x^2\sqrt{x+1}}{e^x}$ usando derivación logarítmica.

   > **Solución:** $\ln h=2\ln x+\dfrac{1}{2}\ln(x+1)-x$.  
   > $\dfrac{h'}{h}=\dfrac{2}{x}+\dfrac{1}{2(x+1)}-1$.  
   > $h'=\dfrac{x^2\sqrt{x+1}}{e^x}\left(\dfrac{2}{x}+\dfrac{1}{2(x+1)}-1\right)$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\left(\dfrac{x+1}{x-1}\right)^x$ para $x>1$.

   a) Calcula $f'(x)$ usando derivación logarítmica.  
   b) Calcula $f'(2)$.

   > **Solución:**
   >
   > **a)** $\ln f=x\left[\ln(x+1)-\ln(x-1)\right]$.  
   > $\dfrac{f'}{f}=\ln\dfrac{x+1}{x-1}+x\left[\dfrac{1}{x+1}-\dfrac{1}{x-1}\right]=\ln\dfrac{x+1}{x-1}+x\cdot\dfrac{-2}{x^2-1}=\ln\dfrac{x+1}{x-1}-\dfrac{2x}{x^2-1}$.  
   > $f'=\left(\dfrac{x+1}{x-1}\right)^x\left(\ln\dfrac{x+1}{x-1}-\dfrac{2x}{x^2-1}\right)$.
   >
   > **b)** $f(2)=\left(\dfrac{3}{1}\right)^2=9$. $f'(2)=9\left(\ln3-\dfrac{4}{3}\right)=9\ln3-12$.

**Test de Opción Múltiple**

6. La derivación logarítmica es especialmente útil para funciones del tipo:
   - a) Polinomios de grado alto
   - b) Productos y cocientes de muchas funciones, y potencias variables
   - c) Funciones trigonométricas simples
   - d) Sumas de funciones elementales

   > **Respuesta correcta:** b) La derivación logarítmica simplifica notablemente las expresiones con muchos factores multiplicados/divididos y potencias con exponente variable.

7. La derivada de $f(x)=x^x$ es:
   - a) $x\cdot x^{x-1}$
   - b) $x^x\ln x$
   - c) $x^x(\ln x+1)$
   - d) $x^{x-1}$

   > **Respuesta correcta:** c) Por derivación logarítmica: $f'(x)=x^x(\ln x+1)$.

---

#### 7.3.1 Derivadas laterales: definición y cálculo

**Ejercicio Resuelto**

Sea $f(x)=|x-2|$. Calcula las derivadas laterales en $x=2$ y determina si $f$ es derivable en ese punto.

**Derivada lateral por la derecha:**

$$f'_+(2) = \lim_{h\to 0^+}\frac{f(2+h)-f(2)}{h} = \lim_{h\to 0^+}\frac{|h|-0}{h} = \lim_{h\to 0^+}\frac{h}{h} = 1$$

(Para $h>0$: $|h|=h$.)

**Derivada lateral por la izquierda:**

$$f'_-(2) = \lim_{h\to 0^-}\frac{f(2+h)-f(2)}{h} = \lim_{h\to 0^-}\frac{|-h|}{h} = \lim_{h\to 0^-}\frac{-h}{h} = -1$$

(Para $h<0$: $|h|=-h$.)

**Conclusión:** $f'_+(2)=1\neq-1=f'_-(2)$, por tanto $f$ **no es derivable** en $x=2$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Sea $f(x)=|3x|$. Calcula $f'_+(0)$ y $f'_-(0)$.

   > **Solución:** Para $h>0$: $f'_+(0)=\lim_{h\to0^+}\dfrac{3h}{h}=3$. Para $h<0$: $f'_-(0)=\lim_{h\to0^-}\dfrac{-3h}{h}=-3$.  
   > No es derivable en $x=0$.

2. Calcula $f'_+(1)$ y $f'_-(1)$ para $f(x)=x^2$.

   > **Solución:** $f'(x)=2x$ en todos los puntos, luego $f'_+(1)=f'_-(1)=2$. $f$ es derivable en $x=1$.

**Nivel Intermedio:**

3. Sea $f(x)=\begin{cases}x^2 & x\leq1 \\ 2x-1 & x>1\end{cases}$. Calcula $f'_+(1)$ y $f'_-(1)$.

   > **Solución:** $f'_-(1)=\lim_{h\to0^-}\dfrac{(1+h)^2-1}{h}=\lim_{h\to0^-}(2+h)=2$.  
   > $f'_+(1)=\lim_{h\to0^+}\dfrac{2(1+h)-1-1}{h}=\lim_{h\to0^+}\dfrac{2h}{h}=2$.  
   > $f'_+(1)=f'_-(1)=2$ → $f$ es derivable en $x=1$ con $f'(1)=2$.

4. Sea $f(x)=\begin{cases}\sin x & x\geq0 \\ x & x<0\end{cases}$. ¿Es $f$ derivable en $x=0$?

   > **Solución:** $f'_-(0)=\lim_{h\to0^-}\dfrac{h-0}{h}=1$. $f'_+(0)=\lim_{h\to0^+}\dfrac{\sin h}{h}=1$.  
   > $f'_+(0)=f'_-(0)=1$ → $f$ es derivable en $x=0$ con $f'(0)=1$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\begin{cases}x^2+ax & x<2 \\ bx+1 & x\geq2\end{cases}$.

   a) Halla los valores de $a$ y $b$ para que $f$ sea continua en $x=2$.  
   b) Con esos valores, estudia si $f$ es derivable en $x=2$.

   > **Solución:**
   >
   > **a)** Continuidad en $x=2$: $\lim_{x\to2^-}f(x)=4+2a$ y $\lim_{x\to2^+}f(x)=2b+1$, $f(2)=2b+1$.  
   > Condición: $4+2a=2b+1 \Rightarrow 2a-2b=-3$ ... (*)
   >
   > **b)** Derivadas laterales:  
   > $f'_-(2)=\lim_{h\to0^-}\dfrac{(2+h)^2+a(2+h)-(4+2a)}{h}=\lim_{h\to0^-}(4+h+2a+a)$... Mejor:  
   > $f'_-(2)=(x^2+ax)'|_{x=2}=2x+a|_{x=2}=4+a$.  
   > $f'_+(2)=(bx+1)'=b$.  
   > Para derivabilidad: $4+a=b$ ... (**)  
   > De (*): $2a-2b=-3 \Rightarrow a-b=-\dfrac{3}{2}$. De (**): $a-b=-4$.  
   > $-4=-\dfrac{3}{2}$ → contradicción. Con las condiciones de derivabilidad, no hay $a,b$ que hagan $f$ tanto continua como derivable con esas condiciones simultáneamente.  
   > **Pero si solo pedimos continuidad** (sin especificar $b$): hay infinitas soluciones paramétricas. Para obtener una solución concreta se necesita un valor adicional (p. ej. $b=3$, entonces $a=-\frac{1}{2}$).

**Test de Opción Múltiple**

6. Las derivadas laterales de $f(x)=|x|$ en $x=0$ son:
   - a) $f'_+(0)=0$, $f'_-(0)=0$
   - b) $f'_+(0)=1$, $f'_-(0)=1$
   - c) $f'_+(0)=1$, $f'_-(0)=-1$
   - d) $f'_+(0)=-1$, $f'_-(0)=1$

   > **Respuesta correcta:** c) Para $h>0$: $|h|/h=1$. Para $h<0$: $|h|/h=-h/h=-1$.

7. Una función es derivable en $x=a$ si y solo si:
   - a) Es continua en $x=a$
   - b) Sus derivadas laterales son iguales y finitas
   - c) $f(a)=0$
   - d) $f'(a)>0$

   > **Respuesta correcta:** b) La derivabilidad requiere que $f'_+(a)=f'_-(a)$ y que ambas sean finitas.

---

#### 7.3.2 Derivabilidad en un punto: condición de igualdad de derivadas laterales

**Ejercicio Resuelto**

Determina si $f(x)=\begin{cases}x^2-1 & x\leq1 \\ 2x-2 & x>1\end{cases}$ es derivable en $x=1$.

**Paso 1 — Verificar continuidad** (condición necesaria):

$\lim_{x\to1^-}(x^2-1)=0$; $f(1)=0$; $\lim_{x\to1^+}(2x-2)=0$. Los tres son iguales → $f$ es continua en $x=1$.

**Paso 2 — Calcular derivadas laterales:**

$$f'_-(1) = (x^2-1)'|_{x=1} = 2x|_{x=1} = 2$$

$$f'_+(1) = (2x-2)'|_{x=1} = 2|_{x=1} = 2$$

**Paso 3 — Conclusión:**

$f'_-(1)=2=f'_+(1)$ → $f$ **es derivable** en $x=1$ con $f'(1)=2$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Determina si $f(x)=\begin{cases}3x & x\leq0\\x^2 & x>0\end{cases}$ es derivable en $x=0$.

   > **Solución:** Continuidad: $f(0)=0$; $\lim_{x\to0^+}x^2=0$ ✓.  
   > $f'_-(0)=3$; $f'_+(0)=0$. Como son distintas, $f$ **no es derivable** en $x=0$.

2. Determina si $g(x)=x|x|$ es derivable en $x=0$.

   > **Solución:** $g(x)=\begin{cases}-x^2 & x<0\\x^2 & x\geq0\end{cases}$.  
   > $g'_-(0)=-2\cdot0=0$; $g'_+(0)=2\cdot0=0$. Iguales → $g$ **es derivable** en $x=0$ con $g'(0)=0$.

**Nivel Intermedio:**

3. Halla el valor de $a$ para que $f(x)=\begin{cases}ax^2+1 & x\leq1\\3x-1 & x>1\end{cases}$ sea derivable en $x=1$.

   > **Solución:** Continuidad: $a+1=2 \Rightarrow a=1$.  
   > $f'_-(1)=2ax|_{x=1}=2a=2$; $f'_+(1)=3$.  
   > Para derivabilidad: $2a=3 \Rightarrow a=\dfrac{3}{2}$, pero esto contradice $a=1$ de continuidad.  
   > **No existe** un valor de $a$ que haga $f$ simultáneamente continua y derivable en $x=1$.

4. Demuestra que $f(x)=x^{1/3}$ no es derivable en $x=0$.

   > **Solución:** $\dfrac{f(0+h)-f(0)}{h}=\dfrac{h^{1/3}}{h}=h^{-2/3}=\dfrac{1}{h^{2/3}}\to+\infty$ cuando $h\to0$.  
   > El límite no es finito → $f$ **no es derivable** en $x=0$ (hay una tangente vertical).

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\begin{cases}ax+b & x<1\\x^2+2 & x\geq1\end{cases}$.

   a) Halla $a$ y $b$ para que $f$ sea derivable en $x=1$.  
   b) Escribe $f'(x)$ para cada tramo con esos valores.  
   c) Calcula $f'(0)$ y $f'(2)$.

   > **Solución:**
   >
   > **a)** Continuidad: $\lim_{x\to1^-}(ax+b)=a+b=f(1)=3 \Rightarrow a+b=3$.  
   > Derivabilidad: $f'_-(1)=a$ y $f'_+(1)=2x|_{x=1}=2$. Para derivabilidad: $a=2$.  
   > Entonces $b=3-2=1$.
   >
   > **b)** $f'(x)=\begin{cases}2 & x<1\\2x & x>1\end{cases}$ (en $x=1$: $f'(1)=2$).
   >
   > **c)** $f'(0)=2$; $f'(2)=4$.

**Test de Opción Múltiple**

6. Si $f$ es derivable en $a$, entonces:
   - a) $f$ es continua en $a$, pero no al revés
   - b) $f$ es continua en $a$ y viceversa
   - c) $f$ no tiene por qué ser continua en $a$
   - d) $f'(a)$ es necesariamente positiva

   > **Respuesta correcta:** a) Derivabilidad implica continuidad, pero la continuidad no implica derivabilidad (contraejemplo: $|x|$ en $x=0$).

7. Una función continua en $a$ es:
   - a) Siempre derivable en $a$
   - b) Nunca derivable en $a$
   - c) No necesariamente derivable en $a$
   - d) Derivable si y solo si $f(a)=0$

   > **Respuesta correcta:** c) La continuidad es condición necesaria pero no suficiente para la derivabilidad.

---

#### 7.3.3 Relación entre derivabilidad y continuidad

**Ejercicio Resuelto**

Demuestra formalmente que si $f$ es derivable en $a$, entonces $f$ es continua en $a$.

**Demostración:**

Supongamos que $f'(a)$ existe (es finita). Queremos probar que $\lim_{x\to a}f(x)=f(a)$, equivalentemente $\lim_{h\to0}f(a+h)=f(a)$.

Escribimos:

$$f(a+h)-f(a) = \frac{f(a+h)-f(a)}{h}\cdot h$$

Tomando el límite cuando $h\to0$:

$$\lim_{h\to0}\left[f(a+h)-f(a)\right] = \lim_{h\to0}\frac{f(a+h)-f(a)}{h}\cdot\lim_{h\to0}h = f'(a)\cdot 0 = 0$$

Por tanto $\lim_{h\to0}f(a+h)=f(a)$, lo que prueba la continuidad de $f$ en $a$. $\blacksquare$

**Contraejemplo del recíproco:** $f(x)=|x|$ es continua en $0$ pero no derivable en $0$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Proporciona un ejemplo de función continua en $x=0$ que no sea derivable en $x=0$.

   > **Solución:** $f(x)=|x|$. Continua en $0$ ($f(0)=0$, límite $0$), pero $f'_+(0)=1\neq-1=f'_-(0)$ → no derivable.

2. ¿Es $f(x)=\sqrt[3]{x}$ continua en $x=0$? ¿Es derivable?

   > **Solución:** Continua ($f(0)=0$, $\lim_{x\to0}\sqrt[3]{x}=0$). No derivable: $f'(x)=\dfrac{1}{3}x^{-2/3}\to\infty$ cuando $x\to0$.

**Nivel Intermedio:**

3. Clasifica como «verdadero» o «falso» y justifica: "Si $f$ no es continua en $a$, entonces no es derivable en $a$."

   > **Solución:** **Verdadero.** El contracontrapositivo del teorema: derivable $\Rightarrow$ continua, equivale a: no continua $\Rightarrow$ no derivable.

4. Da un ejemplo de función no continua en $a=1$. Comprueba que no es derivable ahí.

   > **Solución:** $f(x)=\dfrac{x^2-1}{x-1}$ (para $x\neq1$) con $f(1)=0$.  
   > $\lim_{x\to1}f(x)=2\neq0=f(1)$ → discontinuidad evitable en $x=1$ → no derivable.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\begin{cases}\dfrac{x^2-4}{x-2} & x\neq2 \\ k & x=2\end{cases}$.

   a) Determina el valor de $k$ para que $f$ sea continua en $x=2$.  
   b) Con ese valor, ¿es $f$ derivable en $x=2$?  
   c) Calcula $f'(2)$ si existe.

   > **Solución:**
   >
   > **a)** $\lim_{x\to2}\dfrac{x^2-4}{x-2}=\lim_{x\to2}\dfrac{(x-2)(x+2)}{x-2}=\lim_{x\to2}(x+2)=4$.  
   > Para continuidad: $k=4$.
   >
   > **b)** Con $k=4$, $f(x)=x+2$ para $x\neq2$ y $f(2)=4=2+2$. Luego $f(x)=x+2$ en todos los reales → polinomio, derivable en todos los puntos.
   >
   > **c)** $f'(x)=1$ para todo $x$, en particular $f'(2)=1$.

**Test de Opción Múltiple**

6. La función $f(x)=|x-3|$ en $x=3$:
   - a) Es continua y derivable
   - b) No es continua y no es derivable
   - c) Es continua pero no derivable
   - d) No es continua pero es derivable

   > **Respuesta correcta:** c) $|x-3|$ es continua en todos los reales (en particular en $x=3$), pero no es derivable en $x=3$ (derivadas laterales $1$ y $-1$).

7. La implicación «derivable en $a$ $\Rightarrow$ continua en $a$»:
   - a) Es falsa
   - b) Es verdadera, y su recíproco también es verdadero
   - c) Es verdadera, pero el recíproco es falso en general
   - d) Solo es válida para funciones polinómicas

   > **Respuesta correcta:** c) Toda función derivable es continua, pero no toda función continua es derivable.

---

#### 7.3.4 Estudio de derivabilidad de funciones definidas a trozos

**Ejercicio Resuelto**

Estudia la derivabilidad de $f(x)=\begin{cases}x^3-x & x<0\\x^2 & 0\leq x\leq2\\4x-4 & x>2\end{cases}$ en los puntos $x=0$ y $x=2$.

**En $x=0$:**

*Continuidad:* $\lim_{x\to0^-}(x^3-x)=0$; $f(0)=0$; $\lim_{x\to0^+}x^2=0$ ✓ continua.

*Derivadas laterales:*
$$f'_-(0)=(x^3-x)'|_{x=0}=(3x^2-1)|_{x=0}=-1$$
$$f'_+(0)=(x^2)'|_{x=0}=2x|_{x=0}=0$$

Como $-1\neq0$, **$f$ no es derivable en $x=0$**.

**En $x=2$:**

*Continuidad:* $\lim_{x\to2^-}x^2=4$; $f(2)=4$; $\lim_{x\to2^+}(4x-4)=4$ ✓ continua.

*Derivadas laterales:*
$$f'_-(2)=2x|_{x=2}=4$$
$$f'_+(2)=4$$

Como $4=4$, **$f$ es derivable en $x=2$** con $f'(2)=4$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Estudia la derivabilidad de $f(x)=\begin{cases}2x & x\leq1\\x^2+1 & x>1\end{cases}$ en $x=1$.

   > **Solución:** Continuidad: $f(1)=2$; $\lim_{x\to1^+}(x^2+1)=2$ ✓. Derivadas: $f'_-(1)=2$; $f'_+(1)=2$ ✓.  
   > $f$ **es derivable** en $x=1$.

2. Estudia la derivabilidad de $g(x)=\begin{cases}x+1 & x\leq2\\x^2-1 & x>2\end{cases}$ en $x=2$.

   > **Solución:** Continuidad: $g(2)=3$; $\lim_{x\to2^+}(x^2-1)=3$ ✓. Derivadas: $g'_-(2)=1$; $g'_+(2)=2\cdot2=4$.  
   > $1\neq4$ → $g$ **no es derivable** en $x=2$.

**Nivel Intermedio:**

3. Halla $a$ y $b$ para que $f(x)=\begin{cases}x^2+ax & x\leq1\\bx+2 & x>1\end{cases}$ sea derivable en $x=1$.

   > **Solución:** Continuidad: $1+a=b+2 \Rightarrow a-b=1$ ... (1).  
   > Derivabilidad: $f'_-(1)=2x+a|_{x=1}=2+a$; $f'_+(1)=b$.  
   > $2+a=b$ ... (2). De (1) y (2): $2+a=a-1$? No, $2+a=b=a-1 \Rightarrow 2=-1$ → contradicción.  
   > De (1): $b=a-1$. De (2): $b=2+a$. Entonces $a-1=2+a \Rightarrow -1=2$ → **no existe** solución. Ambas condiciones son incompatibles.

4. Estudia la continuidad y derivabilidad de $f(x)=\begin{cases}e^x & x\leq0\\\cos x & x>0\end{cases}$ en $x=0$.

   > **Solución:** Continuidad: $f(0)=e^0=1$; $\lim_{x\to0^+}\cos x=1$ ✓.  
   > Derivadas: $f'_-(0)=e^0=1$; $f'_+(0)=-\sin0=0$. $1\neq0$ → **no derivable** en $x=0$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\begin{cases}x^2-1 & x<0\\ax+b & 0\leq x<3\\x^2-6x+k & x\geq3\end{cases}$.

   Determina $a$, $b$, $k$ para que $f$ sea derivable en $x=0$ y $x=3$.

   > **Solución:**
   >
   > **En $x=0$:**  
   > Continuidad: $\lim_{x\to0^-}(x^2-1)=-1=f(0)=b \Rightarrow b=-1$.  
   > Derivabilidad: $f'_-(0)=2\cdot0=0$; $f'_+(0)=a$. Luego $a=0$.
   >
   > **En $x=3$** (con $a=0$, $b=-1$, tramo medio $f(x)=-1$):  
   > Continuidad: $f(3^-)=0\cdot3-1=-1$; $f(3^+)=9-18+k=k-9$. Luego $k-9=-1 \Rightarrow k=8$.  
   > Derivabilidad: $f'_-(3)=a=0$; $f'_+(3)=(2x-6)|_{x=3}=0$ ✓.
   >
   > **Resultado:** $a=0$, $b=-1$, $k=8$.

**Test de Opción Múltiple**

6. Para estudiar la derivabilidad de una función definida a trozos en el punto de unión $x=a$, se debe:
   - a) Solo verificar que $f(a)$ existe
   - b) Calcular la derivada ordinaria en $x=a$
   - c) Verificar continuidad y luego igualar las derivadas laterales de cada tramo en $x=a$
   - d) Comprobar que ambos trozos son polinomios

   > **Respuesta correcta:** c) Primero continuidad, luego igualdad de derivadas laterales calculadas desde cada tramo.

7. Si una función a trozos es continua pero no derivable en el punto de unión, la gráfica tiene:
   - a) Un salto
   - b) Una asíntota
   - c) Un ángulo o "pico" (cambio brusco de pendiente)
   - d) Un punto de inflexión

   > **Respuesta correcta:** c) La no derivabilidad con continuidad indica un cambio brusco de dirección (pico o vértice) en la gráfica.

---

#### 7.3.5 Cálculo de parámetros para que una función sea derivable

**Ejercicio Resuelto**

Halla $a$ y $b$ para que $f(x)=\begin{cases}ax^2+bx & x\leq2\\x^3-5x & x>2\end{cases}$ sea derivable en $x=2$.

**Paso 1 — Continuidad (condición necesaria):**

$$\lim_{x\to2^-}(ax^2+bx)=4a+2b$$
$$\lim_{x\to2^+}(x^3-5x)=8-10=-2$$

$4a+2b=-2$ → $2a+b=-1$ ... (I)

**Paso 2 — Derivabilidad:**

$$f'_-(2)=(2ax+b)|_{x=2}=4a+b$$
$$f'_+(2)=(3x^2-5)|_{x=2}=12-5=7$$

$4a+b=7$ ... (II)

**Paso 3 — Resolver el sistema:**

De (II)−(I): $(4a+b)-(2a+b)=7-(-1) \Rightarrow 2a=8 \Rightarrow a=4$

Sustituyendo en (I): $8+b=-1 \Rightarrow b=-9$

**Conclusión:** $a=4$, $b=-9$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla $a$ para que $f(x)=\begin{cases}ax+1 & x\leq3\\x^2-8 & x>3\end{cases}$ sea continua en $x=3$.

   > **Solución:** $3a+1=9-8=1 \Rightarrow 3a=0 \Rightarrow a=0$.

2. Halla $a$ para que $f(x)=\begin{cases}x^2 & x\leq1\\ax+2 & x>1\end{cases}$ sea continua y derivable en $x=1$.

   > **Solución:** Continuidad: $1=a+2 \Rightarrow a=-1$. Derivabilidad: $f'_-(1)=2$; $f'_+(1)=a=-1$. $2\neq-1$ → **no existe** $a$ que cumpla ambas condiciones.

**Nivel Intermedio:**

3. Halla $a$ y $b$ para que $f(x)=\begin{cases}x^2+1 & x\leq1\\ax+b & x>1\end{cases}$ sea derivable en $x=1$.

   > **Solución:** Continuidad: $2=a+b$ ... (I). Derivabilidad: $f'_-(1)=2$; $f'_+(1)=a$. Luego $a=2$, $b=0$.

4. Sea $f(x)=\begin{cases}\ln(x+1)+a & x>0\\bx^2+x & x\leq0\end{cases}$. Halla $a$ y $b$ para que $f$ sea derivable en $x=0$.

   > **Solución:** Continuidad: $f(0^-)=0$; $f(0^+)=\ln1+a=a$. Luego $a=0$.  
   > Derivadas: $f'_-(0)=b\cdot0\cdot2+1=1$ (derivada de $bx^2+x$ en $x=0$: $(2bx+1)|_{x=0}=1$).  
   > $f'_+(0)=\dfrac{1}{0+1}=1$. Ambas son $1$ para cualquier $b$. Luego $a=0$ y $b$ puede ser cualquier valor.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\begin{cases}x^2+ax+b & x\leq1\\x^3-x+c & x>1\end{cases}$.

   Halla los valores de $a$, $b$, $c$ para que $f$ sea derivable en $x=1$ y $f(0)=3$.

   > **Solución:**
   > $f(0)=0+0+b=b=3 \Rightarrow b=3$.  
   > Continuidad en $x=1$: $1+a+3=1-1+c \Rightarrow 4+a=c$ ... (I).  
   > Derivabilidad en $x=1$: $f'_-(1)=2x+a|_{x=1}=2+a$; $f'_+(1)=3x^2-1|_{x=1}=2$. Luego $2+a=2 \Rightarrow a=0$.  
   > De (I): $c=4$.
   >
   > **Resultado:** $a=0$, $b=3$, $c=4$.

**Test de Opción Múltiple**

6. Para que una función a trozos sea derivable en el punto de unión, el número de condiciones que se debe satisfacer es:
   - a) 1 (solo la derivada)
   - b) 2 (continuidad y derivadas laterales iguales)
   - c) 3 (límites por la izquierda, por la derecha y el valor)
   - d) Depende del grado de los polinomios

   > **Respuesta correcta:** b) Continuidad (una condición) y igualdad de derivadas laterales (otra condición): 2 condiciones en total.

7. Si se tienen dos parámetros $a$ y $b$, el sistema para derivabilidad en un punto de unión suele tener:
   - a) Siempre solución única
   - b) Siempre infinitas soluciones
   - c) Solución única, ninguna solución, o infinitas, dependiendo del sistema
   - d) Solo solución si los trozos son polinomios de igual grado

   > **Respuesta correcta:** c) El sistema $2\times2$ puede tener solución única, ser incompatible o indeterminado.

---

#### 7.4.1 Ecuación de la recta tangente a una curva en un punto

**Ejercicio Resuelto**

Halla la ecuación de la recta tangente a $f(x)=x^3-3x+2$ en el punto de abscisa $x=1$.

**Paso 1 — Calcular el punto de tangencia:**

$$f(1) = 1-3+2 = 0 \quad \Rightarrow \quad P=(1,0)$$

**Paso 2 — Calcular la pendiente (derivada en $x=1$):**

$$f'(x) = 3x^2-3 \quad \Rightarrow \quad f'(1)=3-3=0$$

**Paso 3 — Ecuación de la recta tangente** (pendiente $0$ → tangente horizontal):

$$y - 0 = 0\cdot(x-1) \quad \Rightarrow \quad \boxed{y=0}$$

La tangente en $(1,0)$ es el propio eje $OX$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla la recta tangente a $f(x)=x^2$ en $x=-2$.

   > **Solución:** $f(-2)=4$, $f'(x)=2x$, $f'(-2)=-4$.  
   > Tangente: $y-4=-4(x+2) \Rightarrow y=-4x-4$.

2. Halla la recta tangente a $f(x)=\sqrt{x}$ en $x=9$.

   > **Solución:** $f(9)=3$, $f'(x)=\dfrac{1}{2\sqrt{x}}$, $f'(9)=\dfrac{1}{6}$.  
   > Tangente: $y-3=\dfrac{1}{6}(x-9) \Rightarrow y=\dfrac{x}{6}+\dfrac{3}{2}$.

**Nivel Intermedio:**

3. Halla la recta tangente a $f(x)=e^x$ que sea paralela a $y=e^2\cdot x$.

   > **Solución:** La pendiente de la tangente debe ser $e^2$. $f'(x)=e^x=e^2 \Rightarrow x=2$. Punto: $(2, e^2)$.  
   > Tangente: $y-e^2=e^2(x-2) \Rightarrow y=e^2x-e^2$.

4. Halla la recta tangente a $f(x)=\ln x$ en el punto donde la pendiente es $\dfrac{1}{3}$.

   > **Solución:** $f'(x)=\dfrac{1}{x}=\dfrac{1}{3} \Rightarrow x=3$. $f(3)=\ln3$.  
   > Tangente: $y-\ln3=\dfrac{1}{3}(x-3) \Rightarrow y=\dfrac{x}{3}-1+\ln3$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\dfrac{x^2}{x-1}$.

   a) Halla $f'(x)$.  
   b) Determina la ecuación de la tangente en $x=2$.  
   c) Determina en qué puntos la tangente es horizontal.

   > **Solución:**
   >
   > **a)** $f'(x)=\dfrac{2x(x-1)-x^2\cdot1}{(x-1)^2}=\dfrac{x^2-2x}{(x-1)^2}=\dfrac{x(x-2)}{(x-1)^2}$.
   >
   > **b)** $f(2)=4$; $f'(2)=\dfrac{2\cdot0}{1}=0$. Tangente: $y=4$ (horizontal).
   >
   > **c)** $f'(x)=0 \Leftrightarrow x=0$ o $x=2$.  
   > Puntos: $(0, 0)$ y $(2, 4)$.

**Test de Opción Múltiple**

6. La ecuación de la recta tangente a $y=f(x)$ en el punto $(a, f(a))$ es:
   - a) $y=f'(a)$
   - b) $y=f'(a)(x-a)$
   - c) $y-f(a)=f'(a)(x-a)$
   - d) $y=f(a)x+f'(a)$

   > **Respuesta correcta:** c) La ecuación punto-pendiente con punto $(a,f(a))$ y pendiente $f'(a)$.

7. Si la recta tangente a $f(x)=x^2+bx$ en $x=1$ tiene pendiente $5$, entonces $b=$:
   - a) $3$
   - b) $5$
   - c) $1$
   - d) $-1$

   > **Respuesta correcta:** a) $f'(x)=2x+b$; $f'(1)=2+b=5 \Rightarrow b=3$.

---

#### 7.4.2 Ecuación de la recta normal a una curva en un punto

**Ejercicio Resuelto**

Halla la ecuación de la recta normal a $f(x)=x^2-4$ en el punto $(2, 0)$.

**Paso 1 — Pendiente de la tangente:**

$$f'(x)=2x \quad \Rightarrow \quad f'(2)=4$$

**Paso 2 — Pendiente de la normal** (perpendicular a la tangente):

$$m_n = -\frac{1}{m_t} = -\frac{1}{4}$$

**Paso 3 — Ecuación de la normal:**

$$y-0=-\frac{1}{4}(x-2) \quad \Rightarrow \quad y=-\frac{x}{4}+\frac{1}{2}$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla la recta normal a $f(x)=x^3$ en $x=1$.

   > **Solución:** $f(1)=1$; $f'(1)=3$. Normal: pendiente $m_n=-\dfrac{1}{3}$.  
   > $y-1=-\dfrac{1}{3}(x-1) \Rightarrow y=-\dfrac{x}{3}+\dfrac{4}{3}$.

2. Halla la recta normal a $f(x)=\sin x$ en $x=0$.

   > **Solución:** $f(0)=0$; $f'(0)=\cos0=1$. Normal: $m_n=-1$.  
   > $y=-x$.

**Nivel Intermedio:**

3. Halla la recta normal a $f(x)=e^x$ en el punto donde $f'=e$.

   > **Solución:** $f'(x)=e^x=e \Rightarrow x=1$; $f(1)=e$. Normal: $m_n=-\dfrac{1}{e}$.  
   > $y-e=-\dfrac{1}{e}(x-1) \Rightarrow y=-\dfrac{x}{e}+\dfrac{1}{e}+e$.

4. Halla las ecuaciones de la tangente y la normal a $f(x)=\ln x$ en $x=1$.

   > **Solución:** $f(1)=0$; $f'(1)=1$. Tangente: $y=x-1$. Normal: $m_n=-1$; $y=-(x-1)=-x+1$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\sqrt{4-x^2}$ (semicircunferencia superior de radio 2).

   a) Calcula $f'(x)$ para $x\in(-2,2)$.  
   b) Halla la tangente y la normal en el punto $(\sqrt{2}, \sqrt{2})$.  
   c) Interpreta geométricamente la recta normal.

   > **Solución:**
   >
   > **a)** $f'(x)=\dfrac{-2x}{2\sqrt{4-x^2}}=\dfrac{-x}{\sqrt{4-x^2}}$.
   >
   > **b)** En $x=\sqrt{2}$: $f'(\sqrt{2})=\dfrac{-\sqrt{2}}{\sqrt{2}}=-1$.  
   > Tangente: $y-\sqrt{2}=-1(x-\sqrt{2}) \Rightarrow y=-x+2\sqrt{2}$.  
   > Normal: $m_n=1$; $y-\sqrt{2}=x-\sqrt{2} \Rightarrow y=x$.
   >
   > **c)** La recta normal $y=x$ pasa por el origen $(0,0)$, que es el centro de la circunferencia. Geométricamente, la normal en cualquier punto de una circunferencia pasa por su centro.

**Test de Opción Múltiple**

6. Si la recta tangente a $f$ en un punto tiene pendiente $m\neq0$, la recta normal tiene pendiente:
   - a) $m$
   - b) $-m$
   - c) $\dfrac{1}{m}$
   - d) $-\dfrac{1}{m}$

   > **Respuesta correcta:** d) Dos rectas perpendiculares cumplen $m_1\cdot m_2=-1$, luego $m_n=-\dfrac{1}{m_t}$.

7. Si la recta tangente a $f$ en un punto es horizontal ($m_t=0$), la recta normal es:
   - a) Horizontal
   - b) Vertical
   - c) Con pendiente $1$
   - d) Con pendiente $-1$

   > **Respuesta correcta:** b) Si $m_t=0$, la normal es perpendicular a la horizontal, es decir, vertical.

---

#### 7.4.3 Puntos de la curva con tangente horizontal o con pendiente dada

**Ejercicio Resuelto**

Halla todos los puntos de $f(x)=x^3-6x^2+9x+1$ donde la recta tangente es horizontal.

**Tangente horizontal** ↔ $f'(x)=0$.

$$f'(x)=3x^2-12x+9=3(x^2-4x+3)=3(x-1)(x-3)$$

$$f'(x)=0 \Leftrightarrow x=1 \quad \text{o} \quad x=3$$

**Puntos de la curva:**

$$f(1)=1-6+9+1=5 \quad \Rightarrow \quad P_1=(1,5)$$
$$f(3)=27-54+27+1=1 \quad \Rightarrow \quad P_2=(3,1)$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla los puntos de $f(x)=x^2-4x+3$ donde la tangente es horizontal.

   > **Solución:** $f'(x)=2x-4=0 \Rightarrow x=2$. Punto: $(2, -1)$.

2. Halla los puntos de $f(x)=\sin x$ en $[0, 2\pi]$ donde la pendiente de la tangente es $0$.

   > **Solución:** $f'(x)=\cos x=0 \Rightarrow x=\dfrac{\pi}{2}$ y $x=\dfrac{3\pi}{2}$.  
   > Puntos: $\left(\dfrac{\pi}{2},1\right)$ y $\left(\dfrac{3\pi}{2},-1\right)$.

**Nivel Intermedio:**

3. Halla los puntos de $f(x)=x^3-3x$ donde la tangente tiene pendiente $9$.

   > **Solución:** $f'(x)=3x^2-3=9 \Rightarrow x^2=4 \Rightarrow x=\pm2$.  
   > Puntos: $(2, 2)$ y $(-2, -2)$.

4. Halla los puntos de $f(x)=x^4-8x^2$ donde la tangente es paralela a $y=-8x$.

   > **Solución:** Pendiente deseada: $-8$. $f'(x)=4x^3-16x=-8 \Rightarrow 4x^3-16x+8=0 \Rightarrow x^3-4x+2=0$.  
   > Una raíz evidente: $x=$ no trivial. Numéricamente: una raíz en $(-2{,}2;-2{,}1)$, otra cerca de $(0{,}5)$ y otra cerca de $(1{,}7)$. (Ecuación cúbica sin raíces racionales obvias; se acepta dejar en forma implícita.)

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=x^3-3x^2$.

   a) Calcula $f'(x)$.  
   b) Halla los puntos donde la tangente es horizontal e indica si son máximos o mínimos locales.  
   c) Escribe la ecuación de la tangente en $x=-1$.

   > **Solución:**
   >
   > **a)** $f'(x)=3x^2-6x=3x(x-2)$.
   >
   > **b)** $f'(x)=0 \Leftrightarrow x=0$ o $x=2$.  
   > $f''(x)=6x-6$: $f''(0)=-6<0$ → máximo local en $(0, 0)$.  
   > $f''(2)=6>0$ → mínimo local en $(2, -4)$.
   >
   > **c)** $f(-1)=-1-3=-4$; $f'(-1)=3+6=9$. Tangente: $y+4=9(x+1) \Rightarrow y=9x+5$.

**Test de Opción Múltiple**

6. En los puntos donde la tangente a $f$ es horizontal, necesariamente:
   - a) $f$ tiene un máximo o mínimo local
   - b) $f'=0$, pero puede haber también un punto de inflexión
   - c) $f$ es constante
   - d) $f''=0$

   > **Respuesta correcta:** b) $f'(x)=0$ es condición necesaria para extremo relativo, pero también puede ocurrir en un punto de inflexión (ej. $f(x)=x^3$ en $x=0$).

7. Si $f'(2)=3$, la recta tangente en $x=2$ tiene:
   - a) Pendiente $3$ e intersecta el eje $OY$ en $3$
   - b) Pendiente $3$ y pasa por $(2, f(2))$
   - c) Pendiente $\dfrac{1}{3}$
   - d) Ecuación $y=3x$

   > **Respuesta correcta:** b) La tangente en $x=2$ tiene pendiente $f'(2)=3$ y pasa por el punto $(2, f(2))$.

---

#### 7.5.1 Enunciado de la regla de L'Hôpital (formas 0/0 y ∞/∞)

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x\to 0}\frac{\sin x}{x}$ usando la regla de L'Hôpital.

**Verificar la indeterminación:**

$$\lim_{x\to 0}\frac{\sin x}{x} = \frac{\sin 0}{0} = \frac{0}{0} \quad \checkmark$$

**Aplicar L'Hôpital** (derivar numerador y denominador por separado):

$$\lim_{x\to 0}\frac{\sin x}{x} \stackrel{L'H}{=} \lim_{x\to 0}\frac{(\sin x)'}{(x)'} = \lim_{x\to 0}\frac{\cos x}{1} = \cos 0 = 1$$

**Nota:** Este es el **límite fundamental trigonométrico**, confirmado por L'Hôpital.

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $\displaystyle\lim_{x\to1}\dfrac{x^2-1}{x-1}$ mediante L'Hôpital.

   > **Solución:** $\dfrac{0}{0}$. L'H: $\lim_{x\to1}\dfrac{2x}{1}=2$.  
   > (Verificación directa: $\dfrac{(x-1)(x+1)}{x-1}=x+1\to2$.)

2. Calcula $\displaystyle\lim_{x\to0}\dfrac{e^x-1}{x}$.

   > **Solución:** $\dfrac{0}{0}$. L'H: $\lim_{x\to0}\dfrac{e^x}{1}=e^0=1$.

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x\to+\infty}\dfrac{\ln x}{x}$.

   > **Solución:** $\dfrac{\infty}{\infty}$. L'H: $\lim_{x\to\infty}\dfrac{1/x}{1}=\lim_{x\to\infty}\dfrac{1}{x}=0$.

4. Calcula $\displaystyle\lim_{x\to0}\dfrac{1-\cos x}{x^2}$.

   > **Solución:** $\dfrac{0}{0}$. L'H: $\lim_{x\to0}\dfrac{\sin x}{2x}$. Otra vez $\dfrac{0}{0}$. L'H de nuevo: $\lim_{x\to0}\dfrac{\cos x}{2}=\dfrac{1}{2}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula los siguientes límites, indicando la indeterminación y el método:

   a) $\displaystyle\lim_{x\to0}\dfrac{\tan x - x}{x^3}$  
   b) $\displaystyle\lim_{x\to+\infty}\dfrac{e^x}{x^2}$  
   c) $\displaystyle\lim_{x\to0}\dfrac{\ln(1+x)}{x}$

   > **Solución:**
   >
   > **a)** $\dfrac{0}{0}$. L'H: $\lim\dfrac{\sec^2x-1}{3x^2}=\lim\dfrac{\tan^2x}{3x^2}$. L'H: $\lim\dfrac{2\tan x\sec^2x}{6x}$. L'H: en $x=0$: $\dfrac{0}{0}$.  
   > Alternativamente, usando $\tan^2x\approx x^2$ cerca de $0$: $\lim\dfrac{x^2}{3x^2}=\dfrac{1}{3}$.  
   > Resultado: $\dfrac{1}{3}$.
   >
   > **b)** $\dfrac{\infty}{\infty}$. L'H: $\lim\dfrac{e^x}{2x}$. $\dfrac{\infty}{\infty}$. L'H: $\lim\dfrac{e^x}{2}=+\infty$.
   >
   > **c)** $\dfrac{0}{0}$. L'H: $\lim_{x\to0}\dfrac{\frac{1}{1+x}}{1}=\dfrac{1}{1}=1$.

**Test de Opción Múltiple**

6. La regla de L'Hôpital se puede aplicar cuando el límite presenta la forma:
   - a) $0+\infty$
   - b) $\dfrac{0}{0}$ o $\dfrac{\infty}{\infty}$
   - c) $0\cdot0$
   - d) $1+\infty$

   > **Respuesta correcta:** b) L'Hôpital se aplica directamente a las formas indeterminadas $\dfrac{0}{0}$ y $\dfrac{\infty}{\infty}$.

7. Al aplicar L'Hôpital a $\lim\dfrac{f(x)}{g(x)}$, se deriva:
   - a) El cociente completo $\dfrac{f}{g}$
   - b) El numerador $f$ y el denominador $g$ por separado, formando $\dfrac{f'}{g'}$
   - c) Solo el numerador
   - d) El cociente usando la regla del cociente

   > **Respuesta correcta:** b) L'Hôpital indica que $\lim\dfrac{f(x)}{g(x)}=\lim\dfrac{f'(x)}{g'(x)}$, derivando numerador y denominador por separado.

---

#### 7.5.2 Aplicación iterada de L'Hôpital

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x\to0}\frac{e^x-1-x}{x^2}$ aplicando L'Hôpital las veces necesarias.

**Primera aplicación** (forma $\frac{0}{0}$):

$$\lim_{x\to0}\frac{e^x-1-x}{x^2} \stackrel{L'H}{=} \lim_{x\to0}\frac{e^x-1}{2x}$$

**Segunda aplicación** (sigue siendo $\frac{0}{0}$):

$$\lim_{x\to0}\frac{e^x-1}{2x} \stackrel{L'H}{=} \lim_{x\to0}\frac{e^x}{2} = \frac{e^0}{2} = \frac{1}{2}$$

**Ejercicios con Solución**

**Nivel Básico:**

1. Aplica L'Hôpital dos veces para calcular $\displaystyle\lim_{x\to0}\dfrac{x-\sin x}{x^3}$.

   > **Solución:** L'H$_1$: $\lim\dfrac{1-\cos x}{3x^2}$ ($\frac{0}{0}$). L'H$_2$: $\lim\dfrac{\sin x}{6x}$ ($\frac{0}{0}$). L'H$_3$: $\lim\dfrac{\cos x}{6}=\dfrac{1}{6}$.

2. Calcula $\displaystyle\lim_{x\to+\infty}\dfrac{x^2}{e^x}$.

   > **Solución:** $\dfrac{\infty}{\infty}$. L'H: $\lim\dfrac{2x}{e^x}$. L'H: $\lim\dfrac{2}{e^x}=0$.

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x\to0}\dfrac{e^x - 1 - x - \frac{x^2}{2}}{x^3}$.

   > **Solución:** Aplicando L'Hôpital tres veces:  
   > L'H$_1$: $\lim\dfrac{e^x-1-x}{3x^2}$. L'H$_2$: $\lim\dfrac{e^x-1}{6x}$. L'H$_3$: $\lim\dfrac{e^x}{6}=\dfrac{1}{6}$.

4. Calcula $\displaystyle\lim_{x\to+\infty}\dfrac{(\ln x)^3}{x}$.

   > **Solución:** $\dfrac{\infty}{\infty}$. L'H: $\lim\dfrac{3(\ln x)^2\cdot\frac{1}{x}}{1}=\lim\dfrac{3(\ln x)^2}{x}$.  
   > L'H de nuevo: $\lim\dfrac{6\ln x\cdot\frac{1}{x}}{1}=\lim\dfrac{6\ln x}{x}$. L'H: $\lim\dfrac{6/x}{1}=0$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula:

   a) $\displaystyle\lim_{x\to0}\dfrac{x^2}{1-\cos x}$  
   b) $\displaystyle\lim_{x\to0}\dfrac{\sin x - x\cos x}{x^3}$

   > **Solución:**
   >
   > **a)** $\dfrac{0}{0}$. L'H: $\lim\dfrac{2x}{\sin x}=\lim\dfrac{2}{\cos x/x}$... Mejor: L'H otra vez: $\lim\dfrac{2x}{\sin x}$ ($\dfrac{0}{0}$), L'H: $\lim\dfrac{2}{\cos x}=\dfrac{2}{1}=2$.
   >
   > **b)** $\dfrac{0}{0}$. L'H: $\lim\dfrac{\cos x - (\cos x - x\sin x)}{3x^2}=\lim\dfrac{x\sin x}{3x^2}=\lim\dfrac{\sin x}{3x}$.  
   > L'H: $\lim\dfrac{\cos x}{3}=\dfrac{1}{3}$.

**Test de Opción Múltiple**

6. Si tras aplicar L'Hôpital una vez el límite sigue siendo $\frac{0}{0}$ o $\frac{\infty}{\infty}$:
   - a) El límite no existe
   - b) Se puede aplicar L'Hôpital de nuevo
   - c) El resultado es $0$
   - d) Se debe usar otro método

   > **Respuesta correcta:** b) L'Hôpital puede aplicarse iteradamente mientras persista la indeterminación.

7. $\displaystyle\lim_{x\to0}\dfrac{\sin x - x}{x^3}$ usando L'Hôpital da:
   - a) $0$
   - b) $1$
   - c) $-\dfrac{1}{6}$
   - d) $\dfrac{1}{6}$

   > **Respuesta correcta:** c) Tras tres aplicaciones de L'Hôpital se obtiene $\lim_{x\to0}\dfrac{-\cos x}{6}=-\dfrac{1}{6}$.

---

#### 7.5.3 Resolución de indeterminaciones 0·∞, ∞−∞ y formas exponenciales mediante L'Hôpital

**Ejercicio Resuelto**

Calcula $\displaystyle\lim_{x\to 0^+}x\ln x$ (forma $0\cdot\infty$).

**Transformar a forma $\frac{0}{0}$ o $\frac{\infty}{\infty}$:**

$$x\ln x = \frac{\ln x}{1/x}$$

Cuando $x\to0^+$: numerador $\to-\infty$, denominador $\to+\infty$ → forma $\frac{-\infty}{+\infty}$.

**Aplicar L'Hôpital:**

$$\lim_{x\to 0^+}\frac{\ln x}{1/x} \stackrel{L'H}{=} \lim_{x\to 0^+}\frac{1/x}{-1/x^2} = \lim_{x\to 0^+}\frac{x^2/x}{(-1)} \cdot\frac{1}{1} = \lim_{x\to 0^+}(-x) = 0$$

**Resultado:** $\displaystyle\lim_{x\to 0^+}x\ln x = 0$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula $\displaystyle\lim_{x\to+\infty}xe^{-x}$ (forma $\infty\cdot0$).

   > **Solución:** $\dfrac{x}{e^x}$ ($\dfrac{\infty}{\infty}$). L'H: $\lim\dfrac{1}{e^x}=0$.

2. Calcula $\displaystyle\lim_{x\to+\infty}(\sqrt{x+1}-\sqrt{x})$ (forma $\infty-\infty$).

   > **Solución:** Racionalizar: $\dfrac{(x+1)-x}{\sqrt{x+1}+\sqrt{x}}=\dfrac{1}{\sqrt{x+1}+\sqrt{x}}\to0$.

**Nivel Intermedio:**

3. Calcula $\displaystyle\lim_{x\to1^-}\left(\frac{1}{\ln x}+\frac{1}{x-1}\right)$ (forma $\infty-\infty$... o $-\infty+\infty$).

   > **Solución:** $\dfrac{(x-1)+\ln x}{(x-1)\ln x}$. En $x\to1$: $\dfrac{0}{0}$. L'H: $\dfrac{1+1/x}{\ln x+1}$ → en $x=1$: $\dfrac{2}{0+1}=2$.

4. Calcula $\displaystyle\lim_{x\to0^+}(1+x)^{1/x}$ (forma $1^\infty$).

   > **Solución:** Sea $L=\lim(1+x)^{1/x}$. $\ln L=\lim\dfrac{\ln(1+x)}{x}$. L'H: $\lim\dfrac{1/(1+x)}{1}=1$. Luego $L=e^1=e$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Calcula:

   a) $\displaystyle\lim_{x\to+\infty}\left(1+\dfrac{2}{x}\right)^x$ (forma $1^\infty$)  
   b) $\displaystyle\lim_{x\to0^+}x^x$ (forma $0^0$)  
   c) $\displaystyle\lim_{x\to+\infty}x\cdot\ln\left(1+\dfrac{1}{x}\right)$ (forma $\infty\cdot0$)

   > **Solución:**
   >
   > **a)** $\ln L=\lim x\ln\left(1+\dfrac{2}{x}\right)=\lim\dfrac{\ln(1+2/x)}{1/x}$. L'H: $\lim\dfrac{\frac{-2/x^2}{1+2/x}}{-1/x^2}=\lim\dfrac{2}{1+2/x}=2$. $L=e^2$.
   >
   > **b)** $\ln L=\lim_{x\to0^+}x\ln x=0$ (calculado antes). $L=e^0=1$.
   >
   > **c)** $\dfrac{\ln(1+1/x)}{1/x}$. L'H: $\dfrac{\frac{-1/x^2}{1+1/x}}{-1/x^2}=\dfrac{1}{1+1/x}\to1$.

**Test de Opción Múltiple**

6. Para calcular $\lim_{x\to0^+}x^x$ (forma $0^0$), se usa la técnica:
   - a) Racionalización
   - b) L'Hôpital directamente
   - c) Tomar logaritmos y luego L'Hôpital
   - d) Cambio de variable $t=1/x$

   > **Respuesta correcta:** c) Se escribe $y=x^x$, se toma $\ln y=x\ln x$ y se calcula el límite de $x\ln x$ (forma $0\cdot\infty$) con L'Hôpital.

7. $\displaystyle\lim_{x\to0^+}x\ln x$ es igual a:
   - a) $-\infty$
   - b) $1$
   - c) $0$
   - d) $e$

   > **Respuesta correcta:** c) Como se calculó, $\lim_{x\to0^+}x\ln x=0$.

---

#### 7.6.1 Teorema de Rolle: enunciado, condiciones e interpretación geométrica

**Ejercicio Resuelto**

Verifica que $f(x)=x^3-3x$ satisface las hipótesis del teorema de Rolle en $[-\sqrt{3},\sqrt{3}]$ y halla el punto $c$ garantizado.

**Verificación de hipótesis:**

1. **Continuidad en $[-\sqrt{3},\sqrt{3}]$:** $f$ es polinómica → continua en $\mathbb{R}$.

2. **Derivabilidad en $(-\sqrt{3},\sqrt{3})$:** $f$ polinómica → derivable en $\mathbb{R}$.

3. **Igual valor en los extremos:**
$$f(-\sqrt{3})=(-\sqrt{3})^3-3(-\sqrt{3})=-3\sqrt{3}+3\sqrt{3}=0$$
$$f(\sqrt{3})=(\sqrt{3})^3-3\sqrt{3}=3\sqrt{3}-3\sqrt{3}=0$$
$f(-\sqrt{3})=f(\sqrt{3})=0$ ✓

**Conclusión del teorema de Rolle:** Existe $c\in(-\sqrt{3},\sqrt{3})$ tal que $f'(c)=0$.

**Hallar $c$:**

$$f'(x)=3x^2-3=0 \Rightarrow x^2=1 \Rightarrow x=\pm1$$

Ambos $\pm1\in(-\sqrt{3},\sqrt{3})$ ✓. Los valores son $c=-1$ y $c=1$.

**Interpretación geométrica:** En los puntos $(-1, 2)$ y $(1, -2)$, la tangente a la curva es horizontal (paralela a la cuerda que une los extremos, que también es horizontal).

**Ejercicios con Solución**

**Nivel Básico:**

1. ¿Se puede aplicar el teorema de Rolle a $f(x)=x^2-4$ en $[-2,2]$? Si sí, halla $c$.

   > **Solución:** $f(-2)=0=f(2)$, $f$ continua y derivable. Sí. $f'(x)=2x=0 \Rightarrow c=0\in(-2,2)$ ✓.

2. ¿Puede aplicarse Rolle a $g(x)=|x|$ en $[-1,1]$?

   > **Solución:** $g(-1)=1=g(1)$, $g$ continua en $[-1,1]$. Pero $g$ **no es derivable** en $x=0\in(-1,1)$. Las hipótesis de Rolle **no se cumplen**; no se puede aplicar directamente.

**Nivel Intermedio:**

3. Comprueba que $f(x)=\sin x$ satisface Rolle en $[0,\pi]$ y halla $c$.

   > **Solución:** $f(0)=0=f(\pi)$, $\sin$ continua y derivable. $f'(x)=\cos x=0 \Rightarrow x=\pi/2\in(0,\pi)$. $c=\pi/2$.

4. Prueba que $f(x)=e^x\sin x$ tiene al menos un cero de $f'$ en $(0,\pi)$.

   > **Solución:** $f(0)=0$ y $f(\pi)=e^\pi\sin\pi=0$. $f$ continua y derivable. Por Rolle, $\exists c\in(0,\pi)$: $f'(c)=0$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=x^3-x^2-x+1$.

   a) Factoriza $f(x)$ o halla sus raíces.  
   b) Verifica que se cumplen las hipótesis de Rolle entre dos raíces consecutivas.  
   c) Halla los valores de $c$ garantizados por Rolle entre cada par de raíces.

   > **Solución:**
   >
   > **a)** $f(1)=1-1-1+1=0$, $f(-1)=-1-1+1+1=0$. Raíces: $x=1$ y $x=-1$.  
   > $f(x)=(x-1)(x+1)(x-1)=(x-1)^2(x+1)$. Raíces: $x=-1$ (simple) y $x=1$ (doble).
   >
   > **b)** En $[-1,1]$: $f(-1)=0=f(1)$, $f$ continua y derivable (polinomio). Hipótesis de Rolle cumplidas ✓.
   >
   > **c)** $f'(x)=3x^2-2x-1=(3x+1)(x-1)=0 \Rightarrow x=-\dfrac{1}{3}$ o $x=1$.  
   > $c=-\dfrac{1}{3}\in(-1,1)$ ✓ (el otro valor $x=1$ es el extremo, no el interior).

**Test de Opción Múltiple**

6. El teorema de Rolle garantiza la existencia de $c\in(a,b)$ con $f'(c)=0$ si:
   - a) $f(a)=f(b)$, $f$ continua en $[a,b]$ y derivable en $(a,b)$
   - b) $f(a)\neq f(b)$ y $f$ es derivable
   - c) $f'(a)=f'(b)=0$
   - d) $f$ es creciente en $(a,b)$

   > **Respuesta correcta:** a) Estas son exactamente las tres hipótesis del teorema de Rolle.

7. Si $f$ satisface las hipótesis de Rolle en $[a,b]$, entonces existe al menos un $c\in(a,b)$ con:
   - a) $f(c)=0$
   - b) $f(c)=\dfrac{f(a)+f(b)}{2}$
   - c) $f'(c)=0$
   - d) $f''(c)=0$

   > **Respuesta correcta:** c) La conclusión de Rolle es la existencia de un punto con derivada nula, no la nulidad de la función.

---

#### 7.6.2 Teorema del valor medio de Lagrange: enunciado y aplicaciones

**Ejercicio Resuelto**

Aplica el teorema del valor medio (Lagrange) a $f(x)=x^3$ en $[0,2]$: verifica las hipótesis y halla $c$.

**Hipótesis:**

1. $f$ continua en $[0,2]$ ✓ (polinomio)
2. $f$ derivable en $(0,2)$ ✓

**Conclusión de Lagrange:** $\exists c\in(0,2)$ tal que:

$$f'(c) = \frac{f(2)-f(0)}{2-0} = \frac{8-0}{2} = 4$$

**Hallar $c$:**

$$f'(x)=3x^2=4 \Rightarrow x^2=\frac{4}{3} \Rightarrow x=\frac{2}{\sqrt{3}}=\frac{2\sqrt{3}}{3}\approx1{,}15$$

Como $\dfrac{2\sqrt{3}}{3}\approx1{,}15\in(0,2)$ ✓.

**Interpretación:** En $c=\dfrac{2\sqrt{3}}{3}$, la pendiente de la tangente a $x^3$ es igual a la pendiente de la cuerda que une $(0,0)$ y $(2,8)$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Aplica Lagrange a $f(x)=x^2+1$ en $[1,3]$ y halla $c$.

   > **Solución:** $\dfrac{f(3)-f(1)}{3-1}=\dfrac{10-2}{2}=4=f'(c)=2c$. Luego $c=2\in(1,3)$ ✓.

2. ¿Se puede aplicar Lagrange a $f(x)=|x|$ en $[-1,1]$?

   > **Solución:** $f$ es continua en $[-1,1]$ pero no derivable en $x=0\in(-1,1)$. Las hipótesis de Lagrange **no se cumplen** (falta derivabilidad en $(-1,1)$).

**Nivel Intermedio:**

3. Aplica Lagrange a $f(x)=\ln x$ en $[1,e]$ y halla $c$.

   > **Solución:** $\dfrac{f(e)-f(1)}{e-1}=\dfrac{1-0}{e-1}=\dfrac{1}{e-1}=f'(c)=\dfrac{1}{c}$. Luego $c=e-1\approx1{,}72\in(1,e)$ ✓.

4. Usa el teorema de Lagrange para demostrar que $|\sin a - \sin b|\leq|a-b|$ para todo $a,b\in\mathbb{R}$.

   > **Solución:** Aplicando Lagrange a $f(x)=\sin x$ en $[a,b]$ (o $[b,a]$):  
   > $\exists c$ entre $a$ y $b$ tal que $\sin a-\sin b=\cos c\cdot(a-b)$.  
   > $|\sin a-\sin b|=|\cos c|\cdot|a-b|\leq1\cdot|a-b|=|a-b|$. $\blacksquare$

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=e^x$.

   a) Enuncia el teorema del valor medio de Lagrange.  
   b) Aplícalo a $f$ en el intervalo $[0,1]$ y halla $c$.  
   c) Interpreta geométricamente el resultado.

   > **Solución:**
   >
   > **a)** Si $f$ es continua en $[a,b]$ y derivable en $(a,b)$, entonces existe $c\in(a,b)$ tal que $f'(c)=\dfrac{f(b)-f(a)}{b-a}$.
   >
   > **b)** $\dfrac{f(1)-f(0)}{1-0}=e-1=f'(c)=e^c$. Luego $e^c=e-1 \Rightarrow c=\ln(e-1)\approx\ln(1{,}718)\approx0{,}541\in(0,1)$ ✓.
   >
   > **c)** En $c=\ln(e-1)$, la recta tangente a $e^x$ es paralela a la cuerda que une $(0,1)$ y $(1,e)$.

**Test de Opción Múltiple**

6. El teorema de Lagrange (valor medio) garantiza la existencia de $c\in(a,b)$ tal que $f'(c)$ es igual a:
   - a) $\dfrac{f(a)+f(b)}{2}$
   - b) $\dfrac{f(b)-f(a)}{b-a}$
   - c) $\dfrac{f'(a)+f'(b)}{2}$
   - d) $f(b)-f(a)$

   > **Respuesta correcta:** b) La pendiente de la cuerda es $\dfrac{f(b)-f(a)}{b-a}$, que iguala a la pendiente de alguna tangente interior.

7. El teorema de Rolle es un caso particular de Lagrange cuando:
   - a) $f(a)=f(b)=0$
   - b) $f(a)=f(b)$
   - c) $f'(a)=f'(b)$
   - d) $a=-b$

   > **Respuesta correcta:** b) Si $f(a)=f(b)$, la cuerda es horizontal (pendiente $0$), y Lagrange garantiza $f'(c)=0$, que es exactamente Rolle.

---

#### 7.6.3 Consecuencias: funciones con derivada nula, funciones con la misma derivada

**Ejercicio Resuelto**

Demuestra que si $f'(x)=0$ para todo $x\in(a,b)$, entonces $f$ es constante en $[a,b]$. Aplícalo a $f(x)=\sin^2x+\cos^2x$.

**Demostración:**

Sean $x_1, x_2\in[a,b]$ con $x_1<x_2$. Aplicando Lagrange a $f$ en $[x_1,x_2]$:

$$\exists c\in(x_1,x_2): \quad f(x_2)-f(x_1)=f'(c)(x_2-x_1)=0\cdot(x_2-x_1)=0$$

Por tanto $f(x_2)=f(x_1)$ para todo par de puntos → $f$ es constante. $\blacksquare$

**Aplicación:** $f(x)=\sin^2x+\cos^2x$. $f'(x)=2\sin x\cos x+2\cos x(-\sin x)=0$ para todo $x$. Por el teorema, $f$ es constante en $\mathbb{R}$, y como $f(0)=0+1=1$, se tiene $\sin^2x+\cos^2x=1$ para todo $x$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Si $f'(x)=g'(x)$ para todo $x\in\mathbb{R}$, ¿qué relación existe entre $f$ y $g$?

   > **Solución:** $(f-g)'(x)=f'(x)-g'(x)=0$. Por el teorema, $f(x)-g(x)=C$ (constante), es decir $f(x)=g(x)+C$.

2. Halla todas las funciones cuya derivada es $f'(x)=3x^2$.

   > **Solución:** Cualquier primitiva de $3x^2$ es $x^3+C$ ($C\in\mathbb{R}$). Por el teorema de la derivada nula aplicado a la diferencia, todas las soluciones difieren en una constante.

**Nivel Intermedio:**

3. Demuestra que $f(x)=\arcsin x+\arccos x$ es constante usando la derivada.

   > **Solución:** $f'(x)=\dfrac{1}{\sqrt{1-x^2}}+\left(-\dfrac{1}{\sqrt{1-x^2}}\right)=0$ para $x\in(-1,1)$.  
   > Por el teorema, $f$ es constante. $f(0)=0+\pi/2=\pi/2$. Luego $\arcsin x+\arccos x=\dfrac{\pi}{2}$.

4. ¿Existe una función $f$ tal que $f'(x)=f(x)$ para todo $x$ con $f(0)=1$? Justifica tu respuesta.

   > **Solución:** Sí: $f(x)=e^x$. Si hubiera otra solución $g$ con $g'=g$ y $g(0)=1$, entonces $(g/e^x)'=\dfrac{g'e^x-ge^x}{e^{2x}}=0$, luego $g/e^x=C=1$ y $g=e^x$. La solución es única.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** 

   a) Enuncia la consecuencia del teorema de Lagrange relativa a funciones con derivada cero.  
   b) Usa este resultado para demostrar que si $f'(x)>0$ en $(a,b)$, entonces $f$ es estrictamente creciente en $(a,b)$.  
   c) Aplica el apartado b) para verificar que $f(x)=e^x$ es creciente en $\mathbb{R}$.

   > **Solución:**
   >
   > **a)** Si $f'(x)=0$ para todo $x\in(a,b)$ y $f$ es continua en $[a,b]$, entonces $f$ es constante en $[a,b]$.
   >
   > **b)** Sean $x_1<x_2$ en $(a,b)$. Por Lagrange: $f(x_2)-f(x_1)=f'(c)(x_2-x_1)$ con $c\in(x_1,x_2)$.  
   > Como $f'(c)>0$ y $x_2-x_1>0$: $f(x_2)-f(x_1)>0$, es decir $f(x_2)>f(x_1)$ → $f$ es estrictamente creciente.
   >
   > **c)** $(e^x)'=e^x>0$ para todo $x\in\mathbb{R}$. Por el apartado b), $e^x$ es estrictamente creciente en $\mathbb{R}$.

**Test de Opción Múltiple**

6. Si $f'(x)=g'(x)$ para todo $x$ real, entonces:
   - a) $f(x)=g(x)$ para todo $x$
   - b) $f(x)=g(x)+C$ para alguna constante $C$
   - c) $f$ y $g$ son iguales si $f(0)=0$
   - d) $f(x)=g(x)\cdot C$ para alguna constante $C$

   > **Respuesta correcta:** b) Si dos funciones tienen la misma derivada en un intervalo, difieren en una constante aditiva.

7. La demostración de que $f'=0$ implica constancia usa:
   - a) El teorema de Bolzano
   - b) El teorema del valor medio de Lagrange
   - c) La definición de límite
   - d) La regla de L'Hôpital

   > **Respuesta correcta:** b) Se aplica Lagrange para mostrar que $f(x_2)-f(x_1)=f'(c)\cdot(x_2-x_1)=0$.

---

#### 7.7.1 Extremos relativos: condición necesaria y criterio de la segunda derivada

**Ejercicio Resuelto**

Halla los extremos relativos de $f(x)=x^4-4x^3+4x^2$ mediante la condición necesaria y el criterio de la segunda derivada.

**Paso 1 — Derivada primera:**

$$f'(x) = 4x^3-12x^2+8x = 4x(x^2-3x+2) = 4x(x-1)(x-2)$$

**Paso 2 — Puntos críticos** ($f'=0$): $x=0$, $x=1$, $x=2$.

**Paso 3 — Segunda derivada:**

$$f''(x) = 12x^2-24x+8$$

**Paso 4 — Criterio de la segunda derivada:**

| $x$ | $f'(x)=0$ | $f''(x)$ | Tipo |
|-----|-----------|-----------|------|
| $0$ | ✓ | $f''(0)=8>0$ | Mínimo relativo |
| $1$ | ✓ | $f''(1)=12-24+8=-4<0$ | Máximo relativo |
| $2$ | ✓ | $f''(2)=48-48+8=8>0$ | Mínimo relativo |

**Valores:** $f(0)=0$, $f(1)=1-4+4=1$, $f(2)=16-32+16=0$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla los extremos de $f(x)=x^2-6x+5$.

   > **Solución:** $f'(x)=2x-6=0 \Rightarrow x=3$. $f''(3)=2>0$ → mínimo relativo en $(3,-4)$.

2. Halla los extremos de $g(x)=-x^3+3x$.

   > **Solución:** $g'(x)=-3x^2+3=0 \Rightarrow x=\pm1$. $g''(x)=-6x$.  
   > $g''(1)=-6<0$ → máximo en $(1,2)$. $g''(-1)=6>0$ → mínimo en $(-1,-2)$.

**Nivel Intermedio:**

3. Halla los extremos de $h(x)=xe^{-x}$.

   > **Solución:** $h'(x)=e^{-x}-xe^{-x}=e^{-x}(1-x)=0 \Rightarrow x=1$ (ya que $e^{-x}>0$).  
   > $h''(x)=-e^{-x}(1-x)+e^{-x}(-1)=e^{-x}(x-2)$.  
   > $h''(1)=e^{-1}(-1)<0$ → máximo relativo en $(1,e^{-1})$.

4. Halla los extremos de $f(x)=\ln x - x$ para $x>0$.

   > **Solución:** $f'(x)=\dfrac{1}{x}-1=0 \Rightarrow x=1$.  
   > $f''(x)=-\dfrac{1}{x^2}$; $f''(1)=-1<0$ → máximo relativo en $(1,-1)$... Espera: $f(1)=\ln1-1=-1$. Máximo en $(1,-1)$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=\dfrac{x^2}{e^x}$.

   a) Halla $f'(x)$ y los puntos críticos.  
   b) Clasifica los extremos usando el criterio de la segunda derivada.  
   c) Determina el valor máximo/mínimo.

   > **Solución:**
   >
   > **a)** $f'(x)=\dfrac{2x\cdot e^x-x^2\cdot e^x}{e^{2x}}=\dfrac{e^x\cdot x(2-x)}{e^{2x}}=\dfrac{x(2-x)}{e^x}$.  
   > $f'(x)=0 \Leftrightarrow x=0$ o $x=2$.
   >
   > **b)** $f''(x)=\dfrac{(2-2x)e^x-x(2-x)e^x}{e^{2x}}=\dfrac{(2-2x-2x+x^2)}{e^x}=\dfrac{x^2-4x+2}{e^x}$.  
   > $f''(0)=\dfrac{2}{1}=2>0$ → mínimo relativo en $x=0$.  
   > $f''(2)=\dfrac{4-8+2}{e^2}=\dfrac{-2}{e^2}<0$ → máximo relativo en $x=2$.
   >
   > **c)** $f(0)=0$ (mínimo relativo); $f(2)=\dfrac{4}{e^2}$ (máximo relativo).

**Test de Opción Múltiple**

6. La condición $f'(a)=0$ en un punto interior del dominio es:
   - a) Suficiente para que $a$ sea un extremo relativo
   - b) Necesaria pero no suficiente para que $a$ sea un extremo relativo
   - c) Necesaria y suficiente para un extremo relativo
   - d) Innecesaria para estudiar extremos

   > **Respuesta correcta:** b) $f'(a)=0$ es condición necesaria; puede ocurrir en puntos de inflexión (ej. $f(x)=x^3$ en $x=0$).

7. Si $f'(a)=0$ y $f''(a)>0$, entonces $f$ tiene en $x=a$:
   - a) Un máximo relativo
   - b) Un mínimo relativo
   - c) Un punto de inflexión
   - d) Una asíntota

   > **Respuesta correcta:** b) Por el criterio de la segunda derivada, $f''(a)>0$ indica mínimo relativo.

---

#### 7.7.2 Extremos en el extremo del dominio y en puntos de no derivabilidad

**Ejercicio Resuelto**

Halla los extremos absolutos de $f(x)=|x^2-4|$ en $[-3,3]$.

**Paso 1 — Puntos críticos interiores:**

$f(x)=|x^2-4|=\begin{cases}x^2-4 & |x|\geq2\\4-x^2 & |x|<2\end{cases}$

En el interior del dominio: puntos de no derivabilidad en $x=\pm2$ (quiebro) y punto crítico de cada tramo:

- Para $|x|>2$: $f'(x)=2x=0\Rightarrow x=0$ (fuera del dominio de este tramo).
- Para $|x|<2$: $f'(x)=-2x=0\Rightarrow x=0$. En $x=0$: $f(0)=4$.
- En $x=\pm2$: $f(\pm2)=0$.

**Paso 2 — Extremos en los bordes del dominio:** $f(-3)=|9-4|=5$; $f(3)=5$.

**Paso 3 — Tabla de candidatos:**

| $x$ | $f(x)$ |
|-----|--------|
| $-3$ | $5$ |
| $-2$ | $0$ |
| $0$ | $4$ |
| $2$ | $0$ |
| $3$ | $5$ |

**Extremos absolutos:** Máximo absoluto $5$ en $x=\pm3$; mínimos absolutos $0$ en $x=\pm2$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla los extremos absolutos de $f(x)=x^2-2x$ en $[0,3]$.

   > **Solución:** $f'(x)=2x-2=0 \Rightarrow x=1$. $f(0)=0$; $f(1)=-1$; $f(3)=3$. Mínimo absoluto: $-1$ en $x=1$; máximo absoluto: $3$ en $x=3$.

2. Halla los extremos absolutos de $g(x)=\sin x$ en $[0, 2\pi]$.

   > **Solución:** $g'=\cos x=0 \Rightarrow x=\pi/2, 3\pi/2$. $g(0)=0$; $g(\pi/2)=1$; $g(3\pi/2)=-1$; $g(2\pi)=0$.  
   > Máximo absoluto: $1$ en $x=\pi/2$; mínimo absoluto: $-1$ en $x=3\pi/2$.

**Nivel Intermedio:**

3. Halla los extremos absolutos de $h(x)=x^3-3x$ en $[-2,2]$.

   > **Solución:** $h'=3x^2-3=0 \Rightarrow x=\pm1$. $h(-2)=-2$; $h(-1)=2$; $h(1)=-2$; $h(2)=2$.  
   > Máximos absolutos: $2$ en $x=-1$ y $x=2$; mínimos absolutos: $-2$ en $x=2$ y $x=-2$... Con precisión: máximo: $2$ (en $x=-1$ y $x=2$); mínimo: $-2$ (en $x=1$ y $x=-2$).

4. Determina si $f(x)=x^{2/3}$ tiene extremo en $x=0$ aunque no sea derivable.

   > **Solución:** $f'(x)=\dfrac{2}{3}x^{-1/3}$ no existe en $x=0$. Pero para $x<0$: $f'<0$; para $x>0$: $f'>0$. Hay cambio de signo de $-$ a $+$ → mínimo en $x=0$, $f(0)=0$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Sea $f(x)=2x^3-3x^2-12x+1$ en $[-2,3]$.

   a) Halla los puntos críticos interiores.  
   b) Evalúa $f$ en los puntos críticos y en los extremos del intervalo.  
   c) Indica los extremos absolutos de $f$ en $[-2,3]$.

   > **Solución:**
   >
   > **a)** $f'(x)=6x^2-6x-12=6(x^2-x-2)=6(x-2)(x+1)=0 \Rightarrow x=-1$ y $x=2$.
   >
   > **b)** $f(-2)=2(-8)-3(4)-12(-2)+1=-16-12+24+1=-3$.  
   > $f(-1)=2(-1)-3(1)-12(-1)+1=-2-3+12+1=8$.  
   > $f(2)=2(8)-3(4)-12(2)+1=16-12-24+1=-19$.  
   > $f(3)=2(27)-3(9)-12(3)+1=54-27-36+1=-8$.
   >
   > **c)** Máximo absoluto: $8$ en $x=-1$. Mínimo absoluto: $-19$ en $x=2$.

**Test de Opción Múltiple**

6. Para hallar el extremo absoluto de una función continua en $[a,b]$, se evalúa $f$ en:
   - a) Solo los puntos donde $f'=0$
   - b) Los extremos del intervalo y los puntos críticos interiores (donde $f'=0$ o no existe)
   - c) El punto medio del intervalo
   - d) Solo los extremos del intervalo

   > **Respuesta correcta:** b) Los candidatos a extremo absoluto son los puntos interiores críticos y los extremos del intervalo.

7. Si $f$ no es derivable en $x=c\in(a,b)$ pero es continua, el punto $c$:
   - a) No puede ser extremo relativo
   - b) Puede ser extremo relativo
   - c) Es necesariamente un extremo absoluto
   - d) Es un punto de inflexión

   > **Respuesta correcta:** b) Los puntos de no derivabilidad son candidatos a extremo. Ejemplo: $|x|$ en $x=0$ tiene mínimo aunque no sea derivable.

---

#### 7.7.3 Planteamiento y resolución de problemas de optimización en contextos reales

**Ejercicio Resuelto**

Una granja rectangular va a cercarse usando $120$ m de valla. Un lado linda con un río y no necesita valla. ¿Qué dimensiones maximizan el área?

**Variables:** Sea $x$ el lado perpendicular al río (dos lados) e $y$ el lado paralelo al río (un lado).

**Restricción:** $2x+y=120 \Rightarrow y=120-2x$.

**Función objetivo (área):**

$$A(x) = x\cdot y = x(120-2x) = 120x-2x^2, \quad x\in(0,60)$$

**Optimizar:**

$$A'(x) = 120-4x = 0 \Rightarrow x=30$$

$$A''(x)=-4<0 \quad \Rightarrow \quad x=30 \text{ es un máximo.}$$

**Dimensiones óptimas:** $x=30$ m, $y=120-60=60$ m. **Área máxima:** $A=30\times60=1800$ m².

**Ejercicios con Solución**

**Nivel Básico:**

1. La suma de dos números positivos es $20$. ¿Cuál es el máximo de su producto?

   > **Solución:** Sea $x$ e $y=20-x$. $P=x(20-x)=20x-x^2$.  
   > $P'=20-2x=0 \Rightarrow x=10$. $P(10)=100$. Máximo producto: $100$ (cuando $x=y=10$).

2. Se quiere construir una caja cúbica de volumen $8$ m³. Minimiza la superficie total.

   > **Solución:** Cubo de lado $a$: $V=a^3=8 \Rightarrow a=2$. Superficie $=6a^2=24$ m². (Para un cubo fijo, la superficie es $6a^2$, que decrece al decrecer $a$; la restricción fija $a=2$, un único valor.)

**Nivel Intermedio:**

3. Encuentra el rectángulo de perímetro $P=40$ cm con área máxima.

   > **Solución:** $2(x+y)=40$, $y=20-x$. $A=x(20-x)=20x-x^2$. $A'=20-2x=0\Rightarrow x=10$. Cuadrado de lado $10$, área $100$ cm².

4. Un cable de longitud $L$ se corta en dos trozos; con uno se forma un cuadrado y con el otro un círculo. ¿Cómo se corta para minimizar la suma de áreas?

   > **Solución:** Sea $x$ el lado del cuadrado: $4x+2\pi r=L$, $r=\dfrac{L-4x}{2\pi}$.  
   > $A=x^2+\pi r^2=x^2+\dfrac{(L-4x)^2}{4\pi}$.  
   > $A'=2x-\dfrac{8(L-4x)}{4\pi}=2x-\dfrac{2(L-4x)}{\pi}=0$.  
   > $\pi x=(L-4x) \Rightarrow x(\pi+4)=L \Rightarrow x=\dfrac{L}{\pi+4}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Una lata cilíndrica de refresco tiene volumen $330$ cm³. Halla las dimensiones del cilindro (radio $r$ y altura $h$) que minimizan la cantidad de material (superficie total).

   **Nota:** $V=\pi r^2 h=330$; $S=2\pi r^2+2\pi rh$.

   > **Solución:**
   >
   > De la restricción: $h=\dfrac{330}{\pi r^2}$.
   >
   > $S(r)=2\pi r^2+2\pi r\cdot\dfrac{330}{\pi r^2}=2\pi r^2+\dfrac{660}{r}$.
   >
   > $S'(r)=4\pi r-\dfrac{660}{r^2}=0 \Rightarrow 4\pi r^3=660 \Rightarrow r^3=\dfrac{165}{\pi} \Rightarrow r=\sqrt[3]{\dfrac{165}{\pi}}\approx3{,}74$ cm.
   >
   > $h=\dfrac{330}{\pi r^2}\approx\dfrac{330}{\pi\cdot13{,}98}\approx7{,}51$ cm.
   >
   > Verificación: $h\approx2r$ (altura igual al diámetro, resultado clásico de la lata óptima). $S''=4\pi+\dfrac{1320}{r^3}>0$ → mínimo ✓.

**Test de Opción Múltiple**

6. En un problema de optimización, la "función objetivo" es:
   - a) La restricción del problema
   - b) La función que se quiere maximizar o minimizar
   - c) La derivada del área
   - d) El límite de la función en los extremos

   > **Respuesta correcta:** b) La función objetivo es la que se desea optimizar; la restricción establece la condición que une las variables.

7. En el problema de la caja sin tapa de volumen fijo $V=1$, la superficie mínima se obtiene cuando:
   - a) La caja es un cubo
   - b) La base es un cuadrado y $h=\dfrac{a}{2}$ (mitad del lado)
   - c) La caja es más alta que ancha
   - d) La relación $h/a=1$ (cubo)

   > **Respuesta correcta:** b) Para una caja sin tapa con base cuadrada, el mínimo de material se obtiene cuando $h=a/2$, es decir, la altura es la mitad del lado de la base.

---

#### 7.7.4 Optimización geométrica: distancias mínimas, áreas y volúmenes extremos

**Ejercicio Resuelto**

Halla el punto de la parábola $y=x^2$ más cercano al punto $A=(0,1)$.

**Distancia al cuadrado** (más cómodo que la distancia directa):

$$D(x)=x^2+(x^2-1)^2=x^2+x^4-2x^2+1=x^4-x^2+1$$

**Minimizar $D$:**

$$D'(x)=4x^3-2x=2x(2x^2-1)=0 \Rightarrow x=0 \quad \text{o} \quad x^2=\frac{1}{2} \Rightarrow x=\pm\frac{1}{\sqrt{2}}$$

**Análisis:** $D''(x)=12x^2-2$.

- $D''(0)=-2<0$ → máximo en $x=0$.
- $D''\!\left(\pm\dfrac{1}{\sqrt{2}}\right)=6-2=4>0$ → mínimos en $x=\pm\dfrac{1}{\sqrt{2}}$.

**Puntos más cercanos:** $\left(\pm\dfrac{1}{\sqrt{2}},\dfrac{1}{2}\right)$. Distancia mínima: $D=\dfrac{1}{4}-\dfrac{1}{2}+1=\dfrac{3}{4}$, luego $d=\dfrac{\sqrt{3}}{2}$.

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla el punto de la recta $y=2x+1$ más cercano al origen.

   > **Solución:** Distancia²: $D(x)=x^2+(2x+1)^2=5x^2+4x+1$. $D'=10x+4=0\Rightarrow x=-\frac{2}{5}$.  
   > Punto: $\left(-\frac{2}{5},\frac{1}{5}\right)$. Distancia: $\dfrac{|0-0+1|}{\sqrt{5}}=\dfrac{1}{\sqrt{5}}=\dfrac{\sqrt{5}}{5}$.

2. Halla el área máxima de un triángulo rectángulo con hipotenusa $10$.

   > **Solución:** Catetos $a$ y $b$ con $a^2+b^2=100$. $A=\dfrac{ab}{2}$. Por AM-GM: $ab\leq\dfrac{a^2+b^2}{2}=50$, con igualdad cuando $a=b=5\sqrt{2}$. Área máxima: $\dfrac{50}{2}=25$.

**Nivel Intermedio:**

3. Inscribe el rectángulo de área máxima en un semicírculo de radio $R$.

   > **Solución:** Vértices en $(x,0)$, $(-x,0)$, $(-x,y)$, $(x,y)$ con $x^2+y^2=R^2$.  
   > $A=2x\cdot y=2x\sqrt{R^2-x^2}$. $A^2=4x^2(R^2-x^2)$.  
   > $(A^2)'=4(2xR^2-4x^3)=0\Rightarrow x^2=R^2/2\Rightarrow x=\dfrac{R}{\sqrt{2}}$, $y=\dfrac{R}{\sqrt{2}}$. Área: $R^2$.

4. Halla el cilindro de volumen máximo inscrito en una esfera de radio $R$.

   > **Solución:** Cilindro con radio $r$ y semialtua $h$: $r^2+h^2=R^2$.  
   > $V=\pi r^2(2h)=2\pi(R^2-h^2)h$. $V'=2\pi(R^2-3h^2)=0\Rightarrow h=\dfrac{R}{\sqrt{3}}$.  
   > $r^2=R^2-\dfrac{R^2}{3}=\dfrac{2R^2}{3}$. $V_{max}=\dfrac{4\pi R^3}{3\sqrt{3}}$.

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Se quiere construir una ventana con forma de rectángulo coronado por un semicírculo. El perímetro total es $P=6$ m. Halla las dimensiones que maximizan el área de la ventana.

   > **Solución:**
   >
   > Sea $2r$ la anchura (diámetro del semicírculo = ancho del rectángulo) y $h$ la altura del rectángulo.
   >
   > **Perímetro:** $2h+2r+\pi r=6 \Rightarrow h=\dfrac{6-2r-\pi r}{2}=3-r-\dfrac{\pi r}{2}$.
   >
   > **Área:** $A=2rh+\dfrac{\pi r^2}{2}=2r\left(3-r-\dfrac{\pi r}{2}\right)+\dfrac{\pi r^2}{2}=6r-2r^2-\pi r^2+\dfrac{\pi r^2}{2}=6r-2r^2-\dfrac{\pi r^2}{2}$.
   >
   > $A'=6-4r-\pi r=6-r(4+\pi)=0 \Rightarrow r=\dfrac{6}{4+\pi}\approx0{,}84$ m.
   >
   > $h=3-r-\dfrac{\pi r}{2}=3-r\left(1+\dfrac{\pi}{2}\right)=3-\dfrac{6}{4+\pi}\cdot\dfrac{4+\pi}{2}=3-3=0$... Re-verificando:  
   > $h=3-\dfrac{6}{4+\pi}-\dfrac{\pi}{2}\cdot\dfrac{6}{4+\pi}=3-\dfrac{6(1+\pi/2)}{4+\pi}=3-\dfrac{6(2+\pi)}{2(4+\pi)}=3-\dfrac{3(2+\pi)}{4+\pi}=\dfrac{3(4+\pi)-3(2+\pi)}{4+\pi}=\dfrac{6}{4+\pi}=r$.
   >
   > Por tanto $h=r=\dfrac{6}{4+\pi}\approx0{,}84$ m. La anchura es $2r\approx1{,}68$ m.

**Test de Opción Múltiple**

6. Para minimizar la distancia de un punto $P$ a una curva, es conveniente minimizar:
   - a) La distancia directamente
   - b) El cuadrado de la distancia (para evitar la raíz cuadrada)
   - c) La tangente a la curva
   - d) La función inversa de la curva

   > **Respuesta correcta:** b) Minimizar $d^2$ es equivalente a minimizar $d$ (ya que $d\geq0$), pero algebraicamente más sencillo al eliminar la raíz.

7. El rectángulo de área máxima inscrito en una circunferencia es:
   - a) Cualquier rectángulo
   - b) El cuadrado
   - c) El rectángulo de lados $1:2$
   - d) El triángulo equilátero

   > **Respuesta correcta:** b) Por simetría y cálculo de optimización, el rectángulo de área máxima inscrito en un círculo es el cuadrado.

---

#### 7.7.5 Optimización en problemas de movimiento y física (velocidad, aceleración)

**Ejercicio Resuelto**

La posición de un proyectil en función del tiempo es $s(t)=-5t^2+20t+1$ (m), para $t\geq0$.

a) Halla la velocidad máxima. ¿Cuándo se alcanza?
b) Halla la altura máxima.
c) ¿Cuándo vuelve al suelo?

**a) Velocidad:**

$$v(t)=s'(t)=-10t+20$$

La velocidad es máxima al inicio ($t=0$): $v(0)=20$ m/s. La velocidad decrece linealmente (aceleración constante $a=-10$ m/s²). Si la pregunta es cuándo la velocidad es cero (punto más alto):

$$v(t)=0 \Rightarrow -10t+20=0 \Rightarrow t=2 \text{ s}$$

**b) Altura máxima** (en $t=2$):

$$s(2)=-5(4)+20(2)+1=-20+40+1=21 \text{ m}$$

**c) Vuelta al suelo** ($s=0$):

$$-5t^2+20t+1=0 \Rightarrow t=\frac{-20\pm\sqrt{400+20}}{-10}=\frac{-20\pm\sqrt{420}}{-10}$$

$t=\dfrac{20\pm\sqrt{420}}{10}=2\pm\dfrac{\sqrt{420}}{10}$. Como $t>0$: $t=2+\dfrac{\sqrt{420}}{10}\approx2+2{,}05=4{,}05$ s.

**Ejercicios con Solución**

**Nivel Básico:**

1. La posición de un coche es $s(t)=3t^2-12t+5$. ¿En qué instante la velocidad es cero? ¿Es ese un mínimo o máximo de posición?

   > **Solución:** $v(t)=6t-12=0 \Rightarrow t=2$ s. $s''(t)=6>0$ → mínimo de posición en $t=2$.  
   > $s(2)=12-24+5=-7$ m.

2. Una pelota sube con $v(t)=10-2t$ m/s. 2. Una pelota sube con $v(t)=10-2t$ m/s. ¿En qué instante la velocidad es cero? ¿Cuál es la altura máxima si $s(0)=0$?

   > **Solución:** $v(t)=0 \Rightarrow t=5$ s.  
   > $s(t)=\int v\,dt=10t-t^2+C$; $s(0)=0 \Rightarrow C=0$.  
   > Altura máxima: $s(5)=50-25=25$ m.

**Nivel Intermedio:**

3. La temperatura de un objeto que se enfría sigue $T(t)=70e^{-0{,}1t}+20$ (°C), para $t\geq0$. Halla la velocidad de enfriamiento máxima (en valor absoluto) y el instante en que se alcanza.

   > **Solución:** $T'(t)=-7e^{-0{,}1t}$.  
   > $|T'(t)|=7e^{-0{,}1t}$ es estrictamente decreciente. El valor máximo es en $t=0$: $|T'(0)|=7$ °C/s.  
   > El enfriamiento es más rápido al inicio.

4. La altura de un cohete es $h(t)=-t^3+9t^2$ para $0\leq t\leq9$. Halla la velocidad y aceleración máximas positivas.

   > **Solución:** $v(t)=h'(t)=-3t^2+18t$; $a(t)=v'(t)=-6t+18$.  
   > **Velocidad máxima:** $v'(t)=0 \Rightarrow t=3$. $v(3)=-27+54=27$ m/s.  
   > **Aceleración máxima positiva:** $a(t)>0$ para $t<3$. El máximo de $a$ en $[0,9]$ es en $t=0$: $a(0)=18$ m/s².

**Nivel EVAU:**

5. **(Estilo EVAU Madrid)** Una partícula se mueve en línea recta con posición $s(t) = 2t^3 - 9t^2 + 12t$ (metros), $t\geq0$ (segundos).

   a) Halla la velocidad $v(t)$ y la aceleración $a(t)$.  
   b) ¿Cuándo está la partícula en reposo?  
   c) ¿Cuándo la velocidad es máxima? ¿Cuál es ese valor?  
   d) ¿En qué intervalos la partícula avanza? ¿En cuáles retrocede?

   > **Solución:**
   >
   > **a)** $v(t)=s'(t)=6t^2-18t+12=6(t^2-3t+2)=6(t-1)(t-2)$.  
   > $a(t)=v'(t)=12t-18=6(2t-3)$.
   >
   > **b)** $v(t)=0 \Rightarrow t=1$ s y $t=2$ s.
   >
   > **c)** $v'(t)=a(t)=0 \Rightarrow 12t-18=0 \Rightarrow t=\dfrac{3}{2}$ s.  
   > $v''(t)=12>0$ → mínimo de $v$. Luego la velocidad tiene un **mínimo** en $t=3/2$ (no máximo en sentido estricto).  
   > Para $t\geq0$: $v(0)=12$ m/s, $v\to+\infty$ cuando $t\to+\infty$. No hay máximo global. El mínimo local es $v(3/2)=6\cdot(9/4-9/2+2)=6\cdot(-1/4)=-3/2$ m/s.
   >
   > **d)** $v(t)=6(t-1)(t-2)$:  
   > - $v>0$ para $t\in[0,1)$: **avanza**.  
   > - $v<0$ para $t\in(1,2)$: **retrocede**.  
   > - $v>0$ para $t\in(2,+\infty)$: **avanza**.

**Test de Opción Múltiple**

6. Una partícula tiene posición $s(t)=t^3-6t^2$. La aceleración es cero cuando:
   - a) $t=0$
   - b) $t=2$
   - c) $t=4$
   - d) $t=6$

   > **Respuesta correcta:** b) $s'(t)=3t^2-12t$; $s''(t)=6t-12=0 \Rightarrow t=2$.

7. Si la velocidad de un objeto es $v(t)=4t-8$, el objeto está en reposo en:
   - a) $t=0$
   - b) $t=1$
   - c) $t=2$
   - d) $t=4$

   > **Respuesta correcta:** c) $v(t)=0 \Rightarrow 4t-8=0 \Rightarrow t=2$ s.

---

## Resumen de Capítulos 6 y 7

Este archivo contiene ejercicios completos para:

**Capítulo 6 — Límites y Continuidad:**
- 6.1 Límite de una función en un punto (5 subsecciones)
- 6.2 Cálculo de límites e indeterminaciones (6 subsecciones)
- 6.3 Límites en el infinito y asíntotas (6 subsecciones)
- 6.4 Continuidad de funciones (5 subsecciones)
- 6.5 Teoremas de continuidad (3 subsecciones)

**Capítulo 7 — Derivadas y Aplicaciones:**
- 7.1 Concepto de derivada (5 subsecciones)
- 7.2 Reglas de derivación (6 subsecciones)
- 7.3 Derivabilidad (5 subsecciones)
- 7.4 Recta tangente y normal (3 subsecciones)
- 7.5 Regla de L'Hôpital (3 subsecciones)
- 7.6 Teoremas del cálculo diferencial (3 subsecciones)
- 7.7 Optimización (5 subsecciones)

**Total de ejercicios por subsección:** 1 Ejercicio Resuelto + 2 Básico + 2 Intermedio + 1 EVAU + 2 Test = 8 ítems.

*Matemáticas II — 2.º Bachillerato · Comunidad de Madrid · EVAU-estilo LOMLOE*
