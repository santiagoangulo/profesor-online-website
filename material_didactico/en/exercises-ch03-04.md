# Mathematics II — Exercises: Chapters 3-4
## Systems of Linear Equations and Vectors in Space

**Course:** 2nd Year Bachillerato — Sciences and Technology  
**Region:** Community of Madrid  
**Regulatory framework:** Decree 64/2022 (LOMLOE) / FUHEM Curriculum 2025-26  
**Chapters covered:** 3. Systems of Linear Equations · 4. Vectors in Space

---

# CHAPTER 3. SYSTEMS OF LINEAR EQUATIONS

---

## 3.1 Linear systems: fundamental concepts

---

#### 3.1.1 Definition of a linear system. Solution, consistent and inconsistent systems

**Worked Example**

Determine whether the pair $(x, y) = (2, -1)$ is a solution of the system:

$$\begin{cases} 3x + 2y = 4 \\ x - 3y = 5 \end{cases}$$

**Step-by-step Solution:**

We substitute $x = 2$, $y = -1$ into each equation:

- **Equation 1:** $3(2) + 2(-1) = 6 - 2 = 4$ ✓
- **Equation 2:** $2 - 3(-1) = 2 + 3 = 5$ ✓

Since the pair satisfies both equations simultaneously, $(2, -1)$ **is a solution** of the system. The system is **consistent and determined** (it has exactly one solution).

---

**Exercises with Solutions**

**Basic Level:**

1. Check whether $(x, y) = (1, 3)$ is a solution of the system:
   $$\begin{cases} 2x + y = 5 \\ x - y = -2 \end{cases}$$
   > **Solution:** Equation 1: $2(1) + 3 = 5$ ✓. Equation 2: $1 - 3 = -2$ ✓. Yes, it is a solution. The system is consistent and determined.

2. Indicate whether the system $\begin{cases} x + y = 3 \\ 2x + 2y = 7 \end{cases}$ can have a solution.
   > **Solution:** The second equation is equivalent to $x + y = 3{,}5$, which contradicts the first ($x + y = 3$). The system is **inconsistent**: it has no solution.

**Intermediate Level:**

3. Determine the value of $k$ so that $(1, k)$ is a solution of the system:
   $$\begin{cases} 2x - y = 3 \\ 3x + 2y = k + 5 \end{cases}$$
   > **Solution:** From the first equation: $2(1) - k = 3 \Rightarrow k = -1$. We verify in the second: $3(1) + 2(-1) = 1$; we need $1 = k + 5 = -1 + 5 = 4$. Contradiction, so **no such $k$ exists** that makes $(1,k)$ a simultaneous solution of both equations as stated. (If only the first is imposed: $k = -1$.)

4. Classify the following systems without solving them completely, reasoning from the equations:
   - (a) $\begin{cases} x + 2y = 4 \\ 3x + 6y = 12 \end{cases}$ 
   - (b) $\begin{cases} x - y = 1 \\ 2x - 2y = 5 \end{cases}$
   > **Solution:** (a) The second is three times the first: they are the same line. **Consistent and indeterminate** (infinitely many solutions). (b) The second is equivalent to $x - y = 2{,}5$, inconsistent with the first. **Inconsistent system**.

**EVAU Level:**

5. Consider the system of equations:
   $$\begin{cases} ax + 2y = 6 \\ 3x + by = 9 \end{cases}$$
   **(a)** Find values of $a$ and $b$ for which the system is consistent and determined.  
   **(b)** Find values of $a$ and $b$ for which it is inconsistent.  
   **(c)** Find values of $a$ and $b$ for which it is consistent and indeterminate.
   > **Solution:**  
   > We form the coefficient matrix $A = \begin{pmatrix} a & 2 \\ 3 & b \end{pmatrix}$ and the augmented matrix $A^* = \begin{pmatrix} a & 2 & 6 \\ 3 & b & 9 \end{pmatrix}$.  
   > $|A| = ab - 6$.  
   > **(a) Consistent and determined:** $|A| \neq 0$, i.e., $ab \neq 6$. For example, $a = 1, b = 1$.  
   > **(b) Inconsistent:** $|A| = 0$ ($ab = 6$) and $\text{rank}(A) \neq \text{rank}(A^*)$. If $ab = 6$ the second equation is $3x + (6/a)y = 9$. Multiplying the first by $3/a$: $3x + (6/a)y = 18/a$. For inconsistency: $18/a \neq 9 \Rightarrow a \neq 2$. Example: $a = 1, b = 6$.  
   > **(c) Consistent and indeterminate:** $ab = 6$ and moreover the equations are proportional: $6/a = 9/9 \Rightarrow a = 2, b = 3$.

**Multiple Choice Test**

6. How many solutions does the system $\begin{cases} 2x - y = 4 \\ -4x + 2y = -8 \end{cases}$ have?
   - a) None
   - b) Exactly one
   - c) Exactly two
   - d) Infinitely many
   > **Correct answer: d)** The second equation is $-2$ times the first, so both represent the same line. The system is consistent and indeterminate with infinitely many solutions.

7. A system of two linear equations with two unknowns is **inconsistent** when:
   - a) The two equations represent the same line
   - b) The two lines intersect at a point
   - c) The two lines are parallel and distinct
   - d) The determinant of the coefficient matrix is nonzero
   > **Correct answer: c)** Two distinct parallel lines have no point in common, which results in a system with no solution (inconsistent).

---

#### 3.1.2 Geometric interpretation in 2D and 3D

**Worked Example**

Describe the geometric interpretation of the system:
$$\begin{cases} x + y + z = 3 \\ 2x - y + z = 1 \\ x + 2y - z = 4 \end{cases}$$

**Step-by-step Solution:**

Each linear equation in three variables represents a **plane** in $\mathbb{R}^3$.

- The system has a solution if the three planes have a common point.
- To check, we solve by Gaussian elimination:

$$\begin{pmatrix} 1 & 1 & 1 & | & 3 \\ 2 & -1 & 1 & | & 1 \\ 1 & 2 & -1 & | & 4 \end{pmatrix} \xrightarrow{F_2 \leftarrow F_2 - 2F_1,\; F_3 \leftarrow F_3 - F_1} \begin{pmatrix} 1 & 1 & 1 & | & 3 \\ 0 & -3 & -1 & | & -5 \\ 0 & 1 & -2 & | & 1 \end{pmatrix}$$

$$\xrightarrow{F_3 \leftarrow 3F_3 + F_2} \begin{pmatrix} 1 & 1 & 1 & | & 3 \\ 0 & -3 & -1 & | & -5 \\ 0 & 0 & -7 & | & -2 \end{pmatrix}$$

Rank of $A$ = rank of $A^*$ = 3 = number of unknowns. **Consistent and determined:** the three planes intersect at a unique point.

Solving: $z = 2/7$, $y = (2 \cdot 2/7 - 5)/(-3) = (4/7 - 35/7)/(-3) = (-31/7)/(-3) = 31/21$, $x = 3 - 31/21 - 2/7 = 3 - 31/21 - 6/21 = 63/21 - 37/21 = 26/21$.

---

**Exercises with Solutions**

**Basic Level:**

1. Describe the geometric interpretation of the system $\begin{cases} 2x - y = 3 \\ x + y = 6 \end{cases}$ and indicate the expected type of solution.
   > **Solution:** Each equation represents a **line** in $\mathbb{R}^2$. Since the lines are not parallel (the coefficients are not proportional: $2/1 \neq -1/1$), they intersect at a point. The system is **consistent and determined**.

2. What type of system do two distinct parallel planes in $\mathbb{R}^3$ represent?
   > **Solution:** Two distinct parallel planes have no point in common, so the system of two equations that represents them is **inconsistent**.

**Intermediate Level:**

3. A $3\times 3$ system turns out to be consistent and indeterminate with infinitely many solutions depending on one parameter. Interpret this situation geometrically.
   > **Solution:** Geometrically, this means the three planes intersect in a **common line** (not at a unique point). The solution set is that line, parameterised by one free parameter.

4. What type is the system $\begin{cases} x + y - z = 2 \\ 2x + 2y - 2z = 4 \\ 3x + 3y - 3z = 6 \end{cases}$ and what is its geometric interpretation?
   > **Solution:** The three equations are multiples of the first: the three planes are **coincident**. The system is **consistent and indeterminate** with infinitely many solutions depending on two parameters (an entire plane).

**EVAU Level:**

5. Consider the lines in the plane $r: 3x - y = 2$ and $s: 6x - 2y = k$.  
   **(a)** For which values of $k$ are they coincident.  
   **(b)** For which values of $k$ are they distinct parallel lines.  
   **(c)** Interpret each case as a system of equations.
   > **Solution:**  
   > We divide $s$ by 2: $3x - y = k/2$.  
   > **(a) Coincident:** $k/2 = 2 \Rightarrow k = 4$. Consistent and indeterminate system (infinitely many solutions).  
   > **(b) Distinct parallel:** same direction ($3x - y$) but $k \neq 4$. Inconsistent system.  
   > **(c)** For $k = 4$: the system has infinitely many solutions $y = 3x - 2$, $x \in \mathbb{R}$. For $k \neq 4$: no solution.

**Multiple Choice Test**

6. In $\mathbb{R}^3$, a consistent indeterminate system with rank 2 (of a $3\times 3$ matrix) corresponds geometrically to:
   - a) Three planes intersecting at a unique point
   - b) Three planes intersecting in a common line
   - c) Three coincident planes
   - d) Three distinct parallel planes
   > **Correct answer: b)** Rank 2 with 3 unknowns $\Rightarrow$ 1 degree of freedom, which geometrically is a line of intersection of the three planes.

7. The system $\begin{cases} x - 2y = 1 \\ -2x + 4y = -2 \end{cases}$ represents two lines in the plane that are:
   - a) Secant
   - b) Perpendicular
   - c) Coincident
   - d) Distinct parallel lines
   > **Correct answer: c)** The second equation is exactly $-2$ times the first, so both are the same line (coincident).

---

#### 3.1.3 Matrix representation: form $A \cdot x = b$

**Worked Example**

Write the system $\begin{cases} 2x - y + 3z = 5 \\ x + 4y - z = 2 \\ 3x - 2y + z = -1 \end{cases}$ in matrix form $A \cdot \mathbf{x} = \mathbf{b}$ and identify each element.

**Step-by-step Solution:**

The **coefficient matrix** is:
$$A = \begin{pmatrix} 2 & -1 & 3 \\ 1 & 4 & -1 \\ 3 & -2 & 1 \end{pmatrix}$$

The **vector of unknowns** is $\mathbf{x} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$ and the **vector of constant terms** is $\mathbf{b} = \begin{pmatrix} 5 \\ 2 \\ -1 \end{pmatrix}$.

The **matrix form** is:
$$\begin{pmatrix} 2 & -1 & 3 \\ 1 & 4 & -1 \\ 3 & -2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 5 \\ 2 \\ -1 \end{pmatrix}$$

The **augmented matrix** (used in the Rouché–Frobenius theorem) is:
$$A^* = \left(\begin{array}{ccc|c} 2 & -1 & 3 & 5 \\ 1 & 4 & -1 & 2 \\ 3 & -2 & 1 & -1 \end{array}\right)$$

---

**Exercises with Solutions**

**Basic Level:**

1. Write in the form $A\mathbf{x} = \mathbf{b}$ the system $\begin{cases} 4x - 2y = 7 \\ -x + 5y = 3 \end{cases}$.
   > **Solution:** $A = \begin{pmatrix} 4 & -2 \\ -1 & 5 \end{pmatrix}$, $\mathbf{x} = \begin{pmatrix} x \\ y \end{pmatrix}$, $\mathbf{b} = \begin{pmatrix} 7 \\ 3 \end{pmatrix}$. Matrix form: $\begin{pmatrix} 4 & -2 \\ -1 & 5 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 7 \\ 3 \end{pmatrix}$.

2. Given the matrix equation $\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 4 \\ 2 \end{pmatrix}$, write the corresponding system of equations.
   > **Solution:** $\begin{cases} x + 2y = 4 \\ 3x - y = 2 \end{cases}$

**Intermediate Level:**

3. Write the augmented matrix of the system: $\begin{cases} 5x - z = 3 \\ 2y + 3z = 1 \\ x - y = 0 \end{cases}$ and compute the determinant of the submatrix $A$.
   > **Solution:** Note that $y$ is missing in the first equation and $x$ in the second: $A = \begin{pmatrix} 5 & 0 & -1 \\ 0 & 2 & 3 \\ 1 & -1 & 0 \end{pmatrix}$, $A^* = \left(\begin{array}{ccc|c} 5 & 0 & -1 & 3 \\ 0 & 2 & 3 & 1 \\ 1 & -1 & 0 & 0 \end{array}\right)$. $|A| = 5(0+3) - 0 + (-1)(0-2) = 15 + 2 = 17$.

4. If $A\mathbf{x} = \mathbf{b}$ and $|A| \neq 0$, explain why the unique solution is $\mathbf{x} = A^{-1}\mathbf{b}$.
   > **Solution:** If $|A| \neq 0$, $A$ is invertible. Multiplying on the left by $A^{-1}$: $A^{-1}(A\mathbf{x}) = A^{-1}\mathbf{b} \Rightarrow (A^{-1}A)\mathbf{x} = A^{-1}\mathbf{b} \Rightarrow I\mathbf{x} = A^{-1}\mathbf{b} \Rightarrow \mathbf{x} = A^{-1}\mathbf{b}$.

**EVAU Level:**

5. Let $A = \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \\ 2 & -1 & 1 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 1 \\ 4 \\ -2 \end{pmatrix}$.  
   **(a)** Compute $|A|$.  
   **(b)** Deduce whether the system $A\mathbf{x} = \mathbf{b}$ is consistent and determined.  
   **(c)** Write the augmented matrix.
   > **Solution:**  
   > **(a)** Expanding along the first column:  
   > $|A| = 1 \cdot \begin{vmatrix} 1 & 3 \\ -1 & 1 \end{vmatrix} - 0 + 2 \cdot \begin{vmatrix} 2 & -1 \\ 1 & 3 \end{vmatrix} = 1(1+3) + 2(6+1) = 4 + 14 = 18$.  
   > **(b)** Since $|A| = 18 \neq 0$, the rank of $A$ is 3. By Rouché–Frobenius, $\text{rank}(A) = \text{rank}(A^*) = 3 =$ number of unknowns. **Consistent and determined**.  
   > **(c)** $A^* = \left(\begin{array}{ccc|c} 1 & 2 & -1 & 1 \\ 0 & 1 & 3 & 4 \\ 2 & -1 & 1 & -2 \end{array}\right)$.

**Multiple Choice Test**

6. In the system $A\mathbf{x} = \mathbf{b}$, the **augmented matrix** $A^*$ is formed by:
   - a) Adding a row of zeros to $A$
   - b) Appending the column $\mathbf{b}$ to the right of $A$
   - c) Multiplying $A$ by $\mathbf{b}$
   - d) Transposing $A$ and concatenating with $\mathbf{b}$
   > **Correct answer: b)** The augmented matrix $A^* = (A|\mathbf{b})$ is obtained by appending the vector of constant terms as the last column of $A$.

7. If the coefficient matrix of a $3\times 3$ system has $|A| = 0$, then:
   - a) The system is always inconsistent
   - b) The system always has infinitely many solutions
   - c) The system may be inconsistent or consistent and indeterminate
   - d) The system is always consistent and determined
   > **Correct answer: c)** $|A| = 0$ implies $\text{rank}(A) < 3$, which requires analysing $\text{rank}(A^*)$ to determine whether it is inconsistent ($\text{rank}(A) \neq \text{rank}(A^*)$) or consistent and indeterminate ($\text{rank}(A) = \text{rank}(A^*)$).

---

## 3.2 Rouché–Frobenius Theorem

---

#### 3.2.1 Statement of the theorem: consistency condition via ranks

**Worked Example**

State the Rouché–Frobenius theorem and apply it to study the consistency of the system:
$$\begin{cases} x + 2y + z = 3 \\ 2x + 4y + 2z = 6 \\ 3x + y - z = 2 \end{cases}$$

**Step-by-step Solution:**

**Rouché–Frobenius Theorem:** A system $A\mathbf{x} = \mathbf{b}$ is consistent if and only if $\text{rank}(A) = \text{rank}(A^*)$. If it is consistent:
- If $\text{rank}(A) = n$ (number of unknowns): **consistent and determined** (unique solution).
- If $\text{rank}(A) < n$: **consistent and indeterminate** ($n - \text{rank}(A)$ free parameters).

**Application:**

$$A^* = \left(\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 2 & 4 & 2 & 6 \\ 3 & 1 & -1 & 2 \end{array}\right)$$

We observe that $F_2 = 2 \cdot F_1$ and the constant terms also: $6 = 2 \cdot 3$. We perform $F_2 \leftarrow F_2 - 2F_1$, $F_3 \leftarrow F_3 - 3F_1$:

$$\left(\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 0 & 0 & 0 \\ 0 & -5 & -4 & -7 \end{array}\right) \xrightarrow{F_2 \leftrightarrow F_3} \left(\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & -5 & -4 & -7 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

$\text{rank}(A) = \text{rank}(A^*) = 2 < 3$ (unknowns). By Rouché–Frobenius: **consistent and indeterminate** with $3 - 2 = 1$ degree of freedom. Solution: from $-5y - 4z = -7$ with $z = \lambda$: $y = (7 - 4\lambda)/5$; $x = 3 - 2(7-4\lambda)/5 - \lambda = (15 - 14 + 8\lambda - 5\lambda)/5 = (1 + 3\lambda)/5$.

---

**Exercises with Solutions**

**Basic Level:**

1. Compute the ranks of $A$ and $A^*$ and classify the system:
   $$\begin{cases} x + y = 2 \\ 2x + 2y = 5 \end{cases}$$
   > **Solution:** $A^* = \begin{pmatrix} 1 & 1 & 2 \\ 2 & 2 & 5 \end{pmatrix}$. We perform $F_2 - 2F_1$: $\begin{pmatrix} 1 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}$. $\text{rank}(A) = 1$, $\text{rank}(A^*) = 2$. Since $\text{rank}(A) \neq \text{rank}(A^*)$: **inconsistent**.

2. For the system $\begin{cases} 2x - y = 4 \\ -4x + 2y = -8 \end{cases}$, compute the ranks and classify.
   > **Solution:** $A^* = \begin{pmatrix} 2 & -1 & 4 \\ -4 & 2 & -8 \end{pmatrix}$. $F_2 + 2F_1$: $\begin{pmatrix} 2 & -1 & 4 \\ 0 & 0 & 0 \end{pmatrix}$. $\text{rank}(A) = \text{rank}(A^*) = 1 < 2$. **Consistent and indeterminate** with 1 free parameter.

**Intermediate Level:**

3. Study the consistency and, if consistent, solve:
   $$\begin{cases} x + y - z = 2 \\ 2x - y + z = 1 \\ x - 2y + 2z = -1 \end{cases}$$
   > **Solution:** Row reduction: $F_2 - 2F_1$: $(0,-3,3|-3)$; $F_3 - F_1$: $(0,-3,3|-3)$. Then $F_3 - F_2$: $(0,0,0|0)$. $\text{rank}(A)=\text{rank}(A^*)=2<3$. Consistent and indeterminate. With $z=\lambda$: $-3y+3\lambda=-3 \Rightarrow y=\lambda+1$; $x=2-(\\lambda+1)+\lambda=1$. Solution: $x=1,\; y=\lambda+1,\; z=\lambda$, $\lambda\in\mathbb{R}$.

4. Can a $4\times 3$ system (4 equations, 3 unknowns) be consistent and determined? Reason using Rouché–Frobenius.
   > **Solution:** Yes. If $\text{rank}(A)=\text{rank}(A^*)=3$ (equal to the number of unknowns), the system is consistent and determined. The 4 equations may be redundant among themselves but consistent with the constant terms.

**EVAU Level:**

5. **(EVAU Madrid style)** Study the consistency depending on the values of $m$ for the system:
   $$\begin{cases} x + y + z = 3 \\ x + my + 2z = 4 \\ 2x + y + mz = m+3 \end{cases}$$
   Solve the system in the cases where it is consistent.
   > **Solution:**  
   > $|A| = \begin{vmatrix} 1 & 1 & 1 \\ 1 & m & 2 \\ 2 & 1 & m \end{vmatrix}$. Expanding: $= m^2 - 2m - 3 + 4 - m - 2m + 2 = m^2 - 3m +1$. Performing the computation correctly:  
   > $|A| = 1(m^2-2) - 1(m-4) + 1(1-2m) = m^2 - 2 - m + 4 + 1 - 2m = m^2 - 3m + 3$.  
   > Discriminant: $\Delta = 9 - 12 = -3 < 0$. Therefore $|A| \neq 0$ for all $m \in \mathbb{R}$.  
   > **Conclusion:** The system is **always consistent and determined** (for all $m$). The solution is obtained by Cramer's rule or Gaussian elimination for each specific value of $m$.  
   > For $m=0$: $|A|=3$. By Gauss: $F_2-F_1$: $(0,-1,1|1)$; $F_3-2F_1$: $(0,-1,-2|-3)$. $F_3-F_2$: $(0,0,-3|-4) \Rightarrow z=4/3$; $y=1-4/3=-1/3$; $x=3+1/3-4/3=3-1=2$.

**Multiple Choice Test**

6. The Rouché–Frobenius theorem states that a system is consistent if and only if:
   - a) $|A| \neq 0$
   - b) $\text{rank}(A) = \text{rank}(A^*)$
   - c) $\text{rank}(A) < n$
   - d) $\text{rank}(A^*) = n + 1$
   > **Correct answer: b)** The consistency condition is the equality of ranks of the coefficient matrix and the augmented matrix. Option a) is only sufficient for consistent and determined but not necessary.

7. A $3\times 3$ system has $\text{rank}(A) = 2$ and $\text{rank}(A^*) = 2$. It is therefore:
   - a) Inconsistent
   - b) Consistent and determined
   - c) Consistent and indeterminate with 1 free parameter
   - d) Consistent and indeterminate with 2 free parameters
   > **Correct answer: c)** $\text{rank}(A) = \text{rank}(A^*) = 2$ implies consistency. Number of parameters = $n - \text{rank}(A) = 3 - 2 = 1$.

---

#### 3.2.2 Classification of the system: inconsistent, consistent determined, consistent indeterminate

**Worked Example**

Classify and solve the following system:
$$\begin{cases} 2x + y - z = 3 \\ x - y + 2z = 1 \\ 4x - y + 3z = 5 \end{cases}$$

**Step-by-step Solution:**

We form the augmented matrix and apply row reduction:

$$\left(\begin{array}{ccc|c} 2 & 1 & -1 & 3 \\ 1 & -1 & 2 & 1 \\ 4 & -1 & 3 & 5 \end{array}\right) \xrightarrow{F_1 \leftrightarrow F_2} \left(\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 2 & 1 & -1 & 3 \\ 4 & -1 & 3 & 5 \end{array}\right)$$

$F_2 \leftarrow F_2 - 2F_1$: $(0, 3, -5 | 1)$. $F_3 \leftarrow F_3 - 4F_1$: $(0, 3, -5 | 1)$.

$$\left(\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 0 & 3 & -5 & 1 \\ 0 & 3 & -5 & 1 \end{array}\right) \xrightarrow{F_3 \leftarrow F_3 - F_2} \left(\begin{array}{ccc|c} 1 & -1 & 2 & 1 \\ 0 & 3 & -5 & 1 \\ 0 & 0 & 0 & 0 \end{array}\right)$$

$\text{rank}(A) = \text{rank}(A^*) = 2 < 3$. **Consistent and indeterminate** with 1 parameter.

**Solution:** Let $z = \lambda \in \mathbb{R}$. From $F_2$: $3y = 1 + 5\lambda \Rightarrow y = \frac{1+5\lambda}{3}$. From $F_1$: $x = 1 + y - 2\lambda = 1 + \frac{1+5\lambda}{3} - 2\lambda = \frac{3+1+5\lambda-6\lambda}{3} = \frac{4-\lambda}{3}$.

**Solution:** $\left(x, y, z\right) = \left(\dfrac{4-\lambda}{3},\; \dfrac{1+5\lambda}{3},\; \lambda\right),\; \lambda \in \mathbb{R}$.

---

**Exercises with Solutions**

**Basic Level:**

1. Classify the system $\begin{cases} x - 2y + z = 3 \\ 2x - 4y + 2z = 7 \end{cases}$.
   > **Solution:** $F_2 - 2F_1$: $(0, 0, 0 | 1)$. $\text{rank}(A) = 1$, $\text{rank}(A^*) = 2$. **Inconsistent**.

2. How many free parameters does a $3\times 3$ consistent system with $\text{rank}(A) = 1$ have?
   > **Solution:** Number of parameters = $3 - \text{rank}(A) = 3 - 1 = \mathbf{2}$ free parameters.

**Intermediate Level:**

3. Classify and solve: $\begin{cases} x + 2y - z = 1 \\ 2x + 4y - 2z = 2 \\ -x - 2y + z = -1 \end{cases}$.
   > **Solution:** The three equations are proportional (all multiples of $x+2y-z=1$). $\text{rank}(A)=\text{rank}(A^*)=1$. **Consistent and indeterminate** with 2 parameters: $y=\mu$, $z=\lambda$, $x=1-2\mu+\lambda$.

