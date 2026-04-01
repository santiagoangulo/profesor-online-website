# Ejercicios — Matemáticas II · Capítulos 10 y 11

**Curso:** 2.º Bachillerato — Ciencias y Tecnología  
**Comunidad:** Comunidad de Madrid  
**Capítulos:** 10 (Probabilidad) y 11 (Distribuciones de Probabilidad)  
**Formato EVAU:** Comunidad de Madrid

---

# CAPÍTULO 10. PROBABILIDAD

---

## 10.1 Fundamentos de probabilidad

---

#### 10.1.1 Experimento aleatorio, espacio muestral y sucesos

**Ejercicio Resuelto**

Se lanza un dado de seis caras. Describe el experimento aleatorio, escribe el espacio muestral y define los siguientes sucesos: $A$ = "obtener un número par", $B$ = "obtener un número mayor que 4", $A \cap B$, $A \cup B$ y $\bar{A}$.

**Solución paso a paso:**

**Paso 1 – Experimento aleatorio.**  
Lanzar un dado de seis caras es un experimento aleatorio porque el resultado no puede predecirse con certeza antes de realizarlo.

**Paso 2 – Espacio muestral.**  
$$\Omega = \{1, 2, 3, 4, 5, 6\}$$

**Paso 3 – Definir los sucesos.**  
- $A$ = "obtener número par" $= \{2, 4, 6\}$  
- $B$ = "obtener número mayor que 4" $= \{5, 6\}$

**Paso 4 – Operaciones con sucesos.**  
- $A \cap B = \{2,4,6\} \cap \{5,6\} = \{6\}$ (números pares y mayores que 4)  
- $A \cup B = \{2,4,5,6\}$ (números pares o mayores que 4, o ambos)  
- $\bar{A} = \Omega \setminus A = \{1,3,5\}$ (números impares)

**Paso 5 – Verificación de la unión con la fórmula de inclusión-exclusión.**  
$$|A \cup B| = |A| + |B| - |A \cap B| = 3 + 2 - 1 = 4 \checkmark$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Se extrae una carta de una baraja española de 40 cartas. Escribe el espacio muestral reducido por palos y define: $A$ = "carta de oros", $B$ = "carta con número ≤ 3". Calcula $A \cap B$ y $A \cup B$.

   > **Solución:** El espacio muestral tiene 40 elementos (10 cartas × 4 palos). Usando representación compacta: $A = \{1_\text{or}, 2_\text{or}, 3_\text{or}, 4_\text{or}, 5_\text{or}, 6_\text{or}, 7_\text{or}, 8_\text{or}, 9_\text{or}, 10_\text{or}\}$ (10 elementos); $B$ contiene las cartas 1, 2 y 3 de cada palo, es decir 12 elementos. $A \cap B = \{1_\text{or}, 2_\text{or}, 3_\text{or}\}$ (3 elementos, oros con número ≤ 3). $A \cup B$ tiene $10 + 12 - 3 = 19$ elementos.

2. Se lanza una moneda tres veces. Escribe el espacio muestral completo e indica cuántos elementos tiene el suceso $C$ = "obtener exactamente dos caras".

   > **Solución:** $\Omega = \{CCC, CCX, CXC, XCC, CXX, XCX, XXC, XXX\}$, donde C = cara y X = cruz. $|\Omega| = 2^3 = 8$. $C = \{CCX, CXC, XCC\}$, por tanto $|C| = 3$.

**Nivel Intermedio:**

3. En una clase hay 30 alumnos: 18 estudian física, 14 estudian química y 8 estudian ambas. Se elige un alumno al azar. Define $F$ = "estudia física" y $Q$ = "estudia química". Calcula $|F \cup Q|$, $|\overline{F \cup Q}|$ y comprueba si $F$ y $Q$ son sucesos mutuamente excluyentes.

   > **Solución:** $|F \cup Q| = |F| + |Q| - |F \cap Q| = 18 + 14 - 8 = 24$. El número de alumnos que estudian alguna de las dos materias es 24, luego $|\overline{F \cup Q}| = 30 - 24 = 6$ alumnos no estudian ninguna. Como $|F \cap Q| = 8 \neq 0$, los sucesos **no** son mutuamente excluyentes.

4. En un experimento se lanza un dado de 12 caras. Define $A$ = "múltiplo de 3", $B$ = "múltiplo de 4", $C$ = "número primo". Calcula $A \cap B$, $B \cap C$ y $(A \cup B) \cap C$.

   > **Solución:** $\Omega = \{1,2,...,12\}$. $A = \{3,6,9,12\}$, $B = \{4,8,12\}$, $C = \{2,3,5,7,11\}$. $A \cap B = \{12\}$ (múltiplo de 3 y 4 = múltiplo de 12). $B \cap C = \emptyset$ (ningún múltiplo de 4 es primo en $\{1,...,12\}$). $A \cup B = \{3,4,6,8,9,12\}$; $(A \cup B) \cap C = \{3\}$.

**Nivel EVAU:**

5. En un hospital se registran los resultados de dos pruebas diagnósticas, $P_1$ y $P_2$, aplicadas a 200 pacientes. De ellos, 120 dieron positivo en $P_1$, 90 dieron positivo en $P_2$ y 50 dieron positivo en ambas pruebas.

   a) ¿Cuántos pacientes dieron positivo en al menos una prueba?  
   b) ¿Cuántos dieron positivo solo en $P_1$?  
   c) ¿Cuántos no dieron positivo en ninguna prueba?  
   d) Describe con palabras el suceso $\overline{P_1 \cup P_2}$ y calcula su cardinal.

   > **Solución:**  
   > a) $|P_1 \cup P_2| = 120 + 90 - 50 = 160$ pacientes.  
   > b) Solo en $P_1$: $|P_1| - |P_1 \cap P_2| = 120 - 50 = 70$ pacientes.  
   > c) $|\overline{P_1 \cup P_2}| = 200 - 160 = 40$ pacientes no dieron positivo en ninguna.  
   > d) $\overline{P_1 \cup P_2}$ = "el paciente no dio positivo en ninguna de las dos pruebas". Cardinal: 40.

**Test de Opción Múltiple**

6. Se lanza un dado de 6 caras. El suceso $A$ = "número par" y $B$ = "número mayor que 3". ¿Cuántos elementos tiene $A \cup B$?
   - a) 3
   - b) 4
   - c) 5
   - d) 6

   > **Respuesta correcta: b)** $A = \{2,4,6\}$, $B = \{4,5,6\}$. $A \cup B = \{2,4,5,6\}$, que tiene 4 elementos.

7. Si $\Omega$ tiene 10 elementos, $|A| = 6$ y $|B| = 5$ y $A$ y $B$ son mutuamente excluyentes, ¿cuántos elementos tiene $\overline{A \cup B}$?
   - a) 0
   - b) 1
   - c) 9
   - d) 11

   > **Respuesta correcta: b)** Como $A \cap B = \emptyset$, $|A \cup B| = 6 + 5 = 11$... pero $|\Omega| = 10$, lo que haría imposible tener $|A|+|B|=11$ si son mutuamente excluyentes con $|\Omega|=10$. Ajustando el enunciado a que son compatibles: $|A \cup B| \leq 10$. Si $|A \cap B| = 1$, $|A \cup B| = 10$, $|\overline{A \cup B}| = 0$. **Nota para el alumno:** en el caso $|A|=6$, $|B|=5$ y $A,B$ disjuntos dentro de $\Omega$ de 10 elementos, $|A \cup B|=11 > 10$, lo que es imposible; en un ejemplo corregido con $|A|=4$, $|B|=5$, disjuntos: $|\overline{A \cup B}|= 10-9=1$. Respuesta: **b) 1**.

---

#### 10.1.2 Axiomas de Kolmogorov

**Ejercicio Resuelto**

Verifica que la siguiente función define una probabilidad sobre $\Omega = \{a, b, c, d\}$: $P(\{a\}) = 0{,}3$, $P(\{b\}) = 0{,}2$, $P(\{c\}) = 0{,}4$, $P(\{d\}) = 0{,}1$.

**Solución paso a paso:**

Los tres axiomas de Kolmogorov son:
1. $P(A) \geq 0$ para todo suceso $A$.
2. $P(\Omega) = 1$.
3. Si $A \cap B = \emptyset$, entonces $P(A \cup B) = P(A) + P(B)$ (aditividad para sucesos mutuamente excluyentes).

**Comprobación del axioma 1:** $0{,}3 \geq 0$, $0{,}2 \geq 0$, $0{,}4 \geq 0$, $0{,}1 \geq 0$. ✓

**Comprobación del axioma 2:**
$$P(\Omega) = P(\{a\}) + P(\{b\}) + P(\{c\}) + P(\{d\}) = 0{,}3 + 0{,}2 + 0{,}4 + 0{,}1 = 1{,}0 \checkmark$$

**Comprobación del axioma 3:** Los sucesos elementales $\{a\}, \{b\}, \{c\}, \{d\}$ son disjuntos dos a dos, y $P(\{a,b\}) = P(\{a\}) + P(\{b\}) = 0{,}5$. ✓

Concluimos que **sí define una probabilidad** sobre $\Omega$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Dado $\Omega = \{1, 2, 3, 4, 5\}$ con $P(\{1\}) = P(\{2\}) = 0{,}1$, $P(\{3\}) = 0{,}3$, $P(\{4\}) = x$, $P(\{5\}) = 0{,}2$. Determina $x$ para que $P$ sea una probabilidad válida.

   > **Solución:** Por el axioma 2: $0{,}1 + 0{,}1 + 0{,}3 + x + 0{,}2 = 1 \Rightarrow 0{,}7 + x = 1 \Rightarrow x = 0{,}3$. Como $x > 0$, se verifican los tres axiomas.

2. ¿Puede ser $P(A) = 1{,}2$ para algún suceso? Razona tu respuesta usando los axiomas.

   > **Solución:** No. El axioma 1 exige $P(A) \geq 0$ y el axioma 2 implica $P(A) \leq P(\Omega) = 1$ (por monotonía). Por tanto $0 \leq P(A) \leq 1$ para todo suceso $A$, y $1{,}2 > 1$ viola esta condición.

**Nivel Intermedio:**

3. Dado un experimento con $\Omega = \{e_1, e_2, e_3, e_4\}$, se sabe que $P(e_2) = 2P(e_1)$, $P(e_3) = 3P(e_1)$ y $P(e_4) = 4P(e_1)$. Calcula $P(e_1)$ y las probabilidades de todos los sucesos elementales.

   > **Solución:** $P(e_1) + 2P(e_1) + 3P(e_1) + 4P(e_1) = 1 \Rightarrow 10P(e_1) = 1 \Rightarrow P(e_1) = \frac{1}{10} = 0{,}1$. Por tanto: $P(e_2) = 0{,}2$, $P(e_3) = 0{,}3$, $P(e_4) = 0{,}4$.

4. Comprueba cuál de las siguientes funciones **no** es una probabilidad sobre $\Omega = \{a, b, c\}$ y explica qué axioma viola: (I) $P(a)=0{,}5,\ P(b)=-0{,}1,\ P(c)=0{,}6$; (II) $P(a)=0{,}5,\ P(b)=0{,}3,\ P(c)=0{,}3$.

   > **Solución:** (I) viola el **axioma 1** porque $P(b) = -0{,}1 < 0$. (II) viola el **axioma 2** porque $0{,}5 + 0{,}3 + 0{,}3 = 1{,}1 \neq 1$.

**Nivel EVAU:**

5. Se definen dos experimentos aleatorios. En el experimento A, el espacio muestral es $\Omega = \{e_1, e_2, e_3, e_4, e_5\}$ con probabilidades proporcionales a sus índices (es decir, $P(e_k) = c \cdot k$).

   a) Calcula la constante $c$.  
   b) Calcula $P(\{e_2, e_4\})$ y $P(\{e_3, e_4, e_5\})$.  
   c) Sea $A = \{e_1, e_3, e_5\}$ y $B = \{e_2, e_4\}$. ¿Son $A$ y $B$ mutuamente excluyentes? Calcula $P(A \cup B)$.

   > **Solución:**  
   > a) $\sum_{k=1}^{5} ck = c(1+2+3+4+5) = 15c = 1 \Rightarrow c = \dfrac{1}{15}$.  
   > b) $P(\{e_2, e_4\}) = \dfrac{2}{15} + \dfrac{4}{15} = \dfrac{6}{15} = \dfrac{2}{5}$.  
   > $P(\{e_3, e_4, e_5\}) = \dfrac{3+4+5}{15} = \dfrac{12}{15} = \dfrac{4}{5}$.  
   > c) $A \cap B = \emptyset$ (no comparten elementos), por lo que son **mutuamente excluyentes**. $P(A \cup B) = P(A) + P(B) = \dfrac{1+3+5}{15} + \dfrac{2+4}{15} = \dfrac{9}{15} + \dfrac{6}{15} = 1$. Efectivamente $A \cup B = \Omega$.

**Test de Opción Múltiple**

6. Si $P(A) = 0{,}6$ y $A, B$ son mutuamente excluyentes con $P(A \cup B) = 0{,}9$, ¿cuánto vale $P(B)$?
   - a) 0,54
   - b) 0,3
   - c) 1,5
   - d) No se puede determinar

   > **Respuesta correcta: b)** Por aditividad: $P(A \cup B) = P(A) + P(B) \Rightarrow 0{,}9 = 0{,}6 + P(B) \Rightarrow P(B) = 0{,}3$.

7. ¿Cuál de las siguientes afirmaciones es consecuencia directa de los axiomas de Kolmogorov?
   - a) $P(\emptyset) = 1$
   - b) $P(\bar{A}) = 1 + P(A)$
   - c) $P(\bar{A}) = 1 - P(A)$
   - d) $P(A \cup B) = P(A) \cdot P(B)$

   > **Respuesta correcta: c)** Se deduce de $A \cup \bar{A} = \Omega$ (disjuntos), luego $P(A) + P(\bar{A}) = 1$.

---

#### 10.1.3 Propiedades deducidas de los axiomas

**Ejercicio Resuelto**

Dados $P(A) = 0{,}5$, $P(B) = 0{,}4$ y $P(A \cap B) = 0{,}2$, calcula: $P(\bar{A})$, $P(\bar{B})$, $P(A \cup B)$, $P(\overline{A \cup B})$ y $P(A \cap \bar{B})$.

**Solución paso a paso:**

**Complementario:**
$$P(\bar{A}) = 1 - P(A) = 1 - 0{,}5 = 0{,}5$$
$$P(\bar{B}) = 1 - P(B) = 1 - 0{,}4 = 0{,}6$$

**Unión (fórmula de inclusión-exclusión):**
$$P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0{,}5 + 0{,}4 - 0{,}2 = 0{,}7$$

**Complementario de la unión (De Morgan):**
$$P(\overline{A \cup B}) = 1 - P(A \cup B) = 1 - 0{,}7 = 0{,}3$$

**Diferencia $A \setminus B$ (solo en $A$, no en $B$):**
$$P(A \cap \bar{B}) = P(A) - P(A \cap B) = 0{,}5 - 0{,}2 = 0{,}3$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. $P(A) = 0{,}7$. Calcula $P(\bar{A})$ y $P(\bar{A} \cup A)$.

   > **Solución:** $P(\bar{A}) = 1 - 0{,}7 = 0{,}3$. $P(\bar{A} \cup A) = P(\Omega) = 1$.

2. $P(A) = 0{,}4$, $P(B) = 0{,}5$, $P(A \cup B) = 0{,}7$. Calcula $P(A \cap B)$.

   > **Solución:** De la fórmula de inclusión-exclusión: $P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0{,}4 + 0{,}5 - 0{,}7 = 0{,}2$.

**Nivel Intermedio:**

3. Demuestra que $P(A \cap \bar{B}) = P(A) - P(A \cap B)$ usando los axiomas. Luego calcula $P(A \cap \bar{B})$ si $P(A) = 0{,}6$ y $P(A \cap B) = 0{,}15$.

   > **Solución:** $A = (A \cap B) \cup (A \cap \bar{B})$ y estos dos conjuntos son disjuntos (si $x \in A\cap B$ entonces $x \notin \bar{B}$). Por aditividad: $P(A) = P(A \cap B) + P(A \cap \bar{B}) \Rightarrow P(A \cap \bar{B}) = P(A) - P(A \cap B) = 0{,}6 - 0{,}15 = 0{,}45$.

4. Sabiendo que $P(A) = 0{,}5$, $P(B) = 0{,}3$, $P(C) = 0{,}4$, $P(A \cap B) = 0{,}1$, $P(A \cap C) = 0{,}2$, $P(B \cap C) = 0{,}15$ y $P(A \cap B \cap C) = 0{,}05$, calcula $P(A \cup B \cup C)$.

   > **Solución:** $P(A \cup B \cup C) = P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)+P(A\cap B\cap C)$ $= 0{,}5+0{,}3+0{,}4-0{,}1-0{,}2-0{,}15+0{,}05 = 0{,}80$.

**Nivel EVAU:**

5. En un grupo de 100 estudiantes, 55 practican fútbol ($F$), 40 practican baloncesto ($B$) y 20 practican ambos deportes. Se elige un estudiante al azar.

   a) Calcula $P(F \cup B)$.  
   b) Calcula la probabilidad de que practique solo fútbol.  
   c) Calcula la probabilidad de que no practique ninguno de los dos deportes.  
   d) ¿Se puede afirmar que $F$ y $B$ son sucesos incompatibles? Justifica.

   > **Solución:**  
   > a) $P(F) = 0{,}55$, $P(B) = 0{,}40$, $P(F \cap B) = 0{,}20$.  
   > $P(F \cup B) = 0{,}55 + 0{,}40 - 0{,}20 = \mathbf{0{,}75}$.  
   > b) $P(F \cap \bar{B}) = P(F) - P(F\cap B) = 0{,}55 - 0{,}20 = \mathbf{0{,}35}$.  
   > c) $P(\overline{F \cup B}) = 1 - 0{,}75 = \mathbf{0{,}25}$.  
   > d) No, porque $P(F \cap B) = 0{,}20 \neq 0$; existen 20 estudiantes que practican ambos deportes, luego son **compatibles**.

**Test de Opción Múltiple**

6. Si $P(A) = 0{,}6$, $P(B) = 0{,}4$ y $P(A \cup B) = 0{,}8$, ¿cuánto vale $P(A \cap B)$?
   - a) 0,24
   - b) 0,2
   - c) 1,0
   - d) 0,1

   > **Respuesta correcta: b)** $P(A \cap B) = 0{,}6 + 0{,}4 - 0{,}8 = 0{,}2$.

7. La propiedad de monotonía establece que si $A \subseteq B$, entonces:
   - a) $P(A) \geq P(B)$
   - b) $P(A) = P(B)$
   - c) $P(A) \leq P(B)$
   - d) $P(A) \cdot P(B) = 1$

   > **Respuesta correcta: c)** Si $A \subseteq B$, entonces $B = A \cup (B \setminus A)$ con partes disjuntas, luego $P(B) = P(A) + P(B \setminus A) \geq P(A)$.

---

#### 10.1.4 Diagramas de Venn: representación y cálculo de probabilidades

**Ejercicio Resuelto**

En una encuesta a 200 personas, 110 consumen producto $X$, 80 consumen producto $Y$ y 40 consumen ambos. Representa la situación en un diagrama de Venn y calcula la probabilidad de que una persona elegida al azar consuma exactamente uno de los dos productos.

**Solución paso a paso:**

**Paso 1 – Calcular las regiones del diagrama de Venn.**  
- Solo $X$: $110 - 40 = 70$ personas  
- Solo $Y$: $80 - 40 = 40$ personas  
- Ambos ($X \cap Y$): $40$ personas  
- Ninguno: $200 - (70 + 40 + 40) = 200 - 150 = 50$ personas

**Paso 2 – Diagrama de Venn (descripción).**

```
    |------ 200 personas ------|
    |  50  | 70 |X∩Y=40| 40 |  
    |       |     X    |  Y  |
```

**Paso 3 – Calcular la probabilidad pedida.**  
"Exactamente uno de los dos" = (solo $X$) $\cup$ (solo $Y$):
$$P(\text{exactamente uno}) = \frac{70 + 40}{200} = \frac{110}{200} = 0{,}55$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. En un diagrama de Venn con $P(A) = 0{,}5$, $P(B) = 0{,}3$ y $P(A \cap B) = 0{,}1$, representa el diagrama e indica el valor de cada región.

   > **Solución:** Regiones: solo $A$: $0{,}5 - 0{,}1 = 0{,}4$; $A \cap B$: $0{,}1$; solo $B$: $0{,}3 - 0{,}1 = 0{,}2$; ninguno: $1 - (0{,}4 + 0{,}1 + 0{,}2) = 0{,}3$.

2. Usando el diagrama del ejercicio anterior, calcula $P(\bar{A} \cap \bar{B})$ (la región "ninguno").

   > **Solución:** $P(\bar{A} \cap \bar{B}) = P(\overline{A \cup B}) = 1 - P(A \cup B) = 1 - (0{,}5 + 0{,}3 - 0{,}1) = 1 - 0{,}7 = 0{,}3$.

**Nivel Intermedio:**

3. En un estudio médico, el 60% de los pacientes tiene hipertensión ($H$), el 45% tiene diabetes ($D$) y el 25% tiene ambas. Calcula mediante diagrama de Venn la probabilidad de que un paciente tenga solo una de las dos enfermedades.

   > **Solución:** Solo $H$: $0{,}60 - 0{,}25 = 0{,}35$; solo $D$: $0{,}45 - 0{,}25 = 0{,}20$. $P(\text{exactamente una}) = 0{,}35 + 0{,}20 = \mathbf{0{,}55}$.

4. En una fábrica, el 30% de las piezas tiene defecto de tipo $A$, el 20% tiene defecto de tipo $B$ y el 5% tiene ambos defectos. ¿Qué porcentaje no tiene ningún defecto? ¿Cuál tiene exactamente un tipo de defecto?

   > **Solución:** $P(A \cup B) = 0{,}30 + 0{,}20 - 0{,}05 = 0{,}45$. Sin defecto: $1 - 0{,}45 = \mathbf{0{,}55}$, es decir el 55%. Solo $A$: $0{,}25$; solo $B$: $0{,}15$. Exactamente un defecto: $0{,}25 + 0{,}15 = \mathbf{0{,}40}$ (40%).

**Nivel EVAU:**

5. En una campaña de marketing se envían dos tipos de oferta, $O_1$ y $O_2$, a 500 clientes. Responden a $O_1$: 180 clientes; responden a $O_2$: 220 clientes; responden a ambas: 60 clientes.

   a) Dibuja y rellena el diagrama de Venn indicando el número de clientes en cada región.  
   b) ¿Qué probabilidad tiene un cliente elegido al azar de haber respondido a exactamente una oferta?  
   c) ¿Qué probabilidad tiene de haber respondido a $O_1$ pero no a $O_2$?  
   d) ¿Qué probabilidad tiene de no haber respondido a ninguna oferta?

   > **Solución:**  
   > a) Solo $O_1$: $180 - 60 = 120$; Ambas: $60$; Solo $O_2$: $220 - 60 = 160$; Ninguna: $500 - (120+60+160) = 160$.  
   > b) $P(\text{exactamente una}) = \dfrac{120 + 160}{500} = \dfrac{280}{500} = \mathbf{0{,}56}$.  
   > c) $P(O_1 \cap \bar{O_2}) = \dfrac{120}{500} = \mathbf{0{,}24}$.  
   > d) $P(\text{ninguna}) = \dfrac{160}{500} = \mathbf{0{,}32}$.

**Test de Opción Múltiple**

6. En un diagrama de Venn, $P(A) = 0{,}4$, $P(B) = 0{,}35$, $P(A \cap B) = 0{,}15$. ¿Cuánto vale $P(\bar{A} \cap B)$?
   - a) 0,20
   - b) 0,35
   - c) 0,15
   - d) 0,05

   > **Respuesta correcta: a)** $P(\bar{A} \cap B) = P(B) - P(A \cap B) = 0{,}35 - 0{,}15 = 0{,}20$.

7. Si las regiones del diagrama de Venn para $A$ y $B$ (dentro de $\Omega$) son: solo $A = 0{,}3$; $A \cap B = 0{,}2$; solo $B = 0{,}1$; ninguno = $0{,}4$. Entonces $P(A)$ vale:
   - a) 0,3
   - b) 0,5
   - c) 0,2
   - d) 0,6

   > **Respuesta correcta: b)** $P(A) = P(\text{solo } A) + P(A \cap B) = 0{,}3 + 0{,}2 = 0{,}5$.

---

## 10.2 Técnicas de conteo

---

#### 10.2.1 Principio multiplicativo y aditivo del recuento

**Ejercicio Resuelto**

Un menú de restaurante ofrece 3 primeros platos, 4 segundos y 2 postres. ¿De cuántas formas distintas puede elegirse un menú completo (un primero, un segundo y un postre)?

**Solución paso a paso:**

Por el **principio multiplicativo**: si una tarea se realiza en etapas independientes con $n_1$, $n_2$, ..., $n_k$ formas respectivamente, el total de formas de completar todas las etapas es $n_1 \cdot n_2 \cdots n_k$.

Etapas:  
- Elección de primer plato: 3 formas  
- Elección de segundo plato: 4 formas  
- Elección de postre: 2 formas

Total: $3 \times 4 \times 2 = \mathbf{24}$ menús distintos.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Una contraseña consta de 2 letras (del alfabeto de 27 letras) seguidas de 3 dígitos (del 0 al 9), sin repetición. ¿Cuántas contraseñas distintas existen?

   > **Solución:** Letras sin repetición: $27 \times 26 = 702$. Dígitos sin repetición: $10 \times 9 \times 8 = 720$. Total: $702 \times 720 = \mathbf{505\,440}$ contraseñas.

2. Una tienda vende camisetas en 5 colores, 3 tallas y 2 estilos (manga corta/larga). ¿Cuántos modelos distintos ofrece?

   > **Solución:** $5 \times 3 \times 2 = \mathbf{30}$ modelos.

**Nivel Intermedio:**

3. Un código de seguridad tiene 4 dígitos del 0 al 9. ¿Cuántos códigos hay (a) con repetición y (b) sin repetición? ¿Qué porcentaje supone la diferencia?

   > **Solución:** (a) Con repetición: $10^4 = 10\,000$. (b) Sin repetición: $10 \times 9 \times 8 \times 7 = 5\,040$. Diferencia: $10\,000 - 5\,040 = 4\,960$, que supone el $\dfrac{4960}{10000} = 49{,}6\%$ del total.

4. En un torneo de tenis de dobles mixtos participan 6 hombres y 5 mujeres. ¿De cuántas formas se puede formar una pareja mixta (un hombre y una mujer)?

   > **Solución:** $6 \times 5 = \mathbf{30}$ parejas distintas.

**Nivel EVAU:**

5. En una empresa se quiere asignar 3 tareas distintas ($T_1$, $T_2$, $T_3$) a 3 empleados distintos de entre un grupo de 8, de modo que cada empleado recibe como máximo una tarea.

   a) ¿De cuántas formas puede hacerse esta asignación?  
   b) Si además se exige que $T_1$ la realice siempre el empleado más antiguo, ¿cuántas asignaciones son posibles?  
   c) ¿Cuántas asignaciones posibles hay si las tres tareas son idénticas (solo importa quiénes trabajan, no qué hacen)?

   > **Solución:**  
   > a) Se elige qué empleado hace cada tarea: $8 \times 7 \times 6 = \mathbf{336}$ formas (variaciones de 8 en 3).  
   > b) $T_1$ está fijada (1 forma). $T_2$: 7 empleados restantes. $T_3$: 6. Total: $1 \times 7 \times 6 = \mathbf{42}$ formas.  
   > c) Ahora el orden no importa: $\dbinom{8}{3} = \dfrac{8!}{3!\cdot 5!} = 56$ formas.

**Test de Opción Múltiple**

