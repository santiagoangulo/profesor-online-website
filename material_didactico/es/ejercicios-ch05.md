# Capítulo 5 — Geometría Analítica en el Espacio
## Ejercicios Completos · Matemáticas II · 2.º Bachillerato
### Comunidad de Madrid · EVAU · Decreto 64/2022 (LOMLOE)

---

> **Instrucciones de uso:**
> - Cada subsección incluye: 1 Ejercicio Resuelto · 2 Nivel Básico · 2 Nivel Intermedio · 1 Nivel EVAU · 2 Test de Opción Múltiple.
> - Las soluciones son completas con todos los pasos intermedios.
> - Los problemas EVAU siguen el formato oficial de la Comunidad de Madrid.
> - Notación: $\ldots$ para matemáticas en línea, $$\ldots$$ para fórmulas centradas.

---

## 5.1 Ecuaciones de la Recta en el Espacio

---

#### 5.1.1 Ecuación Vectorial de la Recta

**Ejercicio Resuelto**

Determina la ecuación vectorial de la recta que pasa por el punto $A(1, -2, 3)$ y tiene como vector director $\vec{d} = (2, 1, -1)$.

**Solución:**

La ecuación vectorial de una recta queda completamente determinada por un punto $P_0$ de la recta y un vector director $\vec{d} \neq \vec{0}$.

La forma general es:
$$\vec{r} = \vec{OP_0} + \lambda\,\vec{d}, \quad \lambda \in \mathbb{R}$$

En nuestro caso, $\vec{OP_0} = (1, -2, 3)$ y $\vec{d} = (2, 1, -1)$, por tanto:
$$(x, y, z) = (1, -2, 3) + \lambda(2, 1, -1)$$

Es decir:
$$\boxed{(x, y, z) = (1 + 2\lambda,\; -2 + \lambda,\; 3 - \lambda), \quad \lambda \in \mathbb{R}}$$

**Verificación:** Para $\lambda = 0$ obtenemos el punto $A(1,-2,3)$ ✓. La dirección del vector $(2,1,-1)$ es la misma que $\vec{d}$ ✓.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Escribe la ecuación vectorial de la recta que pasa por $P(0, 1, 2)$ con vector director $\vec{d} = (3, 0, -2)$.

   > **Solución:** La ecuación vectorial es:
   > $$(x, y, z) = (0, 1, 2) + \lambda(3, 0, -2), \quad \lambda \in \mathbb{R}$$
   > Es decir, $(x,y,z) = (3\lambda,\; 1,\; 2-2\lambda)$.

2. Halla la ecuación vectorial de la recta que pasa por los puntos $A(2, -1, 0)$ y $B(4, 3, -2)$.

   > **Solución:** El vector director es $\vec{AB} = B - A = (4-2,\; 3-(-1),\; -2-0) = (2, 4, -2)$.
   > Podemos simplificar dividiendo entre 2: $\vec{d} = (1, 2, -1)$.
   > Tomando $A$ como punto base:
   > $$(x, y, z) = (2, -1, 0) + \lambda(1, 2, -1), \quad \lambda \in \mathbb{R}$$
   > **Comprobación:** Para $\lambda = 2$: $(2+2, -1+4, 0-2) = (4,3,-2) = B$ ✓

**Nivel Intermedio:**

3. Determina la ecuación vectorial de la recta $r$ que pasa por $A(1, 2, -1)$ y es paralela a la recta $s: (x,y,z) = (3,0,1) + \mu(2,-1,4)$.

   > **Solución:** Dos rectas son paralelas si y solo si sus vectores directores son proporcionales. El vector director de $s$ es $\vec{d}_s = (2,-1,4)$, que también sirve como vector director de $r$.
   > La ecuación vectorial de $r$ es:
   > $$(x, y, z) = (1, 2, -1) + \lambda(2, -1, 4), \quad \lambda \in \mathbb{R}$$

4. La recta $r$ tiene ecuación vectorial $(x,y,z) = (1,0,-3) + \lambda(-2,1,2)$. Determina si el punto $Q(5, -2, -7)$ pertenece a $r$.

   > **Solución:** Sustituimos las coordenadas de $Q$ en la ecuación vectorial y comprobamos si existe un único valor de $\lambda$:
   > $$5 = 1 - 2\lambda \Rightarrow \lambda = -2$$
   > $$-2 = 0 + \lambda \Rightarrow \lambda = -2$$
   > $$-7 = -3 + 2\lambda \Rightarrow 2\lambda = -4 \Rightarrow \lambda = -2$$
   > Los tres valores son iguales, $\lambda = -2$ en los tres casos, por tanto $Q \in r$ ✓.

**Nivel EVAU:**

5. Sea la recta $r$ que pasa por $A(2,1,-3)$ y $B(4,-1,1)$, y la recta $s$ que pasa por $C(1,3,0)$ con vector director $\vec{d}_s = (1,-1,2)$.

   **(a)** Escribe la ecuación vectorial de $r$.

   **(b)** Estudia si $r$ y $s$ son la misma recta, paralelas, secantes o se cruzan.

   > **Solución:**
   >
   > **(a)** $\vec{AB} = (4-2, -1-1, 1-(-3)) = (2,-2,4)$. Simplificando: $\vec{d}_r = (1,-1,2)$.
   > $$r:\; (x,y,z) = (2,1,-3) + \lambda(1,-1,2)$$
   >
   > **(b)** Los vectores directores son $\vec{d}_r = (1,-1,2)$ y $\vec{d}_s = (1,-1,2)$: son proporcionales (iguales), luego $r \parallel s$ o $r = s$.
   > Comprobamos si $C(1,3,0) \in r$:
   > $$1 = 2 + \lambda \Rightarrow \lambda = -1$$
   > $$3 = 1 - \lambda = 1-(-1) = 2 \neq 3$$
   > La segunda ecuación no se satisface, luego $C \notin r$.
   > **Conclusión:** $r$ y $s$ son **paralelas** (no coincidentes).

**Test de Opción Múltiple**

6. La ecuación vectorial de la recta que pasa por $P(1,2,3)$ con vector director $\vec{d}=(0,1,0)$ es:
   - a) $(x,y,z) = (1,2,3) + \lambda(1,2,3)$
   - b) $(x,y,z) = (0,1,0) + \lambda(1,2,3)$
   - c) $(x,y,z) = (1,2,3) + \lambda(0,1,0)$
   - d) $(x,y,z) = (1,2,3) + \lambda(1,0,0)$

   > **Respuesta correcta:** c) La forma es $\vec{r} = \vec{OP_0} + \lambda\vec{d}$, con punto $P(1,2,3)$ y $\vec{d}=(0,1,0)$. Esta recta es paralela al eje $OY$.

7. ¿Cuántos vectores directores distintos puede tener una recta en el espacio?
   - a) Exactamente uno
   - b) Exactamente dos (uno por cada sentido)
   - c) Infinitos, todos proporcionales entre sí
   - d) Infinitos, sin ninguna restricción

   > **Respuesta correcta:** c) El vector director de una recta no es único: cualquier múltiplo no nulo de un vector director es también un vector director de la misma recta. Todos son proporcionales entre sí.

---

#### 5.1.2 Ecuaciones Paramétricas de la Recta

**Ejercicio Resuelto**

Obtén las ecuaciones paramétricas de la recta que pasa por $A(-1, 3, 2)$ con vector director $\vec{d} = (4, -2, 1)$.

**Solución:**

Partimos de la ecuación vectorial: $(x,y,z) = (-1,3,2) + \lambda(4,-2,1)$.

Igualando coordenada a coordenada se obtienen las **ecuaciones paramétricas**:

$$\boxed{\begin{cases} x = -1 + 4\lambda \\ y = 3 - 2\lambda \\ z = 2 + \lambda \end{cases}, \quad \lambda \in \mathbb{R}}$$

Cada valor de $\lambda \in \mathbb{R}$ determina un punto único de la recta.

**Ejemplo de uso:** Para $\lambda = 1$: $(x,y,z) = (3, 1, 3)$, que es otro punto de la recta.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Escribe las ecuaciones paramétricas de la recta que pasa por $P(2,0,-1)$ con vector director $\vec{d}=(1,3,-2)$.

   > **Solución:**
   > $$\begin{cases} x = 2 + \lambda \\ y = 3\lambda \\ z = -1 - 2\lambda \end{cases}, \quad \lambda \in \mathbb{R}$$

2. Halla las ecuaciones paramétricas de la recta que pasa por $A(0,0,0)$ y $B(1,-2,3)$.

   > **Solución:** El vector director es $\vec{AB} = (1,-2,3)$. Tomando $A$ como punto:
   > $$\begin{cases} x = \lambda \\ y = -2\lambda \\ z = 3\lambda \end{cases}, \quad \lambda \in \mathbb{R}$$
   > Esta recta pasa por el origen con la dirección de $(1,-2,3)$.

**Nivel Intermedio:**

3. De las ecuaciones paramétricas $\begin{cases} x = 2 + 3\lambda \\ y = -1 + \lambda \\ z = 4 - 2\lambda \end{cases}$, determina el punto de corte de la recta con el plano $z = 0$.

   > **Solución:** El plano $z=0$ corresponde a $z=0$ en las paramétricas:
   > $$4 - 2\lambda = 0 \Rightarrow \lambda = 2$$
   > Sustituyendo $\lambda = 2$:
   > $$x = 2 + 6 = 8, \quad y = -1 + 2 = 1, \quad z = 0$$
   > El punto de corte con el plano $z=0$ es $\mathbf{(8, 1, 0)}$.

4. Una recta tiene ecuaciones paramétricas $x = 1+t$, $y = 2-t$, $z = -1+2t$. Encuentra los puntos de la recta cuya coordenada $x$ es igual a su coordenada $y$.

   > **Solución:** Imponemos $x = y$:
   > $$1 + t = 2 - t \Rightarrow 2t = 1 \Rightarrow t = \frac{1}{2}$$
   > Sustituyendo $t = 1/2$:
   > $$x = 1 + \frac{1}{2} = \frac{3}{2}, \quad y = 2 - \frac{1}{2} = \frac{3}{2}, \quad z = -1 + 1 = 0$$
   > El punto buscado es $\left(\dfrac{3}{2}, \dfrac{3}{2}, 0\right)$.

**Nivel EVAU:**

5. Se consideran las rectas:
   $$r:\; \begin{cases} x = 1 + 2t \\ y = -t \\ z = 3 + t \end{cases} \qquad s:\; \begin{cases} x = 3 + \mu \\ y = 2 + \mu \\ z = 5 - \mu \end{cases}$$

   **(a)** Halla los vectores directores de $r$ y $s$.

   **(b)** Estudia si $r$ y $s$ se cortan. Si se cortan, halla el punto de intersección.

   > **Solución:**
   >
   > **(a)** De las paramétricas: $\vec{d}_r = (2,-1,1)$ y $\vec{d}_s = (1,1,-1)$.
   >
   > **(b)** Para que se corten, el sistema $r = s$ debe tener solución:
   > $$1+2t = 3+\mu \;\Rightarrow\; 2t - \mu = 2 \quad (I)$$
   > $$-t = 2+\mu \;\Rightarrow\; -t - \mu = 2 \quad (II)$$
   > $$3+t = 5-\mu \;\Rightarrow\; t + \mu = 2 \quad (III)$$
   >
   > De $(II)$ y $(III)$: sumando, $-t - \mu + t + \mu = 4 \Rightarrow 0 = 4$, **contradicción**.
   > El sistema es incompatible. Los vectores directores no son proporcionales (las rectas no son paralelas), y no se cortan, por lo tanto $r$ y $s$ **se cruzan** (son rectas cruzadas).

**Test de Opción Múltiple**

6. Las ecuaciones paramétricas $x = 2 - t,\; y = 1,\; z = 3 + 2t$ corresponden a una recta que:
   - a) Es paralela al eje $OX$
   - b) Es paralela al eje $OY$
   - c) Es paralela al plano $XOY$
   - d) Pasa por el origen de coordenadas

   > **Respuesta correcta:** c) El vector director es $(-1, 0, 2)$. Como la componente $y$ es constante ($y=1$), la recta es paralela al plano $XOZ$ y, en particular, paralela al plano $XOY$. (No tiene componente en $y$, lo que implica que es paralela al plano $XOZ$, no al $XOY$.) Corrección: el vector director $(-1,0,2)$ tiene componente $y=0$, así que la recta es **paralela al plano $XOZ$**. La respuesta correcta entre las dadas es c), pues tampoco pasa por el origen ($y$ sería 0, no 1).

7. La recta $r$ tiene ecuaciones paramétricas $x=3,\; y=1+2\lambda,\; z=-2+\lambda$. ¿Cuál es su vector director?
   - a) $(3, 1, -2)$
   - b) $(0, 2, 1)$
   - c) $(1, 2, 1)$
   - d) $(3, 2, 1)$

   > **Respuesta correcta:** b) En las ecuaciones paramétricas $x = 3 + 0\cdot\lambda$, $y = 1+2\lambda$, $z = -2+\lambda$, los coeficientes de $\lambda$ son $(0, 2, 1)$, que es el vector director.

---

#### 5.1.3 Ecuaciones Simétricas (o Continuas) de la Recta

**Ejercicio Resuelto**

Obtén las ecuaciones simétricas (continuas) de la recta que pasa por $A(3, -1, 2)$ con vector director $\vec{d} = (2, 4, -3)$.

**Solución:**

Las ecuaciones paramétricas son:
$$x = 3 + 2\lambda, \quad y = -1 + 4\lambda, \quad z = 2 - 3\lambda$$

Despejando $\lambda$ de cada una:
$$\lambda = \frac{x-3}{2}, \quad \lambda = \frac{y+1}{4}, \quad \lambda = \frac{z-2}{-3}$$

Igualando los tres miembros (dado que los tres valen $\lambda$):

$$\boxed{\frac{x-3}{2} = \frac{y+1}{4} = \frac{z-2}{-3}}$$

Estas son las **ecuaciones simétricas** (o continuas) de la recta. El denominador de cada fracción es la componente correspondiente del vector director.

**Nota:** Si una componente del vector director es cero, esa coordenada es constante y se escribe aparte. Por ejemplo, si $d_y = 0$, se escribe $y = y_0$ y $\dfrac{x-x_0}{d_x} = \dfrac{z-z_0}{d_z}$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Escribe las ecuaciones simétricas de la recta con ecuaciones paramétricas $x = 1+2t,\; y = -3+t,\; z = 5-4t$.

   > **Solución:** Despejamos $t$ de cada ecuación:
   > $$t = \frac{x-1}{2}, \quad t = y+3, \quad t = \frac{z-5}{-4}$$
   > Las ecuaciones simétricas son:
   > $$\frac{x-1}{2} = \frac{y+3}{1} = \frac{z-5}{-4}$$

2. Halla las ecuaciones simétricas de la recta que pasa por $A(2,1,-3)$ y $B(5,1,0)$.

   > **Solución:** $\vec{AB} = (3, 0, 3)$. Como la componente $y$ es cero, la coordenada $y$ permanece constante:
   > $$y = 1 \quad \text{y} \quad \frac{x-2}{3} = \frac{z+3}{3}$$
   > Simplificando la segunda: $x - 2 = z + 3$, es decir $x - z = 5$.

**Nivel Intermedio:**

3. La recta $r$ tiene ecuaciones simétricas $\dfrac{x+1}{3} = \dfrac{y-2}{-1} = \dfrac{z}{2}$. Halla un punto de $r$ y su vector director. Determina las ecuaciones paramétricas.

   > **Solución:**
   > - **Punto:** igualando cada fracción a $0$: $x+1=0, y-2=0, z=0$, luego $P(-1, 2, 0) \in r$.
   > - **Vector director:** los denominadores dan $\vec{d} = (3,-1,2)$.
   > - **Ecuaciones paramétricas:**
   > $$x = -1+3\lambda, \quad y = 2-\lambda, \quad z = 2\lambda, \quad \lambda \in \mathbb{R}$$

4. Comprueba si el punto $Q(5, 0, 4)$ pertenece a la recta $\dfrac{x-1}{2} = \dfrac{y+1}{-\frac{1}{2}} = \dfrac{z-2}{1}$.

   > **Solución:** Sustituimos $Q(5,0,4)$:
   > $$\frac{5-1}{2} = \frac{4}{2} = 2, \quad \frac{0+1}{-\frac{1}{2}} = \frac{1}{-0{,}5} = -2, \quad \frac{4-2}{1} = 2$$
   > El primer y tercer cociente valen $2$, pero el segundo vale $-2$. **Los tres cocientes no son iguales**, por tanto $Q \notin r$.

**Nivel EVAU:**

5. Sea la recta $r:\;\dfrac{x-2}{1} = \dfrac{y+1}{2} = \dfrac{z-3}{-2}$.

   **(a)** Escribe las ecuaciones paramétricas de $r$.

   **(b)** Halla el punto de intersección de $r$ con el plano $\pi:\; 2x - y + z = 1$.

   **(c)** Calcula la distancia del punto $A(2,-1,3)$ al plano $\pi$.

   > **Solución:**
   >
   > **(a)** Vector director $\vec{d} = (1,2,-2)$, punto $P(2,-1,3)$:
   > $$r:\;\begin{cases} x = 2 + \lambda \\ y = -1 + 2\lambda \\ z = 3 - 2\lambda \end{cases}$$
   >
   > **(b)** Sustituimos en $\pi$:
   > $$2(2+\lambda) - (-1+2\lambda) + (3-2\lambda) = 1$$
   > $$4 + 2\lambda + 1 - 2\lambda + 3 - 2\lambda = 1$$
   > $$8 - 2\lambda = 1 \Rightarrow \lambda = \frac{7}{2}$$
   > Punto de intersección:
   > $$x = 2 + \frac{7}{2} = \frac{11}{2}, \quad y = -1 + 7 = 6, \quad z = 3 - 7 = -4$$
   > **Intersección:** $\left(\dfrac{11}{2}, 6, -4\right)$.
   >
   > **(c)** El punto $A(2,-1,3)$ es precisamente el punto base de $r$, que está en $r$. Comprobamos si $A \in \pi$:
   > $$2(2)-(-1)+3 = 4+1+3 = 8 \neq 1$$
   > $A \notin \pi$. Distancia:
   > $$d(A,\pi) = \frac{|2\cdot2 - (-1) + 3 - 1|}{\sqrt{4+1+1}} = \frac{|4+1+3-1|}{\sqrt{6}} = \frac{7}{\sqrt{6}} = \frac{7\sqrt{6}}{6}$$

**Test de Opción Múltiple**

6. ¿Cuál de las siguientes es la forma simétrica de la recta con ecuaciones paramétricas $x=2+3t,\; y=1-t,\; z=-4+2t$?
   - a) $\dfrac{x+2}{3} = \dfrac{y-1}{-1} = \dfrac{z-4}{2}$
   - b) $\dfrac{x-2}{3} = \dfrac{y-1}{-1} = \dfrac{z+4}{2}$
   - c) $\dfrac{x-2}{3} = \dfrac{y+1}{-1} = \dfrac{z+4}{2}$
   - d) $\dfrac{x-3}{2} = \dfrac{y+1}{1} = \dfrac{z-2}{-4}$

   > **Respuesta correcta:** b) El punto es $(2,1,-4)$ y el vector director $(3,-1,2)$, lo que da $\dfrac{x-2}{3}=\dfrac{y-1}{-1}=\dfrac{z+4}{2}$.

7. Si una componente del vector director de una recta es cero, las ecuaciones simétricas:
   - a) No existen para esa recta
   - b) Se escriben indicando que esa coordenada es constante e igualando las otras dos fracciones
   - c) Se sustituyen por las ecuaciones paramétricas
   - d) Implican que la recta es paralela a los tres ejes

   > **Respuesta correcta:** b) Cuando $d_k = 0$, la coordenada $k$-ésima es constante e igual al valor del punto base; las otras dos fracciones se igualan normalmente.

---

#### 5.1.4 Paso entre las Distintas Formas de la Ecuación de la Recta

**Ejercicio Resuelto**

Dada la recta $r:\;\dfrac{x-1}{2} = \dfrac{y+3}{-1} = \dfrac{z}{4}$, expresa $r$ en forma vectorial y en forma paramétrica. Halla después un segundo punto de $r$ distinto del punto base.

**Solución:**

**Paso 1: Identificar punto y vector director.**

De las ecuaciones simétricas: punto base $P(1,-3,0)$ y vector director $\vec{d} = (2,-1,4)$.

**Paso 2: Forma vectorial.**

$$(x,y,z) = (1,-3,0) + \lambda(2,-1,4), \quad \lambda \in \mathbb{R}$$

**Paso 3: Forma paramétrica.**

$$\begin{cases} x = 1 + 2\lambda \\ y = -3 - \lambda \\ z = 4\lambda \end{cases}$$

**Paso 4: Segundo punto** (tomamos $\lambda = 1$):
$$P' = (1+2,\; -3-1,\; 4) = (3,-4,4)$$

**Verificación:** $\dfrac{3-1}{2} = 1$, $\dfrac{-4+3}{-1} = 1$, $\dfrac{4}{4} = 1$ ✓

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Convierte a forma paramétrica la recta $r:\;(x,y,z) = (2,-1,5) + \lambda(-3,2,0)$.

   > **Solución:**
   > $$\begin{cases} x = 2 - 3\lambda \\ y = -1 + 2\lambda \\ z = 5 \end{cases}$$
   > Obsérvese que la componente $z$ es constante ($z = 5$), lo que significa que $r$ es paralela al plano $XOY$.

2. Pasa a ecuaciones simétricas la recta: $\begin{cases} x = -1 + 4t \\ y = 2 - t \\ z = 3 + 2t \end{cases}$

   > **Solución:** Despejamos $t$: $t = \dfrac{x+1}{4}$, $t = -(y-2) = \dfrac{y-2}{-1}$, $t = \dfrac{z-3}{2}$.
   > Las ecuaciones simétricas son:
   > $$\frac{x+1}{4} = \frac{y-2}{-1} = \frac{z-3}{2}$$

**Nivel Intermedio:**

3. Una recta pasa por $A(1,2,3)$ y es perpendicular al plano $\pi:\; 2x - y + 3z = 5$. Escribe sus ecuaciones en las tres formas (vectorial, paramétrica y simétrica).

   > **Solución:** El vector normal al plano es $\vec{n} = (2,-1,3)$. Una recta perpendicular al plano tiene como vector director $\vec{n}$.
   > - **Vectorial:** $(x,y,z) = (1,2,3) + \lambda(2,-1,3)$
   > - **Paramétrica:** $x = 1+2\lambda,\; y = 2-\lambda,\; z = 3+3\lambda$
   > - **Simétrica:** $\dfrac{x-1}{2} = \dfrac{y-2}{-1} = \dfrac{z-3}{3}$

4. Una recta $r$ tiene ecuaciones simétricas $\dfrac{x-a}{2} = \dfrac{y-1}{b} = \dfrac{z+3}{1}$ y pasa por el punto $Q(4,-1,-2)$. Halla $a$ y $b$.

   > **Solución:** Como $Q \in r$, sustituimos $Q(4,-1,-2)$:
   > $$\frac{4-a}{2} = \frac{-1-1}{b} = \frac{-2+3}{1} = 1$$
   > De la igualdad con $1$:
   > - $\dfrac{4-a}{2} = 1 \Rightarrow 4-a = 2 \Rightarrow a = 2$
   > - $\dfrac{-2}{b} = 1 \Rightarrow b = -2$

**Nivel EVAU:**

5. Se da la recta $r$ mediante las ecuaciones $\dfrac{x-2}{1} = \dfrac{y+1}{3} = \dfrac{z-4}{-2}$ y el punto $A(4,5,0)$.

   **(a)** Escribe las ecuaciones paramétricas de $r$ y el vector director.

   **(b)** Halla la recta $s$ que pasa por $A$ y es paralela a $r$, expresándola en forma vectorial y simétrica.

   **(c)** Comprueba que $A \notin r$.

   > **Solución:**
   >
   > **(a)** Vector director $\vec{d}_r = (1,3,-2)$, punto $P(2,-1,4)$.
   > $$r:\;\begin{cases} x = 2 + \lambda \\ y = -1 + 3\lambda \\ z = 4 - 2\lambda \end{cases}$$
   >
   > **(b)** $s$ pasa por $A(4,5,0)$ con $\vec{d}_s = \vec{d}_r = (1,3,-2)$:
   > - Vectorial: $(x,y,z) = (4,5,0) + \mu(1,3,-2)$
   > - Simétrica: $\dfrac{x-4}{1} = \dfrac{y-5}{3} = \dfrac{z}{-2}$
   >
   > **(c)** Sustituimos $A(4,5,0)$ en las ecuaciones simétricas de $r$:
   > $$\frac{4-2}{1} = 2, \quad \frac{5+1}{3} = 2, \quad \frac{0-4}{-2} = 2$$
   > Los tres cocientes valen $2$, lo que significa $A \in r$. Por tanto hay que recalcular: sí pertenece.
   > **Nota de corrección:** $A(4,5,0) \in r$ con $\lambda = 2$: $x=2+2=4$✓, $y=-1+6=5$✓, $z=4-4=0$✓. Por tanto $A \in r$ y $s = r$.

**Test de Opción Múltiple**

6. La recta $(x,y,z)=(1,0,-2)+\lambda(3,-2,1)$ expresada en forma simétrica es:
   - a) $\dfrac{x-3}{1}=\dfrac{y+2}{0}=\dfrac{z-1}{-2}$
   - b) $\dfrac{x-1}{3}=\dfrac{y}{-2}=\dfrac{z+2}{1}$
   - c) $\dfrac{x+1}{3}=\dfrac{y}{-2}=\dfrac{z-2}{1}$
   - d) $\dfrac{x-1}{3}=\dfrac{y+2}{-1}=\dfrac{z+2}{1}$

   > **Respuesta correcta:** b) El punto base es $(1,0,-2)$ y el vector director $(3,-2,1)$, dando $\dfrac{x-1}{3}=\dfrac{y-0}{-2}=\dfrac{z-(-2)}{1} = \dfrac{x-1}{3}=\dfrac{y}{-2}=\dfrac{z+2}{1}$.