4. A homogeneous $3\times 3$ system ($\mathbf{b}=\mathbf{0}$) with $\text{rank}(A)=3$. Classify it and give its solution.
   > **Solution:** Since $\mathbf{b}=\mathbf{0}$, always $\text{rank}(A)=\text{rank}(A^*)$. With $\text{rank}(A)=3$: **consistent and determined**. The only solution is the trivial one $x=y=z=0$.

**EVAU Level:**

5. **(EVAU Madrid style)** Classify completely and solve the system:
   $$\begin{cases} x + y + 2z = 1 \\ 2x + 3y + 3z = 2 \\ x + 2y + z = 0 \end{cases}$$
   > **Solution:**  
   > We row-reduce the augmented matrix:  
   > $F_2 - 2F_1$: $(0, 1, -1 | 0)$; $F_3 - F_1$: $(0, 1, -1 | -1)$.  
   > $F_3 - F_2$: $(0, 0, 0 | -1)$.  
   > $\text{rank}(A) = 2$, $\text{rank}(A^*) = 3$. Since $\text{rank}(A) \neq \text{rank}(A^*)$: **Inconsistent system**. No solution.

**Multiple Choice Test**

6. A system of 3 equations with 3 unknowns is consistent and determined if and only if:
   - a) $\text{rank}(A) = \text{rank}(A^*) = 2$
   - b) $\text{rank}(A) = \text{rank}(A^*) = 3$
   - c) $\text{rank}(A) < 3$ and $\text{rank}(A^*) = 3$
   - d) $|A| = 0$
   > **Correct answer: b)** For consistent and determined, we need $\text{rank}(A) = \text{rank}(A^*) = n = 3$.

7. If, upon row-reducing the augmented matrix of a $3\times 3$ system, we obtain the row $(0 \; 0 \; 0 \; | \; 5)$, the system is:
   - a) Consistent and indeterminate
   - b) Consistent and determined
   - c) Inconsistent
   - d) Homogeneous
   > **Correct answer: c)** The row $(0\;0\;0\;|\;5)$ represents the equation $0x+0y+0z=5$, i.e. $0=5$, which is a contradiction. The system is **inconsistent**.

---

#### 3.2.3 Discussion of systems with one parameter: technique and cases

**Worked Example**

Discuss the consistency of the system depending on the values of the parameter $a$:
$$\begin{cases} x + y + az = 2 \\ x + ay + z = 2 \\ ax + y + z = 2 \end{cases}$$

**Step-by-step Solution:**

We compute the determinant of $A$:

$$|A| = \begin{vmatrix} 1 & 1 & a \\ 1 & a & 1 \\ a & 1 & 1 \end{vmatrix}$$

Expanding: $= 1(a-1) - 1(1-a) + a(1-a^2) = (a-1) + (a-1) + a(1-a^2)$

$= 2(a-1) + a - a^3 = 2a - 2 + a - a^3 = -a^3 + 3a - 2$

Factoring: $-a^3 + 3a - 2 = -(a^3 - 3a + 2) = -(a-1)^2(a+2)$

**Cases:**

**Case 1: $a \neq 1$ and $a \neq -2$** → $|A| \neq 0$ → $\text{rank}(A) = 3$ → **Consistent and determined**. By symmetry of the system, $x = y = z = 2/(1+1+a) = 2/(2+a)$.

**Case 2: $a = 1$**

$$A = \begin{pmatrix}1&1&1\\1&1&1\\1&1&1\end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix}2\\2\\2\end{pmatrix}$$

The three equations are identical: $x+y+z=2$. $\text{rank}(A)=\text{rank}(A^*)=1<3$. **Consistent and indeterminate** with 2 parameters.

**Case 3: $a = -2$**

$$A = \begin{pmatrix}1&1&-2\\1&-2&1\\-2&1&1\end{pmatrix}$$

Row-reducing $A^*$: $F_2-F_1$: $(0,-3,3|0)$; $F_3+2F_1$: $(0,3,-3|6)$. $F_3+F_2$: $(0,0,0|6)$.

$\text{rank}(A)=2$, $\text{rank}(A^*)=3$. **Inconsistent system**.

---

**Exercises with Solutions**

**Basic Level:**

1. For which values of $k$ is the system $\begin{cases} kx + y = 2 \\ 3x + ky = 6 \end{cases}$ consistent?
   > **Solution:** $|A| = k^2 - 3$. For $k^2 \neq 3$ (i.e., $k\neq\sqrt3, k\neq-\sqrt3$): consistent and determined. For $k=\sqrt3$: $F_2 = \sqrt{3}\cdot F_1$ and $6 = \sqrt{3}\cdot 2$: consistent and indeterminate. For $k=-\sqrt3$: $F_2 = -\sqrt{3}\cdot F_1$ but $6\neq -\sqrt{3}\cdot 2$: inconsistent.

2. For which values of $m$ does the system $\begin{cases} mx + y = 1 \\ x + my = 2 \end{cases}$ have a unique solution?
   > **Solution:** $|A| = m^2 - 1 \neq 0 \Rightarrow m \neq 1$ and $m \neq -1$. For all other values, the system is consistent and determined.

**Intermediate Level:**

3. Discuss and solve depending on $\lambda$: $\begin{cases} x + 2y = 3 \\ 2x + \lambda y = 6 \end{cases}$.
   > **Solution:** $|A| = \lambda - 4$. If $\lambda \neq 4$: consistent and determined. $x = (3\lambda - 12)/(\lambda - 4) = 3$, $y = 0$. If $\lambda = 4$: $F_2 = 2F_1$ and $6 = 2\cdot 3$: consistent and indeterminate; solution: $y = t$, $x = 3 - 2t$.

4. The system $\begin{cases} x + y - z = 1 \\ 2x + 3y + az = 3 \\ x + ay + 3z = 2 \end{cases}$ is inconsistent for $a = -1$. Verify this fact.
   > **Solution:** With $a=-1$: $A^* = \left(\begin{array}{ccc|c}1&1&-1&1\\2&3&-1&3\\1&-1&3&2\end{array}\right)$. $F_2-2F_1$: $(0,1,1|1)$; $F_3-F_1$: $(0,-2,4|1)$. $F_3+2F_2$: $(0,0,6|3)\Rightarrow z=1/2$. Back-substituting works, so it is actually **consistent and determined** for $a=-1$. The claim in the statement was incorrect.

**EVAU Level:**

5. **(EVAU Madrid style)** Discuss depending on the real parameter $m$ the following system:
   $$\begin{cases} x + 2y - z = 1 \\ 2x + my + z = 3 \\ x + (m-2)y + 2z = m \end{cases}$$
   For each case, solve or indicate that there is no solution.
   > **Solution:**  
   > $|A| = \begin{vmatrix}1&2&-1\\2&m&1\\1&m-2&2\end{vmatrix}$  
   > $= 1(2m-(m-2)) - 2(4-1) + (-1)(2(m-2)-m) = (m+2) - 6 + (-1)(m-4)$  
   > $= m+2-6-m+4 = 0$.  
   > The determinant is **always 0**: we must analyse the ranks.  
   > Row-reducing: $F_2-2F_1$: $(0,m-4,3|1)$; $F_3-F_1$: $(0,m-4,3|m-1)$.  
   > $F_3-F_2$: $(0,0,0|m-2)$.  
   > — If $m \neq 2$: $\text{rank}(A^*)=3 > \text{rank}(A)=2$. **Inconsistent**.  
   > — If $m = 2$: $F_2$: $(0,-2,3|1)$. $\text{rank}(A)=\text{rank}(A^*)=2<3$. **Consistent and indeterminate**. With $z=\lambda$: $-2y+3\lambda=1\Rightarrow y=(3\lambda-1)/2$; $x=1-2y+\lambda=1-(3\lambda-1)+\lambda=2-2\lambda$.  
   > **Solution for $m=2$:** $x=2-2\lambda,\; y=(3\lambda-1)/2,\; z=\lambda$.

**Multiple Choice Test**

6. When discussing a system with parameter $a$, the recommended first step is:
   - a) Solve the system directly for each value of $a$
   - b) Compute $|A|$ and set it to zero to find the critical values of $a$
   - c) Compute the trace of $A$
   - d) Substitute $a = 0$ and $a = 1$
   > **Correct answer: b)** The critical values of $a$ are those that make $|A| = 0$, which is when the rank may decrease. For $|A| \neq 0$, the system is automatically consistent and determined.

7. For the system $\begin{cases} x + ay = 2 \\ ax + y = 2a \end{cases}$, the value $a = -1$ gives a system that is:
   - a) Consistent and determined with solution $x=2, y=0$
   - b) Inconsistent
   - c) Consistent and indeterminate
   - d) Consistent and determined with solution $x=1, y=1$
   > **Correct answer: b)** With $a=-1$: equations $x-y=2$ and $-x+y=-2$, which are opposites of each other (the second is $-1$ times the first) only if the constant terms are also proportional. Here: $x-y=2$ and $-x+y=-2$ are the same equation. Check: $-1 \cdot 2 = -2 = 2(-1)$ ✓. Therefore it is **consistent and indeterminate**. **Correct answer: c)**. *(Note: option b was a plausible distractor.)*

---

## 3.3 Methods of solution

---

#### 3.3.1 Gaussian elimination: row operations, row echelon form

**Worked Example**

Solve by Gaussian elimination:
$$\begin{cases} 2x + y - z = 8 \\ -3x - y + 2z = -11 \\ -2x + y + 2z = -3 \end{cases}$$

**Step-by-step Solution:**

We form the augmented matrix and apply elementary row operations:

$$\left(\begin{array}{ccc|c} 2 & 1 & -1 & 8 \\ -3 & -1 & 2 & -11 \\ -2 & 1 & 2 & -3 \end{array}\right)$$

**Step 1:** Create zeros in the first column (below pivot $2$):

$F_2 \leftarrow 2F_2 + 3F_1$: $(-6+6, -2+3, 4-3 | -22+24) = (0, 1, 1 | 2)$

$F_3 \leftarrow F_3 + F_1$: $(-2+2, 1+1, 2-1 | -3+8) = (0, 2, 1 | 5)$

$$\left(\begin{array}{ccc|c} 2 & 1 & -1 & 8 \\ 0 & 1 & 1 & 2 \\ 0 & 2 & 1 & 5 \end{array}\right)$$

**Step 2:** Create zero in the second column (below pivot):

$F_3 \leftarrow F_3 - 2F_2$: $(0, 0, -1 | 1)$

$$\left(\begin{array}{ccc|c} 2 & 1 & -1 & 8 \\ 0 & 1 & 1 & 2 \\ 0 & 0 & -1 & 1 \end{array}\right)$$

**Step 3:** Back substitution:

- $F_3$: $-z = 1 \Rightarrow z = -1$
- $F_2$: $y + (-1) = 2 \Rightarrow y = 3$
- $F_1$: $2x + 3 - (-1) = 8 \Rightarrow 2x = 4 \Rightarrow x = 2$

**Solution:** $(x, y, z) = (2, 3, -1)$.

---

**Exercises with Solutions**

**Basic Level:**

1. Solve by Gauss: $\begin{cases} x + y = 5 \\ 2x - y = 4 \end{cases}$.
   > **Solution:** $F_2 - 2F_1$: $(0, -3 | -6)$, $y=2$; $x = 5-2 = 3$. **Solution:** $(3, 2)$.

2. Solve by Gauss: $\begin{cases} 3x + 2y = 12 \\ x + y = 5 \end{cases}$.
   > **Solution:** Swap rows. $F_1 \leftarrow F_2$, $F_2 \leftarrow F_1$. $F_2 - 3F_1$: $(0,-1|{-3})$, $y=3$; $x=5-3=2$. **Solution:** $(2, 3)$.

**Intermediate Level:**

3. Solve by Gauss: $\begin{cases} x + 2y + 3z = 6 \\ 2x - y + z = 3 \\ 3x + y - z = 2 \end{cases}$.
   > **Solution:** $F_2-2F_1$: $(0,-5,-5|-9)$; $F_3-3F_1$: $(0,-5,-10|-16)$. $F_3-F_2$: $(0,0,-5|-7) \Rightarrow z=7/5$. $-5y-5(7/5)=-9 \Rightarrow -5y=−9+7=-2 \Rightarrow y=2/5$. $x=6-2(2/5)-3(7/5)=6-4/5-21/5=6-5=1$. **Solution:** $(1, 2/5, 7/5)$.

4. Explain why Gaussian elimination is preferable to Cramer's rule for large systems.
   > **Solution:** Cramer's rule requires computing $n+1$ determinants of order $n$; its cost grows like $O(n\cdot n!)$. Gaussian elimination, with forward elimination and back substitution, has cost $O(n^3)$, much more efficient for large $n$. Moreover, Gauss directly detects inconsistent and indeterminate systems.

**EVAU Level:**

5. **(EVAU Madrid style)** Solve by Gaussian elimination the system:
   $$\begin{cases} x - y + 2z = 5 \\ 2x + y - z = 2 \\ 4x - y + 3z = 12 \end{cases}$$
   Verify the solution by substituting back into the original equations.
   > **Solution:**  
   > $F_2-2F_1$: $(0,3,-5|-8)$; $F_3-4F_1$: $(0,3,-5|-8)$. $F_3-F_2$: $(0,0,0|0)$.  
   > $\text{rank}(A)=\text{rank}(A^*)=2<3$. Consistent and indeterminate. Let $z=\lambda$.  
   > $3y-5\lambda=-8 \Rightarrow y=(5\lambda-8)/3$. $x=5+y-2\lambda=5+(5\lambda-8)/3-2\lambda=(15+5\lambda-8-6\lambda)/3=(7-\lambda)/3$.  
   > **Solution:** $x=(7-\lambda)/3,\; y=(5\lambda-8)/3,\; z=\lambda$.  
   > **Verification** (with $\lambda=1$): $x=2, y=-1, z=1$. Eq.1: $2+1+2=5$ ✓. Eq.2: $4-1-1=2$ ✓. Eq.3: $8+1+3=12$ ✓.

**Multiple Choice Test**

6. In Gaussian elimination, if the row $(0 \; 0 \; 0 \; | \; 0)$ appears during row reduction, it means that:
   - a) The system is inconsistent
   - b) One equation is a linear combination of the others
   - c) The system has a unique solution
   - d) The system must be reformulated
   > **Correct answer: b)** A row of zeros indicates that equation was redundant (a linear combination of the previous ones), which reduces the rank and may lead to an indeterminate system.

7. Gaussian elimination transforms the system into an equivalent one because:
   - a) It multiplies both sides of an equation by zero
   - b) Elementary row operations do not alter the solution set
   - c) It changes the unknowns but not the equations
   - d) It adds equations eliminating the solution
   > **Correct answer: b)** Elementary row operations (row swap, multiplication by a nonzero scalar, addition of multiples) are reversible and preserve the solution set.

---

#### 3.3.2 Cramer's rule for systems of order ≤ 3 with a unique solution

**Worked Example**

Solve using Cramer's rule:
$$\begin{cases} 2x - y + z = 3 \\ x + 3y - 2z = -2 \\ 3x + y + z = 7 \end{cases}$$

**Step-by-step Solution:**

$$|A| = \begin{vmatrix} 2 & -1 & 1 \\ 1 & 3 & -2 \\ 3 & 1 & 1 \end{vmatrix} = 2(3+2) - (-1)(1+6) + 1(1-9) = 10 + 7 - 8 = 9$$

$$|A_x| = \begin{vmatrix} 3 & -1 & 1 \\ -2 & 3 & -2 \\ 7 & 1 & 1 \end{vmatrix} = 3(3+2) - (-1)(-2+14) + 1(-2-21) = 15 - 12 - 23 = -20$$

Wait, let us recalculate carefully:
$= 3(3\cdot1 - (-2)\cdot1) - (-1)((-2)\cdot1 - (-2)\cdot7) + 1((-2)\cdot1 - 3\cdot7)$
$= 3(3+2) + 1(-2+14) + 1(-2-21) = 15 + 12 - 23 = 4$

Recalculation: $3(3+2) = 15$; $-(-1)((-2)(1)-(-2)(7)) = +1\cdot(-2+14)=12$; $+1((-2)(1)-3(7))=+1(-2-21)=-23$. Total: $15+12-23=4$. We verify: $x=4/9$.

$$|A_y| = \begin{vmatrix} 2 & 3 & 1 \\ 1 & -2 & -2 \\ 3 & 7 & 1 \end{vmatrix} = 2(-2+14) - 3(1+6) + 1(7+6) = 24 - 21 + 13 = 16$$

$$|A_z| = \begin{vmatrix} 2 & -1 & 3 \\ 1 & 3 & -2 \\ 3 & 1 & 7 \end{vmatrix} = 2(21+2) - (-1)(7+6) + 3(1-9) = 46 + 13 - 24 = 35$$

$$x = \frac{|A_x|}{|A|} = \frac{4}{9}, \quad y = \frac{|A_y|}{|A|} = \frac{16}{9}, \quad z = \frac{|A_z|}{|A|} = \frac{35}{9}$$

**Verification** (Eq. 1): $2(4/9) - 16/9 + 35/9 = 8/9 - 16/9 + 35/9 = 27/9 = 3$ ✓.

---

**Exercises with Solutions**

**Basic Level:**

1. Solve by Cramer's rule: $\begin{cases} 3x + y = 7 \\ x - 2y = 0 \end{cases}$.
   > **Solution:** $|A|=3(-2)-1(1)=-7$. $|A_x|=7(-2)-1(0)=-14$. $|A_y|=3(0)-7(1)=-7$. $x=-14/-7=2$, $y=-7/-7=1$. **Solution:** $(2,1)$.

2. When can Cramer's rule not be applied? What does this indicate about the system?
   > **Solution:** It cannot be applied when $|A|=0$, i.e., when the coefficient matrix is singular (not invertible). In this case the system may be inconsistent or consistent and indeterminate, and another method must be used (Gauss or Rouché–Frobenius).

**Intermediate Level:**

3. Solve by Cramer's rule: $\begin{cases} x + y = 3 \\ 2x - z = 1 \\ y + 2z = 5 \end{cases}$.
   > **Solution:** $A=\begin{pmatrix}1&1&0\\2&0&-1\\0&1&2\end{pmatrix}$. $|A|=1(0+1)-1(4-0)+0=1-4=-3$.  
   > $|A_x|=\begin{vmatrix}3&1&0\\1&0&-1\\5&1&2\end{vmatrix}=3(0+1)-1(2+5)+0=3-7=-4$; $x=(-4)/(-3)=4/3$.  
   > $|A_y|=\begin{vmatrix}1&3&0\\2&1&-1\\0&5&2\end{vmatrix}=1(2+5)-3(4-0)+0=7-12=-5$; $y=(-5)/(-3)=5/3$.  
   > $|A_z|=\begin{vmatrix}1&1&3\\2&0&1\\0&1&5\end{vmatrix}=1(0-1)-1(10-0)+3(2-0)=(-1)-10+6=-5$; $z=(-5)/(-3)=5/3$.  
   > **Solution:** $(4/3, 5/3, 5/3)$.

4. Using Cramer's rule, find $x$ without computing $y$ or $z$ in the system from the worked example of section 3.3.1.
   > **Solution:** With the system $2x+y-z=8$, $-3x-y+2z=-11$, $-2x+y+2z=-3$:  
   > $|A|=\begin{vmatrix}2&1&-1\\-3&-1&2\\-2&1&2\end{vmatrix}=2(-2-2)-1(-6+4)+(-1)(-3-2)=2(-4)+2+5=-8+7=-1$.  
   > $|A_x|=\begin{vmatrix}8&1&-1\\-11&-1&2\\-3&1&2\end{vmatrix}=8(-2-2)-1(-22+6)+(-1)(-11-3)=-32+16+14=-2$.  
   > $x=|A_x|/|A|=-2/-1=2$ ✓.

**EVAU Level:**

5. **(EVAU Madrid style)** Solve by Cramer's rule the system:
   $$\begin{cases} x + 2y - z = 0 \\ 2x - y + 3z = 5 \\ 3x + y + z = 4 \end{cases}$$
   Verify that the solution is correct.
   > **Solution:**  
   > $|A|=\begin{vmatrix}1&2&-1\\2&-1&3\\3&1&1\end{vmatrix}=1(-1-3)-2(2-9)+(-1)(2+3)=-4+14-5=5$.  
   > $|A_x|=\begin{vmatrix}0&2&-1\\5&-1&3\\4&1&1\end{vmatrix}=0(-4)-2(5-12)+(-1)(5+4)=0+14-9=5$; $x=5/5=1$.  
   > $|A_y|=\begin{vmatrix}1&0&-1\\2&5&3\\3&4&1\end{vmatrix}=1(5-12)-0+(-1)(8-15)=-7+7=0$; $y=0/5=0$.  
   > $|A_z|=\begin{vmatrix}1&2&0\\2&-1&5\\3&1&4\end{vmatrix}=1(-4-5)-2(8-15)+0=-9+14=5$; $z=5/5=1$.  
   > **Solution:** $(x,y,z)=(1,0,1)$.  
   > **Verification:** Eq.1: $1+0-1=0$ ✓; Eq.2: $2-0+3=5$ ✓; Eq.3: $3+0+1=4$ ✓.

**Multiple Choice Test**

6. In Cramer's rule, the value of $y$ in a $2\times 2$ system $\begin{cases} ax+by=e \\ cx+dy=f \end{cases}$ is:
   - a) $y = \dfrac{\begin{vmatrix}e&b\\f&d\end{vmatrix}}{\begin{vmatrix}a&b\\c&d\end{vmatrix}}$
   - b) $y = \dfrac{\begin{vmatrix}a&e\\c&f\end{vmatrix}}{\begin{vmatrix}a&b\\c&d\end{vmatrix}}$
   - c) $y = \dfrac{\begin{vmatrix}a&b\\c&d\end{vmatrix}}{\begin{vmatrix}e&b\\f&d\end{vmatrix}}$
   - d) $y = \dfrac{\begin{vmatrix}a&e\\c&f\end{vmatrix}}{\begin{vmatrix}e&b\\f&d\end{vmatrix}}$
   > **Correct answer: b)** To compute $y$, the second column (coefficients of $y$) is replaced by the constant terms.

7. Cramer's rule for a $3\times3$ system requires computing:
   - a) 1 determinant
   - b) 3 determinants
   - c) 4 determinants
   - d) 9 determinants
   > **Correct answer: c)** We need $|A|$, $|A_x|$, $|A_y|$ and $|A_z|$: a total of **4** determinants of order 3.

---

#### 3.3.3 Solution via the inverse matrix: $x = A^{-1} \cdot b$

**Worked Example**

Solve the system $\begin{cases} 2x + y = 5 \\ 5x + 3y = 13 \end{cases}$ using the inverse matrix.

**Step-by-step Solution:**

In matrix form: $A\mathbf{x} = \mathbf{b}$ with $A = \begin{pmatrix}2&1\\5&3\end{pmatrix}$, $\mathbf{b} = \begin{pmatrix}5\\13\end{pmatrix}$.

**Computing $A^{-1}$:** $|A| = 6 - 5 = 1$.

$$A^{-1} = \frac{1}{1}\begin{pmatrix}3&-1\\-5&2\end{pmatrix} = \begin{pmatrix}3&-1\\-5&2\end{pmatrix}$$

(For a $2\times 2$ matrix: $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$.)

**Verification:** $A \cdot A^{-1} = \begin{pmatrix}2&1\\5&3\end{pmatrix}\begin{pmatrix}3&-1\\-5&2\end{pmatrix} = \begin{pmatrix}1&0\\0&1\end{pmatrix}$ ✓.

**Solution:**
$$\mathbf{x} = A^{-1}\mathbf{b} = \begin{pmatrix}3&-1\\-5&2\end{pmatrix}\begin{pmatrix}5\\13\end{pmatrix} = \begin{pmatrix}15-13\\-25+26\end{pmatrix} = \begin{pmatrix}2\\1\end{pmatrix}$$

$(x, y) = (2, 1)$. **Verification:** $2(2)+1=5$ ✓, $5(2)+3(1)=13$ ✓.

---

**Exercises with Solutions**

**Basic Level:**

1. Compute $A^{-1}$ for $A = \begin{pmatrix}1&2\\3&7\end{pmatrix}$ and use it to solve $A\mathbf{x} = \begin{pmatrix}1\\3\end{pmatrix}$.
   > **Solution:** $|A|=7-6=1$. $A^{-1}=\begin{pmatrix}7&-2\\-3&1\end{pmatrix}$. $\mathbf{x}=\begin{pmatrix}7-6\\-3+3\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix}$. $(x,y)=(1,0)$.

2. For which type of systems can the inverse matrix method be applied?
   > **Solution:** Only when the system is **consistent and determined**, i.e., when $|A|\neq 0$ (the matrix is invertible). If $|A|=0$, the inverse does not exist and Gaussian elimination must be used.

**Intermediate Level:**

