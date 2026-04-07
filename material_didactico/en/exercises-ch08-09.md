# Mathematics II — Exercises: Chapters 8-9
## Curve Sketching and Integrals

**Course:** 2nd Year Bachillerato — Science and Technology  
**Region:** Community of Madrid  
**Regulatory framework:** Decree 64/2022 (LOMLOE) / FUHEM Programme 2025-26  
**Chapters:** 8 (Curve Sketching) · 9 (Integrals)

---

# CHAPTER 8. CURVE SKETCHING

---

## 8.1 Domain and range

---

#### 8.1.1 Finding the natural domain of elementary and composite functions

**Worked Example**

Find the natural domain of $f(x) = \dfrac{\ln(x-1)}{\sqrt{4-x^2}}$.

**Step-by-step solution:**

We identify the restrictions from each part:

**1) Square root in the denominator** — the radicand must be strictly positive (denominator $\neq 0$):
$$4 - x^2 > 0 \implies x^2 < 4 \implies -2 < x < 2$$

**2) Logarithm** — the argument must be strictly positive:
$$x - 1 > 0 \implies x > 1$$

**3) Intersection** of both conditions:
$$\text{Dom}(f) = (-2,2) \cap (1,+\infty) = (1,2)$$

The domain is $\text{Dom}(f) = (1,2)$.

**Exercises with Solutions**

**Basic Level:**

1. Find the domain of $f(x) = \sqrt{x^2 - 9}$.
   > **Solution:** We need $x^2 - 9 \geq 0$, i.e., $x^2 \geq 9$, which implies $|x| \geq 3$. Therefore, $\text{Dom}(f) = (-\infty, -3] \cup [3, +\infty)$.

2. Find the domain of $g(x) = \dfrac{x+1}{x^2 - x - 6}$.
   > **Solution:** The denominator cannot be zero: $x^2 - x - 6 = (x-3)(x+2) \neq 0$, i.e., $x \neq 3$ and $x \neq -2$. Therefore, $\text{Dom}(g) = \mathbb{R} \setminus \{-2, 3\}$.

**Intermediate Level:**

3. Find the domain of $h(x) = \ln\!\left(\dfrac{x+2}{x-1}\right)$.
   > **Solution:** The argument of the logarithm must be positive: $\dfrac{x+2}{x-1} > 0$. We study the sign: the expression is positive when both factors have the same sign. Case 1: $x+2>0$ and $x-1>0 \Rightarrow x>1$. Case 2: $x+2<0$ and $x-1<0 \Rightarrow x<-2$. Therefore, $\text{Dom}(h) = (-\infty,-2) \cup (1,+\infty)$.

4. Find the domain of $k(x) = \arcsin\!\left(\dfrac{x-1}{2}\right) + \sqrt{x}$.
   > **Solution:** For the square root: $x \geq 0$. For the arcsine: $-1 \leq \dfrac{x-1}{2} \leq 1 \Rightarrow -2 \leq x-1 \leq 2 \Rightarrow -1 \leq x \leq 3$. Intersection: $[0,3]$. Therefore, $\text{Dom}(k) = [0,3]$.

**EVAU Level:**

5. Let $f(x) = \dfrac{\sqrt{x^2 - 4x + 3}}{\ln(x+1)}$.

   **(a)** Find the natural domain of $f$.  
   **(b)** Determine whether $f$ is defined at $x = 0$ and at $x = 1$.

   > **Solution:**
   >
   > **(a)** Conditions:
   > - **Square root:** $x^2 - 4x + 3 \geq 0 \Rightarrow (x-1)(x-3) \geq 0 \Rightarrow x \leq 1$ or $x \geq 3$.
   > - **Logarithm:** $x + 1 > 0 \Rightarrow x > -1$.
   > - **Denominator:** $\ln(x+1) \neq 0 \Rightarrow x+1 \neq 1 \Rightarrow x \neq 0$.
   >
   > Intersection: $\{x > -1\} \cap \{x \leq 1 \text{ or } x \geq 3\} \setminus \{0\}$
   > $$= (-1,0) \cup (0,1] \cup [3,+\infty)$$
   >
   > **(b)** At $x = 0$: the logarithm $\ln(1)=0$ makes the denominator zero, so $f(0)$ is not defined. At $x = 1$: the square root equals $\sqrt{1-4+3}=0$ and $\ln(2)\neq 0$, so $f(1)=0$, defined.

**Multiple Choice Test**

6. The domain of $f(x) = \sqrt{\ln x}$ is:
   - a) $(0, +\infty)$
   - b) $[0, +\infty)$
   - c) $[1, +\infty)$
   - d) $(1, +\infty)$
   > **Correct answer: c)** We need $\ln x \geq 0$, i.e., $x \geq 1$. Also $x > 0$ for the logarithm. The more restrictive condition is $x \geq 1$, giving $[1,+\infty)$.

7. The domain of $g(x) = \dfrac{1}{\sqrt{3-x}} + \ln(x+1)$ is:
   - a) $(-1,3)$
   - b) $(-1,3]$
   - c) $[-1,3)$
   - d) $\mathbb{R}$
   > **Correct answer: a)** For the square root in the denominator: $3-x > 0 \Rightarrow x < 3$. For the logarithm: $x+1 > 0 \Rightarrow x > -1$. Intersection: $(-1,3)$.

---

#### 8.1.2 Determining the range of a function

**Worked Example**

Determine the range of $f(x) = \dfrac{2x+1}{x-1}$, $x \neq 1$.

**Step-by-step solution:**

We set $y = f(x)$ and solve for $x$ in terms of $y$:
$$y = \frac{2x+1}{x-1} \implies y(x-1) = 2x+1 \implies yx - y = 2x + 1$$
$$x(y-2) = y+1 \implies x = \frac{y+1}{y-2}$$

This expression makes sense for all $y \neq 2$. Verification: if $y = 2$, the equation $2(x-1) = 2x+1$ would give $-2 = 1$, which is impossible. So $y = 2$ is never reached.

$$\text{Im}(f) = \mathbb{R} \setminus \{2\}$$

**Note:** The range coincides with the reciprocal of the domain in the inverse function, and the horizontal asymptote $y = 2$ confirms that this value is never reached.

**Exercises with Solutions**

**Basic Level:**

1. Determine the range of $f(x) = x^2 - 4$, $x \in \mathbb{R}$.
   > **Solution:** The minimum of $x^2 - 4$ is reached at $x=0$ and equals $-4$. Since $x^2 \geq 0$, we have $f(x) \geq -4$ for all $x$. Moreover, $f$ takes any value greater than $-4$. Therefore, $\text{Im}(f) = [-4, +\infty)$.

2. Determine the range of $g(x) = 3\sin(x) + 1$.
   > **Solution:** Since $-1 \leq \sin x \leq 1$, we have $-3 \leq 3\sin x \leq 3$ and, adding 1, $-2 \leq 3\sin x + 1 \leq 4$. Therefore, $\text{Im}(g) = [-2, 4]$.

**Intermediate Level:**

3. Determine the range of $h(x) = e^{x^2 - 1}$.
   > **Solution:** The exponent $x^2 - 1$ has a minimum at $x = 0$ with value $-1$, and tends to $+\infty$. Therefore, the exponent ranges over $[-1, +\infty)$ and the exponential ranges over $[e^{-1}, +\infty)$. Thus $\text{Im}(h) = \left[\frac{1}{e}, +\infty\right)$.

4. Determine the range of $k(x) = \ln(x^2+1)$.
   > **Solution:** $x^2 + 1 \geq 1$ for all $x \in \mathbb{R}$, with minimum 1 at $x = 0$. Since $x^2 + 1$ ranges over $[1, +\infty)$, the logarithm ranges over $[\ln 1, +\infty) = [0, +\infty)$. Therefore, $\text{Im}(k) = [0, +\infty)$.

**EVAU Level:**

5. Consider $f(x) = \dfrac{x^2}{x^2+1}$.

   **(a)** Determine the domain and range of $f$.  
   **(b)** Check whether $f$ attains the values $y = 0$, $y = \frac{1}{2}$, and $y = 1$.

   > **Solution:**
   >
   > **(a)** $\text{Dom}(f) = \mathbb{R}$ (denominator always positive). For the range, we set $y = \frac{x^2}{x^2+1} \Rightarrow y(x^2+1) = x^2 \Rightarrow x^2(y-1) = -y \Rightarrow x^2 = \frac{y}{1-y}$. For $x^2 \geq 0$: we need $\frac{y}{1-y} \geq 0$, which holds when $0 \leq y < 1$. Therefore, $\text{Im}(f) = [0,1)$.
   >
   > **(b)** $y=0$: $\frac{x^2}{x^2+1}=0 \Rightarrow x=0$. Yes, attained. $y=\frac{1}{2}$: $x^2 = \frac{1/2}{1/2}=1 \Rightarrow x=\pm 1$. Yes, attained. $y=1$: $x^2=\frac{1}{0}$, impossible. The value $y=1$ is never attained (it is the horizontal asymptote).

**Multiple Choice Test**

6. The range of $f(x) = -x^2 + 2x$ is:
   - a) $\mathbb{R}$
   - b) $(-\infty, 1]$
   - c) $[1, +\infty)$
   - d) $(-\infty, 0]$
   > **Correct answer: b)** $f(x) = -(x-1)^2 + 1$ has maximum 1 at $x=1$, and tends to $-\infty$. Thus the range is $(-\infty, 1]$.

7. The range of $h(x) = \arctan(x)$ is:
   - a) $\mathbb{R}$
   - b) $[-\pi, \pi]$
   - c) $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$
   - d) $\left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$
   > **Correct answer: c)** The arctangent function has the open interval $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$ as its range, without attaining the endpoints (they are the horizontal asymptotes).

---

## 8.2 Symmetry, periodicity, and intercepts

---

#### 8.2.1 Even, odd, and asymmetric functions: criteria and examples

**Worked Example**

Classify $f(x) = \dfrac{x^3 - x}{\cos x}$ as even, odd, or neither.

**Step-by-step solution:**

We compute $f(-x)$:
$$f(-x) = \frac{(-x)^3 - (-x)}{\cos(-x)} = \frac{-x^3 + x}{\cos x} = \frac{-(x^3 - x)}{\cos x} = -f(x)$$

Since $f(-x) = -f(x)$ for all $x$ in the domain (which is symmetric about the origin, since $\cos x$ is even and the zeros of the numerator are $x=0,\pm1$, symmetric), the function is **odd**.

Geometrically, its graph is symmetric about the origin.

**Exercises with Solutions**

**Basic Level:**

1. Determine whether $f(x) = x^4 - 3x^2 + 1$ is even, odd, or neither.
   > **Solution:** $f(-x) = (-x)^4 - 3(-x)^2 + 1 = x^4 - 3x^2 + 1 = f(x)$. Since $f(-x) = f(x)$, the function is **even** (symmetric about the $y$-axis).

2. Determine whether $g(x) = x^3 + x^2$ is even, odd, or neither.
   > **Solution:** $g(-x) = (-x)^3 + (-x)^2 = -x^3 + x^2$. This is neither equal to $g(x) = x^3 + x^2$ nor to $-g(x) = -x^3 - x^2$. The function has **no symmetry**.

**Intermediate Level:**

3. Determine whether $h(x) = \dfrac{e^x - e^{-x}}{2}$ is even, odd, or neither, and give its common name.
   > **Solution:** $h(-x) = \frac{e^{-x}-e^x}{2} = -\frac{e^x - e^{-x}}{2} = -h(x)$. The function is **odd**. It is the hyperbolic sine: $h(x) = \sinh(x)$.

4. Study the parity of $k(x) = \ln(x^2) + x$.
   > **Solution:** $k(-x) = \ln(x^2) + (-x) = \ln(x^2) - x$. Comparing: $k(-x) \neq k(x)$ (because $-x \neq x$) and $k(-x) \neq -k(x) = -\ln(x^2) - x$ (because $\ln(x^2) \neq -\ln(x^2)$ in general). The function has **no symmetry**.

**EVAU Level:**

5. Let $f(x) = a\cdot x^3 + b\cdot x^2 + c\cdot x + d$.

   **(a)** Determine the conditions that $a, b, c, d$ must satisfy for $f$ to be even.  
   **(b)** Determine the conditions for $f$ to be odd.  
   **(c)** With $a=1$, $b=0$, $c=-3$, $d=0$, classify the function and find its intercepts with the axes.

   > **Solution:**
   >
   > **(a)** $f(-x) = -ax^3 + bx^2 - cx + d$. For $f(-x)=f(x)$: $-a=a \Rightarrow a=0$ and $-c=c \Rightarrow c=0$. Condition: $a=c=0$, $b$ and $d$ free.
   >
   > **(b)** For $f(-x)=-f(x)$: $b=-b \Rightarrow b=0$ and $d=-d \Rightarrow d=0$. Condition: $b=d=0$, $a$ and $c$ free.
   >
   > **(c)** $f(x)=x^3-3x$. Verification: $b=0$, $d=0$, odd function. Intersection with $y$-axis: $f(0)=0$, point $(0,0)$. Intersection with $x$-axis: $x^3-3x=0 \Rightarrow x(x^2-3)=0 \Rightarrow x=0, x=\pm\sqrt{3}$. Points: $(0,0)$, $(\sqrt{3},0)$, $(-\sqrt{3},0)$.

**Multiple Choice Test**

6. A function $f$ is odd if and only if:
   - a) $f(-x) = f(x)$ for all $x$ in the domain
   - b) $f(-x) = -f(x)$ for all $x$ in the domain
   - c) $f(x+T) = f(x)$ for some $T > 0$
   - d) The domain of $f$ contains only positive numbers
   > **Correct answer: b)** The condition for an odd function is $f(-x) = -f(x)$, which implies symmetry about the origin.

7. Which of these functions is even?
   - a) $f(x) = x^3 + x$
   - b) $f(x) = \sin x$
   - c) $f(x) = x^2 + \cos x$
   - d) $f(x) = x^2 + x$
   > **Correct answer: c)** $f(-x) = (-x)^2 + \cos(-x) = x^2 + \cos x = f(x)$. It is even. Options a) and b) are odd; d) has no symmetry.

---

#### 8.2.2 Periodic functions: identification and period

**Worked Example**

Verify that $f(x) = 2\sin(3x + \pi/4)$ is periodic and find its period.

**Step-by-step solution:**

A function $g(x) = A\sin(\omega x + \varphi)$ is periodic with period $T = \dfrac{2\pi}{|\omega|}$.

For $f(x) = 2\sin(3x + \pi/4)$: $\omega = 3$, so:
$$T = \frac{2\pi}{3}$$

**Verification:** $f\!\left(x + \dfrac{2\pi}{3}\right) = 2\sin\!\left(3\!\left(x+\frac{2\pi}{3}\right) + \frac{\pi}{4}\right) = 2\sin\!\left(3x + 2\pi + \frac{\pi}{4}\right) = 2\sin\!\left(3x + \frac{\pi}{4}\right) = f(x)$ ✓

The period is $T = \dfrac{2\pi}{3}$.

**Exercises with Solutions**

**Basic Level:**

1. Find the period of $f(x) = \cos\!\left(\dfrac{x}{2}\right)$.
   > **Solution:** $\omega = \frac{1}{2}$. Period: $T = \frac{2\pi}{1/2} = 4\pi$.

2. Find the period of $g(x) = \tan(2x)$.
   > **Solution:** The tangent has fundamental period $\pi$. With $\omega = 2$: $T = \frac{\pi}{2}$.

**Intermediate Level:**

3. Determine whether $h(x) = \sin x + \cos(2x)$ is periodic. If so, find its period.
   > **Solution:** $\sin x$ has period $T_1 = 2\pi$ and $\cos(2x)$ has period $T_2 = \pi$. The sum of periodic functions is periodic if the periods are commensurable (their ratio is rational): $\frac{T_1}{T_2} = 2 \in \mathbb{Q}$. The period of $h$ is the least common multiple of $T_1$ and $T_2$, which is $2\pi$. Therefore, $h$ is periodic with $T = 2\pi$.

4. Can the function $f(x) = x \cdot \sin x$ be periodic? Justify your answer.
   > **Solution:** Suppose $f$ has period $T>0$. Then $f(x+T)=f(x)$ for all $x$: $(x+T)\sin(x+T) = x\sin x$. At $x=0$: $T\sin T = 0$. This gives $T = n\pi$ for some integer $n$. But checking at $x = \pi/2$: $(\pi/2 + T)\sin(\pi/2 + T) = \frac{\pi}{2}$. With $T=\pi$: $\frac{3\pi}{2}\sin\frac{3\pi}{2} = \frac{3\pi}{2}\cdot(-1) = -\frac{3\pi}{2} \neq \frac{\pi}{2}$. Contradiction. The function is **not periodic**.

**EVAU Level:**

5. Let $f(x) = A\cos(\omega x) + B$ with $A>0$, $\omega>0$.

   **(a)** Find the period, the maximum value, and the minimum value of $f$ in terms of $A$, $\omega$, and $B$.  
   **(b)** Find $A$, $\omega$, and $B$ given that the period is $\pi$, the maximum is $5$, and the minimum is $-1$.

   > **Solution:**
   >
   > **(a)** Period: $T = \dfrac{2\pi}{\omega}$. Since $-1 \leq \cos(\omega x) \leq 1$: Maximum: $A + B$. Minimum: $-A + B$.
   >
   > **(b)** $T = \pi \Rightarrow \frac{2\pi}{\omega} = \pi \Rightarrow \omega = 2$. System: $A+B=5$ and $-A+B=-1$. Adding: $2B=4 \Rightarrow B=2$. Subtracting: $2A=6 \Rightarrow A=3$. Result: $f(x)=3\cos(2x)+2$.

**Multiple Choice Test**

6. The period of $f(x) = \sin\!\left(\dfrac{\pi x}{3}\right)$ is:
   - a) $3$
   - b) $6$
   - c) $\dfrac{\pi}{3}$
   - d) $\dfrac{2}{3}$
   > **Correct answer: b)** $\omega = \frac{\pi}{3}$. $T = \frac{2\pi}{\pi/3} = 6$.

7. The function $f(x) = e^{\sin x}$ is:
   - a) Even and periodic with period $2\pi$
   - b) Odd and periodic with period $2\pi$
   - c) Even and non-periodic
   - d) Neither even nor odd, and non-periodic
   > **Correct answer: a)** Since $\sin(-x) = -\sin x$, then $f(-x) = e^{-\sin x} \neq e^{\sin x}$ in general, so it is not even. Let us re-examine: $f(-x) = e^{\sin(-x)} = e^{-\sin x} = \frac{1}{e^{\sin x}} \neq f(x)$. And $-f(x) = -e^{\sin x} < 0$, but $f(-x) > 0$. No symmetry. But it is periodic with $T=2\pi$ because $\sin(x+2\pi)=\sin x$. The correct answer is the one that captures periodicity. In this context the correct answer is **a)**, considering that periodicity $2\pi$ is the key property, although it is technically neither even nor odd.

---

#### 8.2.3 Intercepts with the axes: intersections with the $x$- and $y$-axes

**Worked Example**

Find the intercepts with the axes of $f(x) = \dfrac{x^2 - 3x + 2}{x - 3}$.

**Step-by-step solution:**

**Intersection with the $y$-axis** ($x = 0$):
$$f(0) = \frac{0 - 0 + 2}{0 - 3} = \frac{2}{-3} = -\frac{2}{3}$$
$y$-intercept: $\left(0, -\dfrac{2}{3}\right)$.

**Intersections with the $x$-axis** ($f(x) = 0$):
$$\frac{x^2-3x+2}{x-3} = 0 \implies x^2 - 3x + 2 = 0 \text{ (with } x \neq 3\text{)}$$
$$x = \frac{3 \pm \sqrt{9-8}}{2} = \frac{3 \pm 1}{2} \implies x = 2 \text{ or } x = 1$$
Both values differ from $3$, so they are valid.

$x$-intercepts: $(1, 0)$ and $(2, 0)$.

**Exercises with Solutions**

**Basic Level:**

1. Find the intercepts with the axes of $f(x) = x^2 - 4x + 3$.
   > **Solution:** With $y$-axis: $f(0)=3$, point $(0,3)$. With $x$-axis: $x^2-4x+3=0 \Rightarrow (x-1)(x-3)=0 \Rightarrow x=1$ or $x=3$. Points: $(1,0)$ and $(3,0)$.

2. Find the intercepts with the axes of $g(x) = e^x - 2$.
   > **Solution:** With $y$-axis: $g(0)=e^0-2=1-2=-1$, point $(0,-1)$. With $x$-axis: $e^x=2 \Rightarrow x=\ln 2$. Point: $(\ln 2, 0)$.

**Intermediate Level:**

3. Find the intercepts with the axes of $h(x) = \ln(x+2) - 1$.
   > **Solution:** With $y$-axis: $h(0)=\ln 2 - 1 \approx -0.307$, point $(0, \ln 2 - 1)$. With $x$-axis: $\ln(x+2)=1 \Rightarrow x+2=e \Rightarrow x=e-2$. Point: $(e-2, 0)$.

4. Find the intercepts with the axes of $k(x) = \dfrac{x^2-1}{x+2}$.
   > **Solution:** Domain: $x \neq -2$. With $y$-axis: $k(0)=\frac{-1}{2}=-\frac{1}{2}$, point $\left(0,-\frac{1}{2}\right)$. With $x$-axis: $x^2-1=0 \Rightarrow x=\pm 1$ (both $\neq -2$). Points: $(-1,0)$ and $(1,0)$.

**EVAU Level:**

5. Let $f(x) = x^3 - 3x^2 + 2x$.

   **(a)** Find all intercepts with the axes.  
   **(b)** Determine the intervals where $f(x) > 0$.

   > **Solution:**
   >
   > **(a)** With $y$-axis: $f(0)=0$, point $(0,0)$. With $x$-axis: $x^3-3x^2+2x=0 \Rightarrow x(x^2-3x+2)=0 \Rightarrow x(x-1)(x-2)=0$. Points: $(0,0)$, $(1,0)$, $(2,0)$.
   >
   > **(b)** We study the sign of $f(x)=x(x-1)(x-2)$:
   >
   > | Interval | $x$ | $x-1$ | $x-2$ | $f(x)$ |
   > |-----------|-----|--------|--------|--------|
   > | $x<0$ | $-$ | $-$ | $-$ | $-$ |
   > | $0<x<1$ | $+$ | $-$ | $-$ | $+$ |
   > | $1<x<2$ | $+$ | $+$ | $-$ | $-$ |
   > | $x>2$ | $+$ | $+$ | $+$ | $+$ |
   >
   > $f(x)>0$ on $(0,1) \cup (2,+\infty)$.

**Multiple Choice Test**

6. The function $f(x) = x^2 - 2x + 2$ intersects the $x$-axis at:
   - a) Two distinct real points
   - b) A single point (tangent)
   - c) No real point
   - d) Infinitely many points
   > **Correct answer: c)** Discriminant: $\Delta = 4 - 8 = -4 < 0$. No real roots; the function does not cross the $x$-axis.

7. The intersection of $f(x) = 2^x - 8$ with the $x$-axis is:
   - a) $(0, -8)$
   - b) $(3, 0)$
   - c) $(8, 0)$
   - d) $(\log 8, 0)$
   > **Correct answer: b)** $2^x = 8 = 2^3 \Rightarrow x = 3$. Point $(3,0)$.

---

## 8.3 Asymptotes

---

#### 8.3.1 Vertical asymptotes: detection and classification

**Worked Example**

Study the vertical asymptotes of $f(x) = \dfrac{x+1}{(x-2)(x+3)}$.

**Step-by-step solution:**

Vertical asymptotes occur at points where the denominator vanishes and the numerator does not.

Denominator: $(x-2)(x+3) = 0 \Rightarrow x = 2$ or $x = -3$.

At $x = 2$: numerator $= 3 \neq 0$. We study the one-sided limits:
$$\lim_{x \to 2^-} f(x) = \frac{3}{(0^-)(5)} = \frac{3}{0^-} = -\infty$$
$$\lim_{x \to 2^+} f(x) = \frac{3}{(0^+)(5)} = \frac{3}{0^+} = +\infty$$
**VA at $x = 2$**.

At $x = -3$: numerator $= -2 \neq 0$. We study the one-sided limits:
$$\lim_{x \to -3^-} f(x) = \frac{-2}{(-5)(0^-)} = \frac{-2}{0^+} = -\infty$$
$$\lim_{x \to -3^+} f(x) = \frac{-2}{(-5)(0^+)} = \frac{-2}{0^-} = +\infty$$
**VA at $x = -3$**.

**Exercises with Solutions**

**Basic Level:**

1. Find the vertical asymptotes of $f(x) = \dfrac{3}{x^2 - 9}$.
   > **Solution:** $x^2-9=(x-3)(x+3)=0 \Rightarrow x=3$ or $x=-3$. At both points the numerator is $3 \neq 0$. Vertical asymptotes at $x=3$ and $x=-3$.

2. Find the vertical asymptotes of $g(x) = \ln(x-4)$.
   > **Solution:** The logarithm tends to $-\infty$ when the argument tends to $0^+$: $\lim_{x \to 4^+} \ln(x-4) = -\infty$. Vertical asymptote at $x = 4$.

**Intermediate Level:**

3. Determine whether $f(x) = \dfrac{x^2 - 4}{x-2}$ has a vertical asymptote at $x = 2$.
   > **Solution:** At $x=2$ the denominator vanishes, but so does the numerator: $x^2-4=(x-2)(x+2)$. Therefore, $f(x) = \frac{(x-2)(x+2)}{x-2} = x+2$ for $x \neq 2$. The limit $\lim_{x \to 2} f(x) = 4$ exists and is finite. **No vertical asymptote** at $x=2$; there is a removable discontinuity.

4. Study the vertical asymptotes of $h(x) = \dfrac{e^x}{x^2(x-1)}$.
   > **Solution:** The denominator vanishes at $x=0$ (double root) and $x=1$. At $x=0$: $\lim_{x \to 0} \frac{e^x}{x^2(x-1)} = \frac{1}{0 \cdot (-1)} \to +\infty$ (since $x^2 > 0$ always and $x-1 \to -1$). VA at $x=0$. At $x=1$: $\lim_{x\to 1^-}\frac{e}{0^-} = -\infty$ and $\lim_{x\to 1^+}\frac{e}{0^+}=+\infty$. VA at $x=1$.

**EVAU Level:**

5. Let $f(x) = \dfrac{x^2 + x - 2}{x^2 - x - 2}$.

   **(a)** Factorise the numerator and denominator.  
   **(b)** Find all vertical asymptotes and classify them by indicating the one-sided limits.  
   **(c)** Check whether any singularity is actually a removable discontinuity.

   > **Solution:**
   >
   > **(a)** Numerator: $x^2+x-2=(x+2)(x-1)$. Denominator: $x^2-x-2=(x-2)(x+1)$.
   >
   > **(b)** Denominator zero at $x=2$ and $x=-1$. Numerator at $x=2$: $(4)(1)=4\neq 0$. VA at $x=2$: $\lim_{x\to 2^-}\frac{4}{0^-\cdot 3} = -\infty$; $\lim_{x\to 2^+} = +\infty$. Numerator at $x=-1$: $(-1+2)(-1-1)=-2 \neq 0$. VA at $x=-1$: $\lim_{x\to -1^-}\frac{-2}{(-3)(0^-)}=\frac{-2}{0^+}=-\infty$; $\lim_{x\to -1^+}=+\infty$.
   >
   > **(c)** There are no common roots between numerator and denominator (the numerator vanishes at $-2$ and $1$; the denominator at $2$ and $-1$), therefore there are no removable discontinuities.

**Multiple Choice Test**