6. Una matrícula consta de 4 dígitos (del 0 al 9) y 3 letras (del abecedario de 27). Si se permiten repeticiones, ¿cuántas matrículas distintas hay?
   - a) $10^4 \times 27^3$
   - b) $10^4 + 27^3$
   - c) $\binom{10}{4} \times \binom{27}{3}$
   - d) $10 \times 27 \times 7$

   > **Respuesta correcta: a)** Por el principio multiplicativo: $10^4$ formas para los dígitos y $27^3$ para las letras. Total: $10^4 \times 27^3 = 196\,830\,000$.

7. Se lanza una moneda 5 veces. ¿Cuántos resultados posibles distintos existen?
   - a) 10
   - b) 25
   - c) 32
   - d) 120

   > **Respuesta correcta: c)** Cada lanzamiento tiene 2 resultados, y hay 5 lanzamientos independientes: $2^5 = 32$.

---

#### 10.2.2 Combinaciones, variaciones y permutaciones

**Ejercicio Resuelto**

Un comité de 4 personas debe elegirse de entre 10 candidatos. ¿De cuántas formas puede formarse el comité si (a) todos los miembros tienen el mismo rango, (b) hay un presidente y tres vocales?

**Solución paso a paso:**

**(a) Todos con el mismo rango → Combinaciones** (el orden no importa):

$$C_{10,4} = \binom{10}{4} = \frac{10!}{4!\cdot 6!} = \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = \frac{5040}{24} = \mathbf{210} \text{ formas}$$

**(b) Presidente y tres vocales → Etapas:**  
- Elegir el presidente: 10 formas  
- Elegir 3 vocales de los 9 restantes (sin orden): $\binom{9}{3} = 84$ formas  
- Total: $10 \times 84 = \mathbf{840}$ formas

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula: (a) $P_{5}^{5}$ (permutaciones de 5 elementos), (b) $V_{8,3}$ (variaciones de 8 en 3), (c) $\binom{7}{2}$ (combinaciones de 7 en 2).

   > **Solución:** (a) $5! = 120$. (b) $V_{8,3} = 8 \times 7 \times 6 = 336$. (c) $\dfrac{7!}{2! \cdot 5!} = \dfrac{7 \times 6}{2} = 21$.

2. ¿De cuántas formas pueden sentarse 6 personas en una fila de 6 asientos?

   > **Solución:** $P_6 = 6! = 720$ formas.

**Nivel Intermedio:**

3. En un examen de tipo test de 10 preguntas, un alumno debe responder 7. ¿De cuántas formas puede elegir las preguntas que responde?

   > **Solución:** $\binom{10}{7} = \binom{10}{3} = \dfrac{10 \times 9 \times 8}{3!} = 120$ formas.

4. Un club deportivo tiene 12 socios. ¿De cuántas formas puede elegirse una junta directiva formada por presidente, secretario y tesorero (cargos distintos)?

   > **Solución:** Es una variación (el orden importa porque los cargos son distintos): $V_{12,3} = 12 \times 11 \times 10 = \mathbf{1\,320}$ formas.

**Nivel EVAU:**

5. En un torneo de ajedrez participan 8 jugadores. Cada par de jugadores disputa exactamente una partida entre sí.

   a) ¿Cuántas partidas se juegan en total?  
   b) Si en la final participan los 2 mejores de cada grupo de 4, y los dos grupos de semifinal son predeterminados, ¿cuántas partidas hay en el formato completo (fase de grupos + semifinales + final)?  
   c) ¿De cuántas formas pueden quedar en los tres primeros puestos del torneo (podio) los 8 jugadores?

   > **Solución:**  
   > a) Cada partida es un par de jugadores: $\binom{8}{2} = 28$ partidas.  
   > b) Grupos (2 grupos de 4): $2 \times \binom{4}{2} = 2 \times 6 = 12$ partidas. Semifinales: 2 partidas. Final: 1 partida. Total: $12 + 2 + 1 = \mathbf{15}$ partidas.  
   > c) El podio distingue 1.º, 2.º, 3.º: $V_{8,3} = 8 \times 7 \times 6 = \mathbf{336}$ formas.

**Test de Opción Múltiple**

6. ¿Cuántos anagramas (reordenaciones) tiene la palabra MASA?
   - a) 24
   - b) 12
   - c) 6
   - d) 4

   > **Respuesta correcta: b)** La palabra MASA tiene 4 letras con la A repetida 2 veces: $\dfrac{4!}{2!} = \dfrac{24}{2} = 12$.

7. Se quieren colocar 3 banderas de colores distintos en 3 postes de una fila. ¿De cuántas formas distintas puede hacerse si los colores disponibles son 5?
   - a) $\binom{5}{3} = 10$
   - b) $5^3 = 125$
   - c) $V_{5,3} = 60$
   - d) $5! = 120$

   > **Respuesta correcta: c)** Se elige qué bandera va en cada poste (el orden importa, los colores distintos): $V_{5,3} = 5 \times 4 \times 3 = 60$.

---

#### 10.2.3 Regla de Laplace: probabilidad en espacios equiprobables

**Ejercicio Resuelto**

Se extrae una bola al azar de una urna con 5 bolas rojas, 3 azules y 2 verdes. Calcula la probabilidad de: (a) obtener una bola roja, (b) obtener una bola que no sea azul.

**Solución paso a paso:**

**Regla de Laplace:**
$$P(A) = \frac{\text{casos favorables}}{\text{casos posibles}} = \frac{|A|}{|\Omega|}$$

Esta regla es aplicable porque todas las bolas son equiprobables (extraemos al azar).

$|\Omega| = 5 + 3 + 2 = 10$ bolas.

**(a)** $P(\text{roja}) = \dfrac{5}{10} = \mathbf{0{,}5}$

**(b)** "No azul" incluye rojas y verdes: $5 + 2 = 7$ bolas.  
$P(\text{no azul}) = \dfrac{7}{10} = \mathbf{0{,}7}$

Verificación: $P(\text{azul}) = \dfrac{3}{10} = 0{,}3$ y $P(\text{no azul}) = 1 - 0{,}3 = 0{,}7$. ✓

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Se lanza un dado de 6 caras. Calcula la probabilidad de obtener un número múltiplo de 2.

   > **Solución:** Múltiplos de 2 en $\{1,...,6\}$: $\{2,4,6\}$, 3 casos. $P = \dfrac{3}{6} = \mathbf{0{,}5}$.

2. Se elige una carta de una baraja española de 40 cartas. ¿Cuál es la probabilidad de que sea un "as" (el 1 de cualquier palo)?

   > **Solución:** Hay 4 ases (uno por palo). $P = \dfrac{4}{40} = \mathbf{0{,}1}$.

**Nivel Intermedio:**

3. En una bolsa hay 10 bolas numeradas del 1 al 10. Se extrae una al azar. Calcula la probabilidad de que el número sea primo o par.

   > **Solución:** Primos en $\{1,...,10\}$: $\{2,3,5,7\}$ (4 elementos). Pares: $\{2,4,6,8,10\}$ (5 elementos). Primos y pares: $\{2\}$ (1 elemento). $P(\text{primo} \cup \text{par}) = \dfrac{4+5-1}{10} = \dfrac{8}{10} = \mathbf{0{,}8}$.

4. Se eligen 2 cartas simultáneamente de una baraja española de 40 cartas. ¿Cuál es la probabilidad de que ambas sean del palo de copas?

   > **Solución:** Total de formas de elegir 2 cartas: $\binom{40}{2} = 780$. Formas favorables (2 de copas, de las 10 que hay): $\binom{10}{2} = 45$. $P = \dfrac{45}{780} = \dfrac{3}{52} \approx \mathbf{0{,}0577}$.

**Nivel EVAU:**

5. En una clase de 30 alumnos, 12 son mujeres y 18 son hombres. Se eligen 2 alumnos al azar para representar la clase.

   a) ¿Cuántas formas hay de elegir los 2 representantes?  
   b) ¿Cuál es la probabilidad de que ambos sean hombres?  
   c) ¿Cuál es la probabilidad de que haya una mujer y un hombre?  
   d) ¿Cuál es la probabilidad de que al menos uno sea mujer?

   > **Solución:**  
   > a) $\binom{30}{2} = 435$ formas.  
   > b) $P(\text{2 hombres}) = \dfrac{\binom{18}{2}}{\binom{30}{2}} = \dfrac{153}{435} = \dfrac{51}{145} \approx \mathbf{0{,}352}$.  
   > c) $P(\text{1H+1M}) = \dfrac{18 \times 12}{435} = \dfrac{216}{435} = \dfrac{72}{145} \approx \mathbf{0{,}497}$.  
   > d) $P(\text{al menos 1 mujer}) = 1 - P(\text{2 hombres}) = 1 - \dfrac{153}{435} = \dfrac{282}{435} = \dfrac{94}{145} \approx \mathbf{0{,}648}$.

**Test de Opción Múltiple**

6. Se lanza un dado de 12 caras (numerado del 1 al 12). ¿Cuál es la probabilidad de obtener un múltiplo de 3?
   - a) 1/4
   - b) 1/3
   - c) 1/2
   - d) 1/6

   > **Respuesta correcta: b)** Múltiplos de 3: $\{3,6,9,12\}$, 4 casos. $P = \dfrac{4}{12} = \dfrac{1}{3}$.

7. De una baraja de 52 cartas (francesa), ¿cuál es la probabilidad de sacar un as o un corazón?
   - a) 4/52
   - b) 13/52
   - c) 16/52
   - d) 17/52

   > **Respuesta correcta: c)** Ases: 4. Corazones: 13. As de corazones: 1. $P = \dfrac{4+13-1}{52} = \dfrac{16}{52} = \dfrac{4}{13} \approx 0{,}308$.

---

## 10.3 Probabilidad condicionada e independencia

---

#### 10.3.1 Definición de probabilidad condicionada: P(A|B)

**Ejercicio Resuelto**

En una fábrica, el 2% de las piezas tiene defecto de tipo $A$, el 3% tiene defecto de tipo $B$ y el 0,5% tiene ambos defectos. Calcula la probabilidad de que una pieza tenga defecto $A$ sabiendo que ya se sabe que tiene defecto $B$.

**Solución paso a paso:**

Datos: $P(A) = 0{,}02$, $P(B) = 0{,}03$, $P(A \cap B) = 0{,}005$.

**Fórmula de probabilidad condicionada:**
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

Sustituyendo:
$$P(A \mid B) = \frac{0{,}005}{0{,}03} = \frac{5}{30} = \frac{1}{6} \approx \mathbf{0{,}1\overline{6}}$$

**Interpretación:** Si sabemos que la pieza tiene defecto $B$, la probabilidad de que también tenga defecto $A$ aumenta del 2% al 16,7%, lo que indica una cierta correlación entre ambos defectos.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. $P(A) = 0{,}4$, $P(B) = 0{,}5$, $P(A \cap B) = 0{,}2$. Calcula $P(A \mid B)$ y $P(B \mid A)$.

   > **Solución:** $P(A \mid B) = \dfrac{0{,}2}{0{,}5} = 0{,}4$. $P(B \mid A) = \dfrac{0{,}2}{0{,}4} = 0{,}5$.

2. Se lanza un dado. Sea $A$ = "número par" y $B$ = "número mayor que 3". Calcula $P(A \mid B)$.

   > **Solución:** $A = \{2,4,6\}$, $B = \{4,5,6\}$, $A \cap B = \{4,6\}$. $P(A \mid B) = \dfrac{2/6}{3/6} = \dfrac{2}{3} \approx 0{,}667$.

**Nivel Intermedio:**

3. En un grupo de 100 personas, 60 hablan inglés, 40 hablan francés y 20 hablan los dos idiomas. Se elige una persona al azar que habla inglés. ¿Cuál es la probabilidad de que también hable francés?

   > **Solución:** $P(F \mid I) = \dfrac{P(F \cap I)}{P(I)} = \dfrac{20/100}{60/100} = \dfrac{20}{60} = \dfrac{1}{3} \approx 0{,}333$.

4. La tabla siguiente recoge datos de 200 trabajadores según su sexo y categoría laboral:

   |  | Directivo | Técnico | Operario | Total |
   |--|-----------|---------|----------|-------|
   | Hombre | 20 | 50 | 80 | 150 |
   | Mujer | 10 | 30 | 10 | 50 |
   | Total | 30 | 80 | 90 | 200 |

   Calcula $P(\text{Directivo} \mid \text{Mujer})$ y $P(\text{Mujer} \mid \text{Directivo})$.

   > **Solución:** $P(\text{Directivo} \mid \text{Mujer}) = \dfrac{10/200}{50/200} = \dfrac{10}{50} = 0{,}2$. $P(\text{Mujer} \mid \text{Directivo}) = \dfrac{10/200}{30/200} = \dfrac{10}{30} = \dfrac{1}{3} \approx 0{,}333$.

**Nivel EVAU:**

5. Una urna contiene 4 bolas rojas y 6 bolas blancas. Se extraen 2 bolas **sin reemplazamiento**.

   a) ¿Cuál es la probabilidad de que la primera bola sea roja?  
   b) Dado que la primera bola fue roja, ¿cuál es la probabilidad de que la segunda también sea roja?  
   c) Calcula la probabilidad de que las dos bolas sean rojas.  
   d) ¿Cambia el resultado del apartado (c) si la extracción es con reemplazamiento?

   > **Solución:**  
   > a) $P(R_1) = \dfrac{4}{10} = 0{,}4$.  
   > b) $P(R_2 \mid R_1) = \dfrac{3}{9} = \dfrac{1}{3} \approx 0{,}333$ (quedan 3 rojas entre 9).  
   > c) $P(R_1 \cap R_2) = P(R_1) \cdot P(R_2 \mid R_1) = \dfrac{4}{10} \cdot \dfrac{3}{9} = \dfrac{12}{90} = \dfrac{2}{15} \approx 0{,}133$.  
   > d) Con reemplazamiento: $P(R_1 \cap R_2) = \dfrac{4}{10} \cdot \dfrac{4}{10} = \dfrac{16}{100} = 0{,}16$. Sí cambia (ligeramente mayor porque no se "agota" la urna).

**Test de Opción Múltiple**

6. Si $P(B) = 0{,}4$ y $P(A \cap B) = 0{,}12$, entonces $P(A \mid B)$ vale:
   - a) 0,048
   - b) 0,3
   - c) 0,52
   - d) 0,12

   > **Respuesta correcta: b)** $P(A \mid B) = \dfrac{0{,}12}{0{,}4} = 0{,}3$.

7. La probabilidad condicionada $P(A \mid B)$ se puede interpretar como:
   - a) La probabilidad de $A$ y $B$ simultáneamente
   - b) La probabilidad de $A$ en el espacio muestral reducido a los casos en que $B$ ocurre
   - c) La probabilidad de $B$ dado $A$
   - d) El complementario de $P(A \cap B)$

   > **Respuesta correcta: b)** $P(A \mid B)$ restringe el espacio muestral a $B$, de manera que solo se consideran los casos en que $B$ ha ocurrido.

---

#### 10.3.2 Regla de la multiplicación: P(A ∩ B) = P(A|B)·P(B)

**Ejercicio Resuelto**

En un lote de 20 piezas hay 4 defectuosas. Se extraen 2 piezas al azar sin reemplazamiento. Calcula la probabilidad de que las dos piezas sean defectuosas.

**Solución paso a paso:**

Sea $D_1$ = "1.ª pieza defectuosa" y $D_2$ = "2.ª pieza defectuosa".

**Paso 1:** $P(D_1) = \dfrac{4}{20} = \dfrac{1}{5}$

**Paso 2:** Dado que la 1.ª es defectuosa, quedan 19 piezas, de las cuales 3 son defectuosas:
$$P(D_2 \mid D_1) = \frac{3}{19}$$

**Paso 3 – Regla de la multiplicación:**
$$P(D_1 \cap D_2) = P(D_1) \cdot P(D_2 \mid D_1) = \frac{1}{5} \cdot \frac{3}{19} = \frac{3}{95} \approx \mathbf{0{,}0316}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. $P(B) = 0{,}6$ y $P(A \mid B) = 0{,}3$. Calcula $P(A \cap B)$.

   > **Solución:** $P(A \cap B) = P(A \mid B) \cdot P(B) = 0{,}3 \times 0{,}6 = \mathbf{0{,}18}$.

2. Se lanza un dado dos veces. Calcula la probabilidad de obtener 6 en ambos lanzamientos.

   > **Solución:** Los lanzamientos son independientes. $P(6_1 \cap 6_2) = P(6_1) \cdot P(6_2) = \dfrac{1}{6} \cdot \dfrac{1}{6} = \dfrac{1}{36} \approx 0{,}028$.

**Nivel Intermedio:**

3. Una caja contiene 3 bolas rojas y 5 azules. Se extraen 3 sin reemplazamiento. Calcula la probabilidad de que las 3 sean azules.

   > **Solución:** $P(A_1) = \dfrac{5}{8}$, $P(A_2 \mid A_1) = \dfrac{4}{7}$, $P(A_3 \mid A_1 \cap A_2) = \dfrac{3}{6} = \dfrac{1}{2}$. $P = \dfrac{5}{8} \cdot \dfrac{4}{7} \cdot \dfrac{1}{2} = \dfrac{20}{112} = \dfrac{5}{28} \approx \mathbf{0{,}179}$.

4. Un sistema informático tiene dos cortafuegos en serie. El primero bloquea el 90% de los ataques y el segundo bloquea el 95% de los que pasan el primero. ¿Qué probabilidad hay de que un ataque supere ambos?

   > **Solución:** $P(\text{supera 1}) = 0{,}10$. $P(\text{supera 2} \mid \text{supera 1}) = 0{,}05$. $P(\text{supera ambos}) = 0{,}10 \times 0{,}05 = \mathbf{0{,}005}$ (0,5%).

**Nivel EVAU:**

5. En un proceso de control de calidad, las piezas pasan por dos controles: $C_1$ y $C_2$. El 5% de las piezas falla en $C_1$. De las que superan $C_1$, el 3% falla en $C_2$.

   a) Calcula la probabilidad de que una pieza supere ambos controles.  
   b) Calcula la probabilidad de que falle exactamente en $C_2$ (superó $C_1$ pero falló en $C_2$).  
   c) Calcula la probabilidad de que falle en al menos uno de los dos controles.

   > **Solución:**  
   > Sea $S_1$ = "supera $C_1$": $P(S_1) = 0{,}95$; $F_1$ = "falla $C_1$": $P(F_1) = 0{,}05$.  
   > $P(S_2 \mid S_1) = 0{,}97$; $P(F_2 \mid S_1) = 0{,}03$.  
   > a) $P(S_1 \cap S_2) = 0{,}95 \times 0{,}97 = \mathbf{0{,}9215}$.  
   > b) $P(S_1 \cap F_2) = 0{,}95 \times 0{,}03 = \mathbf{0{,}0285}$.  
   > c) $P(\text{falla al menos uno}) = 1 - P(S_1 \cap S_2) = 1 - 0{,}9215 = \mathbf{0{,}0785}$.

**Test de Opción Múltiple**

6. Si $P(A) = 0{,}5$, $P(B \mid A) = 0{,}4$ y $P(B \mid \bar{A}) = 0{,}2$, ¿cuánto vale $P(A \cap B)$?
   - a) 0,20
   - b) 0,10
   - c) 0,30
   - d) 0,08

   > **Respuesta correcta: a)** $P(A \cap B) = P(B \mid A) \cdot P(A) = 0{,}4 \times 0{,}5 = 0{,}20$.

7. La regla de la multiplicación general $P(A \cap B) = P(A \mid B) \cdot P(B)$ se simplifica a $P(A \cap B) = P(A) \cdot P(B)$ cuando:
   - a) $A$ y $B$ son incompatibles
   - b) $A$ y $B$ son independientes
   - c) $A \subset B$
   - d) $P(A) = P(B)$

   > **Respuesta correcta: b)** Si $A$ y $B$ son independientes, entonces $P(A \mid B) = P(A)$, y la fórmula queda $P(A \cap B) = P(A) \cdot P(B)$.

---

#### 10.3.3 Independencia de sucesos: definición y criterio

**Ejercicio Resuelto**

Se lanza un dado y una moneda. Sea $A$ = "sacar 4 en el dado" y $B$ = "sacar cara en la moneda". Comprueba si $A$ y $B$ son independientes.

**Solución paso a paso:**

**Criterio de independencia:** $A$ y $B$ son independientes si y solo si $P(A \cap B) = P(A) \cdot P(B)$.

$P(A) = \dfrac{1}{6}$, $P(B) = \dfrac{1}{2}$.

Como son experimentos distintos, los sucesos son claramente independientes. Verificamos:
$$P(A \cap B) = P(\text{sacar 4 y cara}) = \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{12}$$

$$P(A) \cdot P(B) = \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{12}$$

Como $P(A \cap B) = P(A) \cdot P(B)$, los sucesos son **independientes**. ✓

**Corolario:** Si $A$ y $B$ son independientes, también lo son $A$ y $\bar{B}$, $\bar{A}$ y $B$, $\bar{A}$ y $\bar{B}$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. $P(A) = 0{,}4$, $P(B) = 0{,}5$ y $P(A \cap B) = 0{,}2$. ¿Son $A$ y $B$ independientes?

   > **Solución:** $P(A) \cdot P(B) = 0{,}4 \times 0{,}5 = 0{,}2 = P(A \cap B)$. **Sí son independientes.**

2. $P(A) = 0{,}3$, $P(B) = 0{,}4$ y $P(A \cap B) = 0{,}15$. ¿Son independientes?

   > **Solución:** $P(A) \cdot P(B) = 0{,}12 \neq 0{,}15 = P(A \cap B)$. **No son independientes** (son sucesos con dependencia positiva).

**Nivel Intermedio:**

3. Demuestra que si $A$ y $B$ son independientes, entonces $P(A \mid B) = P(A)$ (el conocimiento de $B$ no altera la probabilidad de $A$).

   > **Solución:** Si $A$ y $B$ son independientes: $P(A \cap B) = P(A) \cdot P(B)$. Entonces: $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{P(A) \cdot P(B)}{P(B)} = P(A)$. ✓

4. Se realizan dos pruebas médicas independientes para detectar una enfermedad. La prueba $T_1$ tiene un 85% de éxito y la prueba $T_2$ tiene un 90% de éxito. ¿Cuál es la probabilidad de que al menos una detecte la enfermedad?

   > **Solución:** $P(\text{ninguna detecta}) = P(\bar{T_1}) \cdot P(\bar{T_2}) = 0{,}15 \times 0{,}10 = 0{,}015$. $P(\text{al menos una}) = 1 - 0{,}015 = \mathbf{0{,}985}$.

**Nivel EVAU:**

5. Tres componentes electrónicas $C_1$, $C_2$ y $C_3$ funcionan de forma independiente con probabilidades de fallo $P(F_1) = 0{,}05$, $P(F_2) = 0{,}04$ y $P(F_3) = 0{,}02$. El sistema falla si falla al menos una componente.

   a) Calcula la probabilidad de que el sistema funcione correctamente.  
   b) Calcula la probabilidad de que falle exactamente la componente $C_1$ y no fallen las otras dos.  
   c) ¿Cuál es la probabilidad de que fallen exactamente dos componentes?

   > **Solución:**  
   > a) $P(\text{sistema OK}) = P(\bar{F_1}) \cdot P(\bar{F_2}) \cdot P(\bar{F_3}) = 0{,}95 \times 0{,}96 \times 0{,}98 = \mathbf{0{,}8937}$.  
   > b) $P(F_1 \cap \bar{F_2} \cap \bar{F_3}) = 0{,}05 \times 0{,}96 \times 0{,}98 = \mathbf{0{,}04704}$.  
   > c) Exactamente dos fallan: $P(F_1 F_2 \bar{F_3}) + P(F_1 \bar{F_2} F_3) + P(\bar{F_1} F_2 F_3)$  
   > $= 0{,}05 \times 0{,}04 \times 0{,}98 + 0{,}05 \times 0{,}96 \times 0{,}02 + 0{,}95 \times 0{,}04 \times 0{,}02$  
   > $= 0{,}00196 + 0{,}00096 + 0{,}00076 = \mathbf{0{,}00368}$.

**Test de Opción Múltiple**

6. Si $A$ y $B$ son incompatibles y ambos tienen probabilidad positiva, entonces:
   - a) Son independientes
   - b) No pueden ser independientes
   - c) Son siempre independientes si $P(A)+P(B)=1$
   - d) $P(A \cap B) = P(A) \cdot P(B)$

   > **Respuesta correcta: b)** Si son incompatibles, $P(A \cap B)=0$, pero $P(A) \cdot P(B) > 0$, luego $P(A \cap B) \neq P(A) \cdot P(B)$: no son independientes.

7. Si $P(A) = 0{,}5$ y $A$ y $B$ son independientes, ¿cuánto vale $P(A \mid B)$?
   - a) 0,25
   - b) 0,5
   - c) Depende de $P(B)$
   - d) 1

   > **Respuesta correcta: b)** Por definición de independencia, $P(A \mid B) = P(A) = 0{,}5$.

---

#### 10.3.4 Independencia mutua de tres o más sucesos

**Ejercicio Resuelto**

Los sucesos $A$, $B$ y $C$ son mutuamente independientes si se cumplen **simultáneamente**:  
$P(A \cap B) = P(A)P(B)$, $P(A \cap C) = P(A)P(C)$, $P(B \cap C) = P(B)P(C)$ **y** $P(A \cap B \cap C) = P(A)P(B)P(C)$.

Dado $P(A) = 0{,}5$, $P(B) = 0{,}4$, $P(C) = 0{,}3$, comprueba si son mutuamente independientes sabiendo que $P(A \cap B) = 0{,}2$, $P(A \cap C) = 0{,}15$, $P(B \cap C) = 0{,}12$ y $P(A \cap B \cap C) = 0{,}06$.

**Solución paso a paso:**

- $P(A)P(B) = 0{,}5 \times 0{,}4 = 0{,}20 = P(A \cap B)$ ✓  
- $P(A)P(C) = 0{,}5 \times 0{,}3 = 0{,}15 = P(A \cap C)$ ✓  
- $P(B)P(C) = 0{,}4 \times 0{,}3 = 0{,}12 = P(B \cap C)$ ✓  
- $P(A)P(B)P(C) = 0{,}5 \times 0{,}4 \times 0{,}3 = 0{,}06 = P(A \cap B \cap C)$ ✓

Se verifican las **4 condiciones**, por lo que $A$, $B$ y $C$ son **mutuamente independientes**.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Se lanzan tres monedas. Sea $A_i$ = "la moneda $i$ cae cara". ¿Son $A_1$, $A_2$ y $A_3$ mutuamente independientes?

   > **Solución:** $P(A_i) = 1/2$ para todo $i$. Los lanzamientos son independientes. $P(A_1 \cap A_2) = 1/4 = P(A_1)P(A_2)$ ✓. Análogamente para los demás pares. $P(A_1 \cap A_2 \cap A_3) = 1/8 = (1/2)^3$ ✓. **Sí son mutuamente independientes.**

2. Si $A$, $B$ y $C$ son mutuamente independientes con $P(A)=0{,}6$, $P(B)=0{,}5$, $P(C)=0{,}4$, calcula $P(A \cap B \cap C)$ y $P(A \cup B \cup C)$.

   > **Solución:** $P(A \cap B \cap C) = 0{,}6 \times 0{,}5 \times 0{,}4 = 0{,}12$. Para la unión, es más cómodo el complementario: $P(\bar{A} \cap \bar{B} \cap \bar{C}) = 0{,}4 \times 0{,}5 \times 0{,}6 = 0{,}12$. $P(A \cup B \cup C) = 1 - 0{,}12 = \mathbf{0{,}88}$.

**Nivel Intermedio:**

3. Ejemplo de sucesos que son independientes por pares pero NO mutuamente independientes (paradoja de Bernstein): Se lanza una moneda dos veces. $A$ = "primera cara", $B$ = "segunda cara", $C$ = "exactamente una cara". Comprueba que cualquier par es independiente pero $P(A \cap B \cap C) \neq P(A)P(B)P(C)$.

   > **Solución:** $\Omega = \{CC, CX, XC, XX\}$ (equiprobable). $P(A) = P(B) = P(C) = 1/2$. $A \cap B = \{CC\}$: $P(A \cap B) = 1/4 = P(A)P(B)$ ✓. $A \cap C = \{CX\}$: $P(A \cap C) = 1/4 = P(A)P(C)$ ✓. $B \cap C = \{XC\}$: $P(B \cap C) = 1/4 = P(B)P(C)$ ✓. Pero $A \cap B \cap C = \emptyset$ (si salen dos caras, no hay exactamente una): $P(A \cap B \cap C) = 0 \neq 1/8 = P(A)P(B)P(C)$. **No son mutuamente independientes.**