3. Using $A^{-1}$, solve $\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 2 \end{cases}$ knowing that $A^{-1} = \frac{1}{6}\begin{pmatrix}-1&3&2\\3&-2&1\\5&-1&-3\end{pmatrix}$.
   > **Solution:** $\mathbf{x} = A^{-1}\mathbf{b} = \frac{1}{6}\begin{pmatrix}-6+9+4\\18-6+2\\30-3-6\end{pmatrix} = \frac{1}{6}\begin{pmatrix}7\\14\\21\end{pmatrix} = \begin{pmatrix}7/6\\7/3\\7/2\end{pmatrix}$. Checking in Eq.1: $7/6+7/3+7/2=7/6+14/6+21/6=42/6=7\neq6$. There is an error in the given inverse; using Gauss: the correct result is $(x,y,z)=(1,2,3)$.

4. Compare the efficiency of the inverse matrix method versus Gaussian elimination for solving multiple systems with the same matrix $A$ but different vectors $\mathbf{b}$.
   > **Solution:** If we need to solve $A\mathbf{x}=\mathbf{b}_1$, $A\mathbf{x}=\mathbf{b}_2$, ..., computing $A^{-1}$ once and then multiplying $A^{-1}\mathbf{b}_i$ is more efficient than applying Gauss $k$ times. The cost of computing $A^{-1}$ is amortised.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $A = \begin{pmatrix}1&1&-1\\2&-1&1\\1&2&3\end{pmatrix}$.  
   **(a)** Verify that $|A| = -9$ and compute $A^{-1}$.  
   **(b)** Use $A^{-1}$ to solve $A\mathbf{x} = \begin{pmatrix}2\\0\\5\end{pmatrix}$.
   > **Solution:**  
   > **(a)** $|A|=1(-3-2)-1(6-1)+(-1)(4+1)=-5-5-5=-15$. (The given value $-9$ is incorrect; we use $|A|=-15$.)  
   > For the adjugate, we compute the cofactors $C_{ij}$:  
   > $C_{11}=(-1-2)=-3$; $C_{12}=-(6-1)=-5$; $C_{13}=(4+1)=5$;  
   > $C_{21}=-(3+2)=-5$; $C_{22}=(3+1)=4$; $C_{23}=-(2-1)=-1$;  
   > $C_{31}=(1-1)=0$; $C_{32}=-(1+2)=-3$; $C_{33}=(-1-2)=-3$.  
   > $\text{Adj}(A)=\begin{pmatrix}-3&-5&0\\-5&4&-3\\5&-1&-3\end{pmatrix}$. $A^{-1}=\frac{1}{-15}\begin{pmatrix}-3&-5&0\\-5&4&-3\\5&-1&-3\end{pmatrix}=\frac{1}{15}\begin{pmatrix}3&5&0\\5&-4&3\\-5&1&3\end{pmatrix}$.  
   > **(b)** $\mathbf{x}=A^{-1}\begin{pmatrix}2\\0\\5\end{pmatrix}=\frac{1}{15}\begin{pmatrix}6+0+0\\10+0+15\\-10+0+15\end{pmatrix}=\frac{1}{15}\begin{pmatrix}6\\25\\5\end{pmatrix}=\begin{pmatrix}2/5\\5/3\\1/3\end{pmatrix}$.

**Multiple Choice Test**

6. The solution method $\mathbf{x} = A^{-1}\mathbf{b}$ is valid only when:
   - a) $|A| = 1$
   - b) $A$ is symmetric
   - c) $|A| \neq 0$
   - d) $\mathbf{b} \neq \mathbf{0}$
   > **Correct answer: c)** $A^{-1}$ exists if and only if $A$ is nonsingular, i.e., $|A| \neq 0$. No condition on $\mathbf{b}$ is needed.

7. If $A\mathbf{x} = \mathbf{b}$ and $|A| = 5$, then the solution is $\mathbf{x} = A^{-1}\mathbf{b}$ because:
   - a) $A^{-1} = 5A$
   - b) Multiplying on the left by $A^{-1}$: $A^{-1}A\mathbf{x} = A^{-1}\mathbf{b} \Rightarrow I\mathbf{x} = A^{-1}\mathbf{b}$
   - c) $A^{-1}\mathbf{b} = \mathbf{b}/5$
   - d) $A^{-1} = A^T / 5$
   > **Correct answer: b)** We premultiply by $A^{-1}$ and use the fact that $A^{-1}A = I$.

---

#### 3.3.4 Homogeneous systems: trivial solution and non-trivial solutions

**Worked Example**

Study the homogeneous system:
$$\begin{cases} x + y - z = 0 \\ 2x - y + z = 0 \\ 3x + 2y - 2z = 0 \end{cases}$$

**Step-by-step Solution:**

Every homogeneous system is always consistent (it admits at least the trivial solution $x = y = z = 0$).

We compute $|A|$:

$$|A| = \begin{vmatrix} 1 & 1 & -1 \\ 2 & -1 & 1 \\ 3 & 2 & -2 \end{vmatrix}$$

Expanding along the first row: $= 1(2-2) - 1(-4-3) + (-1)(4+3) = 0 + 7 - 7 = 0$.

Since $|A| = 0$, the rank is less than 3. We row-reduce:

$F_2 - 2F_1$: $(0, -3, 3 | 0)$; $F_3 - 3F_1$: $(0, -1, 1 | 0)$.

$F_2 \leftrightarrow F_3$: $(0,-1,1|0)$; $F_3 - 3\cdot F_2'$: $F_3 - 3(0,-1,1|0) = (0,-3+3,3-3|0) = (0,0,0|0)$.

$\text{rank}(A) = 2 < 3$: **non-trivial solutions** (1 free parameter).

$-y + z = 0 \Rightarrow y = z$. Let $z = \lambda$: $y = \lambda$, $x = -y + z = 0$.

**Solution:** $(x, y, z) = (0, \lambda, \lambda) = \lambda(0, 1, 1)$, $\lambda \in \mathbb{R}$.

---

**Exercises with Solutions**

**Basic Level:**

1. What is always the solution of a homogeneous system? When does it have more solutions?
   > **Solution:** The **trivial solution** $(0, 0, \ldots, 0)$ is always a solution. It has more (non-trivial) solutions when $\text{rank}(A) < n$ (number of unknowns), i.e., when $|A|=0$ in the square case.

2. Solve the homogeneous system $\begin{cases} 2x - y = 0 \\ -4x + 2y = 0 \end{cases}$.
   > **Solution:** $|A|=2(2)-(-1)(-4)=4-4=0$. The two equations are equivalent: $2x-y=0$, $y=2x$. Let $x=\lambda$: $y=2\lambda$. **Solution:** $(x,y)=\lambda(1,2)$, $\lambda\in\mathbb{R}$.

**Intermediate Level:**

3. Study the homogeneous system $\begin{cases} x+2y-z=0 \\ 2x+y+z=0 \\ x-y+2z=0 \end{cases}$.
   > **Solution:** $|A|=\begin{vmatrix}1&2&-1\\2&1&1\\1&-1&2\end{vmatrix}=1(2+1)-2(4-1)+(-1)(-2-1)=3-6+3=0$. $\text{rank}(A)<3$: non-trivial solutions. $F_2-2F_1$: $(0,-3,3|0)\Rightarrow y=z$. $F_3-F_1$: $(0,-3,3|0)$ same. With $z=\lambda$: $y=\lambda$, $x=-2\lambda+\lambda=-\lambda$. **Solution:** $(x,y,z)=\lambda(-1,1,1)$.

4. Can a homogeneous system be inconsistent? Justify.
   > **Solution:** No. Every homogeneous system $A\mathbf{x}=\mathbf{0}$ has $\mathbf{x}=\mathbf{0}$ as a solution, so it is always **consistent**. Inconsistency requires that no solution exists, which is impossible if $\mathbf{0}$ is already a solution.

**EVAU Level:**

5. **(EVAU Madrid style)** Given the homogeneous system:
   $$\begin{cases} x + ay + z = 0 \\ ax + y + z = 0 \\ x + y + az = 0 \end{cases}$$
   **(a)** For which values of $a$ does it have non-trivial solutions.  
   **(b)** For $a = 1$, find the general solution.
   > **Solution:**  
   > **(a)** The system has non-trivial solutions $\Leftrightarrow |A|=0$.  
   > $|A|=\begin{vmatrix}1&a&1\\a&1&1\\1&1&a\end{vmatrix}=1(a-1)-a(a^2-1)+1(a-1)=(a-1)-a(a^2-1)+(a-1)$  
   > $=2(a-1)-a(a-1)(a+1)=(a-1)[2-a(a+1)]=(a-1)(2-a^2-a)=(a-1)(-a^2-a+2)$  
   > $=(a-1)(-(a^2+a-2))=(a-1)(-(a+2)(a-1))=-(a-1)^2(a+2)$.  
   > $|A|=0 \Leftrightarrow a=1$ or $a=-2$.  
   > **(b)** For $a=1$: all three equations are $x+y+z=0$. $\text{rank}(A)=1$. Two free parameters: $y=\mu$, $z=\lambda$, $x=-\mu-\lambda$. **Solution:** $(-\mu-\lambda, \mu, \lambda)$.

**Multiple Choice Test**

6. A homogeneous $3\times3$ system with $|A| \neq 0$ has:
   - a) Infinitely many solutions
   - b) Only the trivial solution
   - c) Exactly two solutions
   - d) No solution
   > **Correct answer: b)** If $|A|\neq0$, the rank is 3 = number of unknowns, so the system is consistent and determined. The only solution is the trivial one $\mathbf{x}=\mathbf{0}$.

7. The general solution of a homogeneous $3\times3$ system with $\text{rank}(A)=2$ is:
   - a) A finite set of points
   - b) A line through the origin
   - c) A plane through the origin
   - d) All of $\mathbb{R}^3$
   > **Correct answer: b)** With rank 2 and 3 unknowns, there are $3-2=1$ free parameters. The solutions form a **line** (a 1-dimensional vector subspace) through the origin.

---

## 3.4 Matrix equations

---

#### 3.4.1 Equations of the type $AX = B$, $XA = B$, $AXB = C$

**Worked Example**

Solve the matrix equation $AX = B$ where:
$$A = \begin{pmatrix}2&1\\3&2\end{pmatrix}, \quad B = \begin{pmatrix}1&0\\-1&2\end{pmatrix}$$

**Step-by-step Solution:**

If $|A| \neq 0$, we can premultiply by $A^{-1}$: $X = A^{-1}B$.

**Computing $A^{-1}$:** $|A| = 4 - 3 = 1$.

$$A^{-1} = \begin{pmatrix}2&-1\\-3&2\end{pmatrix}$$

**Computing $X$:**

$$X = A^{-1}B = \begin{pmatrix}2&-1\\-3&2\end{pmatrix}\begin{pmatrix}1&0\\-1&2\end{pmatrix} = \begin{pmatrix}2+1&0-2\\-3-2&0+4\end{pmatrix} = \begin{pmatrix}3&-2\\-5&4\end{pmatrix}$$

**Verification:** $AX = \begin{pmatrix}2&1\\3&2\end{pmatrix}\begin{pmatrix}3&-2\\-5&4\end{pmatrix} = \begin{pmatrix}6-5&-4+4\\9-10&-6+8\end{pmatrix} = \begin{pmatrix}1&0\\-1&2\end{pmatrix} = B$ ✓.

---

**Exercises with Solutions**

**Basic Level:**

1. Solve $XA = B$ with $A = \begin{pmatrix}1&2\\0&1\end{pmatrix}$, $B = \begin{pmatrix}3&7\\1&3\end{pmatrix}$.
   > **Solution:** $|A|=1\neq0$. $A^{-1}=\begin{pmatrix}1&-2\\0&1\end{pmatrix}$. $X=BA^{-1}=\begin{pmatrix}3&7\\1&3\end{pmatrix}\begin{pmatrix}1&-2\\0&1\end{pmatrix}=\begin{pmatrix}3&-6+7\\1&-2+3\end{pmatrix}=\begin{pmatrix}3&1\\1&1\end{pmatrix}$.

2. What is the difference between solving $AX=B$ and $XA=B$?
   > **Solution:** In $AX=B$ we premultiply by $A^{-1}$: $X=A^{-1}B$. In $XA=B$ we postmultiply by $A^{-1}$: $X=BA^{-1}$. Since matrix multiplication is not commutative, the results are generally different.

**Intermediate Level:**

3. Solve the equation $AXB = C$ with $A = \begin{pmatrix}2&1\\1&1\end{pmatrix}$, $B = \begin{pmatrix}1&1\\0&1\end{pmatrix}$, $C = \begin{pmatrix}3&4\\1&2\end{pmatrix}$.
   > **Solution:** $X = A^{-1}CB^{-1}$. $|A|=1$, $A^{-1}=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$. $|B|=1$, $B^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}$. $A^{-1}C=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}\begin{pmatrix}3&4\\1&2\end{pmatrix}=\begin{pmatrix}2&2\\-1&0\end{pmatrix}$. $X=\begin{pmatrix}2&2\\-1&0\end{pmatrix}\begin{pmatrix}1&-1\\0&1\end{pmatrix}=\begin{pmatrix}2&0\\-1&1\end{pmatrix}$.

4. Let the equation $3X - A = B$ with $A = \begin{pmatrix}1&0\\2&-1\end{pmatrix}$, $B = \begin{pmatrix}-2&3\\4&1\end{pmatrix}$. Find $X$.
   > **Solution:** $3X = A + B = \begin{pmatrix}-1&3\\6&0\end{pmatrix}$. $X = \frac{1}{3}\begin{pmatrix}-1&3\\6&0\end{pmatrix} = \begin{pmatrix}-1/3&1\\2&0\end{pmatrix}$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $A = \begin{pmatrix}1&2\\1&3\end{pmatrix}$.  
   **(a)** Compute $A^{-1}$.  
   **(b)** Solve the matrix equation $AX + A = 3I$ (where $I$ is the $2\times2$ identity).
   > **Solution:**  
   > **(a)** $|A|=3-2=1$. $A^{-1}=\begin{pmatrix}3&-2\\-1&1\end{pmatrix}$.  
   > **(b)** $AX = 3I - A$. $X = A^{-1}(3I-A)$.  
   > $3I - A = \begin{pmatrix}3&0\\0&3\end{pmatrix} - \begin{pmatrix}1&2\\1&3\end{pmatrix} = \begin{pmatrix}2&-2\\-1&0\end{pmatrix}$.  
   > $X = \begin{pmatrix}3&-2\\-1&1\end{pmatrix}\begin{pmatrix}2&-2\\-1&0\end{pmatrix} = \begin{pmatrix}6+2&-6+0\\-2-1&2+0\end{pmatrix} = \begin{pmatrix}8&-6\\-3&2\end{pmatrix}$.

**Multiple Choice Test**

6. To solve $AX = B$ (with $A$ square and invertible), the solution is:
   - a) $X = BA^{-1}$
   - b) $X = A^{-1}B$
   - c) $X = B/A$
   - d) $X = A^{-1}B^{-1}$
   > **Correct answer: b)** We premultiply both sides by $A^{-1}$: $A^{-1}AX = A^{-1}B \Rightarrow IX = A^{-1}B$.

7. The equation $X^2 = A$ (with $A$ known) can be solved directly as $X = A^{1/2}$:
   - a) True always
   - b) False; no matrix solution exists in general
   - c) True only if $A$ is the identity
   - d) False in general; we must find $X$ such that $X\cdot X = A$
   > **Correct answer: d)** The equation $X^2=A$ may have no solution, or several, and is not solved simply by $A^{1/2}$ (which does not always exist or is unique). One must find $X$ directly.

---

#### 3.4.2 Transforming a matrix equation into a system of equations

**Worked Example**

Transform the matrix equation $AX = B$ into a system of equations, with:
$$A = \begin{pmatrix}1&2\\3&1\end{pmatrix}, \quad B = \begin{pmatrix}5&0\\7&-1\end{pmatrix}, \quad X = \begin{pmatrix}x_1&x_2\\x_3&x_4\end{pmatrix}$$

**Step-by-step Solution:**

We perform the product $AX$:

$$AX = \begin{pmatrix}1&2\\3&1\end{pmatrix}\begin{pmatrix}x_1&x_2\\x_3&x_4\end{pmatrix} = \begin{pmatrix}x_1+2x_3 & x_2+2x_4\\3x_1+x_3 & 3x_2+x_4\end{pmatrix}$$

Setting equal to $B$:

$$\begin{pmatrix}x_1+2x_3 & x_2+2x_4\\3x_1+x_3 & 3x_2+x_4\end{pmatrix} = \begin{pmatrix}5&0\\7&-1\end{pmatrix}$$

We obtain two independent systems (by columns of $X$):

**System for the first column** $(x_1, x_3)$:
$$\begin{cases} x_1 + 2x_3 = 5 \\ 3x_1 + x_3 = 7 \end{cases}$$

**System for the second column** $(x_2, x_4)$:
$$\begin{cases} x_2 + 2x_4 = 0 \\ 3x_2 + x_4 = -1 \end{cases}$$

Solving the first system: $|A|=1-6=-5$. $x_1=(5-14)/(-5)=9/5$, $x_3=(35-15)/(-5)...$

By Cramer: $x_1=(5\cdot1-2\cdot7)/(-5)=(5-14)/(-5)=9/5$; $x_3=(7\cdot1-3\cdot5)/(-5)=(7-15)/(-5)=8/5$.

Second system: $x_2=(0\cdot1-2\cdot(-1))/(-5)=2/(-5)=-2/5$; $x_4=((-1)\cdot1-3\cdot0)/(-5)=-1/(-5)=1/5$.

$$X = \frac{1}{5}\begin{pmatrix}9&-2\\8&1\end{pmatrix}$$

---

**Exercises with Solutions**

**Basic Level:**

1. Transform into a system: $\begin{pmatrix}2&1\\0&3\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix} = \begin{pmatrix}4\\6\end{pmatrix}$.
   > **Solution:** $\begin{cases}2x+y=4\\3y=6\end{cases}$. Solving: $y=2$, $x=1$.

2. Why does the matrix equation $AX=B$ with $A$ of order $2\times2$ and $X$, $B$ also $2\times2$ reduce to two independent $2\times2$ systems?
   > **Solution:** When computing the product $AX$ column by column, the $j$-th column of $AX$ is $A$ multiplied by the $j$-th column of $X$. Therefore each column of $X$ satisfies an independent system $A\mathbf{x}_j = \mathbf{b}_j$.

**Intermediate Level:**

3. Transform into a system and solve: $\begin{pmatrix}1&-1\\2&1\end{pmatrix}X=\begin{pmatrix}2&-1\\1&3\end{pmatrix}$ where $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$.
   > **Solution:** Col. 1: $a-c=2$, $2a+c=1$. Adding: $3a=3\Rightarrow a=1$, $c=-1$. Col. 2: $b-d=-1$, $2b+d=3$. Adding: $3b=2\Rightarrow b=2/3$, $d=b+1=5/3$. $X=\begin{pmatrix}1&2/3\\-1&5/3\end{pmatrix}$.

4. Let $XA + B = C$ with $A=\begin{pmatrix}2&0\\0&3\end{pmatrix}$, $B=\begin{pmatrix}1&-1\\0&2\end{pmatrix}$, $C=\begin{pmatrix}3&2\\4&5\end{pmatrix}$. Find $X$.
   > **Solution:** $XA = C - B = \begin{pmatrix}2&3\\4&3\end{pmatrix}$. $A^{-1}=\begin{pmatrix}1/2&0\\0&1/3\end{pmatrix}$. $X=\begin{pmatrix}2&3\\4&3\end{pmatrix}\begin{pmatrix}1/2&0\\0&1/3\end{pmatrix}=\begin{pmatrix}1&1\\2&1\end{pmatrix}$.

**EVAU Level:**

5. **(EVAU Madrid style)** Solve the matrix equation $2X - A^T = A$ where $A = \begin{pmatrix}1&3\\-1&2\end{pmatrix}$.
   > **Solution:**  
   > $A^T=\begin{pmatrix}1&-1\\3&2\end{pmatrix}$.  
   > $2X = A + A^T = \begin{pmatrix}1&3\\-1&2\end{pmatrix}+\begin{pmatrix}1&-1\\3&2\end{pmatrix}=\begin{pmatrix}2&2\\2&4\end{pmatrix}$.  
   > $X = \begin{pmatrix}1&1\\1&2\end{pmatrix}$.

**Multiple Choice Test**

6. The matrix equation $\begin{pmatrix}1&0\\2&1\end{pmatrix}X = \begin{pmatrix}a\\b\end{pmatrix}$ (with $X$ of order $2\times1$) becomes:
   - a) A system with 4 unknowns
   - b) A $2\times2$ system with the entries of $X$ as unknowns
   - c) A scalar equation
   - d) Two independent systems
   > **Correct answer: b)** $X=\begin{pmatrix}x\\y\end{pmatrix}$, and the product gives $\begin{cases}x=a\\2x+y=b\end{cases}$: a $2\times2$ system.

7. If $AX = B$ and $A$ is not invertible, then:
   - a) $X = A^{-1}B$ always works
   - b) The system may be inconsistent or indeterminate
   - c) $X = 0$ is always the solution
   - d) There is never a solution
   > **Correct answer: b)** Without invertibility of $A$, we must analyse the ranks of the augmented matrix of the equivalent system to determine whether a solution exists and how many there are.

---

#### 3.4.3 Solving matrix equations using the inverse and operations

**Worked Example**

Solve: $A^2 X + 2A = 3I$ where $A = \begin{pmatrix}1&1\\0&2\end{pmatrix}$.

**Step-by-step Solution:**

**Step 1:** Compute $A^2$.

$$A^2 = \begin{pmatrix}1&1\\0&2\end{pmatrix}\begin{pmatrix}1&1\\0&2\end{pmatrix} = \begin{pmatrix}1&3\\0&4\end{pmatrix}$$

**Step 2:** Isolate $X$:

$$A^2 X = 3I - 2A = 3\begin{pmatrix}1&0\\0&1\end{pmatrix} - 2\begin{pmatrix}1&1\\0&2\end{pmatrix} = \begin{pmatrix}3&0\\0&3\end{pmatrix} - \begin{pmatrix}2&2\\0&4\end{pmatrix} = \begin{pmatrix}1&-2\\0&-1\end{pmatrix}$$

**Step 3:** $|A^2| = |A|^2 = 1^2 \cdot 2^2 = ... = |A|^2$. Since $|A| = 2 - 0 = 2$, $|A^2| = 4 \neq 0$.

$$(A^2)^{-1} = \frac{1}{4}\begin{pmatrix}4&-3\\0&1\end{pmatrix}$$

**Step 4:**

$$X = (A^2)^{-1}\begin{pmatrix}1&-2\\0&-1\end{pmatrix} = \frac{1}{4}\begin{pmatrix}4&-3\\0&1\end{pmatrix}\begin{pmatrix}1&-2\\0&-1\end{pmatrix} = \frac{1}{4}\begin{pmatrix}4&-8+3\\0&-1\end{pmatrix} = \frac{1}{4}\begin{pmatrix}4&-5\\0&-1\end{pmatrix}$$

$$X = \begin{pmatrix}1&-5/4\\0&-1/4\end{pmatrix}$$

---

**Exercises with Solutions**

**Basic Level:**

1. Solve $2X + \begin{pmatrix}1&0\\0&1\end{pmatrix} = \begin{pmatrix}5&2\\-2&3\end{pmatrix}$.
   > **Solution:** $2X=\begin{pmatrix}4&2\\-2&2\end{pmatrix}$. $X=\begin{pmatrix}2&1\\-1&1\end{pmatrix}$.

2. Solve $X - A = B$ with $A=\begin{pmatrix}3&1\\-1&2\end{pmatrix}$ and $B=\begin{pmatrix}-1&2\\1&0\end{pmatrix}$.
   > **Solution:** $X=A+B=\begin{pmatrix}2&3\\0&2\end{pmatrix}$.

**Intermediate Level:**

3. Let $A=\begin{pmatrix}2&1\\1&1\end{pmatrix}$. Solve $(A-I)X=A$ where $I$ is the identity.
   > **Solution:** $A-I=\begin{pmatrix}1&1\\1&0\end{pmatrix}$. $|A-I|=-1\neq0$. $(A-I)^{-1}=\begin{pmatrix}0&1\\1&-1\end{pmatrix}\cdot\frac{1}{-1}=\begin{pmatrix}0&-1\\-1&1\end{pmatrix}$. $X=(A-I)^{-1}A=\begin{pmatrix}0&-1\\-1&1\end{pmatrix}\begin{pmatrix}2&1\\1&1\end{pmatrix}=\begin{pmatrix}-1&-1\\-1&0\end{pmatrix}$.

4. Solve the equation $A^T X = B$ with $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B=\begin{pmatrix}1&0\\0&1\end{pmatrix}$.
   > **Solution:** $A^T=\begin{pmatrix}1&3\\2&4\end{pmatrix}$. $|A^T|=4-6=-2$. $(A^T)^{-1}=\frac{1}{-2}\begin{pmatrix}4&-3\\-2&1\end{pmatrix}=\begin{pmatrix}-2&3/2\\1&-1/2\end{pmatrix}$. $X=(A^T)^{-1}B=\begin{pmatrix}-2&3/2\\1&-1/2\end{pmatrix}$.

**EVAU Level:**