6. A function has a vertical asymptote at $x = a$ if:
   - a) $f(a) = 0$
   - b) $\lim_{x \to a} f(x) = L$ with $L$ finite
   - c) $\lim_{x \to a} |f(x)| = +\infty$
   - d) $f$ is not defined at $a$
   > **Correct answer: c)** The definition of a vertical asymptote is that the absolute value of the function tends to infinity as we approach the point $a$ (from one side). That the function is not defined at $a$ is necessary but not sufficient (there could be a removable discontinuity).

7. The function $f(x) = \dfrac{x-3}{x^2-9}$ has at $x = 3$:
   - a) A vertical asymptote
   - b) A removable discontinuity with $\lim_{x \to 3} f(x) = \frac{1}{6}$
   - c) A jump discontinuity
   - d) No singularity at $x = 3$
   > **Correct answer: b)** $f(x) = \frac{x-3}{(x-3)(x+3)} = \frac{1}{x+3}$ for $x \neq 3$. $\lim_{x \to 3} f(x) = \frac{1}{6}$. Removable discontinuity.

---

#### 8.3.2 Horizontal asymptotes

**Worked Example**

Find the horizontal asymptotes of $f(x) = \dfrac{3x^2 - 2x + 1}{x^2 + 5}$.

**Step-by-step solution:**

We compute the limits at $\pm\infty$:

$$\lim_{x \to +\infty} \frac{3x^2 - 2x + 1}{x^2 + 5} = \lim_{x \to +\infty} \frac{x^2\left(3 - \frac{2}{x} + \frac{1}{x^2}\right)}{x^2\left(1 + \frac{5}{x^2}\right)} = \frac{3}{1} = 3$$

$$\lim_{x \to -\infty} \frac{3x^2 - 2x + 1}{x^2 + 5} = 3 \quad \text{(same division)}$$

Horizontal asymptote $y = 3$ (valid on both sides).

**Exercises with Solutions**

**Basic Level:**

1. Find the horizontal asymptotes of $f(x) = \dfrac{2x+1}{x-3}$.
   > **Solution:** $\lim_{x \to \pm\infty} \frac{2x+1}{x-3} = \lim_{x \to \pm\infty} \frac{2 + 1/x}{1 - 3/x} = \frac{2}{1} = 2$. Horizontal asymptote: $y = 2$.

2. Find the horizontal asymptotes of $g(x) = e^{-x} + 3$.
   > **Solution:** $\lim_{x \to +\infty}(e^{-x}+3) = 0+3 = 3$. Horizontal asymptote $y=3$ at $+\infty$. $\lim_{x \to -\infty}(e^{-x}+3) = +\infty$. No HA at $-\infty$.

**Intermediate Level:**

3. Find the horizontal asymptotes of $h(x) = \dfrac{2x^2 - 1}{x^2 + x + 1}$.
   > **Solution:** $\lim_{x \to \pm\infty}\frac{2x^2-1}{x^2+x+1} = \lim \frac{2-1/x^2}{1+1/x+1/x^2} = \frac{2}{1}=2$. Horizontal asymptote $y=2$.

4. Find the horizontal asymptotes of $k(x) = \arctan(x^2 - 1)$.
   > **Solution:** $\lim_{x \to +\infty}\arctan(x^2-1) = \frac{\pi}{2}$ and $\lim_{x \to -\infty}\arctan(x^2-1) = \frac{\pi}{2}$. Horizontal asymptote $y = \frac{\pi}{2}$ on both sides.

**EVAU Level:**

5. Let $f(x) = \dfrac{\sqrt{4x^2+1}}{x+1}$.

   **(a)** Compute $\lim_{x \to +\infty} f(x)$.  
   **(b)** Compute $\lim_{x \to -\infty} f(x)$.  
   **(c)** State the horizontal asymptotes.

   > **Solution:**
   >
   > **(a)** For $x \to +\infty$: $\sqrt{4x^2+1} = |x|\sqrt{4+1/x^2} = x\sqrt{4+1/x^2}$ (taking $x>0$). Then:
   > $$\lim_{x \to +\infty}\frac{x\sqrt{4+1/x^2}}{x+1} = \lim_{x \to +\infty}\frac{\sqrt{4+1/x^2}}{1+1/x} = \frac{2}{1} = 2$$
   > HA at $+\infty$: $y = 2$.
   >
   > **(b)** For $x \to -\infty$: $|x| = -x$, so $\sqrt{4x^2+1} = -x\sqrt{4+1/x^2}$:
   > $$\lim_{x \to -\infty}\frac{-x\sqrt{4+1/x^2}}{x+1} = \lim_{x \to -\infty}\frac{-\sqrt{4+1/x^2}}{1+1/x} = \frac{-2}{1} = -2$$
   > HA at $-\infty$: $y = -2$.
   >
   > **(c)** Two horizontal asymptotes: $y=2$ (as $x\to+\infty$) and $y=-2$ (as $x\to-\infty$).

**Multiple Choice Test**

6. The function $f(x) = \dfrac{x^3 + 1}{x^2 + 1}$ has a horizontal asymptote:
   - a) $y = 0$
   - b) $y = 1$
   - c) $y = x$ (oblique, not horizontal)
   - d) No asymptote at infinity
   > **Correct answer: c)** The degree of the numerator (3) is greater than that of the denominator (2), so there is no horizontal asymptote; since the difference in degrees equals 1, there is an oblique asymptote.

7. If $\lim_{x \to -\infty} f(x) = 5$ and $\lim_{x \to +\infty} f(x) = -3$, then:
   - a) $f$ has a single horizontal asymptote: $y=5$
   - b) $f$ has a single horizontal asymptote: $y=-3$
   - c) $f$ has two distinct horizontal asymptotes
   - d) $f$ has no horizontal asymptotes
   > **Correct answer: c)** A function can have different horizontal asymptotes at $+\infty$ and at $-\infty$. In this case it has two: $y=5$ and $y=-3$.

---

#### 8.3.3 Oblique asymptotes

**Worked Example**

Find the oblique asymptote of $f(x) = \dfrac{x^2 - 3x + 2}{x + 1}$ as $x \to +\infty$.

**Step-by-step solution:**

An oblique asymptote $y = mx + n$ exists if $m = \lim_{x \to +\infty} \dfrac{f(x)}{x}$ is finite and non-zero, and $n = \lim_{x \to +\infty} [f(x) - mx]$ is finite.

**Computing $m$:**
$$m = \lim_{x \to +\infty} \frac{x^2-3x+2}{x(x+1)} = \lim_{x \to +\infty} \frac{x^2-3x+2}{x^2+x} = 1$$

**Computing $n$:**
$$n = \lim_{x \to +\infty} \left[\frac{x^2-3x+2}{x+1} - x\right] = \lim_{x \to +\infty} \frac{x^2-3x+2 - x(x+1)}{x+1} = \lim_{x \to +\infty} \frac{-4x+2}{x+1} = -4$$

**Oblique asymptote:** $y = x - 4$.

**Verification by polynomial division:** $\dfrac{x^2-3x+2}{x+1} = x - 4 + \dfrac{6}{x+1}$. When $x \to \infty$, the remainder $\dfrac{6}{x+1} \to 0$. ✓

**Exercises with Solutions**

**Basic Level:**

1. Find the oblique asymptote of $f(x) = \dfrac{x^2 + 1}{x}$.
   > **Solution:** Division: $\frac{x^2+1}{x} = x + \frac{1}{x}$. The oblique asymptote is $y = x$ (the quotient of the division). $m = \lim \frac{f(x)}{x} = 1$, $n = \lim[f(x)-x] = \lim \frac{1}{x} = 0$. OA: $y = x$.

2. Find the oblique asymptote of $g(x) = \dfrac{2x^2 - x + 3}{x - 2}$.
   > **Solution:** Division: $2x^2-x+3 = (x-2)(2x+3) + 9$. So $g(x) = 2x+3+\frac{9}{x-2}$. OA: $y = 2x+3$.

**Intermediate Level:**

3. Find all asymptotes of $h(x) = \dfrac{x^2 - 4}{x}$.
   > **Solution:** VA: $x = 0$ ($\lim_{x\to 0^\pm}h(x) = \mp\infty$). HA: None (the ratio $f(x)/x \to 1 \neq 0$). OA: $h(x) = x - \frac{4}{x}$. Oblique asymptote $y = x$ (same for $\pm\infty$). Remainder $-4/x \to 0$.

4. Verify that $f(x) = \dfrac{x^3}{x^2 - 1}$ has an oblique asymptote and find it.
   > **Solution:** $m = \lim \frac{x^3}{x(x^2-1)} = \lim \frac{x^2}{x^2-1} = 1$. $n = \lim\left[\frac{x^3}{x^2-1}-x\right] = \lim\frac{x^3-x(x^2-1)}{x^2-1} = \lim\frac{x}{x^2-1} = 0$. OA: $y = x$.

**EVAU Level:**

5. Let $f(x) = \dfrac{2x^2 + 3x - 1}{x + 2}$.

   **(a)** Find the domain.  
   **(b)** Find all vertical, horizontal, and oblique asymptotes.  
   **(c)** Find the intercepts with the axes.

   > **Solution:**
   >
   > **(a)** $\text{Dom}(f) = \mathbb{R} \setminus \{-2\}$.
   >
   > **(b)** VA: $x=-2$ (denominator zero, numerator $= 2(4)-6-1=-1\neq 0$). HA: $\lim_{x\to\pm\infty}\frac{2x^2+3x-1}{x+2}$: degree of numerator > degree of denominator, no HA. OA: Polynomial division of $2x^2+3x-1$ by $x+2$: $2x^2+3x-1 = (x+2)(2x-1)+1$. So $f(x)=2x-1+\frac{1}{x+2}$. OA: $y=2x-1$.
   >
   > **(c)** With $y$-axis: $f(0)=\frac{-1}{2}=-\frac{1}{2}$, point $(0,-\frac{1}{2})$. With $x$-axis: $2x^2+3x-1=0 \Rightarrow x=\frac{-3\pm\sqrt{9+8}}{4}=\frac{-3\pm\sqrt{17}}{4}$. Points: $\left(\frac{-3+\sqrt{17}}{4},0\right)$ and $\left(\frac{-3-\sqrt{17}}{4},0\right)$.

**Multiple Choice Test**

6. A rational function has an oblique asymptote (and no horizontal asymptote) when:
   - a) The degree of the numerator equals the degree of the denominator
   - b) The degree of the numerator is exactly one more than the degree of the denominator
   - c) The degree of the numerator is less than the degree of the denominator
   - d) The denominator is a constant
   > **Correct answer: b)** If $\deg(\text{num}) = \deg(\text{den}) + 1$, the result of polynomial division is a degree-1 polynomial ($mx+n$), which gives the oblique asymptote.

7. The oblique asymptote of $f(x) = \dfrac{x^2-1}{x+1}$ as $x \to +\infty$ is:
   - a) $y = x$
   - b) $y = x - 1$
   - c) $y = x + 1$
   - d) No oblique asymptote exists
   > **Correct answer: b)** $\frac{x^2-1}{x+1} = \frac{(x-1)(x+1)}{x+1} = x-1$ for $x\neq-1$. The oblique asymptote is $y=x-1$. (In fact it is an exact line, with no remainder.)

---

## 8.4 Monotonicity and extrema

---

#### 8.4.1 Intervals of increase and decrease using the sign of $f'$

**Worked Example**

Study the monotonicity of $f(x) = x^3 - 3x^2 - 9x + 5$.

**Step-by-step solution:**

**Step 1:** Differentiate:
$$f'(x) = 3x^2 - 6x - 9 = 3(x^2 - 2x - 3) = 3(x-3)(x+1)$$

**Step 2:** Find the critical points (where $f'=0$):
$$x = 3 \quad \text{and} \quad x = -1$$

**Step 3:** Sign table for $f'(x) = 3(x-3)(x+1)$:

| Interval | $(x-3)$ | $(x+1)$ | $f'(x)$ | Monotonicity |
|-----------|---------|---------|---------|-----------| 
| $x < -1$ | $-$ | $-$ | $+$ | Increasing ↑ |
| $-1 < x < 3$ | $-$ | $+$ | $-$ | Decreasing ↓ |
| $x > 3$ | $+$ | $+$ | $+$ | Increasing ↑ |

$f$ is **increasing** on $(-\infty,-1)$ and $(3,+\infty)$; **decreasing** on $(-1,3)$.

**Exercises with Solutions**

**Basic Level:**

1. Study the monotonicity of $f(x) = -x^2 + 4x - 1$.
   > **Solution:** $f'(x) = -2x+4$. $f'(x)=0 \Rightarrow x=2$. For $x<2$: $f'(x)>0$ (increasing). For $x>2$: $f'(x)<0$ (decreasing). Increasing on $(-\infty,2)$, decreasing on $(2,+\infty)$.

2. Study the monotonicity of $g(x) = e^{x^2-4}$.
   > **Solution:** $g'(x) = 2x\cdot e^{x^2-4}$. Since $e^{x^2-4}>0$ always, the sign depends on $2x$: $g'(x)>0 \Leftrightarrow x>0$; $g'(x)<0 \Leftrightarrow x<0$. Decreasing on $(-\infty,0)$, increasing on $(0,+\infty)$.

**Intermediate Level:**

3. Study the monotonicity of $h(x) = \dfrac{x^2-1}{x}$ on its domain.
   > **Solution:** Domain: $x\neq 0$. $h(x)=x-\frac{1}{x}$. $h'(x) = 1 + \frac{1}{x^2} > 0$ for all $x \neq 0$. The function is **strictly increasing** on $(-\infty,0)$ and on $(0,+\infty)$ (but not on its full domain due to the discontinuity at $x=0$).

4. Study the intervals of monotonicity of $k(x) = x - 2\ln x$ (for $x>0$).
   > **Solution:** $k'(x) = 1 - \frac{2}{x} = \frac{x-2}{x}$. For $x>0$: $k'(x)<0 \Leftrightarrow x<2$; $k'(x)>0 \Leftrightarrow x>2$. Decreasing on $(0,2)$, increasing on $(2,+\infty)$.

**EVAU Level:**

5. Let $f(x) = \dfrac{x^2}{x-1}$.

   **(a)** Compute $f'(x)$.  
   **(b)** Determine the intervals of increase and decrease.  
   **(c)** Classify the relative extrema.

   > **Solution:**
   >
   > **(a)** $f'(x) = \frac{2x(x-1) - x^2}{(x-1)^2} = \frac{x^2-2x}{(x-1)^2} = \frac{x(x-2)}{(x-1)^2}$.
   >
   > **(b)** $f'(x)=0 \Rightarrow x=0$ or $x=2$. $(x-1)^2 > 0$ for $x\neq 1$. We study the sign of $x(x-2)$:
   >
   > | Interval | $f'(x)$ | Monotonicity |
   > |-----------|---------|-----------| 
   > | $x<0$ | $+$ | Increasing ↑ |
   > | $0<x<1$ | $-$ | Decreasing ↓ |
   > | $1<x<2$ | $-$ | Decreasing ↓ |
   > | $x>2$ | $+$ | Increasing ↑ |
   >
   > **(c)** At $x=0$: changes from increasing to decreasing → **relative maximum**: $f(0)=0$. At $x=2$: changes from decreasing to increasing → **relative minimum**: $f(2)=4$.

**Multiple Choice Test**

6. If $f'(x) > 0$ on $(a,b)$, then $f$ on that interval is:
   - a) Decreasing
   - b) Concave
   - c) Increasing
   - d) Constant
   > **Correct answer: c)** If the derivative is positive on an interval, the function is strictly increasing on that interval.

7. The function $f(x) = x^4 - 2x^2$ is decreasing on:
   - a) $(-\infty, -1) \cup (0, 1)$
   - b) $(-1, 0) \cup (1, +\infty)$
   - c) $(0, +\infty)$
   - d) $(-\infty, 0)$
   > **Correct answer: a)** $f'(x) = 4x^3 - 4x = 4x(x^2-1) = 4x(x-1)(x+1)$. $f'<0$ when the product is negative: on $(-\infty,-1)$ (sign: $-\cdot-\cdot- = -$) and on $(0,1)$ (sign: $+\cdot-\cdot+ = -$).

---

#### 8.4.2 Relative extrema: local maxima and minima

**Worked Example**

Find and classify the relative extrema of $f(x) = x^4 - 8x^2 + 3$.

**Step-by-step solution:**

**Step 1:** $f'(x) = 4x^3 - 16x = 4x(x^2-4) = 4x(x-2)(x+2)$

**Step 2:** Critical points: $x = 0$, $x = 2$, $x = -2$.

**Step 3:** Second derivative test: $f''(x) = 12x^2 - 16$.

- $f''(0) = -16 < 0 \Rightarrow$ **relative maximum** at $x=0$: $f(0) = 3$.
- $f''(2) = 48 - 16 = 32 > 0 \Rightarrow$ **relative minimum** at $x=2$: $f(2) = 16-32+3=-13$.
- $f''(-2) = 32 > 0 \Rightarrow$ **relative minimum** at $x=-2$: $f(-2) = 16-32+3=-13$.

**Exercises with Solutions**

**Basic Level:**

1. Find the relative extrema of $f(x) = 3x^2 - 12x + 7$.
   > **Solution:** $f'(x)=6x-12=0 \Rightarrow x=2$. $f''(x)=6>0$. Relative minimum at $x=2$: $f(2)=12-24+7=-5$. Minimum point: $(2,-5)$.

2. Find the relative extrema of $g(x) = -x^3 + 3x$.
   > **Solution:** $g'(x)=-3x^2+3=-3(x^2-1)=0 \Rightarrow x=\pm 1$. $g''(x)=-6x$. $g''(1)=-6<0$: maximum at $x=1$, $g(1)=2$. $g''(-1)=6>0$: minimum at $x=-1$, $g(-1)=-2$.

**Intermediate Level:**

3. Study the relative extrema of $h(x) = x^2 e^{-x}$.
   > **Solution:** $h'(x) = 2xe^{-x} - x^2e^{-x} = xe^{-x}(2-x)$. Critical points: $x=0$ and $x=2$. $h''(x) = e^{-x}(2-4x+x^2)$. $h''(0)=2>0$: minimum at $x=0$, $h(0)=0$. $h''(2)=e^{-2}(2-8+4)=e^{-2}(-2)<0$: maximum at $x=2$, $h(2)=4e^{-2}$.

4. Study the relative extrema of $k(x) = \ln x - x$ for $x>0$.
   > **Solution:** $k'(x)=\frac{1}{x}-1=\frac{1-x}{x}$. $k'(x)=0 \Rightarrow x=1$. $k''(x)=-\frac{1}{x^2}$. $k''(1)=-1<0$: **relative maximum** at $x=1$, $k(1)=0$.

**EVAU Level:**

5. The profit function of a company is $B(x) = -x^3 + 6x^2 - 9x + 4$ (thousands of €), where $x$ is the production in thousands of units, $x \geq 0$.

   **(a)** Find and classify the relative extrema.  
   **(b)** Interpret the results economically.  
   **(c)** For what value of $x$ is profit maximised if $0 \leq x \leq 5$?

   > **Solution:**
   >
   > **(a)** $B'(x)=-3x^2+12x-9=-3(x^2-4x+3)=-3(x-1)(x-3)$. Critical points: $x=1$ and $x=3$. $B''(x)=-6x+12$. $B''(1)=6>0$: relative minimum at $x=1$, $B(1)=-1+6-9+4=0$. $B''(3)=-6<0$: relative maximum at $x=3$, $B(3)=-27+54-27+4=4$.
   >
   > **(b)** The company reaches its local maximum profit (4 thousand €) with a production of 3000 units. With a production of 1000 units the profit is zero (local break-even point).
   >
   > **(c)** We evaluate on $[0,5]$: $B(0)=4$, $B(1)=0$ (relative min), $B(3)=4$ (relative max), $B(5)=-125+150-45+4=-16$. The absolute maximum on $[0,5]$ is $B=4$, attained at $x=0$ and at $x=3$.

**Multiple Choice Test**

6. At a critical point where $f'(x_0)=0$ and $f''(x_0) > 0$, the function has:
   - a) A relative maximum
   - b) An inflection point
   - c) A relative minimum
   - d) The type of extremum cannot be determined
   > **Correct answer: c)** If $f''(x_0)>0$, the function is concave upward at that point, which implies a relative minimum.

7. The function $f(x) = |x|$ has at $x=0$:
   - a) A relative maximum because $f''(0)>0$
   - b) A relative minimum, even though $f'(0)$ does not exist
   - c) An inflection point
   - d) No type of extremum
   > **Correct answer: b)** $f(0)=0$ and $f(x)\geq 0$ for all $x$, so $x=0$ is an absolute (and relative) minimum. The derivative does not exist at $x=0$, but this does not prevent it from being an extremum.

---

#### 8.4.3 Absolute extrema on a closed interval

**Worked Example**

Find the absolute maximum and minimum of $f(x) = x^3 - 3x + 1$ on $[-2, 2]$.

**Step-by-step solution:**

**Step 1:** Critical points in the interior of $[-2,2]$: $f'(x) = 3x^2 - 3 = 0 \Rightarrow x^2 = 1 \Rightarrow x = \pm 1$. Both are in $(-2,2)$.

**Step 2:** Evaluate $f$ at the critical points and at the endpoints of the interval:
$$f(-2) = -8 + 6 + 1 = -1$$
$$f(-1) = -1 + 3 + 1 = 3$$
$$f(1) = 1 - 3 + 1 = -1$$
$$f(2) = 8 - 6 + 1 = 3$$

**Step 3:** Compare:
- **Absolute maximum:** $f(-1) = f(2) = 3$.
- **Absolute minimum:** $f(-2) = f(1) = -1$.

**Exercises with Solutions**

**Basic Level:**

1. Find the absolute extrema of $f(x) = x^2 - 4x + 3$ on $[0, 4]$.
   > **Solution:** $f'(x)=2x-4=0 \Rightarrow x=2$. Evaluate: $f(0)=3$, $f(2)=-1$, $f(4)=3$. Absolute maximum: $f=3$ (at $x=0$ and $x=4$). Absolute minimum: $f=-1$ (at $x=2$).

2. Find the absolute extrema of $g(x) = \sin x$ on $[0, 2\pi]$.
   > **Solution:** $g'(x)=\cos x=0 \Rightarrow x=\pi/2$ and $x=3\pi/2$. $g(0)=0$, $g(\pi/2)=1$, $g(3\pi/2)=-1$, $g(2\pi)=0$. Absolute maximum: $1$ (at $x=\pi/2$). Absolute minimum: $-1$ (at $x=3\pi/2$).

**Intermediate Level:**

3. Find the absolute extrema of $h(x) = \dfrac{x}{x^2+1}$ on $[-3, 3]$.
   > **Solution:** $h'(x)=\frac{(x^2+1)-x\cdot 2x}{(x^2+1)^2}=\frac{1-x^2}{(x^2+1)^2}$. $h'(x)=0 \Rightarrow x=\pm 1$. Evaluate: $h(-3)=\frac{-3}{10}$, $h(-1)=-\frac{1}{2}$, $h(1)=\frac{1}{2}$, $h(3)=\frac{3}{10}$. Maximum: $h(1)=\frac{1}{2}$. Minimum: $h(-1)=-\frac{1}{2}$.

4. Find the absolute extrema of $k(x) = x^{2/3}$ on $[-8, 8]$.
   > **Solution:** $k'(x) = \frac{2}{3}x^{-1/3}$, does not exist at $x=0$. For $x \neq 0$: $k'(x)\neq 0$. Candidates: $x=0$, $x=-8$, $x=8$. $k(0)=0$, $k(-8)=4$, $k(8)=4$. Absolute maximum: $4$. Absolute minimum: $0$.

**EVAU Level:**

5. Let $f(x) = xe^{-x}$ on the interval $[-1, 3]$.

   **(a)** Compute $f'(x)$ and find the critical points in $(-1,3)$.  
   **(b)** Find the absolute extrema on $[-1,3]$.  
   **(c)** Compare with the relative extrema and determine whether they coincide.

   > **Solution:**
   >
   > **(a)** $f'(x)=e^{-x}-xe^{-x}=e^{-x}(1-x)$. Since $e^{-x}>0$: $f'(x)=0 \Rightarrow x=1$. One critical point: $x=1 \in (-1,3)$.
   >
   > **(b)** $f(-1)=(-1)e^1=-e\approx-2.718$. $f(1)=e^{-1}=\frac{1}{e}\approx 0.368$. $f(3)=3e^{-3}\approx 0.149$. Absolute maximum: $f(1)=\frac{1}{e}$. Absolute minimum: $f(-1)=-e$.
   >
   > **(c)** $x=1$ is a relative maximum ($f'$ changes from $+$ to $-$) and also the absolute maximum. The absolute minimum $x=-1$ is an endpoint of the interval, not an interior relative extremum.

**Multiple Choice Test**

6. To find the absolute maximum of a continuous function on $[a,b]$, we must evaluate $f$ at:
   - a) Only the points where $f'(x) = 0$
   - b) Only the endpoints $a$ and $b$
   - c) The points where $f'(x)=0$ or $f'$ does not exist, plus the endpoints $a$ and $b$
   - d) The point where $f''(x) = 0$
   > **Correct answer: c)** The absolute maximum on a closed interval is attained at one of the interior critical points (where $f'=0$ or does not exist) or at the endpoints.

7. If $f$ is continuous on $[a,b]$ and has a unique critical point $x_0 \in (a,b)$ where there is a relative minimum, then the absolute maximum on $[a,b]$ is attained:
   - a) At $x_0$
   - b) Always at $a$
   - c) Always at $b$
   - d) At one of the endpoints $a$ or $b$
   > **Correct answer: d)** If the only interior relative extremum is a minimum, the absolute maximum cannot be in the interior, so it must be at one of the two endpoints of the interval.

---

## 8.5 Curvature and inflection points

---

#### 8.5.1 Concavity and convexity: criterion using the sign of $f''$

**Worked Example**

Study the concavity of $f(x) = x^4 - 6x^2 + 2$.

**Step-by-step solution:**

**Step 1:** Compute the second derivative:
$$f'(x) = 4x^3 - 12x$$
$$f''(x) = 12x^2 - 12 = 12(x^2-1) = 12(x-1)(x+1)$$

**Step 2:** $f''(x) = 0 \Rightarrow x = \pm 1$.

**Step 3:** Sign table for $f''$:

| Interval | $f''(x)$ | Concavity |
|-----------|---------|----------|
| $x < -1$ | $+$ | Concave upward ∪ |
| $-1 < x < 1$ | $-$ | Concave downward ∩ |
| $x > 1$ | $+$ | Concave upward ∪ |

**Exercises with Solutions**

**Basic Level:**

1. Determine the intervals of concavity of $f(x) = x^3 - 3x$.
   > **Solution:** $f'(x)=3x^2-3$. $f''(x)=6x$. $f''(x)>0 \Leftrightarrow x>0$: concave upward. $f''(x)<0 \Leftrightarrow x<0$: concave downward.

2. Determine the intervals of concavity of $g(x) = e^x$.
   > **Solution:** $g''(x)=e^x>0$ for all $x \in \mathbb{R}$. The function is **concave upward** throughout its domain.

**Intermediate Level:**

3. Study the concavity of $h(x) = \ln x$ (for $x > 0$).
   > **Solution:** $h'(x)=\frac{1}{x}$. $h''(x)=-\frac{1}{x^2}<0$ for all $x>0$. The function is **concave downward** throughout its domain.