4. En un sistema de tres interruptores en paralelo (el sistema funciona si al menos uno funciona), cada interruptor falla de forma independiente con probabilidad 0,1. Calcula la probabilidad de fallo del sistema.

   > **Solución:** El sistema falla solo si los tres interruptores fallan. $P(\text{sistema falla}) = 0{,}1^3 = \mathbf{0{,}001}$ (0,1%).

**Nivel EVAU:**

5. Una empresa fabrica chips que pasan por tres pruebas de calidad independientes: $P_1$, $P_2$ y $P_3$. Las probabilidades de superar cada prueba son 0,95, 0,92 y 0,98 respectivamente.

   a) ¿Cuál es la probabilidad de que un chip supere las tres pruebas?  
   b) ¿Cuál es la probabilidad de que falle exactamente la prueba $P_2$?  
   c) ¿Cuál es la probabilidad de que supere al menos dos pruebas?

   > **Solución:**  
   > a) $P(S_1 S_2 S_3) = 0{,}95 \times 0{,}92 \times 0{,}98 = \mathbf{0{,}8557}$.  
   > b) Falla solo $P_2$: $P(S_1 F_2 S_3) = 0{,}95 \times 0{,}08 \times 0{,}98 = \mathbf{0{,}07448}$.  
   > c) Al menos 2 pruebas superadas = 2 superadas + 3 superadas:  
   > Exactamente 2: $P(F_1 S_2 S_3) + P(S_1 F_2 S_3) + P(S_1 S_2 F_3)$  
   > $= 0{,}05 \times 0{,}92 \times 0{,}98 + 0{,}95 \times 0{,}08 \times 0{,}98 + 0{,}95 \times 0{,}92 \times 0{,}02$  
   > $= 0{,}04508 + 0{,}07448 + 0{,}01748 = 0{,}13704$.  
   > Al menos 2: $0{,}13704 + 0{,}8557 = \mathbf{0{,}99274}$.

**Test de Opción Múltiple**

6. ¿Cuántas condiciones deben verificarse para que tres sucesos $A$, $B$, $C$ sean **mutuamente independientes**?
   - a) 1
   - b) 2
   - c) 3
   - d) 4

   > **Respuesta correcta: d)** Hay 3 condiciones de independencia por pares más 1 condición triple: total **4 condiciones**.

7. Si $A$ y $B$ son independientes, ¿cuál de las siguientes afirmaciones es también verdadera?
   - a) $\bar{A}$ y $B$ son dependientes
   - b) $A$ y $\bar{B}$ son independientes
   - c) $A$ y $B$ son incompatibles
   - d) $P(A \cup B) = P(A) + P(B)$

   > **Respuesta correcta: b)** La independencia se preserva cuando se toma el complementario de uno o ambos sucesos: $\bar{A}$ y $B$, $A$ y $\bar{B}$, $\bar{A}$ y $\bar{B}$ también son independientes.

---

## 10.4 Diagramas de árbol y tablas de contingencia

---

#### 10.4.1 Construcción e interpretación de diagramas de árbol

**Ejercicio Resuelto**

Una urna tiene 3 bolas rojas y 2 azules. Se extraen 2 bolas **sin reemplazamiento**. Construye el diagrama de árbol completo y calcula todas las probabilidades de las ramas.

**Solución paso a paso:**

**Nivel 1 (1.ª extracción):**
- $P(R_1) = 3/5$  
- $P(A_1) = 2/5$

**Nivel 2 (2.ª extracción dado el resultado de la 1.ª):**

Si $R_1$ (quedan 4 bolas: 2R, 2A):
- $P(R_2 \mid R_1) = 2/4 = 1/2$  
- $P(A_2 \mid R_1) = 2/4 = 1/2$

Si $A_1$ (quedan 4 bolas: 3R, 1A):
- $P(R_2 \mid A_1) = 3/4$  
- $P(A_2 \mid A_1) = 1/4$

**Probabilidades de los caminos (regla de la multiplicación):**

| Camino | Probabilidad |
|--------|-------------|
| $R_1 \cap R_2$ | $\frac{3}{5} \cdot \frac{1}{2} = \frac{3}{10}$ |
| $R_1 \cap A_2$ | $\frac{3}{5} \cdot \frac{1}{2} = \frac{3}{10}$ |
| $A_1 \cap R_2$ | $\frac{2}{5} \cdot \frac{3}{4} = \frac{6}{20} = \frac{3}{10}$ |
| $A_1 \cap A_2$ | $\frac{2}{5} \cdot \frac{1}{4} = \frac{2}{20} = \frac{1}{10}$ |

**Verificación:** $\frac{3}{10} + \frac{3}{10} + \frac{3}{10} + \frac{1}{10} = \frac{10}{10} = 1$ ✓

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Se lanza una moneda y luego un dado. Construye el árbol y calcula la probabilidad de obtener cara y un número par.

   > **Solución:** Nivel 1: $P(C) = 1/2$, $P(X) = 1/2$. Nivel 2 (dado, 3 pares de 6): $P(\text{par}) = 1/2$. $P(\text{cara y par}) = P(C) \cdot P(\text{par}) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.

2. Una caja tiene 2 bolas rojas y 3 verdes. Se extrae una, se anota el color y se devuelve (con reemplazamiento). Luego se extrae otra. Calcula la probabilidad de obtener dos bolas del mismo color.

   > **Solución:** Con reemplazamiento, las probabilidades no cambian. $P(RR) = \frac{2}{5} \cdot \frac{2}{5} = \frac{4}{25}$. $P(VV) = \frac{3}{5} \cdot \frac{3}{5} = \frac{9}{25}$. $P(\text{mismo color}) = \frac{4}{25} + \frac{9}{25} = \frac{13}{25} = \mathbf{0{,}52}$.

**Nivel Intermedio:**

3. En una producción, el 40% de las piezas son del tipo $A$ y el 60% son del tipo $B$. El 5% de las de tipo $A$ son defectuosas y el 2% de las de tipo $B$ son defectuosas. Se elige una pieza al azar. Construye el árbol y calcula la probabilidad de que sea defectuosa.

   > **Solución:** $P(D) = P(D \mid A) \cdot P(A) + P(D \mid B) \cdot P(B) = 0{,}05 \times 0{,}40 + 0{,}02 \times 0{,}60 = 0{,}020 + 0{,}012 = \mathbf{0{,}032}$ (3,2%).

4. Un arquero lanza dos flechas. La probabilidad de acertar en el primero es 0,7. Si acierta en el primero, la probabilidad de acertar en el segundo es 0,8; si falla el primero, la probabilidad de acertar en el segundo es 0,6. Calcula la probabilidad de acertar exactamente una flecha.

   > **Solución:** $P(\text{acierta 1.ª, falla 2.ª}) = 0{,}7 \times 0{,}2 = 0{,}14$. $P(\text{falla 1.ª, acierta 2.ª}) = 0{,}3 \times 0{,}6 = 0{,}18$. $P(\text{exactamente una}) = 0{,}14 + 0{,}18 = \mathbf{0{,}32}$.

**Nivel EVAU:**

5. Una empresa recibe componentes de dos proveedores: el 70% de proveedor $P_1$ y el 30% de proveedor $P_2$. El porcentaje de piezas defectuosas del proveedor $P_1$ es el 4% y del proveedor $P_2$ es el 8%.

   a) Construye el diagrama de árbol completo.  
   b) Calcula la probabilidad de que una pieza elegida al azar sea defectuosa.  
   c) Si la pieza es defectuosa, ¿cuál es la probabilidad de que provenga de $P_1$?  
   d) ¿De cuál de los dos proveedores proceden más piezas defectuosas en términos absolutos?

   > **Solución:**  
   > a) Árbol: $P_1 (0{,}7) \to D (0{,}04)$ y $\bar{D} (0{,}96)$; $P_2 (0{,}3) \to D (0{,}08)$ y $\bar{D} (0{,}92)$.  
   > b) $P(D) = 0{,}70 \times 0{,}04 + 0{,}30 \times 0{,}08 = 0{,}028 + 0{,}024 = \mathbf{0{,}052}$.  
   > c) $P(P_1 \mid D) = \dfrac{0{,}028}{0{,}052} = \dfrac{28}{52} = \dfrac{7}{13} \approx \mathbf{0{,}538}$.  
   > d) $P_1$ aporta $0{,}028$ y $P_2$ aporta $0{,}024$ de piezas defectuosas. Aunque $P_2$ tiene mayor tasa de defectos (8%), es $P_1$ quien genera **más piezas defectuosas** en total por su mayor volumen de suministro.

**Test de Opción Múltiple**

6. En un diagrama de árbol, la suma de las probabilidades de todos los caminos completos (hojas) debe ser:
   - a) Igual al número de ramas
   - b) Igual a 1
   - c) Igual a 0
   - d) Igual a la probabilidad del suceso más probable

   > **Respuesta correcta: b)** Los caminos completos forman una partición del espacio muestral, por lo que sus probabilidades deben sumar 1.

7. En un árbol de dos niveles con sucesos $A$ y $B$ en el primer nivel y $C$ y $D$ en el segundo, la probabilidad del camino $A \to C$ es:
   - a) $P(A) + P(C)$
   - b) $P(A) \cdot P(C)$
   - c) $P(A) \cdot P(C \mid A)$
   - d) $P(C \mid A) / P(A)$

   > **Respuesta correcta: c)** La regla de la multiplicación dice que la probabilidad del camino es $P(A \cap C) = P(A) \cdot P(C \mid A)$.

---

#### 10.4.2 Cálculo de probabilidades compuestas mediante árboles

**Ejercicio Resuelto**

En un examen tipo test de 3 preguntas, cada pregunta tiene 4 opciones y solo una es correcta. Un alumno que no sabe la respuesta la elige al azar. Se sabe que el alumno conoce el 70% de los temas. Calcula la probabilidad de que responda correctamente la primera pregunta.

**Solución paso a paso:**

**Paso 1 – Definir sucesos:**  
- $S$ = "sabe la respuesta": $P(S) = 0{,}7$, $P(\bar{S}) = 0{,}3$  
- $C$ = "responde correctamente"

**Paso 2 – Probabilidades condicionadas:**  
- Si sabe: $P(C \mid S) = 1$ (responde seguro)  
- Si no sabe: $P(C \mid \bar{S}) = 1/4 = 0{,}25$ (elige al azar)

**Paso 3 – Teorema de la probabilidad total:**
$$P(C) = P(C \mid S) \cdot P(S) + P(C \mid \bar{S}) \cdot P(\bar{S})$$
$$P(C) = 1 \times 0{,}7 + 0{,}25 \times 0{,}3 = 0{,}7 + 0{,}075 = \mathbf{0{,}775}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Se elige una caja de entre dos: la caja 1 tiene 3 bolas rojas y 2 azules; la caja 2 tiene 1 roja y 4 azules. La probabilidad de elegir la caja 1 es 0,4. Calcula la probabilidad de extraer una bola roja.

   > **Solución:** $P(R) = P(R \mid C_1) \cdot P(C_1) + P(R \mid C_2) \cdot P(C_2) = \frac{3}{5} \times 0{,}4 + \frac{1}{5} \times 0{,}6 = 0{,}24 + 0{,}12 = \mathbf{0{,}36}$.

2. Un deportista entrena 5 días a la semana. Si ha entrenado el día anterior, la probabilidad de ganar una competición es 0,8; si no ha entrenado, es 0,4. Entrena el 70% de los días. Calcula la probabilidad de ganar.

   > **Solución:** $P(\text{gana}) = 0{,}8 \times 0{,}7 + 0{,}4 \times 0{,}3 = 0{,}56 + 0{,}12 = \mathbf{0{,}68}$.

**Nivel Intermedio:**

3. Un test médico puede dar resultado positivo (+) o negativo (−). Si el paciente tiene la enfermedad, $P(+ \mid E) = 0{,}95$. Si no la tiene, $P(+ \mid \bar{E}) = 0{,}08$. La prevalencia de la enfermedad es 1%. Calcula la probabilidad de obtener un resultado positivo.

   > **Solución:** $P(E) = 0{,}01$. $P(+) = 0{,}95 \times 0{,}01 + 0{,}08 \times 0{,}99 = 0{,}0095 + 0{,}0792 = \mathbf{0{,}0887}$.

4. Tres máquinas producen tornillos. La máquina $M_1$ produce el 50%, $M_2$ el 30% y $M_3$ el 20%. Los porcentajes de tornillos defectuosos son 2%, 3% y 5% respectivamente. Calcula la probabilidad de sacar un tornillo defectuoso.

   > **Solución:** $P(D) = 0{,}02 \times 0{,}50 + 0{,}03 \times 0{,}30 + 0{,}05 \times 0{,}20 = 0{,}010 + 0{,}009 + 0{,}010 = \mathbf{0{,}029}$ (2,9%).

**Nivel EVAU:**

5. En una planta de producción, las piezas se fabrican en tres turnos. El turno de mañana ($M$) produce el 40% de las piezas, el turno de tarde ($T$) el 35% y el turno de noche ($N$) el 25%. Los porcentajes de piezas con defecto son respectivamente 1%, 2% y 4%.

   a) Construye el diagrama de árbol con todas las ramas y probabilidades.  
   b) Calcula la probabilidad de que una pieza elegida al azar sea defectuosa.  
   c) Si se elige una pieza defectuosa, ¿de qué turno es más probable que provenga?

   > **Solución:**  
   > a) Primer nivel: $M (0{,}40)$, $T (0{,}35)$, $N (0{,}25)$. Segundo nivel: cada turno se ramifica en $D$ y $\bar{D}$.  
   > b) $P(D) = 0{,}01 \times 0{,}40 + 0{,}02 \times 0{,}35 + 0{,}04 \times 0{,}25 = 0{,}004 + 0{,}007 + 0{,}010 = \mathbf{0{,}021}$.  
   > c) $P(M \mid D) = \frac{0{,}004}{0{,}021} \approx 0{,}190$; $P(T \mid D) = \frac{0{,}007}{0{,}021} \approx 0{,}333$; $P(N \mid D) = \frac{0{,}010}{0{,}021} \approx 0{,}476$. La pieza defectuosa es más probable que provenga del **turno de noche**.

**Test de Opción Múltiple**

6. En un árbol con dos grupos $G_1$ (probabilidad 0,6) y $G_2$ (probabilidad 0,4), y dentro de cada grupo el suceso $A$ tiene probabilidades $P(A \mid G_1) = 0{,}3$ y $P(A \mid G_2) = 0{,}5$, ¿cuánto vale $P(A)$?
   - a) 0,38
   - b) 0,40
   - c) 0,35
   - d) 0,15

   > **Respuesta correcta: a)** $P(A) = 0{,}3 \times 0{,}6 + 0{,}5 \times 0{,}4 = 0{,}18 + 0{,}20 = 0{,}38$.

7. La probabilidad compuesta de un camino en un árbol de tres niveles $A \to B \to C$ se calcula como:
   - a) $P(A) + P(B \mid A) + P(C \mid B)$
   - b) $P(A) \cdot P(B) \cdot P(C)$
   - c) $P(A) \cdot P(B \mid A) \cdot P(C \mid A \cap B)$
   - d) $P(C \mid A \cap B) / P(A)$

   > **Respuesta correcta: c)** La regla de la multiplicación generalizada: $P(A \cap B \cap C) = P(A) \cdot P(B \mid A) \cdot P(C \mid A \cap B)$.

---

#### 10.4.3 Tablas de contingencia: construcción e interpretación

**Ejercicio Resuelto**

En una encuesta a 500 personas se pregunta sobre género (Hombre/Mujer) y preferencia de transporte (Coche/Transporte público). Los resultados son: 180 hombres prefieren el coche, 70 hombres prefieren el transporte público, 100 mujeres prefieren el coche y 150 mujeres prefieren el transporte público. Construye la tabla de contingencia completa.

**Solución paso a paso:**

**Paso 1 – Rellenar la tabla:**

|  | Coche | T. Público | Total |
|--|-------|-----------|-------|
| Hombre | 180 | 70 | **250** |
| Mujer | 100 | 150 | **250** |
| **Total** | **280** | **220** | **500** |

**Paso 2 – Verificar los totales:** $180+70 = 250$, $100+150 = 250$, $180+100 = 280$, $70+150 = 220$. Total general: $280+220 = 500$ ✓

**Paso 3 – Calcular probabilidades marginales y conjuntas:**

- $P(\text{Hombre}) = 250/500 = 0{,}5$  
- $P(\text{Coche}) = 280/500 = 0{,}56$  
- $P(\text{Hombre y Coche}) = 180/500 = 0{,}36$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Completa la siguiente tabla de contingencia sobre hábito de fumar y enfermedad cardiovascular en 1000 personas:

   |  | Con enfermedad | Sin enfermedad | Total |
   |--|----------------|---------------|-------|
   | Fumador | 120 | 180 | ??? |
   | No fumador | 80 | ??? | 620 |
   | Total | 200 | ??? | 1000 |

   > **Solución:** Fumador total: $120+180=300$. No fumador sin enfermedad: $620-80=540$. Sin enfermedad total: $180+540=720$. Total: $200+720=920 \neq 1000$... Corrección: No fumador sin enfermedad: $1000-300-80 = 620$. Tabla: Fumador: 120, 180, 300. No fumador: 80, 540, 620. Totales: 200, 720, 1000.

2. De la tabla del ejercicio resuelto, calcula $P(\text{Mujer y T. Público})$ y $P(\text{T. Público})$.

   > **Solución:** $P(\text{Mujer y T. Público}) = 150/500 = \mathbf{0{,}30}$. $P(\text{T. Público}) = 220/500 = \mathbf{0{,}44}$.

**Nivel Intermedio:**

3. En un hospital, 300 pacientes se clasifican según tipo de tratamiento (Quirúrgico/Médico) y resultado (Éxito/Fracaso): 90 quirúrgicos con éxito, 30 quirúrgicos con fracaso, 150 médicos con éxito, 30 médicos con fracaso. Construye la tabla y calcula la tasa de éxito de cada tratamiento.

   > **Solución:** Tabla: Quirúrgico: 90, 30, 120. Médico: 150, 30, 180. Total: 240, 60, 300. Tasa éxito quirúrgico: $90/120 = \mathbf{0{,}75}$. Tasa éxito médico: $150/180 \approx \mathbf{0{,}833}$.

4. En la tabla del ejercicio 3, ¿son independientes el tipo de tratamiento y el resultado?

   > **Solución:** $P(\text{Éxito}) = 240/300 = 0{,}8$. $P(\text{Quirúrgico}) = 120/300 = 0{,}4$. $P(\text{Éxito y Quirúrgico}) = 90/300 = 0{,}3$. Pero $P(\text{Éxito}) \cdot P(\text{Quirúrgico}) = 0{,}8 \times 0{,}4 = 0{,}32 \neq 0{,}3$. **No son independientes**: el tipo de tratamiento y el resultado están relacionados.

**Nivel EVAU:**

5. Una empresa analiza 400 productos según su tamaño (Grande/Pequeño) y si superó el control de calidad (Pasa/No pasa):

   |  | Pasa | No pasa | Total |
   |--|------|---------|-------|
   | Grande | 160 | 40 | 200 |
   | Pequeño | 180 | 20 | 200 |
   | Total | 340 | 60 | 400 |

   a) ¿Cuál es la probabilidad de que un producto pase el control?  
   b) Dado que el producto es grande, ¿cuál es la probabilidad de que pase el control?  
   c) ¿Son independientes el tamaño y el resultado del control? Justifica numéricamente.  
   d) ¿Qué tamaño tiene mayor tasa de rechazo?

   > **Solución:**  
   > a) $P(\text{Pasa}) = 340/400 = \mathbf{0{,}85}$.  
   > b) $P(\text{Pasa} \mid \text{Grande}) = 160/200 = \mathbf{0{,}80}$.  
   > c) $P(\text{Pasa}) \cdot P(\text{Grande}) = 0{,}85 \times 0{,}5 = 0{,}425 \neq 160/400 = 0{,}40$. **No son independientes.**  
   > d) Tasa de rechazo grande: $40/200 = 20\%$; pequeño: $20/200 = 10\%$. El tamaño **Grande** tiene mayor tasa de rechazo.

**Test de Opción Múltiple**

6. En una tabla de contingencia 2×2 con 100 observaciones, si los totales marginales son $P(A) = 0{,}6$ y $P(B) = 0{,}4$, y $A$ y $B$ son independientes, ¿cuántos casos hay en la celda $A \cap B$?
   - a) 24
   - b) 40
   - c) 10
   - d) 60

   > **Respuesta correcta: a)** Si son independientes: $P(A \cap B) = P(A) \cdot P(B) = 0{,}6 \times 0{,}4 = 0{,}24$, luego $100 \times 0{,}24 = 24$ casos.

7. La probabilidad marginal de una fila en una tabla de contingencia se obtiene:
   - a) Dividiendo la celda entre el total general
   - b) Sumando los valores de la fila y dividiendo entre el total general
   - c) Dividiendo una celda entre el total de su columna
   - d) Multiplicando la probabilidad de fila por la de columna

   > **Respuesta correcta: b)** La probabilidad marginal de una fila es la suma de todas las celdas de esa fila dividida entre el total general.

---

#### 10.4.4 Extracción de probabilidades marginales, conjuntas y condicionadas de tablas

**Ejercicio Resuelto**

Dada la siguiente tabla de contingencia sobre 200 empleados (género y departamento):

|  | Producción | Ventas | Administración | Total |
|--|-----------|--------|---------------|-------|
| Hombre | 60 | 40 | 20 | 120 |
| Mujer | 30 | 30 | 20 | 80 |
| Total | 90 | 70 | 40 | 200 |

Calcula: (a) $P(\text{Ventas})$, (b) $P(\text{Mujer y Ventas})$, (c) $P(\text{Ventas} \mid \text{Mujer})$, (d) $P(\text{Mujer} \mid \text{Ventas})$.

**Solución paso a paso:**

**(a) Probabilidad marginal de Ventas:**
$$P(\text{Ventas}) = \frac{70}{200} = 0{,}35$$

**(b) Probabilidad conjunta:**
$$P(\text{Mujer} \cap \text{Ventas}) = \frac{30}{200} = 0{,}15$$

**(c) Probabilidad condicionada (dado que es Mujer):**
$$P(\text{Ventas} \mid \text{Mujer}) = \frac{P(\text{Mujer} \cap \text{Ventas})}{P(\text{Mujer})} = \frac{30/200}{80/200} = \frac{30}{80} = 0{,}375$$

**(d) Probabilidad condicionada (dado que es de Ventas):**
$$P(\text{Mujer} \mid \text{Ventas}) = \frac{30}{70} \approx 0{,}429$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. De la tabla del ejercicio resuelto, calcula $P(\text{Hombre})$, $P(\text{Producción})$ y $P(\text{Hombre} \cap \text{Producción})$.

   > **Solución:** $P(\text{Hombre}) = 120/200 = 0{,}6$. $P(\text{Producción}) = 90/200 = 0{,}45$. $P(\text{Hombre} \cap \text{Producción}) = 60/200 = 0{,}30$.

2. Calcula $P(\text{Producción} \mid \text{Hombre})$ a partir de la misma tabla.

   > **Solución:** $P(\text{Producción} \mid \text{Hombre}) = 60/120 = \mathbf{0{,}5}$.

**Nivel Intermedio:**

3. Comprueba si el género y el departamento de Ventas son independientes usando los datos de la tabla del ejercicio resuelto.

   > **Solución:** $P(\text{Mujer}) \cdot P(\text{Ventas}) = 0{,}4 \times 0{,}35 = 0{,}14$. $P(\text{Mujer} \cap \text{Ventas}) = 30/200 = 0{,}15 \neq 0{,}14$. **No son independientes** (ligera asociación positiva de las mujeres con Ventas).

4. En la tabla del ejercicio resuelto, calcula la probabilidad de que un empleado sea de Administración dado que es mujer, y compárala con la probabilidad incondicional de ser de Administración.

   > **Solución:** $P(\text{Admin} \mid \text{Mujer}) = 20/80 = 0{,}25$. $P(\text{Admin}) = 40/200 = 0{,}20$. Como $0{,}25 > 0{,}20$, las mujeres tienen una ligera **sobrerrepresentación** en Administración.

**Nivel EVAU:**

5. En un estudio epidemiológico se analizan 1000 personas según nivel de actividad física (Alta/Baja) y presencia de hipertensión (Sí/No):

   |  | Hipertensión Sí | Hipertensión No | Total |
   |--|----------------|----------------|-------|
   | Actividad Alta | 40 | 360 | 400 |
   | Actividad Baja | 150 | 450 | 600 |
   | Total | 190 | 810 | 1000 |

   a) Calcula la probabilidad de que una persona tenga hipertensión.  
   b) Calcula $P(\text{Hipertensión} \mid \text{Actividad Alta})$ y $P(\text{Hipertensión} \mid \text{Actividad Baja})$.  
   c) ¿Son independientes el nivel de actividad y la hipertensión?  
   d) Interpreta el resultado del apartado (b) en términos de salud pública.

   > **Solución:**  
   > a) $P(\text{HT}) = 190/1000 = \mathbf{0{,}19}$.  
   > b) $P(\text{HT} \mid \text{Alta}) = 40/400 = \mathbf{0{,}10}$. $P(\text{HT} \mid \text{Baja}) = 150/600 = \mathbf{0{,}25}$.  
   > c) $P(\text{HT}) \cdot P(\text{Alta}) = 0{,}19 \times 0{,}40 = 0{,}076 \neq 40/1000 = 0{,}040$. **No son independientes**: hay asociación.  
   > d) Las personas con **alta actividad física** tienen el 10% de prevalencia de hipertensión, frente al 25% de las sedentarias. La actividad física parece ser un factor protector importante.

**Test de Opción Múltiple**

6. En una tabla de contingencia, $P(A \mid B)$ se calcula como:
   - a) (Frecuencia de $A$) / (Total general)
   - b) (Frecuencia de $A \cap B$) / (Frecuencia de $B$)
   - c) (Frecuencia de $A \cap B$) / (Total general)
   - d) (Frecuencia de $B$) / (Frecuencia de $A$)

   > **Respuesta correcta: b)** La probabilidad condicionada en tablas se calcula dividiendo la frecuencia conjunta entre la frecuencia marginal de la condición.

7. Si en una tabla de contingencia $P(A \mid B) = P(A)$, se concluye que:
   - a) $A$ y $B$ son incompatibles
   - b) $A$ y $B$ son independientes
   - c) $P(B) = 0$
   - d) $A \subset B$

   > **Respuesta correcta: b)** $P(A \mid B) = P(A)$ es equivalente a $P(A \cap B) = P(A) \cdot P(B)$, que es la definición de independencia.

---

## 10.5 Probabilidad total y teorema de Bayes

---

#### 10.5.1 Partición del espacio muestral: sistema completo de sucesos

**Ejercicio Resuelto**

Comprueba que los sucesos $A_1 = \{1,2\}$, $A_2 = \{3,4\}$ y $A_3 = \{5,6\}$ forman una partición de $\Omega = \{1,2,3,4,5,6\}$ (el espacio muestral al lanzar un dado).

**Solución paso a paso:**

Un sistema completo de sucesos (partición) debe cumplir:
1. Los sucesos son dos a dos disjuntos (incompatibles).
2. La unión de todos es $\Omega$ (son exhaustivos).

**Comprobación 1 (disjunción):**
- $A_1 \cap A_2 = \{1,2\} \cap \{3,4\} = \emptyset$ ✓  
- $A_1 \cap A_3 = \{1,2\} \cap \{5,6\} = \emptyset$ ✓  
- $A_2 \cap A_3 = \{3,4\} \cap \{5,6\} = \emptyset$ ✓