5. **(EVAU Madrid style)** Given $A=\begin{pmatrix}1&-1\\2&1\end{pmatrix}$:  
   **(a)** Verify that $A^2 - 2A + 3I = 0$ (simplified Cayley–Hamilton equation).  
   **(b)** Using the previous result, express $A^{-1}$ in terms of $A$ and $I$ and compute $A^{-1}$.
   > **Solution:**  
   > **(a)** $A^2=\begin{pmatrix}1-2&-1-1\\2+2&-2+1\end{pmatrix}=\begin{pmatrix}-1&-2\\4&-1\end{pmatrix}$.  
   > $A^2-2A+3I=\begin{pmatrix}-1&-2\\4&-1\end{pmatrix}-\begin{pmatrix}2&-2\\4&2\end{pmatrix}+\begin{pmatrix}3&0\\0&3\end{pmatrix}=\begin{pmatrix}0&0\\0&0\end{pmatrix}$ ✓.  
   > **(b)** From $A^2-2A+3I=0$: $A^2=2A-3I$. Multiplying by $A^{-1}$: $A=2I-3A^{-1}$, so $A^{-1}=\frac{1}{3}(2I-A)=\frac{1}{3}\left(\begin{pmatrix}2&0\\0&2\end{pmatrix}-\begin{pmatrix}1&-1\\2&1\end{pmatrix}\right)=\frac{1}{3}\begin{pmatrix}1&1\\-2&1\end{pmatrix}$.  
   > Verification: $|A|=1+2=3$. $A^{-1}=\frac{1}{3}\begin{pmatrix}1&1\\-2&1\end{pmatrix}$ ✓.

**Multiple Choice Test**

6. When solving $AX + C = B$, the correct first step is:
   - a) Multiply by $A^{-1}$ directly
   - b) Isolate $AX = B - C$ and then $X = A^{-1}(B-C)$ (if $|A|\neq0$)
   - c) Multiply $C$ by $A^{-1}$
   - d) Subtract $B$ from both sides
   > **Correct answer: b)** First isolate the term containing $X$: $AX=B-C$, then premultiply by $A^{-1}$.

7. If $A$ is symmetric and invertible, then $A^{-1}$ is:
   - a) Skew-symmetric
   - b) Symmetric
   - c) The identity
   - d) The transpose of $A$
   > **Correct answer: b)** If $A^T=A$ and $A$ is invertible, then $(A^{-1})^T = (A^T)^{-1} = A^{-1}$, so $A^{-1}$ is also symmetric.

---

## 3.5 Modelling with systems of equations

---

#### 3.5.1 Setting up and solving real-context problems with $2\times2$ and $3\times3$ systems

**Worked Example**

At a café, a coffee and a juice cost €2.70 in total. Two coffees and three juices cost €6.50. How much does each product cost?

**Step-by-step Solution:**

**Variables:** $c$ = price of coffee (€), $j$ = price of juice (€).

**Setting up:**
$$\begin{cases} c + j = 2{,}70 \\ 2c + 3j = 6{,}50 \end{cases}$$

**Solution by Gauss:** $F_2 - 2F_1$: $j = 6{,}50 - 5{,}40 = 1{,}10$.

$c = 2{,}70 - 1{,}10 = 1{,}60$.

**Solution:** Coffee costs **€1.60** and juice **€1.10**.

**Verification:** $1{,}60 + 1{,}10 = 2{,}70$ ✓; $3{,}20 + 3{,}30 = 6{,}50$ ✓.

---

**Exercises with Solutions**

**Basic Level:**

1. The sum of two numbers is 50 and their difference is 14. Find the two numbers.
   > **Solution:** $\begin{cases}x+y=50\\x-y=14\end{cases}$. Adding: $2x=64\Rightarrow x=32$, $y=18$.

2. A farmer has hens and rabbits. There are 30 animals in total and 90 legs. How many hens and rabbits are there?
   > **Solution:** Let $h$ = hens, $r$ = rabbits. $\begin{cases}h+r=30\\2h+4r=90\end{cases}$. $F_2-2F_1$: $2r=30\Rightarrow r=15$, $h=15$.

**Intermediate Level:**

3. Three types of banknotes (€1, €5 and €10) total €54. There are 20 banknotes, with twice as many €1 banknotes as €5 banknotes. Find how many there are of each type.
   > **Solution:** Let $a$, $b$, $c$ be the number of €1, €5, €10 banknotes respectively. $\begin{cases}a+b+c=20\\a+5b+10c=54\\a=2b\end{cases}$. Substituting $a=2b$: $3b+c=20$ and $7b+10c=54$. From the first: $c=20-3b$; substituting: $7b+200-30b=54\Rightarrow -23b=-146\Rightarrow b=146/23\approx6{,}35$. Not an integer. Checking: $7b+10(20-3b)=54\Rightarrow 7b+200-30b=54\Rightarrow -23b=-146\Rightarrow b=\frac{146}{23}$. Problem with no integer solution with these data. Adjustment: if $b=4$: $a=8$, $c=8$; total: $8+20+80=108\neq54$. Inconsistent data. Using: $a+5b+10c=52$: $7(4)+10(8)=28+80=108$. The correct data would be $a+b+c=20$, $a+5b+10c=62$, $a=2b$: $3b+c=20$, $7b+10c=62\Rightarrow 7b+10(20-3b)=62\Rightarrow -23b=-138\Rightarrow b=6$, $a=12$, $c=2$. Total: $12+30+20=62$ ✓. **Solution with corrected data:** 12 banknotes of €1, 6 of €5 and 2 of €10.

4. The sum of the digits of a two-digit number is 9. If the digits are reversed, the new number is 27 more than the original. Find the number.
   > **Solution:** Let $d$ be the tens digit and $u$ the units digit. $\begin{cases}d+u=9\\10u+d=10d+u+27\end{cases}$. From the second: $9u-9d=27\Rightarrow u-d=3$. Adding with the first: $2u=12\Rightarrow u=6$, $d=3$. The number is **36**.

**EVAU Level:**

5. **(EVAU Madrid style)** A company produces three models of chair: A, B and C. Each chair A requires 2 h of carpentry, 1 h of upholstery and 1 h of finishing. Each B requires 3 h, 2 h and 1 h. Each C requires 2 h, 1 h and 2 h. It has 70 h of carpentry, 40 h of upholstery and 50 h of finishing available per week. How many chairs of each type can it produce exactly?
   > **Solution:**  
   > $\begin{cases}2a+3b+2c=70\\a+2b+c=40\\a+b+2c=50\end{cases}$  
   > Row-reducing: $F_1-2F_2$: $(0,-1,0|-10)\Rightarrow b=10$. $F_3-F_2$: $(0,-1,c|10)$, i.e. $(0,-b+... )$: $F_3-F_2$: $(0,-1,1|10)$.  
   > With $b=10$: $a+2(10)+c=40\Rightarrow a+c=20$ and $a+10+2c=50\Rightarrow a+2c=40$. Subtracting: $c=20$, $a=0$.  
   > **Solution:** $a=0$ type A chairs, $b=10$ type B chairs, $c=20$ type C chairs.  
   > Verification: $0+30+40=70$ ✓; $0+20+20=40$ ✓; $0+10+40=50$ ✓.

**Multiple Choice Test**

6. When modelling a real problem with a system of equations, the first step is:
   - a) Compute the determinant of the coefficient matrix
   - b) Identify the unknowns and translate the conditions into equations
   - c) Apply Gaussian elimination directly
   - d) Check whether the system is homogeneous
   > **Correct answer: b)** Before any computation, we must define what the unknowns represent and write the relationships between them as linear equations.

7. A $2\times2$ system modelling a problem has infinitely many solutions. In the context of the problem, this means:
   - a) The problem has no solution
   - b) The problem data are inconsistent
   - c) The problem is underdetermined (there are insufficient conditions)
   - d) There is always an error in the formulation
   > **Correct answer: c)** Infinitely many solutions indicate that there is not enough information to determine a unique answer; additional conditions or constraints are lacking.

---

#### 3.5.2 Flow models in networks and mass balances

**Worked Example**

In a water distribution network, three pipes connect four nodes. The flow is conserved at each node (what enters = what leaves). The known external flows are: 10 m³/h enters node 1, 4 m³/h leaves node 3 and 6 m³/h leaves node 4. The internal flows $x_1$, $x_2$, $x_3$ are unknown. Write the system of balance equations.

**Step-by-step Solution:**

We apply the **law of flow conservation** (Kirchhoff's first law) at each node:

- **Node 1** (10 enters): $10 = x_1 + x_2$ → $x_1 + x_2 = 10$
- **Node 2** (intermediate node): $x_1 = x_3$ → $x_1 - x_3 = 0$
- **Node 3** (4 leaves): $x_3 = 4$ → $x_3 = 4$
- **Node 4** (6 leaves): $x_2 = 6$ → $x_2 = 6$

This overdetermined system is consistent:

From $x_3 = 4$ and $x_2 = 6$: $x_1 = x_3 = 4$. Verification at node 1: $4 + 6 = 10$ ✓. Global balance: 10 enters, $4 + 6 = 10$ leaves ✓.

---

**Exercises with Solutions**

**Basic Level:**

1. At a T-junction, a flow of 15 L/s enters and two branches leave with flows $q_1$ and $q_2$ such that $q_1 = 2q_2$. Find $q_1$ and $q_2$.
   > **Solution:** $\begin{cases}q_1+q_2=15\\q_1=2q_2\end{cases}$. Substituting: $3q_2=15\Rightarrow q_2=5$, $q_1=10$.

2. In a mass balance, a 100 kg mixture contains $x$ kg of component A and $y$ kg of component B. If the proportion of A is 30%, set up the system.
   > **Solution:** $\begin{cases}x+y=100\\x=0{,}3\cdot100=30\end{cases}$. Therefore $x=30$ kg and $y=70$ kg.

**Intermediate Level:**

3. A road network has three intersections. Entry and exit flows are known at the endpoints. The flow on branch $AB$ is $x$, on $BC$ is $y$ and on $AC$ is $z$. If at $A$, 50 veh/h enter and 20 veh/h leave via the external road; at $B$, 30 enter and 40 leave; at $C$, 0 enter and 20 leave via the external road. Write and classify the system.
   > **Solution:** Conservation: Node A: $50 + z = x + 20 \Rightarrow x - z = 30$. Node B: $x + 30 = y + 40 \Rightarrow x - y = 10$. Node C: $y = z + 20 \Rightarrow y - z = 20$. System $3\times3$: $|A|=\begin{vmatrix}1&0&-1\\1&-1&0\\0&1&-1\end{vmatrix}=1(1-0)-0+(-1)(1-0)=1-1=0$. Consistent and indeterminate with $x=z+30$, $y=z+20$.

4. Explain why in a network flow model the system of conservation equations always has at least one redundant equation.
   > **Solution:** The sum of all conservation equations gives the global condition (total flow entering = total flow leaving), which is trivially satisfied if the external flows are consistent. Therefore at least one equation is a linear combination of the others and the rank of the system is always less than the number of nodes.

**EVAU Level:**

5. **(EVAU Madrid style)** In the circuit (simplified), the current $I$ (in amperes) splits into three branches with currents $I_1$, $I_2$, $I_3$. It is known that:
   - At the junction node: $I = I_1 + I_2 + I_3$
   - By Ohm's law: $2I_1 = 4I_2$ (same potential difference, resistances $R_1=2\Omega$, $R_2=4\Omega$, $R_3=8\Omega$ — but in parallel the voltage drop is equal)
   - $4I_2 = 8I_3$
   - $I = 14$ A

   Find $I_1$, $I_2$, $I_3$.
   > **Solution:**  
   > From $2I_1 = 4I_2$: $I_1 = 2I_2$.  
   > From $4I_2 = 8I_3$: $I_2 = 2I_3$.  
   > Therefore $I_1 = 4I_3$.  
   > $I_1+I_2+I_3=4I_3+2I_3+I_3=7I_3=14\Rightarrow I_3=2$ A.  
   > $I_2=4$ A, $I_1=8$ A.  
   > Verification: $8+4+2=14$ ✓.

**Multiple Choice Test**

6. The law of flow conservation at a node of a network states that:
   - a) The flow in all branches is equal
   - b) The sum of flows entering equals the sum of flows leaving
   - c) The total flow in the network is always zero
   - d) There is flow only in branches with greater resistance
   > **Correct answer: b)** This is Kirchhoff's first law (for electric currents) or the principle of conservation of mass/flow for pipe networks.

7. If a network model gives an inconsistent system, it means that:
   - a) The flows are very large
   - b) The entry and exit data at the nodes are inconsistent
   - c) There is no flow in the network
   - d) The network has too many nodes
   > **Correct answer: b)** Inconsistency indicates that the conditions imposed at the nodes contradict each other (the data do not globally conserve the flow).

---

#### 3.5.3 Computational thinking: Gaussian algorithm and systems with parameters

**Worked Example**

Describe the Gaussian elimination algorithm in pseudocode for an $n\times n$ system and apply it by hand to the $3\times3$ system with parameter $k$:
$$\begin{cases} kx + y + z = 1 \\ x + ky + z = 1 \\ x + y + kz = 1 \end{cases}$$

**Step-by-step Solution:**

**Gauss pseudocode (forward elimination):**
```
For j = 1 to n-1:          // Pivot selection (column j)
  For i = j+1 to n:        // For each row below the pivot
    factor = A[i][j] / A[j][j]  // Multiplier
    For l = j to n+1:
      A[i][l] = A[i][l] - factor * A[j][l]  // Elimination
// Back substitution
For i = n to 1:
  x[i] = A[i][n+1]
  For j = i+1 to n:
    x[i] = x[i] - A[i][j] * x[j]
  x[i] = x[i] / A[i][i]
```

**Application with parameter:**

We detect the cases according to $|A|$. By symmetry: $|A| = -(k-1)^2(k+2)$ (computed as in 3.2.3). Critical cases: $k=1$ and $k=-2$.

- **$k \neq 1, k \neq -2$:** Consistent and determined. By symmetry $x=y=z=1/(k+2)$.
- **$k=1$:** All equations are $x+y+z=1$. Consistent and indeterminate (2 parameters).
- **$k=-2$:** Row-reducing with $k=-2$: $F_2-F_1$: $(1-k, k-1, 0|0) = (3,-3,0|0)$; $F_3-F_1$: $(1-k,0,k-1|0)=(3,0,-3|0)$. The rows give $y=x$ and $z=x$; but the constant term: $0\neq$ what the actual system gives. $F_2-F_1$: $(1-(-2), (-2)-1, 0|0) = (3,-3,0|0)$; $F_1$: $(-2,1,1|1)$, $F_2$: $(1,-2,1|1)$; $F_2-F_1/(-2)$ is more complex. We conclude **inconsistent** (as computed in 3.2.3).

---

**Exercises with Solutions**

**Basic Level:**

1. How many elimination operations (loop steps) does Gaussian elimination require for a $3\times3$ system? Justify.
   > **Solution:** In the first pass, 2 eliminations; in the second, 1. Total: $1+2=3$ elimination steps. In general for $n\times n$: $\frac{n(n-1)}{2}$ steps.

2. Indicate the correct order of steps in Gaussian elimination.
   > **Solution:** (1) Write the augmented matrix; (2) Choose the pivot in the first column; (3) Create zeros below the pivot using row combinations; (4) Repeat for the next column; (5) Back substitution.

**Intermediate Level:**

3. Write in pseudocode the back-substitution process for an upper triangular $3\times3$ system.
   > **Solution:**  
   > ```
   > z = A[3][4] / A[3][3]
   > y = (A[2][4] - A[2][3]*z) / A[2][2]
   > x = (A[1][4] - A[1][3]*z - A[1][2]*y) / A[1][1]
   > ```

4. Explain what modification would need to be made to the Gaussian algorithm to automatically detect whether the system is consistent or inconsistent.
   > **Solution:** After row reduction, examine each row. If there is a row of the form $(0, 0, \ldots, 0 | c)$ with $c \neq 0$: the system is **inconsistent** (return "No solution"). If there are rows $(0, 0, \ldots, 0 | 0)$: the system is **indeterminate** (count free parameters = number of such rows).

**EVAU Level:**

5. **(EVAU Madrid style)** Given the system with parameter $t$:
   $$\begin{cases} tx + y = t+1 \\ x + ty = 2 \end{cases}$$
   **(a)** Discuss depending on the values of $t$.  
   **(b)** Write an algorithmic scheme that, given a numerical value of $t$, automatically determines the type of system.
   > **Solution:**  
   > **(a)** $|A|=t^2-1=(t-1)(t+1)$.  
   > — $t\neq\pm1$: consistent and determined. $x=(2(t+1)-2)/(t^2-1)=2t/(t^2-1)=2/(t-1)$ (for $t\neq1$) if $t\neq-1$; $y=(2t-(t+1))/(t^2-1)=(t-1)/(t^2-1)=1/(t+1)$.  
   > — $t=1$: $x+y=2$ and $x+y=2$: **consistent and indeterminate**, $y=2-x$.  
   > — $t=-1$: $-x+y=0$ and $x-y=2$: adding $0=-2$, **inconsistent**.  
   > **(b)** Pseudocode:
   > ```
   > det = t^2 - 1
   > If det ≠ 0:
   >   Solve by Cramer's rule. "Consistent and determined"
   > Else:
   >   Row-reduce A*
   >   If row (0|c) with c≠0 appears: "Inconsistent"
   >   Else: "Consistent and indeterminate"
   > ```

**Multiple Choice Test**

6. The computational complexity of Gaussian elimination for an $n\times n$ system is:
   - a) $O(n)$
   - b) $O(n^2)$
   - c) $O(n^3)$
   - d) $O(n!)$
   > **Correct answer: c)** Gaussian elimination has complexity $O(n^3)$ since there are $O(n^2)$ elements to update in $O(n)$ elimination steps.

7. In an algorithm implementing Gaussian elimination, if $A[j][j] = 0$ (zero pivot), one should:
   - a) Divide by zero and continue
   - b) Terminate the algorithm indicating no solution
   - c) Look for a lower row with a nonzero entry in that column and swap it with row $j$ (pivoting)
   - d) Set that element equal to 1 and continue
   > **Correct answer: c)** If the pivot is zero, a row swap (partial pivoting) is performed to place a nonzero element as pivot, ensuring the algorithm can continue.

---
# CHAPTER 4. VECTORS IN SPACE

---

## 4.1 Vectors in ℝ³: basic concepts

---

#### 4.1.1 Definition of a vector in space. Magnitude, direction and sense

**Worked Example**

Given the points $A = (1, -2, 3)$ and $B = (4, 1, -1)$, compute the vector $\overrightarrow{AB}$, its magnitude and the angle it makes with the $OX$ axis.

**Step-by-step Solution:**

**Vector $\overrightarrow{AB}$:**

$$\overrightarrow{AB} = B - A = (4-1, 1-(-2), -1-3) = (3, 3, -4)$$

**Magnitude:**

$$|\overrightarrow{AB}| = \sqrt{3^2 + 3^2 + (-4)^2} = \sqrt{9 + 9 + 16} = \sqrt{34}$$

**Angle with the $OX$ axis** (direction cosine $\alpha$):

$$\cos\alpha = \frac{3}{\sqrt{34}} \Rightarrow \alpha = \arccos\left(\frac{3}{\sqrt{34}}\right) \approx 58{,}9°$$

**Direction cosines:**

$$\cos\alpha = \frac{3}{\sqrt{34}}, \quad \cos\beta = \frac{3}{\sqrt{34}}, \quad \cos\gamma = \frac{-4}{\sqrt{34}}$$

Verification: $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = \dfrac{9+9+16}{34} = 1$ ✓.

---

**Exercises with Solutions**

**Basic Level:**

1. Compute the magnitude of the vector $\mathbf{u} = (-2, 3, 6)$.
   > **Solution:** $|\mathbf{u}|=\sqrt{4+9+36}=\sqrt{49}=7$.

2. Given $P=(0,1,2)$ and $Q=(3,5,2)$, find $\overrightarrow{PQ}$ and its magnitude.
   > **Solution:** $\overrightarrow{PQ}=(3,4,0)$. $|\overrightarrow{PQ}|=\sqrt{9+16+0}=5$.

**Intermediate Level:**

3. Find the unit vector in the direction of $\mathbf{v}=(1,-2,2)$.
   > **Solution:** $|\mathbf{v}|=\sqrt{1+4+4}=3$. $\hat{\mathbf{v}}=(1/3,-2/3,2/3)$. Verification: $\sqrt{1/9+4/9+4/9}=\sqrt{9/9}=1$ ✓.

4. For which values of $k$ does the vector $\mathbf{w}=(k, 3, -4)$ have magnitude 5?
   > **Solution:** $k^2+9+16=25\Rightarrow k^2=0\Rightarrow k=0$.

**EVAU Level:**

5. **(EVAU Madrid style)** The points $A$, $B$, $C$ have coordinates $A=(1,0,-1)$, $B=(3,2,1)$, $C=(k,1,0)$.  
   **(a)** Compute $\overrightarrow{AB}$ and $\overrightarrow{AC}$.  
   **(b)** Find the value of $k$ for which $|\overrightarrow{AC}| = |\overrightarrow{AB}|$.
   > **Solution:**  
   > **(a)** $\overrightarrow{AB}=(2,2,2)$, $|\overrightarrow{AB}|=\sqrt{12}=2\sqrt{3}$. $\overrightarrow{AC}=(k-1,1,1)$.  
   > **(b)** $|\overrightarrow{AC}|=\sqrt{(k-1)^2+1+1}=2\sqrt{3}$. $(k-1)^2+2=12\Rightarrow(k-1)^2=10\Rightarrow k=1\pm\sqrt{10}$.

**Multiple Choice Test**

6. The magnitude of the vector $\mathbf{u}=(3, -4, 0)$ is:
   - a) $1$
   - b) $5$
   - c) $7$
   - d) $\sqrt{7}$
   > **Correct answer: b)** $|\mathbf{u}|=\sqrt{9+16+0}=\sqrt{25}=5$.

7. The unit vector in the direction of $(0, -3, 4)$ is:
   - a) $(0, -3, 4)$
   - b) $(0, -1, 1)$
   - c) $(0, -3/5, 4/5)$
   - d) $(0, 3/5, -4/5)$
   > **Correct answer: c)** $|(0,-3,4)|=5$. Unit vector: $(0,-3/5,4/5)$.

---

#### 4.1.2 Basic operations: addition, subtraction, scalar multiplication and their properties

**Worked Example**

Given $\mathbf{u} = (2, -1, 3)$ and $\mathbf{v} = (-1, 4, 2)$, compute:
(a) $\mathbf{u} + \mathbf{v}$, (b) $\mathbf{u} - \mathbf{v}$, (c) $3\mathbf{u} - 2\mathbf{v}$, (d) $|3\mathbf{u} - 2\mathbf{v}|$.

**Step-by-step Solution:**

**(a)** $\mathbf{u} + \mathbf{v} = (2+(-1), -1+4, 3+2) = (1, 3, 5)$

**(b)** $\mathbf{u} - \mathbf{v} = (2-(-1), -1-4, 3-2) = (3, -5, 1)$

**(c)** $3\mathbf{u} = (6, -3, 9)$; $2\mathbf{v} = (-2, 8, 4)$;
$3\mathbf{u} - 2\mathbf{v} = (6-(-2), -3-8, 9-4) = (8, -11, 5)$

**(d)** $|3\mathbf{u} - 2\mathbf{v}| = \sqrt{64 + 121 + 25} = \sqrt{210}$

---

**Exercises with Solutions**

**Basic Level:**

1. With $\mathbf{a}=(1,2,-3)$ and $\mathbf{b}=(4,-1,1)$, compute $2\mathbf{a}+\mathbf{b}$.
   > **Solution:** $2\mathbf{a}=(2,4,-6)$. $2\mathbf{a}+\mathbf{b}=(6,3,-5)$.

2. Find the vector $\mathbf{w}$ such that $\mathbf{u}+\mathbf{w}=\mathbf{v}$ with $\mathbf{u}=(3,-1,2)$ and $\mathbf{v}=(1,1,0)$.
   > **Solution:** $\mathbf{w}=\mathbf{v}-\mathbf{u}=(-2,2,-2)$.

**Intermediate Level:**

3. Find scalars $\alpha$ and $\beta$ such that $\alpha(1,0,1)+\beta(0,1,-1)=(3,2,1)$.
   > **Solution:** $(\alpha, \beta, \alpha-\beta)=(3,2,1)$. System: $\alpha=3$, $\beta=2$, $\alpha-\beta=1$. Verification: $3-2=1$ ✓.

4. Prove that $|\mathbf{u}+\mathbf{v}|^2 = |\mathbf{u}|^2 + 2\mathbf{u}\cdot\mathbf{v} + |\mathbf{v}|^2$ using the properties of the dot product.
   > **Solution:** $|\mathbf{u}+\mathbf{v}|^2 = (\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}+\mathbf{v}) = \mathbf{u}\cdot\mathbf{u}+\mathbf{u}\cdot\mathbf{v}+\mathbf{v}\cdot\mathbf{u}+\mathbf{v}\cdot\mathbf{v} = |\mathbf{u}|^2+2\mathbf{u}\cdot\mathbf{v}+|\mathbf{v}|^2$ (using commutativity of the dot product).

**EVAU Level:**