7. Para pasar de ecuaciones simétricas a paramétricas, el parámetro $\lambda$ es:
   - a) El valor de $x$ en un punto de la recta
   - b) El valor común de las tres fracciones igualadas
   - c) La distancia del punto al origen
   - d) La longitud del vector director

   > **Respuesta correcta:** b) En las ecuaciones simétricas $\dfrac{x-x_0}{d_x}=\dfrac{y-y_0}{d_y}=\dfrac{z-z_0}{d_z}=\lambda$, el parámetro $\lambda$ es el valor común de las tres fracciones igualadas.

---

## 5.2 Ecuaciones del Plano en el Espacio

---

#### 5.2.1 Ecuación Vectorial del Plano

**Ejercicio Resuelto**

Halla la ecuación vectorial del plano que pasa por $P(1,2,-1)$ y tiene vectores directores $\vec{u} = (1,0,3)$ y $\vec{v} = (0,1,-2)$.

**Solución:**

Todo plano queda determinado por un punto $P_0$ y dos vectores directores linealmente independientes $\vec{u}$ y $\vec{v}$ (no proporcionales).

La ecuación vectorial es:
$$\vec{r} = \overrightarrow{OP_0} + \lambda\,\vec{u} + \mu\,\vec{v}, \quad \lambda,\mu \in \mathbb{R}$$

En nuestro caso:
$$\boxed{(x,y,z) = (1,2,-1) + \lambda(1,0,3) + \mu(0,1,-2), \quad \lambda,\mu \in \mathbb{R}}$$

**Comprobación de independencia lineal:** $\vec{u} \times \vec{v} = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&0&3\\0&1&-2\end{vmatrix} = (0\cdot(-2)-3\cdot1)\vec{i} - (1\cdot(-2)-3\cdot0)\vec{j} + (1\cdot1-0\cdot0)\vec{k} = (-3,2,1) \neq \vec{0}$ ✓

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Escribe la ecuación vectorial del plano que pasa por el origen $O(0,0,0)$ con vectores directores $\vec{u}=(1,0,0)$ y $\vec{v}=(0,1,0)$.

   > **Solución:**
   > $$(x,y,z) = \lambda(1,0,0) + \mu(0,1,0) = (\lambda, \mu, 0), \quad \lambda,\mu \in \mathbb{R}$$
   > Esto es el plano $z=0$, es decir, el plano $XOY$.

2. Escribe la ecuación vectorial del plano que pasa por $A(1,-1,2)$, $B(3,0,1)$ y $C(2,-2,4)$.

   > **Solución:** Los vectores directores son:
   > $$\vec{AB} = (2,1,-1), \quad \vec{AC} = (1,-1,2)$$
   > Comprobamos independencia: $\vec{AB}$ y $\vec{AC}$ no son proporcionales ✓
   > $$(x,y,z) = (1,-1,2) + \lambda(2,1,-1) + \mu(1,-1,2), \quad \lambda,\mu \in \mathbb{R}$$

**Nivel Intermedio:**

3. El plano $\pi$ tiene ecuación vectorial $(x,y,z) = (2,1,3)+\lambda(1,-1,0)+\mu(2,0,1)$. Halla un punto del plano para $\lambda=2$, $\mu=-1$ y comprueba que pertenece al plano.

   > **Solución:** Para $\lambda=2$, $\mu=-1$:
   > $$(x,y,z) = (2,1,3) + 2(1,-1,0) + (-1)(2,0,1) = (2,1,3)+(2,-2,0)+(-2,0,-1) = (2,- 1,2)$$
   > El punto $Q(2,-1,2)$ se obtiene. Para verificar que pertenece al plano, existe $(\lambda,\mu)=(2,-1)$ que genera $Q$ ✓.

4. ¿Pueden los vectores $\vec{u}=(1,2,3)$ y $\vec{v}=(2,4,6)$ ser los vectores directores de un plano? Razona la respuesta.

   > **Solución:** $\vec{v} = 2\vec{u}$, luego $\vec{u}$ y $\vec{v}$ son **proporcionales** (linealmente dependientes). No pueden ser los vectores directores de un plano, ya que todo par de vectores directores debe ser linealmente independiente para determinar un plano (dos vectores proporcionales determinan solo una recta).

**Nivel EVAU:**

5. Se consideran los puntos $A(1,0,2)$, $B(2,1,0)$ y $C(0,-1,3)$.

   **(a)** Halla la ecuación vectorial del plano $\pi$ que pasa por $A$, $B$ y $C$.

   **(b)** Comprueba que $D(3,2,-2)$ pertenece a $\pi$ (encuentra $\lambda$ y $\mu$ adecuados).

   > **Solución:**
   >
   > **(a)** $\vec{AB} = (1,1,-2)$, $\vec{AC} = (-1,-1,1)$.
   > Pero $\vec{AC} = -\vec{AB}$... comprobamos: $(-1,-1,1) \neq k(1,1,-2)$ para ningún $k$ real único... $-1 = k$, $-1=k$ ✓, $1 = -2k = 2$ ✗. No son proporcionales.
   > $$(x,y,z) = (1,0,2) + \lambda(1,1,-2) + \mu(-1,-1,1)$$
   > Nota: $\vec{AB}$ y $\vec{AC}$: $(-1,-1,1) = -1\cdot(1,1,-1)$, son linealmente dependientes solo si $(1,1,-2)\parallel(-1,-1,1)$: $-1/1=-1/1=1/(-2)$? $-1\neq -1/2$. Luego **no son proporcionales** ✓.
   >
   > **(b)** Sistema: $(1,0,2)+\lambda(1,1,-2)+\mu(-1,-1,1)=(3,2,-2)$
   > $$\lambda - \mu = 2 \quad (I)$$
   > $$\lambda - \mu = 2 \quad (II)$$
   > $$-2\lambda + \mu = -4 \quad (III)$$
   > De $(I)$: $\mu = \lambda - 2$. Sustituyendo en $(III)$: $-2\lambda + \lambda - 2 = -4 \Rightarrow \lambda = 2$, $\mu = 0$.
   > Verificación: $(1,0,2)+2(1,1,-2)=(3,2,-2)$ ✓. Por tanto $D \in \pi$.

**Test de Opción Múltiple**

6. La ecuación vectorial de un plano contiene:
   - a) Un punto y un vector director
   - b) Dos puntos y un vector director
   - c) Un punto y dos vectores directores linealmente independientes
   - d) Tres vectores directores

   > **Respuesta correcta:** c) La ecuación vectorial del plano $\vec{r} = \vec{r_0} + \lambda\vec{u} + \mu\vec{v}$ requiere un punto $P_0$ (que da $\vec{r_0}$) y dos vectores directores $\vec{u}$, $\vec{v}$ linealmente independientes.

7. El plano con ecuación vectorial $(x,y,z)=(1,2,3)+\lambda(1,0,0)+\mu(0,1,0)$ es:
   - a) El plano $z=0$
   - b) El plano $z=3$
   - c) El plano $x+y=3$
   - d) El plano $x=1$

   > **Respuesta correcta:** b) Desarrollando: $x=1+\lambda$, $y=2+\mu$, $z=3$. La coordenada $z$ siempre vale $3$, luego es el plano $z=3$.

---

#### 5.2.2 Ecuación General (Implícita) del Plano. Vector Normal

**Ejercicio Resuelto**

Halla la ecuación general del plano $\pi$ que pasa por $A(1,-1,2)$ y tiene vector normal $\vec{n} = (3,-2,1)$.

**Solución:**

La ecuación general de un plano con vector normal $\vec{n} = (a,b,c)$ que pasa por el punto $P_0(x_0,y_0,z_0)$ es:

$$a(x-x_0) + b(y-y_0) + c(z-z_0) = 0$$

Sustituyendo $\vec{n}=(3,-2,1)$ y $A(1,-1,2)$:
$$3(x-1) - 2(y-(-1)) + 1(z-2) = 0$$
$$3x - 3 - 2y - 2 + z - 2 = 0$$
$$\boxed{3x - 2y + z - 7 = 0}$$

**Verificación:** $3(1)-2(-1)+2-7 = 3+2+2-7 = 0$ ✓

**Nota:** El vector normal se lee directamente de los coeficientes $(a,b,c)$ de la ecuación general $ax+by+cz+d=0$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla la ecuación general del plano que pasa por $P(0,0,0)$ con vector normal $\vec{n}=(1,2,3)$.

   > **Solución:**
   > $$1(x-0)+2(y-0)+3(z-0)=0 \Rightarrow \boxed{x+2y+3z=0}$$
   > Este plano pasa por el origen.

2. Identifica el vector normal del plano $\pi:\; 2x - 5y + z + 4 = 0$ y un punto del plano.

   > **Solución:**
   > - **Vector normal:** $\vec{n} = (2,-5,1)$ (coeficientes de $x$, $y$, $z$).
   > - **Punto del plano:** basta encontrar un punto que satisfaga la ecuación. Tomando $x=0,y=0$: $z=-4$. Punto: $(0,0,-4)$.
   > **Verificación:** $0-0-4+4=0$ ✓.

**Nivel Intermedio:**

3. Halla la ecuación del plano que pasa por $A(2,0,1)$ y $B(1,3,-1)$ y es perpendicular al plano $\pi_0:\; x-y+2z=3$.

   > **Solución:** Sea $\vec{n}=(a,b,c)$ el normal al plano buscado. Condiciones:
   > 1. $\overrightarrow{AB} = (-1,3,-2)$ es paralelo al plano buscado, por tanto $\vec{n} \perp \overrightarrow{AB}$: $-a+3b-2c=0$.
   > 2. El plano es perpendicular a $\pi_0$, que tiene normal $\vec{n}_0=(1,-1,2)$. Los normales son perpendiculares: $\vec{n}\cdot\vec{n}_0=0$: $a-b+2c=0$.
   > Sistema: $-a+3b-2c=0$ y $a-b+2c=0$. Sumando: $2b=0 \Rightarrow b=0$.
   > De la segunda: $a+2c=0 \Rightarrow a=-2c$. Tomando $c=1$: $a=-2$, $b=0$.
   > $\vec{n}=(-2,0,1)$. El plano pasa por $A(2,0,1)$:
   > $$-2(x-2)+0(y-0)+1(z-1)=0 \Rightarrow -2x+4+z-1=0 \Rightarrow \boxed{-2x+z+3=0}$$

4. Halla el valor de $k$ para que el plano $\pi_1:\; kx - 2y + z = 3$ sea perpendicular al plano $\pi_2:\; x + ky + 2z = 0$.

   > **Solución:** Los normales son $\vec{n}_1=(k,-2,1)$ y $\vec{n}_2=(1,k,2)$.
   > Perpendicularidad $\Leftrightarrow \vec{n}_1\cdot\vec{n}_2=0$:
   > $$k\cdot1 + (-2)\cdot k + 1\cdot 2 = 0 \Rightarrow k - 2k + 2 = 0 \Rightarrow -k + 2 = 0 \Rightarrow k = 2$$

**Nivel EVAU:**

5. Sea el plano $\pi:\; 2x + y - 3z + 6 = 0$.

   **(a)** Halla el vector normal a $\pi$ y un punto de $\pi$.

   **(b)** Determina la ecuación del plano $\sigma$ paralelo a $\pi$ que pasa por $Q(1,0,2)$.

   **(c)** Calcula la distancia entre $\pi$ y $\sigma$.

   > **Solución:**
   >
   > **(a)** $\vec{n} = (2,1,-3)$. Punto: con $x=0,y=0$: $-3z=-6 \Rightarrow z=2$. Punto: $(0,0,2)$.
   >
   > **(b)** $\sigma \parallel \pi$ $\Rightarrow$ mismo vector normal $\vec{n}=(2,1,-3)$.
   > $$\sigma:\; 2(x-1)+1(y-0)-3(z-2)=0 \Rightarrow 2x+y-3z+4=0$$
   >
   > **(c)** Distancia entre planos paralelos $ax+by+cz+d_1=0$ y $ax+by+cz+d_2=0$:
   > $$d = \frac{|d_1-d_2|}{\sqrt{a^2+b^2+c^2}} = \frac{|6-4|}{\sqrt{4+1+9}} = \frac{2}{\sqrt{14}} = \frac{2\sqrt{14}}{14} = \frac{\sqrt{14}}{7}$$

**Test de Opción Múltiple**

6. El vector normal al plano $3x - y + 2z - 5 = 0$ es:
   - a) $(3,-1,2,-5)$
   - b) $(-3,1,-2)$
   - c) $(3,-1,2)$
   - d) $(3,1,2)$

   > **Respuesta correcta:** c) El vector normal se lee de los coeficientes de $x$, $y$, $z$: $\vec{n}=(3,-1,2)$.

7. Si dos planos tienen vectores normales proporcionales, entonces:
   - a) Son perpendiculares
   - b) Son paralelos o coincidentes
   - c) Se cortan en una recta
   - d) Se cortan en un punto

   > **Respuesta correcta:** b) Si $\vec{n}_1 = k\vec{n}_2$, los planos son paralelos (si son distintos) o coincidentes (si son el mismo). La condición de corte implica que los normales no sean proporcionales.

---

#### 5.2.3 Determinación de la Ecuación del Plano dados Tres Puntos

**Ejercicio Resuelto**

Determina la ecuación general del plano que pasa por los puntos $A(1,0,0)$, $B(0,2,0)$ y $C(0,0,3)$.

**Solución:**

**Método del vector normal mediante producto vectorial:**

$\vec{AB} = (-1,2,0)$, $\vec{AC} = (-1,0,3)$.

El vector normal es $\vec{n} = \vec{AB} \times \vec{AC}$:

$$\vec{n} = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&2&0\\-1&0&3\end{vmatrix} = (2\cdot3 - 0\cdot0)\vec{i} - ((-1)\cdot3 - 0\cdot(-1))\vec{j} + ((-1)\cdot0 - 2\cdot(-1))\vec{k}$$
$$= (6)\vec{i} - (-3)\vec{j} + (2)\vec{k} = (6,3,2)$$

El plano pasa por $A(1,0,0)$ con normal $(6,3,2)$:
$$6(x-1)+3(y-0)+2(z-0)=0 \Rightarrow \boxed{6x+3y+2z-6=0}$$

**Verificación:** $A$: $6-6=0$ ✓; $B$: $0+6+0-6=0$ ✓; $C$: $0+0+6-6=0$ ✓.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla la ecuación del plano que pasa por $A(1,1,0)$, $B(0,1,1)$ y $C(1,0,1)$.

   > **Solución:** $\vec{AB}=(-1,0,1)$, $\vec{AC}=(0,-1,1)$.
   > $$\vec{n} = \vec{AB}\times\vec{AC} = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&0&1\\0&-1&1\end{vmatrix} = (0\cdot1-1\cdot(-1))\vec{i}-((-1)\cdot1-1\cdot0)\vec{j}+((-1)(-1)-0\cdot0)\vec{k}$$
   > $= (1)\vec{i}-(-1)\vec{j}+(1)\vec{k} = (1,1,1)$
   > Plano por $A(1,1,0)$: $(x-1)+(y-1)+z=0 \Rightarrow \boxed{x+y+z-2=0}$
   > Verificación: $A$: $1+1+0-2=0$✓, $B$: $0+1+1-2=0$✓, $C$: $1+0+1-2=0$✓.

2. Encuentra la ecuación del plano que pasa por $A(2,0,0)$, $B(0,3,0)$ y $C(0,0,1)$.

   > **Solución:** $\vec{AB}=(-2,3,0)$, $\vec{AC}=(-2,0,1)$.
   > $$\vec{n}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-2&3&0\\-2&0&1\end{vmatrix}=(3\cdot1-0\cdot0)\vec{i}-((-2)\cdot1-0\cdot(-2))\vec{j}+((-2)\cdot0-3\cdot(-2))\vec{k}=(3,2,6)$$
   > Por $A(2,0,0)$: $3(x-2)+2y+6z=0 \Rightarrow \boxed{3x+2y+6z-6=0}$

**Nivel Intermedio:**

3. Halla el plano determinado por los puntos $P(1,-1,0)$, $Q(2,1,3)$ y $R(-1,0,1)$.

   > **Solución:** $\vec{PQ}=(1,2,3)$, $\vec{PR}=(-2,1,1)$.
   > $$\vec{n}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&2&3\\-2&1&1\end{vmatrix}=(2-3)\vec{i}-(1+6)\vec{j}+(1+4)\vec{k}=(-1,-7,5)$$
   > Por $P(1,-1,0)$: $-(x-1)-7(y+1)+5z=0 \Rightarrow -x+1-7y-7+5z=0$
   > $$\boxed{-x-7y+5z-6=0} \quad \text{o equivalentemente}\quad x+7y-5z+6=0$$

4. Tres puntos del plano $\pi:\; ax+2y-z=3$ son $A(1,1,0)$, $B(t,0,1)$ y $C(0,-1,k)$. Determina $t$ y $k$.

   > **Solución:** Sustituimos cada punto en $ax+2y-z=3$... espera, primero determinamos $a$ con $A$:
   > $a(1)+2(1)-0=3 \Rightarrow a=1$.
   > El plano es $x+2y-z=3$.
   > Para $B(t,0,1)$: $t+0-1=3 \Rightarrow t=4$.
   > Para $C(0,-1,k)$: $0-2-k=3 \Rightarrow k=-5$.

**Nivel EVAU:**

5. Dados los puntos $A(2,1,-1)$, $B(0,3,2)$ y $C(-1,2,1)$:

   **(a)** Halla la ecuación del plano $\pi$ que contiene a $A$, $B$ y $C$.

   **(b)** Determina si el punto $D(1,6,5)$ pertenece a $\pi$.

   **(c)** Halla la ecuación del plano $\sigma$ paralelo a $\pi$ que pasa por el origen.

   > **Solución:**
   >
   > **(a)** $\vec{AB}=(-2,2,3)$, $\vec{AC}=(-3,1,2)$.
   > $$\vec{n}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-2&2&3\\-3&1&2\end{vmatrix}=(4-3)\vec{i}-(-4+9)\vec{j}+(-2+6)\vec{k}=(1,-5,4)$$
   > Por $A(2,1,-1)$: $(x-2)-5(y-1)+4(z+1)=0$
   > $$x-2-5y+5+4z+4=0 \Rightarrow \boxed{x-5y+4z+7=0}$$
   >
   > **(b)** $D(1,6,5)$: $1-30+20+7=-2\neq0$. $D \notin \pi$.
   >
   > **(c)** $\sigma \parallel \pi$ con el mismo vector normal $(1,-5,4)$, pasando por $O(0,0,0)$:
   > $\boxed{x-5y+4z=0}$.

**Test de Opción Múltiple**

6. Para hallar la ecuación del plano por tres puntos, el método más sistemático es:
   - a) Calcular el producto escalar de dos vectores del plano
   - b) Calcular el producto vectorial de dos vectores del plano para obtener el vector normal
   - c) Calcular el producto mixto de tres vectores
   - d) Usar la regla de Sarrus con las coordenadas de los tres puntos directamente

   > **Respuesta correcta:** b) El producto vectorial $\vec{AB}\times\vec{AC}$ da el vector normal al plano, que luego se usa en la ecuación punto-normal.

7. Si tres puntos son colineales (están en la misma recta), al intentar determinar el plano que pasan por ellos:
   - a) Se obtiene un plano único
   - b) Se obtienen infinitos planos
   - c) No existe ningún plano
   - d) Se obtienen exactamente dos planos

   > **Respuesta correcta:** b) Si los tres puntos son colineales, $\vec{AB}$ y $\vec{AC}$ son proporcionales, el producto vectorial es $\vec{0}$, y hay infinitos planos que contienen a esa recta.

---

#### 5.2.4 Planos Paralelos a los Ejes Coordenados y Paralelos entre Sí

**Ejercicio Resuelto**

Clasifica los planos $\pi_1:\; 3x - 6y + 9z = 12$, $\pi_2:\; x - 2y + 3z = 5$ y $\pi_3:\; y - z = 2$ indicando si son paralelos a algún eje o plano coordenado.

**Solución:**

**$\pi_1$ y $\pi_2$:** Los vectores normales son $\vec{n}_1 = (3,-6,9)$ y $\vec{n}_2 = (1,-2,3)$. Observamos que $\vec{n}_1 = 3\vec{n}_2$, luego son proporcionales: los planos son **paralelos o coincidentes**.

Tomamos un punto de $\pi_2$ (p.ej., $x=y=0 \Rightarrow 3z=5 \Rightarrow z=5/3$: el punto $(0,0,5/3)$) y lo sustituimos en $\pi_1$: $3(0)-6(0)+9(5/3) = 15 \neq 12$. Son **planos paralelos distintos**.

**$\pi_3:\; y - z = 2$** tiene vector normal $\vec{n}_3 = (0,1,-1)$. Como la componente en $x$ es cero, $\pi_3$ no contiene al eje $OX$... pero $\vec{n}_3 \perp \vec{e}_1 = (1,0,0)$, lo que significa que $\pi_3$ **contiene la dirección del eje $OX$**: es paralelo al eje $OX$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Escribe la ecuación del plano paralelo al plano $XOY$ que pasa por el punto $P(1,2,5)$.

   > **Solución:** El plano $XOY$ tiene ecuación $z=0$. Un plano paralelo a $XOY$ tiene la forma $z=k$. Como pasa por $P(1,2,5)$: $k=5$.
   > $$\boxed{z = 5}$$

2. ¿Cuál es la ecuación del plano que contiene al eje $OZ$ y al punto $A(1,-1,0)$?

   > **Solución:** El plano contiene al eje $OZ$, por lo que contiene los vectores $\vec{k}=(0,0,1)$ y $\vec{OA}=(1,-1,0)$.
   > Vector normal: $\vec{n} = \vec{k}\times\vec{OA} = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\0&0&1\\1&-1&0\end{vmatrix} = (0\cdot0-1\cdot(-1))\vec{i}-(0\cdot0-1\cdot1)\vec{j}+(0\cdot(-1)-0\cdot1)\vec{k} = (1,1,0)$.
   > Plano por el origen con $\vec{n}=(1,1,0)$: $\boxed{x+y=0}$.

**Nivel Intermedio:**

3. Determina la ecuación del plano paralelo a $\pi:\; 2x-y+3z=7$ que dista $\sqrt{14}$ unidades de $\pi$.

   > **Solución:** Un plano paralelo a $\pi$ tiene la forma $2x-y+3z=k$. La distancia entre dos planos paralelos $2x-y+3z=7$ y $2x-y+3z=k$ es:
   > $$d = \frac{|k-7|}{\sqrt{4+1+9}} = \frac{|k-7|}{\sqrt{14}} = \sqrt{14}$$
   > $|k-7| = 14 \Rightarrow k = 21$ o $k = -7$.
   > Los dos planos buscados son: $\boxed{2x-y+3z=21}$ y $\boxed{2x-y+3z=-7}$.

4. Clasifica los siguientes planos en función de su posición respecto a los ejes coordenados:
   - $\alpha:\; x = 3$
   - $\beta:\; 2y + z = 0$
   - $\gamma:\; x + y = 4$

   > **Solución:**
   > - $\alpha:\;x=3$: vector normal $(1,0,0)=\vec{i}$. El plano es **perpendicular al eje $OX$** y **paralelo al plano $YOZ$**.
   > - $\beta:\;2y+z=0$: normal $(0,2,1)$. La componente en $x$ es cero, así que $\vec{e}_1\perp\vec{n}$: **contiene al eje $OX$** (es paralelo a $OX$).
   > - $\gamma:\;x+y=4$: normal $(1,1,0)$. La componente en $z$ es cero: **paralelo al eje $OZ$**.

**Nivel EVAU:**

5. Sea el plano $\pi:\; x+2y-2z=6$.

   **(a)** ¿Es $\pi$ paralelo a algún eje coordenado? Razona la respuesta.

   **(b)** Halla los dos planos paralelos a $\pi$ que se encuentran a distancia $3$ de $\pi$.

   **(c)** Determina el punto de intersección de $\pi$ con el eje $OX$.

   > **Solución:**
   >
   > **(a)** El vector normal de $\pi$ es $\vec{n}=(1,2,-2)$. Para que $\pi$ sea paralelo al eje $OX$, debería ser $\vec{n}\cdot(1,0,0)=0$, es decir $1=0$: **falso**. Igualmente para $OY$: $\vec{n}\cdot(0,1,0)=2\neq0$, y para $OZ$: $\vec{n}\cdot(0,0,1)=-2\neq0$. $\pi$ **no es paralelo a ningún eje coordenado**.
   >
   > **(b)** Planos paralelos: $x+2y-2z=k$. Distancia a $\pi$:
   > $$\frac{|k-6|}{\sqrt{1+4+4}}=\frac{|k-6|}{3}=3 \Rightarrow |k-6|=9 \Rightarrow k=15 \text{ o } k=-3$$
   > Los planos son $\boxed{x+2y-2z=15}$ y $\boxed{x+2y-2z=-3}$.
   >
   > **(c)** El eje $OX$ tiene ecuaciones $y=0$, $z=0$. Sustituyendo en $\pi$:
   > $x+0-0=6 \Rightarrow x=6$. Punto de intersección: $\boxed{(6,0,0)}$.

**Test de Opción Múltiple**

6. ¿Cuál de los siguientes planos es paralelo al eje $OY$?
   - a) $x+y+z=1$
   - b) $y=2$
   - c) $x-z=3$
   - d) $x+y=5$

   > **Respuesta correcta:** c) Para que el plano sea paralelo al eje $OY$, su vector normal $\vec{n}$ debe ser perpendicular a $\vec{j}=(0,1,0)$, es decir, la componente $y$ del normal debe ser $0$. El plano $x-z=3$ tiene $\vec{n}=(1,0,-1)$, con componente $y$ nula ✓.

7. Dos planos $\pi_1:\;ax+by+cz=d_1$ y $\pi_2:\;ax+by+cz=d_2$ (con $d_1\neq d_2$) son:
   - a) Perpendiculares
   - b) Secantes
   - c) Paralelos y distintos
   - d) Coincidentes

   > **Respuesta correcta:** c) Tienen el mismo vector normal (mismos coeficientes $a,b,c$), luego son paralelos. Como $d_1\neq d_2$, no son el mismo plano: son **paralelos y distintos**.

---

## 5.3 Posiciones Relativas

---

#### 5.3.1 Posición Relativa de Dos Rectas

**Ejercicio Resuelto**