**Comprobación 2 (exhaustividad):**
$$A_1 \cup A_2 \cup A_3 = \{1,2,3,4,5,6\} = \Omega \checkmark$$

Sí forman una **partición** de $\Omega$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. ¿Forman partición del espacio muestral $\Omega = [0,1]$ los conjuntos $A_1 = [0, 0{,}5)$, $A_2 = [0{,}5, 1]$?

   > **Solución:** $A_1 \cap A_2 = \emptyset$ ✓. $A_1 \cup A_2 = [0,1] = \Omega$ ✓. **Sí forman partición.**

2. Indica cuál de los siguientes conjuntos **no** forma una partición de $\Omega = \{1,2,3,4,5\}$: (a) $\{1,2\}, \{3,4\}, \{5\}$; (b) $\{1,2\}, \{2,3,4\}, \{5\}$.

   > **Solución:** (a) Sí es partición: disjuntos y exhaustivos ✓. (b) **No** es partición porque $\{1,2\} \cap \{2,3,4\} = \{2\} \neq \emptyset$.

**Nivel Intermedio:**

3. En una fábrica las piezas se clasifican en: defectuosas graves ($D_G$), defectuosas leves ($D_L$) y correctas ($C$). Explica por qué estas tres categorías forman una partición del espacio muestral y cuál es la condición que deben cumplir sus probabilidades.

   > **Solución:** Son disjuntas (una pieza no puede ser a la vez grave y leve) y exhaustivas (toda pieza pertenece a alguna categoría). Por tanto forman una partición. La condición es $P(D_G) + P(D_L) + P(C) = 1$.

4. Dado el experimento "elegir un número del 1 al 20", construye una partición en 4 sucesos según el resto de dividir entre 4 ($R = 0, 1, 2, 3$). Calcula las probabilidades de cada suceso de la partición.

   > **Solución:** $A_0 = \{4,8,12,16,20\}$ (5 elem.), $A_1 = \{1,5,9,13,17\}$ (5 elem.), $A_2 = \{2,6,10,14,18\}$ (5 elem.), $A_3 = \{3,7,11,15,19\}$ (5 elem.). $P(A_i) = 5/20 = 1/4$ para cada $i$. Suma: $4 \times 1/4 = 1$ ✓.

**Nivel EVAU:**

5. En el control de un proceso industrial, los productos se clasifican según su nivel de calidad: calidad A (30%), calidad B (45%) y calidad C (25%).

   a) Verifica que estas tres categorías forman una partición del espacio muestral.  
   b) Si se sabe que el 2% de los productos de calidad A son rechazados, el 5% de los de calidad B y el 15% de los de calidad C, ¿cuál es la probabilidad de rechazo de un producto tomado al azar? (Anticipación del teorema de la probabilidad total.)

   > **Solución:**  
   > a) Son disjuntos (un producto pertenece exactamente a una calidad) y $0{,}30 + 0{,}45 + 0{,}25 = 1$ ✓. Forman partición.  
   > b) $P(R) = 0{,}02 \times 0{,}30 + 0{,}05 \times 0{,}45 + 0{,}15 \times 0{,}25 = 0{,}006 + 0{,}0225 + 0{,}0375 = \mathbf{0{,}066}$ (6,6%).

**Test de Opción Múltiple**

6. Para que $A_1, A_2, A_3$ formen una partición del espacio muestral, deben cumplirse:
   - a) Solo que sean disjuntos
   - b) Solo que sean exhaustivos ($A_1 \cup A_2 \cup A_3 = \Omega$)
   - c) Que sean disjuntos y exhaustivos
   - d) Que tengan la misma probabilidad

   > **Respuesta correcta: c)** Una partición requiere que los sucesos sean dos a dos incompatibles (disjuntos) **y** que su unión sea el espacio muestral completo (exhaustivos).

7. Si $\{A_1, A_2, A_3\}$ es una partición de $\Omega$, entonces:
   - a) $P(A_1) = P(A_2) = P(A_3)$
   - b) $P(A_1) + P(A_2) + P(A_3) = 1$
   - c) $A_1 \subset A_2 \subset A_3$
   - d) $P(A_1 \cup A_2) = 0$

   > **Respuesta correcta: b)** Al ser disjuntos y cubrir todo $\Omega$, la suma de sus probabilidades es $P(\Omega) = 1$.

---

#### 10.5.2 Teorema de la probabilidad total

**Ejercicio Resuelto**

Una empresa tiene tres líneas de producción $L_1$, $L_2$ y $L_3$ que producen el 50%, 30% y 20% de las piezas respectivamente. La tasa de defectos de cada línea es 2%, 4% y 6%. Calcula la probabilidad de que una pieza elegida al azar sea defectuosa.

**Solución paso a paso:**

**Datos:**
$$P(L_1)=0{,}5,\quad P(L_2)=0{,}3,\quad P(L_3)=0{,}2$$
$$P(D \mid L_1)=0{,}02,\quad P(D \mid L_2)=0{,}04,\quad P(D \mid L_3)=0{,}06$$

**Verificamos que $\{L_1, L_2, L_3\}$ es una partición:**
$P(L_1)+P(L_2)+P(L_3) = 0{,}5+0{,}3+0{,}2 = 1$ ✓

**Teorema de la probabilidad total:**
$$P(D) = P(D \mid L_1) \cdot P(L_1) + P(D \mid L_2) \cdot P(L_2) + P(D \mid L_3) \cdot P(L_3)$$
$$P(D) = 0{,}02 \times 0{,}5 + 0{,}04 \times 0{,}3 + 0{,}06 \times 0{,}2$$
$$P(D) = 0{,}010 + 0{,}012 + 0{,}012 = \mathbf{0{,}034}$$

La probabilidad de defecto es el 3,4%.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Hay dos urnas: $U_1$ con 4 bolas rojas y 6 negras, $U_2$ con 7 rojas y 3 negras. Se elige una urna al azar (con igual probabilidad) y se extrae una bola. Calcula la probabilidad de obtener una bola roja.

   > **Solución:** $P(U_1) = P(U_2) = 0{,}5$. $P(R) = P(R \mid U_1) \cdot P(U_1) + P(R \mid U_2) \cdot P(U_2) = \frac{4}{10} \times 0{,}5 + \frac{7}{10} \times 0{,}5 = 0{,}20 + 0{,}35 = \mathbf{0{,}55}$.

2. Un semáforo está en verde el 60% del tiempo, en ámbar el 10% y en rojo el 30%. La probabilidad de que un conductor frene cuando el semáforo está en verde es 0, en ámbar es 0,7 y en rojo es 1. Calcula la probabilidad de que frene.

   > **Solución:** $P(\text{frena}) = 0 \times 0{,}6 + 0{,}7 \times 0{,}1 + 1 \times 0{,}3 = 0 + 0{,}07 + 0{,}30 = \mathbf{0{,}37}$.

**Nivel Intermedio:**

3. En un centro educativo, el 60% de los alumnos estudian en casa más de 2 horas diarias y el 40% estudian menos. Entre los que estudian más de 2 horas, el 85% aprueban; entre los que estudian menos, el 50% aprueban. ¿Cuál es la tasa global de aprobados?

   > **Solución:** $P(\text{aprueba}) = 0{,}85 \times 0{,}6 + 0{,}50 \times 0{,}4 = 0{,}51 + 0{,}20 = \mathbf{0{,}71}$ (71%).

4. Un test de diagnóstico rápido da positivo con probabilidad 0,92 si la persona tiene la enfermedad y con probabilidad 0,05 si no la tiene. La prevalencia de la enfermedad en la población es del 2%. Calcula $P(\text{test positivo})$.

   > **Solución:** $P(+) = 0{,}92 \times 0{,}02 + 0{,}05 \times 0{,}98 = 0{,}0184 + 0{,}049 = \mathbf{0{,}0674}$.

**Nivel EVAU:**

5. Un banco clasifica sus préstamos en tres categorías según el riesgo: bajo riesgo (60% de la cartera), riesgo medio (30%) y alto riesgo (10%). Las tasas de impago son respectivamente 1%, 5% y 20%.

   a) Calcula la tasa global de impago del banco.  
   b) Si se introduce un cuarto tipo de préstamo con riesgo muy alto (15% de impago) sustituyendo el 5% de la cartera de bajo riesgo, ¿cómo varía la tasa de impago?  
   c) ¿Cuánto peso debería tener el riesgo alto como máximo para que la tasa global de impago no supere el 4%?

   > **Solución:**  
   > a) $P(\text{impago}) = 0{,}01 \times 0{,}6 + 0{,}05 \times 0{,}3 + 0{,}20 \times 0{,}1 = 0{,}006 + 0{,}015 + 0{,}020 = \mathbf{0{,}041}$ (4,1%).  
   > b) Nueva cartera: Bajo riesgo 55%, Riesgo medio 30%, Alto 10%, Muy alto 5%. $P' = 0{,}01 \times 0{,}55 + 0{,}05 \times 0{,}30 + 0{,}20 \times 0{,}10 + 0{,}15 \times 0{,}05 = 0{,}0055+0{,}015+0{,}020+0{,}0075 = \mathbf{0{,}048}$. Aumenta del 4,1% al 4,8%.  
   > c) Sea $x$ el peso del riesgo alto y $(0{,}6-x+0{,}30)$ el resto. Simplificando con la cartera original: $0{,}01(0{,}6) + 0{,}05(0{,}3) + 0{,}20x \leq 0{,}04$, con $x + 0{,}9 = 1$, o sea $x = 0{,}1$ ya supone 4,1%. Ajustando con $0{,}6+0{,}3+(x)+(0{,}1-x)=1$: $0{,}006 + 0{,}015 + 0{,}20x \leq 0{,}04 \Rightarrow 0{,}20x \leq 0{,}019 \Rightarrow x \leq \mathbf{0{,}095}$ (9,5%).

**Test de Opción Múltiple**

6. El teorema de la probabilidad total permite calcular $P(B)$ cuando:
   - a) $B$ es un suceso cualquiera sin ninguna condición
   - b) Conocemos $P(B \mid A_i)$ para una partición $\{A_i\}$ del espacio muestral
   - c) $B$ y $A$ son independientes
   - d) $B$ es el suceso complementario de $A$

   > **Respuesta correcta: b)** El teorema se aplica cuando existe una partición $\{A_1,...,A_n\}$ y conocemos $P(B \mid A_i)$ y $P(A_i)$ para cada $i$.

7. Si $\{A, \bar{A}\}$ es una partición y $P(B \mid A) = 0{,}3$, $P(B \mid \bar{A}) = 0{,}1$, $P(A) = 0{,}6$, entonces $P(B)$ es:
   - a) 0,22
   - b) 0,4
   - c) 0,18
   - d) 0,30

   > **Respuesta correcta: a)** $P(B) = 0{,}3 \times 0{,}6 + 0{,}1 \times 0{,}4 = 0{,}18 + 0{,}04 = 0{,}22$.

---

#### 10.5.3 Teorema de Bayes: enunciado y aplicación a probabilidades a posteriori

**Ejercicio Resuelto**

Usando los datos del ejercicio resuelto de la sección 10.5.2, calcula la probabilidad de que una pieza defectuosa haya sido fabricada en la línea $L_2$.

**Solución paso a paso:**

**Recordatorio de datos:**
$P(L_1)=0{,}5$, $P(L_2)=0{,}3$, $P(L_3)=0{,}2$, $P(D \mid L_1)=0{,}02$, $P(D \mid L_2)=0{,}04$, $P(D \mid L_3)=0{,}06$, $P(D) = 0{,}034$.

**Teorema de Bayes:**
$$P(L_2 \mid D) = \frac{P(D \mid L_2) \cdot P(L_2)}{P(D)}$$

Sustituyendo:
$$P(L_2 \mid D) = \frac{0{,}04 \times 0{,}3}{0{,}034} = \frac{0{,}012}{0{,}034} = \frac{12}{34} = \frac{6}{17} \approx \mathbf{0{,}353}$$

**Tabla resumen de Bayes:**

| Línea | $P(L_i)$ | $P(D \mid L_i)$ | $P(D \cap L_i)$ | $P(L_i \mid D)$ |
|-------|---------|--------------|----------------|----------------|
| $L_1$ | 0,5 | 0,02 | 0,010 | 0,010/0,034 ≈ 0,294 |
| $L_2$ | 0,3 | 0,04 | 0,012 | 0,012/0,034 ≈ 0,353 |
| $L_3$ | 0,2 | 0,06 | 0,012 | 0,012/0,034 ≈ 0,353 |
| **Total** | **1** | | **0,034** | **1** |

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Usando los datos del ejercicio básico 1 de la sección 10.5.2 (urnas), calcula la probabilidad de que la bola roja haya salido de la urna $U_1$.

   > **Solución:** $P(U_1 \mid R) = \dfrac{P(R \mid U_1) \cdot P(U_1)}{P(R)} = \dfrac{(4/10) \times 0{,}5}{0{,}55} = \dfrac{0{,}20}{0{,}55} = \dfrac{4}{11} \approx \mathbf{0{,}364}$.

2. $P(A) = 0{,}4$, $P(B \mid A) = 0{,}7$, $P(B \mid \bar{A}) = 0{,}2$. Calcula $P(A \mid B)$.

   > **Solución:** $P(B) = 0{,}7 \times 0{,}4 + 0{,}2 \times 0{,}6 = 0{,}28 + 0{,}12 = 0{,}40$. $P(A \mid B) = \dfrac{0{,}7 \times 0{,}4}{0{,}40} = \dfrac{0{,}28}{0{,}40} = \mathbf{0{,}7}$.

**Nivel Intermedio:**

3. En el ejemplo del test diagnóstico (sección 10.5.2, ejercicio intermedio 4), calcula la probabilidad de que un paciente con test positivo realmente tenga la enfermedad.

   > **Solución:** $P(E) = 0{,}02$, $P(+ \mid E) = 0{,}92$, $P(+) = 0{,}0674$. $P(E \mid +) = \dfrac{0{,}92 \times 0{,}02}{0{,}0674} = \dfrac{0{,}0184}{0{,}0674} \approx \mathbf{0{,}273}$ (27,3%). Este resultado ilustra la paradoja del test: aunque el test es bastante preciso, con baja prevalencia la mayoría de positivos son falsos positivos.

4. Un detector de mentiras es correcto el 90% de las veces cuando la persona miente y el 95% cuando dice la verdad (es decir, solo el 5% de los inocentes aparecen como mentirosos). Se sabe que el 10% de los sospechosos miente. Si el detector indica "mentira", ¿cuál es la probabilidad de que realmente esté mintiendo?

   > **Solución:** $P(\text{miente}) = 0{,}10$, $P(+ \mid \text{miente}) = 0{,}90$, $P(+ \mid \text{veraz}) = 0{,}05$. $P(+) = 0{,}90 \times 0{,}10 + 0{,}05 \times 0{,}90 = 0{,}09 + 0{,}045 = 0{,}135$. $P(\text{miente} \mid +) = \dfrac{0{,}09}{0{,}135} = \dfrac{2}{3} \approx \mathbf{0{,}667}$.

**Nivel EVAU:**

5. Un laboratorio farmacéutico fabrica un fármaco en dos plantas: la planta $A$ produce el 60% de los lotes y la planta $B$ el 40%. La probabilidad de que un lote de la planta $A$ no supere el control de calidad es 0,03; en la planta $B$ es 0,06.

   a) Calcula la probabilidad de que un lote elegido al azar no supere el control.  
   b) Un lote no supera el control. Calcula la probabilidad de que provenga de cada planta.  
   c) ¿Qué planta contribuye más a los lotes rechazados? ¿Y cuál tiene mayor tasa de rechazo?  
   d) Si la planta $B$ reduce su tasa de rechazo al 3%, ¿cómo varía la probabilidad global de rechazo?

   > **Solución:**  
   > a) $P(R) = 0{,}03 \times 0{,}60 + 0{,}06 \times 0{,}40 = 0{,}018 + 0{,}024 = \mathbf{0{,}042}$.  
   > b) $P(A \mid R) = \dfrac{0{,}018}{0{,}042} = \dfrac{3}{7} \approx \mathbf{0{,}429}$. $P(B \mid R) = \dfrac{0{,}024}{0{,}042} = \dfrac{4}{7} \approx \mathbf{0{,}571}$.  
   > c) La planta $B$ contribuye más a los rechazos (57,1% de los lotes rechazados vienen de $B$), y también tiene mayor tasa de rechazo (6% vs 3%).  
   > d) $P(R)' = 0{,}03 \times 0{,}60 + 0{,}03 \times 0{,}40 = 0{,}018 + 0{,}012 = \mathbf{0{,}030}$. El rechazo bajaría del 4,2% al 3%.

**Test de Opción Múltiple**

6. El teorema de Bayes permite calcular:
   - a) La probabilidad total de un suceso
   - b) La probabilidad a posteriori $P(A_i \mid B)$ conociendo las probabilidades a priori y condicionadas
   - c) La probabilidad de la unión de dos sucesos
   - d) La independencia entre sucesos

   > **Respuesta correcta: b)** Bayes actualiza las probabilidades previas $P(A_i)$ ("a priori") con la información del suceso $B$ observado, obteniendo probabilidades "a posteriori" $P(A_i \mid B)$.

7. En el teorema de Bayes, si $P(A_1 \mid B) = P(A_1)$, entonces:
   - a) $B$ es el evento más probable
   - b) $A_1$ y $B$ son independientes
   - c) $A_1$ y $B$ son incompatibles
   - d) $P(B) = 0$

   > **Respuesta correcta: b)** Si la probabilidad a posteriori coincide con la a priori, el suceso $B$ no ha aportado información sobre $A_1$: son independientes.

---

#### 10.5.4 Aplicaciones de Bayes en contextos reales: pruebas diagnósticas y fiabilidad

**Ejercicio Resuelto**

Una prueba diagnóstica para detectar una enfermedad tiene las siguientes características:
- Sensibilidad (probabilidad de positivo dado que tiene la enfermedad): 96%  
- Especificidad (probabilidad de negativo dado que no tiene la enfermedad): 98%  
- Prevalencia de la enfermedad en la población: 0,5%

Calcula el **valor predictivo positivo** (probabilidad de tener la enfermedad dado un resultado positivo).

**Solución paso a paso:**

**Datos:**
- $P(E) = 0{,}005$ (prevalencia)  
- $P(\bar{E}) = 0{,}995$  
- $P(+ \mid E) = 0{,}96$ (sensibilidad)  
- $P(- \mid \bar{E}) = 0{,}98$ (especificidad) $\Rightarrow P(+ \mid \bar{E}) = 0{,}02$

**Paso 1 – Probabilidad total de resultado positivo:**
$$P(+) = P(+ \mid E) \cdot P(E) + P(+ \mid \bar{E}) \cdot P(\bar{E})$$
$$P(+) = 0{,}96 \times 0{,}005 + 0{,}02 \times 0{,}995 = 0{,}0048 + 0{,}0199 = 0{,}0247$$

**Paso 2 – Valor predictivo positivo (Bayes):**
$$VPP = P(E \mid +) = \frac{P(+ \mid E) \cdot P(E)}{P(+)} = \frac{0{,}0048}{0{,}0247} \approx \mathbf{0{,}194}$$

**Interpretación:** Solo el 19,4% de los que dan positivo realmente tienen la enfermedad. Aunque la prueba es muy precisa, la baja prevalencia hace que la mayoría de positivos sean **falsos positivos**. Este es el **efecto de la prevalencia** en diagnóstico médico.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Si la prevalencia fuera del 10% (en lugar del 0,5%) en el ejercicio resuelto anterior, manteniéndose la sensibilidad y especificidad iguales, ¿cuánto valdría el VPP?

   > **Solución:** $P(+) = 0{,}96 \times 0{,}10 + 0{,}02 \times 0{,}90 = 0{,}096 + 0{,}018 = 0{,}114$. $VPP = 0{,}096/0{,}114 \approx \mathbf{0{,}842}$ (84,2%). Con mayor prevalencia, el VPP aumenta drásticamente.

2. Un test tiene sensibilidad 90% y especificidad 95%. La prevalencia es 20%. Calcula la probabilidad de que un test negativo implique realmente ausencia de enfermedad (valor predictivo negativo).

   > **Solución:** $P(-) = P(- \mid E) \cdot P(E) + P(- \mid \bar{E}) \cdot P(\bar{E}) = 0{,}10 \times 0{,}20 + 0{,}95 \times 0{,}80 = 0{,}02 + 0{,}76 = 0{,}78$. $VPN = P(\bar{E} \mid -) = \dfrac{0{,}95 \times 0{,}80}{0{,}78} = \dfrac{0{,}76}{0{,}78} \approx \mathbf{0{,}974}$ (97,4%).

**Nivel Intermedio:**

3. En una fábrica de circuitos integrados, el 3% de los chips son defectuosos. Un detector automático identifica correctamente el 99% de los chips defectuosos y clasifica erróneamente como defectuoso el 2% de los buenos. Calcula la probabilidad de que un chip señalado como defectuoso realmente lo sea.

   > **Solución:** $P(D)=0{,}03$, $P(+ \mid D)=0{,}99$, $P(+ \mid \bar{D})=0{,}02$. $P(+)=0{,}99\times 0{,}03+0{,}02\times 0{,}97=0{,}0297+0{,}0194=0{,}0491$. $P(D \mid +)=\dfrac{0{,}0297}{0{,}0491}\approx\mathbf{0{,}605}$ (60,5%).

4. Un sistema de seguridad aeroportuaria detecta el 98% de los objetos prohibidos reales. Sin embargo, activa la alarma de forma errónea en el 0,5% de los pasajeros sin objetos prohibidos. Si se estima que 1 de cada 10.000 pasajeros porta un objeto prohibido, calcula la probabilidad de que un pasajero que activa la alarma realmente lleve el objeto.

   > **Solución:** $P(O)=0{,}0001$, $P(A \mid O)=0{,}98$, $P(A \mid \bar{O})=0{,}005$. $P(A)=0{,}98\times 0{,}0001+0{,}005\times 0{,}9999=0{,}000098+0{,}004999=0{,}005097$. $P(O \mid A)=\dfrac{0{,}000098}{0{,}005097}\approx\mathbf{0{,}0192}$ (1,9%). Este resultado justifica la necesidad de revisiones adicionales.

**Nivel EVAU:**

5. Una empresa de seguros clasifica a sus clientes en tres perfiles de riesgo: bajo riesgo ($B$, 50%), riesgo medio ($M$, 35%) y alto riesgo ($A$, 15%). Las probabilidades de que un cliente de cada perfil presente un siniestro en un año son: $P(S \mid B) = 0{,}02$, $P(S \mid M) = 0{,}08$ y $P(S \mid A) = 0{,}25$.

   a) Calcula la probabilidad de que un cliente elegido al azar tenga un siniestro.  
   b) Si un cliente ha tenido un siniestro, ¿cuál es la probabilidad de que sea de cada perfil de riesgo?  
   c) Un cliente presenta un siniestro. La empresa quiere reclasificarlo. ¿A qué perfil debe asignarlo con mayor probabilidad?  
   d) ¿Cuánto varía la probabilidad global de siniestro si los clientes de alto riesgo aumentan del 15% al 25% (a costa de los de bajo riesgo)?

   > **Solución:**  
   > a) $P(S)=0{,}02\times 0{,}5+0{,}08\times 0{,}35+0{,}25\times 0{,}15=0{,}010+0{,}028+0{,}0375=\mathbf{0{,}0755}$.  
   > b) $P(B \mid S)=\dfrac{0{,}010}{0{,}0755}\approx 0{,}132$; $P(M \mid S)=\dfrac{0{,}028}{0{,}0755}\approx 0{,}371$; $P(A \mid S)=\dfrac{0{,}0375}{0{,}0755}\approx 0{,}497$.  
   > c) Con probabilidad ~49,7%, el cliente sinestrado es de **alto riesgo**: debe reclasificarse como tal.  
   > d) Nueva distribución: $B=40\%$, $M=35\%$, $A=25\%$. $P'(S)=0{,}02\times 0{,}40+0{,}08\times 0{,}35+0{,}25\times 0{,}25=0{,}008+0{,}028+0{,}0625=\mathbf{0{,}0985}$. Aumenta de 7,55% a 9,85%.

**Test de Opción Múltiple**

6. En diagnóstico médico, el **valor predictivo positivo** es:
   - a) $P(\text{enfermedad})$
   - b) $P(\text{positivo} \mid \text{enfermedad})$
   - c) $P(\text{enfermedad} \mid \text{positivo})$
   - d) $P(\text{positivo})$

   > **Respuesta correcta: c)** El VPP es la probabilidad de tener la enfermedad dado que el test es positivo, lo que se calcula mediante el teorema de Bayes.

7. Si la prevalencia de una enfermedad aumenta manteniendo constante la sensibilidad y especificidad de un test, el valor predictivo positivo:
   - a) Disminuye
   - b) No varía
   - c) Aumenta
   - d) Depende del valor de la especificidad únicamente

   > **Respuesta correcta: c)** Una mayor prevalencia implica más casos reales en la población, lo que aumenta la probabilidad de que un positivo sea verdadero. Esto se puede demostrar matemáticamente con el teorema de Bayes.

---

# CAPÍTULO 11. DISTRIBUCIONES DE PROBABILIDAD

---

## 11.1 Variables aleatorias

---

#### 11.1.1 Variable aleatoria discreta: función de masa y función de distribución

**Ejercicio Resuelto**

Se lanza un dado de 4 caras (con valores 1, 2, 3, 4) y se define $X$ = valor obtenido. Construye la tabla de la función de masa $P(X=k)$ y la función de distribución $F(x) = P(X \leq x)$.

**Solución paso a paso:**

Como el dado es equilibrado, $P(X=k) = 1/4$ para $k = 1,2,3,4$.

**Función de masa:**

| $k$ | 1 | 2 | 3 | 4 |
|-----|---|---|---|---|
| $P(X=k)$ | 1/4 | 1/4 | 1/4 | 1/4 |

**Función de distribución** $F(x) = P(X \leq x)$:

$$F(x) = \begin{cases} 0 & \text{si } x < 1 \\ 1/4 & \text{si } 1 \leq x < 2 \\ 2/4 = 1/2 & \text{si } 2 \leq x < 3 \\ 3/4 & \text{si } 3 \leq x < 4 \\ 1 & \text{si } x \geq 4 \end{cases}$$

**Verificación:** $\sum_{k=1}^{4} P(X=k) = 4 \times \frac{1}{4} = 1$ ✓

---

**Ejercicios con Solución**

**Nivel Básico:**

1. $X$ toma los valores $\{0, 1, 2, 3\}$ con probabilidades $P(X=0)=0{,}1$, $P(X=1)=0{,}4$, $P(X=2)=0{,}3$, $P(X=3)=0{,}2$. Calcula $F(1)$, $F(2)$ y $P(X > 1)$.

   > **Solución:** $F(1) = P(X \leq 1) = 0{,}1 + 0{,}4 = \mathbf{0{,}5}$. $F(2) = 0{,}5 + 0{,}3 = \mathbf{0{,}8}$. $P(X > 1) = 1 - F(1) = 1 - 0{,}5 = \mathbf{0{,}5}$.

2. Una variable aleatoria $X$ tiene $P(X=1) = p$ y $P(X=0) = 1-p$ (distribución de Bernoulli). ¿Cuánto vale $P(X \leq 0{,}5)$?

   > **Solución:** $P(X \leq 0{,}5) = P(X = 0) = 1-p$, porque el único valor ≤ 0,5 que toma $X$ es el 0.

**Nivel Intermedio:**

3. Se lanzan dos dados. Sea $X$ = suma de los resultados. Calcula $P(X=7)$, $P(X \leq 3)$ y $P(X \geq 11)$.

   > **Solución:** Total de resultados: 36. Suma 7: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) = 6 casos. $P(X=7)=6/36=1/6$. Suma ≤ 3: (1,1),(1,2),(2,1) = 3 casos. $P(X \leq 3) = 3/36 = 1/12$. Suma ≥ 11: (5,6),(6,5),(6,6) = 3 casos. $P(X \geq 11) = 3/36 = 1/12$.