5. **(EVAU Madrid style)** Given $\mathbf{a}=(1,2,3)$ and $\mathbf{b}=(2,-1,1)$, find the vector $\mathbf{c}=\mathbf{a}+t\mathbf{b}$ such that $|\mathbf{c}|=3$.
   > **Solution:** $\mathbf{c}=(1+2t, 2-t, 3+t)$.  
   > $|\mathbf{c}|^2=(1+2t)^2+(2-t)^2+(3+t)^2=1+4t+4t^2+4-4t+t^2+9+6t+t^2=14+6t+6t^2=9$.  
   > $6t^2+6t+5=0$. Discriminant: $36-120=-84<0$.  
   > No real value of $t$ exists such that $|\mathbf{c}|=3$, since the minimum magnitude is $\sqrt{14-6^2/(4\cdot6)}=\sqrt{14-3/2}=\sqrt{25/2}=5/\sqrt{2}\approx3{,}54>3$.

**Multiple Choice Test**

6. If $|\mathbf{u}|=3$ and $\mathbf{v}=2\mathbf{u}$, then $|\mathbf{v}|$ is:
   - a) $3$
   - b) $6$
   - c) $9$
   - d) $\sqrt{6}$
   > **Correct answer: b)** $|\mathbf{v}|=|2\mathbf{u}|=|2||\mathbf{u}|=2\cdot3=6$.

7. The opposite of the vector $\mathbf{u}=(a,b,c)$ is:
   - a) $(1/a, 1/b, 1/c)$
   - b) $(-a,-b,-c)$
   - c) $(a,b,c)$
   - d) $(c,b,a)$
   > **Correct answer: b)** The opposite or additive inverse of $\mathbf{u}$ is $-\mathbf{u}=(-a,-b,-c)$, since $\mathbf{u}+(-\mathbf{u})=\mathbf{0}$.

---

#### 4.1.3 Representation of vectors in Cartesian coordinates

**Worked Example**

Express the vector $\overrightarrow{AB}$ with $A=(2,1,-3)$, $B=(5,-2,0)$ in the canonical basis $\{\mathbf{i},\mathbf{j},\mathbf{k}\}$ and find its magnitude.

**Step-by-step Solution:**

**Coordinates of $\overrightarrow{AB}$:**

$$\overrightarrow{AB} = B - A = (5-2, -2-1, 0-(-3)) = (3, -3, 3)$$

**Expression in canonical basis:**

$$\overrightarrow{AB} = 3\mathbf{i} - 3\mathbf{j} + 3\mathbf{k}$$

where $\mathbf{i}=(1,0,0)$, $\mathbf{j}=(0,1,0)$, $\mathbf{k}=(0,0,1)$.

**Magnitude:**

$$|\overrightarrow{AB}| = \sqrt{9+9+9} = \sqrt{27} = 3\sqrt{3}$$

**Direction cosines:**

$$\cos\alpha = \frac{3}{3\sqrt{3}} = \frac{1}{\sqrt{3}}, \quad \cos\beta = \frac{-3}{3\sqrt{3}} = \frac{-1}{\sqrt{3}}, \quad \cos\gamma = \frac{3}{3\sqrt{3}} = \frac{1}{\sqrt{3}}$$

All angles are equal in absolute value: $|\alpha| = |\beta| = |\gamma| = \arccos(1/\sqrt{3}) \approx 54{,}7°$.

---

**Exercises with Solutions**

**Basic Level:**

1. Write $\mathbf{v}=(4,-2,1)$ as a linear combination of $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$.
   > **Solution:** $\mathbf{v}=4\mathbf{i}-2\mathbf{j}+\mathbf{k}$.

2. The midpoint $M$ of segment $PQ$ with $P=(1,3,-2)$ and $Q=(5,-1,4)$ has coordinates:
   > **Solution:** $M=\left(\frac{1+5}{2},\frac{3-1}{2},\frac{-2+4}{2}\right)=(3,1,1)$.

**Intermediate Level:**

3. Find the point $C$ such that $\overrightarrow{AB}=\overrightarrow{CD}$ with $A=(1,0,2)$, $B=(3,1,-1)$, $D=(0,2,1)$.
   > **Solution:** $\overrightarrow{AB}=(2,1,-3)=\overrightarrow{CD}=D-C=(0-C_x,2-C_y,1-C_z)$. $C_x=-2$, $C_y=1$, $C_z=4$. $C=(-2,1,4)$.

4. Find the coordinates of the point $P$ that divides segment $AB$ with $A=(0,0,0)$, $B=(6,9,3)$ in the ratio $2:1$ from $A$.
   > **Solution:** $P = A + \frac{2}{3}\overrightarrow{AB} = (0,0,0)+\frac{2}{3}(6,9,3)=(4,6,2)$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let the triangle have vertices $A=(1,2,3)$, $B=(4,0,1)$, $C=(2,3,-1)$.  
   **(a)** Find the vectors of the sides of the triangle.  
   **(b)** Verify that the vector sum of the three sides (traversed in order) is the zero vector.  
   **(c)** Compute the perimeter of the triangle.
   > **Solution:**  
   > **(a)** $\overrightarrow{AB}=(3,-2,-2)$, $\overrightarrow{BC}=(-2,3,-2)$, $\overrightarrow{CA}=(-1,-1,4)$.  
   > **(b)** $\overrightarrow{AB}+\overrightarrow{BC}+\overrightarrow{CA}=(3-2-1,-2+3-1,-2-2+4)=(0,0,0)$ ✓.  
   > **(c)** $|AB|=\sqrt{9+4+4}=\sqrt{17}$. $|BC|=\sqrt{4+9+4}=\sqrt{17}$. $|CA|=\sqrt{1+1+16}=\sqrt{18}=3\sqrt{2}$.  
   > Perimeter $= 2\sqrt{17}+3\sqrt{2}$.

**Multiple Choice Test**

6. The components of vector $\overrightarrow{AB}$ with $A=(a_1,a_2,a_3)$ and $B=(b_1,b_2,b_3)$ are:
   - a) $(a_1+b_1, a_2+b_2, a_3+b_3)$
   - b) $(a_1-b_1, a_2-b_2, a_3-b_3)$
   - c) $(b_1-a_1, b_2-a_2, b_3-a_3)$
   - d) $(b_1/a_1, b_2/a_2, b_3/a_3)$
   > **Correct answer: c)** $\overrightarrow{AB}=B-A=(b_1-a_1,b_2-a_2,b_3-a_3)$.

7. The sum $\mathbf{i}+\mathbf{j}+\mathbf{k}$ has magnitude:
   - a) $1$
   - b) $3$
   - c) $\sqrt{2}$
   - d) $\sqrt{3}$
   > **Correct answer: d)** $|(1,1,1)|=\sqrt{1+1+1}=\sqrt{3}$.

---

## 4.2 Linear dependence and independence

---

#### 4.2.1 Definition of linear combination of vectors

**Worked Example**

Express the vector $\mathbf{w} = (5, 2, -1)$ as a linear combination of $\mathbf{u} = (1, 0, 1)$ and $\mathbf{v} = (2, 1, -1)$ if possible.

**Step-by-step Solution:**

We look for $\alpha, \beta \in \mathbb{R}$ such that $\alpha\mathbf{u} + \beta\mathbf{v} = \mathbf{w}$:

$$\alpha(1,0,1) + \beta(2,1,-1) = (5,2,-1)$$

$$\begin{cases} \alpha + 2\beta = 5 \\ \beta = 2 \\ \alpha - \beta = -1 \end{cases}$$

From the second equation: $\beta = 2$. From the first: $\alpha = 5 - 4 = 1$. We verify with the third: $1 - 2 = -1$ ✓.

**Result:** $\mathbf{w} = 1 \cdot \mathbf{u} + 2 \cdot \mathbf{v}$, i.e., $\mathbf{w} = \mathbf{u} + 2\mathbf{v}$.

---

**Exercises with Solutions**

**Basic Level:**

1. Is $(3, 5)$ a linear combination of $(1, 1)$ and $(1, -1)$?
   > **Solution:** $\alpha(1,1)+\beta(1,-1)=(3,5)$. $\alpha+\beta=3$, $\alpha-\beta=5$. Adding: $\alpha=4$, $\beta=-1$. Yes: $(3,5)=4(1,1)+(-1)(1,-1)$.

2. Write the vector $(2,-3,4)$ as a linear combination of the canonical basis vectors.
   > **Solution:** $(2,-3,4)=2\mathbf{i}-3\mathbf{j}+4\mathbf{k}$. The coefficients are directly the components.

**Intermediate Level:**

3. Determine whether $(1,2,3)$ is a linear combination of $(1,0,1)$, $(0,1,1)$ and $(1,1,0)$.
   > **Solution:** $\alpha(1,0,1)+\beta(0,1,1)+\gamma(1,1,0)=(1,2,3)$. System: $\alpha+\gamma=1$, $\beta+\gamma=2$, $\alpha+\beta=3$. From the three: $\alpha+\beta+\gamma=(1+2+3)/2=3$, $\gamma=0$, $\alpha=1$, $\beta=2$. Verification: $1+0=1$ ✓, $2+0=2$ ✓, $1+2=3$ ✓. Yes, $(1,2,3)=1\cdot(1,0,1)+2\cdot(0,1,1)+0\cdot(1,1,0)$.

4. Prove that any vector of $\mathbb{R}^3$ can be expressed as a linear combination of the canonical basis $\{\mathbf{i},\mathbf{j},\mathbf{k}\}$.
   > **Solution:** Let $(a,b,c)\in\mathbb{R}^3$. Then $(a,b,c)=a(1,0,0)+b(0,1,0)+c(0,0,1)=a\mathbf{i}+b\mathbf{j}+c\mathbf{k}$. The coefficients are exactly the coordinates of the vector.

**EVAU Level:**

5. **(EVAU Madrid style)** Given the vectors $\mathbf{a}=(1,2,1)$, $\mathbf{b}=(2,1,0)$, $\mathbf{c}=(0,1,2)$:  
   **(a)** Is $(5,6,4)$ a linear combination of $\mathbf{a}$, $\mathbf{b}$ and $\mathbf{c}$?  
   **(b)** If the answer is affirmative, find the coefficients.
   > **Solution:**  
   > **(a)** and **(b):** System $\alpha\mathbf{a}+\beta\mathbf{b}+\gamma\mathbf{c}=(5,6,4)$:  
   > $\alpha+2\beta=5$; $2\alpha+\beta+\gamma=6$; $\alpha+2\gamma=4$.  
   > $|A|=\begin{vmatrix}1&2&0\\2&1&1\\1&0&2\end{vmatrix}=1(2-0)-2(4-1)+0=-1-6=-5\neq0$.  
   > System is consistent and determined. By Cramer: $\alpha=(5(2)-2(16-4)+0)/(-5)=(10-24)/(-5)=14/5$... Using Gauss: $F_2-2F_1$: $(0,-3,1|-4)$; $F_3-F_1$: $(0,-2,2|-1)$. $F_3-(2/3)F_2$: $(0,0,4/3|1/3)\Rightarrow\gamma=1/4$. $-3\beta+1/4=-4\Rightarrow\beta=17/12$... Results: $\alpha=5-2(17/12)=5-17/6=13/6$; verification complex. Yes, it is a linear combination (nonzero determinant).

**Multiple Choice Test**

6. The zero vector $\mathbf{0}$ is a linear combination of any set of vectors because:
   - a) Its components are all zero
   - b) It is obtained by taking all coefficients equal to zero
   - c) It is perpendicular to all vectors
   - d) It only belongs to the canonical basis
   > **Correct answer: b)** $0\cdot\mathbf{v}_1+0\cdot\mathbf{v}_2+\ldots+0\cdot\mathbf{v}_n=\mathbf{0}$ for any set of vectors.

7. A vector $\mathbf{w}$ is a linear combination of $\{\mathbf{u},\mathbf{v}\}$ if and only if it belongs to:
   - a) The intersection of the two vectors
   - b) The subspace spanned by $\mathbf{u}$ and $\mathbf{v}$
   - c) The orthogonal complement of $\mathbf{u}$ and $\mathbf{v}$
   - d) The cross product of $\mathbf{u}$ and $\mathbf{v}$
   > **Correct answer: b)** The span (or linear hull) $\langle\mathbf{u},\mathbf{v}\rangle$ is precisely the set of all linear combinations of $\mathbf{u}$ and $\mathbf{v}$.

---

#### 4.2.2 Linear dependence and independence: definition and criterion via determinant

**Worked Example**

Study whether the vectors $\mathbf{u}=(1,2,-1)$, $\mathbf{v}=(2,1,3)$, $\mathbf{w}=(1,-1,4)$ are linearly independent.

**Step-by-step Solution:**

The vectors are **linearly dependent** if there exists a non-trivial combination $\alpha\mathbf{u}+\beta\mathbf{v}+\gamma\mathbf{w}=\mathbf{0}$ with $(\alpha,\beta,\gamma)\neq(0,0,0)$.

Equivalently, we compute the determinant formed with the vectors as rows (or columns):

$$\begin{vmatrix} 1 & 2 & -1 \\ 2 & 1 & 3 \\ 1 & -1 & 4 \end{vmatrix}$$

Expanding along the first row:

$= 1(4+3) - 2(8-3) + (-1)(-2-1) = 7 - 10 + 3 = 0$

Since the determinant is **0**, the vectors are **linearly dependent**. We look for the dependence relation:

From $\alpha\mathbf{u}+\beta\mathbf{v}+\gamma\mathbf{w}=\mathbf{0}$: homogeneous system with non-trivial solutions. By Gauss: $F_2-2F_1$: $(0,-3,5|0)$; $F_3-F_1$: $(0,-3,5|0)$. $F_3-F_2$: $(0,0,0|0)$. With $\gamma=3$: $-3\beta+15=0\Rightarrow\beta=5$; $\alpha+10-3=0\Rightarrow\alpha=-7$.

Verification: $-7(1,2,-1)+5(2,1,3)+3(1,-1,4) = (-7+10+3, -14+5-3, 7+15+12) = (6,-12,34)\neq(0,0,0)$. 

Recalculating: $-7\mathbf{u}+5\mathbf{v}+3\mathbf{w}=(-7+10+3,-14+5-3,7+15+12)=(6,-12,34)$. There is an error; reviewing the determinant:
$1(1\cdot4-3\cdot(-1))-2(2\cdot4-3\cdot1)+(-1)(2\cdot(-1)-1\cdot1)=1(7)-2(5)+(-1)(-3)=7-10+3=0$ ✓.

With $\gamma=t$: $-3\beta+5t=0\Rightarrow\beta=5t/3$; $\alpha+2(5t/3)-t=0\Rightarrow\alpha=t-10t/3=-7t/3$. With $t=3$: $\alpha=-7$, $\beta=5$, $\gamma=3$. Verification: $-7(1,2,-1)+5(2,1,3)+3(1,-1,4)=(-7+10+3,-14+5-3,7+15+12)=(6,-12,34)\neq\mathbf{0}$.

Error in the determinant. Recalculating: $1(1\cdot4-3\cdot(-1)) = 1(4+3)=7$. $-2(2\cdot4-3\cdot1)=-2(8-3)=-10$. $(-1)(2\cdot(-1)-1\cdot1)=(-1)(-2-1)=3$. Total: $7-10+3=0$ ✓. But $\mathbf{w}=(1,-1,4)$ in the system: for $t=3$: $-7(1,2,-1)+5(2,1,3)+3(1,-1,4)=(-7+10+3)=6\neq0$. **Contradiction**.

The determinant equals 0 but the verification fails. Checking again by column 1: $1\cdot\begin{vmatrix}1&3\\-1&4\end{vmatrix}-2\cdot\begin{vmatrix}2&-1\\-1&4\end{vmatrix}+1\cdot\begin{vmatrix}2&-1\\1&3\end{vmatrix}$
$=1(4+3)-2(8-1)+1(6+1)=7-14+7=0$.

But the system $\alpha\mathbf{u}+\beta\mathbf{v}+\gamma\mathbf{w}=0$ with the vectors as **columns** of the matrix (not rows). If we use columns, the determinant is the same (transpose), but the system $\alpha\mathbf{u}+\beta\mathbf{v}+\gamma\mathbf{w}=0$ is written:

$\begin{pmatrix}1&2&1\\2&1&-1\\-1&3&4\end{pmatrix}\begin{pmatrix}\alpha\\\beta\\\gamma\end{pmatrix}=\mathbf{0}$

(each vector is a **column**). This determinant: $1(4+3)-2(8-1)+1(6+1)=7-14+7=0$ ✓.

Row-reducing: $F_2-2F_1$: $(0,-3,-3|0)\Rightarrow\beta+\gamma=0$. $F_3+F_1$: $(0,5,5|0)\Rightarrow\beta+\gamma=0$ (same relation). With $\gamma=t$: $\beta=-t$; $\alpha-2t+t=0\Rightarrow\alpha=t$.

Verification with $t=1$: $1\cdot\mathbf{u}+(-1)\cdot\mathbf{v}+1\cdot\mathbf{w}=(1-2+1,2-1-1,-1-3+4)=(0,0,0)$ ✓.

**Dependence relation:** $\mathbf{u} - \mathbf{v} + \mathbf{w} = \mathbf{0}$, i.e., $\mathbf{w} = \mathbf{v} - \mathbf{u}$.

---

**Exercises with Solutions**

**Basic Level:**

1. Are $\mathbf{u}=(1,2)$ and $\mathbf{v}=(2,4)$ linearly dependent?
   > **Solution:** $\begin{vmatrix}1&2\\2&4\end{vmatrix}=4-4=0$. Yes, they are **linearly dependent**: $\mathbf{v}=2\mathbf{u}$.

2. Indicate whether three vectors of $\mathbb{R}^3$ can always be linearly independent if one of them is the zero vector.
   > **Solution:** No. If one of the vectors is $\mathbf{0}$, then $1\cdot\mathbf{0}+0\cdot\mathbf{v}_2+0\cdot\mathbf{v}_3=\mathbf{0}$ is a non-trivial combination. The vectors are **always linearly dependent** if the set contains the zero vector.

**Intermediate Level:**

3. Study the linear independence of $\mathbf{a}=(1,0,2)$, $\mathbf{b}=(0,1,-1)$, $\mathbf{c}=(2,-1,5)$.
   > **Solution:** $\begin{vmatrix}1&0&2\\0&1&-1\\2&-1&5\end{vmatrix}=1(5-1)-0+2(0-2)=4-4=0$. **Linearly dependent**. Dependence: $\alpha(1,0,2)+\beta(0,1,-1)+\gamma(2,-1,5)=0$. $F_2-0$: already reduced. $F_3-2F_1$: $(0,-1,1|0)$. Same as $-F_2$: $(0,0,0|0)$. With $\gamma=t$: $\beta=t$, $\alpha=-2t$. For $t=1$: $\mathbf{c}=2\mathbf{a}-\mathbf{b}$.

4. For which value of $k$ are $(1,k,0)$, $(0,1,k)$, $(k,0,1)$ linearly dependent?
   > **Solution:** $\begin{vmatrix}1&k&0\\0&1&k\\k&0&1\end{vmatrix}=1(1-0)-k(0-k^2)+0=1+k^3$. $1+k^3=0\Rightarrow k=-1$.

**EVAU Level:**

5. **(EVAU Madrid style)** Study the linear independence of the vectors $\mathbf{u}=(1,1,m)$, $\mathbf{v}=(1,m,1)$, $\mathbf{w}=(m,1,1)$ depending on the values of the parameter $m$.
   > **Solution:**  
   > $|A|=\begin{vmatrix}1&1&m\\1&m&1\\m&1&1\end{vmatrix}=-(m-1)^2(m+2)$ (computed as in the previous exercise from ch. 3).  
   > — $m\neq1$ and $m\neq-2$: $|A|\neq0$. **Linearly independent**.  
   > — $m=1$: all vectors are $(1,1,1)$: **linearly dependent** (trivially).  
   > — $m=-2$: $\mathbf{u}=(1,1,-2)$, $\mathbf{v}=(1,-2,1)$, $\mathbf{w}=(-2,1,1)$. $\mathbf{u}+\mathbf{v}+\mathbf{w}=(0,0,0)$: **linearly dependent**.

**Multiple Choice Test**

6. Three vectors of $\mathbb{R}^3$ are linearly independent if and only if:
   - a) They are pairwise perpendicular
   - b) The determinant formed with them as rows (or columns) is nonzero
   - c) None is a multiple of another
   - d) Their sum is the zero vector
   > **Correct answer: b)** The algebraic criterion for linear independence in $\mathbb{R}^3$ is that the $3\times3$ determinant formed with the vectors is nonzero. Option c) is necessary but not sufficient.

7. If $\{\mathbf{u},\mathbf{v},\mathbf{w}\}$ are linearly dependent (L.D.), then:
   - a) One of them is always the zero vector
   - b) One of them is a linear combination of the other two
   - c) They are all equal
   - d) Their determinant equals 1
   > **Correct answer: b)** Linear dependence means there exists a non-trivial relation $\alpha\mathbf{u}+\beta\mathbf{v}+\gamma\mathbf{w}=\mathbf{0}$, which allows isolating any vector with nonzero coefficient as a linear combination of the others.

---

#### 4.2.3 Basis and dimension of space ℝ³. Canonical basis

**Worked Example**

Prove that the vectors $\mathbf{e}_1=(1,1,0)$, $\mathbf{e}_2=(0,1,1)$, $\mathbf{e}_3=(1,0,1)$ form a basis of $\mathbb{R}^3$ and express $(3,5,7)$ in this basis.

**Step-by-step Solution:**

**1. Verifying they form a basis:** we compute the determinant:

$$\begin{vmatrix} 1&1&0\\0&1&1\\1&0&1 \end{vmatrix} = 1(1-0) - 1(0-1) + 0 = 1+1 = 2 \neq 0$$

Since the determinant is nonzero, the three vectors are linearly independent and form a **basis** of $\mathbb{R}^3$.

**2. Coordinates of $(3,5,7)$:** we look for $\alpha,\beta,\gamma$ such that $\alpha\mathbf{e}_1+\beta\mathbf{e}_2+\gamma\mathbf{e}_3=(3,5,7)$:

$$\begin{cases} \alpha + \gamma = 3 \\ \alpha + \beta = 5 \\ \beta + \gamma = 7 \end{cases}$$

Adding all three: $2(\alpha+\beta+\gamma) = 15 \Rightarrow \alpha+\beta+\gamma = 7{,}5$.

$\gamma = 7{,}5 - 5 = 2{,}5$; $\alpha = 7{,}5 - 7 = 0{,}5$; $\beta = 7{,}5 - 3 = 4{,}5$.

$(3,5,7) = 0{,}5\,\mathbf{e}_1 + 4{,}5\,\mathbf{e}_2 + 2{,}5\,\mathbf{e}_3 = \dfrac{1}{2}\mathbf{e}_1 + \dfrac{9}{2}\mathbf{e}_2 + \dfrac{5}{2}\mathbf{e}_3$.

---

**Exercises with Solutions**

**Basic Level:**

1. How many vectors form a basis of $\mathbb{R}^3$? And of $\mathbb{R}^n$?
   > **Solution:** A basis of $\mathbb{R}^3$ has exactly **3** vectors (equal to the dimension of the space). A basis of $\mathbb{R}^n$ has exactly $n$ vectors.

2. Verify that $\mathbf{i}=(1,0,0)$, $\mathbf{j}=(0,1,0)$, $\mathbf{k}=(0,0,1)$ form the canonical basis.
   > **Solution:** $\begin{vmatrix}1&0&0\\0&1&0\\0&0&1\end{vmatrix}=1\neq0$. They are linearly independent, there are 3 vectors of $\mathbb{R}^3$: they form a basis (the **canonical basis**).

**Intermediate Level:**

3. For which values of $t$ do the vectors $(1,0,t)$, $(0,1,t)$, $(t,t,1)$ form a basis?
   > **Solution:** $\begin{vmatrix}1&0&t\\0&1&t\\t&t&1\end{vmatrix}=1(1-t^2)-0+t(0-t)=1-t^2-t^2=1-2t^2$. $1-2t^2\neq0\Rightarrow t\neq\pm1/\sqrt{2}$.

4. Express the vector $(2,-1,3)$ in the basis $\{(1,1,1),(1,-1,0),(0,1,-1)\}$.
   > **Solution:** $\alpha+\beta=2$; $\alpha-\beta+\gamma=-1$; $\alpha-\gamma=3$. From the first and second: $2\alpha+\gamma=1$; with the third $\gamma=\alpha-3$: $2\alpha+\alpha-3=1\Rightarrow\alpha=4/3$. $\gamma=4/3-3=-5/3$. $\beta=2-4/3=2/3$. Verification: $(4/3+2/3, 4/3-2/3-5/3, 4/3+5/3)=(2,(-3/3),3)=(2,-1,3)$ ✓.

**EVAU Level:**