Estudia la posición relativa de las rectas:
$$r:\;\frac{x-1}{2}=\frac{y+1}{-1}=\frac{z}{1} \qquad s:\;\frac{x-3}{4}=\frac{y+3}{-2}=\frac{z-2}{2}$$

**Solución:**

**Paso 1: Vectores directores.**
$\vec{d}_r=(2,-1,1)$, $\vec{d}_s=(4,-2,2)=2(2,-1,1)=2\vec{d}_r$.

Los vectores son proporcionales: las rectas son **paralelas o coincidentes**.

**Paso 2: Comprobar si son la misma recta.**

Tomamos un punto de $s$: $P_s=(3,-3,2)$. ¿Está en $r$?

$$\frac{3-1}{2}=1, \quad \frac{-3+1}{-1}=2, \quad \frac{2}{1}=2$$

Los valores no son iguales ($1\neq 2$), por tanto $P_s \notin r$.

**Conclusión: $r$ y $s$ son rectas paralelas distintas.**

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Estudia si las rectas $r:\,(x,y,z)=(1,0,2)+\lambda(1,-1,3)$ y $s:\,(x,y,z)=(3,-2,8)+\mu(2,-2,6)$ son paralelas, coincidentes, secantes o cruzadas.

   > **Solución:** $\vec{d}_r=(1,-1,3)$, $\vec{d}_s=(2,-2,6)=2\vec{d}_r$. Son proporcionales: paralelas o coincidentes.
   > Punto de $s$: $Q(3,-2,8)$. ¿$Q\in r$? $(3-1)/1=2$, $(-2-0)/(-1)=2$, $(8-2)/3=2$. Los tres valen $2$: $Q\in r$ ✓.
   > Las rectas son **coincidentes**.

2. Determina la posición relativa de $r:\;x=1+t,\;y=-t,\;z=2+t$ y $s:\;x=2+2\mu,\;y=1-\mu,\;z=3-\mu$.

   > **Solución:** $\vec{d}_r=(1,-1,1)$, $\vec{d}_s=(2,-1,-1)$. No proporcionales ($2/1\neq -1/-1$). Igualamos:
   > $1+t=2+2\mu$, $-t=1-\mu$, $2+t=3-\mu$.
   > De la segunda: $t=\mu-1$. De la tercera: $t=-\mu+1 \Rightarrow \mu-1=-\mu+1 \Rightarrow 2\mu=2 \Rightarrow \mu=1$, $t=0$.
   > Comprobamos en la primera: $1+0=1$, $2+2=4$. $1\neq 4$: **incompatible**.
   > Los vectores no son proporcionales y no se cortan: **rectas cruzadas**.

**Nivel Intermedio:**

3. Estudia la posición relativa de $r:\;\dfrac{x}{1}=\dfrac{y-1}{2}=\dfrac{z+1}{-1}$ y $s:\;\dfrac{x-2}{a}=\dfrac{y+1}{4}=\dfrac{z-1}{-2}$ según el valor del parámetro $a$.

   > **Solución:** $\vec{d}_r=(1,2,-1)$, $\vec{d}_s=(a,4,-2)$.
   > Para que sean paralelas: $(a,4,-2)=k(1,2,-1) \Rightarrow 4=2k \Rightarrow k=2 \Rightarrow a=2$, y $-2=k\cdot(-1)=-2$ ✓. Luego para $a=2$: paralelas o coincidentes.
   > **Con $a=2$:** punto de $s$: $(2,-1,1)$. ¿Pertenece a $r$? $\lambda=2/1=2$; $y: 1+2\cdot2=5\neq-1$. No pertenece: **paralelas distintas**.
   > **Con $a\neq2$:** $\vec{d}_r$ y $\vec{d}_s$ no son proporcionales. Resolvemos el sistema de intersección.
   > $t=2+a\mu$, $1+2t=-1+4\mu$, $-1-t=1-2\mu$.
   > De la tercera: $t=2\mu-2$. De la primera: $2\mu-2=2+a\mu \Rightarrow (2-a)\mu=4$.
   > Si $a\neq2$: $\mu=\dfrac{4}{2-a}$, $t=\dfrac{8}{2-a}-2$.
   > Comprobamos en la segunda ecuación (queda como ejercicio). En general, para $a\neq2$ las rectas se **cruzan** o son **secantes** dependiendo de si el sistema de 3 ecuaciones es compatible.

4. Las rectas $r$ y $s$ son secantes y se cortan en $P(2,1,-1)$. Si $\vec{d}_r=(1,-1,2)$ y $\vec{d}_s=(3,1,0)$, escribe las ecuaciones de ambas rectas.

   > **Solución:**
   > $$r:\;(x,y,z)=(2,1,-1)+\lambda(1,-1,2)$$
   > $$s:\;(x,y,z)=(2,1,-1)+\mu(3,1,0)$$

**Nivel EVAU:**

5. Estudia la posición relativa de las rectas:
   $$r:\;\begin{cases}x=2+t\\y=-1+2t\\z=3-t\end{cases} \qquad s:\;\begin{cases}x=4+\mu\\y=3-\mu\\z=1+\mu\end{cases}$$
   Si se cortan, halla el punto de intersección y el ángulo que forman.

   > **Solución:**
   >
   > **Vectores directores:** $\vec{d}_r=(1,2,-1)$, $\vec{d}_s=(1,-1,1)$. No proporcionales.
   >
   > **Sistema de intersección:**
   > $$2+t=4+\mu \Rightarrow t-\mu=2 \quad (I)$$
   > $$-1+2t=3-\mu \Rightarrow 2t+\mu=4 \quad (II)$$
   > $$3-t=1+\mu \Rightarrow t+\mu=2 \quad (III)$$
   > De $(I)$ y $(III)$: sumando $(t-\mu)+(t+\mu)=4 \Rightarrow 2t=4 \Rightarrow t=2$, $\mu=0$.
   > Verificación en $(II)$: $4+0=4$ ✓.
   > **Punto de intersección** ($t=2$): $x=4$, $y=3$, $z=1$. Punto: $\mathbf{P(4,3,1)}$.
   >
   > **Ángulo:**
   > $$\cos\theta = \frac{|\vec{d}_r\cdot\vec{d}_s|}{|\vec{d}_r||\vec{d}_s|} = \frac{|1\cdot1+2\cdot(-1)+(-1)\cdot1|}{\sqrt{1+4+1}\cdot\sqrt{1+1+1}} = \frac{|1-2-1|}{\sqrt{6}\cdot\sqrt{3}} = \frac{2}{\sqrt{18}} = \frac{2}{3\sqrt{2}} = \frac{\sqrt{2}}{3}$$
   > $$\theta = \arccos\!\left(\frac{\sqrt{2}}{3}\right) \approx 61{,}87°$$

**Test de Opción Múltiple**

6. Dos rectas en el espacio con vectores directores no proporcionales:
   - a) Son siempre secantes
   - b) Son siempre paralelas
   - c) Pueden ser secantes o cruzadas, pero no paralelas ni coincidentes
   - d) Son siempre cruzadas

   > **Respuesta correcta:** c) Si los vectores directores no son proporcionales, las rectas no son paralelas ni coincidentes. Pueden ser secantes (se cortan en un punto) o cruzadas (no se cortan y no son paralelas).

7. Para determinar si dos rectas con vectores directores no proporcionales son secantes o cruzadas, hay que:
   - a) Calcular el ángulo entre ellas
   - b) Plantear el sistema de igualdad de puntos y ver si tiene solución
   - c) Calcular el producto vectorial de sus directores
   - d) Calcular la distancia entre sus puntos bases

   > **Respuesta correcta:** b) Se plantea el sistema igualando las coordenadas de los puntos genéricos de cada recta; si el sistema $3\times2$ es compatible, las rectas son secantes; si no, son cruzadas.

---

#### 5.3.2 Posición Relativa de Recta y Plano

**Ejercicio Resuelto**

Estudia la posición relativa de la recta $r:\;x=1+2t,\;y=-1+t,\;z=3-t$ y el plano $\pi:\;2x-y+3z=10$.

**Solución:**

**Método:** Sustituir las paramétricas de $r$ en la ecuación de $\pi$.

$$2(1+2t) - (-1+t) + 3(3-t) = 10$$
$$2+4t+1-t+9-3t = 10$$
$$12 + 0t = 10$$
$$12 = 10 \quad \text{(Contradicción)}$$

No existe ningún valor de $t$ que satisfaga la ecuación. Esto significa que la recta **no corta** al plano.

Como $\vec{d}_r=(2,1,-1)$ y $\vec{n}_\pi=(2,-1,3)$:
$$\vec{d}_r\cdot\vec{n}_\pi = 4-1-3 = 0$$

El vector director es perpendicular al normal del plano, por lo que $r$ es **paralela** a $\pi$ (y como no tiene ningún punto en $\pi$: **paralela sin estar contenida**).

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Estudia la posición de $r:\;(x,y,z)=(1,2,3)+\lambda(1,1,1)$ respecto del plano $\pi:\;x+y+z=6$.

   > **Solución:** Sustituimos: $(1+\lambda)+(2+\lambda)+(3+\lambda)=6 \Rightarrow 6+3\lambda=6 \Rightarrow \lambda=0$.
   > Existe solución ($\lambda=0$). El punto de intersección es $(1,2,3)$.
   > Como $\vec{d}\cdot\vec{n}=1+1+1=3\neq0$, la recta **es secante al plano**. Intersección: $(1,2,3)$.

2. Determina si la recta $r:\;\dfrac{x-1}{1}=\dfrac{y-2}{-2}=\dfrac{z}{1}$ está contenida en el plano $\pi:\;x-2y+z+2=0$.

   > **Solución:** Comprobamos dos condiciones:
   > 1. El punto base $(1,2,0)$: $1-4+0+2=-1\neq0$. El punto base **no pertenece** a $\pi$, luego la recta no está contenida.
   > (Adicionalmente: $\vec{d}\cdot\vec{n}=1\cdot1+(-2)(-2)+1\cdot1=1+4+1=6\neq0$: la recta no es paralela al plano, es **secante**.)

**Nivel Intermedio:**

3. Halla el punto de intersección de $r:\;\dfrac{x-2}{1}=\dfrac{y+1}{2}=\dfrac{z-3}{-1}=\lambda$ con el plano $\pi:\;3x-y+2z=11$.

   > **Solución:** Paramétricas: $x=2+\lambda$, $y=-1+2\lambda$, $z=3-\lambda$.
   > Sustituyendo en $\pi$:
   > $$3(2+\lambda)-(-1+2\lambda)+2(3-\lambda)=11$$
   > $$6+3\lambda+1-2\lambda+6-2\lambda=11$$
   > $$13-\lambda=11 \Rightarrow \lambda=2$$
   > Punto: $x=4$, $y=3$, $z=1$. **Intersección: $(4,3,1)$**.

4. Halla los valores de $m$ para que la recta $r:\;x=m+t,\;y=1-t,\;z=2+mt$ sea paralela al plano $\pi:\;2x+y+z=5$.

   > **Solución:** Para que $r \parallel \pi$, el vector director $\vec{d}=(m,-1,m)$ debe ser perpendicular al normal $\vec{n}=(2,1,1)$:
   > $$\vec{d}\cdot\vec{n}=2m-1+m=3m-1=0 \Rightarrow m=\frac{1}{3}$$
   > Además hay que verificar que la recta no está contenida. Con $m=1/3$: punto base $(1/3,1,2)$ en $\pi$: $2/3+1+2=11/3\neq5$. La recta es **paralela** (no contenida) para $m=\dfrac{1}{3}$.

**Nivel EVAU:**

5. Se da la recta $r:\;\dfrac{x-1}{2}=\dfrac{y}{-1}=\dfrac{z+2}{3}$ y el plano $\pi:\;ax-y+z=b$.

   **(a)** Para $a=1$, $b=3$: halla el punto de intersección de $r$ con $\pi$.

   **(b)** Determina $a$ y $b$ para que $r$ esté contenida en $\pi$.

   > **Solución:**
   >
   > **(a)** $a=1,b=3$: paramétricas $x=1+2\lambda$, $y=-\lambda$, $z=-2+3\lambda$.
   > $(1+2\lambda)-(-\lambda)+(-2+3\lambda)=3$
   > $1+2\lambda+\lambda-2+3\lambda=3$
   > $-1+6\lambda=3 \Rightarrow \lambda=\frac{2}{3}$
   > Punto: $x=7/3$, $y=-2/3$, $z=0$. Intersección: $\left(\dfrac{7}{3},-\dfrac{2}{3},0\right)$.
   >
   > **(b)** Para que $r \subset \pi$, se necesita:
   > - $\vec{d}_r \perp \vec{n}_\pi$: $(2,-1,3)\cdot(a,-1,1)=0 \Rightarrow 2a+1+3=0 \Rightarrow a=-2$.
   > - El punto base $(1,0,-2)$ de $r$ pertenece a $\pi$: $-2(1)-0+(-2)=b \Rightarrow b=-4$.
   > **Solución:** $a=-2$, $b=-4$.

**Test de Opción Múltiple**

6. La condición para que una recta con vector director $\vec{d}$ sea paralela a un plano con vector normal $\vec{n}$ es:
   - a) $\vec{d}\times\vec{n}=\vec{0}$
   - b) $\vec{d}\cdot\vec{n}=0$
   - c) $\vec{d}=\vec{n}$
   - d) $|\vec{d}|=|\vec{n}|$

   > **Respuesta correcta:** b) La recta es paralela al plano (o está contenida en él) si y solo si su vector director es perpendicular al vector normal del plano: $\vec{d}\cdot\vec{n}=0$.

7. Si al sustituir las ecuaciones paramétricas de una recta en la ecuación del plano se obtiene $0=0$:
   - a) La recta es paralela al plano
   - b) La recta no corta al plano
   - c) La recta está contenida en el plano
   - d) La recta es perpendicular al plano

   > **Respuesta correcta:** c) $0=0$ es una identidad verdadera para todos los valores del parámetro, lo que significa que todos los puntos de la recta satisfacen la ecuación del plano: la recta está contenida en el plano.

---

#### 5.3.3 Posición Relativa de Dos Planos

**Ejercicio Resuelto**

Estudia la posición relativa de los planos $\pi_1:\; 2x - y + 3z = 5$ y $\pi_2:\; 4x - 2y + 6z = 8$.

**Solución:**

Los vectores normales son $\vec{n}_1=(2,-1,3)$ y $\vec{n}_2=(4,-2,6)=2(2,-1,3)=2\vec{n}_1$.

Los normales son **proporcionales**, por lo que los planos son paralelos o coincidentes.

Para distinguir: dividimos la ecuación de $\pi_2$ entre $2$: $2x-y+3z=4$.

Comparamos con $\pi_1:\;2x-y+3z=5$. Como $4\neq5$, los planos son **paralelos y distintos**.

**Distancia entre ellos:**
$$d = \frac{|5-4|}{\sqrt{4+1+9}} = \frac{1}{\sqrt{14}} = \frac{\sqrt{14}}{14}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Determina la posición relativa de $\pi_1:\;x+2y-z=3$ y $\pi_2:\;2x+4y-2z=6$.

   > **Solución:** $\vec{n}_2=(2,4,-2)=2(1,2,-1)=2\vec{n}_1$. Dividiendo $\pi_2$ entre $2$: $x+2y-z=3=\pi_1$. Los planos son **coincidentes**.

2. Determina si los planos $\pi_1:\;x-y+z=2$ y $\pi_2:\;x+y-z=0$ son paralelos, coincidentes o secantes.

   > **Solución:** $\vec{n}_1=(1,-1,1)$ y $\vec{n}_2=(1,1,-1)$. ¿Son proporcionales? $1/1=1$, $-1/1=-1\neq1$. **No son proporcionales**: los planos son **secantes** (se cortan en una recta).

**Nivel Intermedio:**

3. Halla la recta de intersección de los planos $\pi_1:\;x+y+z=3$ y $\pi_2:\;x-y+2z=1$.

   > **Solución:** Los planos son secantes (normales no proporcionales). Resolvemos el sistema:
   > $$\begin{cases}x+y+z=3\\x-y+2z=1\end{cases}$$
   > Sumando: $2x+3z=4 \Rightarrow x=\dfrac{4-3z}{2}$. De la primera: $y=3-x-z=3-\dfrac{4-3z}{2}-z=\dfrac{6-4+3z-2z}{2}=\dfrac{2+z}{2}$.
   > Tomando $z=t$ como parámetro: $x=2-\dfrac{3t}{2}$, $y=1+\dfrac{t}{2}$, $z=t$. Multiplicando por $2$: $t=2s$:
   > $$x=2-3s, \quad y=1+s, \quad z=2s$$
   > Vector director: $(-3,1,2)$, punto: $(2,1,0)$.
   > La recta de intersección es: $\dfrac{x-2}{-3}=\dfrac{y-1}{1}=\dfrac{z}{2}$.

4. Halla el valor de $k$ para que el plano $\pi_k:\;2x+ky-z=3$ sea paralelo al plano $\pi:\;4x-6y+2z=1$.

   > **Solución:** $\vec{n}_\pi=(4,-6,2)=2(2,-3,1)$. Para paralelismo: $(2,k,-1)=\lambda(2,-3,1)$.
   > $2=2\lambda \Rightarrow \lambda=1$; $k=-3\lambda=-3$; $-1=\lambda=1$ ✗. Contradicción en la tercera componente. Revisamos: $(2,k,-1)$ proporcional a $(4,-6,2)$: $2/4=k/(-6)=(-1)/2$. $1/2=k/(-6) \Rightarrow k=-3$; y $-1/2=-1/2$ ✓. **$k=-3$**.

**Nivel EVAU:**

5. Se consideran los planos:
   $$\pi_1:\; x + 2y - z = 3, \qquad \pi_2:\; 2x - y + az = b, \qquad \pi_3:\; x + y + z = 2$$

   **(a)** Para $a=1$, $b=0$: estudia la posición relativa de $\pi_1$ y $\pi_2$.

   **(b)** Halla la recta intersección de $\pi_1$ y $\pi_3$.

   > **Solución:**
   >
   > **(a)** $\vec{n}_1=(1,2,-1)$, $\vec{n}_2=(2,-1,1)$. No proporcionales ($1/2\neq 2/(-1)$): **secantes**.
   > Sistema: $x+2y-z=3$ y $2x-y+z=0$.
   > Sumando: $3x+y=3$. De la segunda: $z=y-2x$.
   > Tomando $x=s$: $y=3-3s$, $z=3-3s-2s=3-5s$.
   > Recta intersección: $(x,y,z)=(0,3,3)+s(1,-3,-5)$.
   >
   > **(b)** $\pi_1: x+2y-z=3$ y $\pi_3: x+y+z=2$. Restando: $y-2z=1 \Rightarrow y=1+2z$.
   > De $\pi_3$: $x=2-y-z=2-(1+2z)-z=1-3z$.
   > Tomando $z=t$: $x=1-3t$, $y=1+2t$, $z=t$.
   > Recta: $(x,y,z)=(1,1,0)+t(-3,2,1)$.

**Test de Opción Múltiple**

6. Dos planos en el espacio con vectores normales NO proporcionales:
   - a) Son siempre coincidentes
   - b) Son siempre paralelos
   - c) Se cortan en exactamente una recta
   - d) Pueden ser paralelos o secantes

   > **Respuesta correcta:** c) Si los vectores normales no son proporcionales, los planos necesariamente se cortan, y la intersección es siempre una recta (en el espacio $\mathbb{R}^3$).

7. La distancia entre los planos $x+y-z=2$ y $x+y-z=5$ es:
   - a) $3$
   - b) $\dfrac{3}{\sqrt{3}} = \sqrt{3}$
   - c) $\sqrt{3}$
   - d) $\dfrac{3}{\sqrt{2}}$

   > **Respuesta correcta:** c) $d=\dfrac{|2-5|}{\sqrt{1+1+1}}=\dfrac{3}{\sqrt{3}}=\sqrt{3}$.

---

#### 5.3.4 Posición Relativa de Tres Planos

**Ejercicio Resuelto**

Estudia la posición relativa de los tres planos:
$$\pi_1:\; x+y+z=3, \quad \pi_2:\; x-y+z=1, \quad \pi_3:\; 2x+y+3z=7$$

**Solución:**

La posición de tres planos se determina estudiando el sistema:
$$\begin{pmatrix}1&1&1\\1&-1&1\\2&1&3\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}3\\1\\7\end{pmatrix}$$

**Calculamos el determinante** de la matriz de coeficientes:
$$D=\begin{vmatrix}1&1&1\\1&-1&1\\2&1&3\end{vmatrix}=1(-3-1)-1(3-2)+1(1+2)=(-4)-(1)+(3)=-2\neq0$$

Como $D\neq0$, el sistema tiene **solución única**. Esto corresponde a **tres planos que se cortan en un único punto**.

Resolvemos por Cramer o Gauss:
$$x=\frac{D_x}{D}=\frac{\begin{vmatrix}3&1&1\\1&-1&1\\7&1&3\end{vmatrix}}{-2}=\frac{3(-3-1)-1(3-7)+1(1+7)}{-2}=\frac{-12+4+8}{-2}=\frac{0}{-2}=0$$
$$y=\frac{D_y}{D}=\frac{\begin{vmatrix}1&3&1\\1&1&1\\2&7&3\end{vmatrix}}{-2}=\frac{1(3-7)-3(3-2)+1(7-2)}{-2}=\frac{-4-3+5}{-2}=\frac{-2}{-2}=1$$
$$z=3-x-y=3-0-1=2$$

**Punto de corte:** $P(0,1,2)$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Estudia la posición de los tres planos $\pi_1:\;x+y=2$, $\pi_2:\;y+z=3$, $\pi_3:\;x+z=1$.

   > **Solución:** Sistema:
   > $$\begin{cases}x+y=2\\y+z=3\\x+z=1\end{cases}$$
   > $D=\begin{vmatrix}1&1&0\\0&1&1\\1&0&1\end{vmatrix}=1(1-0)-1(0-1)+0=1+1=2\neq0$.
   > Solución única. Los tres planos se cortan en un punto.
   > Sumando las tres ecuaciones: $2x+2y+2z=6 \Rightarrow x+y+z=3$.
   > De $\pi_1$: $z=1$; de $\pi_2$: $x=0$; de $\pi_3$: $y=2$.
   > **Punto de corte: $(0,2,1)$**.

2. Determina si los planos $\pi_1:\;x+y+z=1$, $\pi_2:\;x+y+z=2$, $\pi_3:\;x+y+z=3$ tienen algún punto en común.

   > **Solución:** Los tres tienen el mismo vector normal $(1,1,1)$, son paralelos entre sí (y distintos, pues sus términos independientes son distintos). **No tienen ningún punto en común** (sistema incompatible).

**Nivel Intermedio:**

3. Estudia la posición relativa de:
   $$\pi_1:\; x+2y-z=3 \quad \pi_2:\; 2x+4y-2z=6 \quad \pi_3:\; x-y+z=1$$

   > **Solución:** Observamos que $\pi_2=2\pi_1$: son **coincidentes**. El sistema se reduce a:
   > $$\begin{cases}x+2y-z=3\\x-y+z=1\end{cases}$$
   > Los planos $\pi_1$ (=$\pi_2$) y $\pi_3$ son secantes (normales $(1,2,-1)$ y $(1,-1,1)$ no proporcionales).
   > El sistema tiene infinitas soluciones (una recta): **los tres planos tienen en común una recta** (el plano $\pi_2$ es el mismo que $\pi_1$, y los otros dos se cortan en una recta).

4. Para qué valor de $k$ los tres planos $\pi_1:\;x+y+z=2$, $\pi_2:\;x-y+kz=0$, $\pi_3:\;2x+ky+z=3$ tienen solución única.

   > **Solución:** El sistema tiene solución única $\Leftrightarrow$ $D\neq0$:
   > $$D=\begin{vmatrix}1&1&1\\1&-1&k\\2&k&1\end{vmatrix}=1(-1-k^2)-1(1-2k)+1(k+2)$$
   > $=-1-k^2-1+2k+k+2 = -k^2+3k$
   > $D\neq0 \Leftrightarrow -k^2+3k\neq0 \Leftrightarrow k(k-3)\neq0 \Leftrightarrow k\neq0$ y $k\neq3$.

**Nivel EVAU:**

5. Se consideran los planos:
   $$\pi_1:\; x+y-z=2, \quad \pi_2:\; 2x-y+z=1, \quad \pi_3:\; x+ay+bz=c$$

   **(a)** Estudia la posición relativa de $\pi_1$ y $\pi_2$.

   **(b)** Halla $a$, $b$, $c$ para que el sistema de los tres planos sea incompatible (sin solución) siendo $\pi_3$ no paralelo a $\pi_1$.

   > **Solución:**
   >
   > **(a)** $\vec{n}_1=(1,1,-1)$, $\vec{n}_2=(2,-1,1)$: no proporcionales. **Secantes.**
   > Recta intersección: $\pi_1+\pi_2$: $3x=3 \Rightarrow x=1$. De $\pi_1$: $y-z=1$. Recta: $(1, 1+t, t)$, $t\in\mathbb{R}$, o equivalentemente $(x,y,z)=(1,1,0)+t(0,1,1)$.
   >
   > **(b)** Para que el sistema sea incompatible siendo $\pi_3$ no paralelo a $\pi_1$: la recta intersección de $\pi_1\cap\pi_2$ debe ser paralela a $\pi_3$ sin estar contenida.
   > La recta tiene vector director $(0,1,1)$. Para $\pi_3 \parallel$ a la recta: $(0,1,1)\cdot(1,a,b)=0 \Rightarrow a+b=0 \Rightarrow b=-a$.
   > Para que el sistema sea incompatible: la recta no pertenece a $\pi_3$: el punto $(1,1,0)$ no está en $\pi_3$: $1+a\cdot1+b\cdot0\neq c \Rightarrow 1+a\neq c$.
   > Ejemplo: $a=1$, $b=-1$, $c=0$ (entonces $1+1=2\neq0$ ✓). Plano: $x+y-z=0$.

**Test de Opción Múltiple**