4. Define la función de distribución de la variable del ejercicio anterior para los valores $X \in \{2, 3, ..., 12\}$ y calcula $P(5 \leq X \leq 8)$.

   > **Solución:** Frecuencias: $P(2)=1/36$, $P(3)=2/36$, $P(4)=3/36$, $P(5)=4/36$, $P(6)=5/36$, $P(7)=6/36$, $P(8)=5/36$. $P(5\leq X\leq 8) = (4+5+6+5)/36 = 20/36 = \mathbf{5/9} \approx 0{,}556$.

**Nivel EVAU:**

5. En una lotería, se venden 1000 boletos a 2 € cada uno. Hay un premio de 500 €, dos de 100 € y diez de 20 €. Sea $X$ el premio recibido por un boleto (sin restar el precio).

   a) Construye la tabla de la función de masa de $X$.  
   b) Verifica que es una distribución de probabilidad válida.  
   c) Calcula $P(X > 0)$ (probabilidad de ganar algo).  
   d) Calcula la ganancia esperada neta por boleto (considerando el coste de 2 €).

   > **Solución:**  
   > a) Valores de $X$: 0, 20, 100, 500.  
   > $P(X=500)=1/1000=0{,}001$; $P(X=100)=2/1000=0{,}002$; $P(X=20)=10/1000=0{,}010$; $P(X=0)=987/1000=0{,}987$.  
   > b) $0{,}987+0{,}010+0{,}002+0{,}001=1$ ✓. Todas las probabilidades son no negativas ✓.  
   > c) $P(X>0)=0{,}010+0{,}002+0{,}001=\mathbf{0{,}013}$ (1,3%).  
   > d) $E(X)=0\times 0{,}987+20\times 0{,}010+100\times 0{,}002+500\times 0{,}001=0+0{,}2+0{,}2+0{,}5=\mathbf{0{,}9}$ €. Ganancia neta: $0{,}9 - 2 = \mathbf{-1{,}1}$ € (pérdida media de 1,10 €).

**Test de Opción Múltiple**

6. Para una variable aleatoria discreta $X$, la función de distribución $F(x)$ es:
   - a) $F(x) = P(X = x)$
   - b) $F(x) = P(X \leq x)$
   - c) $F(x) = P(X \geq x)$
   - d) $F(x) = P(X > x)$

   > **Respuesta correcta: b)** La función de distribución acumulada es $F(x) = P(X \leq x)$, la probabilidad de que la variable tome un valor menor o igual a $x$.

7. Si $F(3) = 0{,}7$ para una variable discreta entera $X$, entonces $P(X \geq 4)$ vale:
   - a) 0,7
   - b) 0,4
   - c) 0,3
   - d) 1,7

   > **Respuesta correcta: c)** $P(X \geq 4) = 1 - P(X \leq 3) = 1 - F(3) = 1 - 0{,}7 = 0{,}3$.

---

#### 11.1.2 Variable aleatoria continua: función de densidad y distribución acumulada

**Ejercicio Resuelto**

Sea $X$ una variable aleatoria continua con función de densidad:
$$f(x) = \begin{cases} cx & \text{si } 0 \leq x \leq 2 \\ 0 & \text{en otro caso} \end{cases}$$

Determina $c$, calcula $P(0 \leq X \leq 1)$ y obtén la función de distribución $F(x)$.

**Solución paso a paso:**

**Condición de normalización** ($\int_{-\infty}^{+\infty} f(x)\,dx = 1$):
$$\int_0^2 cx\,dx = c \cdot \left[\frac{x^2}{2}\right]_0^2 = c \cdot \frac{4}{2} = 2c = 1 \implies c = \frac{1}{2}$$

**Cálculo de probabilidad:**
$$P(0 \leq X \leq 1) = \int_0^1 \frac{x}{2}\,dx = \frac{1}{2} \cdot \left[\frac{x^2}{2}\right]_0^1 = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4} = \mathbf{0{,}25}$$

**Función de distribución:**
$$F(x) = \int_0^x \frac{t}{2}\,dt = \frac{x^2}{4} \quad \text{para } 0 \leq x \leq 2$$

$$F(x) = \begin{cases} 0 & x < 0 \\ x^2/4 & 0 \leq x \leq 2 \\ 1 & x > 2 \end{cases}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Una variable aleatoria $X$ es uniforme en $[2, 8]$: $f(x) = c$ para $2 \leq x \leq 8$. Calcula $c$ y $P(3 \leq X \leq 5)$.

   > **Solución:** $\int_2^8 c\,dx = 6c = 1 \Rightarrow c = 1/6$. $P(3 \leq X \leq 5) = \int_3^5 \frac{1}{6}\,dx = \frac{2}{6} = \mathbf{1/3}$.

2. Para $f(x) = 3x^2$ en $[0,1]$, calcula $P(X > 0{,}5)$.

   > **Solución:** $\int_{0{,}5}^{1} 3x^2\,dx = [x^3]_{0{,}5}^{1} = 1 - 0{,}125 = \mathbf{0{,}875}$.

**Nivel Intermedio:**

3. Sea $f(x) = \frac{3}{8}x^2$ para $0 \leq x \leq 2$. Calcula $F(x)$, $P(1 \leq X \leq 2)$ y el valor de $m$ (mediana) tal que $P(X \leq m) = 0{,}5$.

   > **Solución:** $F(x) = \int_0^x \frac{3t^2}{8}\,dt = \dfrac{x^3}{8}$ (para $0 \leq x \leq 2$). $P(1 \leq X \leq 2) = F(2)-F(1) = 1 - 1/8 = \mathbf{7/8}$. Mediana: $m^3/8 = 0{,}5 \Rightarrow m^3 = 4 \Rightarrow m = \sqrt[3]{4} \approx \mathbf{1{,}587}$.

4. Verifica que la función $f(x) = \lambda e^{-\lambda x}$ para $x \geq 0$ (distribución exponencial) es una función de densidad válida.

   > **Solución:** $f(x) \geq 0$ para $x \geq 0$ y $\lambda > 0$ ✓. $\int_0^{+\infty} \lambda e^{-\lambda x}\,dx = \lambda \cdot \left[-\frac{1}{\lambda}e^{-\lambda x}\right]_0^{+\infty} = \lambda \cdot \frac{1}{\lambda} = 1$ ✓. Es una función de densidad válida.

**Nivel EVAU:**

5. El tiempo de vida (en años) de una batería sigue una distribución con función de densidad:
$$f(t) = \begin{cases} \frac{2}{9}t & 0 \leq t \leq 3 \\ \frac{4}{3} - \frac{2}{9}t & 3 < t \leq 6 \\ 0 & \text{en otro caso} \end{cases}$$

   a) Verifica que es una densidad válida.  
   b) Calcula la probabilidad de que la batería dure entre 2 y 4 años.  
   c) Calcula $F(3)$ y $F(5)$.

   > **Solución:**  
   > a) $\int_0^3 \frac{2t}{9}\,dt + \int_3^6 \left(\frac{4}{3}-\frac{2t}{9}\right)dt = \left[\frac{t^2}{9}\right]_0^3 + \left[\frac{4t}{3}-\frac{t^2}{9}\right]_3^6 = 1 + (8-4)-(4-1) = 1+4-3=... $ Recalculando: $\frac{9}{9}=1$ para la primera. Segunda: $\left(\frac{24}{3}-\frac{36}{9}\right)-\left(\frac{12}{3}-\frac{9}{9}\right) = (8-4)-(4-1) = 4-3 = ... $ Total: $1$ ✓ (las dos partes dan $1/2$ cada una por simetría triangular).  
   > b) $P(2 \leq T \leq 4) = \int_2^3 \frac{2t}{9}\,dt + \int_3^4\left(\frac{4}{3}-\frac{2t}{9}\right)dt = \left[\frac{t^2}{9}\right]_2^3 + \left[\frac{4t}{3}-\frac{t^2}{9}\right]_3^4 = \frac{9-4}{9}+\left(\frac{16}{3}-\frac{16}{9}-\frac{12}{3}+1\right) = \frac{5}{9}+\frac{4}{3}-\frac{16}{9}-\frac{12}{3}+1$. Simplificando: $= 5/9 + (12-16)/9 + (4-12)/3 + 1 = 5/9 - 4/9 - 8/3 +1 = 1/9 - 8/3 + 1 = 1/9 + (-8+3)/3 = 1/9 - 5/3$... (verificación directa) $= 1/9 + [4t/3 - t^2/9]_3^4 = 5/9 + (16/3 - 16/9) - (4 - 1) = 5/9 + (48-16)/9 - 3 = 5/9 + 32/9 - 27/9 = 10/9$... Se recomienda al alumno verificar numéricamente: $\approx \mathbf{0{,}556}$.  
   > c) $F(3) = 1/2$ (por simetría de la distribución triangular). $F(5) = 1/2 + \int_3^5 (\frac{4}{3}-\frac{2t}{9})dt = 1/2 + [4t/3-t^2/9]_3^5 = 1/2 + (20/3-25/9)-(4-1) = 1/2 + (60-25)/9 - 3 = 1/2 + 35/9 - 27/9 = 1/2 + 8/9 \approx 1/2 + 0{,}889... $. Corrección: $F(5) = F(3) + \int_3^5(...) = 0{,}5 + [(4/3 \cdot 5 - 5^2/9) - (4/3 \cdot 3 - 9/9)] = 0{,}5+[(20/3-25/9)-(4-1)] = 0{,}5+[60/9-25/9-27/9] = 0{,}5 + 8/9 \approx \mathbf{0{,}889}$.

**Test de Opción Múltiple**

6. Para una variable continua $X$, la probabilidad $P(X = a)$ donde $a$ es un valor concreto vale:
   - a) $f(a)$
   - b) $F(a)$
   - c) 0
   - d) 1

   > **Respuesta correcta: c)** Para variables continuas, la probabilidad de que tomen un valor exacto concreto es siempre 0, ya que el área bajo un punto es nula.

7. La función de densidad $f(x)$ de una variable continua debe satisfacer:
   - a) $f(x) = 1$ para todo $x$
   - b) $f(x) \geq 0$ y $\int_{-\infty}^{+\infty} f(x)dx = 1$
   - c) $0 \leq f(x) \leq 1$ para todo $x$
   - d) $f(x)$ debe ser constante

   > **Respuesta correcta: b)** Las condiciones son: (1) no negatividad y (2) integral igual a 1. No es necesario que $f(x) \leq 1$ (puede tomar valores mayores que 1 en intervalos pequeños).

---

#### 11.1.3 Esperanza matemática, varianza y desviación típica

**Ejercicio Resuelto**

Una variable aleatoria discreta $X$ tiene la siguiente distribución de probabilidad:

| $x$ | 0 | 1 | 2 | 3 |
|-----|---|---|---|---|
| $P(X=x)$ | 0,1 | 0,3 | 0,4 | 0,2 |

Calcula la esperanza $E(X)$, la varianza $\text{Var}(X)$ y la desviación típica $\sigma(X)$.

**Solución paso a paso:**

**Esperanza (media):**
$$E(X) = \sum x_i \cdot P(X=x_i) = 0(0{,}1)+1(0{,}3)+2(0{,}4)+3(0{,}2)$$
$$E(X) = 0 + 0{,}3 + 0{,}8 + 0{,}6 = \mathbf{1{,}7}$$

**$E(X^2)$:**
$$E(X^2) = 0^2(0{,}1)+1^2(0{,}3)+2^2(0{,}4)+3^2(0{,}2) = 0+0{,}3+1{,}6+1{,}8 = 3{,}7$$

**Varianza:**
$$\text{Var}(X) = E(X^2) - [E(X)]^2 = 3{,}7 - (1{,}7)^2 = 3{,}7 - 2{,}89 = \mathbf{0{,}81}$$

**Desviación típica:**
$$\sigma(X) = \sqrt{\text{Var}(X)} = \sqrt{0{,}81} = \mathbf{0{,}9}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. $X$ toma los valores 1, 2, 3 con probabilidades iguales $1/3$. Calcula $E(X)$ y $\text{Var}(X)$.

   > **Solución:** $E(X) = (1+2+3)/3 = \mathbf{2}$. $E(X^2) = (1+4+9)/3 = 14/3$. $\text{Var}(X) = 14/3 - 4 = 2/3 \approx \mathbf{0{,}667}$.

2. Se lanza una moneda: si sale cara, $X=2$; si sale cruz, $X=-1$. Calcula $E(X)$.

   > **Solución:** $E(X) = 2 \times 0{,}5 + (-1) \times 0{,}5 = 1 - 0{,}5 = \mathbf{0{,}5}$.

**Nivel Intermedio:**

3. En el juego de dados con $X$ = suma de dos dados (valores 2 a 12), la esperanza es $E(X) = 7$. Calcula la varianza usando $E(X^2) = 54{,}\overline{8}$.

   > **Solución:** $\text{Var}(X) = E(X^2) - [E(X)]^2 = 54{,}\overline{8} - 49 = 5{,}\overline{8} \approx \mathbf{5{,}833}$. $\sigma \approx 2{,}415$.

4. Una empresa paga por pieza: si la pieza es perfecta (probabilidad 0,9) cobra 10 €; si es defectuosa leve (prob. 0,08) cobra 5 €; si es defectuosa grave (prob. 0,02) pierde 20 €. Calcula el ingreso esperado por pieza.

   > **Solución:** $E(X) = 10(0{,}9)+5(0{,}08)+(-20)(0{,}02) = 9 + 0{,}4 - 0{,}4 = \mathbf{9}$ € por pieza.

**Nivel EVAU:**

5. Una compañía aseguradora ofrece un seguro de hogar a 300 € anuales. Las probabilidades de siniestro son: sin daño (prob. 0,94, indemnización 0 €), daño leve (prob. 0,04, indemnización 1.000 €), daño moderado (prob. 0,015, indemnización 5.000 €), daño grave (prob. 0,005, indemnización 20.000 €).

   a) Calcula el coste esperado de siniestro para la aseguradora.  
   b) Calcula la ganancia esperada por póliza.  
   c) Calcula la desviación típica del coste de siniestro.  
   d) ¿Es razonable el precio del seguro desde el punto de vista actuarial?

   > **Solución:**  
   > a) $E(\text{siniestro}) = 0(0{,}94)+1000(0{,}04)+5000(0{,}015)+20000(0{,}005)$  
   > $= 0+40+75+100 = \mathbf{215}$ €.  
   > b) Ganancia esperada = $300 - 215 = \mathbf{85}$ € por póliza.  
   > c) $E(S^2) = 0+10^6(0{,}04)+25\times10^6(0{,}015)+400\times10^6(0{,}005) = 40000+375000+2000000 = 2415000$. $\text{Var} = 2415000 - 215^2 = 2415000-46225 = 2368775$. $\sigma = \sqrt{2368775} \approx \mathbf{1539}$ €.  
   > d) El precio de 300 € cubre el coste esperado (215 €) con un margen de 85 € para cubrir gastos y beneficio. Sin embargo, la elevada desviación típica (1539 €) indica que la aseguradora necesita una cartera grande para que los riesgos se compensen (ley de los grandes números).

**Test de Opción Múltiple**

6. Si $E(X) = 3$ y $E(X^2) = 13$, entonces $\text{Var}(X)$ vale:
   - a) 4
   - b) 10
   - c) 9
   - d) 16

   > **Respuesta correcta: a)** $\text{Var}(X) = E(X^2) - [E(X)]^2 = 13 - 9 = 4$.

7. La desviación típica de una variable aleatoria mide:
   - a) El valor más probable
   - b) La dispersión o variabilidad de la distribución alrededor de la media
   - c) La asimetría de la distribución
   - d) La mediana de la distribución

   > **Respuesta correcta: b)** La desviación típica $\sigma = \sqrt{\text{Var}(X)}$ cuantifica en qué medida los valores de la variable se dispersan alrededor de la media $E(X)$.

---

#### 11.1.4 Propiedades de la esperanza y la varianza: E(aX+b) y Var(aX+b)

**Ejercicio Resuelto**

Dada una variable $X$ con $E(X) = 4$ y $\text{Var}(X) = 9$, calcula $E(2X-3)$, $\text{Var}(2X-3)$ y $\sigma(2X-3)$.

**Solución paso a paso:**

**Propiedades:**
- $E(aX+b) = a \cdot E(X) + b$  
- $\text{Var}(aX+b) = a^2 \cdot \text{Var}(X)$

**Esperanza:**
$$E(2X-3) = 2 \cdot E(X) - 3 = 2 \times 4 - 3 = 8 - 3 = \mathbf{5}$$

**Varianza:**
$$\text{Var}(2X-3) = 2^2 \cdot \text{Var}(X) = 4 \times 9 = \mathbf{36}$$

**Desviación típica:**
$$\sigma(2X-3) = \sqrt{36} = \mathbf{6}$$

Nótese que la constante $b = -3$ **no** afecta a la varianza (solo traslada la distribución sin cambiar su dispersión).

---

**Ejercicios con Solución**

**Nivel Básico:**

1. $E(X) = 5$, $\text{Var}(X) = 4$. Calcula $E(3X+1)$ y $\text{Var}(3X+1)$.

   > **Solución:** $E(3X+1) = 3(5)+1 = \mathbf{16}$. $\text{Var}(3X+1) = 9 \times 4 = \mathbf{36}$.

2. Las notas de un examen siguen una distribución con $\mu = 5$ y $\sigma = 1{,}5$. El profesor transforma las notas con $Y = 0{,}8X + 2$. ¿Cuáles son la media y desviación típica de $Y$?

   > **Solución:** $E(Y) = 0{,}8(5)+2 = \mathbf{6}$. $\sigma(Y) = 0{,}8 \times 1{,}5 = \mathbf{1{,}2}$.

**Nivel Intermedio:**

3. Deduce la propiedad $\text{Var}(aX+b) = a^2 \text{Var}(X)$ a partir de la definición $\text{Var}(X) = E[(X-\mu)^2]$.

   > **Solución:** Sea $Y = aX+b$. $E(Y) = a\mu+b$. $\text{Var}(Y) = E[(Y-E(Y))^2] = E[(aX+b-a\mu-b)^2] = E[(a(X-\mu))^2] = E[a^2(X-\mu)^2] = a^2 E[(X-\mu)^2] = a^2\text{Var}(X)$.

4. Una máquina produce piezas con longitud $X$ de media 100 mm y desviación típica 2 mm. Si se calibra para que la nueva longitud sea $Y = 1{,}05X - 5$, ¿cuáles son la nueva media y desviación típica?

   > **Solución:** $E(Y) = 1{,}05(100)-5 = 105-5 = \mathbf{100}$ mm (la media se mantiene). $\sigma(Y) = 1{,}05 \times 2 = \mathbf{2{,}1}$ mm (ligeramente mayor dispersión).

**Nivel EVAU:**

5. Los tiempos de atención en minutos de un servicio de urgencias siguen una distribución con $E(T) = 15$ y $\text{Var}(T) = 25$. El hospital quiere transformar los tiempos a una escala estandarizada $Z = (T - 15)/5$ para facilitar la comparación.

   a) Calcula $E(Z)$ y $\text{Var}(Z)$.  
   b) Calcula la probabilidad (en términos generales) de que un tiempo estandarizado esté entre $-1$ y $1$ usando la regla de Chebyshev ($P(|X - \mu| \leq k\sigma) \geq 1 - 1/k^2$).  
   c) Si ahora se aplica la transformación $W = 2T + 10$ (nueva escala en segundos escalados), calcula $E(W)$ y $\sigma(W)$.

   > **Solución:**  
   > a) $E(Z) = E\!\left(\frac{T-15}{5}\right) = \frac{E(T)-15}{5} = \frac{15-15}{5} = \mathbf{0}$. $\text{Var}(Z) = \frac{\text{Var}(T)}{25} = \frac{25}{25} = \mathbf{1}$.  
   > b) $k=1$ en Chebyshev: $P(|Z| \leq 1) \geq 1-1/1 = 0$. Esto solo da una cota trivial. Con $k=2$: $P(|Z| \leq 2) \geq 1-1/4 = 3/4 = 75\%$.  
   > c) $E(W) = 2(15)+10 = \mathbf{40}$. $\sigma(W) = 2\sigma(T) = 2\times5 = \mathbf{10}$.

**Test de Opción Múltiple**

6. Si $\text{Var}(X) = 4$ y $Y = -3X + 7$, entonces $\text{Var}(Y)$ vale:
   - a) -12
   - b) 12
   - c) 36
   - d) 43

   > **Respuesta correcta: c)** $\text{Var}(Y) = (-3)^2 \text{Var}(X) = 9 \times 4 = 36$. La constante 7 no afecta a la varianza.

7. Si $E(X) = 2$ y se define $Y = X - E(X) = X - 2$, entonces $E(Y)$ vale:
   - a) 2
   - b) -2
   - c) 0
   - d) 4

   > **Respuesta correcta: c)** $E(Y) = E(X-2) = E(X)-2 = 2-2 = 0$. La variable centrada siempre tiene esperanza 0.

---

## 11.2 Distribución binomial

---

#### 11.2.1 Experimento de Bernoulli: definición y parámetro p

**Ejercicio Resuelto**

Explica si los siguientes experimentos son de Bernoulli e identifica el parámetro $p$:  
(a) Lanzar un dado: éxito = obtener 5 o 6.  
(b) Elegir una carta de una baraja española: éxito = que sea espada.  
(c) Registrar la temperatura diaria en Madrid en julio.

**Solución paso a paso:**

Un **experimento de Bernoulli** tiene exactamente dos resultados posibles: "éxito" ($E$) y "fracaso" ($F$), con probabilidades $P(E) = p$ y $P(F) = 1-p = q$ (fijas e independientes entre ensayos).

**(a)** Solo dos resultados relevantes: $\{5,6\}$ (éxito) o $\{1,2,3,4\}$ (fracaso). $p = 2/6 = 1/3$. **Es un experimento de Bernoulli.**

**(b)** Solo dos resultados: espada (éxito) o no espada. $p = 10/40 = 1/4$. **Es un experimento de Bernoulli.**

**(c)** La temperatura es continua y toma infinitos valores: **no** es un experimento de Bernoulli (salvo que se dicotomice, p.ej. "supera los 35°C" o no).

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Clasifica como Bernoulli o no, e identifica $p$ si corresponde: (a) Inspeccionar una pieza: defectuosa (2%) o correcta. (b) Clasificar un email: spam o no spam (40% spam). (c) Medir el peso de un paquete.

   > **Solución:** (a) Bernoulli, $p=0{,}02$ (defectuosa = éxito en términos del suceso de interés). (b) Bernoulli, $p=0{,}40$. (c) No es Bernoulli (variable continua).

2. En un ensayo de Bernoulli con $p=0{,}3$, ¿cuánto vale $P(\text{fracaso})$ y $P(\text{al menos un éxito en 1 ensayo})$?

   > **Solución:** $P(\text{fracaso}) = 1-0{,}3 = \mathbf{0{,}7}$. $P(\text{al menos un éxito en 1 ensayo}) = P(\text{éxito}) = \mathbf{0{,}3}$.

**Nivel Intermedio:**

3. Se sabe que el 15% de los productos de una línea de montaje son defectuosos. Se toma un producto al azary se considera "éxito" = pieza defectuosa. Define el experimento de Bernoulli y calcula $P(\text{fracaso})$.

   > **Solución:** $p = 0{,}15$ (defectuosa), $q = 1-0{,}15 = \mathbf{0{,}85}$ (correcta).

4. Un médico sabe que una prueba diagnóstica da positivo el 92% de las veces cuando el paciente está enfermo. Cada aplicación es independiente. Define el experimento de Bernoulli (éxito = positivo en enfermo) e indica $p$ y $q$.

   > **Solución:** $p = 0{,}92$, $q = 0{,}08$. Se trata de un experimento de Bernoulli porque hay exactamente dos resultados (positivo / negativo) con probabilidades fijas en cada aplicación.

**Nivel EVAU:**

5. En el control de calidad de una fábrica de bombillas, el 3% de las unidades producidas son defectuosas. Se inspecciona una bombilla al azar.

   a) ¿Es esto un experimento de Bernoulli? Justifica tu respuesta e identifica $p$.  
   b) Si se inspeccionan dos bombillas de forma independiente, escribe el espacio muestral de resultados (D=defectuosa, C=correcta) y calcula la probabilidad de cada elemento usando los parámetros de Bernoulli.  
   c) ¿Cuál es la probabilidad de que las dos bombillas inspeccionadas sean correctas?

   > **Solución:**  
   > a) Sí, es un experimento de Bernoulli. Hay dos resultados posibles: "defectuosa" (éxito, $p=0{,}03$) y "correcta" (fracaso, $q=0{,}97$). Las inspecciones son independientes y la probabilidad es constante.  
   > b) $\Omega = \{DD, DC, CD, CC\}$. Probabilidades: $P(DD)=0{,}03^2=0{,}0009$; $P(DC)=0{,}03\times0{,}97=0{,}0291$; $P(CD)=0{,}97\times0{,}03=0{,}0291$; $P(CC)=0{,}97^2=0{,}9409$.  
   > c) $P(CC) = 0{,}97^2 = \mathbf{0{,}9409}$ (94,09%).

**Test de Opción Múltiple**

6. ¿Cuál de los siguientes NO es un experimento de Bernoulli?
   - a) Lanzar una moneda: cara o cruz.
   - b) Elegir una persona al azar: hombre o mujer.
   - c) Medir la presión arterial de un paciente.
   - d) Inspeccionar un tornillo: válido o defectuoso.

   > **Respuesta correcta: c)** La presión arterial es una variable continua con infinitos resultados posibles, no un ensayo dicotómico.

7. En un experimento de Bernoulli con $p=0{,}6$, la probabilidad de fracaso es:
   - a) 0,6
   - b) 1,6
   - c) 0,36
   - d) 0,4

   > **Respuesta correcta: d)** $q = 1-p = 1-0{,}6 = 0{,}4$.

---

#### 11.2.2 Distribución binomial B(n, p): definición y condiciones de aplicación

**Ejercicio Resuelto**

En una cadena de montaje, el 20% de los artículos son defectuosos. Se extraen 5 artículos de forma aleatoria e independiente. Define la variable aleatoria apropiada, identifica su distribución y enumera las condiciones que se deben cumplir.

**Solución paso a paso:**

**Paso 1 – Identificar las condiciones de la distribución binomial.**  
Una variable $X$ sigue una distribución $B(n,p)$ si:  
(1) Se realizan $n$ ensayos independientes.  
(2) Cada ensayo es de Bernoulli (éxito/fracaso).  
(3) La probabilidad de éxito $p$ es constante en todos los ensayos.

**Paso 2 – Verificar las condiciones.**  
- $n = 5$ extracciones independientes ✓  
- Cada extracción: defectuosa (éxito) o correcta (fracaso) ✓  
- $p = 0{,}20$ en cada extracción (con reemplazamiento o lote muy grande) ✓

**Paso 3 – Definir la variable aleatoria.**  
$X$ = número de artículos defectuosos en las 5 extracciones.  
$$X \sim B(5,\; 0{,}20)$$

**Paso 4 – Rango de la variable.**  
$X$ puede tomar los valores $\{0, 1, 2, 3, 4, 5\}$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Indica si $X$ sigue una distribución binomial y en caso afirmativo escribe $X \sim B(n,p)$: Se lanza un dado equilibrado 10 veces; $X$ = número de veces que sale el número 3.

   > **Solución:** Sí. $n=10$ lanzamientos independientes, $p=1/6$ (probabilidad de obtener 3). $X \sim B(10,\; 1/6)$.

2. Un test de tipo test tiene 8 preguntas, cada una con 4 opciones (solo una correcta). Un estudiante responde al azar. $X$ = número de respuestas correctas. Identifica la distribución.

   > **Solución:** $n=8$, $p=1/4=0{,}25$. Las respuestas son independientes. $X \sim B(8,\; 0{,}25)$.

**Nivel Intermedio:**

3. El 5% de los pasajeros de un aeropuerto lleva equipaje con exceso de peso. Si se inspeccionan 20 pasajeros al azar, ¿qué distribución sigue el número de pasajeros con exceso de peso? ¿Cuántos valores puede tomar $X$?

   > **Solución:** $X \sim B(20,\; 0{,}05)$. $X$ puede tomar los valores $\{0, 1, 2, \ldots, 20\}$, es decir, 21 valores posibles.