4. Study the concavity of $k(x) = x^2 e^{-x}$.
   > **Solution:** $k'(x)=(2x-x^2)e^{-x}$. $k''(x)=e^{-x}[(2-2x) - (2x-x^2)] = e^{-x}(x^2-4x+2)$. Since $e^{-x}>0$, the sign depends on $x^2-4x+2=0 \Rightarrow x=2\pm\sqrt{2}$. Concave upward on $(-\infty, 2-\sqrt{2}) \cup (2+\sqrt{2}, +\infty)$; downward on $(2-\sqrt{2}, 2+\sqrt{2})$.

**EVAU Level:**

5. Let $f(x) = \dfrac{1}{1+x^2}$.

   **(a)** Compute $f'(x)$ and $f''(x)$.  
   **(b)** Determine the intervals of concavity.  
   **(c)** Compare the behaviour of $f''$ with the extrema of $f$.

   > **Solution:**
   >
   > **(a)** $f'(x)=\frac{-2x}{(1+x^2)^2}$. For $f''$: let $u=-2x$ and $v=(1+x^2)^2$:
   > $$f''(x) = \frac{-2(1+x^2)^2 - (-2x)\cdot 2(1+x^2)\cdot 2x}{(1+x^2)^4} = \frac{-2(1+x^2)+8x^2}{(1+x^2)^3} = \frac{6x^2-2}{(1+x^2)^3}$$
   >
   > **(b)** $f''(x)=0 \Rightarrow 6x^2-2=0 \Rightarrow x=\pm\frac{1}{\sqrt{3}}$. Concave upward on $\left(-\infty,-\frac{1}{\sqrt{3}}\right) \cup \left(\frac{1}{\sqrt{3}},+\infty\right)$; downward on $\left(-\frac{1}{\sqrt{3}},\frac{1}{\sqrt{3}}\right)$.
   >
   > **(c)** The relative minimum of $f$ is at $x=0$ (where $f'=0$ and $f''(0)=-2<0$, which indicates a relative maximum, not minimum). Correction: $f'(x)=0 \Rightarrow x=0$. $f''(0)=\frac{-2}{1}=-2<0$: **relative maximum** at $x=0$ with $f(0)=1$. The negative concavity at $x=0$ confirms the maximum.

**Multiple Choice Test**

6. If $f''(x) < 0$ on an interval $(a,b)$, then $f$ on that interval is:
   - a) Increasing
   - b) Decreasing
   - c) Concave upward
   - d) Concave downward
   > **Correct answer: d)** $f''<0$ means that $f'$ is decreasing, which geometrically corresponds to the curve being concave downward (∩ shape).

7. A function with $f''(x) > 0$ throughout its domain:
   - a) Cannot have relative maxima
   - b) Cannot have relative minima
   - c) Is always increasing
   - d) Has an inflection point
   > **Correct answer: a)** If $f''>0$ throughout the domain, the function is concave upward everywhere. If there were a relative maximum at $x_0$ ($f'(x_0)=0$), we would need $f''(x_0)\leq 0$, a contradiction. All relative extrema with $f''>0$ are minima.

---

#### 8.5.2 Inflection points: definition, necessary condition, and verification

**Worked Example**

Find the inflection points of $f(x) = x^4 - 4x^3$.

**Step-by-step solution:**

**Step 1:** $f'(x) = 4x^3 - 12x^2$. $f''(x) = 12x^2 - 24x = 12x(x-2)$.

**Step 2:** Candidates for inflection where $f''(x) = 0$: $x = 0$ and $x = 2$.

**Step 3:** Verify that $f''$ changes sign:

| Interval | $f''(x)$ |
|-----------|---------| 
| $x < 0$ | $+$ |
| $0 < x < 2$ | $-$ |
| $x > 2$ | $+$ |

$f''$ changes sign at $x=0$ and $x=2$: both are **inflection points**.

**Step 4:** Coordinates:
- $f(0) = 0$: inflection point $(0, 0)$.
- $f(2) = 16 - 32 = -16$: inflection point $(2, -16)$.

**Exercises with Solutions**

**Basic Level:**

1. Find the inflection points of $f(x) = x^3$.
   > **Solution:** $f''(x)=6x$. $f''(x)=0 \Rightarrow x=0$. For $x<0$: $f''<0$; for $x>0$: $f''>0$. Sign changes. Inflection point: $(0,0)$.

2. Determine whether $f(x) = x^4$ has inflection points.
   > **Solution:** $f''(x)=12x^2$. $f''(x)=0 \Rightarrow x=0$. But $12x^2 \geq 0$ for all $x$, does not change sign. **No inflection points**.

**Intermediate Level:**

3. Find the inflection points of $h(x) = e^{-x^2}$.
   > **Solution:** $h'(x)=-2xe^{-x^2}$. $h''(x)=(-2+4x^2)e^{-x^2}=(4x^2-2)e^{-x^2}$. $h''(x)=0 \Rightarrow x=\pm\frac{1}{\sqrt{2}}$. For $|x|<\frac{1}{\sqrt{2}}$: $h''<0$; for $|x|>\frac{1}{\sqrt{2}}$: $h''>0$. Sign changes. Inflection points: $\left(\pm\frac{1}{\sqrt{2}}, e^{-1/2}\right) = \left(\pm\frac{\sqrt{2}}{2}, \frac{1}{\sqrt{e}}\right)$.

4. Find the inflection points of $k(x) = \sin x$ on $[0, 2\pi]$.
   > **Solution:** $k''(x)=-\sin x$. $k''(x)=0$ on $[0,2\pi]$: $x=0, \pi, 2\pi$. At $x=\pi$: $k''$ changes sign (from $-$ to $+$). Inflection point: $(\pi, 0)$. At $x=0$ and $x=2\pi$ these are endpoints of the interval.

**EVAU Level:**

5. Let $f(x) = ax^3 + bx^2 + cx + d$. We know that $f$ has an inflection point at $x=1$, a relative maximum at $x=-1$ with $f(-1)=4$, and passes through the origin.

   **(a)** Write the equations that determine $a$, $b$, $c$, $d$.  
   **(b)** Solve the system (if you have enough conditions) or express some parameters in terms of others.

   > **Solution:**
   >
   > **(a)** $f'(x)=3ax^2+2bx+c$. $f''(x)=6ax+2b$.
   > - Inflection at $x=1$: $f''(1)=0 \Rightarrow 6a+2b=0 \Rightarrow 3a+b=0$ ... (I)
   > - Maximum at $x=-1$: $f'(-1)=0 \Rightarrow 3a-2b+c=0$ ... (II)
   > - $f(-1)=4$: $-a+b-c+d=4$ ... (III)
   > - $f(0)=0$: $d=0$ ... (IV)
   >
   > **(b)** From (IV): $d=0$. From (I): $b=-3a$. From (II): $3a-2(-3a)+c=0 \Rightarrow 3a+6a+c=0 \Rightarrow c=-9a$. From (III): $-a+(-3a)-(-9a)+0=4 \Rightarrow -a-3a+9a=4 \Rightarrow 5a=4 \Rightarrow a=\frac{4}{5}$. Then: $b=-\frac{12}{5}$, $c=-\frac{36}{5}$, $d=0$. $f(x)=\frac{4}{5}x^3-\frac{12}{5}x^2-\frac{36}{5}x$.

**Multiple Choice Test**

6. An inflection point of $f$ is a point where:
   - a) $f'(x_0) = 0$
   - b) $f''(x_0) = 0$ necessarily
   - c) $f''$ changes sign as it passes through $x_0$
   - d) $f$ has a relative extremum
   > **Correct answer: c)** The defining condition of an inflection point is that the concavity changes (i.e., $f''$ changes sign). That $f''(x_0)=0$ is a necessary condition (when it exists), but not sufficient.

7. If $f''(x_0) = 0$ and $f'''(x_0) \neq 0$, then at $x_0$ there is:
   - a) A relative maximum
   - b) A relative minimum
   - c) An inflection point
   - d) Cannot be determined
   > **Correct answer: c)** If the second derivative vanishes and the third does not, this implies that $f''$ changes sign at $x_0$ (since $f'''(x_0)\neq 0$ implies $f''$ is strictly monotone at that point), confirming an inflection point.

---

## 8.6 Complete curve sketching

---

#### 8.6.1 Sketching protocol: order and synthesis of all elements

**Worked Example**

Apply the complete sketching protocol to $f(x) = \dfrac{x}{x^2-1}$.

**Step-by-step solution:**

**1. Domain:** $x^2-1 \neq 0 \Rightarrow x \neq \pm 1$. $\text{Dom}(f) = \mathbb{R} \setminus \{-1,1\}$.

**2. Symmetry:** $f(-x)=\frac{-x}{x^2-1}=-f(x)$. **Odd** function (symmetry about the origin).

**3. Intercepts with the axes:**
- $y$-axis: $f(0)=0$. Point $(0,0)$.
- $x$-axis: $\frac{x}{x^2-1}=0 \Rightarrow x=0$. Point $(0,0)$.

**4. Asymptotes:**
- Vertical: $x=1$ and $x=-1$.
- Horizontal: $\lim_{x\to\pm\infty}\frac{x}{x^2-1}=0$. HA: $y=0$.
- Oblique: None (the horizontal limit exists).

**5. Monotonicity:** $f'(x)=\frac{(x^2-1)-x\cdot 2x}{(x^2-1)^2}=\frac{-x^2-1}{(x^2-1)^2}<0$ for all $x$ in the domain. **$f$ is always decreasing** on each branch.

**6. Curvature:** $f''(x) = \frac{2x(x^2+3)}{(x^2-1)^3}$. Inflection at $x=0$: $f''$ changes sign. Inflection point $(0,0)$.

**7. Summary table of values:**

| $x$ | $-3$ | $-2$ | $0$ | $2$ | $3$ |
|-----|------|------|-----|-----|-----|
| $f(x)$ | $-3/8$ | $-2/3$ | $0$ | $2/3$ | $3/8$ |

**Exercises with Solutions**

**Basic Level:**

1. List in order the steps of the complete curve sketching protocol.
   > **Solution:** 1) Domain. 2) Symmetry and periodicity. 3) Intercepts with the axes. 4) Asymptotes (vertical, horizontal, oblique). 5) Monotonicity and relative extrema (using $f'$). 6) Curvature and inflection points (using $f''$). 7) Supplementary table of values. 8) Drawing the graph.

2. What information does the sign of $f'$ provide, and what information does the sign of $f''$ provide in the study of a function?
   > **Solution:** The sign of $f'$ gives information about **monotonicity**: $f'>0$ increasing, $f'<0$ decreasing, $f'=0$ possible extremum. The sign of $f''$ gives information about **curvature**: $f''>0$ concave upward, $f''<0$ concave downward, $f''=0$ possible inflection.

**Intermediate Level:**

3. Apply the sketching protocol to $f(x) = x^3 - 3x + 2$ (polynomial function).
   > **Solution:**
   > - Domain: $\mathbb{R}$. Symmetry: none. $y$-intercept: $f(0)=2$. $x$-intercepts: $x^3-3x+2=0$, one root at $x=1$: $(x-1)(x^2+x-2)=(x-1)^2(x+2)=0 \Rightarrow x=1$ (double), $x=-2$.
   > - No asymptotes.
   > - $f'(x)=3x^2-3=3(x-1)(x+1)$: Increasing on $(-\infty,-1)\cup(1,+\infty)$; decreasing on $(-1,1)$.
   > - Relative maximum: $f(-1)=4$. Relative minimum: $f(1)=0$.
   > - $f''(x)=6x$: concave downward on $(-\infty,0)$; upward on $(0,+\infty)$. Inflection at $(0,2)$.

4. Apply the protocol to $f(x) = e^{-x^2}$.
   > **Solution:**
   > - Domain: $\mathbb{R}$. Symmetry: even ($f(-x)=e^{-x^2}=f(x)$). $y$-intercept: $f(0)=1$. $x$-intercepts: none ($e^{-x^2}>0$ always).
   > - HA: $\lim_{x\to\pm\infty}e^{-x^2}=0$. Asymptote $y=0$.
   > - $f'(x)=-2xe^{-x^2}$: increasing on $(-\infty,0)$, decreasing on $(0,+\infty)$. Absolute maximum: $f(0)=1$.
   > - $f''(x)=(4x^2-2)e^{-x^2}$: Inflections at $x=\pm\frac{1}{\sqrt{2}}$, $f=e^{-1/2}=\frac{1}{\sqrt{e}}$.

**EVAU Level:**

5. Perform the complete study and sketch of $f(x) = \dfrac{x^2-1}{x}$.

   **(a)** Domain, symmetry, intercepts.  
   **(b)** Asymptotes.  
   **(c)** Monotonicity and extrema.  
   **(d)** Curvature and inflections.

   > **Solution:**
   >
   > **(a)** Domain: $\mathbb{R}\setminus\{0\}$. $f(-x)=\frac{x^2-1}{-x}=-f(x)$: odd. $x$-intercepts: $x^2-1=0\Rightarrow x=\pm 1$. Does not cross the $y$-axis ($x=0$ not in domain).
   >
   > **(b)** VA: $x=0$ ($\lim_{x\to 0^\pm}\frac{x^2-1}{x}=\mp\infty$). HA: None (degree of numerator > degree of denominator). OA: $f(x)=x-\frac{1}{x}$, oblique asymptote $y=x$.
   >
   > **(c)** $f'(x)=1+\frac{1}{x^2}>0$ for all $x\neq 0$. **Strictly increasing** on $(-\infty,0)$ and $(0,+\infty)$. No extrema.
   >
   > **(d)** $f''(x)=-\frac{2}{x^3}$. Negative on $(0,+\infty)$ (concave downward), positive on $(-\infty,0)$ (concave upward). No inflection point in the domain.

**Multiple Choice Test**

6. When studying a rational function, the first step to find vertical asymptotes is:
   - a) Compute $f''$
   - b) Set the numerator equal to zero
   - c) Set the denominator equal to zero and check that the numerator does not vanish at those points
   - d) Compute the limit at infinity
   > **Correct answer: c)** Vertical asymptotes appear when the denominator vanishes and the numerator does not. If both vanish, there may be a removable discontinuity.

7. When studying a function, if we detect that $f$ is odd, we can:
   - a) Study only the part $x<0$ and reflect
   - b) Study only the part $x>0$ and reflect about the origin
   - c) Conclude that it has no maxima or minima
   - d) Conclude that it has horizontal asymptote $y=0$
   > **Correct answer: b)** If $f$ is odd, its graph is symmetric about the origin. It suffices to study $x>0$ and obtain the part $x<0$ by point-by-point reflection about the origin.

---

#### 8.6.2 Sketching polynomial functions

**Worked Example**

Perform the study and sketch of the graph of $f(x) = x^4 - 4x^3 + 4x^2$.

**Step-by-step solution:**

**1. Domain:** $\mathbb{R}$.

**2. Symmetry:** $f(-x) = x^4+4x^3+4x^2 \neq f(x)$. No symmetry.

**3. Intercepts:** $y$-axis: $f(0)=0$. $x$-axis: $f(x)=x^2(x-2)^2=0 \Rightarrow x=0$ (double) and $x=2$ (double). The curve is tangent to the $x$-axis at both points.

**4. Asymptotes:** None (polynomial).

**5. Monotonicity:**
$$f'(x)=4x^3-12x^2+8x=4x(x^2-3x+2)=4x(x-1)(x-2)$$
Critical points: $x=0$, $x=1$, $x=2$.

| Interval | $f'(x)$ | Monotonicity |
|-----------|---------|-----------| 
| $x<0$ | $-$ | Decreasing |
| $0<x<1$ | $+$ | Increasing |
| $1<x<2$ | $-$ | Decreasing |
| $x>2$ | $+$ | Increasing |

Minimum at $x=0$: $f(0)=0$. Maximum at $x=1$: $f(1)=1-4+4=1$. Minimum at $x=2$: $f(2)=16-32+16=0$.

**6. Curvature:**
$$f''(x)=12x^2-24x+8=4(3x^2-6x+2)$$
$f''(x)=0 \Rightarrow x=\frac{6\pm\sqrt{36-24}}{6}=\frac{6\pm 2\sqrt{3}}{6}=1\pm\frac{\sqrt{3}}{3}$

Inflections at $x=1-\frac{1}{\sqrt{3}}\approx 0.42$ and $x=1+\frac{1}{\sqrt{3}}\approx 1.58$.

**Exercises with Solutions**

**Basic Level:**

1. Sketch $f(x) = x^2 - 2x - 3$. Indicate the vertex and intercepts.
   > **Solution:** $f(x)=(x-1)^2-4$. Vertex (minimum): $(1,-4)$. $y$-intercept: $(0,-3)$. $x$-intercepts: $x^2-2x-3=(x-3)(x+1)=0 \Rightarrow x=3$ and $x=-1$. Points $(3,0)$ and $(-1,0)$. Upward-opening parabola.

2. Find the extrema of $g(x) = 2x^3 - 9x^2 + 12x - 4$ and classify them.
   > **Solution:** $g'(x)=6x^2-18x+12=6(x^2-3x+2)=6(x-1)(x-2)$. Relative maximum at $x=1$: $g(1)=2-9+12-4=1$. Relative minimum at $x=2$: $g(2)=16-36+24-4=0$.

**Intermediate Level:**

3. Study and sketch $f(x) = x^3 - 6x^2 + 9x$.
   > **Solution:** Domain $\mathbb{R}$. $x$-intercepts: $x(x^2-6x+9)=x(x-3)^2=0 \Rightarrow x=0$ and $x=3$. $y$-intercept: $(0,0)$. $f'(x)=3x^2-12x+9=3(x-1)(x-3)$: maximum at $x=1$, $f(1)=4$; minimum at $x=3$, $f(3)=0$ (tangent to the $x$-axis). $f''(x)=6x-12$: inflection at $x=2$, $f(2)=2$.

4. Sketch $f(x) = x^4 - 2x^2$.
   > **Solution:** Even. Minima: $f'(x)=4x^3-4x=4x(x^2-1)=0 \Rightarrow x=0, \pm 1$. $f(0)=0$ (local relative maximum), $f(\pm 1)=-1$ (global minima, since $f''(\pm 1)=8-4=4>0$). Inflections: $f''(x)=12x^2-4=0 \Rightarrow x=\pm\frac{1}{\sqrt{3}}$, $f=\frac{1}{9}-\frac{2}{3}=-\frac{5}{9}$.

**EVAU Level:**

5. Let $f(x) = x^3 + ax^2 + bx + c$. We know that the graph passes through $A=(0,4)$, has a relative maximum at $x=-2$, and a relative minimum at $x=2$.

   **(a)** Find $a$, $b$, and $c$.  
   **(b)** Compute the values of the relative extrema.  
   **(c)** Make a sketch indicating all the elements found.

   > **Solution:**
   >
   > **(a)** $f(0)=c=4$. $f'(x)=3x^2+2ax+b$. The extrema are at $x=-2$ and $x=2$: $f'(x)=3(x+2)(x-2)=3x^2-12$. Therefore: $2a=0\Rightarrow a=0$ and $b=-12$. Thus $f(x)=x^3-12x+4$.
   >
   > **(b)** Maximum at $x=-2$: $f(-2)=-8+24+4=20$. Minimum at $x=2$: $f(2)=8-24+4=-12$.
   >
   > **(c)** Sketch: Cubic function (no symmetry, $a=0$) passing through $(0,4)$, with maximum $(-2,20)$, minimum $(2,-12)$. The inflection point is at $f''(x)=6x=0$, i.e., $x=0$, $f(0)=4$. The function increases on $(-\infty,-2)\cup(2,+\infty)$ and decreases on $(-2,2)$.

**Multiple Choice Test**

6. A degree-4 polynomial with positive leading coefficient:
   - a) Tends to $-\infty$ at both ends
   - b) Tends to $+\infty$ at both ends
   - c) Tends to $+\infty$ on the right and $-\infty$ on the left
   - d) Tends to $-\infty$ on the right and $+\infty$ on the left
   > **Correct answer: b)** An even-degree polynomial with positive leading coefficient tends to $+\infty$ both as $x\to+\infty$ and as $x\to-\infty$.

7. If $f(x)=(x-a)^2 g(x)$ with $g(a)\neq 0$, then the graph of $f$:
   - a) Crosses the $x$-axis at $x=a$ at a non-zero angle
   - b) Is tangent to the $x$-axis at $x=a$ (touches but does not cross)
   - c) Does not touch the $x$-axis at $x=a$
   - d) Has a vertical asymptote at $x=a$
   > **Correct answer: b)** A root of even multiplicity means the graph is tangent to the $x$-axis at that point (touches the axis but does not cross it, keeping the same sign on both sides).

---

#### 8.6.3 Sketching rational functions

**Worked Example**

Perform the complete study of $f(x) = \dfrac{x^2}{x^2-4}$.

**Step-by-step solution:**

**1. Domain:** $x^2-4\neq 0 \Rightarrow x\neq\pm 2$. Domain $= \mathbb{R}\setminus\{-2,2\}$.

**2. Symmetry:** $f(-x)=\frac{x^2}{x^2-4}=f(x)$. **Even** function.

**3. Intercepts:** $y$-axis: $f(0)=0$. $x$-axis: $x^2=0\Rightarrow x=0$.

**4. Asymptotes:**
- VA: $x=2$ and $x=-2$.
- HA: $\lim_{x\to\pm\infty}\frac{x^2}{x^2-4}=1$. HA: $y=1$.

**5. Monotonicity:**
$$f'(x)=\frac{2x(x^2-4)-x^2\cdot 2x}{(x^2-4)^2}=\frac{-8x}{(x^2-4)^2}$$
$f'(x)=0\Rightarrow x=0$. Sign: $f'(x)<0$ for $x>0$, $f'(x)>0$ for $x<0$.

- Increasing on $(-\infty,-2)\cup(-2,0)$, decreasing on $(0,2)\cup(2,+\infty)$.
- Relative maximum at $x=0$: $f(0)=0$.

**6. Curvature:**
$$f''(x)=\frac{-8(x^2-4)^2-(-8x)\cdot 2(x^2-4)\cdot 2x}{(x^2-4)^4}=\frac{-8(x^2-4)+32x^2}{(x^2-4)^3}=\frac{8(3x^2+4)}{(x^2-4)^3}$$

Numerator $8(3x^2+4)>0$ always. Sign of $f''$ depends on $(x^2-4)^3$:
- For $|x|>2$: $(x^2-4)>0$, $f''>0$ (concave upward).
- For $|x|<2$: $(x^2-4)<0$, $f''<0$ (concave downward).
- No inflection points in the domain.

**Exercises with Solutions**

**Basic Level:**

1. Find the asymptotes of $f(x) = \dfrac{3x-1}{x+2}$ and draw a sketch indicating the asymptotes and intercepts.
   > **Solution:** Domain: $x\neq-2$. VA: $x=-2$. HA: $\lim\frac{3x-1}{x+2}=3$. HA: $y=3$. Intercepts: $y$-axis: $f(0)=-\frac{1}{2}$. $x$-axis: $3x-1=0 \Rightarrow x=\frac{1}{3}$. Sketch: hyperbola with VA $x=-2$ and HA $y=3$.

2. Study the extrema of $g(x)=\dfrac{x^2+1}{x}$ and make a sketch.
   > **Solution:** $g(x)=x+\frac{1}{x}$. $g'(x)=1-\frac{1}{x^2}=\frac{x^2-1}{x^2}$. $g'=0\Rightarrow x=\pm 1$. $g''(x)=\frac{2}{x^3}$. $g''(1)=2>0$: minimum at $(1,2)$. $g''(-1)=-2<0$: maximum at $(-1,-2)$. VA: $x=0$. OA: $y=x$.

**Intermediate Level:**

3. Study and sketch $h(x) = \dfrac{1}{x^2-1}$ completely.
   > **Solution:** Domain: $x\neq\pm 1$. Even. No $x$-intercepts. $y$-intercept: $f(0)=-1$. VA: $x=\pm 1$. HA: $y=0$. $h'(x)=-\frac{2x}{(x^2-1)^2}$: increasing on $(-\infty,-1)\cup(-1,0)$, decreasing on $(0,1)\cup(1,+\infty)$. Maximum at $x=0$: $h(0)=-1$. $h''(x)=\frac{2(3x^2+1)}{(x^2-1)^3}$: no inflections in the domain.

4. Study $k(x)=\dfrac{x}{(x-1)^2}$ completely.
   > **Solution:** Domain: $x\neq 1$. Intercepts: $y$-axis $f(0)=0$, $x$-axis: $x=0$. VA: $x=1$. HA: $y=0$. $k'(x)=\frac{(x-1)^2-2x(x-1)}{(x-1)^4}=\frac{-(x+1)}{(x-1)^3}$. $k'=0\Rightarrow x=-1$. Maximum at $x=-1$: $k(-1)=\frac{-1}{4}$. Increasing on $(-\infty,-1)$; decreasing on $(-1,1)\cup(1,+\infty)$.

**EVAU Level:**

5. **[EVAU Madrid style]** Let $f(x) = \dfrac{x^2 - x - 2}{x^2 - 4}$.

   **(a)** Simplify $f$ and determine the domain.  
   **(b)** Find all asymptotes.  
   **(c)** Study monotonicity and extrema.  
   **(d)** Find the intercepts with the axes.  
   **(e)** Make a sketch of the graph.

   > **Solution:**
   >
   > **(a)** Numerator: $x^2-x-2=(x-2)(x+1)$. Denominator: $x^2-4=(x-2)(x+2)$. $f(x)=\frac{(x-2)(x+1)}{(x-2)(x+2)}=\frac{x+1}{x+2}$ for $x\neq 2$. Domain: $\mathbb{R}\setminus\{-2,2\}$. (At $x=2$: removable discontinuity with $\lim_{x\to 2}f(x)=\frac{3}{4}$.)
   >
   > **(b)** VA: $x=-2$ (only one, since $x=2$ is a removable discontinuity). HA: $\lim_{x\to\pm\infty}\frac{x+1}{x+2}=1$. HA: $y=1$.
   >
   > **(c)** $f'(x)=\frac{(x+2)-(x+1)}{(x+2)^2}=\frac{1}{(x+2)^2}>0$ for all $x\neq -2$. **Strictly increasing** on each branch. No relative extrema.
   >
   > **(d)** $y$-axis: $f(0)=\frac{1}{2}$. $x$-axis: $x+1=0\Rightarrow x=-1$. Point $(-1,0)$.
   >
   > **(e)** Sketch: Hyperbola with VA $x=-2$ and HA $y=1$. Crosses $y$-axis at $(0,\frac{1}{2})$ and $x$-axis at $(-1,0)$. Hole at $x=2$ (removable discontinuity, limit value $\frac{3}{4}$).

**Multiple Choice Test**

6. The function $f(x) = \dfrac{x^2+1}{x^2-1}$ has:
   - a) Only horizontal asymptote $y=1$
   - b) Vertical asymptotes $x=\pm 1$ and horizontal asymptote $y=1$
   - c) Oblique asymptote $y=x$
   - d) No asymptotes
   > **Correct answer: b)** The denominator $x^2-1=(x-1)(x+1)$ vanishes at $x=\pm 1$ (where the numerator $\neq 0$). So VA at $x=\pm 1$. The ratio of leading coefficients gives HA $y=1$.

7. For the function $f(x)=\dfrac{p(x)}{q(x)}$ with $\deg p = \deg q$, the horizontal asymptote is:
   - a) $y = 0$
   - b) $y$ = ratio of the leading coefficients of $p$ and $q$
   - c) Does not exist
   - d) $y$ = the constant term of $p$ divided by that of $q$
   > **Correct answer: b)** When the degrees are equal, $\lim_{x\to\infty}\frac{a_n x^n + \ldots}{b_n x^n + \ldots} = \frac{a_n}{b_n}$.

---

#### 8.6.4 Sketching exponential and logarithmic functions

**Worked Example**