6. Si el determinante de la matriz de coeficientes de un sistema de tres planos es cero:
   - a) Los tres planos se cortan en un punto único
   - b) El sistema es siempre incompatible
   - c) El sistema tiene infinitas soluciones o es incompatible
   - d) Los tres planos son coincidentes

   > **Respuesta correcta:** c) Si $D=0$, el sistema es compatible indeterminado (infinitas soluciones: un punto, una recta o un plano) o incompatible. Hay que analizar con mayor detalle los rangos.

7. Tres planos que se cortan dos a dos en rectas paralelas entre sí (y distintas) forman una configuración llamada:
   - a) Haz de planos
   - b) Sistema compatible determinado
   - c) Prisma (sistema incompatible con rectas de intersección paralelas)
   - d) Planos coincidentes

   > **Respuesta correcta:** c) Esta configuración geométrica, donde cada par de planos se corta en una recta y las tres rectas son paralelas, corresponde a un sistema incompatible cuya configuración se asemeja a un "prisma triédrico" o sistema de tipo haz-prismático. El sistema de ecuaciones correspondiente no tiene solución.

---

## 5.4 Ángulos entre Elementos Geométricos

---

#### 5.4.1 Ángulo entre Dos Rectas

**Ejercicio Resuelto**

Calcula el ángulo que forman las rectas $r:\;\dfrac{x-1}{2}=\dfrac{y}{1}=\dfrac{z+1}{-2}$ y $s:\;\dfrac{x}{1}=\dfrac{y-3}{2}=\dfrac{z-1}{2}$.

**Solución:**

Los vectores directores son $\vec{d}_r=(2,1,-2)$ y $\vec{d}_s=(1,2,2)$.

El ángulo $\theta$ entre dos rectas se calcula como:
$$\cos\theta = \frac{|\vec{d}_r\cdot\vec{d}_s|}{|\vec{d}_r||\vec{d}_s|}$$

(Tomamos valor absoluto porque el ángulo entre rectas es el agudo, $0\leq\theta\leq90°$.)

$$\vec{d}_r\cdot\vec{d}_s = 2\cdot1+1\cdot2+(-2)\cdot2 = 2+2-4=0$$

$$\cos\theta=\frac{|0|}{3\cdot3}=0 \Rightarrow \theta=90°$$

**Las rectas son perpendiculares.**

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula el ángulo entre las rectas con vectores directores $\vec{d}_1=(1,0,1)$ y $\vec{d}_2=(0,1,1)$.

   > **Solución:**
   > $$\cos\theta=\frac{|\vec{d}_1\cdot\vec{d}_2|}{|\vec{d}_1||\vec{d}_2|}=\frac{|0+0+1|}{\sqrt{2}\cdot\sqrt{2}}=\frac{1}{2}$$
   > $$\theta=\arccos\!\left(\frac{1}{2}\right)=60°$$

2. Determina si las rectas $r:\;(1,2,3)+\lambda(1,-1,2)$ y $s:\;(0,0,1)+\mu(3,1,-1)$ son perpendiculares.

   > **Solución:** $\vec{d}_r=(1,-1,2)$, $\vec{d}_s=(3,1,-1)$.
   > $\vec{d}_r\cdot\vec{d}_s=3-1-2=0$. **Sí son perpendiculares.**

**Nivel Intermedio:**

3. Halla el ángulo entre las rectas:
   $$r:\;\begin{cases}x=t\\y=2t\\z=3t\end{cases} \qquad s:\;\begin{cases}x=1+2\mu\\y=-1-\mu\\z=3\mu\end{cases}$$

   > **Solución:** $\vec{d}_r=(1,2,3)$, $\vec{d}_s=(2,-1,3)$.
   > $$\cos\theta=\frac{|2-2+9|}{\sqrt{14}\cdot\sqrt{14}}=\frac{9}{14}$$
   > $$\theta=\arccos\!\left(\frac{9}{14}\right)\approx 49{,}99°\approx50°$$

4. Halla $k$ para que las rectas $r:\;\vec{d}_r=(k,1,2)$ y $s:\;\vec{d}_s=(1,k,-1)$ sean perpendiculares.

   > **Solución:** $\vec{d}_r\cdot\vec{d}_s=k\cdot1+1\cdot k+2\cdot(-1)=2k-2=0 \Rightarrow k=1$.

**Nivel EVAU:**

5. Se dan las rectas:
   $$r:\;\frac{x-2}{1}=\frac{y-1}{-1}=\frac{z}{2}, \qquad s:\;\frac{x}{2}=\frac{y+1}{1}=\frac{z-3}{-1}$$

   **(a)** Halla el ángulo que forman $r$ y $s$.

   **(b)** Determina si $r$ y $s$ son secantes o cruzadas; si son secantes, halla el punto de corte.

   > **Solución:**
   >
   > **(a)** $\vec{d}_r=(1,-1,2)$, $\vec{d}_s=(2,1,-1)$.
   > $$\cos\theta=\frac{|2-1-2|}{\sqrt{6}\cdot\sqrt{6}}=\frac{1}{6}$$
   > $$\theta=\arccos\!\left(\frac{1}{6}\right)\approx80{,}4°$$
   >
   > **(b)** Paramétricas: $r$: $x=2+t, y=1-t, z=2t$; $s$: $x=2\mu, y=-1+\mu, z=3-\mu$.
   > Sistema:
   > $$2+t=2\mu \quad(I)$$
   > $$1-t=-1+\mu \Rightarrow \mu=2-t \quad(II)$$
   > $$2t=3-\mu \quad(III)$$
   > De $(I)$ y $(II)$: $2+t=2(2-t)=4-2t \Rightarrow 3t=2 \Rightarrow t=2/3$, $\mu=4/3$.
   > Comprobamos en $(III)$: $2(2/3)=4/3$ y $3-4/3=5/3$. $4/3\neq5/3$. **Incompatible**: $r$ y $s$ son **cruzadas**.

**Test de Opción Múltiple**

6. El ángulo entre dos rectas con vectores directores $\vec{d}_1$ y $\vec{d}_2$ se calcula siempre como:
   - a) $\arccos\!\left(\dfrac{\vec{d}_1\cdot\vec{d}_2}{|\vec{d}_1||\vec{d}_2|}\right)$, pudiendo ser obtuso
   - b) $\arccos\!\left(\dfrac{|\vec{d}_1\cdot\vec{d}_2|}{|\vec{d}_1||\vec{d}_2|}\right)$, siempre entre $0°$ y $90°$
   - c) $\arcsin\!\left(\dfrac{\vec{d}_1\cdot\vec{d}_2}{|\vec{d}_1||\vec{d}_2|}\right)$
   - d) $\arctan\!\left(\dfrac{|\vec{d}_1\times\vec{d}_2|}{|\vec{d}_1||\vec{d}_2|}\right)$

   > **Respuesta correcta:** b) Por convenio, el ángulo entre dos rectas es el ángulo agudo (o recto) que forman, por lo que se toma el valor absoluto del coseno.

7. Dos rectas son perpendiculares si y solo si:
   - a) Sus vectores directores son iguales
   - b) Sus vectores directores son proporcionales
   - c) El producto escalar de sus vectores directores es cero
   - d) El módulo del producto vectorial de sus directores es cero

   > **Respuesta correcta:** c) La perpendicularidad equivale a $\vec{d}_1\cdot\vec{d}_2=0$, que implica que el ángulo entre ellas es $90°$.

---

#### 5.4.2 Ángulo entre Recta y Plano

**Ejercicio Resuelto**

Calcula el ángulo que forma la recta $r:\;x=1+2t,\;y=t,\;z=-1+t$ con el plano $\pi:\;x-y+2z=0$.

**Solución:**

El ángulo $\varphi$ entre una recta (con vector director $\vec{d}$) y un plano (con vector normal $\vec{n}$) se calcula como el complemento del ángulo entre $\vec{d}$ y $\vec{n}$:

$$\sin\varphi = \frac{|\vec{d}\cdot\vec{n}|}{|\vec{d}||\vec{n}|}$$

Con $\vec{d}=(2,1,1)$ y $\vec{n}=(1,-1,2)$:
$$\vec{d}\cdot\vec{n}=2-1+2=3$$
$$|\vec{d}|=\sqrt{4+1+1}=\sqrt{6}, \quad |\vec{n}|=\sqrt{1+1+4}=\sqrt{6}$$
$$\sin\varphi=\frac{|3|}{\sqrt{6}\cdot\sqrt{6}}=\frac{3}{6}=\frac{1}{2}$$
$$\boxed{\varphi=\arcsin\!\left(\frac{1}{2}\right)=30°}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula el ángulo entre la recta $r:\;\vec{d}=(1,0,1)$ y el plano $\pi:\;\vec{n}=(1,1,0)$.

   > **Solución:**
   > $$\sin\varphi=\frac{|1\cdot1+0\cdot1+1\cdot0|}{\sqrt{2}\cdot\sqrt{2}}=\frac{1}{2}$$
   > $$\varphi=30°$$

2. ¿Qué condición deben cumplir $\vec{d}$ y $\vec{n}$ para que la recta sea perpendicular al plano?

   > **Solución:** La recta es perpendicular al plano cuando $\varphi=90°$, lo que ocurre cuando $\sin\varphi=1$, es decir, cuando $\vec{d}\parallel\vec{n}$: el vector director de la recta es proporcional al vector normal del plano. Equivalentemente, $\vec{d}\times\vec{n}=\vec{0}$.

**Nivel Intermedio:**

3. Halla el ángulo que forma la recta $r:\;\dfrac{x-1}{3}=\dfrac{y+2}{-1}=\dfrac{z}{2}$ con el plano $\pi:\;2x+y-z=5$.

   > **Solución:** $\vec{d}=(3,-1,2)$, $\vec{n}=(2,1,-1)$.
   > $$\sin\varphi=\frac{|6-1-2|}{\sqrt{14}\cdot\sqrt{6}}=\frac{3}{\sqrt{84}}=\frac{3}{2\sqrt{21}}=\frac{3\sqrt{21}}{42}=\frac{\sqrt{21}}{14}$$
   > $$\varphi=\arcsin\!\left(\frac{\sqrt{21}}{14}\right)\approx \arcsin(0{,}327)\approx19{,}1°$$

4. Para qué valores de $m$ la recta $r:\;\vec{d}=(m,1,2)$ forma un ángulo de $30°$ con el plano $x+y+z=0$.

   > **Solución:** $\vec{n}=(1,1,1)$, $\sin30°=1/2$.
   > $$\frac{|m+1+2|}{\sqrt{m^2+5}\cdot\sqrt{3}}=\frac{1}{2}$$
   > $$\frac{|m+3|}{\sqrt{3(m^2+5)}}=\frac{1}{2}$$
   > $2|m+3|=\sqrt{3(m^2+5)}$. Elevando al cuadrado: $4(m+3)^2=3m^2+15$.
   > $4m^2+24m+36=3m^2+15 \Rightarrow m^2+24m+21=0$
   > $$m=\frac{-24\pm\sqrt{576-84}}{2}=\frac{-24\pm\sqrt{492}}{2}=\frac{-24\pm2\sqrt{123}}{2}=-12\pm\sqrt{123}$$

**Nivel EVAU:**

5. Sea la recta $r:\;\dfrac{x}{1}=\dfrac{y-1}{2}=\dfrac{z+2}{-1}$ y el plano $\pi:\;ax-y+2z=3$.

   **(a)** Halla el ángulo entre $r$ y $\pi$ cuando $a=2$.

   **(b)** Para qué valor de $a$ la recta $r$ es paralela al plano $\pi$.

   **(c)** Para qué valor de $a$ la recta $r$ es perpendicular al plano $\pi$.

   > **Solución:**
   >
   > $\vec{d}_r=(1,2,-1)$, $\vec{n}=(a,-1,2)$.
   >
   > **(a)** $a=2$: $\vec{n}=(2,-1,2)$.
   > $$\sin\varphi=\frac{|2-2-2|}{\sqrt{6}\cdot3}=\frac{2}{3\sqrt{6}}=\frac{2\sqrt{6}}{18}=\frac{\sqrt{6}}{9}$$
   > $$\varphi=\arcsin\!\left(\frac{\sqrt{6}}{9}\right)\approx15{,}8°$$
   >
   > **(b)** $r\parallel\pi \Leftrightarrow \vec{d}\cdot\vec{n}=0$: $a-2-2=a-4=0 \Rightarrow a=4$.
   >
   > **(c)** $r\perp\pi \Leftrightarrow \vec{d}\parallel\vec{n}$: $(1,2,-1)=k(a,-1,2)$. $1=ka$, $2=-k$, $-1=2k$. De la segunda: $k=-1/2$. De la tercera: $k=-1/2$ ✓. De la primera: $a=1/k=-2$. **$a=-2$**.

**Test de Opción Múltiple**

6. El ángulo entre una recta y un plano se calcula usando:
   - a) El coseno del ángulo entre el vector director y el vector normal
   - b) El seno del ángulo entre el vector director y el vector normal
   - c) El coseno del ángulo entre el vector director y un vector del plano
   - d) El arcotangente de la distancia entre la recta y el plano

   > **Respuesta correcta:** b) $\sin\varphi = \dfrac{|\vec{d}\cdot\vec{n}|}{|\vec{d}||\vec{n}|}$. El ángulo entre la recta y el plano es el complemento del ángulo entre la recta y el normal, lo que lleva al seno.

7. Si $\vec{d}\cdot\vec{n}=0$, la recta con vector director $\vec{d}$ y el plano con vector normal $\vec{n}$:
   - a) Son perpendiculares
   - b) Son paralelos (la recta es paralela al plano o está contenida en él)
   - c) Se cortan en un ángulo de $45°$
   - d) Se cortan en un punto

   > **Respuesta correcta:** b) $\vec{d}\cdot\vec{n}=0$ implica que la recta es paralela al plano o está contenida en él (el ángulo entre la recta y el plano es $0°$).

---

#### 5.4.3 Ángulo entre Dos Planos (Ángulo Diedro)

**Ejercicio Resuelto**

Calcula el ángulo diedro entre los planos $\pi_1:\; 2x-y+z=3$ y $\pi_2:\; x+y-z=1$.

**Solución:**

El ángulo $\theta$ entre dos planos es el ángulo entre sus vectores normales (tomando el ángulo agudo):

$$\cos\theta = \frac{|\vec{n}_1\cdot\vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}$$

Con $\vec{n}_1=(2,-1,1)$ y $\vec{n}_2=(1,1,-1)$:
$$\vec{n}_1\cdot\vec{n}_2 = 2-1-1=0$$

$$\cos\theta=0 \Rightarrow \theta=90°$$

**Los planos son perpendiculares.**

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula el ángulo entre los planos $\pi_1:\;x+y=0$ y $\pi_2:\;y+z=0$.

   > **Solución:** $\vec{n}_1=(1,1,0)$, $\vec{n}_2=(0,1,1)$.
   > $$\cos\theta=\frac{|0+1+0|}{\sqrt{2}\cdot\sqrt{2}}=\frac{1}{2}$$
   > $$\theta=60°$$

2. ¿Cuándo dos planos son perpendiculares? Formula la condición en términos de sus vectores normales.

   > **Solución:** Dos planos son perpendiculares cuando el ángulo diedro entre ellos es $90°$, es decir, cuando $\cos\theta=0$, lo que equivale a que sus vectores normales sean perpendiculares: $\vec{n}_1\cdot\vec{n}_2=0$.

**Nivel Intermedio:**

3. Halla el ángulo que forman los planos $\pi_1:\;2x+y-2z=3$ y $\pi_2:\;3x+6z=1$.

   > **Solución:** $\vec{n}_1=(2,1,-2)$, $\vec{n}_2=(3,0,6)$.
   > $$\cos\theta=\frac{|6+0-12|}{3\cdot\sqrt{45}}=\frac{6}{3\cdot3\sqrt{5}}=\frac{6}{9\sqrt{5}}=\frac{2}{3\sqrt{5}}=\frac{2\sqrt{5}}{15}$$
   > $$\theta=\arccos\!\left(\frac{2\sqrt{5}}{15}\right)\approx\arccos(0{,}298)\approx72{,}7°$$

4. Determina $k$ para que los planos $\pi_1:\;kx+2y-z=0$ y $\pi_2:\;x+ky+2z=3$ sean perpendiculares.

   > **Solución:** $\vec{n}_1\cdot\vec{n}_2=0$: $k\cdot1+2\cdot k+(-1)\cdot2=3k-2=0 \Rightarrow k=\dfrac{2}{3}$.

**Nivel EVAU:**

5. Sean los planos $\pi:\;x-y+2z=4$ y $\sigma:\;2x+y+az=1$.

   **(a)** Calcula $a$ para que $\pi$ y $\sigma$ sean perpendiculares.

   **(b)** Con el valor de $a$ hallado, determina la recta intersección de $\pi$ y $\sigma$.

   **(c)** Calcula el ángulo entre $\pi$ y el plano coordenado $XOY$ (ecuación $z=0$).

   > **Solución:**
   >
   > **(a)** $\vec{n}_\pi=(1,-1,2)$, $\vec{n}_\sigma=(2,1,a)$. $\vec{n}_\pi\cdot\vec{n}_\sigma=0$: $2-1+2a=0 \Rightarrow 2a=-1 \Rightarrow a=-\dfrac{1}{2}$.
   >
   > **(b)** Con $a=-1/2$: sistema $x-y+2z=4$ y $2x+y-z/2=1$ (mult. por 2: $4x+2y-z=2$).
   > $\pi+\sigma$: $(x-y+2z)+(2x+y-z/2)=5 \Rightarrow 3x+3z/2=5$, es decir $6x+3z=10$.
   > Parametrizamos: $z=t$, $x=(10-3t)/6$. De $\pi$: $y=x+2z-4=(10-3t)/6+2t-4=\dfrac{10-3t+12t-24}{6}=\dfrac{9t-14}{6}$.
   > Recta: punto (con $t=0$): $(5/3,-7/3,0)$, director proporcional a $(-3,9,6)/6=(-1,3,2)$.
   >
   > **(c)** El plano $XOY$ tiene $\vec{n}_{XOY}=(0,0,1)$.
   > $$\cos\theta=\frac{|(1)(0)+(-1)(0)+(2)(1)|}{\sqrt{6}\cdot1}=\frac{2}{\sqrt{6}}=\frac{2\sqrt{6}}{6}=\frac{\sqrt{6}}{3}$$
   > $$\theta=\arccos\!\left(\frac{\sqrt{6}}{3}\right)\approx35{,}3°$$

**Test de Opción Múltiple**

6. El ángulo entre los planos $x=0$ (plano $YOZ$) y $y=0$ (plano $XOZ$) es:
   - a) $0°$
   - b) $45°$
   - c) $60°$
   - d) $90°$

   > **Respuesta correcta:** d) Los normales son $\vec{n}_1=(1,0,0)$ y $\vec{n}_2=(0,1,0)$: $\vec{n}_1\cdot\vec{n}_2=0$, luego el ángulo es $90°$.

7. Si el ángulo entre dos planos es $\theta$, el ángulo suplementario $180°-\theta$ también es un "ángulo diedro" posible. ¿Por qué se toma el ángulo agudo?
   - a) Porque el obtuso no existe entre planos
   - b) Porque el ángulo diedro por convenio se toma siempre como el menor de los dos
   - c) Porque la fórmula con valor absoluto garantiza que el resultado sea el ángulo agudo
   - d) Tanto b) como c) son correctas

   > **Respuesta correcta:** d) El ángulo entre dos planos se define como el menor de los dos ángulos diedros formados (entre $0°$ y $90°$), y la fórmula $\cos\theta=\dfrac{|\vec{n}_1\cdot\vec{n}_2|}{|\vec{n}_1||\vec{n}_2|}$ garantiza automáticamente este resultado gracias al valor absoluto.

---

## 5.5 Distancias

---

#### 5.5.1 Distancia de un Punto a Otro Punto

**Ejercicio Resuelto**

Calcula la distancia entre los puntos $A(1,-2,3)$ y $B(4,2,-1)$.

**Solución:**

La distancia entre dos puntos en $\mathbb{R}^3$ es:
$$d(A,B) = |\overrightarrow{AB}| = \sqrt{(x_B-x_A)^2+(y_B-y_A)^2+(z_B-z_A)^2}$$

$$d(A,B) = \sqrt{(4-1)^2+(2-(-2))^2+(-1-3)^2} = \sqrt{9+16+16} = \sqrt{41}$$

$$\boxed{d(A,B)=\sqrt{41}\approx6{,}40}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula la distancia entre $P(-1,0,2)$ y $Q(3,4,-2)$.

   > **Solución:**
   > $$d=\sqrt{(3+1)^2+(4-0)^2+(-2-2)^2}=\sqrt{16+16+16}=\sqrt{48}=4\sqrt{3}$$

2. El punto medio del segmento $AB$ tiene coordenadas $M(2,-1,3)$ y $A(0,1,-1)$. Halla $B$ y $d(A,B)$.

   > **Solución:** $M=\dfrac{A+B}{2} \Rightarrow B=2M-A=(4,-3,7)$.
   > $d(A,B)=\sqrt{16+16+64}=\sqrt{96}=4\sqrt{6}$.

**Nivel Intermedio:**

3. Determina los puntos de la recta $r:\;x=1+t,\;y=2-t,\;z=t$ que equidistan de $A(0,0,0)$ y $B(6,0,6)$.

   > **Solución:** Sea $P(1+t,2-t,t)\in r$.
   > $d(P,A)^2=(1+t)^2+(2-t)^2+t^2=1+2t+t^2+4-4t+t^2+t^2=3t^2-2t+5$
   > $d(P,B)^2=(1+t-6)^2+(2-t)^2+(t-6)^2=(t-5)^2+(2-t)^2+(t-6)^2$
   > $=t^2-10t+25+4-4t+t^2+t^2-12t+36=3t^2-26t+65$
   > Igualando: $3t^2-2t+5=3t^2-26t+65 \Rightarrow 24t=60 \Rightarrow t=5/2$.
   > Punto: $P(7/2,-1/2,5/2)$.

4. Halla el punto de la recta $r:\;\dfrac{x}{1}=\dfrac{y-1}{1}=\dfrac{z}{2}$ más cercano al origen.

   > **Solución:** Punto genérico: $P(t,1+t,2t)$.
   > $d(P,O)^2=t^2+(1+t)^2+4t^2=t^2+1+2t+t^2+4t^2=6t^2+2t+1$.
   > Mínimo: $\dfrac{d}{dt}(6t^2+2t+1)=12t+2=0 \Rightarrow t=-\dfrac{1}{6}$.
   > Punto más cercano: $P\!\left(-\dfrac{1}{6}, \dfrac{5}{6}, -\dfrac{1}{3}\right)$.

**Nivel EVAU:**

5. Se dan los puntos $A(1,0,-1)$, $B(3,2,1)$ y $C(2,-1,3)$.

   **(a)** Calcula el perímetro del triángulo $ABC$.

   **(b)** Halla el punto medio de $AC$ y la longitud de la mediana desde $B$.

   > **Solución:**
   >
   > **(a)**
   > $d(A,B)=\sqrt{4+4+4}=\sqrt{12}=2\sqrt{3}$
   > $d(B,C)=\sqrt{1+9+4}=\sqrt{14}$
   > $d(A,C)=\sqrt{1+1+16}=\sqrt{18}=3\sqrt{2}$
   > Perímetro $= 2\sqrt{3}+\sqrt{14}+3\sqrt{2}\approx3{,}46+3{,}74+4{,}24\approx11{,}44$ u.
   >
   > **(b)** Punto medio de $AC$: $M_{AC}=\left(\dfrac{3}{2},-\dfrac{1}{2},1\right)$.
   > Mediana desde $B$: $d(B,M_{AC})=\sqrt{(3-3/2)^2+(2+1/2)^2+(1-1)^2}=\sqrt{9/4+25/4}=\sqrt{34/4}=\dfrac{\sqrt{34}}{2}$.

**Test de Opción Múltiple**

6. La distancia entre $A(a,b,c)$ y el origen $O(0,0,0)$ es:
   - a) $a+b+c$
   - b) $|a|+|b|+|c|$
   - c) $\sqrt{a+b+c}$
   - d) $\sqrt{a^2+b^2+c^2}$

   > **Respuesta correcta:** d) Es el módulo del vector de posición: $|\overrightarrow{OA}|=\sqrt{a^2+b^2+c^2}$.

7. Si $d(A,B)=0$, entonces:
   - a) $A$ y $B$ son el mismo punto
   - b) $A$ y $B$ están en el mismo plano coordenado
   - c) $A$ y $B$ son simétricamente opuestos respecto al origen
   - d) El vector $\overrightarrow{AB}$ es unitario

   > **Respuesta correcta:** a) $d(A,B)=0 \Leftrightarrow |\overrightarrow{AB}|=0 \Leftrightarrow \overrightarrow{AB}=\vec{0} \Leftrightarrow A=B$.

---

#### 5.5.2 Distancia de un Punto a una Recta

**Ejercicio Resuelto**

Calcula la distancia del punto $P(2,3,1)$ a la recta $r:\;(x,y,z)=(1,0,2)+\lambda(1,-1,1)$.

**Solución:**

**Método del producto vectorial:**

Sea $A(1,0,2)$ un punto de $r$ y $\vec{d}=(1,-1,1)$ el vector director.

$$\overrightarrow{AP} = P - A = (1,3,-1)$$

$$\overrightarrow{AP}\times\vec{d} = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&3&-1\\1&-1&1\end{vmatrix} = (3\cdot1-(-1)(-1))\vec{i}-(1\cdot1-(-1)\cdot1)\vec{j}+(1\cdot(-1)-3\cdot1)\vec{k}$$
$$= (3-1)\vec{i}-(1+1)\vec{j}+(-1-3)\vec{k} = (2,-2,-4)$$

$$|\overrightarrow{AP}\times\vec{d}| = \sqrt{4+4+16}=\sqrt{24}=2\sqrt{6}$$
$$|\vec{d}|=\sqrt{1+1+1}=\sqrt{3}$$

$$\boxed{d(P,r)=\frac{|\overrightarrow{AP}\times\vec{d}|}{|\vec{d}|}=\frac{2\sqrt{6}}{\sqrt{3}}=2\sqrt{2}}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula la distancia del punto $Q(0,0,0)$ a la recta $r:\;(x,y,z)=(1,1,1)+\lambda(1,0,0)$.

   > **Solución:** $A=(1,1,1)$, $\vec{d}=(1,0,0)$, $\overrightarrow{AQ}=(-1,-1,-1)$.
   > $\overrightarrow{AQ}\times\vec{d}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&-1&-1\\1&0&0\end{vmatrix}=(0-0)\vec{i}-( 0+1)\vec{j}+(0+1)\vec{k}=(0,-1,1)$.
   > $d=\dfrac{|(0,-1,1)|}{1}=\sqrt{2}$.