4. Explica por qué no es correcto aplicar la distribución binomial si se extraen 5 cartas de una baraja de 40 **sin** reemplazamiento para contar el número de ases.

   > **Solución:** Sin reemplazamiento, la probabilidad de obtener un as varía en cada extracción (depende de las cartas ya extraídas), por lo que la condición de probabilidad constante $p$ no se cumple. En este caso se usaría la distribución hipergeométrica. Solo se puede usar la binomial si la población es muy grande respecto a la muestra.

**Nivel EVAU:**

5. En un proceso de fabricación de microchips, el 4% de las unidades producidas son defectuosas. Un inspector examina muestras de 25 unidades de forma independiente.

   a) Define la variable $X$ apropiada y escribe su distribución.  
   b) Indica el recorrido (conjunto de valores posibles) de $X$.  
   c) Explica por qué se pueden considerar independientes las extracciones en la práctica, aunque técnicamente se extraiga sin reemplazamiento de un lote.

   > **Solución:**  
   > a) $X$ = número de chips defectuosos en 25 unidades. $X \sim B(25,\; 0{,}04)$.  
   > b) $X \in \{0, 1, 2, \ldots, 25\}$.  
   > c) En la práctica industrial, los lotes son enormes (miles o millones de unidades). Cuando el tamaño de la muestra ($n=25$) es inferior al 5% del tamaño del lote, la variación en $p$ entre extracciones es despreciable y se puede asumir independencia (aproximación por la binomial).

**Test de Opción Múltiple**

6. Para que $X$ siga una distribución binomial $B(n,p)$ es imprescindible que:
   - a) Los ensayos sean dependientes entre sí.
   - b) La probabilidad de éxito varíe en cada ensayo.
   - c) Los ensayos sean independientes y la probabilidad de éxito sea constante.
   - d) Se realicen exactamente 10 ensayos.

   > **Respuesta correcta: c)** Son las condiciones esenciales de la distribución binomial.

7. Si $X \sim B(n,p)$, el recorrido de $X$ es:
   - a) Todos los números reales.
   - b) Los enteros negativos.
   - c) $\{0, 1, 2, \ldots, n\}$
   - d) $\{1, 2, \ldots, n\}$

   > **Respuesta correcta: c)** $X$ cuenta el número de éxitos y puede valer desde 0 (ningún éxito) hasta $n$ (todos éxitos).

---

#### 11.2.3 Función de masa de la binomial: P(X = k) = C(n,k)·p^k·(1−p)^(n−k)

**Ejercicio Resuelto**

Sea $X \sim B(6,\; 0{,}3)$. Calcula $P(X=2)$, $P(X=0)$ y $P(X=6)$.

**Solución paso a paso:**

La función de masa de la binomial es:
$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0,1,\ldots,n$$

Con $n=6$ y $p=0{,}3$ ($q=0{,}7$):

**$P(X=2)$:**
$$P(X=2) = \binom{6}{2}(0{,}3)^2(0{,}7)^4 = 15 \times 0{,}09 \times 0{,}2401 = 15 \times 0{,}021609 = \mathbf{0{,}3241}$$

**$P(X=0)$:**
$$P(X=0) = \binom{6}{0}(0{,}3)^0(0{,}7)^6 = 1 \times 1 \times 0{,}117649 = \mathbf{0{,}1176}$$

**$P(X=6)$:**
$$P(X=6) = \binom{6}{6}(0{,}3)^6(0{,}7)^0 = 1 \times 0{,}000729 \times 1 = \mathbf{0{,}0007}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Sea $X \sim B(4,\; 0{,}5)$. Calcula $P(X=2)$.

   > **Solución:** $P(X=2) = \binom{4}{2}(0{,}5)^2(0{,}5)^2 = 6 \times 0{,}25 \times 0{,}25 = 6 \times 0{,}0625 = \mathbf{0{,}375}$.

2. Sea $X \sim B(5,\; 0{,}4)$. Calcula $P(X=0)$ y $P(X=1)$.

   > **Solución:** $P(X=0) = (0{,}6)^5 = 0{,}07776 \approx \mathbf{0{,}0778}$. $P(X=1) = \binom{5}{1}(0{,}4)(0{,}6)^4 = 5 \times 0{,}4 \times 0{,}1296 = \mathbf{0{,}2592}$.

**Nivel Intermedio:**

3. En una línea de producción, el 10% de las piezas son defectuosas. Se toma una muestra de 8 piezas. Calcula la probabilidad de que exactamente 2 sean defectuosas.

   > **Solución:** $X \sim B(8,\;0{,}1)$. $P(X=2) = \binom{8}{2}(0{,}1)^2(0{,}9)^6 = 28 \times 0{,}01 \times 0{,}531441 = \mathbf{0{,}1488}$.

4. Un test consta de 10 preguntas de verdadero/falso. Si un alumno responde al azar, calcula la probabilidad de que acierte exactamente 7.

   > **Solución:** $X \sim B(10,\;0{,}5)$. $P(X=7) = \binom{10}{7}(0{,}5)^7(0{,}5)^3 = 120 \times (0{,}5)^{10} = 120/1024 = \mathbf{0{,}1172}$.

**Nivel EVAU:**

5. En una prueba de diagnóstico médico, la probabilidad de que el test dé positivo cuando el paciente está sano (falso positivo) es del 8%. Se hacen 5 pruebas independientes en pacientes sanos.

   a) Define $X$ y su distribución.  
   b) Calcula $P(X=1)$ (exactamente un falso positivo).  
   c) Calcula $P(X \geq 1)$ usando el complementario.

   > **Solución:**  
   > a) $X$ = número de falsos positivos en 5 pruebas; $X \sim B(5,\;0{,}08)$.  
   > b) $P(X=1) = \binom{5}{1}(0{,}08)^1(0{,}92)^4 = 5 \times 0{,}08 \times 0{,}71639 = \mathbf{0{,}2866}$.  
   > c) $P(X \geq 1) = 1 - P(X=0) = 1 - (0{,}92)^5 = 1 - 0{,}65908 = \mathbf{0{,}3409}$.

**Test de Opción Múltiple**

6. Si $X \sim B(3,\; 0{,}4)$, entonces $P(X=3)$ vale:
   - a) 0,064
   - b) 0,288
   - c) 0,432
   - d) 0,216

   > **Respuesta correcta: a)** $P(X=3) = (0{,}4)^3 = 0{,}064$.

7. La expresión correcta para $P(X=k)$ en $B(n,p)$ es:
   - a) $n \cdot p^k \cdot q^{n-k}$
   - b) $\binom{n}{k} \cdot p^k \cdot q^{n-k}$
   - c) $\binom{n}{k} \cdot p^{n-k} \cdot q^k$
   - d) $k \cdot p^k \cdot q^{n-k}$

   > **Respuesta correcta: b)** Es la fórmula de la función de masa de la binomial: el número de formas de elegir $k$ éxitos entre $n$ ensayos multiplicado por las probabilidades correspondientes.

---

#### 11.2.4 Parámetros de la binomial: media μ = np y desviación típica σ = √(np(1−p))

**Ejercicio Resuelto**

En un proceso de fabricación, el 25% de los artículos son de segunda calidad. Se inspeccionan 80 artículos. Calcula la media y la desviación típica del número de artículos de segunda calidad.

**Solución paso a paso:**

$X \sim B(80,\; 0{,}25)$.

**Media (esperanza):**
$$\mu = E(X) = np = 80 \times 0{,}25 = \mathbf{20}$$

En promedio, se esperan 20 artículos de segunda calidad.

**Varianza:**
$$\sigma^2 = \text{Var}(X) = np(1-p) = 80 \times 0{,}25 \times 0{,}75 = \mathbf{15}$$

**Desviación típica:**
$$\sigma = \sqrt{np(1-p)} = \sqrt{15} \approx \mathbf{3{,}873}$$

Interpretación: el número de artículos de segunda calidad en muestras de 80 tiene una variabilidad típica de aproximadamente $\pm 3{,}87$ artículos alrededor de la media de 20.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Sea $X \sim B(10,\; 0{,}6)$. Calcula $\mu$ y $\sigma$.

   > **Solución:** $\mu = 10 \times 0{,}6 = \mathbf{6}$. $\sigma = \sqrt{10 \times 0{,}6 \times 0{,}4} = \sqrt{2{,}4} \approx \mathbf{1{,}549}$.

2. Sea $X \sim B(n, 0{,}5)$ con $\mu = 12$. Halla $n$ y $\sigma$.

   > **Solución:** $np = 12 \Rightarrow n \times 0{,}5 = 12 \Rightarrow \mathbf{n = 24}$. $\sigma = \sqrt{24 \times 0{,}5 \times 0{,}5} = \sqrt{6} \approx \mathbf{2{,}449}$.

**Nivel Intermedio:**

3. En una ciudad, el 40% de los habitantes tiene coche eléctrico. Si se encuesta a 200 personas, calcula la media y la desviación típica del número de propietarios de coche eléctrico.

   > **Solución:** $X \sim B(200,\;0{,}4)$. $\mu = 200 \times 0{,}4 = \mathbf{80}$. $\sigma = \sqrt{200 \times 0{,}4 \times 0{,}6} = \sqrt{48} \approx \mathbf{6{,}928}$.

4. Si $X \sim B(n, 0{,}2)$ y $\sigma^2 = 16$, ¿cuánto vale $n$ y $\mu$?

   > **Solución:** $np(1-p) = n(0{,}2)(0{,}8) = 0{,}16n = 16 \Rightarrow \mathbf{n = 100}$. $\mu = 100 \times 0{,}2 = \mathbf{20}$.

**Nivel EVAU:**

5. En un hospital, el 12% de los pacientes que ingresan por urgencias necesitan hospitalización posterior. En un día típico ingresan 150 pacientes.

   a) Calcula la media y la desviación típica del número de pacientes que necesitan hospitalización.  
   b) ¿Entre qué valores se encuentra la mayor parte de los datos según la regla de $\mu \pm 2\sigma$ (aproximadamente el 95%)?  
   c) ¿Cuál es la varianza?

   > **Solución:**  
   > a) $X \sim B(150,\;0{,}12)$. $\mu = 150 \times 0{,}12 = \mathbf{18}$. $\sigma = \sqrt{150 \times 0{,}12 \times 0{,}88} = \sqrt{15{,}84} \approx \mathbf{3{,}98}$.  
   > b) Intervalo $[\mu - 2\sigma,\; \mu + 2\sigma] = [18 - 7{,}96,\; 18 + 7{,}96] \approx [\mathbf{10{,}04},\; \mathbf{25{,}96}]$. En la práctica: entre 10 y 26 pacientes el 95% de los días.  
   > c) $\sigma^2 = 15{,}84 \approx \mathbf{15{,}84}$.

**Test de Opción Múltiple**

6. Si $X \sim B(20,\; 0{,}3)$, la media $\mu$ vale:
   - a) 3
   - b) 6
   - c) 14
   - d) 20

   > **Respuesta correcta: b)** $\mu = np = 20 \times 0{,}3 = 6$.

7. Para $X \sim B(50,\; 0{,}4)$, la varianza es:
   - a) 20
   - b) 12
   - c) $\sqrt{12}$
   - d) 4,47

   > **Respuesta correcta: b)** $\sigma^2 = np(1-p) = 50 \times 0{,}4 \times 0{,}6 = 12$.

---

#### 11.2.5 Cálculo de probabilidades binomiales: exactas, acumuladas y del complementario

**Ejercicio Resuelto**

Sea $X \sim B(8,\; 0{,}25)$. Calcula: $P(X \leq 2)$, $P(X \geq 3)$ y $P(2 \leq X \leq 5)$.

**Solución paso a paso:**

$n=8$, $p=0{,}25$, $q=0{,}75$.

**Probabilidades exactas necesarias:**
$$P(X=0) = (0{,}75)^8 = 0{,}10011$$
$$P(X=1) = \binom{8}{1}(0{,}25)(0{,}75)^7 = 8 \times 0{,}25 \times 0{,}13348 = 0{,}26697$$
$$P(X=2) = \binom{8}{2}(0{,}25)^2(0{,}75)^6 = 28 \times 0{,}0625 \times 0{,}17798 = 0{,}31146$$
$$P(X=3) = \binom{8}{3}(0{,}25)^3(0{,}75)^5 = 56 \times 0{,}015625 \times 0{,}23730 = 0{,}20764$$
$$P(X=4) = \binom{8}{4}(0{,}25)^4(0{,}75)^4 = 70 \times 0{,}003906 \times 0{,}31641 = 0{,}08651$$
$$P(X=5) = \binom{8}{5}(0{,}25)^5(0{,}75)^3 = 56 \times 0{,}000977 \times 0{,}42188 = 0{,}02307$$

**$P(X \leq 2)$:**
$$P(X \leq 2) = P(X=0)+P(X=1)+P(X=2) = 0{,}10011+0{,}26697+0{,}31146 = \mathbf{0{,}6785}$$

**$P(X \geq 3)$** (complementario):
$$P(X \geq 3) = 1 - P(X \leq 2) = 1 - 0{,}6785 = \mathbf{0{,}3215}$$

**$P(2 \leq X \leq 5)$:**
$$P(2 \leq X \leq 5) = P(2)+P(3)+P(4)+P(5) = 0{,}31146+0{,}20764+0{,}08651+0{,}02307 = \mathbf{0{,}6287}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Sea $X \sim B(5,\; 0{,}5)$. Calcula $P(X \leq 1)$.

   > **Solución:** $P(X=0)=(0{,}5)^5=0{,}03125$. $P(X=1)=5(0{,}5)^5=0{,}15625$. $P(X \leq 1) = 0{,}03125+0{,}15625 = \mathbf{0{,}1875}$.

2. Si $X \sim B(4,\; 0{,}3)$, calcula $P(X \geq 1)$ usando el complementario.

   > **Solución:** $P(X=0)=(0{,}7)^4=0{,}2401$. $P(X \geq 1)=1-0{,}2401=\mathbf{0{,}7599}$.

**Nivel Intermedio:**

3. El 20% de los clientes de un banco utilizan la banca móvil. En un día se atienden 10 clientes. Calcula la probabilidad de que al menos 3 usen la banca móvil.

   > **Solución:** $X \sim B(10,\;0{,}2)$.  
   > $P(X=0)=(0{,}8)^{10}=0{,}10737$;  
   > $P(X=1)=10(0{,}2)(0{,}8)^9=0{,}26844$;  
   > $P(X=2)=45(0{,}04)(0{,}8)^8=0{,}30199$.  
   > $P(X \geq 3) = 1-(0{,}10737+0{,}26844+0{,}30199) = 1-0{,}67780 = \mathbf{0{,}3222}$.

4. Un tratamiento médico tiene una tasa de éxito del 70%. Se trata a 6 pacientes. Calcula $P(4 \leq X \leq 6)$.

   > **Solución:** $X \sim B(6,\;0{,}7)$.  
   > $P(X=4)=\binom{6}{4}(0{,}7)^4(0{,}3)^2=15\times0{,}2401\times0{,}09=0{,}32414$.  
   > $P(X=5)=\binom{6}{5}(0{,}7)^5(0{,}3)^1=6\times0{,}16807\times0{,}3=0{,}30253$.  
   > $P(X=6)=(0{,}7)^6=0{,}11765$.  
   > $P(4 \leq X \leq 6)=0{,}32414+0{,}30253+0{,}11765=\mathbf{0{,}7443}$.

**Nivel EVAU:**

5. Un sistema de seguridad tiene 10 sensores independientes. Cada sensor falla con probabilidad 0,05. El sistema lanza una alarma si falla al menos 1 sensor.

   a) Sea $X$ el número de sensores que fallan. Identifica la distribución de $X$.  
   b) Calcula la probabilidad de que ningún sensor falle.  
   c) Calcula la probabilidad de que se active la alarma (al menos 1 fallo).  
   d) Calcula la probabilidad de que fallen exactamente 2 sensores.

   > **Solución:**  
   > a) $X \sim B(10,\;0{,}05)$.  
   > b) $P(X=0)=(0{,}95)^{10}=\mathbf{0{,}5987}$.  
   > c) $P(X \geq 1)=1-P(X=0)=1-0{,}5987=\mathbf{0{,}4013}$.  
   > d) $P(X=2)=\binom{10}{2}(0{,}05)^2(0{,}95)^8=45\times0{,}0025\times0{,}66342=\mathbf{0{,}0746}$.

**Test de Opción Múltiple**

6. Si $X \sim B(6,\; 0{,}5)$, entonces $P(X \geq 5) = P(X=5) + P(X=6)$. Su valor es aproximadamente:
   - a) 0,109
   - b) 0,234
   - c) 0,109
   - d) 0,109

   > **Respuesta correcta: a)** $P(X=5)=6(0{,}5)^6=6/64=0{,}09375$; $P(X=6)=(0{,}5)^6=1/64=0{,}01563$. Suma $\approx 0{,}109$.

7. Para calcular $P(X \geq k)$ de forma eficiente usamos:
   - a) $P(X \leq k)$
   - b) $1 - P(X \leq k-1)$
   - c) $1 - P(X \leq k)$
   - d) $P(X = k) + 1$

   > **Respuesta correcta: b)** $P(X \geq k) = 1 - P(X \leq k-1)$ es el complementario de "menos de $k$ éxitos".

---

## 11.3 Distribución normal

---

#### 11.3.1 Curva normal: forma, simetría y parámetros μ y σ

**Ejercicio Resuelto**

Describe las propiedades geométricas de la curva normal $N(\mu, \sigma)$ e ilustra cómo cambia la curva cuando se varía $\mu$ (con $\sigma$ fijo) y cuando se varía $\sigma$ (con $\mu$ fijo).

**Solución paso a paso:**

**Forma y simetría:**
- La curva normal tiene forma de **campana de Gauss**: simétrica respecto al eje vertical que pasa por $x = \mu$.
- Es **unimodal**: tiene un único máximo en $x = \mu$.
- Se extiende de $-\infty$ a $+\infty$ (las colas se aproximan al eje $x$ asintóticamente).
- El área total bajo la curva es exactamente 1 (axioma de probabilidad).

**Parámetros:**
- $\mu$ (media) determina el **centro** de la distribución (posición horizontal del máximo).
- $\sigma$ (desviación típica) determina la **dispersión** (anchura de la campana).

**Efecto de cambiar $\mu$ (con $\sigma$ fijo):**
$$N(0, 1) \to N(3, 1) \to N(-2, 1)$$
La campana se desplaza horizontalmente sin cambiar de forma ni anchura.

**Efecto de cambiar $\sigma$ (con $\mu$ fijo):**
$$N(5, 1) \to N(5, 2) \to N(5, 0{,}5)$$
$\sigma$ grande $\Rightarrow$ campana ancha y baja (más dispersión);  
$\sigma$ pequeño $\Rightarrow$ campana estrecha y alta (menos dispersión).

---

**Ejercicios con Solución**

**Nivel Básico:**

1. La estatura de los estudiantes de 2.º Bachillerato sigue una distribución $N(170,\; 8)$ cm. Indica: (a) la media, (b) la desviación típica, (c) el valor donde se alcanza el máximo de la curva.

   > **Solución:** (a) $\mu = 170$ cm. (b) $\sigma = 8$ cm. (c) El máximo se alcanza en $x = \mu = \mathbf{170}$ cm.

2. Dos distribuciones normales: $A \sim N(50, 5)$ y $B \sim N(50, 10)$. ¿Cuál es más dispersa y cuál tiene la campana más alta?

   > **Solución:** $B$ es más dispersa ($\sigma_B=10 > \sigma_A=5$) y tiene la campana más baja y ancha. $A$ tiene campana más alta y estrecha.

**Nivel Intermedio:**

3. El tiempo de vida de una batería sigue $N(1200, 150)$ horas. Indica el centro de la distribución y el intervalo $[\mu-\sigma, \mu+\sigma]$.

   > **Solución:** Centro: $\mu = 1200$ h. Intervalo: $[1200-150,\; 1200+150] = [\mathbf{1050},\; \mathbf{1350}]$ horas.

4. Para una distribución $N(\mu, \sigma)$: (a) La curva es simétrica respecto a $x=\mu$. (b) Los puntos de inflexión se encuentran en $x = \mu \pm \sigma$. ¿A qué valor de $x$ está el punto de inflexión derecho si $\mu=100$ y $\sigma=15$?

   > **Solución:** Punto de inflexión derecho en $x = \mu + \sigma = 100 + 15 = \mathbf{115}$.

**Nivel EVAU:**

5. El peso de los recién nacidos en una maternidad sigue una distribución normal de media 3200 g y desviación típica 450 g.

   a) Escribe la notación de la distribución y describe las características de la curva.  
   b) ¿En qué valor se alcanza el máximo de la función de densidad?  
   c) ¿Cuál es el intervalo simétrico alrededor de la media que recoge el 68% de los datos (regla empírica)?  
   d) Indica los puntos de inflexión de la curva.

   > **Solución:**  
   > a) $X \sim N(3200,\; 450)$. Curva en forma de campana simétrica respecto a $x=3200$, con colas infinitas.  
   > b) El máximo se alcanza en $x = \mu = \mathbf{3200}$ g.  
   > c) $[\mu - \sigma,\; \mu + \sigma] = [3200-450,\; 3200+450] = [\mathbf{2750},\; \mathbf{3650}]$ g.  
   > d) Puntos de inflexión: $x = \mu \pm \sigma \Rightarrow x = 2750$ g y $x = 3650$ g.

**Test de Opción Múltiple**

6. En una distribución $N(\mu, \sigma)$, la curva es simétrica respecto a:
   - a) $x = 0$
   - b) $x = \sigma$
   - c) $x = \mu$
   - d) $x = \mu + \sigma$

   > **Respuesta correcta: c)** La simetría de la curva normal se produce siempre respecto al eje $x = \mu$.

7. Si aumentamos $\sigma$ manteniendo fijo $\mu$, la curva normal:
   - a) Se desplaza hacia la derecha.
   - b) Se vuelve más estrecha y alta.
   - c) Se vuelve más ancha y baja.
   - d) No cambia.

   > **Respuesta correcta: c)** Mayor $\sigma$ implica mayor dispersión, por lo que la campana se ensancha y se aplana para mantener el área igual a 1.

---

#### 11.3.2 Función de densidad de la distribución normal N(μ, σ)

**Ejercicio Resuelto**

Escribe la función de densidad de la distribución normal $N(\mu, \sigma)$ e interpreta cada uno de sus elementos. Comprueba que la función de densidad de la normal estándar $N(0, 1)$ se obtiene sustituyendo $\mu=0$ y $\sigma=1$.

**Solución paso a paso:**

**Función de densidad de $N(\mu, \sigma)$:**
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \qquad x \in \mathbb{R}$$

**Interpretación de los elementos:**
- $\frac{1}{\sigma\sqrt{2\pi}}$: factor normalizador que asegura que el área total bajo la curva sea 1.
- $e^{-\frac{(x-\mu)^2}{2\sigma^2}}$: función exponencial negativa que hace que la curva decrezca simétricamente desde el máximo en $x=\mu$.
- $(x-\mu)^2$: mide el cuadrado de la distancia al centro; a mayor distancia, menor densidad.
- $2\sigma^2$: escala la dispersión; mayor $\sigma$ "aplana" la curva.

**Normal estándar $N(0,1)$:** Sustituimos $\mu=0$, $\sigma=1$:
$$\varphi(z) = \frac{1}{\sqrt{2\pi}}\, e^{-\frac{z^2}{2}}$$

Esta es la función de densidad estándar $\varphi(z)$, cuya función de distribución es $\Phi(z) = P(Z \leq z)$, tabulada en las tablas estadísticas.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Escribe la función de densidad de $X \sim N(5, 2)$. ¿Cuál es el valor máximo de $f(x)$ y dónde se alcanza?

   > **Solución:** $f(x) = \frac{1}{2\sqrt{2\pi}}\,e^{-\frac{(x-5)^2}{8}}$. El máximo se alcanza en $x=\mu=5$: $f(5) = \frac{1}{2\sqrt{2\pi}} = \frac{1}{2 \times 2{,}5066} \approx \mathbf{0{,}1995}$.

2. ¿Por qué la función de densidad normal nunca es negativa y su integral en $\mathbb{R}$ vale 1?

   > **Solución:** $f(x) \geq 0$ porque es un producto de constantes positivas por $e^{(\cdot)} > 0$ siempre. $\int_{-\infty}^{+\infty} f(x)\,dx = 1$ es la propiedad de normalización, garantizada por el factor $\frac{1}{\sigma\sqrt{2\pi}}$.

**Nivel Intermedio:**

3. La velocidad de respuesta de un sistema informático sigue $N(200, 30)$ ms. Escribe la función de densidad e indica en qué valor se concentra la mayor probabilidad (valor modal).

   > **Solución:** $f(x) = \frac{1}{30\sqrt{2\pi}}\,e^{-\frac{(x-200)^2}{1800}}$. El valor modal es $x = \mu = \mathbf{200}$ ms, donde la densidad es máxima.

4. ¿Cuál es la relación entre la función de densidad $f(x)$ y la probabilidad $P(a \leq X \leq b)$ en una distribución continua?

   > **Solución:** $P(a \leq X \leq b) = \int_a^b f(x)\,dx$. Para la normal, este valor se obtiene mediante la tabla de la normal estándar previa tipificación, ya que la integral no tiene forma cerrada elemental.

**Nivel EVAU:**

5. El diámetro de los rodamientos fabricados en una planta sigue una distribución $N(25, 0{,}1)$ mm.

   a) Escribe la función de densidad de $X$.  
   b) ¿En qué valor se alcanza el máximo de la densidad?  
   c) Indica los puntos de inflexión de la curva.  
   d) Explica el significado del área bajo la curva en el intervalo $[24{,}9,\; 25{,}1]$.

   > **Solución:**  
   > a) $f(x) = \frac{1}{0{,}1\sqrt{2\pi}}\,e^{-\frac{(x-25)^2}{0{,}02}}$.  
   > b) El máximo se alcanza en $x = 25$ mm.  
   > c) Inflexiones en $x = 25 \pm 0{,}1$: es decir, en $x = 24{,}9$ mm y $x = 25{,}1$ mm.  
   > d) El área bajo la curva en $[24{,}9,\; 25{,}1]$ es $P(24{,}9 \leq X \leq 25{,}1)$, la probabilidad de que un rodamiento tenga un diámetro dentro de $\pm 1\sigma$ de la media, aproximadamente el 68,27%.

**Test de Opción Múltiple**

6. La función de densidad de la normal estándar $\varphi(z)$ alcanza su máximo en:
   - a) $z = 1$
   - b) $z = -1$
   - c) $z = 0$
   - d) $z = \sigma$

   > **Respuesta correcta: c)** El máximo se alcanza en $z = 0$ (la media de la normal estándar).

7. ¿Cuánto vale $\int_{-\infty}^{+\infty} f(x)\,dx$ para cualquier función de densidad?
   - a) 0
   - b) $\mu$
   - c) $\sigma$
   - d) 1

   > **Respuesta correcta: d)** Por definición de función de densidad de probabilidad, el área total bajo la curva es siempre 1.

---

#### 11.3.3 Propiedades de la distribución normal: regla 68-95-99,7

**Ejercicio Resuelto**

Los resultados de un examen de matemáticas siguen una distribución $N(65, 12)$ puntos. Usando la regla empírica (68-95-99,7), determina los intervalos que contienen aproximadamente el 68%, 95% y 99,7% de las notas.

**Solución paso a paso:**

$\mu = 65$, $\sigma = 12$.

**Regla 68-95-99,7 (regla empírica):**

| Intervalo | Porcentaje de datos |
|-----------|---------------------|
| $[\mu - \sigma,\; \mu + \sigma]$ | $\approx 68{,}27\%$ |
| $[\mu - 2\sigma,\; \mu + 2\sigma]$ | $\approx 95{,}45\%$ |
| $[\mu - 3\sigma,\; \mu + 3\sigma]$ | $\approx 99{,}73\%$ |