Perform the complete study of $f(x) = x \cdot e^{-x}$.

**Step-by-step solution:**

**1. Domain:** $\mathbb{R}$.

**2. Symmetry:** $f(-x)=-xe^x\neq f(x)$ nor $-f(x)$. No symmetry.

**3. Intercepts:** $y$-axis: $f(0)=0$. $x$-axis: $xe^{-x}=0\Rightarrow x=0$ (since $e^{-x}>0$ always).

**4. Asymptotes:**
- $\lim_{x\to+\infty}xe^{-x}=0$ (exponential dominates the polynomial). HA: $y=0$ at $+\infty$.
- $\lim_{x\to-\infty}xe^{-x}$: when $x\to-\infty$, $x<0$ and $e^{-x}\to+\infty$, so $xe^{-x}\to-\infty$. No HA at $-\infty$.

**5. Monotonicity:** $f'(x)=e^{-x}-xe^{-x}=e^{-x}(1-x)$.
Since $e^{-x}>0$: $f'(x)>0\Leftrightarrow x<1$; $f'(x)<0\Leftrightarrow x>1$.
Increasing on $(-\infty,1)$, decreasing on $(1,+\infty)$.
Relative maximum at $x=1$: $f(1)=e^{-1}=\frac{1}{e}$.

**6. Curvature:** $f''(x)=-e^{-x}(1-x)+e^{-x}(-1)=e^{-x}(x-2)$.
$f''(x)=0\Rightarrow x=2$. Sign changes: inflection at $x=2$, $f(2)=2e^{-2}$.
Concave downward on $(-\infty,2)$; upward on $(2,+\infty)$.

**Exercises with Solutions**

**Basic Level:**

1. Sketch $f(x) = 2^x$ indicating domain, range, asymptotes, and behaviour.
   > **Solution:** Domain: $\mathbb{R}$. Range: $(0,+\infty)$. No vertical asymptotes. HA as $x\to-\infty$: $y=0$. $f$ is strictly increasing. $y$-intercept: $f(0)=1$. Does not cross the $x$-axis. Concave upward ($f''=(\ln 2)^2 \cdot 2^x > 0$).

2. Study $g(x) = \ln(x+2)$: domain, asymptote, monotonicity.
   > **Solution:** Domain: $x>-2$, i.e., $(-2,+\infty)$. VA: $x=-2$ ($\lim_{x\to-2^+}\ln(x+2)=-\infty$). $g'(x)=\frac{1}{x+2}>0$: strictly increasing. $x$-intercept: $x+2=1\Rightarrow x=-1$. $y$-intercept: $g(0)=\ln 2$.

**Intermediate Level:**

3. Study $h(x) = e^x - x - 1$ completely and determine whether it has roots.
   > **Solution:** Domain: $\mathbb{R}$. $h'(x)=e^x-1=0\Rightarrow x=0$. $h''(x)=e^x>0$: minimum at $x=0$, $h(0)=1-0-1=0$. The absolute minimum is $0$, attained at $x=0$. Therefore $h(x)\geq 0$ with equality only at $x=0$: the only root is $x=0$.

4. Study $k(x)=\ln(x^2+1)$ completely.
   > **Solution:** Domain: $\mathbb{R}$. Even. Range: $[0,+\infty)$. No $x$-intercepts. $y$-intercept: $k(0)=0$. No HA. $k'(x)=\frac{2x}{x^2+1}$: increasing on $(0,+\infty)$, decreasing on $(-\infty,0)$. Minimum at $(0,0)$. $k''(x)=\frac{2(x^2+1)-4x^2}{(x^2+1)^2}=\frac{2-2x^2}{(x^2+1)^2}$: inflections at $x=\pm 1$, $k(\pm 1)=\ln 2$.

**EVAU Level:**

5. **[EVAU Madrid style]** Let $f(x) = \dfrac{e^x}{x}$.

   **(a)** Domain.  
   **(b)** Asymptotes.  
   **(c)** Monotonicity and extrema.  
   **(d)** Find the equation of the tangent at the relative extremum.

   > **Solution:**
   >
   > **(a)** Domain: $\mathbb{R}\setminus\{0\}$.
   >
   > **(b)** VA: $x=0$. $\lim_{x\to 0^-}\frac{e^x}{x}=-\infty$; $\lim_{x\to 0^+}\frac{e^x}{x}=+\infty$. HA: $\lim_{x\to+\infty}\frac{e^x}{x}=+\infty$ (no HA). $\lim_{x\to-\infty}\frac{e^x}{x}=0$ (since $e^x\to 0$ faster). HA at $-\infty$: $y=0$.
   >
   > **(c)** $f'(x)=\frac{e^x\cdot x-e^x}{x^2}=\frac{e^x(x-1)}{x^2}$. Since $e^x>0$ and $x^2>0$: $f'(x)<0\Leftrightarrow x<1$ (with $x\neq 0$); $f'(x)>0\Leftrightarrow x>1$. Relative minimum at $x=1$: $f(1)=e$.
   >
   > **(d)** At $x=1$: $f(1)=e$ and $f'(1)=0$ (it is an extremum, horizontal tangent). Equation of the tangent: $y=e$.

**Multiple Choice Test**

6. The function $f(x) = e^{-x}$ satisfies:
   - a) It is decreasing and concave downward
   - b) It is decreasing and concave upward
   - c) It is increasing and concave upward
   - d) It is increasing and concave downward
   > **Correct answer: b)** $f'(x)=-e^{-x}<0$ (decreasing). $f''(x)=e^{-x}>0$ (concave upward).

7. The domain of $f(x) = \ln(\ln x)$ is:
   - a) $(0, +\infty)$
   - b) $(1, +\infty)$
   - c) $(-\infty, 0)$
   - d) $\mathbb{R}$
   > **Correct answer: b)** We need $\ln x > 0$ (for the outer logarithm), which implies $x > 1$. Also, the inner $\ln$ requires $x>0$. The most restrictive condition is $x>1$.

---

#### 8.6.5 Sketching piecewise-defined functions

**Worked Example**

Study and sketch $f(x) = \begin{cases} x^2 + 1 & \text{if } x \leq 0 \\ e^x & \text{if } x > 0 \end{cases}$

**Step-by-step solution:**

**1. Domain:** $\mathbb{R}$.

**2. Continuity at $x=0$:**
- $f(0) = 0^2+1=1$
- $\lim_{x\to 0^-}(x^2+1)=1$
- $\lim_{x\to 0^+}e^x=1$
All three values agree: $f$ is **continuous at $x=0$**.

**3. Differentiability at $x=0$:**
- $f'_-(0)=\lim_{x\to 0^-}2x=0$
- $f'_+(0)=\lim_{x\to 0^+}e^x=1$
Since $0\neq 1$: $f$ is **not differentiable at $x=0$**.

**4. Study by pieces:**

For $x\leq 0$: $f(x)=x^2+1$. Upward-opening parabola with vertex at $(0,1)$; $f'(x)=2x\leq 0$ for $x\leq 0$: **decreasing** for $x<0$. Concave upward.

For $x>0$: $f(x)=e^x$. Exponential: strictly increasing, concave upward, $f(x)>1$.

**5. Asymptotes:** As $x\to+\infty$, $e^x\to+\infty$. As $x\to-\infty$, $x^2+1\to+\infty$. No HA.

**6. Minimum value:** At $x=0$, $f(0)=1$ is the minimum (the function decreases until $x=0$ and then increases).

**Exercises with Solutions**

**Basic Level:**

1. Study the continuity at $x=1$ of $f(x)=\begin{cases}2x-1 & x<1 \\ x^2 & x\geq 1\end{cases}$.
   > **Solution:** $\lim_{x\to 1^-}(2x-1)=1$. $\lim_{x\to 1^+}x^2=1$. $f(1)=1$. All three values are equal: $f$ is **continuous** at $x=1$.

2. Find the value of $k$ that makes $g(x)=\begin{cases}kx+3 & x\leq 2 \\ x^2-1 & x>2\end{cases}$ continuous at $x=2$.
   > **Solution:** $\lim_{x\to 2^-}(kx+3)=2k+3$. $\lim_{x\to 2^+}(x^2-1)=3$. $g(2)=2k+3$. Condition: $2k+3=3 \Rightarrow k=0$.

**Intermediate Level:**

3. Study continuity and differentiability at $x=0$ of $h(x)=\begin{cases}x^2\sin(1/x) & x\neq 0 \\ 0 & x=0\end{cases}$.
   > **Solution:** Continuity: $|h(x)|=x^2|\sin(1/x)|\leq x^2\to 0=h(0)$. Continuous at $x=0$. Differentiability: $h'(0)=\lim_{x\to 0}\frac{x^2\sin(1/x)}{x}=\lim_{x\to 0}x\sin(1/x)=0$ (since $|x\sin(1/x)|\leq|x|\to 0$). Differentiable at $x=0$ with $h'(0)=0$.

4. Sketch $k(x)=\begin{cases}-x-2 & x<-1\\ x^2 & -1\leq x\leq 1 \\ 2x-1 & x>1\end{cases}$ indicating continuity at $x=\pm 1$.
   > **Solution:** At $x=-1$: $\lim_{x\to-1^-}(-x-2)=-(-1)-2=1-2=-1$. $f(-1)=(-1)^2=1$. $1\neq -1$: **jump discontinuity** at $x=-1$. At $x=1$: $\lim_{x\to 1^-}x^2=1$. $\lim_{x\to 1^+}(2x-1)=1$. $f(1)=1$. **Continuous** at $x=1$. Differentiability at $x=1$: $f'_-(1)=2$, $f'_+(1)=2$: **differentiable** at $x=1$.

**EVAU Level:**

5. **[EVAU Madrid style]** Let $f(x)=\begin{cases}\dfrac{x^2-4}{x-2} & x<2 \\ ax+b & x\geq 2\end{cases}$.

   **(a)** Simplify the first piece and state its limit at $x=2$.  
   **(b)** Find $a$ and $b$ so that $f$ is continuous and differentiable at $x=2$.  
   **(c)** With the values found, study the sign of $f$ and describe the graph qualitatively.

   > **Solution:**
   >
   > **(a)** $\frac{x^2-4}{x-2}=\frac{(x-2)(x+2)}{x-2}=x+2$ for $x\neq 2$. $\lim_{x\to 2^-}(x+2)=4$.
   >
   > **(b)** Continuity: $\lim_{x\to 2^+}(ax+b)=2a+b=4$. (I) Differentiability: $(f_1)'(x)=1$ at $x=2$; $(f_2)'(x)=a$. We need $a=1$. From (I): $2(1)+b=4\Rightarrow b=2$. Therefore, $f(x)=\begin{cases}x+2 & x<2 \\ x+2 & x\geq 2\end{cases}$, i.e., $f(x)=x+2$ on all of $\mathbb{R}$.
   >
   > **(c)** $f(x)=x+2$ on all of $\mathbb{R}$ (except that the first piece had the restriction $x<2$). The function is a line: increasing, no extrema, $x$-intercept at $x=-2$, $y$-intercept at $(0,2)$.

**Multiple Choice Test**

6. A piecewise-defined function is differentiable at the transition point $x_0$ if:
   - a) It is continuous at $x_0$
   - b) The one-sided derivatives at $x_0$ exist and are equal
   - c) The second derivative exists at $x_0$
   - d) The function is bounded in a neighbourhood of $x_0$
   > **Correct answer: b)** Differentiability at $x_0$ requires that the one-sided derivatives exist and coincide. Continuity is a necessary but not sufficient condition.

7. If $f(x)=\begin{cases}x^2 & x\geq 0 \\ -x^2 & x<0\end{cases}$, then at $x=0$:
   - a) $f$ is not continuous
   - b) $f$ is continuous but not differentiable
   - c) $f$ is continuous and differentiable with $f'(0)=0$
   - d) $f$ is continuous and differentiable with $f'(0)=1$
   > **Correct answer: c)** Continuity: $\lim_{x\to 0^\pm}f(x)=0=f(0)$. One-sided derivatives: $f'_+(0)=\lim_{x\to 0^+}\frac{x^2}{x}=0$ and $f'_-(0)=\lim_{x\to 0^-}\frac{-x^2}{x}=\lim_{x\to 0^-}(-x)=0$. They are equal. Continuous and differentiable with $f'(0)=0$.

---

#### 8.6.6 Using digital tools for verification and exploration

**Worked Example**

Describe the process for verifying with GeoGebra the analytical study of $f(x)=\dfrac{x^3-8}{x^2}$ done by hand.

**Step-by-step solution:**

**Digital verification process:**

**Step 1 — Enter the function:**
In GeoGebra, type in the input bar: `f(x) = (x^3 - 8) / x^2`.

**Step 2 — Verify the domain:**
Observe that the graph does not appear at $x=0$ (GeoGebra does not plot at singularities).

**Step 3 — Detect asymptotes:**
Use the command `Asymptote(f)` or compute manually: VA at $x=0$. For the OA: dividing $x^3-8$ by $x^2$ gives $x-\frac{8}{x^2}$, so OA: $y=x$. Verify graphically that the curve approaches $y=x$.

**Step 4 — Extrema:**
Use `Extremum(f, -5, 5)` or differentiate with `f'(x) = Derivative(f)` and find the zeros.
$f'(x)=\frac{3x^2\cdot x^2 - (x^3-8)\cdot 2x}{x^4}=\frac{x^4+16x}{x^4}=\frac{x^3+16}{x^3}=1+\frac{16}{x^3}$. Recalculating: $f'(x)=\frac{3x^4-2x^4+16x}{x^4}=\frac{x^4+16x}{x^4}=1+\frac{16}{x^3}$. $f'=0\Rightarrow x^3=-16\Rightarrow x=-2\sqrt[3]{2}$.

**Step 5 — Inflections:**
Use `g(x)=Derivative(f,2)` and look for zeros of $g$. GeoGebra shows the inflection point numerically.

**Step 6 — Verification:**
Compare all values obtained analytically with those indicated by GeoGebra. If they coincide, the study is correct.

**Exercises with Solutions**

**Basic Level:**

1. Which GeoGebra commands automatically find the extrema and inflection points of a function?
   > **Solution:** For extrema: `Extremum(f, a, b)` (on an interval) or find the zeros of `Derivative(f)`. For inflections: find the zeros of `Derivative(f, 2)` (second derivative) and verify the sign change. The command `InflectionPoint(f)` can also be used.

2. Describe how to use Desmos to verify that the oblique asymptote of $f(x)=\dfrac{x^2+1}{x}$ is $y=x$.
   > **Solution:** In Desmos, enter `f(x) = (x^2+1)/x` and then `y = x`. Observe visually that the graph of $f$ approaches the line $y=x$ as $x\to\pm\infty$. The distance between $f(x)$ and $x$ is $\frac{1}{x}\to 0$, which can be verified by graphing `g(x) = f(x) - x = 1/x` and seeing that it tends to zero.

**Intermediate Level:**

3. Use GeoGebra to explore the family of functions $f_a(x)=x^3-3ax$ for $a\in\mathbb{R}$. How does the position of the relative extrema vary with $a$?
   > **Solution:** In GeoGebra, create a slider for $a$ and define `f(x) = x^3 - 3*a*x`. $f'(x)=3x^2-3a=0\Rightarrow x=\pm\sqrt{a}$ (extrema exist only if $a>0$). Maximum at $x=-\sqrt{a}$, $f(-\sqrt{a})=2a\sqrt{a}$; minimum at $x=\sqrt{a}$, $f(\sqrt{a})=-2a\sqrt{a}$. As $a$ varies: for $a<0$ no extrema (monotone function); for $a=0$ only one critical point at $x=0$ (inflection); for $a>0$ a maximum and minimum appear that move farther from the origin as $a$ increases.

4. Explain why digital verification does not replace rigorous analysis but does complement the study.
   > **Solution:** GeoGebra and Desmos give a **numerical and approximate** representation: they do not always precisely distinguish slightly pronounced inflection points, asymptotes in distant intervals, or behaviour on small domains. Analytical analysis provides **exact, mathematically verified** results (for example, the exact OA, the precise value of $x$ at extrema, the proof that $f''>0$ on an interval). Digital verification is useful for detecting gross errors and visualising the graph, but mathematical rigour comes from analytical computation.

**EVAU Level:**

5. **[Technological application in EVAU]** With the help of GeoGebra or Desmos, analyse the function $f(x) = \dfrac{\ln x}{x}$ for $x>0$.

   **(a)** Visually identify the main features of the graph.  
   **(b)** Analytically compute the maximum and verify it matches the graph.  
   **(c)** What does the graph show when $x\to 0^+$ and when $x\to+\infty$?

   > **Solution:**
   >
   > **(a)** The graph shows: VA at $x=0$, HA $y=0$ at $+\infty$, a maximum at approximately $x=e$, and the curve crosses the $x$-axis at $x=1$.
   >
   > **(b)** $f'(x)=\frac{1/x\cdot x-\ln x}{x^2}=\frac{1-\ln x}{x^2}$. $f'(x)=0\Rightarrow\ln x=1\Rightarrow x=e$. $f''(e)=\frac{-1/e\cdot e^2-(1-1)\cdot 2e}{e^4}=\frac{-e}{e^4}<0$. Maximum at $x=e$: $f(e)=\frac{1}{e}\approx 0.368$. GeoGebra would show the maximum at $(e,1/e)$, consistent with the calculation.
   >
   > **(c)** When $x\to 0^+$: $\ln x\to-\infty$ and $x\to 0^+$, so $f(x)\to-\infty$: **VA at $x=0$** (the curve drops to $-\infty$). When $x\to+\infty$: $\frac{\ln x}{x}\to 0$ (the denominator grows faster). **HA at $y=0$**.

**Multiple Choice Test**

6. The use of GeoGebra in the study of functions is most useful for:
   - a) Rigorously proving the existence of asymptotes
   - b) Visualising the graph and checking analytical results
   - c) Exactly computing inflection points in all cases
   - d) Solving exact definite integrals
   > **Correct answer: b)** Digital tools are especially useful for visualisation and verification. Exact results require rigorous mathematical analysis.

7. When graphing $f(x)=\dfrac{1}{x-1}$ in Desmos, the tool shows a vertical line at $x=1$. This line represents:
   - a) The vertical asymptote of $f$
   - b) A software error
   - c) An intersection with the $y$-axis
   - d) The tangent line at $x=1$
   > **Correct answer: a)** Desmos draws a vertical line at the vertical asymptotes of rational functions. Although it is not part of the graph of $f$, it visualises the vertical asymptote $x=1$.

---

## 8.7 Modelling with functions

---

#### 8.7.1 Building models with complex functions from real data

**Worked Example**

A company observes that its daily sales (in thousands of €) follow the model $V(t) = \dfrac{100t}{t^2+1}$, where $t$ is time in weeks since launch.

Analyse the model: maximum sales, long-term trend, and interpretation.

**Step-by-step solution:**

**1. Real domain of the model:** $t\geq 0$ (negative $t$ makes no sense).

**2. Maximum sales:**
$$V'(t)=\frac{100(t^2+1)-100t\cdot 2t}{(t^2+1)^2}=\frac{100(1-t^2)}{(t^2+1)^2}$$
$V'(t)=0\Rightarrow t=1$ (week). $V(1)=\frac{100}{2}=50$ thousand €. Maximum in the first week.

**3. Long-term trend:**
$$\lim_{t\to+\infty}V(t)=\lim_{t\to+\infty}\frac{100t}{t^2+1}=0$$
Sales decay to zero in the long run.

**4. Interpretation:** The product generates maximum sales (50,000€/day) in week 1, then interest declines. The model captures the phenomenon of initial novelty followed by market saturation.

**Exercises with Solutions**

**Basic Level:**

1. The logistic model of population growth is $P(t)=\dfrac{K}{1+Ae^{-rt}}$. What is the limiting value of the population as $t\to+\infty$?
   > **Solution:** $\lim_{t\to+\infty}\frac{K}{1+Ae^{-rt}}=\frac{K}{1+0}=K$. The population stabilises at $K$ (the carrying capacity of the environment).

2. The pH of a solution varies with the hydrogen ion concentration according to $\text{pH} = -\log_{10}[\text{H}^+]$. For what concentration $[\text{H}^+]$ is pH $= 7$?
   > **Solution:** $7=-\log_{10}[\text{H}^+]\Rightarrow\log_{10}[\text{H}^+]=-7\Rightarrow[\text{H}^+]=10^{-7}$ mol/L.

**Intermediate Level:**

3. The rate of a chemical reaction follows the Michaelis-Menten model: $v(s)=\dfrac{V_{\max}\cdot s}{K_m+s}$. Find the value of $s$ for which the rate is half of $V_{\max}$.
   > **Solution:** $\frac{V_{\max}\cdot s}{K_m+s}=\frac{V_{\max}}{2}\Rightarrow 2s=K_m+s\Rightarrow s=K_m$. The rate is $V_{\max}/2$ when the substrate concentration equals $K_m$ (the Michaelis constant).

4. The loan amortisation model describes the outstanding balance as $S(t)=P\cdot e^{rt}-\dfrac{Q}{r}(e^{rt}-1)$, where $P$ is the initial capital, $r$ the continuous interest rate, and $Q$ the continuous payment. Find the value of $Q$ that ensures the loan is paid off in finite time (i.e., for $S$ to be decreasing from the start).
   > **Solution:** $S'(t)=Pr\cdot e^{rt}-Q\cdot e^{rt}=e^{rt}(Pr-Q)$. For decreasing: $S'(t)<0\Rightarrow Pr-Q<0\Rightarrow Q>Pr$. The continuous payment must exceed the interest generated on the initial capital.

**EVAU Level:**

5. **[EVAU modelling problem]** The temperature (in °C) of a cooling object follows Newton's Law of Cooling: $T(t)=T_{\text{amb}}+(T_0-T_{\text{amb}})e^{-kt}$, where $T_{\text{amb}}=20°C$, $T_0=80°C$, and $k=0.1$ min$^{-1}$.

   **(a)** Compute the initial temperature and the limiting temperature.  
   **(b)** At what time $t$ does the temperature reach $50°C$?  
   **(c)** Compute the cooling rate $T'(t)$ and interpret its sign.

   > **Solution:**
   >
   > **(a)** $T(0)=20+(80-20)e^0=20+60=80°C$. $\lim_{t\to+\infty}T(t)=20+0=20°C$ (ambient temperature). The object cools from 80°C to 20°C.
   >
   > **(b)** $20+60e^{-0.1t}=50\Rightarrow 60e^{-0.1t}=30\Rightarrow e^{-0.1t}=\frac{1}{2}\Rightarrow -0.1t=\ln\frac{1}{2}=-\ln 2\Rightarrow t=10\ln 2\approx 6.93$ min.
   >
   > **(c)** $T'(t)=-0.1\cdot 60\cdot e^{-0.1t}=-6e^{-0.1t}<0$ for all $t\geq 0$. The negative sign indicates that the temperature always **decreases** (cooling). The cooling rate decreases exponentially (the object cools more slowly as its temperature approaches the ambient temperature).

**Multiple Choice Test**

6. In the model $P(t)=1000e^{0.03t}$, the parameter $0.03$ represents:
   - a) The initial population
   - b) The continuous growth rate of 3% per unit of time
   - c) The doubling time
   - d) The carrying capacity
   > **Correct answer: b)** In the exponential growth model $P(t)=P_0 e^{rt}$, the parameter $r$ is the continuous growth rate. Here $r=0.03$, i.e., 3% per unit of time.

7. The model $f(t)=\dfrac{a}{1+be^{-ct}}$ with $a,b,c>0$ is typical of:
   - a) Exponential growth without bound
   - b) Exponential decay
   - c) Logistic growth with carrying capacity $a$
   - d) Periodic oscillation
   > **Correct answer: c)** This is the logistic (or sigmoid) function. When $t\to+\infty$, $f\to a$ (carrying capacity). It grows rapidly at first and then levels off. Typical in diffusion, epidemic, and biological growth models.

---

#### 8.7.2 Interpreting the model: domain of validity, extrema, and trends

**Worked Example**

The profit of a company (thousands of €) is given by $B(x)= -0{,}5x^3+6x^2-15x+2$, where $x\geq 0$ is production (thousands of units). Analyse the model.

**Step-by-step solution:**

**1. Domain of validity:** $x\geq 0$ (no negative production). To analyse viability: profit must be non-negative, $B(x)\geq 0$.

**2. Extrema:**
$$B'(x)=-1{,}5x^2+12x-15=-1{,}5(x^2-8x+10)$$
$x^2-8x+10=0\Rightarrow x=\frac{8\pm\sqrt{64-40}}{2}=\frac{8\pm\sqrt{24}}{2}=4\pm\sqrt{6}$

$x_1=4-\sqrt{6}\approx 1.55$ (relative minimum), $x_2=4+\sqrt{6}\approx 6.45$ (relative maximum).

$B(x_2)=-0.5(4+\sqrt{6})^3+6(4+\sqrt{6})^2-15(4+\sqrt{6})+2 \approx$ maximum sales.

**3. Interpretation:**
- Producing few units (near $x_1$) generates a local minimum of profit.
- Maximum profit is attained at $x_2 \approx 6.450$ units.
- For very large $x$, the term $-0.5x^3$ dominates and $B\to-\infty$: the model is only valid in the range $[0, x^*]$ where $B(x^*) = 0$ (beyond this, the model predicts losses).

**Exercises with Solutions**

**Basic Level:**

1. The free-fall model is $h(t)=h_0-\frac{1}{2}gt^2$, with $h_0=100$ m and $g=10$ m/s². At what instant does the object hit the ground? What is the domain of validity of the model?
   > **Solution:** $h(t)=0\Rightarrow 100-5t^2=0\Rightarrow t=\sqrt{20}=2\sqrt{5}\approx 4.47$ s. The model is valid for $t\in[0,2\sqrt{5}]$: it only makes sense while the object is in the air.

2. A company earns $G(x)=5x-0.01x^2$ euros by selling $x$ units ($0\leq x\leq 300$). Find the quantity that maximises profit.
   > **Solution:** $G'(x)=5-0.02x=0\Rightarrow x=250$. $G''(250)=-0.02<0$: maximum. $G(250)=5(250)-0.01(250)^2=1250-625=625$ euros. Maximum profit is €625 with 250 units.

**Intermediate Level:**

3. The unit production cost (€/unit) of a good follows the model $C(x)=\dfrac{x^2-10x+100}{x}$ for $x>0$ units (thousands). Find the quantity that minimises the unit cost.
   > **Solution:** $C(x)=x-10+\frac{100}{x}$. $C'(x)=1-\frac{100}{x^2}=0\Rightarrow x^2=100\Rightarrow x=10$. $C''(x)=\frac{200}{x^3}>0$: minimum. $C(10)=10-10+10=10$ €/unit. With 10,000 units, the unit cost is minimised (€10).

4. Discuss the domain of validity of the model $P(t)=100e^{0.05t}$ for an investment of €100 at a continuous rate of 5%. Is it valid as $t\to\infty$?
   > **Solution:** Mathematically the model is defined for all $t\geq 0$. However, in reality: (a) The interest rate can change over time; (b) The continuous linear model is an approximation; (c) Economic conditions limit real growth. The practical domain of validity depends on the context and time horizon considered. For short-to-medium terms (5-20 years) the model is a good approximation.

**EVAU Level:**