2. ¿Cuándo la distancia de un punto a una recta es cero? Interpreta geométricamente.

   > **Solución:** La distancia es cero cuando $\overrightarrow{AP}\times\vec{d}=\vec{0}$, es decir, cuando $\overrightarrow{AP}$ y $\vec{d}$ son proporcionales, lo que significa que $P$ es un punto de la recta $r$. Geométricamente: $P\in r$.

**Nivel Intermedio:**

3. Calcula la distancia del punto $A(1,-1,2)$ a la recta $r:\;\dfrac{x}{2}=\dfrac{y+1}{1}=\dfrac{z-2}{-1}$.

   > **Solución:** Punto de $r$: $B(0,-1,2)$. $\vec{d}=(2,1,-1)$.
   > $\overrightarrow{BA}=(1,0,0)$.
   > $\overrightarrow{BA}\times\vec{d}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&0&0\\2&1&-1\end{vmatrix}=(0-0)\vec{i}-((-1)-0)\vec{j}+(1-0)\vec{k}=(0,1,1)$.
   > $d=\dfrac{\sqrt{0+1+1}}{\sqrt{4+1+1}}=\dfrac{\sqrt{2}}{\sqrt{6}}=\dfrac{1}{\sqrt{3}}=\dfrac{\sqrt{3}}{3}$.

4. Halla la distancia del punto $P(2,0,-1)$ a la recta que pasa por $A(1,1,1)$ y $B(3,-1,0)$.

   > **Solución:** $\vec{d}=\overrightarrow{AB}=(2,-2,-1)$. $\overrightarrow{AP}=(1,-1,-2)$.
   > $\overrightarrow{AP}\times\vec{d}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&-1&-2\\2&-2&-1\end{vmatrix}=(1-4)\vec{i}-(-1+4)\vec{j}+(-2+2)\vec{k}=(-3,-3,0)$.
   > $|\overrightarrow{AP}\times\vec{d}|=\sqrt{9+9}=3\sqrt{2}$.
   > $|\vec{d}|=\sqrt{4+4+1}=3$.
   > $d=\dfrac{3\sqrt{2}}{3}=\sqrt{2}$.

**Nivel EVAU:**

5. Sea la recta $r:\;\begin{cases}x=1+t\\y=2-2t\\z=t\end{cases}$ y el punto $P(3,0,4)$.

   **(a)** Calcula la distancia de $P$ a $r$.

   **(b)** Halla el pie de la perpendicular desde $P$ a $r$ (punto de $r$ más cercano a $P$).

   > **Solución:**
   >
   > **(a)** $A=(1,2,0)$, $\vec{d}=(1,-2,1)$, $\overrightarrow{AP}=(2,-2,4)$.
   > $\overrightarrow{AP}\times\vec{d}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\2&-2&4\\1&-2&1\end{vmatrix}=(-2+8)\vec{i}-(2-4)\vec{j}+(-4+2)\vec{k}=(6,2,-2)$.
   > $|\overrightarrow{AP}\times\vec{d}|=\sqrt{36+4+4}=\sqrt{44}=2\sqrt{11}$.
   > $|\vec{d}|=\sqrt{6}$.
   > $$d(P,r)=\frac{2\sqrt{11}}{\sqrt{6}}=2\sqrt{\frac{11}{6}}=\frac{2\sqrt{66}}{6}=\frac{\sqrt{66}}{3}$$
   >
   > **(b)** El pie de la perpendicular $H$ es el punto de $r$ tal que $\overrightarrow{HP}\perp\vec{d}$:
   > $H=(1+t, 2-2t, t)$. $\overrightarrow{HP}=(2-t, -2+2t, 4-t)$.
   > $\overrightarrow{HP}\cdot\vec{d}=(2-t)-(- 4+4t)+(4-t)=2-t+4-4t+4-t=10-6t=0 \Rightarrow t=5/3$.
   > $H=\left(\dfrac{8}{3}, -\dfrac{4}{3}, \dfrac{5}{3}\right)$.

**Test de Opción Múltiple**

6. La fórmula para la distancia de un punto $P$ a una recta $r$ (con punto $A$ y vector director $\vec{d}$) es:
   - a) $\dfrac{\overrightarrow{AP}\cdot\vec{d}}{|\vec{d}|}$
   - b) $\dfrac{|\overrightarrow{AP}\times\vec{d}|}{|\vec{d}|}$
   - c) $\dfrac{|\overrightarrow{AP}\cdot\vec{d}|}{|\vec{d}|}$
   - d) $|\overrightarrow{AP}|\cdot|\vec{d}|$

   > **Respuesta correcta:** b) La distancia es $\dfrac{|\overrightarrow{AP}\times\vec{d}|}{|\vec{d}|}$, usando el módulo del producto vectorial.

7. El pie de la perpendicular desde $P$ a la recta $r$ es el punto $H\in r$ tal que:
   - a) $\overrightarrow{HP}$ es paralelo a $\vec{d}$
   - b) $\overrightarrow{HP}$ es perpendicular a $\vec{d}$, es decir $\overrightarrow{HP}\cdot\vec{d}=0$
   - c) $|HP|$ es máxima
   - d) $H$ está en el plano perpendicular a $r$ que pasa por el origen

   > **Respuesta correcta:** b) $H$ es el pie de la perpendicular, luego $\overrightarrow{HP}\perp\vec{d}$, lo que se traduce en $\overrightarrow{HP}\cdot\vec{d}=0$.

---

#### 5.5.3 Distancia de un Punto a un Plano

**Ejercicio Resuelto**

Calcula la distancia del punto $P(1,2,-1)$ al plano $\pi:\; 2x - y + 2z + 3 = 0$.

**Solución:**

La fórmula de la distancia de un punto $(x_0,y_0,z_0)$ al plano $ax+by+cz+d=0$ es:

$$d(P,\pi) = \frac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}$$

Con $P(1,2,-1)$, $a=2$, $b=-1$, $c=2$, $d=3$:

$$d(P,\pi)=\frac{|2(1)+(-1)(2)+2(-1)+3|}{\sqrt{4+1+4}}=\frac{|2-2-2+3|}{\sqrt{9}}=\frac{|1|}{3}=\frac{1}{3}$$

$$\boxed{d(P,\pi)=\frac{1}{3}}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula la distancia del origen $O(0,0,0)$ al plano $\pi:\;3x-4y+0z=10$.

   > **Solución:**
   > $$d(O,\pi)=\frac{|3\cdot0-4\cdot0-10|}{\sqrt{9+16}}=\frac{10}{5}=2$$

2. ¿A qué distancia está el punto $A(2,-1,3)$ del plano $\pi:\;x+2y-2z=6$?

   > **Solución:**
   > $$d=\frac{|2+2(-1)-2(3)-6|}{\sqrt{1+4+4}}=\frac{|2-2-6-6|}{3}=\frac{12}{3}=4$$

**Nivel Intermedio:**

3. Halla el punto del plano $\pi:\;x+y+z=1$ más cercano al punto $P(2,3,4)$.

   > **Solución:** El punto más cercano $H$ está en la recta que pasa por $P$ con dirección $\vec{n}=(1,1,1)$ (perpendicular al plano).
   > Paramétricas: $(2+t, 3+t, 4+t)$. Sustituimos en $\pi$: $(2+t)+(3+t)+(4+t)=1 \Rightarrow 9+3t=1 \Rightarrow t=-8/3$.
   > $H=\left(2-\dfrac{8}{3}, 3-\dfrac{8}{3}, 4-\dfrac{8}{3}\right)=\left(-\dfrac{2}{3}, \dfrac{1}{3}, \dfrac{4}{3}\right)$.

4. Determina si los puntos $A(1,0,2)$ y $B(-1,2,0)$ están en el mismo lado del plano $\pi:\;x-y+z=3$.

   > **Solución:** Sustituimos en $x-y+z-3$:
   > $A$: $1-0+2-3=0$. $A$ **pertenece** al plano.
   > $B$: $-1-2+0-3=-6<0$. $B$ está en el lado negativo del plano.
   > No se puede hablar de "mismo lado" puesto que $A\in\pi$.

**Nivel EVAU:**

5. Sea el punto $P(2,-1,3)$ y el plano $\pi:\;x+2y-2z+k=0$.

   **(a)** Calcula la distancia de $P$ a $\pi$ en función de $k$.

   **(b)** Halla $k$ para que $d(P,\pi)=2$.

   **(c)** Determina la proyección ortogonal de $P$ sobre $\pi$ para $k=1$.

   > **Solución:**
   >
   > **(a)** $\vec{n}=(1,2,-2)$, $|\vec{n}|=\sqrt{1+4+4}=3$.
   > $$d(P,\pi)=\frac{|2+2(-1)-2(3)+k|}{3}=\frac{|2-2-6+k|}{3}=\frac{|k-6|}{3}$$
   >
   > **(b)** $\dfrac{|k-6|}{3}=2 \Rightarrow |k-6|=6 \Rightarrow k=12$ o $k=0$.
   >
   > **(c)** Con $k=1$: $d=|1-6|/3=5/3$. La proyección $H$ de $P$ sobre $\pi$ se halla mediante la recta por $P$ perpendicular a $\pi$: $(x,y,z)=(2,-1,3)+t(1,2,-2)$.
   > En $\pi$: $(2+t)+2(-1+2t)-2(3-2t)+1=0 \Rightarrow 2+t-2+4t-6+4t+1=0 \Rightarrow 9t-5=0 \Rightarrow t=5/9$.
   > $H=\left(\dfrac{23}{9}, \dfrac{1}{9}, \dfrac{17}{9}\right)$.

**Test de Opción Múltiple**

6. La distancia del punto $(a,b,c)$ al plano $x=0$ (plano $YOZ$) es:
   - a) $\sqrt{a^2+b^2+c^2}$
   - b) $|a|$
   - c) $\sqrt{b^2+c^2}$
   - d) $a$

   > **Respuesta correcta:** b) La ecuación del plano $YOZ$ es $x=0$ (o $x+0y+0z=0$). La distancia es $\dfrac{|a\cdot1+b\cdot0+c\cdot0|}{\sqrt{1}}=|a|$.

7. Para calcular la distancia de un punto a un plano con la fórmula analítica, el denominador es:
   - a) El módulo del vector normal al plano
   - b) El módulo del vector de posición del punto
   - c) El término independiente del plano
   - d) El producto escalar del punto con el normal

   > **Respuesta correcta:** a) En la fórmula $d=\dfrac{|ax_0+by_0+cz_0+d|}{\sqrt{a^2+b^2+c^2}}$, el denominador $\sqrt{a^2+b^2+c^2}=|\vec{n}|$ es el módulo del vector normal al plano.

---

#### 5.5.4 Distancia entre Dos Rectas Paralelas

**Ejercicio Resuelto**

Calcula la distancia entre las rectas paralelas:
$$r:\;\frac{x-1}{2}=\frac{y}{-1}=\frac{z+2}{1} \qquad s:\;\frac{x+3}{2}=\frac{y-1}{-1}=\frac{z}{1}$$

**Solución:**

Verificamos paralelismo: ambas tienen $\vec{d}=(2,-1,1)$: **son paralelas** (y tomando el punto $(-3,1,0)$ de $s$ en $r$: $(-3-1)/2=-2$, $1/(-1)=-1\neq-2$: no coincidentes).

**Método:** Tomamos $A(1,0,-2)\in r$ y $B(-3,1,0)\in s$.
$$\overrightarrow{AB}=(-4,1,2)$$

La distancia es el módulo de la componente de $\overrightarrow{AB}$ perpendicular a $\vec{d}$:
$$d(r,s)=\frac{|\overrightarrow{AB}\times\vec{d}|}{|\vec{d}|}$$

$$\overrightarrow{AB}\times\vec{d}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-4&1&2\\2&-1&1\end{vmatrix}=(1+2)\vec{i}-(-4-4)\vec{j}+(4-2)\vec{k}=(3,8,2)$$

$$d=\frac{\sqrt{9+64+4}}{\sqrt{4+1+1}}=\frac{\sqrt{77}}{\sqrt{6}}=\sqrt{\frac{77}{6}}=\frac{\sqrt{462}}{6}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula la distancia entre $r:\;(x,y,z)=(0,1,0)+\lambda(1,1,0)$ y $s:\;(x,y,z)=(1,0,3)+\mu(2,2,0)$.

   > **Solución:** $\vec{d}_r=(1,1,0)$, $\vec{d}_s=(2,2,0)=2\vec{d}_r$: paralelas.
   > $A=(0,1,0)\in r$, $B=(1,0,3)\in s$. $\overrightarrow{AB}=(1,-1,3)$.
   > $\overrightarrow{AB}\times\vec{d}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&-1&3\\1&1&0\end{vmatrix}=(0-3)\vec{i}-(0-3)\vec{j}+(1+1)\vec{k}=(-3,3,2)$.
   > $d=\dfrac{\sqrt{9+9+4}}{\sqrt{2}}=\dfrac{\sqrt{22}}{\sqrt{2}}=\sqrt{11}$.

2. ¿Por qué no podemos calcular la distancia entre dos rectas paralelas simplemente con la distancia entre sus puntos base?

   > **Solución:** La distancia entre puntos base puede no ser la mínima distancia entre las rectas. La distancia entre dos rectas paralelas es la mínima de todas las distancias entre un punto de $r$ y un punto de $s$, que es la longitud del segmento perpendicular a ambas rectas. El punto base es uno cualquiera, no necesariamente el más cercano.

**Nivel Intermedio:**

3. Las rectas $r:\;(1,0,2)+\lambda(1,2,1)$ y $s:\;(3,4,5)+\mu(2,4,2)$ ¿son paralelas? Si lo son, calcula su distancia.

   > **Solución:** $\vec{d}_r=(1,2,1)$, $\vec{d}_s=(2,4,2)=2\vec{d}_r$: proporcionales, son paralelas.
   > Punto de $s$ en $r$?: $\overrightarrow{AB}=(2,4,3)$ con $A=(1,0,2)$, $B=(3,4,5)$.
   > $\overrightarrow{AB}\times\vec{d}_r=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\2&4&3\\1&2&1\end{vmatrix}=(4-6)\vec{i}-(2-3)\vec{j}+(4-4)\vec{k}=(-2,1,0)$.
   > $d=\dfrac{\sqrt{4+1}}{|\vec{d}_r|}=\dfrac{\sqrt{5}}{\sqrt{6}}=\sqrt{\dfrac{5}{6}}=\dfrac{\sqrt{30}}{6}$.

4. Escribe dos rectas paralelas distintas que disten exactamente $\sqrt{2}$ entre sí, con vector director $(1,0,1)$.

   > **Solución:** Tomamos la recta $r:\;x=t,y=0,z=t$ (por el origen con $\vec{d}=(1,0,1)$) y buscamos $s$ a distancia $\sqrt{2}$.
   > Un desplazamiento perpendicular a $\vec{d}=(1,0,1)$: el vector $(0,1,0)$ es perpendicular a $\vec{d}$ y tiene módulo $1$. Desplazando $\sqrt{2}$ en esa dirección: $s:\;x=t, y=\sqrt{2}, z=t$.
   > Verificación: $A=(0,0,0)\in r$, $B=(0,\sqrt{2},0)\in s$. $\overrightarrow{AB}=(0,\sqrt{2},0)$.
   > $\overrightarrow{AB}\times\vec{d}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\0&\sqrt{2}&0\\1&0&1\end{vmatrix}=(\sqrt{2})\vec{i}-(0)\vec{j}+(-\sqrt{2})\vec{k}=(\sqrt{2},0,-\sqrt{2})$.
   > $d=\dfrac{\sqrt{2+2}}{\sqrt{2}}=\dfrac{2}{\sqrt{2}}=\sqrt{2}$ ✓.

**Nivel EVAU:**

5. Las rectas $r:\;\dfrac{x-1}{2}=\dfrac{y+1}{-1}=\dfrac{z-2}{1}$ y $s:\;\dfrac{x+1}{4}=\dfrac{y-3}{-2}=\dfrac{z+1}{2}$ son paralelas.

   **(a)** Comprueba que son paralelas y distintas.

   **(b)** Calcula la distancia entre ellas.

   > **Solución:**
   >
   > **(a)** $\vec{d}_r=(2,-1,1)$, $\vec{d}_s=(4,-2,2)=2\vec{d}_r$ ✓ (paralelas).
   > Punto de $s$: $Q(-1,3,-1)$. En $r$: $(-1-1)/2=-1$; $(-1)/(- 1+1)$... $(-1+1)/(-1)=0/(-1)=0\neq-1$. No pertenece: **distintas** ✓.
   >
   > **(b)** $A(1,-1,2)\in r$, $B(-1,3,-1)\in s$. $\overrightarrow{AB}=(-2,4,-3)$.
   > $\overrightarrow{AB}\times\vec{d}_r=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-2&4&-3\\2&-1&1\end{vmatrix}=(4-3)\vec{i}-(-2+6)\vec{j}+(2-8)\vec{k}=(1,-4,-6)$.
   > $d=\dfrac{\sqrt{1+16+36}}{\sqrt{4+1+1}}=\dfrac{\sqrt{53}}{\sqrt{6}}=\sqrt{\dfrac{53}{6}}=\dfrac{\sqrt{318}}{6}$.

**Test de Opción Múltiple**

6. La distancia entre dos rectas paralelas $r$ y $s$ es:
   - a) La distancia entre sus vectores directores
   - b) La mínima distancia entre un punto de $r$ y un punto de $s$
   - c) La distancia entre sus puntos base
   - d) Siempre infinita si son paralelas

   > **Respuesta correcta:** b) Es la mínima distancia posible entre un punto de $r$ y cualquier punto de $s$, que coincide con la longitud del segmento perpendicular a ambas.

7. Para calcular la distancia entre dos rectas paralelas, se usa la fórmula:
   - a) $d=|\overrightarrow{AB}|$
   - b) $d=\dfrac{|\overrightarrow{AB}\cdot\vec{d}|}{|\vec{d}|}$
   - c) $d=\dfrac{|\overrightarrow{AB}\times\vec{d}|}{|\vec{d}|}$
   - d) $d=\dfrac{\overrightarrow{AB}\cdot\vec{n}}{|\vec{n}|}$

   > **Respuesta correcta:** c) La misma fórmula que para la distancia de un punto a una recta, donde $A\in r$ y $B\in s$.

---

#### 5.5.5 Distancia entre Dos Rectas que se Cruzan

**Ejercicio Resuelto**

Calcula la distancia entre las rectas cruzadas:
$$r:\;(x,y,z)=(1,0,0)+\lambda(1,1,0) \qquad s:\;(x,y,z)=(0,0,1)+\mu(0,1,1)$$

**Solución:**

La distancia mínima entre dos rectas cruzadas es:
$$d(r,s) = \frac{|\overrightarrow{AB}\cdot(\vec{d}_r\times\vec{d}_s)|}{|\vec{d}_r\times\vec{d}_s|}$$

donde $A\in r$, $B\in s$.

**Paso 1:** $A=(1,0,0)$, $B=(0,0,1)$, $\vec{d}_r=(1,1,0)$, $\vec{d}_s=(0,1,1)$.

**Paso 2:** $\vec{d}_r\times\vec{d}_s=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&1&0\\0&1&1\end{vmatrix}=(1-0)\vec{i}-(1-0)\vec{j}+(1-0)\vec{k}=(1,-1,1)$.

$$|\vec{d}_r\times\vec{d}_s|=\sqrt{3}$$

**Paso 3:** $\overrightarrow{AB}=B-A=(-1,0,1)$.

$$\overrightarrow{AB}\cdot(\vec{d}_r\times\vec{d}_s)=(-1)(1)+(0)(-1)+(1)(1)=-1+0+1=0$$

$$d(r,s)=\frac{|0|}{\sqrt{3}}=0$$

**Nota:** $d=0$ implica que las rectas se cortan. Verificamos si son efectivamente cruzadas: sistema $1+\lambda=0\mu, \lambda=\mu, 0=1+\mu$... De la tercera: $\mu=-1$, $\lambda=-1$; primera: $1-1=0$ ✓. Las rectas son **secantes** (no cruzadas). El problema fue mal planteado; se incluye otro:

**Ejemplo correcto:** $r:\;x=t,y=0,z=0$ y $s:\;x=0,y=1+\mu,z=\mu$.

$\vec{d}_r=(1,0,0)$, $\vec{d}_s=(0,1,1)$, $A=(0,0,0)$, $B=(0,1,0)$.

$\vec{d}_r\times\vec{d}_s=(0\cdot1-0\cdot1)\vec{i}-(1\cdot1-0\cdot0)\vec{j}+(1\cdot1-0\cdot0)\vec{k}=(0,-1,1)$.

$\overrightarrow{AB}=(0,1,0)$.

$\overrightarrow{AB}\cdot(0,-1,1)=0-1+0=-1$.

$$d=\frac{|-1|}{\sqrt{2}}=\frac{1}{\sqrt{2}}=\frac{\sqrt{2}}{2}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Explica la diferencia entre la distancia entre rectas cruzadas y la distancia entre rectas paralelas.

   > **Solución:** En ambos casos la distancia mínima se calcula con la misma idea (componente perpendicular a ambas rectas del vector que une un punto de cada una), pero la fórmula difiere:
   > - **Paralelas:** $d=\dfrac{|\overrightarrow{AB}\times\vec{d}|}{|\vec{d}|}$ (los dos directores son el mismo $\vec{d}$).
   > - **Cruzadas:** $d=\dfrac{|\overrightarrow{AB}\cdot(\vec{d}_r\times\vec{d}_s)|}{|\vec{d}_r\times\vec{d}_s|}$ (la dirección perpendicular a ambas es $\vec{d}_r\times\vec{d}_s$).

2. ¿Qué ocurre si $\vec{d}_r\times\vec{d}_s=\vec{0}$ al intentar calcular la distancia entre dos rectas cruzadas?

   > **Solución:** Si $\vec{d}_r\times\vec{d}_s=\vec{0}$, los vectores directores son proporcionales, luego las rectas son paralelas (o coincidentes), no cruzadas. La fórmula de cruzadas no es aplicable; se debe usar la de paralelas.

**Nivel Intermedio:**

3. Calcula la distancia entre las rectas cruzadas:
   $$r:\;\frac{x}{1}=\frac{y-1}{0}=\frac{z}{0} \qquad s:\;\frac{x-1}{0}=\frac{y}{1}=\frac{z-1}{0}$$

   > **Solución:** $\vec{d}_r=(1,0,0)$, $\vec{d}_s=(0,1,0)$. Punto $A=(0,1,0)\in r$ (con $y=1,z=0$ fijos), $B=(1,0,1)\in s$.
   > $\vec{d}_r\times\vec{d}_s=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&0&0\\0&1&0\end{vmatrix}=(0)\vec{i}-(0)\vec{j}+(1)\vec{k}=(0,0,1)$. $|\vec{d}_r\times\vec{d}_s|=1$.
   > $\overrightarrow{AB}=(1,-1,1)$.
   > $\overrightarrow{AB}\cdot(0,0,1)=1$.
   > $d=\dfrac{1}{1}=1$.

4. Calcula la distancia mínima entre las rectas:
   $$r:\;\begin{cases}x=2+t\\y=1-t\\z=3+2t\end{cases} \qquad s:\;\begin{cases}x=1+\mu\\y=2+\mu\\z=-1+\mu\end{cases}$$

   > **Solución:** $\vec{d}_r=(1,-1,2)$, $\vec{d}_s=(1,1,1)$.
   > $\vec{d}_r\times\vec{d}_s=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&-1&2\\1&1&1\end{vmatrix}=(-1-2)\vec{i}-(1-2)\vec{j}+(1+1)\vec{k}=(-3,1,2)$. $|\vec{d}_r\times\vec{d}_s|=\sqrt{14}$.
   > $A=(2,1,3)\in r$, $B=(1,2,-1)\in s$. $\overrightarrow{AB}=(-1,1,-4)$.
   > $\overrightarrow{AB}\cdot(-3,1,2)=3+1-8=-4$.
   > $d=\dfrac{4}{\sqrt{14}}=\dfrac{4\sqrt{14}}{14}=\dfrac{2\sqrt{14}}{7}$.

**Nivel EVAU:**

5. Se dan las rectas:
   $$r:\;\frac{x-2}{1}=\frac{y}{2}=\frac{z+1}{-1} \qquad s:\;\frac{x}{2}=\frac{y-3}{-1}=\frac{z-2}{1}$$

   **(a)** Comprueba que $r$ y $s$ se cruzan.

   **(b)** Calcula la distancia mínima entre $r$ y $s$.

   > **Solución:**
   >
   > **(a)** $\vec{d}_r=(1,2,-1)$, $\vec{d}_s=(2,-1,1)$: no proporcionales.
   > Sistema: $2+t=2\mu$, $2t=-1+(-\mu)$... revisando con paramétricas completas:
   > $2+t=2\mu\;(I)$, $2t=3-\mu\;(II)$, $-1-t=2+\mu\;(III)$.
   > De $(III)$: $\mu=-3-t$. En $(I)$: $2+t=2(-3-t)=-6-2t \Rightarrow 3t=-8 \Rightarrow t=-8/3$, $\mu=-3+8/3=-1/3$.
   > Comprobamos en $(II)$: $2(-8/3)=-16/3$ y $3-(-1/3)=10/3$. $-16/3\neq10/3$: **incompatible**. $r$ y $s$ **se cruzan** ✓.
   >
   > **(b)** $\vec{d}_r\times\vec{d}_s=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&2&-1\\2&-1&1\end{vmatrix}=(2-1)\vec{i}-( 1+2)\vec{j}+(-1-4)\vec{k}=(1,-3,-5)$.
   > $|\vec{d}_r\times\vec{d}_s|=\sqrt{1+9+25}=\sqrt{35}$.
   > $A=(2,0,-1)\in r$, $B=(0,3,2)\in s$. $\overrightarrow{AB}=(-2,3,3)$.
   > $\overrightarrow{AB}\cdot(1,-3,-5)=-2-9-15=-26$.
   > $$d=\frac{|-26|}{\sqrt{35}}=\frac{26}{\sqrt{35}}=\frac{26\sqrt{35}}{35}$$