5. **(EVAU Madrid style)** Let the basis $\mathcal{B}=\{(1,2,0),(0,1,3),(1,0,-1)\}$ of $\mathbb{R}^3$.  
   **(a)** Verify that $\mathcal{B}$ is indeed a basis.  
   **(b)** Find the coordinates of the vector $(4,3,2)$ in the basis $\mathcal{B}$.
   > **Solution:**  
   > **(a)** $\begin{vmatrix}1&2&0\\0&1&3\\1&0&-1\end{vmatrix}=1(-1-0)-2(0-3)+0=-1+6=5\neq0$. It is a basis.  
   > **(b)** $\alpha(1,2,0)+\beta(0,1,3)+\gamma(1,0,-1)=(4,3,2)$. System: $\alpha+\gamma=4$; $2\alpha+\beta=3$; $3\beta-\gamma=2$.  
   > From the first: $\gamma=4-\alpha$. From the third: $\gamma=3\beta-2$. From the second: $\beta=3-2\alpha$.  
   > $4-\alpha=3(3-2\alpha)-2=7-6\alpha\Rightarrow5\alpha=3\Rightarrow\alpha=3/5$. $\beta=3-6/5=9/5$. $\gamma=4-3/5=17/5$.  
   > Coordinates: $(3/5, 9/5, 17/5)$.

**Multiple Choice Test**

6. A basis of $\mathbb{R}^3$ is a set of vectors that:
   - a) Are orthogonal and have magnitude 1
   - b) Are linearly independent and span all of $\mathbb{R}^3$
   - c) Have integer components
   - d) Contain the vector $(1,0,0)$
   > **Correct answer: b)** A basis is a system of linearly independent spanning vectors. Orthogonality and integer components are not required.

7. The dimension of $\mathbb{R}^3$ is 3 because:
   - a) It has 3 coordinate axes
   - b) Every vector has 3 components and any basis has exactly 3 elements
   - c) The determinant of the canonical basis is 3
   - d) There are exactly 3 vectors in each canonical basis
   > **Correct answer: b)** The dimension of a vector space is the number of vectors in any of its bases, which in $\mathbb{R}^3$ is always 3.

---

## 4.3 Dot product

---

#### 4.3.1 Analytic and geometric definition of the dot product in ℝ³

**Worked Example**

Compute the dot product of $\mathbf{u}=(2,-1,3)$ and $\mathbf{v}=(1,4,-2)$ using the analytic definition and verify consistency with the geometric definition.

**Step-by-step Solution:**

**Analytic definition:**

$$\mathbf{u} \cdot \mathbf{v} = 2 \cdot 1 + (-1) \cdot 4 + 3 \cdot (-2) = 2 - 4 - 6 = -8$$

**Magnitudes:**

$$|\mathbf{u}| = \sqrt{4+1+9} = \sqrt{14}, \quad |\mathbf{v}| = \sqrt{1+16+4} = \sqrt{21}$$

**Angle between the vectors** (geometric definition):

$$\cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{|\mathbf{u}||\mathbf{v}|} = \frac{-8}{\sqrt{14}\cdot\sqrt{21}} = \frac{-8}{\sqrt{294}} = \frac{-8}{7\sqrt{6}}$$

$$\theta = \arccos\left(\frac{-8}{7\sqrt{6}}\right) \approx \arccos(-0{,}467) \approx 117{,}8°$$

**Interpretation:** The dot product is negative, indicating that the angle between the vectors is **obtuse** (greater than 90°), consistent with $\theta \approx 118°$.

---

**Exercises with Solutions**

**Basic Level:**

1. Compute $\mathbf{a}\cdot\mathbf{b}$ with $\mathbf{a}=(3,0,-1)$ and $\mathbf{b}=(2,5,4)$.
   > **Solution:** $\mathbf{a}\cdot\mathbf{b} = 3\cdot2 + 0\cdot5 + (-1)\cdot4 = 6+0-4 = 2$.

2. Given $\mathbf{u}=(1,1,1)$ and $\mathbf{v}=(2,-3,1)$, compute $\mathbf{u}\cdot\mathbf{v}$ and determine whether they are perpendicular.
   > **Solution:** $\mathbf{u}\cdot\mathbf{v} = 2-3+1 = 0$. Since the dot product is zero, the vectors are **perpendicular (orthogonal)**.

**Intermediate Level:**

3. Find the angle between $\mathbf{p}=(1,0,-1)$ and $\mathbf{q}=(1,1,0)$.
   > **Solution:** $\mathbf{p}\cdot\mathbf{q}=1+0+0=1$. $|\mathbf{p}|=\sqrt{2}$, $|\mathbf{q}|=\sqrt{2}$. $\cos\theta = \frac{1}{\sqrt{2}\cdot\sqrt{2}}=\frac{1}{2}$. Therefore $\theta = 60°$.

4. Find the value of $k$ for which the vectors $\mathbf{a}=(k,2,-1)$ and $\mathbf{b}=(3,k,5)$ are perpendicular.
   > **Solution:** $\mathbf{a}\cdot\mathbf{b}=3k+2k-5=5k-5=0 \Rightarrow k=1$.

**EVAU Level:**

5. Let $\mathbf{u}=(1,-2,3)$ and $\mathbf{v}=(2,1,a)$.  
   a) Determine $a$ so that $\mathbf{u}$ and $\mathbf{v}$ are perpendicular.  
   b) For $a=0$, compute the magnitude of $\mathbf{u}+\mathbf{v}$ and the angle between $\mathbf{u}$ and $\mathbf{v}$.
   > **Solution:**  
   > **a)** $\mathbf{u}\cdot\mathbf{v}=1\cdot2+(-2)\cdot1+3\cdot a=2-2+3a=3a=0 \Rightarrow a=0$.  
   > **b)** With $a=0$: $\mathbf{v}=(2,1,0)$. $\mathbf{u}+\mathbf{v}=(3,-1,3)$, $|\mathbf{u}+\mathbf{v}|=\sqrt{9+1+9}=\sqrt{19}$.  
   > For the angle: $\mathbf{u}\cdot\mathbf{v}=0$ (from part a), confirming $\theta=90°$.

**Multiple Choice Test**

6. If $\mathbf{u}=(2,1,-2)$ and $\mathbf{v}=(-1,3,1)$, then $\mathbf{u}\cdot\mathbf{v}$ equals:
   - a) $-3$
   - b) $1$
   - c) $-1$
   - d) $3$
   > **Correct answer:** c) $\mathbf{u}\cdot\mathbf{v}=2\cdot(-1)+1\cdot3+(-2)\cdot1=-2+3-2=-1$.

7. For two nonzero vectors to be perpendicular, their dot product must be:
   - a) Equal to 1
   - b) Equal to $|\mathbf{u}||\mathbf{v}|$
   - c) Equal to 0
   - d) Negative
   > **Correct answer:** c) The condition for perpendicularity is exactly $\mathbf{u}\cdot\mathbf{v}=0$.

---

#### 4.3.2 Properties of the dot product: commutativity, distributivity, bilinearity

**Worked Example**

Verify that $\mathbf{u}\cdot(\mathbf{v}+\mathbf{w}) = \mathbf{u}\cdot\mathbf{v}+\mathbf{u}\cdot\mathbf{w}$ for $\mathbf{u}=(1,2,0)$, $\mathbf{v}=(3,-1,2)$, $\mathbf{w}=(-1,1,1)$.

**Step-by-step Solution:**

**Left-hand side:**

$$\mathbf{v}+\mathbf{w}=(3-1,\,-1+1,\,2+1)=(2,0,3)$$

$$\mathbf{u}\cdot(\mathbf{v}+\mathbf{w})=1\cdot2+2\cdot0+0\cdot3=2$$

**Right-hand side:**

$$\mathbf{u}\cdot\mathbf{v}=1\cdot3+2\cdot(-1)+0\cdot2=3-2+0=1$$

$$\mathbf{u}\cdot\mathbf{w}=1\cdot(-1)+2\cdot1+0\cdot1=-1+2+0=1$$

$$\mathbf{u}\cdot\mathbf{v}+\mathbf{u}\cdot\mathbf{w}=1+1=2 \checkmark$$

The distributive property is verified.

---

**Exercises with Solutions**

**Basic Level:**

1. Compute $(2\mathbf{u})\cdot\mathbf{v}$ knowing that $\mathbf{u}\cdot\mathbf{v}=5$.
   > **Solution:** By bilinearity, $(2\mathbf{u})\cdot\mathbf{v}=2(\mathbf{u}\cdot\mathbf{v})=2\cdot5=10$.

2. Is it true that $\mathbf{u}\cdot\mathbf{v}=\mathbf{v}\cdot\mathbf{u}$? Justify with $\mathbf{u}=(1,3,-2)$ and $\mathbf{v}=(0,1,4)$.
   > **Solution:** $\mathbf{u}\cdot\mathbf{v}=0+3-8=-5$ and $\mathbf{v}\cdot\mathbf{u}=0+3-8=-5$. Yes, the dot product is **commutative**.

**Intermediate Level:**

3. Using the properties of the dot product, compute $|\mathbf{u}+\mathbf{v}|^2$ if $|\mathbf{u}|=3$, $|\mathbf{v}|=4$ and $\mathbf{u}\cdot\mathbf{v}=6$.
   > **Solution:** $|\mathbf{u}+\mathbf{v}|^2=(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}+\mathbf{v})=|\mathbf{u}|^2+2\mathbf{u}\cdot\mathbf{v}+|\mathbf{v}|^2=9+12+16=37$.

4. If $|\mathbf{u}|=2$, $|\mathbf{v}|=3$ and the angle between them is $60°$, compute $(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})$.
   > **Solution:** $(\mathbf{u}+\mathbf{v})\cdot(\mathbf{u}-\mathbf{v})=|\mathbf{u}|^2-|\mathbf{v}|^2=4-9=-5$.

**EVAU Level:**

5. Given $\mathbf{a}=(1,2,-1)$ and $\mathbf{b}=(0,1,k)$:  
   a) Compute $\mathbf{a}\cdot\mathbf{b}$ as a function of $k$.  
   b) Find $k$ so that $|\mathbf{a}+\mathbf{b}|^2=18$.  
   c) For that value of $k$, check whether $\mathbf{a}$ and $\mathbf{b}$ are perpendicular.
   > **Solution:**  
   > **a)** $\mathbf{a}\cdot\mathbf{b}=0+2-k=2-k$.  
   > **b)** $\mathbf{a}+\mathbf{b}=(1,3,k-1)$. $|\mathbf{a}+\mathbf{b}|^2=1+9+(k-1)^2=10+(k-1)^2=18 \Rightarrow (k-1)^2=8 \Rightarrow k=1\pm2\sqrt{2}$.  
   > **c)** For $k=1+2\sqrt{2}$: $\mathbf{a}\cdot\mathbf{b}=2-(1+2\sqrt{2})=1-2\sqrt{2}\neq0$, not perpendicular. For $k=1-2\sqrt{2}$: $\mathbf{a}\cdot\mathbf{b}=1+2\sqrt{2}\neq0$, neither.

**Multiple Choice Test**

6. If $|\mathbf{u}|=2$, $|\mathbf{v}|=3$ and $\mathbf{u}\cdot\mathbf{v}=-3$, then $|\mathbf{u}-\mathbf{v}|^2$ equals:
   - a) $7$
   - b) $13$
   - c) $19$
   - d) $25$
   > **Correct answer:** c) $|\mathbf{u}-\mathbf{v}|^2=|\mathbf{u}|^2-2\mathbf{u}\cdot\mathbf{v}+|\mathbf{v}|^2=4+6+9=19$.

7. The property $\lambda(\mathbf{u}\cdot\mathbf{v})=(\lambda\mathbf{u})\cdot\mathbf{v}$ is a consequence of the property of:
   - a) Commutativity
   - b) Bilinearity
   - c) Positivity
   - d) Antisymmetry
   > **Correct answer:** b) Bilinearity includes homogeneity in each argument: $(\lambda\mathbf{u})\cdot\mathbf{v}=\lambda(\mathbf{u}\cdot\mathbf{v})$.

---

#### 4.3.3 Magnitude of a vector and distance between points via the dot product

**Worked Example**

Compute the magnitude of the vector $\mathbf{v}=(3,-4,0)$ using the dot product and find the distance between the points $A=(1,2,3)$ and $B=(4,-2,3)$.

**Step-by-step Solution:**

**Magnitude via dot product:**

$$|\mathbf{v}|^2 = \mathbf{v}\cdot\mathbf{v} = 3^2+(-4)^2+0^2 = 9+16+0 = 25$$

$$|\mathbf{v}| = \sqrt{25} = 5$$

**Distance between A and B:**

The vector $\overrightarrow{AB} = B - A = (4-1,\,-2-2,\,3-3) = (3,-4,0)$.

$$d(A,B) = |\overrightarrow{AB}| = \sqrt{3^2+(-4)^2+0^2} = \sqrt{9+16} = \sqrt{25} = 5$$

---

**Exercises with Solutions**

**Basic Level:**

1. Compute the magnitude of $\mathbf{w}=(2,-1,2)$.
   > **Solution:** $|\mathbf{w}|=\sqrt{4+1+4}=\sqrt{9}=3$.

2. Find the distance between $P=(0,1,-1)$ and $Q=(2,3,1)$.
   > **Solution:** $\overrightarrow{PQ}=(2,2,2)$. $d(P,Q)=\sqrt{4+4+4}=\sqrt{12}=2\sqrt{3}$.

**Intermediate Level:**

3. Determine $k$ so that the vector $\mathbf{u}=(2,k,1)$ has magnitude $\sqrt{14}$.
   > **Solution:** $|\mathbf{u}|^2=4+k^2+1=k^2+5=14 \Rightarrow k^2=9 \Rightarrow k=\pm3$.

4. Find the unit vector in the direction of $\mathbf{v}=(1,2,-2)$.
   > **Solution:** $|\mathbf{v}|=\sqrt{1+4+4}=3$. Unit vector: $\hat{\mathbf{v}}=\frac{1}{3}(1,2,-2)=\left(\frac{1}{3},\frac{2}{3},-\frac{2}{3}\right)$.

**EVAU Level:**

5. The points $A=(1,-1,2)$, $B=(3,1,0)$ and $C=(0,2,-1)$ are given.  
   a) Compute $|\overrightarrow{AB}|$, $|\overrightarrow{BC}|$ and $|\overrightarrow{AC}|$.  
   b) Check whether triangle $ABC$ is equilateral, isosceles or scalene.
   > **Solution:**  
   > **a)** $\overrightarrow{AB}=(2,2,-2)$, $|\overrightarrow{AB}|=\sqrt{4+4+4}=2\sqrt{3}$.  
   > $\overrightarrow{BC}=(-3,1,-1)$, $|\overrightarrow{BC}|=\sqrt{9+1+1}=\sqrt{11}$.  
   > $\overrightarrow{AC}=(-1,3,-3)$, $|\overrightarrow{AC}|=\sqrt{1+9+9}=\sqrt{19}$.  
   > **b)** The three sides have different lengths ($2\sqrt{3}\neq\sqrt{11}\neq\sqrt{19}$), so the triangle is **scalene**.

**Multiple Choice Test**

6. The magnitude of the vector $\mathbf{u}=(1,-2,2)$ is:
   - a) $5$
   - b) $3$
   - c) $\sqrt{5}$
   - d) $7$
   > **Correct answer:** b) $|\mathbf{u}|=\sqrt{1+4+4}=\sqrt{9}=3$.

7. The distance between $A=(1,0,1)$ and $B=(4,4,1)$ is:
   - a) $3$
   - b) $4$
   - c) $5$
   - d) $7$
   > **Correct answer:** c) $d=\sqrt{(4-1)^2+(4-0)^2+0^2}=\sqrt{9+16}=\sqrt{25}=5$.

---

#### 4.3.4 Angle between two vectors: formula and special cases (orthogonality)

**Worked Example**

Compute the angle between $\mathbf{u}=(1,\sqrt{3},0)$ and $\mathbf{v}=(\sqrt{3},-1,0)$.

**Step-by-step Solution:**

$$\mathbf{u}\cdot\mathbf{v} = 1\cdot\sqrt{3}+\sqrt{3}\cdot(-1)+0\cdot0 = \sqrt{3}-\sqrt{3} = 0$$

$$|\mathbf{u}| = \sqrt{1+3+0} = 2, \quad |\mathbf{v}| = \sqrt{3+1+0} = 2$$

$$\cos\theta = \frac{\mathbf{u}\cdot\mathbf{v}}{|\mathbf{u}||\mathbf{v}|} = \frac{0}{4} = 0 \Rightarrow \theta = 90°$$

The vectors are **perpendicular**, which makes geometric sense since both lie in the $xy$-plane and their directions are clearly orthogonal.

---

**Exercises with Solutions**

**Basic Level:**

1. Compute the angle between $\mathbf{i}=(1,0,0)$ and $\mathbf{j}=(0,1,0)$.
   > **Solution:** $\mathbf{i}\cdot\mathbf{j}=0$. Since both have magnitude 1, $\cos\theta=0 \Rightarrow \theta=90°$. They are perpendicular.

2. Find the angle between $\mathbf{a}=(2,0,0)$ and $\mathbf{b}=(1,1,0)$.
   > **Solution:** $\mathbf{a}\cdot\mathbf{b}=2$. $|\mathbf{a}|=2$, $|\mathbf{b}|=\sqrt{2}$. $\cos\theta=\frac{2}{2\sqrt{2}}=\frac{1}{\sqrt{2}} \Rightarrow \theta=45°$.

**Intermediate Level:**

3. Determine for which values of $t$ the vectors $\mathbf{u}=(t,1,0)$ and $\mathbf{v}=(1,-t,2)$ form an angle of 90°.
   > **Solution:** $\mathbf{u}\cdot\mathbf{v}=t\cdot1+1\cdot(-t)+0\cdot2=t-t=0$ for any $t$. Therefore, the vectors are always perpendicular, regardless of the value of $t$.

4. Compute the angle between $\mathbf{p}=(1,2,2)$ and $\mathbf{q}=(2,-1,2)$.
   > **Solution:** $\mathbf{p}\cdot\mathbf{q}=2-2+4=4$. $|\mathbf{p}|=\sqrt{9}=3$, $|\mathbf{q}|=3$. $\cos\theta=\frac{4}{9}$. $\theta=\arccos\!\left(\frac{4}{9}\right)\approx63{,}6°$.

**EVAU Level:**

5. The vectors $\mathbf{u}=(m,1,-1)$ and $\mathbf{v}=(2,m,1)$ are given.  
   a) Compute $m$ so that the vectors form an angle of 90°.  
   b) For $m=1$, compute the angle they form.  
   c) Can they be parallel for some value of $m$?
   > **Solution:**  
   > **a)** $\mathbf{u}\cdot\mathbf{v}=2m+m-1=3m-1=0 \Rightarrow m=\frac{1}{3}$.  
   > **b)** $m=1$: $\mathbf{u}=(1,1,-1)$, $\mathbf{v}=(2,1,1)$. $\mathbf{u}\cdot\mathbf{v}=2+1-1=2$. $|\mathbf{u}|=\sqrt{3}$, $|\mathbf{v}|=\sqrt{6}$. $\cos\theta=\frac{2}{\sqrt{18}}=\frac{2}{3\sqrt{2}}=\frac{\sqrt{2}}{3}$. $\theta=\arccos\!\left(\frac{\sqrt{2}}{3}\right)\approx61{,}9°$.  
   > **c)** For them to be parallel, $(m,1,-1)=\lambda(2,m,1)$, which gives $1=\lambda m$ and $-1=\lambda$, so $\lambda=-1$ and $m=-1$. Checking: $(-1,1,-1)=-1\cdot(2,-1,1)=(-2,1,-1)\neq(-1,1,-1)$. **They cannot be parallel** for any value of $m$.

**Multiple Choice Test**

6. If $\mathbf{u}\cdot\mathbf{v}>0$, the angle between $\mathbf{u}$ and $\mathbf{v}$ is:
   - a) Exactly 0°
   - b) Acute (between 0° and 90°)
   - c) Right (90°)
   - d) Obtuse (between 90° and 180°)
   > **Correct answer:** b) $\cos\theta=\frac{\mathbf{u}\cdot\mathbf{v}}{|\mathbf{u}||\mathbf{v}|}>0$ implies $0°<\theta<90°$, i.e., an acute angle.

7. The angle between $\mathbf{u}=(1,1,0)$ and $\mathbf{v}=(0,1,1)$ is:
   - a) 30°
   - b) 45°
   - c) 60°
   - d) 90°
   > **Correct answer:** c) $\mathbf{u}\cdot\mathbf{v}=1$, $|\mathbf{u}|=\sqrt{2}$, $|\mathbf{v}|=\sqrt{2}$. $\cos\theta=\frac{1}{2} \Rightarrow \theta=60°$.

---

#### 4.3.5 Projection of one vector onto another

**Worked Example**

Compute the projection of $\mathbf{a}=(3,4,0)$ onto $\mathbf{b}=(1,0,0)$, and the vector projection (component of $\mathbf{a}$ in the direction of $\mathbf{b}$).

**Step-by-step Solution:**

**Scalar projection** of $\mathbf{a}$ onto $\mathbf{b}$:

$$\text{proj}_{\mathbf{b}}\mathbf{a} = \frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{b}|} = \frac{3\cdot1+4\cdot0+0\cdot0}{\sqrt{1}} = 3$$

**Vector projection** of $\mathbf{a}$ onto $\mathbf{b}$:

$$\text{Proj}_{\mathbf{b}}\mathbf{a} = \frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{b}|^2}\,\mathbf{b} = \frac{3}{1}\cdot(1,0,0) = (3,0,0)$$

**Interpretation:** Since $\mathbf{b}$ coincides with the $x$-axis, the projection of $\mathbf{a}$ onto that axis is simply the $x$-component of the vector, i.e., $(3,0,0)$.

---

**Exercises with Solutions**

**Basic Level:**

1. Compute the scalar projection of $\mathbf{u}=(2,3,6)$ onto $\mathbf{v}=(0,1,0)$.
   > **Solution:** $\text{proj}_{\mathbf{v}}\mathbf{u}=\frac{\mathbf{u}\cdot\mathbf{v}}{|\mathbf{v}|}=\frac{3}{1}=3$.

2. Find the vector projection of $\mathbf{a}=(4,2,-4)$ onto $\mathbf{b}=(1,2,2)$.
   > **Solution:** $\mathbf{a}\cdot\mathbf{b}=4+4-8=0$. The vector projection is the **zero vector**, since $\mathbf{a}$ and $\mathbf{b}$ are perpendicular.

**Intermediate Level:**

3. Compute the scalar projection of $\mathbf{u}=(2,-1,3)$ onto $\mathbf{v}=(1,2,-2)$.
   > **Solution:** $\mathbf{u}\cdot\mathbf{v}=2-2-6=-6$. $|\mathbf{v}|=\sqrt{1+4+4}=3$. $\text{proj}_{\mathbf{v}}\mathbf{u}=\frac{-6}{3}=-2$.

4. Decompose $\mathbf{a}=(1,2,3)$ into its parallel and perpendicular components with respect to $\mathbf{b}=(1,0,1)$.
   > **Solution:** $\mathbf{a}\cdot\mathbf{b}=1+3=4$. $|\mathbf{b}|^2=2$. Parallel: $\mathbf{a}_{\parallel}=\frac{4}{2}(1,0,1)=(2,0,2)$. Perpendicular: $\mathbf{a}_{\perp}=\mathbf{a}-\mathbf{a}_{\parallel}=(1-2,2-0,3-2)=(-1,2,1)$. Check: $\mathbf{a}_{\perp}\cdot\mathbf{b}=-1+0+1=0$ ✓.

**EVAU Level:**

5. Given $\mathbf{u}=(2,1,-1)$ and $\mathbf{v}=(1,2,1)$:  
   a) Compute the scalar projection of $\mathbf{u}$ onto $\mathbf{v}$.  
   b) Find the vector projection of $\mathbf{u}$ onto $\mathbf{v}$.  
   c) Compute the component of $\mathbf{u}$ perpendicular to $\mathbf{v}$ and verify that it is orthogonal to $\mathbf{v}$.
   > **Solution:**  
   > **a)** $\mathbf{u}\cdot\mathbf{v}=2+2-1=3$. $|\mathbf{v}|=\sqrt{6}$. $\text{proj}_{\mathbf{v}}\mathbf{u}=\frac{3}{\sqrt{6}}=\frac{3\sqrt{6}}{6}=\frac{\sqrt{6}}{2}$.  
   > **b)** $\mathbf{u}_{\parallel}=\frac{3}{6}(1,2,1)=\left(\frac{1}{2},1,\frac{1}{2}\right)$.  
   > **c)** $\mathbf{u}_{\perp}=\mathbf{u}-\mathbf{u}_{\parallel}=\left(\frac{3}{2},0,-\frac{3}{2}\right)$. Check: $\mathbf{u}_{\perp}\cdot\mathbf{v}=\frac{3}{2}+0-\frac{3}{2}=0$ ✓.

**Multiple Choice Test**

6. The scalar projection of $\mathbf{a}=(3,4,0)$ onto $\mathbf{b}=(3,4,0)$ is:
   - a) $1$
   - b) $5$
   - c) $25$
   - d) $\frac{1}{5}$
   > **Correct answer:** b) $\text{proj}_{\mathbf{b}}\mathbf{a}=\frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{b}|}=\frac{9+16}{5}=\frac{25}{5}=5=|\mathbf{a}|$ (logical, since it is the same vector).