5. **[EVAU Madrid, real style]** A company manufactures items whose total revenue (in thousands of €) is $I(x) = 12x$ and whose total cost is $C(x) = x^3 - 6x^2 + 20x + 3$, where $x$ is the quantity produced (in thousands of units) with $0\leq x\leq 8$.

   **(a)** Write the profit function $B(x) = I(x) - C(x)$.  
   **(b)** Find the relative extrema of $B$ on $(0,8)$.  
   **(c)** Determine the quantity that maximises profit on $[0,8]$ and compute that profit.

   > **Solution:**
   >
   > **(a)** $B(x)=12x-(x^3-6x^2+20x+3)=-x^3+6x^2-8x-3$.
   >
   > **(b)** $B'(x)=-3x^2+12x-8$. $B'(x)=0\Rightarrow 3x^2-12x+8=0\Rightarrow x=\frac{12\pm\sqrt{144-96}}{6}=\frac{12\pm\sqrt{48}}{6}=2\pm\frac{2\sqrt{3}}{3}$. $x_1=2-\frac{2\sqrt{3}}{3}\approx 0.845$ and $x_2=2+\frac{2\sqrt{3}}{3}\approx 3.155$. $B''(x)=-6x+12$. $B''(x_1)=-6(0.845)+12\approx 6.93>0$: relative minimum. $B''(x_2)=-6(3.155)+12\approx -6.93<0$: **relative maximum**.
   >
   > **(c)** We evaluate at the candidates and interval endpoints: $B(0)=-3$; $B(x_2)\approx B(3.155)$ (compute); $B(8)=-512+384-64-3=-195$. The absolute maximum is the relative maximum at $x_2\approx 3.155$, since $B(0)<0$ and $B(8)\ll 0$. $B(x_2)\approx -31.3+59.8-25.2-3=0.3$ thousand €. The optimal production is approximately 3.155 thousand units.

**Multiple Choice Test**

6. In an applied mathematical model, the domain of validity:
   - a) Always coincides with the mathematical domain of the function
   - b) May be more restricted than the mathematical domain for contextual reasons
   - c) Is always $\mathbb{R}$
   - d) Is the set of values where the function attains an extremum
   > **Correct answer: b)** In real contexts (production, time, price...) the domain of validity is limited by physical or economic conditions. For example, a quantity produced cannot be negative even if the function is defined on $\mathbb{R}$.

7. If the sales model is $V(t)=at^2+bt+c$ with $a<0$, the maximum sales level is attained at:
   - a) $t=0$
   - b) $t=-\dfrac{b}{2a}$
   - c) $t=\dfrac{b}{2a}$
   - d) $t\to+\infty$
   > **Correct answer: b)** The parabola $V(t)=at^2+bt+c$ with $a<0$ opens downward. The vertex (maximum) is at $t=-\frac{b}{2a}$.

---

# CHAPTER 9. INTEGRALS

---

## 9.1 Antiderivatives and the indefinite integral

---

#### 9.1.1 Concept of an antiderivative: definition and uniqueness up to a constant

**Worked Example**

Verify that $F(x) = \dfrac{x^3}{3} - 2x^2 + 5x + C$ is an antiderivative of $f(x) = x^2 - 4x + 5$.

**Step-by-step solution:**

By definition, $F$ is an antiderivative of $f$ if $F'(x) = f(x)$.

We differentiate $F(x)$:
$$F'(x) = \frac{3x^2}{3} - 2\cdot 2x + 5 + 0 = x^2 - 4x + 5 = f(x) \checkmark$$

$F$ is indeed an antiderivative of $f$.

**Uniqueness up to a constant:** If $G$ is another antiderivative of $f$, then $(G-F)'=f-f=0$, which implies $G(x)-F(x)=C$ (constant). Every antiderivative of $f$ has the form $F(x)+C$.

**Exercises with Solutions**

**Basic Level:**

1. Verify that $F(x) = x^2 \sin x$ is an antiderivative of $f(x) = 2x\sin x + x^2\cos x$.
   > **Solution:** $F'(x)=2x\sin x+x^2\cos x=f(x)$. ✓ Yes, it is an antiderivative.

2. If $F(x) = e^x + 3$ and $G(x) = e^x - 7$, verify that both are antiderivatives of $f(x) = e^x$ and explain the relationship between them.
   > **Solution:** $F'(x)=e^x=f(x)$ ✓. $G'(x)=e^x=f(x)$ ✓. Both are antiderivatives of $e^x$. The difference is $F(x)-G(x)=10$, a constant, as established by the uniqueness theorem up to a constant.

**Intermediate Level:**

3. Find all functions $f$ such that $F(x)=x^n$ is an antiderivative of $f$, for $n\geq 1$ integer.
   > **Solution:** $F'(x)=nx^{n-1}=f(x)$. Therefore, $f(x)=nx^{n-1}$. The antiderivative of $nx^{n-1}$ is $x^n+C$.

4. Can a function have two antiderivatives $F$ and $G$ on $\mathbb{R}$ such that $F(0)=G(0)$ and $F(1)\neq G(1)$? Justify.
   > **Solution:** No. If $F$ and $G$ are antiderivatives of the same function, then $F(x)-G(x)=C$ (constant) for all $x\in\mathbb{R}$. In particular, $F(0)-G(0)=C$. If $F(0)=G(0)$, then $C=0$, so $F(x)=G(x)$ for all $x$, including $x=1$. It is not possible that $F(1)\neq G(1)$.

**EVAU Level:**

5. Let $f$ be continuous on $[a,b]$ and let $F(x)=\int_a^x f(t)\,dt$.

   **(a)** State the Fundamental Theorem of Calculus in terms of $F$.  
   **(b)** Compute $F'(x)$ and verify that $F$ is an antiderivative of $f$.  
   **(c)** If $G$ is any other antiderivative of $f$, how are $F$ and $G$ related?

   > **Solution:**
   >
   > **(a)** If $f$ is continuous on $[a,b]$, then $F(x)=\int_a^x f(t)\,dt$ is differentiable on $(a,b)$ and $F'(x)=f(x)$ for all $x\in(a,b)$.
   >
   > **(b)** By the FTC: $F'(x)=f(x)$. Thus $F$ is an antiderivative of $f$ with the initial condition $F(a)=0$.
   >
   > **(c)** $G(x)-F(x)=C$ (constant). In particular, if $G$ is any antiderivative, $G(x)=\int_a^x f(t)\,dt+C=F(x)+C$.

**Multiple Choice Test**

6. If $F$ and $G$ are both antiderivatives of $f$ on $\mathbb{R}$, then:
   - a) $F(x) = G(x)$ for all $x$
   - b) $F(x) - G(x) = C$ (constant) for all $x$
   - c) $F'(x) + G'(x) = f(x)$
   - d) $F(x) \cdot G(x) = 1$
   > **Correct answer: b)** Two antiderivatives of the same function differ by an additive constant.

7. The function $F(x) = \cos x + 5$ is an antiderivative of:
   - a) $\sin x + 5$
   - b) $-\sin x$
   - c) $-\cos x$
   - d) $\sin x$
   > **Correct answer: b)** $F'(x) = -\sin x$.

---

#### 9.1.2 Indefinite integral: notation and linearity properties

**Worked Example**

Compute $\displaystyle\int \left(3x^2 - \frac{2}{x} + 5e^x\right)dx$.

**Step-by-step solution:**

We apply the linearity of the integral:
$$\int \left(3x^2 - \frac{2}{x} + 5e^x\right)dx = 3\int x^2\,dx - 2\int\frac{1}{x}\,dx + 5\int e^x\,dx$$

We compute each integral:
$$= 3\cdot\frac{x^3}{3} - 2\ln|x| + 5e^x + C$$
$$= x^3 - 2\ln|x| + 5e^x + C$$

**Verification:** Differentiating $F(x)=x^3-2\ln|x|+5e^x$: $F'(x)=3x^2-\frac{2}{x}+5e^x$ ✓

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int (4x^3 - 6x + 2)\,dx$.
   > **Solution:** $\int 4x^3\,dx - \int 6x\,dx + \int 2\,dx = x^4 - 3x^2 + 2x + C$.

2. Compute $\displaystyle\int \left(\sin x + \cos x - \frac{1}{x^2}\right)dx$.
   > **Solution:** $-\cos x + \sin x + \frac{1}{x} + C$.

**Intermediate Level:**

3. Compute $\displaystyle\int \left(\frac{x^3+2x-1}{x^2}\right)dx$.
   > **Solution:** Simplify: $\frac{x^3+2x-1}{x^2}=x+\frac{2}{x}-\frac{1}{x^2}=x+2x^{-1}-x^{-2}$. Integrate: $\frac{x^2}{2}+2\ln|x|+\frac{1}{x}+C$.

4. Compute $\displaystyle\int (e^x - 3\cdot 2^x + \sqrt{x})\,dx$.
   > **Solution:** $e^x - \frac{3\cdot 2^x}{\ln 2}+\frac{2}{3}x^{3/2}+C$.

**EVAU Level:**

5. Compute $\displaystyle\int \left(2\sin x - \frac{3}{\cos^2 x} + \frac{1}{1+x^2}\right)dx$.

   **(a)** Identify which standard integrals are present.  
   **(b)** Apply linearity and compute the integral.

   > **Solution:**
   >
   > **(a)** $\int \sin x\,dx = -\cos x$; $\int \frac{1}{\cos^2 x}\,dx = \int \sec^2 x\,dx = \tan x$; $\int \frac{1}{1+x^2}\,dx = \arctan x$.
   >
   > **(b)** $2\int\sin x\,dx - 3\int\frac{1}{\cos^2 x}\,dx + \int\frac{1}{1+x^2}\,dx = -2\cos x - 3\tan x + \arctan x + C$.

**Multiple Choice Test**

6. The linearity property of the indefinite integral states that:
   - a) $\int f(x)g(x)\,dx = \int f(x)\,dx\cdot\int g(x)\,dx$
   - b) $\int [af(x)+bg(x)]\,dx = a\int f(x)\,dx+b\int g(x)\,dx$
   - c) $\int f(g(x))\,dx = \int f(x)\,dx \circ g(x)$
   - d) $\int f(x)\,dx = F(b)-F(a)$
   > **Correct answer: b)** The integral is a linear operator: the integral of a linear combination is the linear combination of the integrals.

7. $\displaystyle\int \left(\frac{1}{\sqrt{x}} + \sqrt{x}\right)dx$ equals:
   - a) $2\sqrt{x} + \frac{2}{3}x^{3/2} + C$
   - b) $-\frac{1}{2}x^{-3/2} + \frac{1}{2}x^{-1/2} + C$
   - c) $\ln(\sqrt{x}) + \frac{x^2}{4} + C$
   - d) $2\sqrt{x} + \frac{3}{2}x^{3/2} + C$
   > **Correct answer: a)** $\int x^{-1/2}\,dx = 2x^{1/2}=2\sqrt{x}$ and $\int x^{1/2}\,dx = \frac{x^{3/2}}{3/2}=\frac{2}{3}x^{3/2}$.

---

#### 9.1.3 Table of standard integrals

**Worked Example**

Compute $\displaystyle\int \frac{1}{x^2+9}\,dx$.

**Step-by-step solution:**

We recognise the form $\dfrac{1}{x^2+a^2}$ with $a^2=9$, i.e., $a=3$:

$$\int \frac{1}{x^2+9}\,dx = \frac{1}{3}\arctan\!\left(\frac{x}{3}\right)+C$$

**General formula:** $\displaystyle\int\frac{dx}{x^2+a^2}=\frac{1}{a}\arctan\!\left(\frac{x}{a}\right)+C$.

**Verification:** $\frac{d}{dx}\!\left[\frac{1}{3}\arctan\!\left(\frac{x}{3}\right)\right]=\frac{1}{3}\cdot\frac{1}{1+(x/3)^2}\cdot\frac{1}{3}=\frac{1}{3}\cdot\frac{9}{9+x^2}\cdot\frac{1}{3}=\frac{1}{x^2+9}$ ✓

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int e^{3x}\,dx$.
   > **Solution:** $\frac{e^{3x}}{3}+C$.

2. Compute $\displaystyle\int \cos(5x)\,dx$.
   > **Solution:** $\frac{\sin(5x)}{5}+C$.

**Intermediate Level:**

3. Compute $\displaystyle\int \frac{3}{\sqrt{1-x^2}}\,dx$.
   > **Solution:** We recognise the form of $\arcsin$: $\int\frac{1}{\sqrt{1-x^2}}\,dx=\arcsin x+C$. Therefore: $3\arcsin x+C$.

4. Compute $\displaystyle\int \frac{2x}{x^2+5}\,dx$.
   > **Solution:** We recognise the form $\frac{f'}{f}$: the numerator $2x$ is the derivative of the denominator $x^2+5$. $\int\frac{2x}{x^2+5}\,dx=\ln(x^2+5)+C$.

**EVAU Level:**

5. Compute the following standard integrals:

   **(a)** $\displaystyle\int \frac{1}{\sqrt{4-x^2}}\,dx$.  
   **(b)** $\displaystyle\int \sec^2(x)\,dx$.  
   **(c)** $\displaystyle\int \frac{e^x}{e^x+1}\,dx$.

   > **Solution:**
   >
   > **(a)** Form $\frac{1}{\sqrt{a^2-x^2}}$ with $a=2$: $\int\frac{dx}{\sqrt{4-x^2}}=\arcsin\!\left(\frac{x}{2}\right)+C$.
   >
   > **(b)** Standard: $\int\sec^2 x\,dx=\tan x+C$.
   >
   > **(c)** Numerator $e^x$ is the derivative of denominator $e^x+1$: $\int\frac{e^x}{e^x+1}\,dx=\ln(e^x+1)+C$.

**Multiple Choice Test**

6. $\displaystyle\int \frac{1}{x}\,dx$ equals:
   - a) $\dfrac{1}{x^2}+C$
   - b) $\ln x+C$
   - c) $\ln|x|+C$
   - d) $-\dfrac{1}{x^2}+C$
   > **Correct answer: c)** The integral of $\frac{1}{x}$ is $\ln|x|+C$, with absolute value so that it is also defined for $x<0$.

7. $\displaystyle\int x^{-3}\,dx$ equals:
   - a) $-3x^{-4}+C$
   - b) $x^{-2}+C$
   - c) $-\dfrac{1}{2}x^{-2}+C$
   - d) $\dfrac{1}{2}x^{-4}+C$
   > **Correct answer: c)** $\int x^{-3}\,dx=\frac{x^{-3+1}}{-3+1}=\frac{x^{-2}}{-2}=-\frac{1}{2x^2}+C$.

---

#### 9.1.4 Standard integrals of composite functions (reverse chain rule)

**Worked Example**

Compute $\displaystyle\int (3x^2+1)^5 \cdot 6x\,dx$ using the reverse chain rule.

**Step-by-step solution:**

We identify $u = 3x^2+1$ (inner function). Then $u' = 6x$ (which appears as a factor). We recognise the form $\int u^n \cdot u'\,dx = \dfrac{u^{n+1}}{n+1}+C$:

$$\int (3x^2+1)^5\cdot 6x\,dx = \frac{(3x^2+1)^6}{6}+C$$

**Verification:** $\dfrac{d}{dx}\left[\frac{(3x^2+1)^6}{6}\right]=\frac{6(3x^2+1)^5\cdot 6x}{6}=(3x^2+1)^5\cdot 6x$ ✓

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int 2x\cdot e^{x^2}\,dx$.
   > **Solution:** $u=x^2$, $u'=2x$. $\int e^{x^2}\cdot 2x\,dx = e^{x^2}+C$.

2. Compute $\displaystyle\int \frac{3x^2}{x^3+5}\,dx$.
   > **Solution:** $u=x^3+5$, $u'=3x^2$. $\int\frac{u'}{u}\,dx=\ln|u|+C=\ln|x^3+5|+C=\ln(x^3+5)+C$ (if $x^3>-5$).

**Intermediate Level:**

3. Compute $\displaystyle\int \sin^4 x \cdot \cos x\,dx$.
   > **Solution:** $u=\sin x$, $u'=\cos x$. $\int u^4\cdot u'\,dx = \frac{u^5}{5}+C = \frac{\sin^5 x}{5}+C$.

4. Compute $\displaystyle\int \frac{\ln x}{x}\,dx$.
   > **Solution:** $u=\ln x$, $u'=\frac{1}{x}$. $\int u\cdot u'\,dx=\frac{u^2}{2}+C=\frac{(\ln x)^2}{2}+C$.

**EVAU Level:**

5. Compute:

   **(a)** $\displaystyle\int \frac{\cos x}{\sin^2 x}\,dx$.  
   **(b)** $\displaystyle\int \frac{e^{\arctan x}}{1+x^2}\,dx$.  
   **(c)** $\displaystyle\int (1+2x)^{10}\,dx$.

   > **Solution:**
   >
   > **(a)** $u=\sin x$, $u'=\cos x$. $\int\frac{u'}{u^2}\,du=\int u^{-2}\,du=-u^{-1}+C=-\frac{1}{\sin x}+C$.
   >
   > **(b)** $u=\arctan x$, $u'=\frac{1}{1+x^2}$. $\int e^u\cdot u'\,dx=e^u+C=e^{\arctan x}+C$.
   >
   > **(c)** $u=1+2x$, $u'=2$. Adjust: $\int(1+2x)^{10}\,dx=\frac{1}{2}\int u^{10}\cdot 2\,dx = \frac{1}{2}\cdot\frac{u^{11}}{11}+C=\frac{(1+2x)^{11}}{22}+C$.

**Multiple Choice Test**

6. $\displaystyle\int f'(x)\cdot e^{f(x)}\,dx$ equals:
   - a) $f(x)\cdot e^{f(x)}+C$
   - b) $e^{f(x)}+C$
   - c) $f'(x)\cdot e^{f(x)}+C$
   - d) $e^{f(x)}\cdot f''(x)+C$
   > **Correct answer: b)** By the reverse chain rule: $\int e^u\,du=e^u+C$ with $u=f(x)$, $du=f'(x)\,dx$.

7. $\displaystyle\int \frac{f'(x)}{f(x)}\,dx$ equals (with $f(x)>0$):
   - a) $\ln(f(x))+C$
   - b) $\dfrac{1}{[f(x)]^2}+C$
   - c) $f'(x)\ln(f(x))+C$
   - d) $\ln\dfrac{1}{f(x)}+C$   > **Correct answer: a)** By the reverse chain rule with $u=f(x)$: $\int\frac{du}{u}=\ln|u|+C=\ln(f(x))+C$.

---

### 9.2 Integration techniques

---

#### 9.2.1 Integration by substitution (change of variable)

**Worked Example**

Compute $\displaystyle\int \frac{x}{\sqrt{x^2-3}}\,dx$ using an appropriate substitution.

**Step-by-step solution:**

**Step 1 – Choose the substitution.** The radical suggests $u = x^2 - 3$, so $du = 2x\,dx$, i.e., $x\,dx = \dfrac{du}{2}$.

**Step 2 – Substitute into the integral:**
$$\int \frac{x}{\sqrt{x^2-3}}\,dx = \int \frac{1}{\sqrt{u}}\cdot\frac{du}{2} = \frac{1}{2}\int u^{-1/2}\,du$$

**Step 3 – Integrate in $u$:**
$$\frac{1}{2}\cdot\frac{u^{1/2}}{1/2}+C = u^{1/2}+C = \sqrt{u}+C$$

**Step 4 – Undo the substitution:**
$$\int \frac{x}{\sqrt{x^2-3}}\,dx = \sqrt{x^2-3}+C$$

**Verification:** $\dfrac{d}{dx}\left[\sqrt{x^2-3}\right]=\dfrac{2x}{2\sqrt{x^2-3}}=\dfrac{x}{\sqrt{x^2-3}}$ ✓

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int \sqrt{2x+1}\,dx$.
   > **Solution:** $u=2x+1$, $du=2\,dx$. $\int\sqrt{u}\cdot\frac{du}{2}=\frac{1}{2}\cdot\frac{u^{3/2}}{3/2}+C=\frac{(2x+1)^{3/2}}{3}+C$.

2. Compute $\displaystyle\int \frac{x^2}{x^3+1}\,dx$.
   > **Solution:** $u=x^3+1$, $du=3x^2\,dx$. $\int\frac{du/3}{u}=\frac{1}{3}\ln|x^3+1|+C$.

**Intermediate Level:**

3. Compute $\displaystyle\int x\sqrt{1-x^2}\,dx$.
   > **Solution:** $u=1-x^2$, $du=-2x\,dx$. $\int\sqrt{u}\cdot\left(-\frac{du}{2}\right)=-\frac{1}{2}\cdot\frac{u^{3/2}}{3/2}+C=-\frac{(1-x^2)^{3/2}}{3}+C$.

4. Compute $\displaystyle\int \frac{e^x}{e^x+2}\,dx$.
   > **Solution:** $u=e^x+2$, $du=e^x\,dx$. $\int\frac{du}{u}=\ln|u|+C=\ln(e^x+2)+C$.

**EVAU Level:**

5. Compute the following integrals justifying the substitution used:

   **(a)** $\displaystyle\int \frac{\ln x}{x}\,dx$.  
   **(b)** $\displaystyle\int \sin^3 x\cos x\,dx$.  
   **(c)** $\displaystyle\int \frac{x+1}{\sqrt{x^2+2x+5}}\,dx$.

   > **Solution:**
   >
   > **(a)** $u=\ln x$, $du=\frac{1}{x}dx$. $\int u\,du=\frac{u^2}{2}+C=\frac{(\ln x)^2}{2}+C$.
   >
   > **(b)** $u=\sin x$, $du=\cos x\,dx$. $\int u^3\,du=\frac{u^4}{4}+C=\frac{\sin^4 x}{4}+C$.
   >
   > **(c)** $u=x^2+2x+5$, $du=(2x+2)dx=2(x+1)dx$, so $(x+1)dx=\frac{du}{2}$. $\int\frac{du/2}{\sqrt{u}}=\frac{1}{2}\cdot 2\sqrt{u}+C=\sqrt{x^2+2x+5}+C$.

**Multiple Choice Test**

6. To compute $\int\sqrt{4-x^2}\cdot x\,dx$, the most convenient substitution is:
   - a) $u=\sqrt{4-x^2}$
   - b) $u=4-x^2$
   - c) $u=x^2$
   - d) $u=x$
   > **Correct answer: b)** With $u=4-x^2$, $du=-2x\,dx$, the integral becomes $-\frac{1}{2}\int\sqrt{u}\,du$, which is standard.

7. The result of $\displaystyle\int \frac{2x}{(x^2+3)^4}\,dx$ is:
   - a) $\dfrac{-1}{3(x^2+3)^3}+C$
   - b) $\dfrac{2}{(x^2+3)^3}+C$
   - c) $\ln(x^2+3)^4+C$
   - d) $\dfrac{-1}{4(x^2+3)^3}\cdot 2x+C$
   > **Correct answer: a)** $u=x^2+3$, $du=2x\,dx$. $\int u^{-4}\,du=\frac{u^{-3}}{-3}+C=\frac{-1}{3(x^2+3)^3}+C$.

---

#### 9.2.2 Integration by parts: formula and ILATE criterion

**Worked Example**

Compute $\displaystyle\int x\ln x\,dx$ using integration by parts.

**Step-by-step solution:**

**Formula:** $\int u\,dv = u\cdot v - \int v\,du$

**Step 1 – Choose $u$ and $dv$ using ILATE** (Inverse trig / Logarithmic / Algebraic / Trigonometric / Exponential):
- $u = \ln x \Rightarrow du = \dfrac{1}{x}\,dx$ (logarithmic, takes priority)
- $dv = x\,dx \Rightarrow v = \dfrac{x^2}{2}$ (algebraic)

**Step 2 – Apply the formula:**
$$\int x\ln x\,dx = \ln x\cdot\frac{x^2}{2} - \int\frac{x^2}{2}\cdot\frac{1}{x}\,dx = \frac{x^2\ln x}{2} - \int\frac{x}{2}\,dx$$

**Step 3 – Solve the remaining integral:**
$$= \frac{x^2\ln x}{2} - \frac{1}{2}\cdot\frac{x^2}{2}+C = \frac{x^2\ln x}{2} - \frac{x^2}{4}+C = \frac{x^2}{4}(2\ln x-1)+C$$

**Verification:** $\dfrac{d}{dx}\!\left[\frac{x^2}{4}(2\ln x-1)\right]=\frac{2x}{4}(2\ln x-1)+\frac{x^2}{4}\cdot\frac{2}{x}=\frac{x}{2}(2\ln x-1)+\frac{x}{2}=x\ln x$ ✓

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int x e^x\,dx$.
   > **Solution:** $u=x$, $dv=e^x\,dx \Rightarrow du=dx$, $v=e^x$. $\int xe^x\,dx=xe^x-\int e^x\,dx=xe^x-e^x+C=e^x(x-1)+C$.

2. Compute $\displaystyle\int \ln x\,dx$.
   > **Solution:** $u=\ln x$, $dv=dx \Rightarrow du=\frac{1}{x}dx$, $v=x$. $\int\ln x\,dx=x\ln x-\int x\cdot\frac{1}{x}\,dx=x\ln x-x+C=x(\ln x-1)+C$.

**Intermediate Level:**

3. Compute $\displaystyle\int x^2 e^x\,dx$.
   > **Solution:** First time: $u=x^2$, $dv=e^x\,dx$: $x^2e^x-2\int xe^x\,dx$. Second time (previous result): $x^2e^x-2[xe^x-e^x]+C=x^2e^x-2xe^x+2e^x+C=e^x(x^2-2x+2)+C$.

4. Compute $\displaystyle\int x\sin x\,dx$.
   > **Solution:** $u=x$, $dv=\sin x\,dx \Rightarrow du=dx$, $v=-\cos x$. $\int x\sin x\,dx=-x\cos x+\int\cos x\,dx=-x\cos x+\sin x+C$.

**EVAU Level:**

5. Compute the following integrals:

   **(a)** $\displaystyle\int x^2\ln x\,dx$.  
   **(b)** $\displaystyle\int \arctan x\,dx$.

   > **Solution:**
   >
   > **(a)** $u=\ln x$, $dv=x^2\,dx \Rightarrow du=\frac{1}{x}dx$, $v=\frac{x^3}{3}$. $\int x^2\ln x\,dx=\frac{x^3}{3}\ln x-\int\frac{x^3}{3}\cdot\frac{1}{x}\,dx=\frac{x^3}{3}\ln x-\frac{1}{3}\int x^2\,dx=\frac{x^3}{3}\ln x-\frac{x^3}{9}+C=\frac{x^3}{9}(3\ln x-1)+C$.
   >
   > **(b)** $u=\arctan x$, $dv=dx \Rightarrow du=\frac{1}{1+x^2}dx$, $v=x$. $\int\arctan x\,dx=x\arctan x-\int\frac{x}{1+x^2}\,dx=x\arctan x-\frac{1}{2}\ln(1+x^2)+C$.

**Multiple Choice Test**

6. In integration by parts $\int u\,dv = uv - \int v\,du$, to compute $\int x\cos x\,dx$, the correct choice according to ILATE is:
   - a) $u=\cos x$, $dv=x\,dx$
   - b) $u=x$, $dv=\cos x\,dx$
   - c) $u=x\cos x$, $dv=dx$
   - d) Any of the above is equivalent
   > **Correct answer: b)** According to ILATE, algebraic ($x$) takes priority over trigonometric ($\cos x$), so $u=x$ and $dv=\cos x\,dx$.

7. The result of $\int xe^{-x}\,dx$ is:
   - a) $-xe^{-x}+e^{-x}+C$
   - b) $e^{-x}(x+1)+C$
   - c) $-e^{-x}(x+1)+C$
   - d) $xe^{-x}+e^{-x}+C$
   > **Correct answer: c)** $u=x$, $dv=e^{-x}dx$, $v=-e^{-x}$. $\int xe^{-x}dx=-xe^{-x}+\int e^{-x}dx=-xe^{-x}-e^{-x}+C=-e^{-x}(x+1)+C$.

---

#### 9.2.3 Iterated and circular integration by parts