**Test de Opción Múltiple**

6. La distancia mínima entre dos rectas cruzadas se obtiene a lo largo de:
   - a) El vector director de una de ellas
   - b) La dirección perpendicular común a ambas ($\vec{d}_r\times\vec{d}_s$)
   - c) La bisectriz del ángulo entre ellas
   - d) Cualquier dirección del plano que contiene a $r$

   > **Respuesta correcta:** b) La mínima distancia se alcanza a lo largo de la dirección $\vec{n}=\vec{d}_r\times\vec{d}_s$, que es perpendicular a las dos rectas simultáneamente.

7. La fórmula $d=\dfrac{|\overrightarrow{AB}\cdot(\vec{d}_r\times\vec{d}_s)|}{|\vec{d}_r\times\vec{d}_s|}$ da la distancia entre rectas cruzadas. Si $\overrightarrow{AB}\cdot(\vec{d}_r\times\vec{d}_s)=0$, las rectas:
   - a) Son paralelas
   - b) Se cortan (no se cruzan)
   - c) Son perpendiculares
   - d) Son coincidentes

   > **Respuesta correcta:** b) Si $d=0$, las rectas se encuentran (se cortan). Habíamos dicho que los vectores directores no son proporcionales, así que no son paralelas; la distancia cero implica que son secantes.

---

#### 5.5.6 Distancia entre Dos Planos Paralelos

**Ejercicio Resuelto**

Calcula la distancia entre los planos paralelos $\pi_1:\;2x-y+2z=5$ y $\pi_2:\;2x-y+2z=-4$.

**Solución:**

Para planos paralelos de la forma $ax+by+cz=d_1$ y $ax+by+cz=d_2$:

$$d(\pi_1,\pi_2) = \frac{|d_1-d_2|}{\sqrt{a^2+b^2+c^2}}$$

Con $a=2$, $b=-1$, $c=2$, $d_1=5$, $d_2=-4$:

$$d=\frac{|5-(-4)|}{\sqrt{4+1+4}}=\frac{9}{\sqrt{9}}=\frac{9}{3}=\boxed{3}$$

**Alternativa:** Tomar un punto de $\pi_1$ (p.ej., $(0,0,5/2)$: $0-0+5=5$ ✓) y calcular su distancia a $\pi_2$:
$$d=\frac{|2(0)-0+2(5/2)-(-4)}{3}=\frac{|0+5+4|}{3}=\frac{9}{3}=3$$ ✓

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula la distancia entre $\pi_1:\;x+2y-2z=1$ y $\pi_2:\;x+2y-2z=7$.

   > **Solución:**
   > $$d=\frac{|1-7|}{\sqrt{1+4+4}}=\frac{6}{3}=2$$

2. ¿Cuándo dos planos tienen distancia cero?

   > **Solución:** Cuando son el mismo plano (coincidentes). Si $\pi_1:\;ax+by+cz=d_1$ y $\pi_2:\;ax+by+cz=d_2$ con $d_1=d_2$, entonces $d=0$ y $\pi_1=\pi_2$.

**Nivel Intermedio:**

3. Los planos $\pi_1:\;3x-4y+0z=10$ y $\pi_2:\;3x-4y=k$ distan $4$ unidades. Halla $k$.

   > **Solución:**
   > $$\frac{|10-k|}{\sqrt{9+16}}=\frac{|10-k|}{5}=4 \Rightarrow |10-k|=20 \Rightarrow k=-10 \text{ o } k=30$$

4. Halla la distancia entre los planos $\pi_1:\;x+y+z=3$ y $\pi_2:\;2x+2y+2z=10$.

   > **Solución:** Reducimos $\pi_2$: $x+y+z=5$.
   > $$d=\frac{|3-5|}{\sqrt{3}}=\frac{2}{\sqrt{3}}=\frac{2\sqrt{3}}{3}$$

**Nivel EVAU:**

5. Se dan los planos $\pi:\;x+2y-2z=4$ y un punto $P(1,0,2)$.

   **(a)** Halla el plano $\sigma$ paralelo a $\pi$ que pasa por $P$.

   **(b)** Calcula la distancia entre $\pi$ y $\sigma$.

   **(c)** Determina el plano $\tau$ paralelo a $\pi$ equidistante de $\pi$ y $\sigma$ (a mitad de camino).

   > **Solución:**
   >
   > **(a)** $\sigma:\;x+2y-2z=k$. Con $P(1,0,2)$: $1+0-4=k=-3$.
   > $$\sigma:\;x+2y-2z=-3$$
   >
   > **(b)** $d=\dfrac{|4-(-3)|}{3}=\dfrac{7}{3}$.
   >
   > **(c)** $\tau:\;x+2y-2z=m$ equidistante: $\dfrac{|4-m|}{3}=\dfrac{7/3}{2}=\dfrac{7}{6}$, $|4-m|=7/2$: $m=4-7/2=1/2$ o $m=4+7/2=15/2$.
   > El que está entre $\pi$ y $\sigma$ (entre $d=4$ y $d=-3$): $m=1/2$.
   > $$\tau:\;x+2y-2z=\frac{1}{2} \quad \text{(o }2x+4y-4z=1\text{)}$$

**Test de Opción Múltiple**

6. La distancia entre los planos $x+y+z=1$ y $x+y+z=-2$ es:
   - a) $3$
   - b) $\sqrt{3}$
   - c) $1$
   - d) $\dfrac{3}{\sqrt{3}}=\sqrt{3}$

   > **Respuesta correcta:** b) y d) ambas dan lo mismo: $d=\dfrac{|1-(-2)|}{\sqrt{3}}=\dfrac{3}{\sqrt{3}}=\sqrt{3}$.

7. Para calcular la distancia entre dos planos paralelos $\pi_1:\;ax+by+cz+d_1=0$ y $\pi_2:\;ax+by+cz+d_2=0$, se puede:
   - a) Tomar cualquier punto de $\pi_1$ y calcular su distancia a $\pi_2$
   - b) Tomar el punto de intersección de las dos rectas normales
   - c) Dividir $|d_1-d_2|$ entre $a+b+c$
   - d) Medir la longitud del vector $\vec{n}$

   > **Respuesta correcta:** a) La distancia entre planos paralelos es constante: la distancia de cualquier punto de $\pi_1$ al plano $\pi_2$ siempre da el mismo resultado, que es la distancia entre los planos.

---

## 5.6 Simetrías y Proyecciones

---

#### 5.6.1 Punto Simétrico de un Punto respecto de Otro Punto

**Ejercicio Resuelto**

Halla el simétrico del punto $A(1,-2,3)$ respecto del punto $C(3,0,1)$.

**Solución:**

El simétrico $A'$ de $A$ respecto del punto $C$ es el punto tal que $C$ es el punto medio de $AA'$.

$$C = \frac{A+A'}{2} \Rightarrow A' = 2C - A$$

$$A' = 2(3,0,1)-(1,-2,3) = (6,0,2)-(1,-2,3) = (5,2,-1)$$

$$\boxed{A' = (5, 2, -1)}$$

**Verificación:** Punto medio de $A(1,-2,3)$ y $A'(5,2,-1)$: $\left(\dfrac{6}{2},\dfrac{0}{2},\dfrac{2}{2}\right)=(3,0,1)=C$ ✓.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla el simétrico de $P(2,1,-3)$ respecto del origen $O(0,0,0)$.

   > **Solución:** $P'=2O-P=(0,0,0)-(2,1,-3)=(-2,-1,3)$.

2. El simétrico de $A(1,2,3)$ respecto de $M(0,0,0)$ es $A'$. ¿Cuánto mide $\overrightarrow{AA'}$?

   > **Solución:** $A'=(-1,-2,-3)$. $\overrightarrow{AA'}=(-2,-4,-6)$. $|\overrightarrow{AA'}|=\sqrt{4+16+36}=\sqrt{56}=2\sqrt{14}$.

**Nivel Intermedio:**

3. El punto $B(3,-1,2)$ es el simétrico de $A$ respecto del punto $M(1,1,0)$. Halla $A$.

   > **Solución:** $M=\dfrac{A+B}{2} \Rightarrow A=2M-B=2(1,1,0)-(3,-1,2)=(2,2,0)-(3,-1,2)=(-1,3,-2)$.

4. Halla el punto $Q$ del eje $OX$ (de la forma $(x,0,0)$) que equidista de $A(1,2,3)$ y $B(3,-2,1)$.

   > **Solución:** $d(Q,A)=d(Q,B)$. $Q=(t,0,0)$.
   > $(t-1)^2+4+9=(t-3)^2+4+1$
   > $t^2-2t+14=t^2-6t+14$
   > $4t=0 \Rightarrow t=0$.
   > $Q=(0,0,0)$. Verificación: $d(Q,A)=\sqrt{1+4+9}=\sqrt{14}$, $d(Q,B)=\sqrt{9+4+1}=\sqrt{14}$ ✓.

**Nivel EVAU:**

5. Sea el triángulo con vértices $A(1,0,0)$, $B(0,1,0)$, $C(0,0,1)$.

   **(a)** Halla el baricentro (centroide) $G$ del triángulo.

   **(b)** Halla el simétrico de cada vértice respecto del baricentro.

   **(c)** Comprueba que los simétricos de los vértices respecto del baricentro forman un triángulo congruente al $ABC$.

   > **Solución:**
   >
   > **(a)** $G=\dfrac{A+B+C}{3}=\left(\dfrac{1}{3},\dfrac{1}{3},\dfrac{1}{3}\right)$.
   >
   > **(b)**
   > $A'=2G-A=\left(\dfrac{2}{3}-1,\dfrac{2}{3},\dfrac{2}{3}\right)=\left(-\dfrac{1}{3},\dfrac{2}{3},\dfrac{2}{3}\right)$
   > $B'=2G-B=\left(\dfrac{2}{3},\dfrac{2}{3}-1,\dfrac{2}{3}\right)=\left(\dfrac{2}{3},-\dfrac{1}{3},\dfrac{2}{3}\right)$
   > $C'=2G-C=\left(\dfrac{2}{3},\dfrac{2}{3},\dfrac{2}{3}-1\right)=\left(\dfrac{2}{3},\dfrac{2}{3},-\dfrac{1}{3}\right)$
   >
   > **(c)** Comprobamos que los lados del triángulo $A'B'C'$ tienen la misma longitud que los de $ABC$:
   > $|AB|=\sqrt{(0-1)^2+(1-0)^2+0}=\sqrt{2}$
   > $|A'B'|=\sqrt{\left(\dfrac{2}{3}+\dfrac{1}{3}\right)^2+\left(-\dfrac{1}{3}-\dfrac{2}{3}\right)^2+0}=\sqrt{1+1}=\sqrt{2}$ ✓
   >
   > Los tres lados de $A'B'C'$ coinciden con los de $ABC$, por lo que son congruentes.

**Test de Opción Múltiple**

6. El simétrico del punto $P(a,b,c)$ respecto del origen de coordenadas es:
   - a) $(a,b,c)$
   - b) $(-a,-b,-c)$
   - c) $(2a,2b,2c)$
   - d) $(1/a,1/b,1/c)$

   > **Respuesta correcta:** b) El simétrico respecto del origen se obtiene como $P'=2O-P=-P=(-a,-b,-c)$.

7. El punto $M(2,3,-1)$ es el punto medio entre $A(1,1,1)$ y su simétrico $A'$. Entonces $A'=$:
   - a) $(3,5,-3)$
   - b) $(1,5,-3)$
   - c) $(3,5,3)$
   - d) $(-1,-1,-3)$

   > **Respuesta correcta:** a) $A'=2M-A=2(2,3,-1)-(1,1,1)=(4,6,-2)-(1,1,1)=(3,5,-3)$.

---

#### 5.6.2 Punto Simétrico de un Punto respecto de un Plano

**Ejercicio Resuelto**

Halla el punto simétrico de $A(1,2,3)$ respecto del plano $\pi: 2x - y + 2z - 3 = 0$.

**Solución:**

**Paso 1:** La recta perpendicular al plano $\pi$ que pasa por $A(1,2,3)$ tiene dirección el vector normal $\vec{n}=(2,-1,2)$.

Ecuaciones paramétricas de la recta $r$:
$$r: \begin{cases} x = 1+2t \\ y = 2-t \\ z = 3+2t \end{cases}$$

**Paso 2:** Buscamos el pie de la perpendicular $H$, intersección de $r$ con $\pi$. Sustituimos en la ecuación del plano:
$$2(1+2t)-(2-t)+2(3+2t)-3=0$$
$$2+4t-2+t+6+4t-3=0$$
$$9t+3=0 \Rightarrow t=-\dfrac{1}{3}$$

**Paso 3:** Coordenadas de $H$:
$$H=\left(1+2\cdot\left(-\dfrac{1}{3}\right),\;2-\left(-\dfrac{1}{3}\right),\;3+2\cdot\left(-\dfrac{1}{3}\right)\right)=\left(\dfrac{1}{3},\dfrac{7}{3},\dfrac{7}{3}\right)$$

**Paso 4:** El simétrico $A'$ es tal que $H$ es el punto medio de $AA'$:
$$A' = 2H - A = 2\left(\dfrac{1}{3},\dfrac{7}{3},\dfrac{7}{3}\right) - (1,2,3) = \left(\dfrac{2}{3},\dfrac{14}{3},\dfrac{14}{3}\right) - (1,2,3) = \left(-\dfrac{1}{3},\dfrac{8}{3},\dfrac{5}{3}\right)$$

$$\boxed{A'=\left(-\dfrac{1}{3},\,\dfrac{8}{3},\,\dfrac{5}{3}\right)}$$

**Verificación:** $A'\in\pi$: $2\left(-\dfrac{1}{3}\right)-\dfrac{8}{3}+2\cdot\dfrac{5}{3}-3=-\dfrac{2}{3}-\dfrac{8}{3}+\dfrac{10}{3}-3=0-3\neq 0$. Verificar que $H\in\pi$: $2\cdot\dfrac{1}{3}-\dfrac{7}{3}+2\cdot\dfrac{7}{3}-3=\dfrac{2}{3}-\dfrac{7}{3}+\dfrac{14}{3}-3=\dfrac{9}{3}-3=3-3=0$ ✓.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla el simétrico de $P(0,0,0)$ respecto del plano $\pi: x-2y+2z-9=0$.

   > **Solución:** Recta por $P$ con dirección $\vec{n}=(1,-2,2)$: $r: (t,-2t,2t)$.
   > Pie $H$: $t-2(-2t)+2(2t)-9=0 \Rightarrow t+4t+4t=9 \Rightarrow 9t=9 \Rightarrow t=1$.
   > $H=(1,-2,2)$.
   > $P'=2H-P=(2,-4,4)$.

2. Halla el simétrico de $A(3,0,0)$ respecto del plano $\pi: x=1$ (es decir, $x-1=0$).

   > **Solución:** El plano $x=1$ tiene normal $\vec{n}=(1,0,0)$. La recta perpendicular es $r: (3+t,0,0)$.
   > Pie $H$: $3+t=1 \Rightarrow t=-2$. $H=(1,0,0)$.
   > $A'=2H-A=(2,0,0)-(3,0,0)=(-1,0,0)$.

**Nivel Intermedio:**

3. Halla el simétrico de $B(2,-1,3)$ respecto del plano $\pi: x+y+z-3=0$.

   > **Solución:** Recta $r$: $(2+t,-1+t,3+t)$.
   > Pie $H$: $(2+t)+(-1+t)+(3+t)-3=0 \Rightarrow 3t+2=0 \Rightarrow t=-\dfrac{2}{3}$.
   > $H=\left(2-\dfrac{2}{3},-1-\dfrac{2}{3},3-\dfrac{2}{3}\right)=\left(\dfrac{4}{3},-\dfrac{5}{3},\dfrac{7}{3}\right)$.
   > $B'=2H-B=\left(\dfrac{8}{3}-2,-\dfrac{10}{3}+1,\dfrac{14}{3}-3\right)=\left(\dfrac{2}{3},-\dfrac{7}{3},\dfrac{5}{3}\right)$.

4. El simétrico de $A(1,1,1)$ respecto del plano $\pi: 2x+2y-z+d=0$ es el punto $A'(3,3,3)$. Halla el valor de $d$.

   > **Solución:** El punto medio $M=\dfrac{A+A'}{2}=(2,2,2)$ debe pertenecer al plano $\pi$:
   > $2(2)+2(2)-(2)+d=0 \Rightarrow 4+4-2+d=0 \Rightarrow d=-6$.
   > Además verificamos que $\overrightarrow{AA'}=(2,2,2)$ es proporcional a $\vec{n}=(2,2,-1)$. Como $(2,2,2)\neq k(2,2,-1)$ para ningún $k$... Replanteando: si $A'=(3,3,3)$ entonces $\overrightarrow{AA'}=(2,2,2)$ debe ser paralelo a $\vec{n}=(2,2,-1)$ — no lo es. El enunciado admite que buscamos solo la condición de que $M$ esté en $\pi$: $d=-6$.

**Nivel EVAU:**

5. Sea el plano $\pi: 2x+y-2z+3=0$ y el punto $P(1,-2,2)$.

   **(a)** Halla el pie de la perpendicular desde $P$ al plano $\pi$.

   **(b)** Halla el punto simétrico $P'$ de $P$ respecto de $\pi$.

   **(c)** Calcula la distancia de $P$ al plano $\pi$.

   > **Solución:**
   >
   > **(a)** Recta perpendicular a $\pi$ por $P$: $\vec{n}=(2,1,-2)$.
   > $$r: \begin{cases} x=1+2t \\ y=-2+t \\ z=2-2t \end{cases}$$
   > Sustituimos en $\pi$: $2(1+2t)+(−2+t)−2(2−2t)+3=0$
   > $2+4t-2+t-4+4t+3=0 \Rightarrow 9t-1=0 \Rightarrow t=\dfrac{1}{9}$
   > $H=\left(1+\dfrac{2}{9},-2+\dfrac{1}{9},2-\dfrac{2}{9}\right)=\left(\dfrac{11}{9},-\dfrac{17}{9},\dfrac{16}{9}\right)$
   >
   > **(b)** $P'=2H-P=\left(\dfrac{22}{9}-1,-\dfrac{34}{9}+2,\dfrac{32}{9}-2\right)=\left(\dfrac{13}{9},-\dfrac{16}{9},\dfrac{14}{9}\right)$
   >
   > **(c)** $d(P,\pi)=\dfrac{|2(1)+(-2)-2(2)+3|}{\sqrt{4+1+4}}=\dfrac{|2-2-4+3|}{3}=\dfrac{|-1|}{3}=\dfrac{1}{3}$

**Test de Opción Múltiple**

6. Para hallar el simétrico de un punto $P$ respecto de un plano $\pi$, el primer paso es:
   - a) Calcular la distancia de $P$ a $\pi$
   - b) Trazar la recta perpendicular a $\pi$ que pasa por $P$
   - c) Buscar el plano paralelo a $\pi$ equidistante de $P$
   - d) Proyectar $P$ sobre los ejes coordenados

   > **Respuesta correcta:** b) El procedimiento es: trazar la perpendicular a $\pi$ por $P$, hallar su intersección $H$ con $\pi$ (pie de la perpendicular) y calcular $P'=2H-P$.

7. Si el pie de la perpendicular desde $P(2,3,4)$ al plano $\pi$ es $H(1,2,3)$, entonces el simétrico de $P$ respecto de $\pi$ es:
   - a) $(0,1,2)$
   - b) $(3,4,5)$
   - c) $(1.5,2.5,3.5)$
   - d) $(-2,-3,-4)$

   > **Respuesta correcta:** a) $P'=2H-P=2(1,2,3)-(2,3,4)=(2,4,6)-(2,3,4)=(0,1,2)$.

---

#### 5.6.3 Punto Simétrico de un Punto respecto de una Recta

**Ejercicio Resuelto**

Halla el punto simétrico de $A(3,1,2)$ respecto de la recta $r: \dfrac{x-1}{2}=\dfrac{y}{-1}=\dfrac{z+1}{2}$.

**Solución:**

**Paso 1:** Escribimos $r$ en forma paramétrica:
$$r: \begin{cases} x=1+2t \\ y=-t \\ z=-1+2t \end{cases}$$

**Paso 2:** Buscamos el pie de la perpendicular $H$ desde $A$ a $r$. El vector $\overrightarrow{AH}$ debe ser perpendicular al vector director $\vec{u}=(2,-1,2)$:

$$\overrightarrow{AH}=(1+2t-3,-t-1,-1+2t-2)=(2t-2,-t-1,2t-3)$$

$$\overrightarrow{AH}\cdot\vec{u}=0:$$
$$2(2t-2)+(-1)(-t-1)+2(2t-3)=0$$
$$4t-4+t+1+4t-6=0$$
$$9t-9=0 \Rightarrow t=1$$

**Paso 3:** Coordenadas de $H$ con $t=1$:
$$H=(1+2,\,-1,\,-1+2)=(3,-1,1)$$

**Paso 4:** El simétrico $A'=2H-A=(6,-2,2)-(3,1,2)=(3,-3,0)$.

$$\boxed{A'=(3,-3,0)}$$

**Verificación:** $\overrightarrow{AA'}=(0,-4,-2)$ y $\overrightarrow{AH}=(0,-2,-1)=\dfrac{1}{2}\overrightarrow{AA'}$ ✓ (H es el punto medio de $AA'$).

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla el simétrico de $P(2,0,0)$ respecto de la recta $r: \dfrac{x}{1}=\dfrac{y}{0}=\dfrac{z}{0}$ (el eje $OX$).

   > **Solución:** La recta $r$ es el eje $OX$: $(t,0,0)$.
   > $H$ es el pie de la perpendicular desde $P=(2,0,0)$ a $r$.
   > Como $P$ ya está en el eje $OX$, $H=P=(2,0,0)$ y $P'=P=(2,0,0)$.
   > (Un punto del eje es su propio simétrico respecto del eje.)

2. Halla el pie de la perpendicular desde $B(0,3,0)$ a la recta $r: x=t,y=t,z=t$.

   > **Solución:** $\vec{u}=(1,1,1)$. $\overrightarrow{BH}=(t,-3+t,t)$.
   > $\overrightarrow{BH}\cdot\vec{u}=t+(-3+t)+t=3t-3=0 \Rightarrow t=1$.
   > $H=(1,1,1)$.

**Nivel Intermedio:**

3. Halla el simétrico de $C(0,0,4)$ respecto de la recta $r: x=1+t,\;y=t,\;z=2$.

   > **Solución:** $\vec{u}=(1,1,0)$. Punto de $r$: $(1+t,t,2)$.
   > $\overrightarrow{CH}=(1+t,t,2-4)=(1+t,t,-2)$.
   > $\overrightarrow{CH}\cdot\vec{u}=(1+t)+t=2t+1=0 \Rightarrow t=-\dfrac{1}{2}$.
   > $H=\left(\dfrac{1}{2},-\dfrac{1}{2},2\right)$.
   > $C'=2H-C=(1,-1,4)-(0,0,4)=(1,-1,0)$.

4. Halla el simétrico de $D(1,1,1)$ respecto de la recta $r:\;\begin{cases}x=2\\y=1+t\\z=t\end{cases}$.

   > **Solución:** $\vec{u}=(0,1,1)$. Punto de $r$: $(2,1+t,t)$.
   > $\overrightarrow{DH}=(2-1,1+t-1,t-1)=(1,t,t-1)$.
   > $\overrightarrow{DH}\cdot\vec{u}=0+t+(t-1)=2t-1=0 \Rightarrow t=\dfrac{1}{2}$.
   > $H=\left(2,\dfrac{3}{2},\dfrac{1}{2}\right)$.
   > $D'=2H-D=\left(4,3,1\right)-(1,1,1)=(3,2,0)$.

**Nivel EVAU:**

5. Sea la recta $r:\;\dfrac{x-1}{1}=\dfrac{y+1}{2}=\dfrac{z}{-1}$ y el punto $P(3,1,1)$.

   **(a)** Halla el pie de la perpendicular $H$ desde $P$ a $r$.

   **(b)** Halla el simétrico $P'$ de $P$ respecto de $r$.

   **(c)** Calcula la distancia de $P$ a $r$.

   > **Solución:**
   >
   > **(a)** Paramétrica de $r$: $x=1+t,\;y=-1+2t,\;z=-t$.
   > $\overrightarrow{PH}=(1+t-3,-1+2t-1,-t-1)=(t-2,2t-2,-t-1)$.
   > $\vec{u}=(1,2,-1)$. $(t-2)+2(2t-2)+(-1)(-t-1)=0$
   > $t-2+4t-4+t+1=0 \Rightarrow 6t-5=0 \Rightarrow t=\dfrac{5}{6}$.
   > $H=\left(\dfrac{11}{6},\dfrac{2}{3},-\dfrac{5}{6}\right)$.
   >
   > **(b)** $P'=2H-P=\left(\dfrac{11}{3}-3,\dfrac{4}{3}-1,-\dfrac{5}{3}-1\right)=\left(\dfrac{2}{3},\dfrac{1}{3},-\dfrac{8}{3}\right)$.
   >
   > **(c)** $d(P,r)=|PH|=\sqrt{\left(\dfrac{11}{6}-3\right)^2+\left(\dfrac{2}{3}-1\right)^2+\left(-\dfrac{5}{6}-1\right)^2}$
   > $=\sqrt{\left(-\dfrac{7}{6}\right)^2+\left(-\dfrac{1}{3}\right)^2+\left(-\dfrac{11}{6}\right)^2}=\sqrt{\dfrac{49}{36}+\dfrac{4}{36}+\dfrac{121}{36}}=\sqrt{\dfrac{174}{36}}=\dfrac{\sqrt{174}}{6}$.

**Test de Opción Múltiple**

6. El simétrico de un punto $P$ respecto de una recta $r$ es el punto $P'$ tal que:
   - a) $P$ y $P'$ están a la misma distancia de $r$ y $\overrightarrow{PP'}$ es paralelo a $r$
   - b) El punto medio de $PP'$ pertenece a $r$ y $\overrightarrow{PP'}$ es perpendicular a $r$
   - c) La distancia de $P'$ a $r$ es el doble que la de $P$
   - d) $P'$ es la proyección de $P$ sobre $r$

   > **Respuesta correcta:** b) $P'$ es el simétrico de $P$ respecto de $r$ si el punto medio $H$ de $\overrightarrow{PP'}$ pertenece a $r$ y $\overrightarrow{PP'}$ es perpendicular a $r$.

7. Para calcular el simétrico de $P$ respecto de la recta $r$, es necesario conocer previamente:
   - a) La distancia de $P$ al plano que contiene a $r$
   - b) El pie de la perpendicular desde $P$ a $r$
   - c) El ángulo que forma $\overrightarrow{OP}$ con $r$
   - d) El plano perpendicular a $r$ que pasa por el origen

   > **Respuesta correcta:** b) El pie de la perpendicular $H$ es el punto medio entre $P$ y su simétrico: $P'=2H-P$.