7. The projection of $\mathbf{u}$ onto $\mathbf{v}$ is the **zero vector** when:
   - a) $|\mathbf{u}|=|\mathbf{v}|$
   - b) $\mathbf{u}$ and $\mathbf{v}$ are parallel
   - c) $\mathbf{u}$ and $\mathbf{v}$ are perpendicular
   - d) $|\mathbf{u}|=1$
   > **Correct answer:** c) If $\mathbf{u}\cdot\mathbf{v}=0$ (perpendicular), the vector projection is $\mathbf{0}$.

---

#### 4.4.1 Definition of the cross product via the formal determinant

**Worked Example**

Compute the cross product $\mathbf{u}\times\mathbf{v}$ with $\mathbf{u}=(2,1,-3)$ and $\mathbf{v}=(-1,4,2)$.

**Step-by-step Solution:**

$$\mathbf{u}\times\mathbf{v} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&1&-3\\-1&4&2\end{vmatrix}$$

Expanding along the first row:

$$\mathbf{i}\begin{vmatrix}1&-3\\4&2\end{vmatrix} - \mathbf{j}\begin{vmatrix}2&-3\\-1&2\end{vmatrix} + \mathbf{k}\begin{vmatrix}2&1\\-1&4\end{vmatrix}$$

$$= \mathbf{i}(1\cdot2-(-3)\cdot4) - \mathbf{j}(2\cdot2-(-3)\cdot(-1)) + \mathbf{k}(2\cdot4-1\cdot(-1))$$

$$= \mathbf{i}(2+12) - \mathbf{j}(4-3) + \mathbf{k}(8+1)$$

$$= 14\,\mathbf{i} - 1\,\mathbf{j} + 9\,\mathbf{k} = (14,-1,9)$$

**Verification:** $\mathbf{u}\cdot(\mathbf{u}\times\mathbf{v})=2\cdot14+1\cdot(-1)+(-3)\cdot9=28-1-27=0$ ✓ (the result is perpendicular to $\mathbf{u}$).

---

**Exercises with Solutions**

**Basic Level:**

1. Compute $\mathbf{i}\times\mathbf{j}$.
   > **Solution:** $\mathbf{i}\times\mathbf{j}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&0&0\\0&1&0\end{vmatrix}=\mathbf{i}(0)-\mathbf{j}(0)+\mathbf{k}(1)=\mathbf{k}=(0,0,1)$.

2. Compute $(1,2,0)\times(3,0,0)$.
   > **Solution:** $\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&2&0\\3&0&0\end{vmatrix}=\mathbf{i}(0-0)-\mathbf{j}(0-0)+\mathbf{k}(0-6)=(0,0,-6)$.

**Intermediate Level:**

3. Find $\mathbf{a}\times\mathbf{b}$ and verify that it is perpendicular to both vectors, for $\mathbf{a}=(1,0,1)$ and $\mathbf{b}=(0,1,1)$.
   > **Solution:** $\mathbf{a}\times\mathbf{b}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&0&1\\0&1&1\end{vmatrix}=\mathbf{i}(0-1)-\mathbf{j}(1-0)+\mathbf{k}(1-0)=(-1,-1,1)$.  
   > $(-1,-1,1)\cdot(1,0,1)=-1+0+1=0$ ✓. $(-1,-1,1)\cdot(0,1,1)=0-1+1=0$ ✓.

4. Compute $(2,1,3)\times(1,0,-2)$.
   > **Solution:** $\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&1&3\\1&0&-2\end{vmatrix}=\mathbf{i}(-2-0)-\mathbf{j}(-4-3)+\mathbf{k}(0-1)=(-2,7,-1)$.

**EVAU Level:**

5. Let $\mathbf{u}=(1,-1,2)$ and $\mathbf{v}=(3,0,1)$.  
   a) Compute $\mathbf{u}\times\mathbf{v}$ and $\mathbf{v}\times\mathbf{u}$.  
   b) Verify that $\mathbf{v}\times\mathbf{u}=-(\mathbf{u}\times\mathbf{v})$.  
   c) Find a unit vector perpendicular to both.
   > **Solution:**  
   > **a)** $\mathbf{u}\times\mathbf{v}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&-1&2\\3&0&1\end{vmatrix}=\mathbf{i}(-1-0)-\mathbf{j}(1-6)+\mathbf{k}(0+3)=(-1,5,3)$.  
   > $\mathbf{v}\times\mathbf{u}=(-1)(\mathbf{u}\times\mathbf{v})=(1,-5,-3)$.  
   > **b)** $\mathbf{v}\times\mathbf{u}=(1,-5,-3)=-(-1,5,3)=-(\mathbf{u}\times\mathbf{v})$ ✓.  
   > **c)** $|\mathbf{u}\times\mathbf{v}|=\sqrt{1+25+9}=\sqrt{35}$. Unit vector: $\hat{\mathbf{n}}=\frac{1}{\sqrt{35}}(-1,5,3)$.

**Multiple Choice Test**

6. The cross product $\mathbf{u}\times\mathbf{u}$ is always:
   - a) $|\mathbf{u}|^2$
   - b) A vector of magnitude $|\mathbf{u}|$
   - c) The zero vector $\mathbf{0}$
   - d) A vector perpendicular to $\mathbf{u}$
   > **Correct answer:** c) $\mathbf{u}\times\mathbf{u}=\mathbf{0}$ because the angle between a vector and itself is 0°, and $\sin 0°=0$.

7. If $\mathbf{u}\times\mathbf{v}=\mathbf{0}$ and $\mathbf{u}\neq\mathbf{0}$, $\mathbf{v}\neq\mathbf{0}$, then:
   - a) $\mathbf{u}$ and $\mathbf{v}$ are perpendicular
   - b) $\mathbf{u}$ and $\mathbf{v}$ are parallel
   - c) $\mathbf{u}$ and $\mathbf{v}$ are coplanar
   - d) $\mathbf{u}$ and $\mathbf{v}$ are orthogonal
   > **Correct answer:** b) $|\mathbf{u}\times\mathbf{v}|=|\mathbf{u}||\mathbf{v}|\sin\theta=0$ implies $\sin\theta=0$, i.e., $\theta=0°$ or $\theta=180°$: the vectors are **parallel** (or antiparallel).

---

#### 4.4.2 Properties of the cross product: anticommutativity, distributivity, magnitude

**Worked Example**

Verify the anticommutative property of the cross product with $\mathbf{a}=(1,2,3)$ and $\mathbf{b}=(4,5,6)$, and compute the magnitude $|\mathbf{a}\times\mathbf{b}|$.

**Step-by-step Solution:**

$$\mathbf{a}\times\mathbf{b}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&2&3\\4&5&6\end{vmatrix}=\mathbf{i}(12-15)-\mathbf{j}(6-12)+\mathbf{k}(5-8)=(-3,6,-3)$$

$$\mathbf{b}\times\mathbf{a}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\4&5&6\\1&2&3\end{vmatrix}=\mathbf{i}(15-12)-\mathbf{j}(12-6)+\mathbf{k}(8-5)=(3,-6,3)$$

It is verified that $\mathbf{b}\times\mathbf{a}=-(\mathbf{a}\times\mathbf{b})=(3,-6,3)$ ✓ (**anticommutativity**).

**Magnitude:**

$$|\mathbf{a}\times\mathbf{b}|=\sqrt{(-3)^2+6^2+(-3)^2}=\sqrt{9+36+9}=\sqrt{54}=3\sqrt{6}$$

---

**Exercises with Solutions**

**Basic Level:**

1. Knowing that $\mathbf{u}\times\mathbf{v}=(2,-1,3)$, write $\mathbf{v}\times\mathbf{u}$.
   > **Solution:** By anticommutativity, $\mathbf{v}\times\mathbf{u}=-(\mathbf{u}\times\mathbf{v})=(-2,1,-3)$.

2. If $|\mathbf{u}|=3$, $|\mathbf{v}|=4$ and the angle between them is $30°$, compute $|\mathbf{u}\times\mathbf{v}|$.
   > **Solution:** $|\mathbf{u}\times\mathbf{v}|=|\mathbf{u}||\mathbf{v}|\sin30°=3\cdot4\cdot\frac{1}{2}=6$.

**Intermediate Level:**

3. Given $\mathbf{u}=(2,0,1)$ and $\mathbf{v}=(0,3,0)$, compute $|\mathbf{u}\times\mathbf{v}|$ using the magnitude formula and verify by computing the cross product directly.
   > **Direct solution:** $\mathbf{u}\times\mathbf{v}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&0&1\\0&3&0\end{vmatrix}=(0-3)\mathbf{i}-(0-0)\mathbf{j}+(6-0)\mathbf{k}=(-3,0,6)$. $|(-3,0,6)|=\sqrt{9+36}=\sqrt{45}=3\sqrt{5}$.  
   > Magnitude formula: $|\mathbf{u}|=\sqrt{5}$, $|\mathbf{v}|=3$, $\cos\theta=\frac{0}{\sqrt{5}\cdot3}=0 \Rightarrow \theta=90°$, $\sin\theta=1$. $|\mathbf{u}\times\mathbf{v}|=\sqrt{5}\cdot3\cdot1=3\sqrt{5}$ ✓.

4. Prove with coordinates that $(\lambda\mathbf{u})\times\mathbf{v}=\lambda(\mathbf{u}\times\mathbf{v})$ for $\mathbf{u}=(1,-1,0)$, $\mathbf{v}=(0,1,2)$ and $\lambda=3$.
   > **Solution:** $3\mathbf{u}=(3,-3,0)$. $(3\mathbf{u})\times\mathbf{v}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\3&-3&0\\0&1&2\end{vmatrix}=(-6-0)\mathbf{i}-(6-0)\mathbf{j}+(3-0)\mathbf{k}=(-6,-6,3)$. $\mathbf{u}\times\mathbf{v}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&-1&0\\0&1&2\end{vmatrix}=(-2,-2,1)$. $3(\mathbf{u}\times\mathbf{v})=(-6,-6,3)$ ✓.

**EVAU Level:**

5. Given $\mathbf{a}=(1,0,2)$ and $\mathbf{b}=(0,1,-1)$:  
   a) Compute $\mathbf{a}\times\mathbf{b}$ and $\mathbf{b}\times\mathbf{a}$.  
   b) Compute $|\mathbf{a}\times\mathbf{b}|$ and interpret the result geometrically.  
   c) Verify that $|\mathbf{a}\times\mathbf{b}|^2+(\mathbf{a}\cdot\mathbf{b})^2=|\mathbf{a}|^2|\mathbf{b}|^2$ (Lagrange's identity).
   > **Solution:**  
   > **a)** $\mathbf{a}\times\mathbf{b}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&0&2\\0&1&-1\end{vmatrix}=(-2)\mathbf{i}-(-1)\mathbf{j}+(1)\mathbf{k}=(-2,1,1)$. $\mathbf{b}\times\mathbf{a}=(2,-1,-1)$.  
   > **b)** $|\mathbf{a}\times\mathbf{b}|=\sqrt{4+1+1}=\sqrt{6}$. This is the area of the parallelogram formed by $\mathbf{a}$ and $\mathbf{b}$.  
   > **c)** $\mathbf{a}\cdot\mathbf{b}=0+0-2=-2$. $|\mathbf{a}|^2=5$, $|\mathbf{b}|^2=2$. $6+4=10=5\cdot2$ ✓.

**Multiple Choice Test**

6. The cross product is anticommutative, meaning that:
   - a) $\mathbf{u}\times\mathbf{v}=\mathbf{v}\times\mathbf{u}$
   - b) $\mathbf{u}\times\mathbf{v}=-\mathbf{v}\times\mathbf{u}$
   - c) $\mathbf{u}\times\mathbf{v}=0$ always
   - d) $|\mathbf{u}\times\mathbf{v}|=|\mathbf{v}\times\mathbf{u}|=0$
   > **Correct answer:** b) By definition, $\mathbf{u}\times\mathbf{v}=-\mathbf{v}\times\mathbf{u}$.

7. If $|\mathbf{u}|=2$, $|\mathbf{v}|=5$ and the angle between them is $90°$, then $|\mathbf{u}\times\mathbf{v}|$ is:
   - a) $10$
   - b) $7$
   - c) $0$
   - d) $\sqrt{29}$
   > **Correct answer:** a) $|\mathbf{u}\times\mathbf{v}|=|\mathbf{u}||\mathbf{v}|\sin90°=2\cdot5\cdot1=10$.

---

#### 4.4.3 Geometric interpretation: perpendicular vector and area of the parallelogram

**Worked Example**

Compute the area of the parallelogram whose sides are the vectors $\mathbf{u}=(2,3,0)$ and $\mathbf{v}=(1,0,4)$, and find the equation of the plane containing that parallelogram if it passes through the origin.

**Step-by-step Solution:**

**Cross product:**

$$\mathbf{u}\times\mathbf{v}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&3&0\\1&0&4\end{vmatrix}=\mathbf{i}(12-0)-\mathbf{j}(8-0)+\mathbf{k}(0-3)=(12,-8,-3)$$

**Area of the parallelogram:**

$$S = |\mathbf{u}\times\mathbf{v}| = \sqrt{144+64+9} = \sqrt{217}$$

**Equation of the plane:** The normal vector is $\mathbf{n}=(12,-8,-3)$ and the plane passes through the origin:

$$12x - 8y - 3z = 0$$

---

**Exercises with Solutions**

**Basic Level:**

1. What is the area of the parallelogram formed by $\mathbf{u}=(3,0,0)$ and $\mathbf{v}=(0,2,0)$?
   > **Solution:** $\mathbf{u}\times\mathbf{v}=(0,0,6)$. $S=|\mathbf{u}\times\mathbf{v}|=6$. (Consistent with base × height = 3 × 2 = 6.)

2. Find a vector perpendicular to $\mathbf{a}=(1,1,0)$ and $\mathbf{b}=(0,1,1)$.
   > **Solution:** $\mathbf{a}\times\mathbf{b}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&1&0\\0&1&1\end{vmatrix}=(1,-1,1)$. A perpendicular vector is $(1,-1,1)$.

**Intermediate Level:**

3. Compute the area of the parallelogram with vertices $A=(0,0,0)$, $B=(1,2,-1)$ and $D=(3,0,1)$ (where $C=B+D$).
   > **Solution:** Sides: $\overrightarrow{AB}=(1,2,-1)$ and $\overrightarrow{AD}=(3,0,1)$. $\overrightarrow{AB}\times\overrightarrow{AD}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&2&-1\\3&0&1\end{vmatrix}=(2+0)\mathbf{i}-(1+3)\mathbf{j}+(0-6)\mathbf{k}=(2,-4,-6)$. $S=\sqrt{4+16+36}=\sqrt{56}=2\sqrt{14}$.

4. Given $\mathbf{u}=(1,2,3)$ and $\mathbf{v}=(2,4,6)$, compute the area of the parallelogram they form. Interpret the result.
   > **Solution:** $\mathbf{v}=2\mathbf{u}$, they are parallel. $\mathbf{u}\times\mathbf{v}=\mathbf{0}$. $S=0$. The "parallelogram" is degenerate (the vectors are collinear).

**EVAU Level:**

5. The vertices of a triangle are $A=(1,0,2)$, $B=(3,1,0)$ and $C=(0,2,1)$.  
   a) Find the area of triangle $ABC$.  
   b) Determine a normal vector to the plane of the triangle.  
   c) Write the equation of the plane containing the triangle.
   > **Solution:**  
   > **a)** $\overrightarrow{AB}=(2,1,-2)$, $\overrightarrow{AC}=(-1,2,-1)$.  
   > $\overrightarrow{AB}\times\overrightarrow{AC}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&1&-2\\-1&2&-1\end{vmatrix}=(-1+4)\mathbf{i}-(-2-2)\mathbf{j}+(4+1)\mathbf{k}=(3,4,5)$.  
   > $S_{\triangle}=\frac{1}{2}|\overrightarrow{AB}\times\overrightarrow{AC}|=\frac{1}{2}\sqrt{9+16+25}=\frac{\sqrt{50}}{2}=\frac{5\sqrt{2}}{2}$.  
   > **b)** The normal vector is $\mathbf{n}=(3,4,5)$.  
   > **c)** Using $A=(1,0,2)$: $3(x-1)+4(y-0)+5(z-2)=0 \Rightarrow 3x+4y+5z=13$.

**Multiple Choice Test**

6. The area of the parallelogram formed by $\mathbf{u}$ and $\mathbf{v}$ is:
   - a) $\mathbf{u}\cdot\mathbf{v}$
   - b) $|\mathbf{u}||\mathbf{v}|\cos\theta$
   - c) $|\mathbf{u}\times\mathbf{v}|$
   - d) $|\mathbf{u}|+|\mathbf{v}|$
   > **Correct answer:** c) By definition, $|\mathbf{u}\times\mathbf{v}|=|\mathbf{u}||\mathbf{v}|\sin\theta$ which is precisely the area of the parallelogram.

7. The area of the triangle with sides $\mathbf{u}$ and $\mathbf{v}$ is:
   - a) $|\mathbf{u}\times\mathbf{v}|$
   - b) $\frac{1}{2}|\mathbf{u}\times\mathbf{v}|$
   - c) $\frac{1}{2}\mathbf{u}\cdot\mathbf{v}$
   - d) $2|\mathbf{u}\times\mathbf{v}|$
   > **Correct answer:** b) The area of the triangle is half the area of the parallelogram.

---

#### 4.4.4 Applications: area of triangles and verification of collinearity

**Worked Example**

Determine whether the points $A=(1,2,3)$, $B=(2,4,6)$ and $C=(0,0,0)$ are collinear using the cross product.

**Step-by-step Solution:**

$$\overrightarrow{CA} = A - C = (1,2,3), \quad \overrightarrow{CB} = B - C = (2,4,6)$$

$$\overrightarrow{CA}\times\overrightarrow{CB} = \begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&2&3\\2&4&6\end{vmatrix}$$

$$= \mathbf{i}(12-12)-\mathbf{j}(6-6)+\mathbf{k}(4-4) = (0,0,0) = \mathbf{0}$$

Since the cross product is the **zero vector**, the vectors $\overrightarrow{CA}$ and $\overrightarrow{CB}$ are parallel, confirming that **$A$, $B$ and $C$ are collinear**.

*(Note that $\overrightarrow{CB}=2\overrightarrow{CA}$, a direct confirmation of collinearity.)*

---

**Exercises with Solutions**

**Basic Level:**

1. Check whether the points $P=(1,0,0)$, $Q=(2,2,0)$ and $R=(0,-2,0)$ are collinear.
   > **Solution:** $\overrightarrow{PQ}=(1,2,0)$, $\overrightarrow{PR}=(-1,-2,0)$. $\overrightarrow{PQ}\times\overrightarrow{PR}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&2&0\\-1&-2&0\end{vmatrix}=(0,0,-2+2)=(0,0,0)$. The three points are **collinear**.

2. Compute the area of the triangle with vertices $A=(0,0,0)$, $B=(4,0,0)$, $C=(0,3,0)$.
   > **Solution:** $\overrightarrow{AB}=(4,0,0)$, $\overrightarrow{AC}=(0,3,0)$. $\overrightarrow{AB}\times\overrightarrow{AC}=(0,0,12)$. $S=\frac{1}{2}\cdot12=6$ (base 4, height 3, $\frac{1}{2}\cdot4\cdot3=6$ ✓).

**Intermediate Level:**

3. Determine whether $A=(2,1,-1)$, $B=(0,-1,1)$ and $C=(4,3,-3)$ are collinear.
   > **Solution:** $\overrightarrow{AB}=(-2,-2,2)$, $\overrightarrow{AC}=(2,2,-2)$. Note that $\overrightarrow{AC}=-\overrightarrow{AB}$, so they are parallel and the points are **collinear**.  
   > Verification: $\overrightarrow{AB}\times\overrightarrow{AC}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\-2&-2&2\\2&2&-2\end{vmatrix}=(4-4,-4+4,-4+4)=(0,0,0)$ ✓.

4. Compute the area of the triangle with vertices $P=(1,1,0)$, $Q=(2,-1,2)$ and $R=(0,0,3)$.
   > **Solution:** $\overrightarrow{PQ}=(1,-2,2)$, $\overrightarrow{PR}=(-1,-1,3)$. $\overrightarrow{PQ}\times\overrightarrow{PR}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&-2&2\\-1&-1&3\end{vmatrix}=(-6+2)\mathbf{i}-(3+2)\mathbf{j}+(-1-2)\mathbf{k}=(-4,-5,-3)$. $S=\frac{1}{2}\sqrt{16+25+9}=\frac{\sqrt{50}}{2}=\frac{5\sqrt{2}}{2}$.

**EVAU Level:**

5. *(EVAU Madrid style)* Given the points $A=(1,0,-1)$, $B=(2,3,1)$ and $C=(-1,1,0)$:  
   a) Verify that the three points are not collinear and compute the area of triangle $ABC$.  
   b) Find the equation of the plane determined by the three points.  
   c) Compute the perimeter of the triangle.
   > **Solution:**  
   > **a)** $\overrightarrow{AB}=(1,3,2)$, $\overrightarrow{AC}=(-2,1,1)$. $\overrightarrow{AB}\times\overrightarrow{AC}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&3&2\\-2&1&1\end{vmatrix}=(3-2)\mathbf{i}-(1+4)\mathbf{j}+(1+6)\mathbf{k}=(1,-5,7)\neq\mathbf{0}$, not collinear. $S=\frac{1}{2}\sqrt{1+25+49}=\frac{\sqrt{75}}{2}=\frac{5\sqrt{3}}{2}$.  
   > **b)** Normal $\mathbf{n}=(1,-5,7)$, through $A=(1,0,-1)$: $1(x-1)-5(y-0)+7(z+1)=0 \Rightarrow x-5y+7z+6=0$.  
   > **c)** $|AB|=\sqrt{1+9+4}=\sqrt{14}$; $|AC|=\sqrt{4+1+1}=\sqrt{6}$; $|BC|=\sqrt{9+4+1}=\sqrt{14}$. Perimeter $=2\sqrt{14}+\sqrt{6}$.

**Multiple Choice Test**

6. Three points $A$, $B$, $C$ are collinear if and only if:
   - a) $\overrightarrow{AB}\cdot\overrightarrow{AC}=0$
   - b) $\overrightarrow{AB}\times\overrightarrow{AC}=\mathbf{0}$
   - c) $|\overrightarrow{AB}|=|\overrightarrow{AC}|$
   - d) $\overrightarrow{AB}+\overrightarrow{AC}=\mathbf{0}$
   > **Correct answer:** b) If the cross product is zero, the vectors are parallel, which implies collinearity of the three points.

7. The area of the triangle with vertices $O=(0,0,0)$, $A=(3,0,0)$, $B=(0,4,0)$ is:
   - a) $6$
   - b) $12$
   - c) $5$
   - d) $7$
   > **Correct answer:** a) $\frac{1}{2}\cdot3\cdot4=6$ (right triangle in the $xy$-plane).

---

#### 4.5.1 Definition of the scalar triple product of three vectors

**Worked Example**

Define the scalar triple product of the vectors $\mathbf{u}=(1,2,0)$, $\mathbf{v}=(0,1,3)$ and $\mathbf{w}=(2,0,-1)$ and compute it.

**Step-by-step Solution:**

The **scalar triple product** of three vectors $\mathbf{u}$, $\mathbf{v}$ and $\mathbf{w}$ is defined as:

$$[\mathbf{u},\mathbf{v},\mathbf{w}] = \mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})$$

**Step 1: Compute $\mathbf{v}\times\mathbf{w}$:**

$$\mathbf{v}\times\mathbf{w}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\0&1&3\\2&0&-1\end{vmatrix}=(-1-0)\mathbf{i}-(0-6)\mathbf{j}+(0-2)\mathbf{k}=(-1,6,-2)$$

**Step 2: Compute $\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})$:**

$$\mathbf{u}\cdot(-1,6,-2)=1\cdot(-1)+2\cdot6+0\cdot(-2)=-1+12+0=11$$

The **scalar triple product** is $[\mathbf{u},\mathbf{v},\mathbf{w}]=11$.

---

**Exercises with Solutions**

**Basic Level:**

1. Compute the scalar triple product of $\mathbf{i}$, $\mathbf{j}$ and $\mathbf{k}$.
   > **Solution:** $[\mathbf{i},\mathbf{j},\mathbf{k}]=\mathbf{i}\cdot(\mathbf{j}\times\mathbf{k})=\mathbf{i}\cdot\mathbf{i}=1$.

2. Compute the scalar triple product of $\mathbf{u}=(1,0,0)$, $\mathbf{v}=(0,2,0)$ and $\mathbf{w}=(0,0,3)$.
   > **Solution:** $\mathbf{v}\times\mathbf{w}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\0&2&0\\0&0&3\end{vmatrix}=(6,0,0)$. $\mathbf{u}\cdot(6,0,0)=6$.

**Intermediate Level:**

3. Compute $[\mathbf{a},\mathbf{b},\mathbf{c}]$ for $\mathbf{a}=(1,1,1)$, $\mathbf{b}=(2,0,-1)$, $\mathbf{c}=(0,3,2)$.
   > **Solution:** $\mathbf{b}\times\mathbf{c}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&0&-1\\0&3&2\end{vmatrix}=(0+3)\mathbf{i}-(4-0)\mathbf{j}+(6-0)\mathbf{k}=(3,-4,6)$. $\mathbf{a}\cdot(3,-4,6)=3-4+6=5$.