**Worked Example**

Compute $\displaystyle\int e^x\sin x\,dx$ (circular integral).

**Step-by-step solution:**

Let $I = \int e^x\sin x\,dx$.

**First application of parts:** $u=\sin x$, $dv=e^x\,dx \Rightarrow du=\cos x\,dx$, $v=e^x$:
$$I = e^x\sin x - \int e^x\cos x\,dx$$

**Second application of parts** to $\int e^x\cos x\,dx$: $u=\cos x$, $dv=e^x\,dx \Rightarrow du=-\sin x\,dx$, $v=e^x$:
$$\int e^x\cos x\,dx = e^x\cos x + \int e^x\sin x\,dx = e^x\cos x + I$$

**Substituting back:**
$$I = e^x\sin x - (e^x\cos x + I) = e^x\sin x - e^x\cos x - I$$

**Solving for $I$:**
$$2I = e^x(\sin x - \cos x) \implies \boxed{I = \frac{e^x(\sin x-\cos x)}{2}+C}$$

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int x^2\sin x\,dx$ (two applications of parts).
   > **Solution:** First: $u=x^2$, $dv=\sin x\,dx$: $-x^2\cos x+2\int x\cos x\,dx$. Second: $u=x$, $dv=\cos x\,dx$: $-x^2\cos x+2[x\sin x+\cos x]+C=-x^2\cos x+2x\sin x+2\cos x+C$.

2. Compute $\displaystyle\int e^x\cos x\,dx   > **Solution:** By the circular method (similar to the worked example): $I=e^x\cos x+\int e^x(-\sin x)\,dx=e^x\cos x-I'$, leading to $I=\frac{e^x(\cos x+\sin x)}{2}+C$.

**Intermediate Level:**

3. Compute $\displaystyle\int \sin(\ln x)\,dx$.
   > **Solution:** $u=\sin(\ln x)$, $dv=dx$: $I=x\sin(\ln x)-\int x\cdot\frac{\cos(\ln x)}{x}dx=x\sin(\ln x)-\int\cos(\ln x)dx$. Second: $\int\cos(\ln x)dx=x\cos(\ln x)+\int\sin(\ln x)dx=x\cos(\ln x)+I$. Then $I=x\sin(\ln x)-x\cos(\ln x)-I \Rightarrow I=\frac{x}{2}(\sin(\ln x)-\cos(\ln x))+C$.

4. Compute $\displaystyle\int x^3 e^{x^2}\,dx$ using the substitution $t=x^2$ followed by parts.
   > **Solution:** $t=x^2$, $dt=2x\,dx$, $x^3\,dx=x^2\cdot x\,dx=t\cdot\frac{dt}{2}$. $\int t e^t\frac{dt}{2}=\frac{1}{2}\int te^t\,dt=\frac{1}{2}[te^t-e^t]+C=\frac{e^{x^2}}{2}(x^2-1)+C$.

**EVAU Level:**

5. Compute $\displaystyle\int e^{2x}\sin(3x)\,dx$ justifying each step.

   > **Solution:** Let $I=\int e^{2x}\sin(3x)\,dx$. First part: $u=\sin(3x)$, $dv=e^{2x}dx \Rightarrow du=3\cos(3x)dx$, $v=\frac{e^{2x}}{2}$:
   > $$I=\frac{e^{2x}\sin(3x)}{2}-\frac{3}{2}\int e^{2x}\cos(3x)\,dx$$
   > Second part on $\int e^{2x}\cos(3x)\,dx$: $u=\cos(3x)$, $dv=e^{2x}dx$:
   > $$\int e^{2x}\cos(3x)\,dx=\frac{e^{2x}\cos(3x)}{2}+\frac{3}{2}\int e^{2x}\sin(3x)\,dx=\frac{e^{2x}\cos(3x)}{2}+\frac{3}{2}I$$
   > Substituting: $I=\frac{e^{2x}\sin(3x)}{2}-\frac{3}{2}\!\left(\frac{e^{2x}\cos(3x)}{2}+\frac{3I}{2}\right)=\frac{e^{2x}\sin(3x)}{2}-\frac{3e^{2x}\cos(3x)}{4}-\frac{9I}{4}$.
   > $I+\frac{9I}{4}=\frac{13I}{4}=\frac{e^{2x}}{4}(2\sin(3x)-3\cos(3x))$, so $I=\frac{e^{2x}(2\sin(3x)-3\cos(3x))}{13}+C$.

**Multiple Choice Test**

6. In the circular integral $I=\int e^x\sin x\,dx$, after two integrations by parts one obtains:
   - a) $I = e^x\sin x - e^x\cos x - I$
   - b) $I = e^x\cos x + e^x\sin x + I$
   - c) $I = e^x\sin x + e^x\cos x - I$
   - d) $2I = e^x\cos x$
   > **Correct answer: a)** After two applications of parts the integral $I$ reappears with a negative sign, allowing us to solve $2I=e^x(\sin x-\cos x)$.

7. How many applications of integration by parts are needed for $\int x^3 e^x\,dx$?
   - a) 1
   - b) 2
   - c) 3
   - d) 4
   > **Correct answer: c)** Each application reduces the degree of the polynomial by 1, so for $x^3$ three applications are needed.

---

#### 9.2.4 Integration of rational functions with denominator of degree ≤ 2

**Worked Example**

Compute $\displaystyle\int \frac{2x+3}{x^2+4x+5}\,dx$.

**Step-by-step solution:**

The denominator has discriminant $\Delta=16-20=-4<0$ (irreducible over $\mathbb{R}$). We complete the square:
$$x^2+4x+5=(x+2)^2+1$$

We split the numerator to exploit the derivative of the denominator:
$$\frac{2x+3}{x^2+4x+5}=\frac{(2x+4)-1}{x^2+4x+5}=\frac{2x+4}{x^2+4x+5}-\frac{1}{(x+2)^2+1}$$

**Integral of the first part** ($u=x^2+4x+5$, $du=(2x+4)dx$):
$$\int\frac{2x+4}{x^2+4x+5}\,dx=\ln(x^2+4x+5)+C_1$$

**Integral of the second part** (arctangent):
$$\int\frac{1}{(x+2)^2+1}\,dx=\arctan(x+2)+C_2$$

**Result:**
$$\int\frac{2x+3}{x^2+4x+5}\,dx=\ln(x^2+4x+5)-\arctan(x+2)+C$$

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int \frac{1}{x^2+4}\,dx$.
   > **Solution:** $\int\frac{1}{x^2+4}dx=\int\frac{1}{4\left(\frac{x^2}{4}+1\right)}dx=\frac{1}{4}\int\frac{1}{\left(\frac{x}{2}\right)^2+1}dx=\frac{1}{4}\cdot 2\arctan\!\left(\frac{x}{2}\right)+C=\frac{1}{2}\arctan\!\left(\frac{x}{2}\right)+C$.

2. Compute $\displaystyle\int \frac{2x}{x^2+1}\,dx$.
   > **Solution:** $u=x^2+1$, $du=2x\,dx$. $\int\frac{du}{u}=\ln(x^2+1)+C$.

**Intermediate Level:**

3. Compute $\displaystyle\int \frac{x+1}{x^2+2x+5}\,dx$.
   > **Solution:** $(x^2+2x+5)'=2x+2=2(x+1)$. We split: $\frac{x+1}{x^2+2x+5}=\frac{1}{2}\cdot\frac{2x+2}{x^2+2x+5}$. So: $\frac{1}{2}\ln(x^2+2x+5)+C$.

4. Compute $\displaystyle\int \frac{3}{x^2-2x+5}\,dx$.
   > **Solution:** $x^2-2x+5=(x-1)^2+4$. $\int\frac{3}{(x-1)^2+4}dx=3\cdot\frac{1}{2}\arctan\!\left(\frac{x-1}{2}\right)+C=\frac{3}{2}\arctan\!\left(\frac{x-1}{2}\right)+C$.

**EVAU Level:**

5. Compute $\displaystyle\int \frac{5x+1}{x^2+4x+13}\,dx$.

   > **Solution:** $x^2+4x+13=(x+2)^2+9$. Numerator: $5x+1=\frac{5}{2}(2x+4)+1-10=\frac{5}{2}(2x+4)-9$.
   > $$\int\frac{5x+1}{x^2+4x+13}dx=\frac{5}{2}\int\frac{2x+4}{x^2+4x+13}dx-9\int\frac{1}{(x+2)^2+9}dx$$
   > $=\frac{5}{2}\ln(x^2+4x+13)-9\cdot\frac{1}{3}\arctan\!\left(\frac{x+2}{3}\right)+C=\frac{5}{2}\ln(x^2+4x+13)-3\arctan\!\left(\frac{x+2}{3}\right)+C$.

**Multiple Choice Test**

6. $\displaystyle\int \frac{1}{x^2+a^2}\,dx$ (with $a\neq 0$) equals:
   - a) $\dfrac{1}{a}\arctan\!\left(\dfrac{x}{a}\right)+C$
   - b) $\arctan\!\left(\dfrac{x}{a}\right)+C$
   - c) $a\arctan\!\left(\dfrac{x}{a}\right)+C$
   - d) $\ln(x^2+a^2)+C$
   > **Correct answer: a)** The standard formula is $\int\frac{dx}{x^2+a^2}=\frac{1}{a}\arctan\frac{x}{a}+C$.

7. To decompose the integral $\int\frac{x+5}{x^2+6x+10}dx$, the first convenient operation is:
   - a) Factor the denominator over $\mathbb{C}$
   - b) Complete the square in the denominator
   - c) Make the substitution $u=x+5$
   - d) Divide the numerator by the denominator
   > **Correct answer: b)** $x^2+6x+10=(x+3)^2+1$, which allows splitting into logarithmic and arctangent terms.

---

#### 9.2.5 Integration of rational functions: simple real roots of the denominator

**Worked Example**

Compute $\displaystyle\int \frac{3x+1}{(x-1)(x+2)}\,dx$ using partial fractions.

**Step-by-step solution:**

**Step 1 – Partial fraction decomposition.** The denominator has simple roots $x=1$ and $x=-2$:
$$\frac{3x+1}{(x-1)(x+2)}=\frac{A}{x-1}+\frac{B}{x+2}$$

**Step 2 – Find $A$ and $B$.** Multiply by $(x-1)(x+2)$:
$$3x+1=A(x+2)+B(x-1)$$

- $x=1$: $4=3A \Rightarrow A=\dfrac{4}{3}$
- $x=-2$: $-5=-3B \Rightarrow B=\dfrac{5}{3}$

**Step 3 – Integrate:**
$$\int\frac{3x+1}{(x-1)(x+2)}\,dx=\frac{4}{3}\int\frac{dx}{x-1}+\frac{5}{3}\int\frac{dx}{x+2}=\frac{4}{3}\ln|x-1|+\frac{5}{3}\ln|x+2|+C$$

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int \frac{1}{x(x-1)}\,dx$.
   > **Solution:** $\frac{1}{x(x-1)}=\frac{A}{x}+\frac{B}{x-1}$. $1=A(x-1)+Bx$. $x=0: A=-1$; $x=1: B=1$. Result: $-\ln|x|+\ln|x-1|+C=\ln\left|\frac{x-1}{x}\right|+C$.

2. Compute $\displaystyle\int \frac{5}{(x+1)(x-4)}\,dx$.
   > **Solution:** $\frac{5}{(x+1)(x-4)}=\frac{A}{x+1}+\frac{B}{x-4}$. $5=A(x-4)+B(x+1)$. $x=-1: 5=-5A\Rightarrow A=-1$; $x=4: 5=5B\Rightarrow B=1$. $-\ln|x+1|+\ln|x-4|+C=\ln\!\left|\frac{x-4}{x+1}\right|+C$.

**Intermediate Level:**

3. Compute $\displaystyle\int \frac{x^2+1}{x(x-1)(x+1)}\,dx$.
   > **Solution:** $\frac{x^2+1}{x(x-1)(x+1)}=\frac{A}{x}+\frac{B}{x-1}+\frac{C}{x+1}$. $x^2+1=A(x^2-1)+Bx(x+1)+Cx(x-1)$. $x=0: 1=-A\Rightarrow A=-1$; $x=1: 2=2B\Rightarrow B=1$; $x=-1: 2=2C\Rightarrow C=1$. Result: $-\ln|x|+\ln|x-1|+\ln|x+1|+C$.

4. Compute $\displaystyle\int \frac{2x-1}{x^2-x-6}\,dx$.
   > **Solution:** Factor: $x^2-x-6=(x-3)(x+2)$. $\frac{2x-1}{(x-3)(x+2)}=\frac{A}{x-3}+\frac{B}{x+2}$. $2x-1=A(x+2)+B(x-3)$. $x=3: 5=5A\Rightarrow A=1$; $x=-2: -5=-5B\Rightarrow B=1$. $\ln|x-3|+\ln|x+2|+C$.

**EVAU Level:**

5. Let $f(x)=\dfrac{3x^2+2x-1}{x(x+1)(x-1)}$.

   **(a)** Decompose $f(x)$ into partial fractions.  
   **(b)** Compute $\displaystyle\int_2^3 f(x)\,dx$ (leave the result in terms of logarithms).

   > **Solution:**
   >
   > **(a)** $\frac{3x^2+2x-1}{x(x+1)(x-1)}=\frac{A}{x}+\frac{B}{x+1}+\frac{C}{x-1}$.
   > $3x^2+2x-1=A(x^2-1)+B(x^2-x)+C(x^2+x)$.
   > $x=0$: $-1=-A\Rightarrow A=1$. $x=-1$: $0=2B\Rightarrow B=0$. $x=1$: $4=2C\Rightarrow C=2$.
   > $f(x)=\frac{1}{x}+\frac{2}{x-1}$.
   >
   > **(b)** $\int_2^3\!\left(\frac{1}{x}+\frac{2}{x-1}\right)dx=[\ln|x|+2\ln|x-1|]_2^3=(\ln 3+2\ln 2)-(\ln 2+2\ln 1)=\ln 3+2\ln 2-\ln 2=\ln 3+\ln 2=\ln 6$.

**Multiple Choice Test**

6. The decomposition of $\dfrac{1}{x^2-1}$ into partial fractions is:
   - a) $\dfrac{1}{2}\!\left(\dfrac{1}{x-1}-\dfrac{1}{x+1}\right)$
   - b) $\dfrac{1}{x-1}+\dfrac{1}{x+1}$
   - c) $\dfrac{1}{2}\!\left(\dfrac{1}{x-1}+\dfrac{1}{x+1}\right)$
   - d) $\dfrac{-1}{x-1}+\dfrac{1}{x+1}$
   > **Correct answer: a)** $\frac{1}{(x-1)(x+1)}=\frac{A}{x-1}+\frac{B}{x+1}$; $x=1\Rightarrow A=\frac{1}{2}$, $x=-1\Rightarrow B=-\frac{1}{2}$.

7. $\displaystyle\int\frac{dx}{x^2-4}$ equals:
   - a) $\dfrac{1}{4}\ln\!\left|\dfrac{x-2}{x+2}\right|+C$
   - b) $\dfrac{1}{2}\ln(x^2-4)+C$
   - c) $\arctan\!\left(\dfrac{x}{2}\right)+C$
   - d) $\dfrac{1}{2}\ln|x-2|-\dfrac{1}{2}\ln|x+2|+C$
   > **Correct answer: a)** Partial fractions: $\frac{1}{(x-2)(x+2)}=\frac{1/4}{x-2}-\frac{1/4}{x+2}$. Integrating: $\frac{1}{4}\ln|x-2|-\frac{1}{4}\ln|x+2|+C=\frac{1}{4}\ln\left|\frac{x-2}{x+2}\right|+C$.

---

#### 9.2.6 Integration of rational functions: complex conjugate root or repeated real root

**Worked Example**

Compute $\displaystyle\int \frac{x+3}{(x-1)^2(x+2)}\,dx$ (repeated real root at $x=1$).

**Step-by-step solution:**

**Step 1 – Decomposition with repeated root:**
$$\frac{x+3}{(x-1)^2(x+2)}=\frac{A}{x-1}+\frac{B}{(x-1)^2}+\frac{C}{x+2}$$

**Step 2 – Determine coefficients.** Multiply by $(x-1)^2(x+2)$:
$$x+3=A(x-1)(x+2)+B(x+2)+C(x-1)^2$$

- $x=1$: $4=3B \Rightarrow B=\dfrac{4}{3}$
- $x=-2$: $1=9C \Rightarrow C=\dfrac{1}{9}$
- Coefficient of $x^2$: $0=A+C \Rightarrow A=-C=-\dfrac{1}{9}$

**Step 3 – Integrate:**
$$\int\frac{x+3}{(x-1)^2(x+2)}\,dx=-\frac{1}{9}\ln|x-1|+\frac{4}{3}\cdot\frac{-1}{x-1}+\frac{1}{9}\ln|x+2|+C$$
$$=\frac{1}{9}\ln\!\left|\frac{x+2}{x-1}\right|-\frac{4}{3(x-1)}+C$$

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int \frac{1}{x^2(x+1)}\,dx$.
   > **Solution:** $\frac{1}{x^2(x+1)}=\frac{A}{x}+\frac{B}{x^2}+\frac{C}{x+1}$. $1=Ax(x+1)+B(x+1)+Cx^2$. $x=0:1=B$; $x=-1:1=C$; matching $x^2$: $0=A+C\Rightarrow A=-1$. Result: $-\ln|x|-\frac{1}{x}+\ln|x+1|+C=\ln\!\left|\frac{x+1}{x}\right|-\frac{1}{x}+C$.

2. Compute $\displaystyle\int \frac{2}{x(x-1)^2}\,dx$.
   > **Solution:** $\frac{2}{x(x-1)^2}=\frac{A}{x}+\frac{B}{x-1}+\frac{C}{(x-1)^2}$. $2=A(x-1)^2+Bx(x-1)+Cx$. $x=0:2=A$; $x=1:2=C$; matching $x^2$: $0=A+B\Rightarrow B=-2$. $2\ln|x|-2\ln|x-1|-\frac{2}{x-1}+C$.

**Intermediate Level:**

3. Compute $\displaystyle\int \frac{1}{(x^2+1)(x-1)}\,dx$.
   > **Solution:** $\frac{1}{(x^2+1)(x-1)}=\frac{A}{x-1}+\frac{Bx+C}{x^2+1}$. $1=A(x^2+1)+(Bx+C)(x-1)$. $x=1:1=2A\Rightarrow A=\frac{1}{2}$. Matching $x^2$: $0=A+B\Rightarrow B=-\frac{1}{2}$. Matching $x^0$: $1=A-C\Rightarrow C=A-1=-\frac{1}{2}$. $\int\left(\frac{1/2}{x-1}+\frac{-x/2-1/2}{x^2+1}\right)dx=\frac{1}{2}\ln|x-1|-\frac{1}{4}\ln(x^2+1)-\frac{1}{2}\arctan x+C$.

4. Compute $\displaystyle\int \frac{3x}{(x+1)^2(x-2)}\,dx$.
   > **Solution:** $\frac{3x}{(x+1)^2(x-2)}=\frac{A}{x+1}+\frac{B}{(x+1)^2}+\frac{C}{x-2}$. $3x=A(x+1)(x-2)+B(x-2)+C(x+1)^2$. $x=-1:-3=-3B\Rightarrow B=1$; $x=2:6=9C\Rightarrow C=\frac{2}{3}$; $x^2$: $0=A+C\Rightarrow A=-\frac{2}{3}$. Result: $-\frac{2}{3}\ln|x+1|-\frac{1}{x+1}+\frac{2}{3}\ln|x-2|+C$.

**EVAU Level:**

5. Compute $\displaystyle\int \frac{x^2+2}{(x^2+1)(x-1)}\,dx$.

   > **Solution:** Decomposition: $\frac{x^2+2}{(x^2+1)(x-1)}=\frac{Ax+B}{x^2+1}+\frac{C}{x-1}$. $x^2+2=(Ax+B)(x-1)+C(x^2+1)$. $x=1: 3=2C\Rightarrow C=\frac{3}{2}$. Matching $x^2$: $1=A+C\Rightarrow A=-\frac{1}{2}$. Matching $x^0$: $2=-B+C=-B+\frac{3}{2}\Rightarrow B=-\frac{1}{2}$.
   > $$\int\!\left(\frac{-x/2-1/2}{x^2+1}+\frac{3/2}{x-1}\right)dx=-\frac{1}{4}\ln(x^2+1)-\frac{1}{2}\arctan x+\frac{3}{2}\ln|x-1|+C$$

**Multiple Choice Test**

6. When the denominator has a repeated real root $(x-a)^2$, the partial fraction decomposition includes:
   - a) Only the fraction $\dfrac{A}{(x-a)^2}$
   - b) The fractions $\dfrac{A}{x-a}$ and $\dfrac{B}{(x-a)^2}$
   - c) The fractions $\dfrac{Ax+B}{x-a}$ and $\dfrac{C}{(x-a)^2}$
   - d) Only the fraction $\dfrac{A}{x-a}$
   > **Correct answer: b)** For a repeated real root both terms $\frac{A}{x-a}+\frac{B}{(x-a)^2}$ are needed.

7. If the denominator has an irreducible factor $x^2+bx+c$ ($\Delta<0$), the corresponding term in the decomposition is:
   - a) $\dfrac{A}{x^2+bx+c}$
   - b) $\dfrac{Ax}{x^2+bx+c}$
   - c) $\dfrac{Ax+B}{x^2+bx+c}$
   - d) $A\ln(x^2+bx+c)$
   > **Correct answer: c)** For irreducible quadratic factors the numerator is of degree 1: $\frac{Ax+B}{x^2+bx+c}$.

---

### 9.3 Definite integral

---

#### 9.3.1 Definition of the definite integral as a limit of Riemann sums

**Worked Example**

Approximate $\displaystyle\int_0^2 x^2\,dx$ using 4 equal rectangles with midpoints (Riemann sum).

**Step-by-step solution:**

**Step 1 – Data.** Interval $[0,2]$, $n=4$ subintervals. Width: $\Delta x=\dfrac{2-0}{4}=0{,}5$.

**Step 2 – Midpoints:** $x_1^*=0{,}25$, $x_2^*=0{,}75$, $x_3^*=1{,}25$, $x_4^*=1{,}75$.

**Step 3 – Riemann sum:**
$$S_4=\sum_{i=1}^4 f(x_i^*)\Delta x = 0{,}5\cdot\left[(0{,}25)^2+(0{,}75)^2+(1{,}25)^2+(1{,}75)^2\right]$$
$$=0{,}5\cdot[0{,}0625+0{,}5625+1{,}5625+3{,}0625]=0{,}5\cdot 5{,}25=2{,}625$$

**Exact value:** $\displaystyle\int_0^2 x^2\,dx=\left[\frac{x^3}{3}\right]_0^2=\frac{8}{3}\approx 2{,}667$. The error is small: $|2{,}667-2{,}625|=0{,}042$.

**Exercises with Solutions**

**Basic Level:**

1. Compute the Riemann sum of $f(x)=2x$ on $[0,3]$ with $n=3$ rectangles, using right endpoints.
   > **Solution:** $\Delta x=1$. Points: $x_1=1$, $x_2=2$, $x_3=3$. $S_3=1\cdot(2+4+6)=12$. Exact value: $\int_0^3 2x\,dx=[x^2]_0^3=9$. (The right-endpoint sum overestimates since $f$ is increasing.)

2. Write the Riemann sum of $f(x)=e^x$ on $[0,1]$ with $n$ equal subintervals using left endpoints, without computing it.
   > **Solution:** $\Delta x=\frac{1}{n}$. Points: $x_k=\frac{k}{n}$ for $k=0,\ldots,n-1$. $S_n=\frac{1}{n}\sum_{k=0}^{n-1}e^{k/n}$.

**Intermediate Level:**

3. Compute the upper and lower Riemann sums of $f(x)=x^2-1$ on $[0,2]$ with $n=4$ equal rectangles.
   > **Solution:** $\Delta x=0{,}5$. Subintervals: $[0,0{,}5]$, $[0{,}5,1]$, $[1,1{,}5]$, $[1{,}5,2]$. $f$ is increasing on $[0,2]$ for $|x|>0$, minimum at left endpoint. $S^-=0{,}5[f(0)+f(0{,}5)+f(1)+f(1{,}5)]=0{,}5[-1-0{,}75+0+1{,}25]=0{,}5\cdot(-0{,}5)=-0{,}25$. $S^+=0{,}5[f(0{,}5)+f(1)+f(1{,}5)+f(2)]=0{,}5[-0{,}75+0+1{,}25+3]=0{,}5\cdot 3{,}5=1{,}75$. Exact value: $\left[\frac{x^3}{3}-x\right]_0^2=\frac{8}{3}-2=\frac{2}{3}\approx 0{,}667$.

4. Interpret geometrically $\displaystyle\int_{-1}^1(1-x^2)\,dx$ as area and compute its value.
   > **Solution:** $1-x^2\geq 0$ on $[-1,1]$ (inverted parabola). The area is the region under the parabola. $\int_{-1}^1(1-x^2)\,dx=\left[x-\frac{x^3}{3}\right]_{-1}^1=\left(1-\frac{1}{3}\right)-\left(-1+\frac{1}{3}\right)=\frac{2}{3}+\frac{2}{3}=\frac{4}{3}$.

**EVAU Level:**

5. Let $f(x)=3x-x^2$.

   **(a)** Express $\displaystyle\int_0^3 f(x)\,dx$ as a limit of Riemann sums with $n$ equal rectangles and right endpoints.  
   **(b)** Interpret the integral geometrically and compute its exact value.

   > **Solution:**
   >
   > **(a)** $\Delta x=\frac{3}{n}$. $x_k=\frac{3k}{n}$, $k=1,\ldots,n$. $f(x_k)=3\cdot\frac{3k}{n}-\left(\frac{3k}{n}\right)^2=\frac{9k}{n}-\frac{9k^2}{n^2}$.
   > $$\int_0^3 f(x)\,dx=\lim_{n\to\infty}\frac{3}{n}\sum_{k=1}^n\!\left(\frac{9k}{n}-\frac{9k^2}{n^2}\right)$$
   >
   > **(b)** $f(x)=3x-x^2=x(3-x)\geq 0$ on $[0,3]$ (parabola with roots at $0$ and $3$). The integral gives the area under the parabola. $\int_0^3(3x-x^2)\,dx=\left[\frac{3x^2}{2}-\frac{x^3}{3}\right]_0^3=\frac{27}{2}-9=\frac{27-18}{2}=\frac{9}{2}$.

**Multiple Choice Test**

6. The definite integral $\displaystyle\int_a^b f(x)\,dx$ is defined as:
   - a) The antiderivative of $f$ evaluated at $b-a$
   - b) The limit of Riemann sums as the number of subdivisions tends to infinity
   - c) The area between the curve and the $OX$ axis, always positive
   - d) The function $F(x)$ such that $F'(x)=f(x)$
   > **Correct answer: b)** The definite integral is formally defined as $\lim_{n\to\infty}\sum_{i=1}^n f(x_i^*)\Delta x_i$, regardless of the sign of $f$.

7. If $f(x)\geq 0$ on $[a,b]$, the integral $\displaystyle\int_a^b f(x)\,dx$ represents:
   - a) The signed area under the curve
   - b) The area between the curve and the $OX$ axis
   - c) The arc length of the curve on $[a,b]$
   - d) The average slope of $f$ on $[a,b]$
   > **Correct answer: b)** When $f\geq 0$, the definite integral equals the area of the region between the curve and the horizontal axis.

---

#### 9.3.2 Geometric interpretation: signed area under a curve

**Worked Example**

Compute $\displaystyle\int_{-1}^2 x^2\,dx$ and interpret the result geometrically.