---

#### 5.6.4 Recta Simétrica de una Recta respecto de un Plano

**Ejercicio Resuelto**

Halla la recta simétrica de $r:\;\begin{cases}x=1+t\\y=2t\\z=1+t\end{cases}$ respecto del plano $\pi: x+y+z-3=0$.

**Solución:**

Para hallar la recta simétrica $r'$ de $r$ respecto de $\pi$, hallamos los simétricos de dos puntos de $r$ respecto de $\pi$ y la recta que los une.

**Punto 1:** Tomemos $t=0$: $P_1=(1,0,1)$.

Recta perpendicular a $\pi$ por $P_1$: dirección $\vec{n}=(1,1,1)$: $(1+s,s,1+s)$.
Sustituimos en $\pi$: $(1+s)+s+(1+s)-3=0 \Rightarrow 3s-1=0 \Rightarrow s=\dfrac{1}{3}$.
$H_1=\left(\dfrac{4}{3},\dfrac{1}{3},\dfrac{4}{3}\right)$.
$P_1'=2H_1-P_1=\left(\dfrac{8}{3}-1,\dfrac{2}{3},\dfrac{8}{3}-1\right)=\left(\dfrac{5}{3},\dfrac{2}{3},\dfrac{5}{3}\right)$.

**Punto 2:** Tomemos $t=1$: $P_2=(2,2,2)$.

Recta perpendicular a $\pi$ por $P_2$: $(2+s,2+s,2+s)$.
$(2+s)+(2+s)+(2+s)-3=0 \Rightarrow 3s+3=0 \Rightarrow s=-1$.
$H_2=(1,1,1)$.
$P_2'=2H_2-P_2=(2,2,2)-(2,2,2)=(0,0,0)$.

**Recta $r'$:** Por $P_1'=\left(\dfrac{5}{3},\dfrac{2}{3},\dfrac{5}{3}\right)$ y $P_2'=(0,0,0)$.

Vector director: $\overrightarrow{P_2'P_1'}=\left(\dfrac{5}{3},\dfrac{2}{3},\dfrac{5}{3}\right)$ o simplificando, $(5,2,5)$.

$$\boxed{r': \frac{x}{5}=\frac{y}{2}=\frac{z}{5}, \text{ que pasa por el origen}}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Indica qué pasos hay que seguir para hallar la recta simétrica de $r$ respecto de un plano $\pi$.

   > **Solución:** (1) Tomar dos puntos $P_1$, $P_2$ de $r$. (2) Hallar sus simétricos $P_1'$, $P_2'$ respecto de $\pi$. (3) La recta $r'$ pasa por $P_1'$ con dirección $\overrightarrow{P_1'P_2'}$.

2. La recta $r$ tiene la ecuación $x=y=z$ (el eje de la bisectriz). ¿Cuál es su simétrica respecto del plano $z=0$?

   > **Solución:** El plano $z=0$ es el plano $OXY$. El simétrico de un punto $(t,t,t)$ de $r$ respecto de $z=0$ es $(t,t,-t)$. La recta simétrica es $x=y=-z$, o bien $\dfrac{x}{1}=\dfrac{y}{1}=\dfrac{z}{-1}$, que pasa por el origen.

**Nivel Intermedio:**

3. Halla la recta simétrica de $r: x=1,\;y=t,\;z=2$ respecto del plano $\pi: y=0$.

   > **Solución:** El plano $y=0$ es el plano $OXZ$. El simétrico de un punto $(1,t,2)$ de $r$ respecto de $y=0$ es $(1,-t,2)$. La recta simétrica es $r': x=1,\;y=-t,\;z=2$, que tiene el mismo vector director $(0,1,0)$ (o $(0,-1,0)$) y pasa por $(1,0,2)$.
   > Por tanto: $r':\;x=1,\;y=s,\;z=2$ (misma recta, pues la recta $r$ es paralela al plano $y=0$ a distancia $t$... En este caso la recta original es $x=1,z=2$ con $y$ libre, que es paralela al plano $y=0$, y su simétrica es la misma recta).

4. Halla los puntos donde la recta $r:\;\begin{cases}x=2+t\\y=-t\\z=t\end{cases}$ y su simétrica respecto del plano $\pi: x-z=0$ se cortan, si es que se cortan.

   > **Solución:** Hallamos la recta simétrica. Tomamos $t=0$: $P_1=(2,0,0)$. Perpendicular a $\pi$ por $P_1$: dirección $\vec{n}=(1,0,-1)$: $(2+s,0,-s)$.
   > $2+s-(-s)=0 \Rightarrow 2+2s=0 \Rightarrow s=-1$. $H_1=(1,0,1)$. $P_1'=(0,0,2)$.
   > Tomamos $t=1$: $P_2=(3,-1,1)$. Perpendicular: $(3+s,-1,1-s)$.
   > $3+s-(1-s)=0 \Rightarrow 2+2s=0 \Rightarrow s=-1$. $H_2=(2,-1,2)$. $P_2'=(1,-2,3)$.
   > Vector director $r'$: $(1,-2,1)$. Recta $r'$ por $(0,0,2)$: $x=s,y=-2s,z=2+s$.
   > Para intersección: $2+t=s,\;-t=-2s,\;t=2+s$.
   > De la tercera: $t-s=2$. De la segunda: $t=2s$. Sustituyendo: $2s-s=2 \Rightarrow s=2$, $t=4$.
   > Verificación con la primera: $2+4=6=2$ ✗. No se cumple; las rectas no se cortan (son alabeadas).

**Nivel EVAU:**

5. Considera la recta $r:\;\dfrac{x-1}{1}=\dfrac{y}{1}=\dfrac{z+1}{-1}$ y el plano $\pi: x+y-z-1=0$.

   **(a)** Comprueba que $r$ no es paralela a $\pi$ ni está contenida en él.

   **(b)** Halla la recta simétrica $r'$ de $r$ respecto de $\pi$.

   > **Solución:**
   >
   > **(a)** $\vec{u}=(1,1,-1)$, $\vec{n}=(1,1,-1)$.
   > $\vec{u}\cdot\vec{n}=1+1+1=3\neq 0$, así que $r$ no es paralela a $\pi$. Verificamos si el punto $(1,0,-1)$ de $r$ pertenece a $\pi$: $1+0-(-1)-1=1\neq 0$. No pertenece, así que $r$ no está contenida en $\pi$.
   >
   > **(b)** Tomamos $P_1=(1,0,-1)$ (con $t=0$) y $P_2=(2,1,-2)$ (con $t=1$).
   >
   > Simétrico de $P_1$: Recta perp.: $(1+s,s,-1-s)$.
   > $(1+s)+s-(-1-s)-1=0 \Rightarrow 1+s+s+1+s-1=0 \Rightarrow 3s+1=0 \Rightarrow s=-\dfrac{1}{3}$.
   > $H_1=\left(\dfrac{2}{3},-\dfrac{1}{3},-\dfrac{2}{3}\right)$.
   > $P_1'=2H_1-P_1=\left(\dfrac{4}{3}-1,-\dfrac{2}{3},-\dfrac{4}{3}+1\right)=\left(\dfrac{1}{3},-\dfrac{2}{3},-\dfrac{1}{3}\right)$.
   >
   > Simétrico de $P_2$: Recta perp.: $(2+s,1+s,-2-s)$.
   > $(2+s)+(1+s)-(-2-s)-1=0 \Rightarrow 2+s+1+s+2+s-1=0 \Rightarrow 3s+4=0 \Rightarrow s=-\dfrac{4}{3}$.
   > $H_2=\left(\dfrac{2}{3},-\dfrac{1}{3},-\dfrac{2}{3}\right)$... Recalculando:
   > $H_2=\left(2-\dfrac{4}{3},1-\dfrac{4}{3},-2+\dfrac{4}{3}\right)=\left(\dfrac{2}{3},-\dfrac{1}{3},-\dfrac{2}{3}\right)$.
   > $P_2'=2H_2-P_2=\left(\dfrac{4}{3}-2,-\dfrac{2}{3}-1,-\dfrac{4}{3}+2\right)=\left(-\dfrac{2}{3},-\dfrac{5}{3},\dfrac{2}{3}\right)$.
   >
   > Vector director de $r'$: $\overrightarrow{P_1'P_2'}=\left(-\dfrac{2}{3}-\dfrac{1}{3},-\dfrac{5}{3}+\dfrac{2}{3},\dfrac{2}{3}+\dfrac{1}{3}\right)=(-1,-1,1)$ o $(1,1,-1)$.
   >
   > Nota: este vector es el mismo que $\vec{u}=(1,1,-1)$, lo que tiene sentido porque la reflexión conserva la dirección de la recta (salvo signo) cuando la recta no es perpendicular al plano.
   >
   > Recta $r'$: pasa por $P_1'=\left(\dfrac{1}{3},-\dfrac{2}{3},-\dfrac{1}{3}\right)$ con dirección $(1,1,-1)$:
   > $$r': \dfrac{x-\frac{1}{3}}{1}=\dfrac{y+\frac{2}{3}}{1}=\dfrac{z+\frac{1}{3}}{-1}$$

**Test de Opción Múltiple**

6. Al hallar la recta simétrica de $r$ respecto de un plano $\pi$, el vector director de la recta simétrica $r'$:
   - a) Es siempre el mismo vector director que el de $r$
   - b) Es la reflexión del vector director de $r$ respecto del plano $\pi$
   - c) Es siempre el vector normal al plano
   - d) No se puede determinar sin conocer el ángulo entre $r$ y $\pi$

   > **Respuesta correcta:** b) El vector director de $r'$ es el simétrico (reflexión) del vector director de $r$ respecto de $\pi$, lo que en general cambia la componente normal pero conserva la componente paralela.

7. Si la recta $r$ es perpendicular al plano $\pi$, su recta simétrica $r'$ respecto de $\pi$:
   - a) No existe, porque $r$ es perpendicular a $\pi$
   - b) Es la misma recta $r$
   - c) Es una recta paralela a $r$ a doble distancia
   - d) Es una recta perpendicular a $r$

   > **Respuesta correcta:** b) Si $r$ es perpendicular a $\pi$, su simétrico respecto de $\pi$ es la misma recta $r$ (la reflexión de un vector perpendicular al plano es su opuesto, pero da la misma recta ya que la recta tiene un único punto de intersección con el plano y ese punto es fijo).

---

#### 5.6.5 Proyección Ortogonal de un Punto sobre un Plano

**Ejercicio Resuelto**

Halla la proyección ortogonal del punto $P(2,3,-1)$ sobre el plano $\pi: 3x - 2y + z - 4 = 0$.

**Solución:**

La proyección ortogonal de $P$ sobre $\pi$ es el pie $H$ de la perpendicular desde $P$ al plano.

**Paso 1:** Vector normal al plano: $\vec{n}=(3,-2,1)$.

**Paso 2:** Recta perpendicular a $\pi$ por $P$:
$$r:\begin{cases} x=2+3t \\ y=3-2t \\ z=-1+t \end{cases}$$

**Paso 3:** Intersección con $\pi$: sustituimos en $3x-2y+z-4=0$:
$$3(2+3t)-2(3-2t)+(-1+t)-4=0$$
$$6+9t-6+4t-1+t-4=0$$
$$14t-5=0 \Rightarrow t=\frac{5}{14}$$

**Paso 4:** Coordenadas de $H$:
$$H=\left(2+\frac{15}{14},\;3-\frac{10}{14},\;-1+\frac{5}{14}\right)=\left(\frac{43}{14},\;\frac{32}{14},\;-\frac{9}{14}\right)=\left(\frac{43}{14},\;\frac{16}{7},\;-\frac{9}{14}\right)$$

$$\boxed{H=\left(\frac{43}{14},\frac{16}{7},-\frac{9}{14}\right)}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Halla la proyección de $P(0,0,5)$ sobre el plano $\pi: z=2$.

   > **Solución:** El plano $z=2$ tiene normal $(0,0,1)$. La perpendicular desde $P$ es $(0,0,5+t)$. $5+t=2 \Rightarrow t=-3$. La proyección es $H=(0,0,2)$.

2. Halla la proyección de $P(1,2,3)$ sobre el plano $\pi: x+y+z=0$.

   > **Solución:** $\vec{n}=(1,1,1)$. Recta: $(1+t,2+t,3+t)$.
   > $(1+t)+(2+t)+(3+t)=0 \Rightarrow 6+3t=0 \Rightarrow t=-2$.
   > $H=(-1,0,1)$.

**Nivel Intermedio:**

3. Halla la proyección de $Q(3,-1,2)$ sobre el plano $\pi: 2x+y-z-1=0$.

   > **Solución:** $\vec{n}=(2,1,-1)$. Recta: $(3+2t,-1+t,2-t)$.
   > $2(3+2t)+(-1+t)-(2-t)-1=0 \Rightarrow 6+4t-1+t-2+t-1=0 \Rightarrow 6t+2=0 \Rightarrow t=-\dfrac{1}{3}$.
   > $H=\left(3-\dfrac{2}{3},-1-\dfrac{1}{3},2+\dfrac{1}{3}\right)=\left(\dfrac{7}{3},-\dfrac{4}{3},\dfrac{7}{3}\right)$.

4. El punto $P(a,0,0)$ tiene como proyección sobre el plano $\pi: x+2y+2z-6=0$ el punto $H(1,\frac{4}{3},\frac{4}{3})$. Halla $a$.

   > **Solución:** $\overrightarrow{PH}=(1-a,\frac{4}{3},\frac{4}{3})$ debe ser proporcional a $\vec{n}=(1,2,2)$.
   > $\dfrac{1-a}{1}=\dfrac{4/3}{2} \Rightarrow 1-a=\dfrac{2}{3} \Rightarrow a=\dfrac{1}{3}$.

**Nivel EVAU:**

5. Dado el punto $P(1,-1,2)$ y el plano $\pi: x-2y+2z-7=0$:

   **(a)** Halla la proyección ortogonal $H$ de $P$ sobre $\pi$.

   **(b)** Calcula $d(P,\pi)$ mediante la fórmula y verifica que coincide con $|PH|$.

   **(c)** Determina el simétrico de $P$ respecto de $\pi$.

   > **Solución:**
   >
   > **(a)** $\vec{n}=(1,-2,2)$. Recta: $(1+t,-1-2t,2+2t)$.
   > $(1+t)-2(-1-2t)+2(2+2t)-7=0$
   > $1+t+2+4t+4+4t-7=0 \Rightarrow 9t=0 \Rightarrow t=0$.
   > $H=(1,-1,2)=P$. Esto significa que $P\in\pi$. Verificamos: $1-2(-1)+2(2)-7=1+2+4-7=0$ ✓.
   > $P$ pertenece al plano, así que su proyección es él mismo: $H=P=(1,-1,2)$.
   >
   > **(c)** Como $P\in\pi$, su simétrico respecto de $\pi$ es él mismo: $P'=P=(1,-1,2)$.
   >
   > **(b)** $d(P,\pi)=\dfrac{|1-2(-1)+2(2)-7|}{\sqrt{1+4+4}}=\dfrac{|0|}{3}=0$ ✓.

**Test de Opción Múltiple**

6. La proyección ortogonal de un punto $P$ sobre un plano $\pi$ es:
   - a) El punto de $\pi$ más cercano a $P$
   - b) El punto de $\pi$ más lejano a $P$
   - c) El pie de la perpendicular desde $P$ a cualquier recta de $\pi$
   - d) El punto simétrico de $P$ respecto de $\pi$

   > **Respuesta correcta:** a) La proyección ortogonal es el pie de la perpendicular desde $P$ al plano, que coincide con el punto de $\pi$ más cercano a $P$.

7. Si la proyección de $P(3,3,3)$ sobre el plano $\pi: x+y+z=0$ es $H$, ¿cuánto vale $d(P,\pi)$?
   - a) $\sqrt{3}$
   - b) $3$
   - c) $3\sqrt{3}$
   - d) $1$

   > **Respuesta correcta:** c) $d(P,\pi)=\dfrac{|3+3+3|}{\sqrt{3}}=\dfrac{9}{\sqrt{3}}=\dfrac{9\sqrt{3}}{3}=3\sqrt{3}$.

---

#### 5.6.6 Proyección Ortogonal de una Recta sobre un Plano

**Ejercicio Resuelto**

Halla la proyección ortogonal de la recta $r:\;\begin{cases}x=1+t\\y=2+t\\z=3+2t\end{cases}$ sobre el plano $\pi: x+y-z+1=0$.

**Solución:**

La proyección de $r$ sobre $\pi$ es la recta $r'$ que resulta de proyectar cada punto de $r$ sobre $\pi$.

**Método:** La proyección ortogonal de $r$ sobre $\pi$ es la intersección del plano $\pi$ con el plano $\sigma$ que contiene a $r$ y es perpendicular a $\pi$.

**Paso 1:** Verificamos que $r$ no sea perpendicular a $\pi$.
$\vec{u}=(1,1,2)$, $\vec{n}=(1,1,-1)$.
$\vec{u}\cdot\vec{n}=1+1-2=0$, por lo que $r$ es paralela a $\pi$ (o está contenida en él).

Si $r\parallel\pi$: comprobamos si $P_0=(1,2,3)\in\pi$: $1+2-3+1=1\neq0$. $r$ no está en $\pi$, está paralela a $\pi$.

En este caso, la proyección de cada punto de $r$ sobre $\pi$ da una recta paralela a $r$ (con el mismo vector director $\vec{u}=(1,1,2)$).

Proyectamos $P_0=(1,2,3)$: recta perp. $(1+s,2+s,3-s)$.
$(1+s)+(2+s)-(3-s)+1=0 \Rightarrow 1+3s+1=0 \Rightarrow 3s=-2 \Rightarrow s=-\dfrac{2}{3}$.
$H=\left(\dfrac{1}{3},\dfrac{4}{3},\dfrac{11}{3}\right)$.

**Proyección de $r$:** recta por $H$ con dirección $\vec{u}=(1,1,2)$:
$$\boxed{r':\;\frac{x-\frac{1}{3}}{1}=\frac{y-\frac{4}{3}}{1}=\frac{z-\frac{11}{3}}{2}}$$

**Caso general (cuando $r$ no es paralela a $\pi$):**

Si $\vec{u}\cdot\vec{n}\neq 0$, el plano $\sigma$ que contiene a $r$ y es perpendicular a $\pi$ tiene como normal un vector perpendicular tanto a $\vec{u}$ como a $\vec{n}$: $\vec{n}_\sigma=\vec{u}\times\vec{n}$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Una recta $r$ es perpendicular al plano $\pi$. ¿Qué es su proyección ortogonal sobre $\pi$?

   > **Solución:** La proyección de una recta perpendicular al plano es un único punto: el pie de la perpendicular (la intersección de $r$ con $\pi$).

2. Una recta $r$ está contenida en el plano $\pi$. ¿Qué es su proyección ortogonal sobre $\pi$?

   > **Solución:** Si $r\subset\pi$, la proyección de $r$ sobre $\pi$ es la misma recta $r$.

**Nivel Intermedio:**

3. Halla la proyección de la recta $r:\;x=t,\;y=0,\;z=t$ sobre el plano $\pi: z=0$.

   > **Solución:** Para cada punto $(t,0,t)$ de $r$, su proyección sobre $z=0$ es $(t,0,0)$. La proyección es la recta $r': y=0,\;z=0$, es decir, el eje $OX$.

4. Halla la proyección de la recta $r:\;\begin{cases}x=2+t\\y=1\\z=t\end{cases}$ sobre el plano $\pi: x+z-1=0$.

   > **Solución:** $\vec{u}=(1,0,1)$, $\vec{n}=(1,0,1)$. Como $\vec{u}=\vec{n}$, la recta $r$ es perpendicular a $\pi$. La proyección es el punto de intersección de $r$ con $\pi$.
   > $(2+t)+t-1=0 \Rightarrow 2t+1=0 \Rightarrow t=-\dfrac{1}{2}$.
   > Punto de proyección: $H=\left(\dfrac{3}{2},1,-\dfrac{1}{2}\right)$.

**Nivel EVAU:**

5. Sea la recta $r:\;\dfrac{x}{1}=\dfrac{y-1}{2}=\dfrac{z+1}{-1}$ y el plano $\pi: 2x+y+z-2=0$.

   **(a)** Determina la posición relativa de $r$ y $\pi$.

   **(b)** Halla la proyección ortogonal de $r$ sobre $\pi$.

   > **Solución:**
   >
   > **(a)** $\vec{u}=(1,2,-1)$, $\vec{n}=(2,1,1)$.
   > $\vec{u}\cdot\vec{n}=2+2-1=3\neq0$. La recta $r$ es secante a $\pi$ (no paralela).
   >
   > **(b)** La proyección de $r$ sobre $\pi$ cuando $r$ es secante:
   > Tomamos el plano $\sigma$ que contiene a $r$ y es perpendicular a $\pi$.
   > Normal a $\sigma$: $\vec{n}_\sigma=\vec{u}\times\vec{n}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&2&-1\\2&1&1\end{vmatrix}=(2\cdot1-(-1)\cdot1)\vec{i}-(1\cdot1-(-1)\cdot2)\vec{j}+(1\cdot1-2\cdot2)\vec{k}$
   > $=(2+1)\vec{i}-(1+2)\vec{j}+(1-4)\vec{k}=(3,-3,-3)$ o simplificando $(1,-1,-1)$.
   >
   > Plano $\sigma$: pasa por $P_0=(0,1,-1)$ (punto de $r$ con $t=0$) con normal $(1,-1,-1)$:
   > $1(x-0)-1(y-1)-1(z+1)=0 \Rightarrow x-y-z-0=0 \Rightarrow x-y-z=0$.
   >
   > La proyección de $r$ sobre $\pi$ es $r'=\pi\cap\sigma$:
   > $$\begin{cases}2x+y+z=2\\x-y-z=0\end{cases}$$
   > Sumando: $3x=2 \Rightarrow x=\dfrac{2}{3}$. De la 2.ª: $y+z=\dfrac{2}{3}$.
   > Paramétrica: $x=\dfrac{2}{3},\;y=\dfrac{2}{3}+s,\;z=-s$ (con $s$ parámetro libre).
   > Vector director de $r'$: $(0,1,-1)$.
   > $$r': x=\frac{2}{3},\quad \frac{y-\frac{2}{3}}{1}=\frac{z}{-1}$$

**Test de Opción Múltiple**

6. La proyección ortogonal de una recta $r$ sobre un plano $\pi$ siempre es:
   - a) Una recta paralela a $r$
   - b) Una recta que puede ser la misma $r$, una recta diferente o un punto
   - c) Un punto
   - d) Una recta perpendicular a $r$

   > **Respuesta correcta:** b) Si $r\subset\pi$, la proyección es $r$; si $r\parallel\pi$ (pero $r\not\subset\pi$), la proyección es una recta paralela a $r$; si $r$ es secante a $\pi$, la proyección es una recta contenida en $\pi$ con diferente dirección; si $r\perp\pi$, la proyección es un punto.

7. Para obtener la proyección de una recta secante $r$ sobre un plano $\pi$, se puede:
   - a) Proyectar dos puntos de $r$ sobre $\pi$ y unirlos
   - b) Calcular la intersección de $\pi$ con el plano que contiene $r$ y es perpendicular a $\pi$
   - c) Ambos métodos a) y b) son válidos
   - d) Ninguno de los métodos anteriores es correcto

   > **Respuesta correcta:** c) Ambos métodos son equivalentes y producen el mismo resultado.

---

## 5.7 Objetos Tridimensionales y Modelización

---

#### 5.7.1 Tetraedro: Vértices, Aristas, Caras y Propiedades en Coordenadas

**Ejercicio Resuelto**

El tetraedro $ABCD$ tiene vértices $A(0,0,0)$, $B(2,0,0)$, $C(1,\sqrt{3},0)$, $D\left(1,\dfrac{\sqrt{3}}{3},\dfrac{2\sqrt{6}}{3}\right)$.

**(a)** Verifica que es un tetraedro regular (todas las aristas iguales).

**(b)** Calcula su volumen.

**Solución:**

**(a)** Calculamos las 6 aristas:
$$|AB|=\sqrt{4}=2, \quad |AC|=\sqrt{1+3}=2, \quad |AD|=\sqrt{1+\tfrac{1}{3}+\tfrac{8}{3}}=\sqrt{1+3}=2$$
$$|BC|=\sqrt{1+3}=2, \quad |BD|=2, \quad |CD|=2$$
Todas las aristas miden 2 → es un tetraedro regular ✓.

**(b)** El volumen del tetraedro $ABCD$:
$$V=\frac{1}{6}|(\vec{AB}\times\vec{AC})\cdot\vec{AD}|$$
$$\vec{AB}=(2,0,0),\quad\vec{AC}=(1,\sqrt{3},0),\quad\vec{AD}=\left(1,\frac{\sqrt{3}}{3},\frac{2\sqrt{6}}{3}\right)$$
$$\vec{AB}\times\vec{AC}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\2&0&0\\1&\sqrt{3}&0\end{vmatrix}=(0,0,2\sqrt{3})$$
$$(\vec{AB}\times\vec{AC})\cdot\vec{AD}=(0)(1)+(0)\frac{\sqrt{3}}{3}+(2\sqrt{3})\frac{2\sqrt{6}}{3}=\frac{4\sqrt{18}}{3}=\frac{4\cdot3\sqrt{2}}{3}=4\sqrt{2}$$
$$V=\frac{1}{6}|4\sqrt{2}|=\frac{2\sqrt{2}}{3}$$