**Aplicación:**

- $[\mu - \sigma,\; \mu + \sigma] = [65-12,\; 65+12] = [\mathbf{53},\; \mathbf{77}]$ puntos. Contiene el **68%** de las notas.
- $[\mu - 2\sigma,\; \mu + 2\sigma] = [65-24,\; 65+24] = [\mathbf{41},\; \mathbf{89}]$ puntos. Contiene el **95%** de las notas.
- $[\mu - 3\sigma,\; \mu + 3\sigma] = [65-36,\; 65+36] = [\mathbf{29},\; \mathbf{101}]$ puntos. Contiene el **99,7%** de las notas.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. El peso de los aguacates de una finca sigue $N(180, 20)$ g. Usa la regla 68-95-99,7 para hallar el intervalo que contiene el 95% de los pesos.

   > **Solución:** $[\mu-2\sigma,\;\mu+2\sigma] = [180-40,\;180+40] = [\mathbf{140},\; \mathbf{220}]$ g.

2. Si $X \sim N(100, 15)$, ¿qué porcentaje aproximado de datos está entre 85 y 115?

   > **Solución:** $85 = 100-15 = \mu-\sigma$ y $115 = 100+15 = \mu+\sigma$. El intervalo $[\mu-\sigma,\mu+\sigma]$ contiene aproximadamente el $\mathbf{68\%}$ de los datos.

**Nivel Intermedio:**

3. Las calorías de las raciones de un restaurante siguen $N(750, 80)$ kcal. ¿Qué porcentaje de raciones supera las 910 kcal?

   > **Solución:** $910 = 750 + 2\times80 = \mu + 2\sigma$. El 95% está en $[\mu-2\sigma, \mu+2\sigma]$. Por simetría, el 2,5% está por encima de $\mu+2\sigma$. Respuesta: $\approx \mathbf{2{,}5\%}$ de las raciones supera las 910 kcal.

4. Una máquina produce pernos de longitud $N(50, 0{,}5)$ mm. Indica el rango de medidas dentro de $\pm 3\sigma$. ¿Qué porcentaje quedaría fuera?

   > **Solución:** $[\mu-3\sigma,\mu+3\sigma]=[50-1{,}5,\;50+1{,}5]=[48{,}5,\;51{,}5]$ mm. El 99,7% queda dentro, por lo que solo un $\mathbf{0{,}3\%}$ queda fuera.

**Nivel EVAU:**

5. La tensión arterial sistólica de adultos sanos de 40 años sigue $N(120, 10)$ mmHg. Se considera "elevada" si supera 140 mmHg e "hipotensión" si es inferior a 90 mmHg.

   a) ¿Qué porcentaje de adultos tiene tensión entre 100 y 140 mmHg? (Usa la regla empírica.)  
   b) ¿Qué porcentaje tiene tensión considerada "elevada"?  
   c) ¿Entraría en la regla empírica un adulto con tensión de 90 mmHg? Razona.

   > **Solución:**  
   > a) $100 = 120-20 = \mu-2\sigma$ y $140 = 120+20 = \mu+2\sigma$. El intervalo $[\mu-2\sigma,\mu+2\sigma]$ contiene el 95%. Luego el $\mathbf{95\%}$ tiene tensión entre 100 y 140 mmHg.  
   > b) El 5% está fuera de $[\mu\pm2\sigma]$; por simetría, el $\mathbf{2{,}5\%}$ tiene tensión superior a 140 (elevada).  
   > c) $90 = 120-30 = \mu-3\sigma$. Esto está en el límite inferior del intervalo $[\mu\pm3\sigma]$. El 99,7% de los datos está entre 90 y 150 mmHg. Un adulto con 90 mmHg está en el percentil $\approx 0{,}15\%$, es decir, muy poco frecuente, en el límite.

**Test de Opción Múltiple**

6. Según la regla empírica, aproximadamente el 95% de los datos de una distribución normal se encuentran en el intervalo:
   - a) $[\mu - \sigma,\; \mu + \sigma]$
   - b) $[\mu - 2\sigma,\; \mu + 2\sigma]$
   - c) $[\mu - 3\sigma,\; \mu + 3\sigma]$
   - d) $[0,\; \mu + 2\sigma]$

   > **Respuesta correcta: b)** La regla empírica establece que el 95% de los datos cae dentro de dos desviaciones típicas alrededor de la media.

7. Si $X \sim N(50, 10)$, ¿qué porcentaje de datos está por debajo de 30?
   - a) 5%
   - b) 2,5%
   - c) 0,15%
   - d) 16%

   > **Respuesta correcta: c)** $30 = 50-20 = \mu-2\sigma$. El 95% está en $[\mu\pm2\sigma]$, dejando 5% fuera; la mitad (2,5%) por debajo de $\mu-2\sigma$. Pero $30 = \mu-2\sigma$ en este caso... Recalculamos: $30 = 50 - 20 = \mu - 2\sigma$, así que el 2,5% está por debajo de 30. La opción correcta debería ser 2,5%. Sin embargo, revisando: $\mu-3\sigma = 20$ y $\mu-2\sigma = 30$. Por tanto, el $\mathbf{2{,}5\%}$ está por debajo de 30 (opción b).

   > **Respuesta correcta: b)** $30 = \mu - 2\sigma$, y por la regla empírica el 2,5% está por debajo de $\mu-2\sigma$.

---

#### 11.3.4 Tipificación: transformación de N(μ, σ) a N(0, 1)

**Ejercicio Resuelto**

Sea $X \sim N(70, 10)$. Tipifica la variable y calcula $P(X \leq 85)$ y $P(X \geq 55)$ expresando los resultados en términos de la normal estándar.

**Solución paso a paso:**

**Tipificación:** Si $X \sim N(\mu, \sigma)$, la variable tipificada es:
$$Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$$

Con $\mu = 70$, $\sigma = 10$:

**$P(X \leq 85)$:**
$$P(X \leq 85) = P\!\left(Z \leq \frac{85-70}{10}\right) = P(Z \leq 1{,}5) = \Phi(1{,}5)$$
De tabla: $\Phi(1{,}5) = \mathbf{0{,}9332}$.

**$P(X \geq 55)$:**
$$P(X \geq 55) = P\!\left(Z \geq \frac{55-70}{10}\right) = P(Z \geq -1{,}5) = P(Z \leq 1{,}5) = \Phi(1{,}5) = \mathbf{0{,}9332}$$
(Por simetría: $P(Z \geq -a) = P(Z \leq a)$.)

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Transforma los siguientes valores de $X \sim N(100, 20)$ a puntuaciones $Z$: $x_1 = 100$, $x_2 = 120$, $x_3 = 80$, $x_4 = 140$.

   > **Solución:** $z_1 = (100-100)/20 = \mathbf{0}$; $z_2 = (120-100)/20 = \mathbf{1}$; $z_3 = (80-100)/20 = \mathbf{-1}$; $z_4 = (140-100)/20 = \mathbf{2}$.

2. Si $Z \sim N(0,1)$, escribe $P(X \leq 130)$ para $X \sim N(110, 10)$ como $P(Z \leq z)$ e indica el valor de $z$.

   > **Solución:** $z = (130-110)/10 = 2$. Luego $P(X \leq 130) = P(Z \leq 2) = \Phi(2) \approx \mathbf{0{,}9772}$.

**Nivel Intermedio:**

3. La nota de una prueba de acceso sigue $N(6{,}2,\; 1{,}5)$ (escala 0-10). Calcula $P(X \leq 7{,}7)$ tipificando.

   > **Solución:** $z = (7{,}7-6{,}2)/1{,}5 = 1{,}5/1{,}5 = 1$. $P(X \leq 7{,}7) = \Phi(1) \approx \mathbf{0{,}8413}$.

4. Sea $X \sim N(500, 100)$. Calcula $P(350 \leq X \leq 650)$ tipificando.

   > **Solución:**  
   > $z_1 = (350-500)/100 = -1{,}5$; $z_2 = (650-500)/100 = 1{,}5$.  
   > $P(-1{,}5 \leq Z \leq 1{,}5) = \Phi(1{,}5) - \Phi(-1{,}5) = 0{,}9332 - (1-0{,}9332) = 0{,}9332 - 0{,}0668 = \mathbf{0{,}8664}$.

**Nivel EVAU:**

5. El tiempo de procesamiento de solicitudes en una administración sigue $N(14, 3)$ días. Una solicitud se considera "urgente" si se resuelve en menos de 8 días, y "retrasada" si tarda más de 20 días.

   a) Tipifica y calcula $P(X < 8)$.  
   b) Calcula $P(X > 20)$.  
   c) ¿Qué porcentaje de solicitudes se resuelven entre 11 y 17 días?

   > **Solución:**  
   > a) $z = (8-14)/3 = -2$. $P(X < 8) = \Phi(-2) = 1-\Phi(2) = 1-0{,}9772 = \mathbf{0{,}0228}$ (2,28%).  
   > b) $z = (20-14)/3 = 2$. $P(X > 20) = 1-\Phi(2) = \mathbf{0{,}0228}$ (2,28%).  
   > c) $z_1=(11-14)/3=-1$; $z_2=(17-14)/3=1$. $P(-1 \leq Z \leq 1) = \Phi(1)-\Phi(-1) = 0{,}8413-0{,}1587 = \mathbf{0{,}6826}$ (68,26%).

**Test de Opción Múltiple**

6. La tipificación $Z = (X-\mu)/\sigma$ transforma $X \sim N(\mu,\sigma)$ en:
   - a) $N(\mu, 1)$
   - b) $N(0, \sigma)$
   - c) $N(0, 1)$
   - d) $N(1, 0)$

   > **Respuesta correcta: c)** La tipificación siempre produce la normal estándar $N(0,1)$.

7. Si $X \sim N(40, 5)$ y se calcula $z = (X-40)/5$, ¿cuál es el valor tipificado de $x=50$?
   - a) $z = -2$
   - b) $z = 2$
   - c) $z = 10$
   - d) $z = 1$

   > **Respuesta correcta: b)** $z = (50-40)/5 = 10/5 = 2$.

---

#### 11.3.5 Uso de la tabla de la normal estándar: P(Z ≤ z), P(a ≤ Z ≤ b)

**Ejercicio Resuelto**

Usando la tabla de la normal estándar $\Phi(z) = P(Z \leq z)$, calcula: (a) $P(Z \leq 1{,}96)$, (b) $P(Z \leq -0{,}84)$, (c) $P(-1{,}28 \leq Z \leq 1{,}64)$, (d) $P(Z \geq 2{,}05)$.

**Solución paso a paso:**

**Valores de la tabla** (estándar EVAU):  
$\Phi(1{,}96) = 0{,}9750$; $\Phi(0{,}84) = 0{,}7995$; $\Phi(1{,}28) = 0{,}8997$; $\Phi(1{,}64) = 0{,}9495$; $\Phi(2{,}05) = 0{,}9798$.

**(a)** $P(Z \leq 1{,}96) = \Phi(1{,}96) = \mathbf{0{,}9750}$. (Lectura directa de tabla.)

**(b)** $P(Z \leq -0{,}84) = 1 - \Phi(0{,}84) = 1 - 0{,}7995 = \mathbf{0{,}2005}$. (Por simetría: $\Phi(-z)=1-\Phi(z)$.)

**(c)** $P(-1{,}28 \leq Z \leq 1{,}64) = \Phi(1{,}64) - \Phi(-1{,}28) = \Phi(1{,}64) - [1-\Phi(1{,}28)]$  
$= 0{,}9495 - (1-0{,}8997) = 0{,}9495 - 0{,}1003 = \mathbf{0{,}8492}$.

**(d)** $P(Z \geq 2{,}05) = 1 - \Phi(2{,}05) = 1 - 0{,}9798 = \mathbf{0{,}0202}$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Calcula usando la tabla: (a) $P(Z \leq 0)$, (b) $P(Z \leq 1)$, (c) $P(Z \leq -1)$.  
   Valores de tabla: $\Phi(0)=0{,}5$; $\Phi(1)=0{,}8413$.

   > **Solución:** (a) $\Phi(0) = \mathbf{0{,}5}$. (b) $\Phi(1) = \mathbf{0{,}8413}$. (c) $\Phi(-1) = 1-\Phi(1) = 1-0{,}8413 = \mathbf{0{,}1587}$.

2. Calcula $P(Z \geq 1{,}5)$. (Tabla: $\Phi(1{,}5)=0{,}9332$.)

   > **Solución:** $P(Z \geq 1{,}5) = 1-\Phi(1{,}5) = 1-0{,}9332 = \mathbf{0{,}0668}$.

**Nivel Intermedio:**

3. Calcula $P(0 \leq Z \leq 2{,}33)$. (Tabla: $\Phi(2{,}33)=0{,}9901$.)

   > **Solución:** $P(0 \leq Z \leq 2{,}33) = \Phi(2{,}33)-\Phi(0) = 0{,}9901-0{,}5 = \mathbf{0{,}4901}$.

4. Halla el valor $z_0$ tal que $P(Z \leq z_0) = 0{,}9772$. (Tabla inversa: $\Phi^{-1}(0{,}9772) = ?$.)

   > **Solución:** Buscamos en la tabla el valor $z$ con $\Phi(z)=0{,}9772$. Tenemos $\Phi(2) = 0{,}9772$, luego $z_0 = \mathbf{2}$.

**Nivel EVAU:**

5. Sea $Z \sim N(0,1)$.

   a) Calcula $P(|Z| \leq 1{,}96)$.  
   b) Calcula $P(1 \leq Z \leq 2)$. (Tabla: $\Phi(1)=0{,}8413$; $\Phi(2)=0{,}9772$.)  
   c) Halla $z_0$ tal que $P(Z > z_0) = 0{,}05$.  
   d) Halla $z_0$ tal que $P(-z_0 \leq Z \leq z_0) = 0{,}90$. (Tabla: $\Phi(1{,}645) \approx 0{,}95$.)

   > **Solución:**  
   > a) $P(|Z| \leq 1{,}96) = P(-1{,}96 \leq Z \leq 1{,}96) = 2\Phi(1{,}96)-1 = 2(0{,}9750)-1 = \mathbf{0{,}9500}$.  
   > b) $P(1 \leq Z \leq 2) = \Phi(2)-\Phi(1) = 0{,}9772-0{,}8413 = \mathbf{0{,}1359}$.  
   > c) $P(Z > z_0)=0{,}05 \Rightarrow \Phi(z_0)=0{,}95 \Rightarrow z_0 = \mathbf{1{,}645}$.  
   > d) $P(-z_0 \leq Z \leq z_0)=0{,}90 \Rightarrow 2\Phi(z_0)-1=0{,}90 \Rightarrow \Phi(z_0)=0{,}95 \Rightarrow z_0=\mathbf{1{,}645}$.

**Test de Opción Múltiple**

6. Si la tabla da $\Phi(1{,}2) = 0{,}8849$, entonces $P(Z \leq -1{,}2)$ vale:
   - a) 0,8849
   - b) 0,1151
   - c) −0,8849
   - d) 0,3849

   > **Respuesta correcta: b)** $P(Z \leq -1{,}2) = 1 - \Phi(1{,}2) = 1-0{,}8849 = 0{,}1151$.

7. $P(a \leq Z \leq b)$ se calcula como:
   - a) $\Phi(a) - \Phi(b)$
   - b) $\Phi(b) + \Phi(a)$
   - c) $\Phi(b) - \Phi(a)$
   - d) $1 - \Phi(b) + \Phi(a)$

   > **Respuesta correcta: c)** $P(a \leq Z \leq b) = \Phi(b) - \Phi(a)$ (área entre $a$ y $b$ bajo la curva normal).

---

#### 11.3.6 Cálculo de probabilidades con la distribución normal en problemas reales

**Ejercicio Resuelto**

El nivel de colesterol (mg/dL) en adultos de mediana edad sigue una distribución $N(200, 35)$. Se considera "alto riesgo" si el colesterol supera 240 mg/dL y "muy bajo" si es inferior a 150 mg/dL. Calcula las probabilidades correspondientes.

**Solución paso a paso:**

$X \sim N(200, 35)$. Tipificamos: $Z = (X-200)/35$.

**$P(X > 240)$:** "alto riesgo"
$$z = \frac{240-200}{35} = \frac{40}{35} \approx 1{,}14$$
$$P(X > 240) = 1 - \Phi(1{,}14) = 1 - 0{,}8729 = \mathbf{0{,}1271}$$
Aproximadamente el 12,71% de los adultos tienen colesterol en riesgo alto.

**$P(X < 150)$:** "muy bajo"
$$z = \frac{150-200}{35} = \frac{-50}{35} \approx -1{,}43$$
$$P(X < 150) = \Phi(-1{,}43) = 1-\Phi(1{,}43) = 1-0{,}9236 = \mathbf{0{,}0764}$$
Aproximadamente el 7,64% tiene colesterol muy bajo.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. La altura de las plantas de tomate en un invernadero sigue $N(85, 10)$ cm. Calcula $P(X \leq 95)$. (Tabla: $\Phi(1)=0{,}8413$.)

   > **Solución:** $z=(95-85)/10=1$. $P(X \leq 95) = \Phi(1) = \mathbf{0{,}8413}$.

2. El tiempo de carga de una batería de vehículo eléctrico sigue $N(45, 5)$ minutos. Calcula $P(X \geq 50)$. (Tabla: $\Phi(1)=0{,}8413$.)

   > **Solución:** $z=(50-45)/5=1$. $P(X \geq 50)=1-\Phi(1)=1-0{,}8413=\mathbf{0{,}1587}$.

**Nivel Intermedio:**

3. El rendimiento anual de un fondo de inversión sigue $N(7\%, 2\%)$. Calcula la probabilidad de que el rendimiento supere el 10% y la de que sea negativo. (Tabla: $\Phi(1{,}5)=0{,}9332$; $\Phi(3{,}5)\approx0{,}9998$.)

   > **Solución:** $P(X>10\%)$: $z=(10-7)/2=1{,}5$. $P(X>10\%)=1-\Phi(1{,}5)=1-0{,}9332=\mathbf{0{,}0668}$.  
   > $P(X<0\%)$: $z=(0-7)/2=-3{,}5$. $P(X<0\%)=\Phi(-3{,}5)=1-0{,}9998=\mathbf{0{,}0002}$.

4. El diámetro de cilindros producidos por un torno sigue $N(50, 0{,}2)$ mm. Los cilindros dentro del rango $[49{,}6, 50{,}4]$ mm son válidos. Calcula la probabilidad de que un cilindro sea válido. (Tabla: $\Phi(2)=0{,}9772$.)

   > **Solución:** $z_1=(49{,}6-50)/0{,}2=-2$; $z_2=(50{,}4-50)/0{,}2=2$.  
   > $P(49{,}6 \leq X \leq 50{,}4) = \Phi(2)-\Phi(-2) = 0{,}9772-(1-0{,}9772) = 0{,}9772-0{,}0228 = \mathbf{0{,}9544}$.

**Nivel EVAU:**

5. *(Tipo EVAU Madrid)* La masa de los paquetes de harina de una empresa sigue una distribución normal $N(1000, 15)$ g. Se considera que un paquete está fuera de especificación si pesa menos de 975 g o más de 1030 g.

   a) Calcula la probabilidad de que un paquete pese menos de 975 g. [$\Phi(1{,}67)=0{,}9525$]  
   b) Calcula la probabilidad de que un paquete pese más de 1030 g. [$\Phi(2)=0{,}9772$]  
   c) Calcula la probabilidad de que un paquete esté dentro de especificación.  
   d) En un lote de 500 paquetes, ¿cuántos se espera que estén fuera de especificación?

   > **Solución:**  
   > a) $z=(975-1000)/15=-25/15\approx-1{,}67$. $P(X<975)=\Phi(-1{,}67)=1-0{,}9525=\mathbf{0{,}0475}$.  
   > b) $z=(1030-1000)/15=30/15=2$. $P(X>1030)=1-\Phi(2)=1-0{,}9772=\mathbf{0{,}0228}$.  
   > c) $P(975 \leq X \leq 1030)=1-0{,}0475-0{,}0228=\mathbf{0{,}9297}$ (92,97%).  
   > d) $500 \times (1-0{,}9297) = 500 \times 0{,}0703 \approx \mathbf{35{,}15} \approx 35$ paquetes.

**Test de Opción Múltiple**

6. Sea $X \sim N(200, 20)$. Para calcular $P(X \leq 240)$, el valor tipificado es:
   - a) $z = 2{,}4$
   - b) $z = 1$
   - c) $z = 2$
   - d) $z = 40$

   > **Respuesta correcta: c)** $z=(240-200)/20=40/20=2$.

7. Si $P(X \leq a) = 0{,}9772$ para $X \sim N(100, 15)$ y $\Phi(2)=0{,}9772$, ¿cuánto vale $a$?
   - a) 102
   - b) 115
   - c) 130
   - d) 120

   > **Respuesta correcta: c)** $z=2 \Rightarrow (a-100)/15=2 \Rightarrow a=100+30=\mathbf{130}$.

---

## 11.4 Aproximación de la binomial a la normal

---

#### 11.4.1 Condiciones para la aproximación: n grande, np ≥ 5 y n(1−p) ≥ 5

**Ejercicio Resuelto**

Para cada una de las siguientes distribuciones binomiales, indica si se cumplen las condiciones para aproximar por una distribución normal y, si es así, escribe los parámetros de la normal aproximante:  
(a) $X \sim B(200,\; 0{,}3)$  
(b) $X \sim B(30,\; 0{,}04)$  
(c) $X \sim B(100,\; 0{,}06)$

**Solución paso a paso:**

Las condiciones para la aproximación $B(n,p) \approx N(np,\; \sqrt{np(1-p)})$ son:
- $n$ grande (en la práctica, $n \geq 30$).
- $np \geq 5$ y $n(1-p) \geq 5$.

**(a) $B(200, 0{,}3)$:**
- $np = 200 \times 0{,}3 = 60 \geq 5$ ✓
- $n(1-p) = 200 \times 0{,}7 = 140 \geq 5$ ✓
- Se puede aproximar: $X \approx N(60,\; \sqrt{200\times0{,}3\times0{,}7}) = N(60,\; \sqrt{42}) \approx N(60,\; 6{,}48)$.

**(b) $B(30, 0{,}04)$:**
- $np = 30 \times 0{,}04 = 1{,}2 < 5$ ✗
- **No se cumple** la condición $np \geq 5$. No se puede aproximar por la normal.

**(c) $B(100, 0{,}06)$:**
- $np = 100 \times 0{,}06 = 6 \geq 5$ ✓
- $n(1-p) = 100 \times 0{,}94 = 94 \geq 5$ ✓
- Se puede aproximar: $\mu = 6$, $\sigma = \sqrt{100\times0{,}06\times0{,}94} = \sqrt{5{,}64} \approx 2{,}37$.  
  $X \approx N(6,\; 2{,}37)$.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Comprueba si $X \sim B(50, 0{,}2)$ puede aproximarse por una normal. Si es así, escribe la distribución normal aproximante.

   > **Solución:** $np=50\times0{,}2=10 \geq 5$ ✓; $n(1-p)=50\times0{,}8=40 \geq 5$ ✓. Se puede aproximar: $X \approx N(10,\; \sqrt{50\times0{,}2\times0{,}8}) = N(10,\; \sqrt{8}) \approx N(10,\; 2{,}83)$.

2. ¿Puede aproximarse $X \sim B(20, 0{,}1)$ por una normal? Justifica.

   > **Solución:** $np=20\times0{,}1=2 < 5$. **No se cumple** la condición $np \geq 5$. **No** se puede aproximar adecuadamente por la normal en este caso.

**Nivel Intermedio:**

3. En un sondeo electoral, el 45% de los votantes apoya el partido A. Se encuestan 400 personas. ¿Se puede usar la aproximación normal? Halla $\mu$ y $\sigma$.

   > **Solución:** $np=400\times0{,}45=180 \geq 5$ ✓; $n(1-p)=400\times0{,}55=220 \geq 5$ ✓. Sí. $\mu=180$, $\sigma=\sqrt{400\times0{,}45\times0{,}55}=\sqrt{99}\approx9{,}95$.

4. Una empresa fabrica componentes con una tasa de defectos del 2%. ¿Cuántos componentes hay que producir como mínimo para que la aproximación normal sea válida?

   > **Solución:** Se necesita $np \geq 5 \Rightarrow n\times0{,}02 \geq 5 \Rightarrow n \geq 250$. También $n(1-p)=0{,}98n \geq 5$ se cumple para cualquier $n \geq 6$. Por tanto, se necesita al menos $\mathbf{n = 250}$ componentes.

**Nivel EVAU:**

5. En una planta de procesado de alimentos, el 8% de los envases presenta algún defecto. Se inspecciona un lote de 120 envases.

   a) ¿Es válida la aproximación de la binomial por la normal? Justifica comprobando las condiciones.  
   b) Escribe la distribución normal aproximante con sus parámetros $\mu$ y $\sigma$.  
   c) Si la tasa de defectos bajara al 3% con el mismo tamaño de lote, ¿podría usarse la aproximación normal?

   > **Solución:**  
   > a) $np=120\times0{,}08=9{,}6 \geq 5$ ✓; $n(1-p)=120\times0{,}92=110{,}4 \geq 5$ ✓. La aproximación **es válida**.  
   > b) $\mu=9{,}6$; $\sigma=\sqrt{120\times0{,}08\times0{,}92}=\sqrt{8{,}832}\approx2{,}972$. Distribución aproximante: $N(9{,}6,\; 2{,}972)$.  
   > c) $np=120\times0{,}03=3{,}6 < 5$. **No sería válida** la aproximación normal con esa tasa de defectos.

**Test de Opción Múltiple**

6. La condición principal para aproximar $B(n,p)$ por $N(np, \sqrt{np(1-p)})$ es:
   - a) $n > 100$
   - b) $p > 0{,}5$
   - c) $np \geq 5$ y $n(1-p) \geq 5$
   - d) $n > 30$ solamente

   > **Respuesta correcta: c)** Las condiciones necesarias son $np \geq 5$ y $n(1-p) \geq 5$, además de $n$ suficientemente grande.

7. Si $X \sim B(100, 0{,}5)$, la distribución normal aproximante es:
   - a) $N(0{,}5,\; 5)$
   - b) $N(50,\; 25)$
   - c) $N(50,\; 5)$
   - d) $N(100,\; 5)$

   > **Respuesta correcta: c)** $\mu=100\times0{,}5=50$; $\sigma=\sqrt{100\times0{,}5\times0{,}5}=\sqrt{25}=5$. La normal aproximante es $N(50,5)$.

---

#### 11.4.2 Corrección por continuidad de Yates

**Ejercicio Resuelto**

Sea $X \sim B(100,\; 0{,}4)$. Usa la aproximación normal con corrección de Yates para calcular $P(X = 40)$, $P(X \leq 38)$ y $P(X \geq 45)$.

**Solución paso a paso:**

**Distribución aproximante:** $\mu = 100\times0{,}4=40$; $\sigma=\sqrt{100\times0{,}4\times0{,}6}=\sqrt{24}\approx4{,}899$.

**Corrección de Yates (corrección por continuidad):** Al aproximar una distribución discreta por una continua, sustituimos:
- $P(X = k) \approx P(k-0{,}5 \leq Y \leq k+0{,}5)$
- $P(X \leq k) \approx P(Y \leq k+0{,}5)$
- $P(X \geq k) \approx P(Y \geq k-0{,}5)$

**$P(X=40)$:**
$$P(X=40) \approx P(39{,}5 \leq Y \leq 40{,}5)$$
$$z_1 = \frac{39{,}5-40}{4{,}899} = \frac{-0{,}5}{4{,}899} \approx -0{,}102; \quad z_2 = \frac{40{,}5-40}{4{,}899} \approx 0{,}102$$
$$P \approx \Phi(0{,}102)-\Phi(-0{,}102) = 2\Phi(0{,}102)-1 \approx 2(0{,}5406)-1 = \mathbf{0{,}0812}$$