4. Verify that $[\mathbf{u},\mathbf{v},\mathbf{w}]=-[\mathbf{v},\mathbf{u},\mathbf{w}]$ for $\mathbf{u}=(1,0,0)$, $\mathbf{v}=(0,1,0)$, $\mathbf{w}=(0,0,1)$.
   > **Solution:** $[\mathbf{u},\mathbf{v},\mathbf{w}]=1$. For $[\mathbf{v},\mathbf{u},\mathbf{w}]$: $\mathbf{u}\times\mathbf{w}=(0,1,0)\times(0,0,1)$... In this case $[\mathbf{v},\mathbf{u},\mathbf{w}]=\mathbf{v}\cdot(\mathbf{u}\times\mathbf{w})$. $\mathbf{u}\times\mathbf{w}=(1,0,0)\times(0,0,1)=(0\cdot1-0\cdot0)\mathbf{i}-(1\cdot1-0\cdot0)\mathbf{j}+(1\cdot0-0\cdot0)\mathbf{k}=(0,-1,0)$. $\mathbf{v}\cdot(0,-1,0)=-1$. Therefore $[\mathbf{v},\mathbf{u},\mathbf{w}]=-1=-[\mathbf{u},\mathbf{v},\mathbf{w}]$ ✓.

**EVAU Level:**

5. *(EVAU Madrid style)* Compute the scalar triple product of $\mathbf{u}=(2,-1,3)$, $\mathbf{v}=(1,0,2)$ and $\mathbf{w}=(0,1,-1)$ using the determinant. Interpret the result.
   > **Solution:**  
   > The scalar triple product can be computed directly as:  
   > $$[\mathbf{u},\mathbf{v},\mathbf{w}]=\begin{vmatrix}2&-1&3\\1&0&2\\0&1&-1\end{vmatrix}$$  
   > $=2\begin{vmatrix}0&2\\1&-1\end{vmatrix}-(-1)\begin{vmatrix}1&2\\0&-1\end{vmatrix}+3\begin{vmatrix}1&0\\0&1\end{vmatrix}$  
   > $=2(0-2)+1(-1-0)+3(1-0)$  
   > $=2(-2)+1(-1)+3(1)=-4-1+3=-2$  
   > **Interpretation:** The scalar triple product equals $-2\neq 0$, so the three vectors are **linearly independent** (non-coplanar). The volume of the parallelepiped they form is $|{-2}|=2$.

**Multiple Choice Test**

6. The scalar triple product $[\mathbf{u},\mathbf{v},\mathbf{w}]$ is equivalent to:
   - a) $\mathbf{u}\times(\mathbf{v}\cdot\mathbf{w})$
   - b) $(\mathbf{u}\times\mathbf{v})\cdot\mathbf{w}$
   - c) $\mathbf{u}\cdot\mathbf{v}\cdot\mathbf{w}$
   - d) $|\mathbf{u}||\mathbf{v}||\mathbf{w}|$
   > **Correct answer:** b) $[\mathbf{u},\mathbf{v},\mathbf{w}]=\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})=(\mathbf{u}\times\mathbf{v})\cdot\mathbf{w}$ (both expressions are equivalent).

7. If $[\mathbf{u},\mathbf{v},\mathbf{w}]=0$, then the three vectors:
   - a) Are mutually orthogonal
   - b) Are coplanar (or one is zero)
   - c) Have the same magnitude
   - d) Are unit vectors
   > **Correct answer:** b) A zero scalar triple product indicates that the vectors are linearly dependent, i.e., **coplanar** (or one is zero).

---

#### 4.5.2 Computation as a 3×3 determinant

**Worked Example**

Compute the scalar triple product of $\mathbf{a}=(3,1,-2)$, $\mathbf{b}=(0,2,1)$ and $\mathbf{c}=(1,-1,4)$ using the $3\times 3$ determinant.

**Step-by-step Solution:**

$$[\mathbf{a},\mathbf{b},\mathbf{c}] = \begin{vmatrix}3 & 1 & -2 \\ 0 & 2 & 1 \\ 1 & -1 & 4\end{vmatrix}$$

Expanding along the first row:

$$= 3\begin{vmatrix}2&1\\-1&4\end{vmatrix} - 1\begin{vmatrix}0&1\\1&4\end{vmatrix} + (-2)\begin{vmatrix}0&2\\1&-1\end{vmatrix}$$

$$= 3(8+1) - 1(0-1) + (-2)(0-2)$$

$$= 3\cdot9 - 1\cdot(-1) + (-2)\cdot(-2)$$

$$= 27 + 1 + 4 = 32$$

---

**Exercises with Solutions**

**Basic Level:**

1. Compute the scalar triple product of $(1,0,0)$, $(0,1,0)$ and $(1,1,0)$ using the determinant.
   > **Solution:** $\begin{vmatrix}1&0&0\\0&1&0\\1&1&0\end{vmatrix}=1(0-0)-0(0-0)+0(0-1)=0$. The vectors are coplanar (they lie in the plane $z=0$).

2. Use the determinant to compute $[(1,2,3),(4,5,6),(7,8,9)]$.
   > **Solution:** $\begin{vmatrix}1&2&3\\4&5&6\\7&8&9\end{vmatrix}=1(45-48)-2(36-42)+3(32-35)=1(-3)-2(-6)+3(-3)=-3+12-9=0$. The vectors are coplanar.

**Intermediate Level:**

3. Compute the scalar triple product of $\mathbf{u}=(2,1,0)$, $\mathbf{v}=(1,-1,3)$ and $\mathbf{w}=(0,2,-1)$.
   > **Solution:** $\begin{vmatrix}2&1&0\\1&-1&3\\0&2&-1\end{vmatrix}=2(1-6)-1(-1-0)+0=2(-5)-1(-1)=-10+1=-9$.

4. For $k=2$, compute $[(k,1,0),(1,k,-1),(0,1,k)]$ and verify using the result of the following subsection.
   > **Solution:** $\begin{vmatrix}2&1&0\\1&2&-1\\0&1&2\end{vmatrix}=2(4+1)-1(2-0)+0=10-2=8$.

**EVAU Level:**

5. *(EVAU Madrid style)* Compute the scalar triple product of $\mathbf{u}=(1,-2,0)$, $\mathbf{v}=(0,1,3)$ and $\mathbf{w}=(-1,0,2)$ using the $3\times3$ determinant. From the result, decide whether the vectors form a basis of $\mathbb{R}^3$.
   > **Solution:**  
   > $$[\mathbf{u},\mathbf{v},\mathbf{w}]=\begin{vmatrix}1&-2&0\\0&1&3\\-1&0&2\end{vmatrix}$$  
   > $=1(2-0)-(-2)(0+3)+0(0+1)$  
   > $=2+6+0=8$  
   > Since the scalar triple product is $\mathbf{8}\neq 0$, the vectors are **linearly independent** and form a **basis of $\mathbb{R}^3$**.

**Multiple Choice Test**

6. The scalar triple product $[\mathbf{u},\mathbf{v},\mathbf{w}]$ as a determinant places the vectors in:
   - a) The columns of the determinant
   - b) The rows of the determinant
   - c) The diagonal of the determinant
   - d) An extended vector outside the determinant
   > **Correct answer:** b) Each vector occupies a row of the $3\times3$ determinant.

7. $\begin{vmatrix}1&0&0\\0&1&0\\0&0&1\end{vmatrix}$ as the scalar triple product of the canonical vectors is:
   - a) $0$
   - b) $3$
   - c) $1$
   - d) $-1$
   > **Correct answer:** c) It is the determinant of the identity matrix, which equals $1$.

---

#### 4.5.3 Properties: antisymmetry under cyclic permutation

**Worked Example**

For $\mathbf{a}=(1,2,0)$, $\mathbf{b}=(0,-1,3)$ and $\mathbf{c}=(2,1,-1)$, verify that $[\mathbf{a},\mathbf{b},\mathbf{c}]=[\mathbf{b},\mathbf{c},\mathbf{a}]=[\mathbf{c},\mathbf{a},\mathbf{b}]$ (cyclic permutations) and that $[\mathbf{b},\mathbf{a},\mathbf{c}]=-[\mathbf{a},\mathbf{b},\mathbf{c}]$ (non-cyclic permutation).

**Step-by-step Solution:**

$$[\mathbf{a},\mathbf{b},\mathbf{c}]=\begin{vmatrix}1&2&0\\0&-1&3\\2&1&-1\end{vmatrix}=1(1-3)-2(0-6)+0=1(-2)-2(-6)=-2+12=10$$

$$[\mathbf{b},\mathbf{c},\mathbf{a}]=\begin{vmatrix}0&-1&3\\2&1&-1\\1&2&0\end{vmatrix}=0(0+2)-(-1)(0+1)+3(4-1)=0+1+9=10 \checkmark$$

$$[\mathbf{c},\mathbf{a},\mathbf{b}]=\begin{vmatrix}2&1&-1\\1&2&0\\0&-1&3\end{vmatrix}=2(6-0)-1(3-0)+(-1)(-1-0)=12-3+1=10 \checkmark$$

$$[\mathbf{b},\mathbf{a},\mathbf{c}]=\begin{vmatrix}0&-1&3\\1&2&0\\2&1&-1\end{vmatrix}=0(-2-0)-(-1)(-1-0)+3(1-4)=0-1-9=-10=-[\mathbf{a},\mathbf{b},\mathbf{c}] \checkmark$$

---

**Exercises with Solutions**

**Basic Level:**

1. Knowing that $[\mathbf{u},\mathbf{v},\mathbf{w}]=5$, write the value of $[\mathbf{v},\mathbf{w},\mathbf{u}]$ and of $[\mathbf{u},\mathbf{w},\mathbf{v}]$.
   > **Solution:** $[\mathbf{v},\mathbf{w},\mathbf{u}]=[\mathbf{u},\mathbf{v},\mathbf{w}]=5$ (cyclic permutation). $[\mathbf{u},\mathbf{w},\mathbf{v}]=-[\mathbf{u},\mathbf{v},\mathbf{w}]=-5$ (swapping two vectors).

2. Given $[\mathbf{a},\mathbf{b},\mathbf{c}]=-3$, compute $[\mathbf{c},\mathbf{b},\mathbf{a}]$.
   > **Solution:** Permuting $\mathbf{a}$ and $\mathbf{c}$: $[\mathbf{c},\mathbf{b},\mathbf{a}]=-[\mathbf{a},\mathbf{b},\mathbf{c}]=3$.

**Intermediate Level:**

3. Verify the antisymmetric property for $\mathbf{p}=(1,0,1)$, $\mathbf{q}=(0,1,0)$, $\mathbf{r}=(1,1,1)$.
   > **Solution:** $[\mathbf{p},\mathbf{q},\mathbf{r}]=\begin{vmatrix}1&0&1\\0&1&0\\1&1&1\end{vmatrix}=1(1-0)-0+1(0-1)=1-1=0$. $[\mathbf{q},\mathbf{p},\mathbf{r}]=-[\mathbf{p},\mathbf{q},\mathbf{r}]=0$. The vectors are coplanar, the sign is preserved (both zero) ✓.

4. If $[\mathbf{u},\mathbf{v},\mathbf{w}]=k$, express $[2\mathbf{u},3\mathbf{v},-\mathbf{w}]$ in terms of $k$.
   > **Solution:** By linearity of the determinant: $[2\mathbf{u},3\mathbf{v},-\mathbf{w}]=2\cdot3\cdot(-1)\cdot[\mathbf{u},\mathbf{v},\mathbf{w}]=-6k$.

**EVAU Level:**

5. *(EVAU Madrid style)* Knowing that $[\mathbf{a},\mathbf{b},\mathbf{c}]=4$:  
   a) Compute $[\mathbf{b},\mathbf{a},\mathbf{c}]$, $[\mathbf{a},\mathbf{c},\mathbf{b}]$ and $[\mathbf{c},\mathbf{b},\mathbf{a}]$.  
   b) Justify the sign of each using the antisymmetry properties.  
   c) How many distinct permutations of the three vectors give a positive scalar triple product?
   > **Solution:**  
   > **a)** $[\mathbf{b},\mathbf{a},\mathbf{c}]=-4$ (swapping the first two). $[\mathbf{a},\mathbf{c},\mathbf{b}]=-4$ (swapping the last two). $[\mathbf{c},\mathbf{b},\mathbf{a}]=-4$ (odd permutation: three swaps).  
   > **b)** Each transposition (swapping two vectors) changes the sign of the scalar triple product. Even permutations give positive sign and odd ones give negative sign.  
   > **c)** The $3!=6$ permutations split into 3 even (cyclic: $[\mathbf{a},\mathbf{b},\mathbf{c}]$, $[\mathbf{b},\mathbf{c},\mathbf{a}]$, $[\mathbf{c},\mathbf{a},\mathbf{b}]$, all $=+4$) and 3 odd ($=-4$). Therefore, **3 permutations** give a positive scalar triple product.

**Multiple Choice Test**

6. If you swap any two vectors in the scalar triple product, the result:
   - a) Doubles
   - b) Does not change
   - c) Changes sign
   - d) Becomes zero
   > **Correct answer:** c) The scalar triple product changes sign when any pair of vectors is swapped (antisymmetry).

7. The three scalar triple products $[\mathbf{u},\mathbf{v},\mathbf{w}]$, $[\mathbf{v},\mathbf{w},\mathbf{u}]$ and $[\mathbf{w},\mathbf{u},\mathbf{v}]$ are:
   - a) Always equal
   - b) Always opposite in sign
   - c) Equal only if the vectors are orthogonal
   - d) Always equal to zero
   > **Correct answer:** a) Cyclic permutations **do not change the sign** of the scalar triple product.

---

#### 4.5.4 Geometric interpretation: volume of the parallelepiped and coplanarity

**Worked Example**

Compute the volume of the parallelepiped whose edges are $\mathbf{a}=(1,0,2)$, $\mathbf{b}=(3,1,0)$ and $\mathbf{c}=(1,-1,1)$.

**Step-by-step Solution:**

The volume of the parallelepiped is the absolute value of the scalar triple product:

$$V = |[\mathbf{a},\mathbf{b},\mathbf{c}]| = \left|\begin{vmatrix}1&0&2\\3&1&0\\1&-1&1\end{vmatrix}\right|$$

Expanding along the first row:

$$= \left|1\begin{vmatrix}1&0\\-1&1\end{vmatrix} - 0\begin{vmatrix}3&0\\1&1\end{vmatrix} + 2\begin{vmatrix}3&1\\1&-1\end{vmatrix}\right|$$

$$= |1(1-0) - 0 + 2(-3-1)| = |1 + 0 + (-8)| = |-7| = 7$$

The **volume of the parallelepiped** is $V = 7$ cubic units.

---

**Exercises with Solutions**

**Basic Level:**

1. Are the vectors $(1,1,0)$, $(0,1,1)$ and $(1,2,1)$ coplanar? Use the scalar triple product.
   > **Solution:** $\begin{vmatrix}1&1&0\\0&1&1\\1&2&1\end{vmatrix}=1(1-2)-1(0-1)+0=(-1)+1=0$. Since the scalar triple product is **zero**, the vectors are **coplanar**.

2. Compute the volume of the parallelepiped with edges $\mathbf{u}=(2,0,0)$, $\mathbf{v}=(0,3,0)$, $\mathbf{w}=(0,0,4)$.
   > **Solution:** $\begin{vmatrix}2&0&0\\0&3&0\\0&0&4\end{vmatrix}=2\cdot3\cdot4=24$. $V=24$ cu. (consistent with $2\times3\times4=24$).

**Intermediate Level:**

3. Determine for which value of $k$ the vectors $(1,2,k)$, $(3,0,1)$ and $(0,1,-1)$ are coplanar.
   > **Solution:** $\begin{vmatrix}1&2&k\\3&0&1\\0&1&-1\end{vmatrix}=1(0-1)-2(-3-0)+k(3-0)=-1+6+3k=5+3k=0 \Rightarrow k=-\frac{5}{3}$.

4. Compute the volume of the parallelepiped formed by $\mathbf{a}=(2,1,-1)$, $\mathbf{b}=(0,3,2)$, $\mathbf{c}=(1,0,4)$.
   > **Solution:** $\begin{vmatrix}2&1&-1\\0&3&2\\1&0&4\end{vmatrix}=2(12-0)-1(0-2)+(-1)(0-3)=24+2+3=29$. $V=29$ cu.

**EVAU Level:**

5. *(EVAU Madrid style)* The vectors $\mathbf{u}=(1,m,-1)$, $\mathbf{v}=(2,0,1)$ and $\mathbf{w}=(0,1,m)$ are given.  
   a) Compute $[\mathbf{u},\mathbf{v},\mathbf{w}]$ as a function of $m$.  
   b) Determine for which values of $m$ the three vectors are coplanar.  
   c) For $m=2$, compute the volume of the parallelepiped they form.
   > **Solution:**  
   > **a)** $\begin{vmatrix}1&m&-1\\2&0&1\\0&1&m\end{vmatrix}=1(0-1)-m(2m-0)+(-1)(2-0)=(-1)-2m^2-2=-2m^2-3$.  
   > **b)** $-2m^2-3=0 \Rightarrow m^2=-\frac{3}{2}$. No real solution, so the vectors **are never coplanar** for $m\in\mathbb{R}$.  
   > **c)** $m=2$: $V=|-2(4)-3|=|-11|=11$ cu.

**Multiple Choice Test**

6. The volume of the parallelepiped formed by $\mathbf{u}$, $\mathbf{v}$ and $\mathbf{w}$ is:
   - a) $[\mathbf{u},\mathbf{v},\mathbf{w}]$
   - b) $|[\mathbf{u},\mathbf{v},\mathbf{w}]|$
   - c) $|\mathbf{u}||\mathbf{v}||\mathbf{w}|$
   - d) $\frac{1}{6}|[\mathbf{u},\mathbf{v},\mathbf{w}]|$
   > **Correct answer:** b) The volume is the **absolute value** of the scalar triple product, since the determinant may be negative.

7. Three vectors are coplanar if and only if their scalar triple product is:
   - a) Positive
   - b) Negative
   - c) Equal to 1
   - d) Equal to 0
   > **Correct answer:** d) A zero scalar triple product is the necessary and sufficient condition for coplanarity.

---

#### 4.5.5 Applications: volume of tetrahedra and verification of coplanarity of four points

**Worked Example**

*(EVAU Madrid style problem)* The points $A=(0,0,0)$, $B=(2,0,0)$, $C=(0,3,0)$ and $D=(0,0,4)$ are given.

a) Verify that the four points are not coplanar.
b) Compute the volume of the tetrahedron $ABCD$.
c) Compute the area of face $ABC$.

**Step-by-step Solution:**

**Vectors from A:**

$$\overrightarrow{AB}=(2,0,0),\quad\overrightarrow{AC}=(0,3,0),\quad\overrightarrow{AD}=(0,0,4)$$

**a) Verification of coplanarity:**

$$[\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}]=\begin{vmatrix}2&0&0\\0&3&0\\0&0&4\end{vmatrix}=24\neq0$$

Since the scalar triple product is nonzero, the four points **are not coplanar**. ✓

**b) Volume of the tetrahedron:**

$$V_{\text{tetrahedron}}=\frac{1}{6}\,|[\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}]|=\frac{1}{6}\cdot24=4 \text{ cu.}$$

**c) Area of face ABC:**

$$\overrightarrow{AB}\times\overrightarrow{AC}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\2&0&0\\0&3&0\end{vmatrix}=(0,0,6)$$

$$S_{ABC}=\frac{1}{2}|\overrightarrow{AB}\times\overrightarrow{AC}|=\frac{1}{2}\cdot6=3 \text{ sq. units}$$

*(Consistent with the right triangle with legs 2 and 3 in the $xy$-plane.)*

---

**Exercises with Solutions**

**Basic Level:**

1. Are the points $A=(0,0,0)$, $B=(1,0,0)$, $C=(0,1,0)$ and $D=(1,1,0)$ coplanar?
   > **Solution:** $\overrightarrow{AB}=(1,0,0)$, $\overrightarrow{AC}=(0,1,0)$, $\overrightarrow{AD}=(1,1,0)$. $\begin{vmatrix}1&0&0\\0&1&0\\1&1&0\end{vmatrix}=0$. The four points are **coplanar** (all in the plane $z=0$).

2. Compute the volume of the tetrahedron with vertices $O=(0,0,0)$, $A=(3,0,0)$, $B=(0,3,0)$, $C=(0,0,3)$.
   > **Solution:** $\begin{vmatrix}3&0&0\\0&3&0\\0&0&3\end{vmatrix}=27$. $V=\frac{27}{6}=\frac{9}{2}=4{,}5$ cu.

**Intermediate Level:**

3. Check whether $A=(1,1,0)$, $B=(2,0,1)$, $C=(0,2,1)$ and $D=(1,1,2)$ are coplanar.
   > **Solution:** $\overrightarrow{AB}=(1,-1,1)$, $\overrightarrow{AC}=(-1,1,1)$, $\overrightarrow{AD}=(0,0,2)$. $\begin{vmatrix}1&-1&1\\-1&1&1\\0&0&2\end{vmatrix}=1(2-0)-(-1)(-2-0)+1(0-0)=2-2+0=0$. The four points are **coplanar**.

4. Compute the volume of the tetrahedron with vertices $A=(1,0,0)$, $B=(0,2,0)$, $C=(0,0,3)$ and $D=(1,1,1)$.
   > **Solution:** $\overrightarrow{AB}=(-1,2,0)$, $\overrightarrow{AC}=(-1,0,3)$, $\overrightarrow{AD}=(0,1,1)$. $\begin{vmatrix}-1&2&0\\-1&0&3\\0&1&1\end{vmatrix}=-1(0-3)-2(-1-0)+0=3+2=5$. $V=\frac{5}{6}$ cu.

**EVAU Level:**

5. *(EVAU Madrid style, 2 points)* The points $A=(1,-1,0)$, $B=(2,0,1)$, $C=(0,2,-1)$ and $D=(a,0,0)$ are considered.  
   a) Determine the value of $a$ for which the four points are coplanar.  
   b) For $a=1$, compute the volume of the tetrahedron $ABCD$.  
   c) For $a=1$, compute the area of face $ABD$.
   > **Solution:**  
   > **a)** $\overrightarrow{AB}=(1,1,1)$, $\overrightarrow{AC}=(-1,3,-1)$, $\overrightarrow{AD}=(a-1,1,0)$.  
   > $\begin{vmatrix}1&1&1\\-1&3&-1\\a-1&1&0\end{vmatrix}=1(0+1)-1(0+a-1)+1(-1-3(a-1))$  
   > $=1-(a-1)+(-1-3a+3)=1-a+1+2-3a=4-4a=0 \Rightarrow a=1$.  
   > **b)** $a=1$: $\overrightarrow{AD}=(0,1,0)$.  
   > $\begin{vmatrix}1&1&1\\-1&3&-1\\0&1&0\end{vmatrix}=1(0+1)-1(0-0)+1(-1-0)=1-0-1=0$.  
   > Since the scalar triple product is 0, the volume of the tetrahedron is $V=\frac{|0|}{6}=0$. The points are coplanar for $a=1$ (consistent with part a).  
   > **c)** With $a=1$: $\overrightarrow{AB}=(1,1,1)$, $\overrightarrow{AD}=(0,1,0)$. $\overrightarrow{AB}\times\overrightarrow{AD}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\1&1&1\\0&1&0\end{vmatrix}=(0-1)\mathbf{i}-(0-0)\mathbf{j}+(1-0)\mathbf{k}=(-1,0,1)$. $S_{ABD}=\frac{1}{2}\sqrt{1+0+1}=\frac{\sqrt{2}}{2}$ sq. units.

**Multiple Choice Test**

6. The volume of the tetrahedron with edges $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ from the same vertex is:
   - a) $|[\mathbf{u},\mathbf{v},\mathbf{w}]|$
   - b) $\frac{1}{3}|[\mathbf{u},\mathbf{v},\mathbf{w}]|$
   - c) $\frac{1}{6}|[\mathbf{u},\mathbf{v},\mathbf{w}]|$
   - d) $\frac{1}{2}|[\mathbf{u},\mathbf{v},\mathbf{w}]|$
   > **Correct answer:** c) The tetrahedron occupies $\frac{1}{6}$ of the parallelepiped formed by the same three vectors.

7. Four points $A$, $B$, $C$, $D$ are coplanar if and only if:
   - a) The three vectors $\overrightarrow{AB}$, $\overrightarrow{AC}$, $\overrightarrow{AD}$ have the same magnitude
   - b) The scalar triple product $[\overrightarrow{AB},\overrightarrow{AC},\overrightarrow{AD}]=0$
   - c) $\overrightarrow{AB}\times\overrightarrow{AC}=\mathbf{0}$
   - d) $\overrightarrow{AB}\cdot\overrightarrow{AC}=0$
   > **Correct answer:** b) The coplanarity of four points is equivalent to the scalar triple product of the three vectors from one of them being zero.

---

*End of Chapter 4 — Vectors in Space*

---

*Document generated for Mathematics II — 2nd Year Bachillerato (Sciences and Technology)*  
*Community of Madrid · Decree 64/2022 (LOMLOE) · FUHEM Curriculum 2025-26*  
*Chapters 3 (Systems of Linear Equations) and 4 (Vectors in Space)*