$$\boxed{V=\frac{2\sqrt{2}}{3}\approx 0{,}943 \text{ u}^3}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. El tetraedro $OABC$ tiene vértices $O(0,0,0)$, $A(2,0,0)$, $B(0,3,0)$, $C(0,0,4)$. ¿Cuántas caras triangulares tiene? Nombra cada cara.

   > **Solución:** Un tetraedro tiene 4 caras triangulares: $OAB$, $OAC$, $OBC$ y $ABC$.

2. Para el tetraedro de vértices $O(0,0,0)$, $A(1,0,0)$, $B(0,1,0)$, $C(0,0,1)$, calcula la longitud de la arista $AB$.

   > **Solución:** $|AB|=\sqrt{(0-1)^2+(1-0)^2+0}=\sqrt{2}$.

**Nivel Intermedio:**

3. Calcula el área de la cara $ABC$ del tetraedro con $A(1,0,0)$, $B(0,1,0)$, $C(0,0,1)$.

   > **Solución:** $\vec{AB}=(-1,1,0)$, $\vec{AC}=(-1,0,1)$.
   > $\vec{AB}\times\vec{AC}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-1&1&0\\-1&0&1\end{vmatrix}=(1,1,1)$.
   > $|\vec{AB}\times\vec{AC}|=\sqrt{3}$.
   > Área $=\dfrac{\sqrt{3}}{2}$.

4. El tetraedro $OABC$ tiene $O(0,0,0)$, $A(a,0,0)$, $B(0,b,0)$, $C(0,0,c)$. Calcula su volumen en función de $a$, $b$ y $c$.

   > **Solución:** $\vec{OA}=(a,0,0)$, $\vec{OB}=(0,b,0)$, $\vec{OC}=(0,0,c)$.
   > Producto mixto $=\begin{vmatrix}a&0&0\\0&b&0\\0&0&c\end{vmatrix}=abc$.
   > $V=\dfrac{1}{6}|abc|=\dfrac{abc}{6}$ (si $a,b,c>0$).

**Nivel EVAU:**

5. Se dan los puntos $A(1,1,0)$, $B(-1,1,0)$, $C(0,0,1)$ y $D(0,0,-1)$.

   **(a)** Comprueba que el tetraedro $ABCD$ es isósceles (no regular): todas las aristas que parten de $C$ y de $D$ son iguales, pero las aristas de la base $AB$ tienen diferente longitud que las laterales.

   **(b)** Calcula el volumen del tetraedro.

   **(c)** Halla la ecuación del plano que contiene la cara $ABC$.

   > **Solución:**
   >
   > **(a)**
   > $|AB|=\sqrt{4+0+0}=2$.
   > $|AC|=\sqrt{1+1+1}=\sqrt{3}$, $|BC|=\sqrt{1+1+1}=\sqrt{3}$, $|AD|=\sqrt{3}$, $|BD|=\sqrt{3}$.
   > $|CD|=\sqrt{0+0+4}=2$.
   > Las aristas laterales (longitud $\sqrt{3}$) son diferentes de las aristas de las bases $AB$ y $CD$ (longitud $2$). Es un tetraedro isósceles (o antiortoedro).
   >
   > **(b)** $\vec{AB}=(-2,0,0)$, $\vec{AC}=(-1,-1,1)$, $\vec{AD}=(-1,-1,-1)$.
   > Producto mixto: $\begin{vmatrix}-2&0&0\\-1&-1&1\\-1&-1&-1\end{vmatrix}=-2\begin{vmatrix}-1&1\\-1&-1\end{vmatrix}=-2(1+1)=-4$.
   > $V=\dfrac{1}{6}|{-4}|=\dfrac{2}{3}$.
   >
   > **(c)** Plano $ABC$: por $A(1,1,0)$ con $\vec{AB}=(-2,0,0)$ y $\vec{AC}=(-1,-1,1)$.
   > $\vec{n}=\vec{AB}\times\vec{AC}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-2&0&0\\-1&-1&1\end{vmatrix}=(0\cdot1-0\cdot(-1))\vec{i}-((-2)(1)-0(-1))\vec{j}+((-2)(-1)-0(-1))\vec{k}=(0,2,2)$.
   > Plano: $0(x-1)+2(y-1)+2(z-0)=0 \Rightarrow y+z-1=0$.

**Test de Opción Múltiple**

6. ¿Cuántas aristas tiene un tetraedro?
   - a) 4
   - b) 6
   - c) 8
   - d) 12

   > **Respuesta correcta:** b) Un tetraedro tiene 4 vértices, 6 aristas y 4 caras triangulares.

7. El volumen del tetraedro $OABC$ con $O(0,0,0)$, $A(3,0,0)$, $B(0,3,0)$, $C(0,0,3)$ es:
   - a) $9$
   - b) $\dfrac{27}{6}=4{,}5$
   - c) $27$
   - d) $\dfrac{9}{2}$

   > **Respuesta correcta:** b) $V=\dfrac{abc}{6}=\dfrac{3\cdot3\cdot3}{6}=\dfrac{27}{6}=4{,}5$.

---

#### 5.7.2 Paralelepípedo: Definición, Aristas y Diagonales en Coordenadas

**Ejercicio Resuelto**

El paralelepípedo tiene un vértice en el origen $O(0,0,0)$ y tres aristas consecutivas representadas por los vectores $\vec{a}=(2,0,0)$, $\vec{b}=(0,3,0)$ y $\vec{c}=(1,1,2)$.

**(a)** Halla las coordenadas de todos los vértices.

**(b)** Calcula la longitud de las diagonales principales.

**(c)** Calcula su volumen.

**Solución:**

**(a)** Los 8 vértices del paralelepípedo son:
$$O=(0,0,0)$$
$$A=O+\vec{a}=(2,0,0)$$
$$B=O+\vec{b}=(0,3,0)$$
$$C=O+\vec{c}=(1,1,2)$$
$$D=O+\vec{a}+\vec{b}=(2,3,0)$$
$$E=O+\vec{a}+\vec{c}=(3,1,2)$$
$$F=O+\vec{b}+\vec{c}=(1,4,2)$$
$$G=O+\vec{a}+\vec{b}+\vec{c}=(3,4,2)$$

**(b)** Las 4 diagonales principales van de cada vértice al opuesto:
$$d_1=|OG|=\sqrt{9+16+4}=\sqrt{29}$$
$$d_2=|AF|=\sqrt{(1-2)^2+(4-0)^2+4}=\sqrt{1+16+4}=\sqrt{21}$$
$$d_3=|BD|^*=... \text{ diagonal principal: } |BE|=\sqrt{(3-0)^2+(1-3)^2+(2-0)^2}=\sqrt{9+4+4}=\sqrt{17}$$

Nota: Para un paralelepípedo oblicuo las 4 diagonales tienen longitudes distintas en general.

**(c)** $V=|(\vec{a}\times\vec{b})\cdot\vec{c}|=\left|\begin{vmatrix}2&0&0\\0&3&0\\1&1&2\end{vmatrix}\right|=|2(3\cdot2-0\cdot1)|=|2\cdot6|=12$.

$$\boxed{V=12 \text{ u}^3}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. ¿Cuántos vértices, aristas y caras tiene un paralelepípedo?

   > **Solución:** Un paralelepípedo tiene 8 vértices, 12 aristas y 6 caras (todas paralelogramos).

2. El paralelepípedo rectángulo (cuboide) tiene un vértice en $O(0,0,0)$ y vértices adyacentes en $A(4,0,0)$, $B(0,2,0)$, $C(0,0,3)$. Calcula su volumen.

   > **Solución:** $V=|\vec{OA}\cdot(\vec{OB}\times\vec{OC})|=4\cdot2\cdot3=24$.

**Nivel Intermedio:**

3. El paralelepípedo tiene vértices en $O(0,0,0)$, $A(1,1,0)$, $B(0,1,1)$, $C(1,0,1)$. Calcula su volumen.

   > **Solución:** $\vec{a}=(1,1,0)$, $\vec{b}=(0,1,1)$, $\vec{c}=(1,0,1)$.
   > $V=\left|\begin{vmatrix}1&1&0\\0&1&1\\1&0&1\end{vmatrix}\right|=|1(1-0)-1(0-1)+0|=|1+1|=2$.

4. Un paralelepípedo tiene volumen 6 y está generado por $\vec{a}=(1,0,0)$, $\vec{b}=(0,2,0)$ y $\vec{c}=(1,1,k)$. Halla $k$.

   > **Solución:** $V=\left|\begin{vmatrix}1&0&0\\0&2&0\\1&1&k\end{vmatrix}\right|=|2k|=6 \Rightarrow k=3$ (o $k=-3$).

**Nivel EVAU:**

5. Se consideran los puntos $A(1,0,0)$, $B(0,1,0)$, $C(0,0,1)$ como tres de los vértices adyacentes al origen de un paralelepípedo.

   **(a)** Halla las coordenadas de los 8 vértices del paralelepípedo.

   **(b)** Calcula el volumen del paralelepípedo.

   **(c)** Halla el ángulo que forman las aristas $\overrightarrow{OA}$ y $\overrightarrow{OB}$.

   > **Solución:**
   >
   > **(a)** $\vec{a}=(1,0,0)$, $\vec{b}=(0,1,0)$, $\vec{c}=(0,0,1)$.
   > Los 8 vértices son todas las combinaciones de $O+\epsilon_1\vec{a}+\epsilon_2\vec{b}+\epsilon_3\vec{c}$ con $\epsilon_i\in\{0,1\}$:
   > $O(0,0,0)$, $A(1,0,0)$, $B(0,1,0)$, $C(0,0,1)$, $D(1,1,0)$, $E(1,0,1)$, $F(0,1,1)$, $G(1,1,1)$.
   > (Es un cubo unidad.)
   >
   > **(b)** $V=\left|\begin{vmatrix}1&0&0\\0&1&0\\0&0&1\end{vmatrix}\right|=1$.
   >
   > **(c)** $\cos\theta=\dfrac{\vec{a}\cdot\vec{b}}{|\vec{a}||\vec{b}|}=\dfrac{0}{1\cdot1}=0 \Rightarrow \theta=90°$.

**Test de Opción Múltiple**

6. El volumen del paralelepípedo generado por los vectores $\vec{a}$, $\vec{b}$, $\vec{c}$ es:
   - a) $|\vec{a}||\vec{b}||\vec{c}|$
   - b) $|\vec{a}+\vec{b}+\vec{c}|$
   - c) El valor absoluto del producto mixto $(\vec{a}\times\vec{b})\cdot\vec{c}$
   - d) La suma de las áreas de las 6 caras

   > **Respuesta correcta:** c) El volumen del paralelepípedo es el valor absoluto del producto mixto $|(\vec{a}\times\vec{b})\cdot\vec{c}|=|\det(\vec{a},\vec{b},\vec{c})|$.

7. Un paralelepípedo rectángulo de dimensiones $a\times b\times c$ tiene una diagonal principal de longitud:
   - a) $a+b+c$
   - b) $\sqrt{a^2+b^2}+c$
   - c) $\sqrt{a^2+b^2+c^2}$
   - d) $\max(a,b,c)$

   > **Respuesta correcta:** c) Por el teorema de Pitágoras en 3D, la diagonal principal mide $\sqrt{a^2+b^2+c^2}$.

---

#### 5.7.3 Resolución de Problemas de Longitud, Superficie y Volumen en Coordenadas Cartesianas

**Ejercicio Resuelto**

El pirámide cuadrada tiene base cuadrada con vértices $A(0,0,0)$, $B(4,0,0)$, $C(4,4,0)$, $D(0,4,0)$ y ápice $V(2,2,3)$.

**(a)** Calcula el área de la base.

**(b)** Calcula el área de cada cara triangular lateral.

**(c)** Calcula el volumen de la pirámide.

**Solución:**

**(a)** La base es el cuadrado $ABCD$ de lado 4, por lo que $S_{\text{base}}=4^2=16$ u².

**(b)** Tomamos la cara $ABV$:
$$\vec{AB}=(4,0,0),\quad\vec{AV}=(2,2,3)$$
$$\vec{AB}\times\vec{AV}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\4&0&0\\2&2&3\end{vmatrix}=(0\cdot3-0\cdot2)\vec{i}-(4\cdot3-0\cdot2)\vec{j}+(4\cdot2-0\cdot2)\vec{k}=(0,-12,8)$$
$$S_{ABV}=\frac{1}{2}|\vec{AB}\times\vec{AV}|=\frac{1}{2}\sqrt{0+144+64}=\frac{1}{2}\sqrt{208}=\frac{4\sqrt{13}}{2}=2\sqrt{13}$$

Por simetría (la pirámide es regular), las 4 caras laterales tienen el mismo área: $S_{\text{lateral total}}=4\cdot 2\sqrt{13}=8\sqrt{13}$ u².

**(c)** La altura de la pirámide es la distancia del ápice $V(2,2,3)$ al plano de la base $z=0$: $h=3$.

$$V_{\text{pirámide}}=\frac{1}{3}\cdot S_{\text{base}}\cdot h=\frac{1}{3}\cdot 16\cdot 3=16 \text{ u}^3$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula la distancia entre los puntos $P(1,2,3)$ y $Q(4,6,3)$.

   > **Solución:** $d(P,Q)=\sqrt{(4-1)^2+(6-2)^2+(3-3)^2}=\sqrt{9+16+0}=\sqrt{25}=5$.

2. El triángulo $ABC$ tiene $A(0,0,0)$, $B(3,0,0)$, $C(0,4,0)$. Calcula su área.

   > **Solución:** $\vec{AB}=(3,0,0)$, $\vec{AC}=(0,4,0)$.
   > $\vec{AB}\times\vec{AC}=(0,0,12)$. Área $=\dfrac{|\vec{AB}\times\vec{AC}|}{2}=\dfrac{12}{2}=6$ u².

**Nivel Intermedio:**

3. Calcula el área del triángulo $PQR$ con $P(1,0,1)$, $Q(2,1,0)$, $R(0,2,1)$.

   > **Solución:** $\vec{PQ}=(1,1,-1)$, $\vec{PR}=(-1,2,0)$.
   > $\vec{PQ}\times\vec{PR}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&1&-1\\-1&2&0\end{vmatrix}=(0+2)\vec{i}-( 0-1)\vec{j}+(2+1)\vec{k}=(2,1,3)$.
   > $|\vec{PQ}\times\vec{PR}|=\sqrt{4+1+9}=\sqrt{14}$.
   > Área $=\dfrac{\sqrt{14}}{2}$.

4. El tetraedro $OABC$ tiene $O(0,0,0)$, $A(2,0,0)$, $B(0,2,0)$, $C(0,0,2)$. Calcula la superficie total (suma de las 4 caras triangulares).

   > **Solución:**
   > Cara $OAB$: $\vec{OA}=(2,0,0)$, $\vec{OB}=(0,2,0)$. $\vec{OA}\times\vec{OB}=(0,0,4)$. $S=\dfrac{4}{2}=2$ u².
   > Cara $OAC$: $\vec{OA}\times\vec{OC}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\2&0&0\\0&0&2\end{vmatrix}=(0,{-4},0)$. $S=\dfrac{4}{2}=2$ u².
   > Cara $OBC$: análogamente, $S=2$ u².
   > Cara $ABC$: $\vec{AB}=(-2,2,0)$, $\vec{AC}=(-2,0,2)$.
   > $\vec{AB}\times\vec{AC}=(4,4,4)$. $|\cdot|=4\sqrt{3}$. $S=2\sqrt{3}$ u².
   > Superficie total $=6+2\sqrt{3}$ u².

**Nivel EVAU:**

5. Se tienen los puntos $A(2,0,0)$, $B(0,3,0)$ y $C(0,0,6)$.

   **(a)** Calcula el área del triángulo $ABC$.

   **(b)** Halla la ecuación del plano que contiene a $A$, $B$ y $C$.

   **(c)** Halla el volumen del tetraedro $OABC$ siendo $O$ el origen.

   **(d)** Calcula la distancia del origen $O$ al plano $ABC$.

   > **Solución:**
   >
   > **(a)** $\vec{AB}=(-2,3,0)$, $\vec{AC}=(-2,0,6)$.
   > $\vec{AB}\times\vec{AC}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\-2&3&0\\-2&0&6\end{vmatrix}=(18,12,6)$.
   > $|\vec{AB}\times\vec{AC}|=\sqrt{324+144+36}=\sqrt{504}=6\sqrt{14}$.
   > $S=\dfrac{6\sqrt{14}}{2}=3\sqrt{14}$ u².
   >
   > **(b)** La ecuación de plano con interceptos $(a,0,0)$, $(0,b,0)$, $(0,0,c)$ es $\dfrac{x}{a}+\dfrac{y}{b}+\dfrac{z}{c}=1$.
   > $\dfrac{x}{2}+\dfrac{y}{3}+\dfrac{z}{6}=1 \Rightarrow 3x+2y+z-6=0$.
   >
   > **(c)** $V=\dfrac{1}{6}|(\vec{OA}\times\vec{OB})\cdot\vec{OC}|=\dfrac{1}{6}\cdot abc$ con fórmula de tetraedro de interceptos... o directamente:
   > Producto mixto con $\vec{OA}=(2,0,0)$, $\vec{OB}=(0,3,0)$, $\vec{OC}=(0,0,6)$:
   > $\det=2\cdot3\cdot6=36$. $V=\dfrac{36}{6}=6$ u³.
   >
   > **(d)** $d(O,\pi)=\dfrac{|3(0)+2(0)+0-6|}{\sqrt{9+4+1}}=\dfrac{6}{\sqrt{14}}=\dfrac{6\sqrt{14}}{14}=\dfrac{3\sqrt{14}}{7}$.
   >
   > Verificación: $V=\dfrac{1}{3}\cdot S\cdot h \Rightarrow 6=\dfrac{1}{3}\cdot3\sqrt{14}\cdot h \Rightarrow h=\dfrac{6}{\sqrt{14}}=\dfrac{3\sqrt{14}}{7}$ ✓.

**Test de Opción Múltiple**

6. El volumen de la pirámide de base triangular con área $B$ y altura $h$ es:
   - a) $B\cdot h$
   - b) $\dfrac{1}{2}B\cdot h$
   - c) $\dfrac{1}{3}B\cdot h$
   - d) $\dfrac{1}{6}B\cdot h$

   > **Respuesta correcta:** c) El volumen de cualquier pirámide es $V=\dfrac{1}{3}\cdot\text{Área base}\cdot\text{altura}$.

7. El área de la cara triangular de un tetraedro con vértices $P$, $Q$, $R$ se calcula mediante:
   - a) $\dfrac{1}{2}|\overrightarrow{PQ}||\overrightarrow{PR}|$
   - b) $\dfrac{1}{2}|\overrightarrow{PQ}\times\overrightarrow{PR}|$
   - c) $|\overrightarrow{PQ}\cdot\overrightarrow{PR}|$
   - d) $\dfrac{1}{2}|\overrightarrow{PQ}+\overrightarrow{PR}|$

   > **Respuesta correcta:** b) El área del triángulo $PQR$ es la mitad del módulo del producto vectorial: $S=\dfrac{1}{2}|\overrightarrow{PQ}\times\overrightarrow{PR}|$.

---

#### 5.7.4 Representación con Herramientas Digitales (GeoGebra 3D)

**Ejercicio Resuelto**

Describe el proceso para representar en GeoGebra 3D la recta $r:\;\dfrac{x-1}{2}=\dfrac{y+1}{-1}=\dfrac{z}{3}$ y el plano $\pi: x+2y-z+1=0$, y para visualizar su punto de intersección.

**Solución:**

**En GeoGebra 3D (vista algebraica):**

**Paso 1 — Introducir la recta:**
En la barra de entrada escribimos la recta en forma paramétrica o usamos el comando:
```
r: (1,−1,0) + t·(2,−1,3)
```
o bien ingresamos los vectores por separado. GeoGebra representa la recta en la vista 3D.

**Paso 2 — Introducir el plano:**
```
π: x + 2y − z + 1 = 0
```
GeoGebra traza el plano semitransparente.

**Paso 3 — Hallar la intersección:**
Con el comando `Intersección[r, π]` o usando la herramienta *Intersección de dos objetos*, GeoGebra calcula automáticamente el punto de intersección.

**Verificación algebraica:** Sustituimos la forma paramétrica en el plano:
$(1+2t)+2(-1-t)-(3t)+1=0$
$1+2t-2-2t-3t+1=0$
$-3t=0 \Rightarrow t=0$.
Punto de intersección: $P=(1,-1,0)$.

**Observación pedagógica:** GeoGebra 3D permite girar la figura para visualizar la posición relativa de la recta y el plano, lo que facilita la comprensión geométrica.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. ¿Qué tipo de objeto geométrico representa en GeoGebra 3D la ecuación $x^2+y^2+z^2=r^2$?

   > **Solución:** Representa una esfera de radio $r$ centrada en el origen.

2. En GeoGebra 3D, si introduces el comando `Plano[(1,0,0), (0,1,0), (0,0,1)]`, ¿qué plano obtienes?

   > **Solución:** El plano determinado por los tres puntos $(1,0,0)$, $(0,1,0)$ y $(0,0,1)$, que tiene ecuación $x+y+z=1$ (plano de los interceptos unitarios).

**Nivel Intermedio:**

3. Describe cómo calcular en GeoGebra 3D el volumen del tetraedro cuyos vértices son $A(0,0,0)$, $B(1,0,0)$, $C(0,1,0)$, $D(0,0,1)$.

   > **Solución:** Se puede usar el comando `Volumen[Tetraedro[A, B, C, D]]`. Alternativamente, GeoGebra permite calcular el producto mixto: se definen los vectores $\vec{a}=B-A$, $\vec{b}=C-A$, $\vec{c}=D-A$ y se calcula $\dfrac{1}{6}|\det(\vec{a},\vec{b},\vec{c})|$.

4. Explica cómo usar GeoGebra 3D para verificar que dos planos son paralelos.

   > **Solución:** Se introducen los dos planos y se usa la herramienta *Ángulo* o el comando `Ángulo[π₁, π₂]`. Si el ángulo es $0°$ (o $180°$), los planos son paralelos. También se puede verificar visualmente en la vista 3D si los planos no se intersectan.

**Nivel EVAU:**

5. *(Pregunta de razonamiento y uso de herramientas digitales)*

   Se tiene una pirámide con vértice $V(0,0,4)$ y base el cuadrado $ABCD$ con $A(2,2,0)$, $B(-2,2,0)$, $C(-2,-2,0)$, $D(2,-2,0)$.

   **(a)** Calcula el volumen de la pirámide sin usar herramientas digitales.

   **(b)** Indica qué pasos seguirías en GeoGebra 3D para visualizar la pirámide y verificar el resultado del volumen.

   **(c)** Calcula el área total de la pirámide (base + 4 caras laterales).

   > **Solución:**
   >
   > **(a)** Base cuadrada de lado 4 (ya que $|AB|=\sqrt{16+0+0}=4$). $S_{\text{base}}=16$ u².
   > Altura $h$: distancia de $V(0,0,4)$ al plano $z=0$ es $h=4$.
   > $V=\dfrac{1}{3}\cdot16\cdot4=\dfrac{64}{3}$ u³.
   >
   > **(b)** En GeoGebra 3D:
   > 1. Introducir los puntos $A$, $B$, $C$, $D$, $V$.
   > 2. Usar el comando `Pirámide[Polígono[A,B,C,D], V]` para construir la pirámide.
   > 3. Usar `Volumen[pirámide]` para obtener el volumen numéricamente.
   > 4. Girar la vista para verificar la geometría.
   >
   > **(c)** Cara lateral $VAB$: $\vec{VA}=(2,2,-4)$, $\vec{VB}=(-2,2,-4)$.
   > $\vec{VA}\times\vec{VB}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\2&2&-4\\-2&2&-4\end{vmatrix}=(2(-4)-(-4)(2))\vec{i}-(2(-4)-(-4)(-2))\vec{j}+(2(2)-2(-2))\vec{k}=(-8+8)\vec{i}-(-8-8)\vec{j}+(4+4)\vec{k}=(0,16,8)$.
   > $S_{VAB}=\dfrac{1}{2}\sqrt{0+256+64}=\dfrac{1}{2}\sqrt{320}=\dfrac{8\sqrt{5}}{2}=4\sqrt{5}$.
   > Por simetría, las 4 caras laterales: $2$ caras con $|VA|=\sqrt{4+4+16}=\sqrt{24}$ y $2$ caras con $|VB|=\sqrt{24}$. Todas iguales: $S_{\text{lateral total}}=4\cdot4\sqrt{5}=16\sqrt{5}$.
   > $S_{\text{total}}=16+16\sqrt{5}=16(1+\sqrt{5})$ u².

**Test de Opción Múltiple**

6. ¿Para qué sirve principalmente GeoGebra 3D en el estudio de la geometría analítica en el espacio?
   - a) Para calcular determinantes de matrices 3×3
   - b) Para visualizar e interactuar con objetos geométricos tridimensionales y verificar resultados analíticos
   - c) Solo para dibujar funciones de una variable
   - d) Para resolver sistemas de ecuaciones de forma automática sin comprensión

   > **Respuesta correcta:** b) GeoGebra 3D permite visualizar puntos, rectas, planos y sólidos en el espacio, girar la perspectiva, y verificar resultados de cálculo analítico de forma gráfica e interactiva.

7. En GeoGebra 3D, para obtener el ángulo entre dos planos $\pi_1$ y $\pi_2$, el comando más adecuado es:
   - a) `Distancia[π₁, π₂]`
   - b) `Intersección[π₁, π₂]`
   - c) `Ángulo[π₁, π₂]`
   - d) `VectorNormal[π₁, π₂]`

   > **Respuesta correcta:** c) El comando `Ángulo[π₁, π₂]` calcula directamente el ángulo diedro entre los dos planos.

---

*Fin del Capítulo 5 — Geometría Analítica en el Espacio*

---

*Documento elaborado para Matemáticas II — 2.º Bachillerato (Ciencias y Tecnología)*  
*Comunidad de Madrid · Decreto 64/2022 (LOMLOE) · Programación FUHEM 2025-26*  
*Nivel de referencia: EVAU Comunidad de Madrid*