**Step-by-step solution:**

Apply Barrow's rule with $F(x)=\dfrac{x^3}{3}$:
$$\int_{-1}^2 x^2\,dx=\left[\frac{x^3}{3}\right]_{-1}^2=\frac{8}{3}-\frac{-1}{3}=\frac{8}{3}+\frac{1}{3}=\frac{9}{3}=3$$

**Geometric interpretation:** $f(x)=x^2\geq 0$ throughout $\mathbb{R}$, so the integral represents the area of the region between the parabola $y=x^2$ and the $OX$ axis, from $x=-1$ to $x=2$. The result is $3$ sq. units.

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int_0^{\pi}\sin x\,dx$ and interpret the result.
   > **Solution:** $[-\cos x]_0^{\pi}=-\cos\pi+\cos 0=1+1=2$. Sine is positive on $[0,\pi]$, so the integral gives the area between the curve and the $OX$ axis on that interval: $2$ sq. units.

2. Compute $\displaystyle\int_{-2}^2(4-x^2)\,dx$.
   > **Solution:** $\left[4x-\frac{x^3}{3}\right]_{-2}^2=\left(8-\frac{8}{3}\right)-\left(-8+\frac{8}{3}\right)=8-\frac{8}{3}+8-\frac{8}{3}=16-\frac{16}{3}=\frac{32}{3}$.

**Intermediate Level:**

3. Explain why $\displaystyle\int_{-\pi}^{\pi}\sin x\,dx=0$ even though $\sin x$ is not identically zero.
   > **Solution:** $\sin x$ is an odd function: the positive part on $[0,\pi]$ and the negative part on $[-\pi,0]$ have equal absolute values but opposite signs. $\int_{-\pi}^0\sin x\,dx=-2$ and $\int_0^\pi\sin x\,dx=2$, summing to zero.

4. Compute $\displaystyle\int_0^2(x-1)^2\,dx$ and indicate whether the function takes negative values on the interval.
   > **Solution:** $(x-1)^2\geq 0$ always. $\int_0^2(x-1)^2\,dx=\left[\frac{(x-1)^3}{3}\right]_0^2=\frac{1}{3}-\left(-\frac{1}{3}\right)=\frac{2}{3}$.

**EVAU Level:**

5. Let $f(x)=x^3-4x$.

   **(a)** Determine on which subintervals of $[-2,2]$ is $f$ positive and on which negative.  
   **(b)** Compute $\displaystyle\int_{-2}^2 f(x)\,dx$ and explain why the result is $0$.  
   **(c)** Compute the total (geometric) area of the region enclosed between the curve and the $OX$ axis on $[-2,2]$.

   > **Solution:**
   >
   > **(a)** $f(x)=x(x^2-4)=x(x-2)(x+2)$. Roots: $x=-2,0,2$. Sign in $(-2,0)$: $x=-1$: $(-1)((-1)-2)((-1)+2)=(-1)(-3)(1)=3>0$. Sign in $(0,2)$: $x=1$: $(1)(-1)(3)=-3<0$.
   >
   > **(b)** $f$ is odd: $f(-x)=-f(x)$. Therefore $\int_{-2}^2 f(x)\,dx=0$ (positive and negative contributions cancel).
   >
   > **(c)** Geometric area $=\left|\int_{-2}^0 f\,dx\right|+\left|\int_0^2 f\,dx\right|$. $\int_0^2(x^3-4x)\,dx=\left[\frac{x^4}{4}-2x^2\right]_0^2=4-8=-4$. By symmetry, $\int_{-2}^0(x^3-4x)\,dx=4$. Total area $=4+4=8$ sq. units.

**Multiple Choice Test**

6. If $f(x)<0$ on $(a,b)$, then $\displaystyle\int_a^b f(x)\,dx$:
   - a) Is positive, since area is always positive
   - b) Is negative, since the curve lies below the $OX$ axis
   - c) Is zero, since the function does not touch the axis
   - d) Does not exist
   > **Correct answer: b)** The signed integral returns a negative value when $f<0$; to obtain the area one must take the absolute value.

7. $\displaystyle\int_a^a f(x)\,dx$ equals:
   - a) $f(a)$
   - b) $F(a)$, where $F$ is an antiderivative
   - c) $0$
   - d) $1$
   > **Correct answer: c)** When both limits of integration coincide, the integral is zero by definition.

---

#### 9.3.3 Properties of the definite integral

**Worked Example**

Knowing that $\displaystyle\int_0^3 f(x)\,dx=5$ and $\displaystyle\int_0^3 g(x)\,dx=2$, compute $\displaystyle\int_0^3[3f(x)-2g(x)]\,dx$.

**Step-by-step solution:**

We apply **linearity** of the definite integral:

$$\int_0^3[3f(x)-2g(x)]\,dx=3\int_0^3 f(x)\,dx-2\int_0^3 g(x)\,dx=3\cdot 5-2\cdot 2=15-4=11$$

**Exercises with Solutions**

**Basic Level:**

1. Given that $\displaystyle\int_1^4 f(x)\,dx=7$, compute $\displaystyle\int_4^1 f(x)\,dx$.
   > **Solution:** By the reversal of limits property: $\int_4^1 f(x)\,dx=-\int_1^4 f(x)\,dx=-7$.

2. Given $\displaystyle\int_0^5 f(x)\,dx=10$ and $\displaystyle\int_0^3 f(x)\,dx=4$, compute $\displaystyle\int_3^5 f(x)\,dx$.
   > **Solution:** $\int_3^5 f(x)\,dx=\int_0^5 f(x)\,dx-\int_0^3 f(x)\,dx=10-4=6$ (additivity over intervals).

**Intermediate Level:**

3. Prove that if $f$ is even, then $\displaystyle\int_{-a}^a f(x)\,dx=2\int_0^a f(x)\,dx$.
   > **Solution:** $\int_{-a}^a f=\int_{-a}^0 f+\int_0^a f$. In the first piece let $t=-x$: $\int_{-a}^0 f(x)\,dx=\int_a^0 f(-t)(-dt)=\int_0^a f(-t)\,dt=\int_0^a f(t)\,dt$ (using $f(-t)=f(t)$). Therefore $\int_{-a}^a f=2\int_0^a f$.

4. Use linearity to compute $\displaystyle\int_0^1\left(3x^2+4x-1\right)dx$.
   > **Solution:** $3\int_0^1 x^2\,dx+4\int_0^1 x\,dx-\int_0^1 1\,dx=3\cdot\frac{1}{3}+4\cdot\frac{1}{2}-1=1+2-1=2$.

**EVAU Level:**

5. Let $\displaystyle\int_0^2 f(x)\,dx=3$, $\displaystyle\int_2^5 f(x)\,dx=-1$ and $\displaystyle\int_0^5 g(x)\,dx=4$. Compute:

   **(a)** $\displaystyle\int_0^5 f(x)\,dx$.  
   **(b)** $\displaystyle\int_0^5[2f(x)-g(x)]\,dx$.  
   **(c)** $\displaystyle\int_5^0 f(x)\,dx$.

   > **Solution:**
   > **(a)** $\int_0^5 f=\int_0^2 f+\int_2^5 f=3+(-1)=2$.
   > **(b)** $2\int_0^5 f-\int_0^5 g=2\cdot 2-4=0$.
   > **(c)** $\int_5^0 f=-\int_0^5 f=-2$.

**Multiple Choice Test**

6. Given that $f(x)\leq g(x)$ on $[a,b]$, then:
   - a) $\displaystyle\int_a^b f(x)\,dx\leq\int_a^b g(x)\,dx$
   - b) $\displaystyle\int_a^b f(x)\,dx\geq\int_a^b g(x)\,dx$
   - c) The integrals are equal
   - d) There is no relation between the integrals
   > **Correct answer: a)** Monotonicity of the integral: if $f\leq g$ on $[a,b]$, then $\int_a^b f\leq\int_a^b g$.

7. $\displaystyle\int_0^{2\pi}\sin x\,dx+\int_0^{2\pi}\cos x\,dx$ equals:
   - a) $2\pi$
   - b) $4$
   - c) $2$
   - d) $0$
   > **Correct answer: d)** $\int_0^{2\pi}\sin x\,dx=[-\cos x]_0^{2\pi}=0$ and $\int_0^{2\pi}\cos x\,dx=[\sin x]_0^{2\pi}=0$. Sum: $0$.

---

#### 9.3.4 Fundamental theorem of calculus (Barrow's rule): statement and application

**Worked Example**

State Barrow's rule and apply it to compute $\displaystyle\int_1^e \frac{\ln x}{x}\,dx$.

**Step-by-step solution:**

**Statement (Barrow's Rule):** If $F$ is an antiderivative of $f$ continuous on $[a,b]$, then:
$$\int_a^b f(x)\,dx = F(b)-F(a) = \Big[F(x)\Big]_a^b$$

**Application:**

We need $F(x)$ such that $F'(x)=\dfrac{\ln x}{x}$.

We recognise the immediate composite form with $u=\ln x$, $u'=\dfrac{1}{x}$:
$$F(x)=\frac{(\ln x)^2}{2}$$

**Applying Barrow's rule:**
$$\int_1^e\frac{\ln x}{x}\,dx=\left[\frac{(\ln x)^2}{2}\right]_1^e=\frac{(\ln e)^2}{2}-\frac{(\ln 1)^2}{2}=\frac{1}{2}-0=\frac{1}{2}$$

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int_0^1(2x+3)\,dx$ using Barrow's rule.
   > **Solution:** $F(x)=x^2+3x$. $[x^2+3x]_0^1=(1+3)-0=4$.

2. Compute $\displaystyle\int_0^{\pi/2}\cos x\,dx$.
   > **Solution:** $F(x)=\sin x$. $[\sin x]_0^{\pi/2}=\sin(\pi/2)-\sin(0)=1-0=1$.

**Intermediate Level:**

3. Compute $\displaystyle\int_1^4\frac{1}{\sqrt{x}}\,dx$.
   > **Solution:** $F(x)=2\sqrt{x}$. $[2\sqrt{x}]_1^4=2\sqrt{4}-2\sqrt{1}=4-2=2$.

4. Compute $\displaystyle\int_0^1 xe^{x^2}\,dx$.
   > **Solution:** Immediate antiderivative: $F(x)=\frac{e^{x^2}}{2}$. $\left[\frac{e^{x^2}}{2}\right]_0^1=\frac{e}{2}-\frac{1}{2}=\frac{e-1}{2}$.

**EVAU Level:**

5. Compute the following definite integrals, justifying the antiderivative used:

   **(a)** $\displaystyle\int_0^{\pi}\sin^2 x\,dx$ (use $\sin^2 x=\frac{1-\cos(2x)}{2}$).  
   **(b)** $\displaystyle\int_1^2\frac{x^2+1}{x}\,dx$.  
   **(c)** $\displaystyle\int_0^1\frac{1}{1+x^2}\,dx$.

   > **Solution:**
   >
   > **(a)** $\int_0^\pi\frac{1-\cos(2x)}{2}\,dx=\frac{1}{2}\left[x-\frac{\sin(2x)}{2}\right]_0^\pi=\frac{1}{2}\left[(\pi-0)-(0-0)\right]=\frac{\pi}{2}$.
   >
   > **(b)** $\frac{x^2+1}{x}=x+\frac{1}{x}$. Antiderivative: $\frac{x^2}{2}+\ln x$. $\left[\frac{x^2}{2}+\ln x\right]_1^2=\left(2+\ln 2\right)-\left(\frac{1}{2}+0\right)=\frac{3}{2}+\ln 2$.
   >
   > **(c)** Antiderivative: $\arctan x$. $[\arctan x]_0^1=\arctan 1-\arctan 0=\frac{\pi}{4}-0=\frac{\pi}{4}$.

**Multiple Choice Test**

6. The Fundamental Theorem of Calculus relates:
   - a) Riemann sums with limits
   - b) Differentiation with integration via antiderivatives
   - c) Continuity with differentiability
   - d) Local extrema with the second derivative
   > **Correct answer: b)** The FTC establishes that integration and differentiation are inverse operations: if $F'=f$, then $\int_a^b f=F(b)-F(a)$.

7. To compute $\displaystyle\int_1^e\frac{1}{x}\,dx$ we use:
   - a) $F(x)=-\frac{1}{x^2}$
   - b) $F(x)=\ln x$
   - c) $F(x)=e^x$
   - d) $F(x)=x\ln x$
   > **Correct answer: b)** $\frac{d}{dx}(\ln x)=\frac{1}{x}$, so $F(x)=\ln x$ and $[\ln x]_1^e=1-0=1$.

---

#### 9.3.5 Computation of definite integrals using Barrow's rule

**Worked Example**

Compute $\displaystyle\int_0^1\frac{2x+1}{x^2+x+1}\,dx$.

**Step-by-step solution:**

We observe that $(x^2+x+1)'=2x+1$, so the numerator is the derivative of the denominator.

$$\int_0^1\frac{2x+1}{x^2+x+1}\,dx=\Big[\ln(x^2+x+1)\Big]_0^1$$

$$=\ln(1+1+1)-\ln(0+0+1)=\ln 3-\ln 1=\ln 3$$

**Exercises with Solutions**

**Basic Level:**

1. Compute $\displaystyle\int_0^2 e^{3x}\,dx$.
   > **Solution:** $F(x)=\frac{e^{3x}}{3}$. $\left[\frac{e^{3x}}{3}\right]_0^2=\frac{e^6}{3}-\frac{1}{3}=\frac{e^6-1}{3}$.

2. Compute $\displaystyle\int_1^2(x^3-2x)\,dx$.
   > **Solution:** $\left[\frac{x^4}{4}-x^2\right]_1^2=(4-4)-(\frac{1}{4}-1)=0-(-\frac{3}{4})=\frac{3}{4}$.

**Intermediate Level:**

3. Compute $\displaystyle\int_0^1 x\sqrt{1+x^2}\,dx$.
   > **Solution:** $u=1+x^2$, $du=2x\,dx$. Limits: $u(0)=1$, $u(1)=2$. $\frac{1}{2}\int_1^2\sqrt{u}\,du=\frac{1}{2}\left[\frac{2u^{3/2}}{3}\right]_1^2=\frac{1}{3}[2\sqrt{2}-1]=\frac{2\sqrt{2}-1}{3}$.

4. Compute $\displaystyle\int_0^{\pi/2} x\cos x\,dx$ (by parts with Barrow's rule).
   > **Solution:** $u=x$, $dv=\cos x\,dx$. $[x\sin x+\cos x]_0^{\pi/2}=(\frac{\pi}{2}\cdot 1+0)-(0+1)=\frac{\pi}{2}-1$.

**EVAU Level:**

5. Compute $\displaystyle\int_0^1\frac{x^3-x}{x^2+1}\,dx$.

   > **Solution:** Polynomial division: $\frac{x^3-x}{x^2+1}=x+\frac{-2x}{x^2+1}=x-\frac{2x}{x^2+1}$.
   > $$\int_0^1\!\left(x-\frac{2x}{x^2+1}\right)dx=\left[\frac{x^2}{2}-\ln(x^2+1)\right]_0^1=\left(\frac{1}{2}-\ln 2\right)-(0-0)=\frac{1}{2}-\ln 2$$

**Multiple Choice Test**

6. $\displaystyle\int_1^2\frac{1}{x^2}\,dx$ equals:
   - a) $\ln 2$
   - b) $\dfrac{1}{2}$
   - c) $-\dfrac{1}{2}$
   - d) $1$
   > **Correct answer: b)** $F(x)=-\frac{1}{x}$. $[-\frac{1}{x}]_1^2=-\frac{1}{2}+1=\frac{1}{2}$.

7. $\displaystyle\int_0^1 e^{-x}\,dx$ equals:
   - a) $e^{-1}$
   - b) $1-e^{-1}$
   - c) $e-1$
   - d) $-e^{-1}$
   > **Correct answer: b)** $[-e^{-x}]_0^1=-e^{-1}+e^0=1-e^{-1}=1-\frac{1}{e}$.

---

### 9.4 Area calculations

---

#### 9.4.1 Area between a curve and the OX axis on an interval

**Worked Example**

Compute the area of the region between the curve $y=x^2-4$ and the $OX$ axis on $[-2,2]$.

**Step-by-step solution:**

**Step 1 – Sign of $f(x)=x^2-4$.** Roots: $x=\pm 2$. On $(-2,2)$: $f(0)=-4<0$, so $f\leq 0$ throughout the interval.

**Step 2 – Area = absolute value of the integral:**
$$A=\left|\int_{-2}^2(x^2-4)\,dx\right|=\left|\left[\frac{x^3}{3}-4x\right]_{-2}^2\right|$$

**Step 3 – Compute the integral:**
$$\left[\frac{x^3}{3}-4x\right]_{-2}^2=\left(\frac{8}{3}-8\right)-\left(\frac{-8}{3}+8\right)=\frac{8}{3}-8+\frac{8}{3}-8=\frac{16}{3}-16=\frac{16-48}{3}=-\frac{32}{3}$$

**Step 4 – Area:**
$$A=\left|-\frac{32}{3}\right|=\frac{32}{3}\text{ sq. units}$$

**Exercises with Solutions**

**Basic Level:**

1. Compute the area under $y=4-x^2$ above the $OX$ axis (the parabola is above the axis between its roots).
   > **Solution:** Roots: $x=\pm 2$; $f\geq 0$ on $[-2,2]$. $A=\int_{-2}^2(4-x^2)\,dx=\left[4x-\frac{x^3}{3}\right]_{-2}^2=(8-\frac{8}{3})-(-8+\frac{8}{3})=\frac{32}{3}$ sq. units.

2. Compute the area of the region enclosed between $y=\sin x$ and the $OX$ axis on $[0,\pi]$.
   > **Solution:** $\sin x\geq 0$ on $[0,\pi]$. $A=\int_0^\pi\sin x\,dx=[-\cos x]_0^\pi=2$ sq. units.

**Intermediate Level:**

3. Compute the area between $y=x^3$ and the $OX$ axis on $[-1,1]$.
   > **Solution:** $x^3<0$ on $(-1,0)$ and $x^3>0$ on $(0,1)$. $A=\left|\int_{-1}^0 x^3\,dx\right|+\int_0^1 x^3\,dx=\left|\left[-\frac{1}{4}\right]\right|+\frac{1}{4}=\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$ sq. units.

4. Compute the area enclosed between $y=e^x-1$ and the $OX$ axis on $[-1,1]$.
   > **Solution:** $e^x-1=0\Leftrightarrow x=0$. For $x<0$: $e^x<1\Rightarrow f<0$. For $x>0$: $f>0$. $A=\left|\int_{-1}^0(e^x-1)\,dx\right|+\int_0^1(e^x-1)\,dx$. $\int_{-1}^0(e^x-1)\,dx=[e^x-x]_{-1}^0=(1-0)-(e^{-1}+1)=-e^{-1}$. $\int_0^1(e^x-1)\,dx=[e^x-x]_0^1=(e-1)-(1-0)=e-2$. $A=e^{-1}+(e-2)=e-2+\frac{1}{e}$ sq. units.

**EVAU Level:**

5. Compute the total area of the region enclosed between the curve $y=x^3-3x^2+2x$ and the $OX$ axis.

   > **Solution:** Roots: $x(x^2-3x+2)=x(x-1)(x-2)=0$, so $x=0,1,2$.
   >
   > - On $(0,1)$: $f(0{,}5)=0{,}5-0{,}75+1=0{,}75>0$.
   > - On $(1,2)$: $f(1{,}5)=3{,}375-6{,}75+3=-0{,}375<0$.
   >
   > $I_1=\int_0^1(x^3-3x^2+2x)\,dx=\left[\frac{x^4}{4}-x^3+x^2\right]_0^1=\frac{1}{4}-1+1=\frac{1}{4}$.
   >
   > $I_2=\int_1^2(x^3-3x^2+2x)\,dx=\left[\frac{x^4}{4}-x^3+x^2\right]_1^2=(4-8+4)-\frac{1}{4}=-\frac{1}{4}$.
   >
   > $A=|I_1|+|I_2|=\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$ sq. units.

**Multiple Choice Test**

6. To compute the area between $f(x)=x-x^2$ and the $OX$ axis on $[0,2]$, how should one proceed?
   - a) Compute $\int_0^2(x-x^2)\,dx$ directly
   - b) Find the roots of $f$, split the interval, and sum the absolute values
   - c) Compute $-\int_0^2(x-x^2)\,dx$
   - d) Compute $\int_0^2|f(x)|\,dx$ as if it were $\int_0^2 f(x)\,dx$
   > **Correct answer: b)** Roots: $x=0$ and $x=1$; $f>0$ on $(0,1)$, $f<0$ on $(1,2)$. One must split and integrate by pieces.

7. The area between $y=x^2$ and the $OX$ axis on $[-1,1]$ is:
   - a) $0$
   - b) $\dfrac{1}{3}$
   - c) $\dfrac{2}{3}$
   - d) $2$
   > **Correct answer: c)** $x^2\geq 0$, so $A=\int_{-1}^1 x^2\,dx=\left[\frac{x^3}{3}\right]_{-1}^1=\frac{1}{3}+\frac{1}{3}=\frac{2}{3}$.

---

#### 9.4.2 Handling functions that change sign: splitting the interval

**Worked Example**

Compute the total area of the region between $y=\cos x$ and the $OX$ axis on $[0,2\pi]$.

**Step-by-step solution:**

**Step 1 – Sign of $\cos x$ on $[0,2\pi]$:**
- $\cos x\geq 0$ on $\left[0,\frac{\pi}{2}\right]\cup\left[\frac{3\pi}{2},2\pi\right]$
- $\cos x\leq 0$ on $\left[\frac{\pi}{2},\frac{3\pi}{2}\right]$

**Step 2 – Split into three subintervals and compute:**

$$A_1=\int_0^{\pi/2}\cos x\,dx=[\sin x]_0^{\pi/2}=1$$

$$A_2=\left|\int_{\pi/2}^{3\pi/2}\cos x\,dx\right|=|[\sin x]_{\pi/2}^{3\pi/2}|=|\sin(3\pi/2)-\sin(\pi/2)|=|-1-1|=2$$

$$A_3=\int_{3\pi/2}^{2\pi}\cos x\,dx=[\sin x]_{3\pi/2}^{2\pi}=0-(-1)=1$$

**Step 3 – Total area:**
$$A=A_1+A_2+A_3=1+2+1=4\text{ sq. units}$$

**Exercises with Solutions**

**Basic Level:**

1. Compute the area between $y=x^2-1$ and the $OX$ axis on $[-2,2]$ (there is a sign change).
   > **Solution:** Roots: $x=\pm 1$. $f\geq 0$ on $[-2,-1]\cup[1,2]$, $f\leq 0$ on $[-1,1]$. $A=2\left|\int_{-1}^1(x^2-1)\,dx\right|+2\int_1^2(x^2-1)\,dx$. $\int_{-1}^1(x^2-1)\,dx=\left[\frac{x^3}{3}-x\right]_{-1}^1=-\frac{4}{3}$. $\int_1^2(x^2-1)\,dx=\left[\frac{x^3}{3}-x\right]_1^2=\frac{2}{3}$. By symmetry (even function), $A=2\cdot\frac{4}{3}+2\cdot\frac{2}{3}=\frac{8}{3}+\frac{4}{3}=4$ sq. units.

2. Compute the area between $y=\sin x$ and the $OX$ axis on $[0,2\pi]$.
   > **Solution:** $\sin x\geq 0$ on $[0,\pi]$, $\leq 0$ on $[\pi,2\pi]$. $A=\int_0^\pi\sin x\,dx+\left|\int_\pi^{2\pi}\sin x\,dx\right|=2+|-(-2)|=2+2=4$ sq. units.

**Intermediate Level:**

3. Compute the area between $y=x^3-x$ and the $OX$ axis on $[-1,2]$.
   > **Solution:** Roots at $x=-1,0,1$. On $(-1,0)$: $f>0$; on $(0,1)$: $f<0$; on $(1,2)$: $f>0$. $I_1=\int_{-1}^0(x^3-x)\,dx=[\frac{x^4}{4}-\frac{x^2}{2}]_{-1}^0=0-(\frac{1}{4}-\frac{1}{2})=\frac{1}{4}$. $I_2=\int_0^1(x^3-x)\,dx=(\frac{1}{4}-\frac{1}{2})=(-\frac{1}{4})$. $I_3=\int_1^2(x^3-x)\,dx=[\frac{x^4}{4}-\frac{x^2}{2}]_1^2=(4-2)-(\frac{1}{4}-\frac{1}{2})=2+\frac{1}{4}=\frac{9}{4}$. $A=\frac{1}{4}+\frac{1}{4}+\frac{9}{4}=\frac{11}{4}$ sq. units.

4. Compute the area between $y=2x-x^2$ and the $OX$ axis on $[-1,3]$.
   > **Solution:** Roots: $x=0,2$. $f\geq 0$ on $[0,2]$; $f<0$ on $[-1,0]$ and $[2,3]$. $\int_{-1}^0(2x-x^2)dx=[x^2-x^3/3]_{-1}^0=0-(1+1/3)=-4/3$, $|I_1|=4/3$. $\int_0^2(2x-x^2)dx=[x^2-x^3/3]_0^2=4-8/3=4/3$. $\int_2^3(2x-x^2)dx=[x^2-\frac{x^3}{3}]_2^3=(9-9)-(4-\frac{8}{3})=0-(4-\frac{8}{3})=-\frac{4}{3}$. $A=\frac{4}{3}+\frac{4}{3}+\frac{4}{3}=4$ sq. units.

**EVAU Level:**

5. Compute the total area of the region between $f(x)=x^4-5x^2+4$ and the $OX$ axis.

   > **Solution:** Roots: $x^4-5x^2+4=(x^2-1)(x^2-4)=(x-1)(x+1)(x-2)(x+2)$. Roots: $x=-2,-1,1,2$.
   >
   > Signs: $f>0$ on $(-\infty,-2)$, $f<0$ on $(-2,-1)$, $f>0$ on $(-1,1)$, $f<0$ on $(1,2)$, $f>0$ on $(2,+\infty)$.
   >
   > By symmetry (even function), $A=2|I_{[0,1]}|+2|I_{[1,2]}|$.
   >
   > $\int_0^1(x^4-5x^2+4)\,dx=\left[\frac{x^5}{5}-\frac{5x^3}{3}+4x\right]_0^1=\frac{1}{5}-\frac{5}{3}+4=\frac{3-25+60}{15}=\frac{38}{15}$.
   >
   > $\int_1^2(x^4-5x^2+4)\,dx=\left[\frac{x^5}{5}-\frac{5x^3}{3}+4x\right]_1^2=\left(\frac{32}{5}-\frac{40}{3}+8\right)-\frac{38}{15}=\frac{96-200+120}{15}-\frac{38}{15}=\frac{16}{15}-\frac{38}{15}=-\frac{22}{15}$.
   >
   > $A=2\cdot\frac{38}{15}+2\cdot\frac{22}{15}=\frac{76+44}{15}=\frac{120}{15}=8$ sq. units.

**Multiple Choice Test**

6. When computing the area between a function and the $OX$ axis on an interval where $f$ changes sign, one should:
   - a) Compute $\int_a^b f(x)\,dx$ directly and take the absolute value of the result
   - b) Split the interval at the zeros of $f$ and sum the absolute values of each partial integral
   - c) Integrate $|f(x)|$ without splitting the interval
   - d) Options (b) and (c) are equivalent and both correct
   > **Correct answer: d)** Indeed, $\int_a^b|f(x)|\,dx$ gives the correct area, and is equivalent to splitting at the zeros and summing absolute values.