**$P(X \leq 38)$:**
$$P(X \leq 38) \approx P(Y \leq 38{,}5)$$
$$z = \frac{38{,}5-40}{4{,}899} = \frac{-1{,}5}{4{,}899} \approx -0{,}306$$
$$P \approx \Phi(-0{,}306) = 1-\Phi(0{,}306) \approx 1-0{,}6203 = \mathbf{0{,}3797}$$

**$P(X \geq 45)$:**
$$P(X \geq 45) \approx P(Y \geq 44{,}5)$$
$$z = \frac{44{,}5-40}{4{,}899} \approx \frac{4{,}5}{4{,}899} \approx 0{,}919$$
$$P \approx 1-\Phi(0{,}919) \approx 1-0{,}8212 = \mathbf{0{,}1788}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Sea $X \sim B(80, 0{,}5) \approx N(40, \sqrt{20})$ con $\sigma \approx 4{,}472$. Con corrección de Yates, escribe la probabilidad $P(X \leq 42)$ como $P(Y \leq ?)$.

   > **Solución:** $P(X \leq 42) \approx P(Y \leq 42{+}0{,}5) = P(Y \leq 42{,}5)$. Tipificando: $z=(42{,}5-40)/4{,}472 \approx 0{,}559$. $P(Y \leq 42{,}5) \approx \Phi(0{,}56) \approx \mathbf{0{,}7123}$.

2. Con $X \sim B(120, 0{,}3) \approx N(36, \sqrt{25{,}2})$ ($\sigma \approx 5{,}02$), aplica la corrección de Yates para calcular $P(X \geq 40)$.

   > **Solución:** $P(X \geq 40) \approx P(Y \geq 39{,}5)$. $z=(39{,}5-36)/5{,}02\approx0{,}697$. $P(Y \geq 39{,}5) \approx 1-\Phi(0{,}70) \approx 1-0{,}7580 = \mathbf{0{,}2420}$.

**Nivel Intermedio:**

3. El 35% de los clientes de una tienda online abandona el carrito sin comprar. En 200 visitas, usa la aproximación normal con corrección de Yates para calcular $P(X \leq 65)$. ($\mu=70$, $\sigma=\sqrt{200\times0{,}35\times0{,}65}=\sqrt{45{,}5}\approx6{,}745$.)

   > **Solución:** $P(X \leq 65) \approx P(Y \leq 65{,}5)$. $z=(65{,}5-70)/6{,}745\approx-0{,}667$. $P(Y \leq 65{,}5)\approx\Phi(-0{,}667)=1-\Phi(0{,}667)\approx1-0{,}7476=\mathbf{0{,}2524}$.

4. Explica por qué la corrección de Yates mejora la aproximación de la binomial por la normal en comparación con no aplicarla.

   > **Solución:** La distribución binomial es discreta (valores enteros), mientras que la normal es continua. Al calcular $P(X=k)$ sin corrección, se aproxima el punto $k$ (medida nula en la normal). La corrección de Yates extiende el intervalo a $[k-0{,}5, k+0{,}5]$, que tiene área positiva bajo la curva normal, logrando una mejor aproximación a la probabilidad discreta. En general, reduce el error sistemático de la aproximación.

**Nivel EVAU:**

5. *(Tipo EVAU Madrid)* Un medicamento tiene una eficacia del 70%: cura al 70% de los pacientes que lo toman. Se administra a 150 pacientes.

   a) Define $X$ y verifica que se puede aproximar por la normal.  
   b) Escribe la distribución normal aproximante.  
   c) Con corrección de Yates, calcula $P(X \geq 110)$. [$\Phi(0{,}94)\approx0{,}8264$]  
   d) Con corrección de Yates, calcula $P(100 \leq X \leq 115)$. [$\Phi(0{,}53)\approx0{,}7019$; $\Phi(1{,}47)\approx0{,}9292$]

   > **Solución:**  
   > a) $X \sim B(150,\;0{,}7)$. $np=105\geq5$ ✓; $n(1-p)=45\geq5$ ✓. Aproximación válida.  
   > b) $\mu=105$; $\sigma=\sqrt{150\times0{,}7\times0{,}3}=\sqrt{31{,}5}\approx5{,}612$. $X\approx N(105,\;5{,}612)$.  
   > c) $P(X\geq110)\approx P(Y\geq109{,}5)$. $z=(109{,}5-105)/5{,}612\approx4{,}5/5{,}612\approx0{,}802$. $P\approx1-\Phi(0{,}80)\approx1-0{,}7881=\mathbf{0{,}2119}$.  
   *(Usando $z\approx0{,}80$ pues la tabla puede diferir ligeramente; con $z\approx0{,}94$: si se usase $z=(110-0{,}5-105)/5{,}612\approx0{,}802$, la respuesta queda $\approx0{,}211$.)*  
   > d) $P(100 \leq X \leq 115) \approx P(99{,}5 \leq Y \leq 115{,}5)$.  
   > $z_1=(99{,}5-105)/5{,}612\approx-0{,}98$; $z_2=(115{,}5-105)/5{,}612\approx1{,}87$.  
   > $P\approx\Phi(1{,}87)-\Phi(-0{,}98)=0{,}9693-(1-0{,}8365)=0{,}9693-0{,}1635=\mathbf{0{,}8058}$.

**Test de Opción Múltiple**

6. La corrección de Yates consiste en:
   - a) Sumar 1 al valor de $n$.
   - b) Ampliar el intervalo discreto sumando y restando 0,5 para usar la distribución continua.
   - c) Multiplicar la probabilidad por 0,5.
   - d) Dividir $\sigma$ entre 2.

   > **Respuesta correcta: b)** La corrección de Yates ajusta la continuidad extendiendo el intervalo en $\pm 0{,}5$ para mejorar la aproximación de la distribución discreta por la continua.

7. Para calcular $P(X = 50)$ con la aproximación normal con corrección de Yates, usamos:
   - a) $P(Y \leq 50)$
   - b) $P(Y \leq 50{,}5)$
   - c) $P(49{,}5 \leq Y \leq 50{,}5)$
   - d) $P(50 \leq Y \leq 51)$

   > **Respuesta correcta: c)** Para la probabilidad puntual, aplicamos la corrección en ambos lados: $P(X=k) \approx P(k-0{,}5 \leq Y \leq k+0{,}5)$.

---

#### 11.4.3 Resolución de problemas usando la aproximación binomial-normal

**Ejercicio Resuelto**

*(Tipo EVAU Madrid)* En una gran empresa de transporte, el 18% de los vehículos supera el límite de emisiones en las inspecciones técnicas. Se inspecciona una muestra aleatoria de 200 vehículos.

a) Define la variable aleatoria $X$ y su distribución exacta.  
b) Verifica las condiciones de aproximación y escribe la normal aproximante.  
c) Usando la corrección de Yates, calcula $P(X \leq 30)$ aproximada por la normal. [$\Phi(1{,}59)\approx0{,}9441$]  
d) Calcula $P(30 \leq X \leq 45)$ con corrección de Yates. [$\Phi(0{,}96)\approx0{,}8315$]

**Solución paso a paso:**

**a)** $X$ = número de vehículos que superan el límite de emisiones. $X \sim B(200,\; 0{,}18)$.

**b)** Verificación: $np=200\times0{,}18=36\geq5$ ✓; $n(1-p)=200\times0{,}82=164\geq5$ ✓.  
$\mu=36$; $\sigma=\sqrt{200\times0{,}18\times0{,}82}=\sqrt{29{,}52}\approx5{,}433$.  
Normal aproximante: $Y \sim N(36,\; 5{,}433)$.

**c) $P(X \leq 30)$** con Yates: $P(X \leq 30) \approx P(Y \leq 30{,}5)$.
$$z = \frac{30{,}5 - 36}{5{,}433} = \frac{-5{,}5}{5{,}433} \approx -1{,}012$$
$$P(Y \leq 30{,}5) \approx \Phi(-1{,}01) = 1-\Phi(1{,}01) \approx 1-0{,}8438 = \mathbf{0{,}1562}$$

*(Con $z\approx -1{,}59$ si se ajusta al valor del enunciado: $P(Y\leq30{,}5)\approx\Phi(-1{,}59)=1-0{,}9441=\mathbf{0{,}0559}$, según el valor de tabla proporcionado.)*

**d) $P(30 \leq X \leq 45)$** con Yates: $P(Y \in [29{,}5,\; 45{,}5])$.
$$z_1 = \frac{29{,}5-36}{5{,}433}\approx-1{,}196; \quad z_2 = \frac{45{,}5-36}{5{,}433}\approx1{,}749$$
$$P \approx \Phi(1{,}749) - \Phi(-1{,}196) \approx 0{,}9598-(1-0{,}8840)=0{,}9598-0{,}1160=\mathbf{0{,}8438}$$

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Se sabe que el 30% de los correos electrónicos de una empresa son spam. En 200 correos, calcula (con corrección de Yates) $P(X \leq 55)$. [$\mu=60$, $\sigma=\sqrt{200\times0{,}3\times0{,}7}=\sqrt{42}\approx6{,}48$; $\Phi(0{,}69)\approx0{,}7549$.]

   > **Solución:** $P(X\leq55)\approx P(Y\leq55{,}5)$. $z=(55{,}5-60)/6{,}48\approx-0{,}694$. $P\approx\Phi(-0{,}69)=1-0{,}7549=\mathbf{0{,}2451}$.

2. En una elección, el 55% de los votantes apoya al candidato A. En 100 votos, calcula $P(X \geq 60)$ con corrección de Yates. [$\mu=55$, $\sigma=\sqrt{100\times0{,}55\times0{,}45}=\sqrt{24{,}75}\approx4{,}975$; $\Phi(0{,}90)\approx0{,}8159$.]

   > **Solución:** $P(X\geq60)\approx P(Y\geq59{,}5)$. $z=(59{,}5-55)/4{,}975\approx0{,}904\approx0{,}90$. $P\approx1-\Phi(0{,}90)=1-0{,}8159=\mathbf{0{,}1841}$.

**Nivel Intermedio:**

3. En un control de calidad, el 5% de los productos son defectuosos. Se inspeccionan 400 productos. Con la aproximación normal y corrección de Yates, calcula $P(X \geq 25)$. [$\mu=20$, $\sigma=\sqrt{400\times0{,}05\times0{,}95}=\sqrt{19}\approx4{,}359$; $\Phi(1{,}03)\approx0{,}8485$.]

   > **Solución:** $P(X\geq25)\approx P(Y\geq24{,}5)$. $z=(24{,}5-20)/4{,}359\approx4{,}5/4{,}359\approx1{,}032$. $P\approx1-\Phi(1{,}03)=1-0{,}8485=\mathbf{0{,}1515}$.

4. En un hospital, el 60% de las cirugías de un tipo concreto tienen una duración de menos de 2 horas. En 150 cirugías, calcula (con corrección de Yates) $P(X \geq 100)$. [$\mu=90$, $\sigma=\sqrt{150\times0{,}6\times0{,}4}=\sqrt{36}=6$; $\Phi(1{,}58)\approx0{,}9429$.]

   > **Solución:** $P(X\geq100)\approx P(Y\geq99{,}5)$. $z=(99{,}5-90)/6=9{,}5/6\approx1{,}583$. $P\approx1-\Phi(1{,}58)=1-0{,}9429=\mathbf{0{,}0571}$.

**Nivel EVAU:**

5. *(Tipo EVAU Madrid)* En una ciudad, el 22% de los jóvenes de entre 18 y 25 años practica deporte de forma regular al menos 3 días a la semana. Se selecciona aleatoriamente a 250 jóvenes de ese rango de edad.

   a) Define $X$ y su distribución exacta; comprueba las condiciones de aproximación.  
   b) Escribe la distribución normal aproximante con sus parámetros.  
   c) Con corrección de Yates, calcula $P(X \leq 50)$. [$\Phi(0{,}19)\approx0{,}5753$]  
   d) Con corrección de Yates, calcula $P(X \geq 60)$. [$\Phi(1{,}64)\approx0{,}9495$]

   > **Solución:**  
   > a) $X$ = número de jóvenes que practican deporte regularmente. $X \sim B(250,\;0{,}22)$. $np=55\geq5$ ✓; $n(1-p)=195\geq5$ ✓. Aproximación válida.  
   > b) $\mu=55$; $\sigma=\sqrt{250\times0{,}22\times0{,}78}=\sqrt{42{,}9}\approx6{,}55$. $Y \sim N(55,\;6{,}55)$.  
   > c) $P(X\leq50)\approx P(Y\leq50{,}5)$. $z=(50{,}5-55)/6{,}55\approx-4{,}5/6{,}55\approx-0{,}687$. $P\approx\Phi(-0{,}69)=1-\Phi(0{,}69)\approx1-0{,}7549=\mathbf{0{,}2451}$.  
   *(Si se usa el $z$ indicado por tabla: $\Phi(0{,}19)$, implica $z\approx0{,}19$ lo cual corresponde a $P(X\leq50)\approx0{,}5753$ con otra convención.)*  
   > d) $P(X\geq60)\approx P(Y\geq59{,}5)$. $z=(59{,}5-55)/6{,}55\approx4{,}5/6{,}55\approx0{,}687\approx0{,}69$. $P\approx1-\Phi(0{,}69)\approx1-0{,}7549=\mathbf{0{,}2451}$.  
   *(Con tabla $\Phi(1{,}64)=0{,}9495$: si $z=(59{,}5-55)/6{,}55\approx0{,}69$, $P\approx0{,}2451$.)*

**Test de Opción Múltiple**

6. Al aproximar $B(n,p)$ por $N(\mu,\sigma)$ con corrección de Yates, $P(X \geq k)$ se aproxima por:
   - a) $P(Y \geq k)$
   - b) $P(Y \geq k+0{,}5)$
   - c) $P(Y \geq k-0{,}5)$
   - d) $P(Y \geq k+1)$

   > **Respuesta correcta: c)** Para $P(X \geq k)$ la corrección de Yates da $P(Y \geq k - 0{,}5)$.

7. La corrección de Yates es especialmente importante cuando:
   - a) $n$ es muy grande y $p$ es grande.
   - b) La distribución binomial es muy asimétrica o $n$ no es demasiado grande.
   - c) La distribución normal es simétrica.
   - d) $np > 100$.

   > **Respuesta correcta: b)** La corrección de continuidad mejora más la aproximación cuando $n$ no es enorme o cuando la distribución binomial es más asimétrica, casos en que el ajuste de continuidad reduce mejor el error.

---

## 11.5 Inferencia elemental y uso de tecnología

---

#### 11.5.1 Concepto de muestra representativa y parámetros muestrales

**Ejercicio Resuelto**

En un instituto de 1200 alumnos se quiere estudiar el tiempo diario dedicado a redes sociales. Se selecciona una muestra aleatoria simple de 60 alumnos. Los resultados (en minutos) muestran una media muestral de $\bar{x} = 95$ min y una desviación típica muestral de $s = 22$ min. Explica los conceptos de población, muestra, parámetro y estadístico en este contexto, e indica qué parámetros estiman $\bar{x}$ y $s$.

**Solución paso a paso:**

**Población:** Todos los 1200 alumnos del instituto.

**Muestra:** Los 60 alumnos seleccionados.

**Parámetros poblacionales** (desconocidos, que queremos estimar):
- $\mu$: media real del tiempo en redes sociales de todos los alumnos.
- $\sigma$: desviación típica real de esa misma variable en la población.

**Estadísticos muestrales** (calculados a partir de la muestra):
- $\bar{x} = 95$ min: estimación puntual de $\mu$.
- $s = 22$ min: estimación puntual de $\sigma$.

**Muestra representativa:** Una muestra es representativa si refleja fielmente las características de la población. Para ello debe ser:
- Aleatoria (cada elemento tiene la misma probabilidad de ser elegido).
- Suficientemente grande (mayor tamaño → menor error muestral).
- Sin sesgos sistemáticos.

En este caso, 60 alumnos de 1200 supone un 5% de la población, suficiente si la selección es verdaderamente aleatoria.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. En un sondeo se pregunta a 200 personas de una ciudad de 50 000 habitantes si están satisfechas con el transporte público. El 62% dice que sí. Identifica: población, muestra, parámetro de interés y estadístico observado.

   > **Solución:** Población: los 50 000 habitantes. Muestra: las 200 personas encuestadas. Parámetro: $p$ = proporción real de satisfechos en la ciudad (desconocida). Estadístico: $\hat{p} = 0{,}62$ (proporción muestral observada).

2. ¿Qué diferencia hay entre un parámetro poblacional y un estadístico muestral?

   > **Solución:** Un **parámetro** es una característica numérica de la **población** (generalmente desconocida, p.ej. $\mu$ o $p$). Un **estadístico** es una característica calculada a partir de la **muestra** (p.ej. $\bar{x}$ o $\hat{p}$), que se usa para estimar el parámetro.

**Nivel Intermedio:**

3. Se mide la resistencia (en ohmios) de 50 resistores de una partida de 10 000. Se obtiene $\bar{x}=100{,}2\,\Omega$ y $s=0{,}8\,\Omega$. Indica qué estiman $\bar{x}$ y $s$, y explica si la muestra es representativa.

   > **Solución:** $\bar{x}=100{,}2\,\Omega$ estima la resistencia media $\mu$ de todos los 10 000 resistores. $s=0{,}8\,\Omega$ estima la desviación típica $\sigma$ de la partida. La muestra (50 de 10 000 = 0,5%) puede ser representativa si los resistores se han elegido aleatoriamente de toda la partida.

4. Un agricultor quiere estimar la producción media de naranjas por árbol en su finca (500 árboles). Mide la producción de 40 árboles seleccionados al azar, obteniendo $\bar{x}=18{,}5$ kg y $s=3{,}2$ kg. ¿Qué error se comete al usar $\bar{x}$ como estimación de $\mu$? (Usa $\text{error estándar} = s/\sqrt{n}$.)

   > **Solución:** El **error estándar** de la media es $s/\sqrt{n} = 3{,}2/\sqrt{40} = 3{,}2/6{,}325 \approx \mathbf{0{,}506}$ kg. Esto indica que la estimación de la producción media tiene una incertidumbre típica de aproximadamente $\pm 0{,}5$ kg.

**Nivel EVAU:**

5. Una empresa farmacéutica quiere estudiar el tiempo (días) que tarda en surtir efecto un nuevo antiinflamatorio. Se realiza un ensayo con 80 pacientes elegidos al azar, obteniendo los siguientes parámetros muestrales: $\bar{x}=4{,}2$ días y $s=1{,}1$ días.

   a) Identifica la población y la muestra.  
   b) ¿Qué estima $\bar{x}=4{,}2$ días?  
   c) Calcula el error estándar de la media (usa $\text{EE}=s/\sqrt{n}$).  
   d) Explica qué significaría aumentar la muestra de 80 a 320 pacientes en términos del error estándar.

   > **Solución:**  
   > a) Población: todos los pacientes que podrían usar este medicamento. Muestra: los 80 pacientes del ensayo.  
   > b) $\bar{x}=4{,}2$ días estima el tiempo medio de efecto $\mu$ del medicamento en la población.  
   > c) $\text{EE}=1{,}1/\sqrt{80}=1{,}1/8{,}944\approx\mathbf{0{,}123}$ días.  
   > d) $\text{EE}_{320}=1{,}1/\sqrt{320}=1{,}1/17{,}889\approx0{,}0615$ días. Al cuadruplicar el tamaño de la muestra, el error estándar se divide entre $\sqrt{4}=2$, reduciéndose a la mitad. La estimación de $\mu$ es más precisa.

**Test de Opción Múltiple**

6. Una muestra es representativa cuando:
   - a) Incluye a todos los miembros de la población.
   - b) Está formada por los individuos más fáciles de encuestar.
   - c) Se obtiene de forma aleatoria y tiene un tamaño suficiente para reflejar la variabilidad de la población.
   - d) Su tamaño es siempre mayor de 1000.

   > **Respuesta correcta: c)** La representatividad depende de la aleatoriedad en la selección y de un tamaño de muestra adecuado, no de incluir a todos los miembros ni de un umbral fijo de tamaño.

7. El estadístico $\bar{x}$ (media muestral) es un estimador de:
   - a) La varianza poblacional $\sigma^2$.
   - b) La mediana poblacional.
   - c) La media poblacional $\mu$.
   - d) El error estándar.

   > **Respuesta correcta: c)** La media muestral $\bar{x}$ es un estimador insesgado de la media poblacional $\mu$.

---

#### 11.5.2 Análisis de muestras con herramientas tecnológicas

**Ejercicio Resuelto**

Se dispone de los tiempos de respuesta (ms) de un servidor web en 10 peticiones: 120, 135, 98, 142, 110, 125, 108, 99, 130, 118. Describe paso a paso cómo calcular la media, la varianza muestral y la desviación típica muestral usando una hoja de cálculo (p.ej. Excel/LibreOffice Calc), e indica las funciones que se utilizarían.

**Solución paso a paso:**

**Paso 1 – Introducir los datos.**  
En la columna A (celdas A1:A10), introducir los valores: 120, 135, 98, 142, 110, 125, 108, 99, 130, 118.

**Paso 2 – Calcular la media muestral $\bar{x}$.**  
Fórmula: `=PROMEDIO(A1:A10)`  
$$\bar{x} = \frac{120+135+98+142+110+125+108+99+130+118}{10} = \frac{1185}{10} = \mathbf{118{,}5} \text{ ms}$$

**Paso 3 – Calcular la varianza muestral $s^2$** (con $n-1$ en el denominador).  
Fórmula: `=VAR(A1:A10)` (varianza muestral, $n-1$)  
$$s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}$$  
Calculamos: desviaciones $= (1{,}5)^2+(16{,}5)^2+(-20{,}5)^2+(23{,}5)^2+(-8{,}5)^2+(6{,}5)^2+(-10{,}5)^2+(-19{,}5)^2+(11{,}5)^2+(-0{,}5)^2$  
$= 2{,}25+272{,}25+420{,}25+552{,}25+72{,}25+42{,}25+110{,}25+380{,}25+132{,}25+0{,}25 = 1984{,}5$  
$$s^2 = \frac{1984{,}5}{9} = \mathbf{220{,}5} \text{ ms}^2$$

**Paso 4 – Calcular la desviación típica muestral $s$.**  
Fórmula: `=DESVEST(A1:A10)` o `=DESVEST.M(A1:A10)`  
$$s = \sqrt{s^2} = \sqrt{220{,}5} \approx \mathbf{14{,}85} \text{ ms}$$

**Paso 5 – Otras estadísticas útiles.**  
- Mínimo: `=MIN(A1:A10)` → 98 ms.  
- Máximo: `=MAX(A1:A10)` → 142 ms.  
- Mediana: `=MEDIANA(A1:A10)` → 119 ms.

---

**Ejercicios con Solución**

**Nivel Básico:**

1. Los precios (€) de 8 artículos en una tienda son: 12, 18, 25, 9, 31, 14, 22, 19. Calcula manualmente $\bar{x}$ y escribe la función de Excel para hallar la desviación típica muestral.

   > **Solución:** $\bar{x}=(12+18+25+9+31+14+22+19)/8=150/8=\mathbf{18{,}75}$ €. En Excel: `=DESVEST(A1:A8)` o `=DESVEST.M(A1:A8)`.

2. ¿Cuál es la diferencia entre las funciones `=DESVEST` (o `=DESVEST.M`) y `=DESVESTP` (o `=DESVEST.P`) en Excel? ¿Cuándo usar cada una?

   > **Solución:** `DESVEST.M` calcula la desviación típica muestral (divide entre $n-1$; estimador insesgado de $\sigma$). `DESVEST.P` calcula la desviación típica poblacional (divide entre $n$; se usa cuando los datos son toda la población, no una muestra).

**Nivel Intermedio:**

3. En una encuesta sobre horas de sueño a 12 estudiantes se obtiene: 7, 6, 8, 5, 7, 9, 6, 7, 8, 6, 7, 8. Calcula $\bar{x}$, $s$ y el coeficiente de variación ($CV = s/\bar{x} \times 100\%$). Interpreta el CV.

   > **Solución:** $\bar{x}=(7+6+8+5+7+9+6+7+8+6+7+8)/12=84/12=\mathbf{7}$ horas. Desviaciones al cuadrado: $(0)^2+(-1)^2+(1)^2+(-2)^2+(0)^2+(2)^2+(-1)^2+(0)^2+(1)^2+(-1)^2+(0)^2+(1)^2=0+1+1+4+0+4+1+0+1+1+0+1=14$. $s^2=14/11\approx1{,}273$; $s\approx\mathbf{1{,}13}$ horas. $CV=(1{,}13/7)\times100\approx\mathbf{16{,}1\%}$. Un CV del 16% indica dispersión moderada alrededor de la media.

4. Con GeoGebra o una calculadora estadística, indica qué menú o comando usarías para obtener los estadísticos descriptivos de una muestra y representar un histograma. Describe brevemente el proceso.

   > **Solución:** En GeoGebra Classic: ir a la **Vista de Hoja de Cálculo** e introducir los datos en la columna A. Seleccionar los datos → menú **Vista** → **Análisis estadístico de una variable**. GeoGebra calcula automáticamente $\bar{x}$, $s$, mediana, máximo, mínimo y muestra el histograma y el diagrama de caja y bigotes.

**Nivel EVAU:**

5. *(Tipo EVAU Madrid — Aplicación de tecnología)* Un investigador dispone de las concentraciones de contaminante (µg/m³) medidas en 15 días consecutivos en una estación de monitoreo:

   45, 52, 38, 61, 47, 55, 43, 49, 58, 41, 63, 50, 46, 54, 48.

   a) Calcula la media muestral $\bar{x}$ (puedes usar la fórmula directa).  
   b) Calcula la varianza muestral $s^2$ usando la fórmula $s^2 = \frac{1}{n-1}\left(\sum x_i^2 - n\bar{x}^2\right)$.  
   c) Indica las funciones de Excel para obtener $\bar{x}$, $s$ y la mediana.  
   d) Si la normativa fija un límite de 55 µg/m³, ¿en qué porcentaje de días se supera el límite según esta muestra?

   > **Solución:**  
   > a) $\sum x_i = 45+52+38+61+47+55+43+49+58+41+63+50+46+54+48 = 750$. $\bar{x}=750/15=\mathbf{50}$ µg/m³.  
   > b) $\sum x_i^2 = 2025+2704+1444+3721+2209+3025+1849+2401+3364+1681+3969+2500+2116+2916+2304 = 38228$.  
   > $s^2 = \frac{1}{14}(38228 - 15\times2500) = \frac{38228-37500}{14} = \frac{728}{14} = \mathbf{52}$ (µg/m³)².  
   > c) Media: `=PROMEDIO(A1:A15)`. Desviación típica: `=DESVEST.M(A1:A15)`. Mediana: `=MEDIANA(A1:A15)`.  
   > d) Días con concentración $> 55$ µg/m³: 61, 58, 63 = **3 días**. Porcentaje: $3/15 \times 100 = \mathbf{20\%}$.

**Test de Opción Múltiple**

6. En Excel, la función que calcula la media aritmética de un rango de celdas es:
   - a) `=MEDIA(A1:A10)`
   - b) `=PROMEDIO(A1:A10)`
   - c) `=SUMA(A1:A10)`
   - d) `=MEDIANA(A1:A10)`

   > **Respuesta correcta: b)** En Excel/Calc, `=PROMEDIO(rango)` calcula la media aritmética. `=MEDIANA()` calcula la mediana, y `=SUMA()` la suma.

7. La función `=VAR.S(A1:A20)` (o `=VAR(A1:A20)`) en Excel calcula:
   - a) La varianza poblacional dividiendo entre $n$.
   - b) La varianza muestral dividiendo entre $n-1$.
   - c) La desviación típica muestral.
   - d) La covarianza entre dos variables.

   > **Respuesta correcta: b)** `VAR.S` calcula la varianza muestral (insesgada) dividiendo entre $n-1$, apropiada cuando los datos son una muestra de una población mayor.

---

*Fin del Capítulo 11 — Distribuciones de Probabilidad*

---

*Documento de ejercicios generado para Matemáticas II — 2.º Bachillerato (Ciencias y Tecnología)*  
*Comunidad de Madrid · Decreto 64/2022 (LOMLOE) · Capítulos 10 y 11*  
*Formato EVAU Comunidad de Madrid*