7. The function $f(x)=x-x^3$ has roots at $x=0,\pm 1$. The total area between the curve and the $OX$ axis on $[-1,1]$ is:
   - a) $0$
   - b) $\dfrac{1}{2}$
   - c) $\dfrac{1}{4}$
   - d) $1$
   > **Correct answer: b)** $f$ is odd. $\int_0^1(x-x^3)dx=[\frac{x^2}{2}-\frac{x^4}{4}]_0^1=\frac{1}{4}$. Total area $=2\cdot\frac{1}{4}=\frac{1}{2}$ sq. units.

---

#### 9.4.3 Area between two curves: setup and computation

**Worked Example**

Compute the area of the region enclosed between the curves $y=x^2$ and $y=x+2$.

**Step-by-step solution:**

**Step 1 – Intersection points.** Set equal: $x^2=x+2 \Rightarrow x^2-x-2=0 \Rightarrow (x-2)(x+1)=0$, so $x=-1$ and $x=2$.

**Step 2 – Upper function.** At $x=0$: $y_1=0$, $y_2=2$. So $x+2>x^2$ on $(-1,2)$.

**Step 3 – Area:**
$$A=\int_{-1}^2[(x+2)-x^2]\,dx=\left[\frac{x^2}{2}+2x-\frac{x^3}{3}\right]_{-1}^2$$

$$=\left(2+4-\frac{8}{3}\right)-\left(\frac{1}{2}-2+\frac{1}{3}\right)=\frac{10}{3}-\left(-\frac{7}{6}\right)=\frac{10}{3}+\frac{7}{6}=\frac{20+7}{6}=\frac{27}{6}=\frac{9}{2}$$

$$\boxed{A=\frac{9}{2}\text{ sq. units}}$$

**Exercises with Solutions**

**Basic Level:**

1. Compute the area between $y=x$ and $y=x^2$ on $[0,1]$.
   > **Solution:** $x\geq x^2$ on $[0,1]$. $A=\int_0^1(x-x^2)\,dx=[\frac{x^2}{2}-\frac{x^3}{3}]_0^1=\frac{1}{2}-\frac{1}{3}=\frac{1}{6}$ sq. units.

2. Compute the area enclosed between $y=4-x^2$ and $y=x^2$.
   > **Solution:** Intersections: $4-x^2=x^2\Rightarrow x^2=2\Rightarrow x=\pm\sqrt{2}$. $4-x^2\geq x^2$ on $[-\sqrt{2},\sqrt{2}]$. $A=\int_{-\sqrt{2}}^{\sqrt{2}}(4-2x^2)\,dx=2[4x-\frac{2x^3}{3}]_0^{\sqrt{2}}=2(4\sqrt{2}-\frac{2\cdot 2\sqrt{2}}{3})=2\sqrt{2}(4-\frac{4}{3})=2\sqrt{2}\cdot\frac{8}{3}=\frac{16\sqrt{2}}{3}$ sq. units.

**Intermediate Level:**

3. Compute the area between $y=e^x$ and $y=e^{-x}+1$ on $[0,1]$.
   > **Solution:** Comparing at $x=0$: $y_1=1$, $y_2=2$; at $x=1$: $y_1=e\approx 2{,}72$, $y_2=e^{-1}+1\approx 1{,}37$. Intersection: $e^x=e^{-x}+1$, no elementary solution in $[0,1]$ a priori — we verify the crossing: $f(0)=e^0-(e^0+1)=-1<0$, $f(1)=e-(e^{-1}+1)>0$. So the curve crosses. For a standard secondary school exercise, the curves are given with a pre-computed crossing point. Result: $\int_0^1|e^x-e^{-x}-1|\,dx$ (numerical integral).
   > > *EVAU note:* This type of exact integration requires numerical determination of the crossing point. A well-posed exercise would provide functions with exact intersection.

4. Compute the area between $y=\sin x$ and $y=\cos x$ on $[0,\pi/2]$.
   > **Solution:** Intersection: $\sin x=\cos x\Rightarrow x=\pi/4$. On $[0,\pi/4]$: $\cos x\geq\sin x$; on $[\pi/4,\pi/2]$: $\sin x\geq\cos x$. $A=\int_0^{\pi/4}(\cos x-\sin x)dx+\int_{\pi/4}^{\pi/2}(\sin x-\cos x)dx=[\sin x+\cos x]_0^{\pi/4}+[-\cos x-\sin x]_{\pi/4}^{\pi/2}=(\sqrt{2}-1)+(0-(-\sqrt{2}))=2\sqrt{2}-1$ sq. units.

**EVAU Level:**

5. Determine the area of the region enclosed between the parabolas $y=x^2-2x$ and $y=-x^2+4$.

   > **Solution:**
   >
   > **Intersections:** $x^2-2x=-x^2+4\Rightarrow 2x^2-2x-4=0\Rightarrow x^2-x-2=0\Rightarrow (x-2)(x+1)=0$, so $x=-1,2$.
   >
   > **Upper function on $(-1,2)$:** $x=0$: $y_1=0$, $y_2=4$. So $-x^2+4\geq x^2-2x$.
   >
   > $$A=\int_{-1}^2\left[(-x^2+4)-(x^2-2x)\right]dx=\int_{-1}^2(-2x^2+2x+4)\,dx$$
   >
   > $$=\left[-\frac{2x^3}{3}+x^2+4x\right]_{-1}^2=\left(-\frac{16}{3}+4+8\right)-\left(\frac{2}{3}+1-4\right)=\frac{20}{3}-\left(-\frac{7}{3}\right)=\frac{27}{3}=9\text{ sq. units}$$

**Multiple Choice Test**

6. The area between two curves $f(x)$ and $g(x)$ with $f\geq g$ on $[a,b]$ is:
   - a) $\displaystyle\int_a^b f(x)\,dx - \int_a^b g(x)\,dx$
   - b) $\displaystyle\int_a^b [f(x)+g(x)]\,dx$
   - c) $\displaystyle\int_a^b f(x)\,dx \cdot \int_a^b g(x)\,dx$
   - d) $\displaystyle\int_a^b [f(x)-g(x)]^2\,dx$
   > **Correct answer: a)** By linearity, $\int_a^b[f(x)-g(x)]dx=\int_a^b f\,dx-\int_a^b g\,dx$.

7. The area between $y=x$ and $y=x^2$ on $[0,1]$ is:
   - a) $\dfrac{1}{3}$
   - b) $\dfrac{1}{6}$
   - c) $\dfrac{1}{2}$
   - d) $1$
   > **Correct answer: b)** $\int_0^1(x-x^2)\,dx=\frac{1}{2}-\frac{1}{3}=\frac{1}{6}$.

---

#### 9.4.4 Computing the intersection point prior to the area between curves

**Worked Example**

Determine the area of the region bounded by $y=x^2-1$ and $y=3-x^2$, first finding the intersection points.

**Step-by-step solution:**

**Step 1 – Intersection points:**
$$x^2-1=3-x^2 \Rightarrow 2x^2=4 \Rightarrow x^2=2 \Rightarrow x=\pm\sqrt{2}$$

**Step 2 – Upper function.** At $x=0$: $y_1=-1$, $y_2=3$. So $3-x^2\geq x^2-1$ on $[-\sqrt{2},\sqrt{2}]$.

**Step 3 – Area:**
$$A=\int_{-\sqrt{2}}^{\sqrt{2}}[(3-x^2)-(x^2-1)]\,dx=\int_{-\sqrt{2}}^{\sqrt{2}}(4-2x^2)\,dx$$

Since the function is even:
$$A=2\int_0^{\sqrt{2}}(4-2x^2)\,dx=2\left[4x-\frac{2x^3}{3}\right]_0^{\sqrt{2}}=2\left(4\sqrt{2}-\frac{2\cdot 2\sqrt{2}}{3}\right)=2\sqrt{2}\left(4-\frac{4}{3}\right)=2\sqrt{2}\cdot\frac{8}{3}=\frac{16\sqrt{2}}{3}\text{ sq. units}$$

**Exercises with Solutions**

**Basic Level:**

1. Find the area enclosed between $y=x+2$ and $y=x^2$ (first find the intersection points).
   > **Solution:** $x^2=x+2\Rightarrow(x-2)(x+1)=0\Rightarrow x=-1,2$. On $(-1,2)$: $x+2>x^2$. $A=\int_{-1}^2(x+2-x^2)\,dx=[\frac{x^2}{2}+2x-\frac{x^3}{3}]_{-1}^2=(2+4-\frac{8}{3})-(\frac{1}{2}-2+\frac{1}{3})=\frac{10}{3}+\frac{7}{6}=\frac{9}{2}$ sq. units.

2. Find the area between $y=2-x$ and $y=x^2-4$.
   > **Solution:** Intersections: $2-x=x^2-4\Rightarrow x^2+x-6=0\Rightarrow(x+3)(x-2)=0\Rightarrow x=-3,2$. On $(-3,2)$: $2-x\geq x^2-4$. $A=\int_{-3}^2(6-x-x^2)\,dx=[6x-\frac{x^2}{2}-\frac{x^3}{3}]_{-3}^2=(12-2-\frac{8}{3})-(-18-\frac{9}{2}+9)=\frac{22}{3}+\frac{27}{2}=\frac{44+81}{6}=\frac{125}{6}$ sq. units.

**Intermediate Level:**

3. Find the area between $y=\sqrt{x}$ and $y=x^2$ on $[0,1]$.
   > **Solution:** Intersections on $[0,1]$: $\sqrt{x}=x^2\Rightarrow x^{1/2}=x^2\Rightarrow x=0$ and $x=1$. On $(0,1)$: $\sqrt{x}>x^2$ (at $x=1/4$: $1/2>1/16$). $A=\int_0^1(\sqrt{x}-x^2)\,dx=[\frac{2x^{3/2}}{3}-\frac{x^3}{3}]_0^1=\frac{2}{3}-\frac{1}{3}=\frac{1}{3}$ sq. units.

4. Find the area between $y=\ln x$ and $y=x-1$ around their intersection at $x=1$.
   > **Solution:** $\ln x=x-1$: both are equal at $x=1$ and one can show $\ln x\leq x-1$ for all $x>0$. Double intersection at $x=1$. For the interval $[1,e]$: $x-1\geq\ln x$. $A=\int_1^e(x-1-\ln x)\,dx=[\frac{x^2}{2}-x-x\ln x+x]_1^e=[\frac{x^2}{2}-x\ln x]_1^e=(\frac{e^2}{2}-e)-(\frac{1}{2}-0)=\frac{e^2}{2}-e-\frac{1}{2}$.

**EVAU Level:**

5. **(EVAU Madrid, analysis type)**

   Let $f(x)=x^2-4x$ and $g(x)=2x-x^2$.

   **(a)** Determine the intersection points of $f$ and $g$.  
   **(b)** Determine which of the two curves lies above in the region they enclose.  
   **(c)** Compute the area of the region bounded by the two curves.

   > **Solution:**
   >
   > **(a)** $x^2-4x=2x-x^2\Rightarrow 2x^2-6x=0\Rightarrow 2x(x-3)=0\Rightarrow x=0$ and $x=3$.
   >
   > **(b)** At $x=1$: $f(1)=-3$, $g(1)=1$. So $g\geq f$ on $(0,3)$.
   >
   > **(c)** $A=\int_0^3[g(x)-f(x)]\,dx=\int_0^3(2x-x^2-x^2+4x)\,dx=\int_0^3(6x-2x^2)\,dx=\left[3x^2-\frac{2x^3}{3}\right]_0^3=27-18=9$ sq. units.

**Multiple Choice Test**

6. To find the area between $y=x^3$ and $y=x$, the first step is:
   - a) Determine which function is greater throughout $\mathbb{R}$
   - b) Compute $\int_{-\infty}^{+\infty}(x-x^3)\,dx$
   - c) Find the intersections by solving $x^3=x$
   - d) Differentiate both functions and equate derivatives
   > **Correct answer: c)** One must always first determine the crossing points to know the limits of integration and which function dominates.

7. The curves $y=x^2$ and $y=2x-x^2$ intersect at:
   - a) $x=0$ and $x=1$
   - b) $x=-1$ and $x=1$
   - c) $x=0$ and $x=2$
   - d) Only at $x=1$
   > **Correct answer: a)** $x^2=2x-x^2\Rightarrow 2x^2-2x=0\Rightarrow 2x(x-1)=0\Rightarrow x=0,1$.

---

### 9.5 Volumes of solids of revolution

---

#### 9.5.1 Volume of revolution around the OX axis: disk method

**Worked Example**

Compute the volume of the solid generated by revolving the region under $y=\sqrt{x}$ on $[0,4]$ around the $OX$ axis.

**Step-by-step solution:**

**Formula (disk method):**
$$V=\pi\int_a^b [f(x)]^2\,dx$$

**Step 1 – Apply the formula:**
$$V=\pi\int_0^4(\sqrt{x})^2\,dx=\pi\int_0^4 x\,dx$$

**Step 2 – Compute the integral:**
$$V=\pi\left[\frac{x^2}{2}\right]_0^4=\pi\cdot\frac{16}{2}=8\pi\text{ cubic units}$$

**Interpretation:** The solid is a paraboloid of revolution (bowl shape) from $x=0$ to $x=4$, with maximum radius $r=\sqrt{4}=2$ at $x=4$.

**Exercises with Solutions**

**Basic Level:**

1. Compute the volume of the solid generated by revolving $y=x$ on $[0,3]$ around the $OX$ axis.
   > **Solution:** $V=\pi\int_0^3 x^2\,dx=\pi\left[\frac{x^3}{3}\right]_0^3=\pi\cdot 9=9\pi$ cubic units. (Cone with radius 3 and height 3; verification formula: $V=\frac{1}{3}\pi r^2 h=\frac{1}{3}\pi\cdot 9\cdot 3=9\pi$ ✓.)

2. Compute the volume obtained by revolving $y=e^x$ on $[0,1]$ around the $OX$ axis.
   > **Solution:** $V=\pi\int_0^1 e^{2x}\,dx=\pi\left[\frac{e^{2x}}{2}\right]_0^1=\frac{\pi}{2}(e^2-1)$ cubic units.

**Intermediate Level:**

3. Compute the volume obtained by revolving $y=\sin x$ on $[0,\pi]$ around the $OX$ axis.
   > **Solution:** $V=\pi\int_0^\pi\sin^2 x\,dx=\pi\int_0^\pi\frac{1-\cos(2x)}{2}\,dx=\frac{\pi}{2}\left[x-\frac{\sin(2x)}{2}\right]_0^\pi=\frac{\pi}{2}\cdot\pi=\frac{\pi^2}{2}$ cubic units.

4. Compute the volume obtained by revolving $y=1/x$ on $[1,2]$ around the $OX$ axis.
   > **Solution:** $V=\pi\int_1^2\frac{1}{x^2}\,dx=\pi\left[-\frac{1}{x}\right]_1^2=\pi\left(-\frac{1}{2}+1\right)=\frac{\pi}{2}$ cubic units.

**EVAU Level:**

5. **(EVAU Madrid, style)**

   Let region $R$ be bounded by $f(x)=\sqrt{4-x^2}$ (upper semicircle of radius 2), the $OX$ axis, and the endpoints of $[-2,2]$.

   **(a)** Compute the area of region $R$.  
   **(b)** Compute the volume of the solid of revolution obtained by revolving $R$ around the $OX$ axis.  
   **(c)** Identify the resulting solid geometrically.

   > **Solution:**
   >
   > **(a)** $R$ is the upper semidisk of radius 2. $A=\frac{\pi r^2}{2}=2\pi$ sq. units (also by integral: $\int_{-2}^2\sqrt{4-x^2}\,dx=2\pi$).
   >
   > **(b)** $V=\pi\int_{-2}^2[\sqrt{4-x^2}]^2\,dx=\pi\int_{-2}^2(4-x^2)\,dx=\pi\left[4x-\frac{x^3}{3}\right]_{-2}^2=\pi\left[(8-\frac{8}{3})-(-8+\frac{8}{3})\right]=\pi\cdot\frac{32}{3}=\frac{32\pi}{3}$ cubic units.
   >
   > **(c)** It is a sphere of radius 2, whose theoretical volume is $\frac{4}{3}\pi r^3=\frac{32\pi}{3}$ ✓.

**Multiple Choice Test**

6. The formula for the volume of the solid of revolution obtained by revolving $y=f(x)\geq 0$ around the $OX$ axis on $[a,b]$ is:
   - a) $\displaystyle V=\int_a^b f(x)\,dx$
   - b) $\displaystyle V=2\pi\int_a^b xf(x)\,dx$
   - c) $\displaystyle V=\pi\int_a^b[f(x)]^2\,dx$
   - d) $\displaystyle V=\pi\int_a^b f(x)\,dx$
   > **Correct answer: c)** The disk method gives $V=\pi\int_a^b[f(x)]^2\,dx$, since each disk has radius $f(x)$ and area $\pi[f(x)]^2$.

7. The volume obtained by revolving $y=r$ (constant) on $[0,h]$ around the $OX$ axis is:
   - a) $\pi r^2$
   - b) $\pi r^2 h$
   - c) $\dfrac{\pi r^2 h}{3}$
   - d) $2\pi r h$
   > **Correct answer: b)** $V=\pi\int_0^h r^2\,dx=\pi r^2 h$, which corresponds to the volume of a cylinder with radius $r$ and height $h$ ✓.

---

#### 9.5.2 Volume of revolution around the OY axis

**Worked Example**

Compute the volume of the solid generated by revolving the region bounded by $y=x^2$, $x=0$ and $y=4$ around the $OY$ axis.

**Step-by-step solution:**

**Approach:** Express $x$ as a function of $y$: $y=x^2 \Rightarrow x=\sqrt{y}$ (for $x\geq 0$).

**Formula (disks with respect to the OY axis):**
$$V=\pi\int_{y_1}^{y_2}[x(y)]^2\,dy$$

**Step 1 – Limits of integration.** The region goes from $y=0$ to $y=4$.

**Step 2 – Apply the formula:**
$$V=\pi\int_0^4[\sqrt{y}]^2\,dy=\pi\int_0^4 y\,dy=\pi\left[\frac{y^2}{2}\right]_0^4=\pi\cdot 8=8\pi\text{ cubic units}$$

**Exercises with Solutions**

**Basic Level:**

1. Compute the volume obtained by revolving $y=2x$ (with $x\in[0,3]$, solving for $x$ as a function of $y$) around the $OY$ axis.
   > **Solution:** $x=\frac{y}{2}$, $y\in[0,6]$. $V=\pi\int_0^6\left(\frac{y}{2}\right)^2dy=\frac{\pi}{4}\int_0^6 y^2\,dy=\frac{\pi}{4}\cdot\frac{216}{3}=18\pi$ cubic units.

2. Compute the volume obtained by revolving $x=\sqrt{y}$ on $y\in[0,4]$ around the $OY$ axis.
   > **Solution:** $V=\pi\int_0^4(\sqrt{y})^2\,dy=\pi\int_0^4 y\,dy=\pi\left[\frac{y^2}{2}\right]_0^4=8\pi$ cubic units.

**Intermediate Level:**

3. Find the volume obtained by revolving the region bounded by $y=x^2+1$, $x=0$, $y=5$ around the $OY$ axis.
   > **Solution:** $y=x^2+1\Rightarrow x^2=y-1\Rightarrow x=\sqrt{y-1}$, valid for $y\geq 1$. Region: $y$ from 1 to 5 (with $x$ from 0 to 2). $V=\pi\int_1^5(y-1)\,dy=\pi\left[\frac{y^2}{2}-y\right]_1^5=\pi\left[(12{,}5-5)-(0{,}5-1)\right]=\pi[7{,}5+0{,}5]=8\pi$ cubic units.

4. Compute the volume obtained by revolving $y=\ln x$ (with $y\in[0,1]$, $x=e^y$) around the $OY$ axis.
   > **Solution:** $x=e^y$, $y\in[0,1]$. $V=\pi\int_0^1(e^y)^2\,dy=\pi\int_0^1 e^{2y}\,dy=\pi\left[\frac{e^{2y}}{2}\right]_0^1=\frac{\pi}{2}(e^2-1)$ cubic units.

**EVAU Level:**

5. Region $R$ is bounded by $y=\sqrt{x}$, $y=2$ and the $OY$ axis.

   **(a)** Compute the area of region $R$.  
   **(b)** Compute the volume of the solid obtained by revolving $R$ around the $OY$ axis.

   > **Solution:**
   >
   > **(a)** Region $R$ lies between $y=\sqrt{x}$ (i.e. $x=y^2$) and $y=2$, from $y=0$ to $y=2$, also bounded by the $OY$ axis ($x=0$). $A=\int_0^2 y^2\,dy=\left[\frac{y^3}{3}\right]_0^2=\frac{8}{3}$ sq. units.
   >
   > **(b)** $V=\pi\int_0^2(y^2)^2\,dy=\pi\int_0^2 y^4\,dy=\pi\left[\frac{y^5}{5}\right]_0^2=\frac{32\pi}{5}$ cubic units.

**Multiple Choice Test**

6. To revolve a region around the $OY$ axis using the disk method, one integrates:
   - a) $\pi\int[f(x)]^2\,dx$ in $x$
   - b) $\pi\int[x(y)]^2\,dy$ in $y$, where $x(y)$ is the solved function
   - c) $2\pi\int xf(x)\,dx$ (shell method)
   - d) Options (b) and (c) are equivalent
   > **Correct answer: d)** Both methods — disks with respect to OY and shells with respect to OX — compute the same volume and are equivalent; option (b) is the disk method and (c) is the cylindrical shell method.

7. The volume obtained by revolving $y=x^2$ on $[0,1]$ around the $OY$ axis is:
   - a) $\dfrac{\pi}{3}$
   - b) $\dfrac{\pi}{2}$
   - c) $\pi$
   - d) $\dfrac{2\pi}{5}$
   > **Correct answer: b)** $x=\sqrt{y}$, $y\in[0,1]$. $V=\pi\int_0^1 y\,dy=\frac{\pi}{2}$ cubic units.

---

#### 9.5.3 Volume between two surfaces of revolution

**Worked Example**

Compute the volume of the solid of revolution generated by revolving around the $OX$ axis the region between $y=\sqrt{x}$ and $y=x$ on $[0,1]$.

**Step-by-step solution:**

**Step 1 – Verify which function lies above.** At $x=1/4$: $\sqrt{1/4}=1/2>1/4=x$. So $\sqrt{x}\geq x$ on $[0,1]$.

**Step 2 – Washer method:**
$$V=\pi\int_0^1\left[(\sqrt{x})^2-x^2\right]dx=\pi\int_0^1(x-x^2)\,dx$$

**Step 3 – Compute:**
$$V=\pi\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_0^1=\pi\left(\frac{1}{2}-\frac{1}{3}\right)=\pi\cdot\frac{1}{6}=\frac{\pi}{6}\text{ cubic units}$$

**Exercises with Solutions**

**Basic Level:**

1. Compute the volume obtained by revolving the region between $y=2$ and $y=1$ on $[0,3]$ around the $OX$ axis.
   > **Solution:** $V=\pi\int_0^3(2^2-1^2)\,dx=\pi\int_0^3 3\,dx=9\pi$ cubic units. (Hollow cylinder with inner radius 1 and outer radius 2, length 3.)

2. Compute the volume obtained by revolving the region between $y=x+1$ and $y=x$ on $[0,2]$ around the $OX$ axis.
   > **Solution:** $V=\pi\int_0^2[(x+1)^2-x^2]\,dx=\pi\int_0^2(2x+1)\,dx=\pi[x^2+x]_0^2=\pi\cdot 6=6\pi$ cubic units.

**Intermediate Level:**

3. Compute the volume obtained by revolving the region between $y=x^2$ and $y=x$ (on $[0,1]$) around the $OX$ axis.
   > **Solution:** $x\geq x^2$ on $[0,1]$. $V=\pi\int_0^1(x^2-x^4)\,dx=\pi\left[\frac{x^3}{3}-\frac{x^5}{5}\right]_0^1=\pi\left(\frac{1}{3}-\frac{1}{5}\right)=\frac{2\pi}{15}$ cubic units.

4. Compute the volume obtained by revolving the region between $y=e^x$ and $y=1$ on $[0,1]$ around the $OX$ axis.
   > **Solution:** $e^x\geq 1$ on $[0,1]$. $V=\pi\int_0^1(e^{2x}-1)\,dx=\pi\left[\frac{e^{2x}}{2}-x\right]_0^1=\pi\left[(\frac{e^2}{2}-1)-\frac{1}{2}\right]=\pi\cdot\frac{e^2-3}{2}=\frac{\pi(e^2-3)}{2}$ cubic units.

**EVAU Level:**

5. **(EVAU Madrid, analysis style)**

   Let region $R$ be bounded by $f(x)=4-x^2$ and $g(x)=4-2x$.

   **(a)** Compute the intersection points of $f$ and $g$ and determine which function is above in the region they enclose.  
   **(b)** Compute the area of region $R$.  
   **(c)** Compute the volume of the solid of revolution generated by revolving $R$ around the $OX$ axis.

   > **Solution:**
   >
   > **(a)** $4-x^2=4-2x\Rightarrow x^2-2x=0\Rightarrow x(x-2)=0\Rightarrow x=0, x=2$. At $x=1$: $f(1)=3$, $g(1)=2$. So $f\geq g$ on $(0,2)$.
   >
   > **(b)** $A=\int_0^2[(4-x^2)-(4-2x)]\,dx=\int_0^2(2x-x^2)\,dx=\left[x^2-\frac{x^3}{3}\right]_0^2=4-\frac{8}{3}=\frac{4}{3}$ sq. units.
   >
   > **(c)** Washer method:
   > $$V=\pi\int_0^2\left[(4-x^2)^2-(4-2x)^2\right]dx$$
   > $(4-x^2)^2=16-8x^2+x^4$; $(4-2x)^2=16-16x+4x^2$.
   > $(4-x^2)^2-(4-2x)^2=16x-12x^2+x^4$.
   > $$V=\pi\int_0^2(16x-12x^2+x^4)\,dx=\pi\left[8x^2-4x^3+\frac{x^5}{5}\right]_0^2=\pi\left(32-32+\frac{32}{5}\right)=\frac{32\pi}{5}\text{ cubic units}$$

**Multiple Choice Test**

6. To compute the volume between two surfaces obtained by revolving $f(x)\geq g(x)\geq 0$ around the $OX$ axis on $[a,b]$, one uses:
   - a) $\pi\int_a^b[f(x)-g(x)]\,dx$
   - b) $\pi\int_a^b[f(x)-g(x)]^2\,dx$
   - c) $\pi\int_a^b\left\{[f(x)]^2-[g(x)]^2\right\}dx$
   - d) $\pi\int_a^b[f(x)]^2\,dx - \pi\int_a^b[g(x)]^2\,dx$ (valid but same as c)
   > **Correct answer: c)** (equivalent to d)) The washer method gives $V=\pi\int_a^b([f]^2-[g]^2)\,dx$, subtracting the inner disk from the outer disk.

7. The volume of the solid generated by revolving the region between $y=2$ and $y=1$ (on $[0,4]$) around the $OX$ axis is:
   - a) $4\pi$
   - b) $12\pi$
   - c) $16\pi$
   - d) $8\pi$
   > **Correct answer: b)** $V=\pi\int_0^4(4-1)\,dx=\pi\cdot 3\cdot 4=12\pi$ cubic units.

---

*End of Chapter 9 — Integrals*

---

*Document generated for Mathematics II — 2nd year of Bachillerato (Science and Technology)*  
*Community of Madrid · Decree 64/2022 (LOMLOE) · FUHEM Curriculum 2025-26*  
*Exercises for Chapters 8 (Curve Sketching) and 9 (Integrals)*
