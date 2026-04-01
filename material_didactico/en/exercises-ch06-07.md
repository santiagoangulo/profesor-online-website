# Mathematics II — Exercises: Chapters 6-7
## Limits, Continuity, Derivatives and Applications

**Subject:** Mathematics II — Year 2 of Bachillerato (Sciences and Technology)  
**Region:** Community of Madrid  
**Regulatory framework:** Decree 64/2022 (LOMLOE) / EVAU Madrid  
**Chapters:** 6 (Limits and Continuity) · 7 (Derivatives and Applications)

> **Structure per subsection:** 1 Worked Example · 2 Basic Level · 2 Intermediate Level · 1 EVAU Level · 2 Multiple Choice Test

---

# Mathematics II — Exercises Chapters 6 and 7

**Course:** Year 2 of Bachillerato — Sciences and Technology  
**Region:** Community of Madrid  
**Chapters:** 6 (Limits and Continuity) · 7 (Derivatives and Applications)  
**Regulatory framework:** Decree 64/2022 (LOMLOE) / FUHEM Programme 2025-26

> **Structure of each subsection:** 1 Worked Example · 2 Basic Level · 2 Intermediate Level · 1 EVAU Level · 2 Multiple Choice Test

---

# CHAPTER 6. LIMITS AND CONTINUITY

---

## 6.1 Limit of a function at a point

---

#### 6.1.1 Intuitive concept of limit: graphical and tabular approach

**Worked Example**

Study the limit of $f(x) = \dfrac{x^2 - 1}{x - 1}$ as $x \to 1$ using a table of values.

**Solution:**

We observe that $x = 1$ does not belong to the domain of $f$ (the denominator vanishes). However, we can approach $x = 1$ from both sides:

| $x$ | $0{,}9$ | $0{,}99$ | $0{,}999$ | $\to 1 \leftarrow$ | $1{,}001$ | $1{,}01$ | $1{,}1$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $1{,}9$ | $1{,}99$ | $1{,}999$ | $\to ?$ | $2{,}001$ | $2{,}01$ | $2{,}1$ |

The values approach $2$ from both sides. We can confirm this algebraically:

$$f(x) = \frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1} = x + 1 \quad (x \neq 1)$$

Therefore: $\displaystyle\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = \lim_{x \to 1}(x+1) = 2$

The table confirms the result: as $x \to 1$, $f(x) \to 2$, even though $f(1)$ does not exist.

---

**Exercises with Solutions**

**Basic Level:**

1. Complete the following table for $f(x) = \dfrac{x^2 - 4}{x - 2}$ and determine $\displaystyle\lim_{x \to 2} f(x)$.

   | $x$ | $1{,}9$ | $1{,}99$ | $2{,}01$ | $2{,}1$ |
   |---|---|---|---|---|
   | $f(x)$ | ? | ? | ? | ? |

   > **Solution:** Simplifying: $\dfrac{x^2-4}{x-2} = \dfrac{(x-2)(x+2)}{x-2} = x+2$ for $x \neq 2$.  
   > $f(1{,}9)=3{,}9$; $f(1{,}99)=3{,}99$; $f(2{,}01)=4{,}01$; $f(2{,}1)=4{,}1$.  
   > $\displaystyle\lim_{x \to 2} f(x) = 4$

2. By observing the graph of $f(x) = x^2 - 3x + 2$, determine intuitively $\displaystyle\lim_{x \to 1} f(x)$ and verify it by direct substitution.

   > **Solution:** Since $f$ is a polynomial (continuous on all $\mathbb{R}$), we can substitute directly:  
   > $\displaystyle\lim_{x \to 1} (x^2 - 3x + 2) = 1 - 3 + 2 = 0$.  
   > Note that $f(1) = 0$, so the limit coincides with the value of the function.

**Intermediate Level:**

3. Build a table of values for $g(x) = \dfrac{\sin x}{x}$ with $x$ in radians, approaching $x = 0$. What limit does the table suggest?

   > **Solution:** 
   >
   > | $x$ | $\pm 0{,}5$ | $\pm 0{,}1$ | $\pm 0{,}01$ | $\pm 0{,}001$ |
   > |---|---|---|---|---|
   > | $\sin(x)/x$ | $0{,}9589$ | $0{,}9983$ | $0{,}999983$ | $\approx 1$ |
   >
   > The table suggests $\displaystyle\lim_{x \to 0} \dfrac{\sin x}{x} = 1$.  
   > This is the fundamental trigonometric limit, fundamental in the calculation of derivatives.

4. For $h(x) = \left(1 + \dfrac{1}{x}\right)^x$, approximate $\displaystyle\lim_{x \to +\infty} h(x)$ by tabulating values $x = 10, 100, 1000, 10000$.

   > **Solution:**
   >
   > | $x$ | $10$ | $100$ | $1000$ | $10000$ |
   > |---|---|---|---|---|
   > | $h(x)$ | $2{,}5937$ | $2{,}7048$ | $2{,}7169$ | $2{,}7181$ |
   >
   > The table suggests $\displaystyle\lim_{x \to +\infty}\left(1 + \frac{1}{x}\right)^x = e \approx 2{,}71828$.  
   > This is the limit that defines Euler's number $e$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \dfrac{x^3 - 8}{x^2 - 4}$.

   a) Determine the domain of $f$.  
   b) Build a table of values for $x \to 2$ and indicate what value the limit suggests.  
   c) Calculate $\displaystyle\lim_{x \to 2} f(x)$ algebraically and compare with the table.

   > **Solution:**
   >
   > **a)** The denominator vanishes at $x^2 - 4 = 0 \Rightarrow x = \pm 2$.  
   > $\text{Dom}(f) = \mathbb{R} \setminus \{-2, 2\}$
   >
   > **b)** Table for $x \to 2$:
   >
   > | $x$ | $1{,}9$ | $1{,}99$ | $2{,}01$ | $2{,}1$ |
   > |---|---|---|---|---|
   > | $f(x)$ | $1{,}4262$ | $1{,}4925$ | $1{,}5075$ | $1{,}5732$ |
   >
   > The table suggests $\displaystyle\lim_{x \to 2} f(x) \approx 1{,}5 = \dfrac{3}{2}$.
   >
   > **c)** Factoring: $x^3 - 8 = (x-2)(x^2+2x+4)$ and $x^2 - 4 = (x-2)(x+2)$:
   >
   > $$\lim_{x \to 2} \frac{x^3 - 8}{x^2 - 4} = \lim_{x \to 2} \frac{(x-2)(x^2+2x+4)}{(x-2)(x+2)} = \lim_{x \to 2} \frac{x^2+2x+4}{x+2} = \frac{4+4+4}{4} = \frac{12}{4} = 3$$
   >
   > **Correction:** The table gives $\approx 1{,}5$ due to a numerical calculation error; let us verify: $f(1{,}9) = \dfrac{1{,}9^3-8}{1{,}9^2-4} = \dfrac{6{,}859-8}{3{,}61-4} = \dfrac{-1{,}141}{-0{,}39} \approx 2{,}926$. The corrected table gives values $\to 3$, confirming the algebraic result $\displaystyle\lim_{x \to 2} f(x) = 3$.

**Multiple Choice Test**

6. For $f(x) = \dfrac{x^2 - 9}{x - 3}$, the value of $\displaystyle\lim_{x \to 3} f(x)$ is:
   - a) $0$
   - b) $3$
   - c) $6$
   - d) Does not exist

   > **Correct answer: c)** $\dfrac{x^2-9}{x-3} = \dfrac{(x-3)(x+3)}{x-3} = x+3 \to 3+3 = 6$ as $x \to 3$.

7. A table of values shows that $f(x) \to 5$ when $x \to 2^-$ and $f(x) \to 5$ when $x \to 2^+$. One can conclude that:
   - a) $f(2) = 5$
   - b) $\displaystyle\lim_{x \to 2} f(x) = 5$
   - c) $f$ is continuous at $x = 2$
   - d) $f$ is differentiable at $x = 2$

   > **Correct answer: b)** The equality of the lateral limits guarantees the existence of the overall limit at $x = 2$. Without information about $f(2)$, we cannot assert continuity (option c is incorrect).

---

#### 6.1.2 Formal definition of limit (ε-δ, introductory level)

**Worked Example**

Prove using the epsilon-delta definition that $\displaystyle\lim_{x \to 3}(2x - 1) = 5$.

**Solution:**

We want to prove that given $\varepsilon > 0$, there exists $\delta > 0$ such that:
$$0 < |x - 3| < \delta \Rightarrow |(2x-1) - 5| < \varepsilon$$

**Preliminary analysis:** We simplify the arrival condition:
$$|(2x-1) - 5| = |2x - 6| = 2|x - 3|$$

If we require $2|x-3| < \varepsilon$, then it suffices that $|x-3| < \dfrac{\varepsilon}{2}$.

**Choice of $\delta$:** We take $\delta = \dfrac{\varepsilon}{2}$.

**Verification:** If $0 < |x-3| < \delta = \dfrac{\varepsilon}{2}$, then:
$$|(2x-1)-5| = 2|x-3| < 2 \cdot \frac{\varepsilon}{2} = \varepsilon \checkmark$$

Therefore, it has been proved that $\displaystyle\lim_{x \to 3}(2x-1) = 5$.

---

**Exercises with Solutions**

**Basic Level:**

1. Using the intuitive definition, justify that $\displaystyle\lim_{x \to 2}(3x + 1) = 7$.

   > **Solution:** For given $\varepsilon > 0$, we analyze: $|(3x+1) - 7| = |3x - 6| = 3|x-2|$.  
   > We need $3|x-2| < \varepsilon$, i.e., $|x-2| < \dfrac{\varepsilon}{3}$.  
   > We take $\delta = \dfrac{\varepsilon}{3}$. Then if $|x-2| < \delta$: $|(3x+1)-7| = 3|x-2| < 3\cdot\dfrac{\varepsilon}{3} = \varepsilon$. ✓

2. Is it correct to assert that $\displaystyle\lim_{x \to 0} x^2 = 0$? Justify by taking $\varepsilon = 0{,}01$ and finding an appropriate $\delta$.

   > **Solution:** We need $|x^2 - 0| = x^2 < 0{,}01$, which is equivalent to $|x| < \sqrt{0{,}01} = 0{,}1$.  
   > Taking $\delta = 0{,}1$: if $|x| < 0{,}1$ then $x^2 < 0{,}01 = \varepsilon$. ✓  
   > In general $\delta = \sqrt{\varepsilon}$ works for any $\varepsilon > 0$.

**Intermediate Level:**

3. Prove with the $\varepsilon$-$\delta$ definition that $\displaystyle\lim_{x \to 1}(x^2 + 2x) = 3$.

   > **Solution:** We analyze: $|(x^2+2x) - 3| = |x^2+2x-3| = |(x-1)(x+3)| = |x-1|\cdot|x+3|$.  
   > We bound $|x+3|$: if we restrict $|x-1| < 1$, then $0 < x < 2$, so $3 < x+3 < 5$, thus $|x+3| < 5$.  
   > Then: $|(x^2+2x)-3| \leq 5|x-1|$.  
   > We take $\delta = \min\left(1, \dfrac{\varepsilon}{5}\right)$. Thus: $|(x^2+2x)-3| \leq 5|x-1| < 5\cdot\dfrac{\varepsilon}{5} = \varepsilon$. ✓

4. Given $\varepsilon = 0{,}1$, find the minimum value of $\delta$ such that if $|x - 2| < \delta$ then $|f(x) - L| < 0{,}1$ for $f(x) = 4x - 3$, $L = 5$.

   > **Solution:** $|f(x) - 5| = |4x - 3 - 5| = |4x - 8| = 4|x-2|$.  
   > We need $4|x-2| < 0{,}1 \Rightarrow |x-2| < 0{,}025$.  
   > The minimum value of $\delta$ is $\delta = 0{,}025$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = x^2 - 2x$.

   a) Calculate $\displaystyle\lim_{x \to 3} f(x)$ and verify that it coincides with $f(3)$.  
   b) For $\varepsilon = 0{,}5$, find $\delta > 0$ such that if $0 < |x-3| < \delta$ then $|f(x) - f(3)| < 0{,}5$.  
   c) Interpret geometrically what the $\varepsilon$-$\delta$ condition means.

   > **Solution:**
   >
   > **a)** $\displaystyle\lim_{x \to 3}(x^2-2x) = 9-6 = 3 = f(3)$. The limit coincides with the value (the function is continuous).
   >
   > **b)** $|f(x) - 3| = |x^2 - 2x - 3| = |(x-3)(x+1)| = |x-3|\cdot|x+1|$.  
   > If $|x-3| < 1$, then $2 < x < 4$, so $3 < x+1 < 5$, i.e. $|x+1| < 5$.  
   > We need $5|x-3| < 0{,}5 \Rightarrow |x-3| < 0{,}1$.  
   > We take $\delta = \min(1; 0{,}1) = 0{,}1$.
   >
   > **c)** Geometrically: for the values of $f$ to remain within the horizontal band $(3-0{,}5,\, 3+0{,}5) = (2{,}5;\, 3{,}5)$ around the limit, it suffices that $x$ is within the interval $(3-0{,}1;\, 3+0{,}1) = (2{,}9;\, 3{,}1)$. The $\varepsilon$-$\delta$ definition says that we can always find a neighbourhood of $x=3$ that guarantees the desired precision in $f$.

**Multiple Choice Test**

6. In the $\varepsilon$-$\delta$ definition of limit, if $\displaystyle\lim_{x\to a} f(x) = L$, then for any $\varepsilon > 0$ there exists $\delta > 0$ such that $0 < |x - a| < \delta$ implies:
   - a) $|f(x)| < \varepsilon$
   - b) $|f(x) - L| < \varepsilon$
   - c) $|x - a| < \varepsilon$
   - d) $|f(x) - a| < \delta$

   > **Correct answer: b)** The definition states that $|f(x) - L| < \varepsilon$, i.e., $f(x)$ approaches the limit $L$ with precision $\varepsilon$.

7. In the $\varepsilon$-$\delta$ definition, the condition $0 < |x - a| < \delta$ (with $0 < |x-a|$) is imposed in order to:
   - a) Require that $x > a$
   - b) Exclude the point $x = a$ from the analysis
   - c) Guarantee that $\delta < \varepsilon$
   - d) Ensure that $f(a)$ is defined

   > **Correct answer: b)** The condition $|x - a| > 0$ explicitly excludes the point $x = a$: the limit describes the behaviour of $f$ near $a$, not at $a$. The function may not even be defined at $a$.

---

#### 6.1.3 One-sided limits: left-hand and right-hand limits

**Worked Example**

Calculate the one-sided limits of $f(x) = \dfrac{|x-2|}{x-2}$ at $x = 2$.

**Solution:**

We recall that $|x - 2| = \begin{cases} x-2 & \text{if } x \geq 2 \\ -(x-2) & \text{if } x < 2 \end{cases}$

**Right-hand limit** ($x \to 2^+$): In this case $x > 2$, so $|x-2| = x-2$:
$$\lim_{x \to 2^+} \frac{|x-2|}{x-2} = \lim_{x \to 2^+} \frac{x-2}{x-2} = \lim_{x \to 2^+} 1 = 1$$

**Left-hand limit** ($x \to 2^-$): In this case $x < 2$, so $|x-2| = -(x-2)$:
$$\lim_{x \to 2^-} \frac{|x-2|}{x-2} = \lim_{x \to 2^-} \frac{-(x-2)}{x-2} = \lim_{x \to 2^-}(-1) = -1$$

Since $\displaystyle\lim_{x \to 2^+} f(x) = 1 \neq -1 = \lim_{x \to 2^-} f(x)$, **the limit at $x = 2$ does not exist**.

---

**Exercises with Solutions**

**Basic Level:**

1. Calculate the one-sided limits of $f(x) = \begin{cases} x + 1 & \text{if } x < 0 \\ x^2 + 1 & \text{if } x \geq 0 \end{cases}$ at $x = 0$.

   > **Solution:**  
   > $\displaystyle\lim_{x \to 0^-} (x+1) = 0+1 = 1$  
   > $\displaystyle\lim_{x \to 0^+} (x^2+1) = 0+1 = 1$  
   > Since both one-sided limits equal $1$: $\displaystyle\lim_{x \to 0} f(x) = 1$.

2. For $g(x) = \begin{cases} 2x & \text{if } x \leq 1 \\ 3 & \text{if } x > 1 \end{cases}$, calculate the one-sided limits at $x = 1$ and determine whether the limit exists.

   > **Solution:**  
   > $\displaystyle\lim_{x \to 1^-} 2x = 2$  
   > $\displaystyle\lim_{x \to 1^+} 3 = 3$  
   > The one-sided limits are different ($2 \neq 3$), therefore **the limit at $x = 1$ does not exist**.

**Intermediate Level:**

3. Let $f(x) = \dfrac{x^2 - 4}{|x - 2|}$. Calculate $\displaystyle\lim_{x \to 2^-} f(x)$ and $\displaystyle\lim_{x \to 2^+} f(x)$.

   > **Solution:** We factor: $x^2 - 4 = (x-2)(x+2)$.  
   > For $x \to 2^+$: $|x-2| = x-2$, so $f(x) = \dfrac{(x-2)(x+2)}{x-2} = x+2 \to 4$.  
   > For $x \to 2^-$: $|x-2| = -(x-2)$, so $f(x) = \dfrac{(x-2)(x+2)}{-(x-2)} = -(x+2) \to -4$.  
   > $\displaystyle\lim_{x \to 2^+} f(x) = 4$, $\quad \displaystyle\lim_{x \to 2^-} f(x) = -4$. The overall limit does not exist.

4. Calculate the one-sided limits of $h(x) = \dfrac{1}{x-3}$ at $x = 3$. What type of behaviour does it exhibit?

   > **Solution:**  
   > For $x \to 3^+$: $x - 3 > 0$ and tends to $0^+$, so $\dfrac{1}{x-3} \to +\infty$.  
   > For $x \to 3^-$: $x - 3 < 0$ and tends to $0^-$, so $\dfrac{1}{x-3} \to -\infty$.  
   > The function has a **vertical asymptote** at $x = 3$ with branches of opposite sign.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \begin{cases} \dfrac{x^2 - 1}{x - 1} & \text{if } x < 1 \\ ax + b & \text{if } x \geq 1 \end{cases}$

   a) Calculate $\displaystyle\lim_{x \to 1^-} f(x)$.  
   b) For $\displaystyle\lim_{x \to 1} f(x)$ to exist, what condition must $a$ and $b$ satisfy?  
   c) If additionally $f(1) = 3$ is required, determine $a$ and $b$ so that the limit exists and give an example of valid values.

   > **Solution:**
   >
   > **a)** For $x < 1$: $\dfrac{x^2-1}{x-1} = \dfrac{(x-1)(x+1)}{x-1} = x+1 \to 1+1 = 2$.  
   > $\displaystyle\lim_{x \to 1^-} f(x) = 2$
   >
   > **b)** $\displaystyle\lim_{x \to 1^+} (ax+b) = a+b$.  
   > For the limit to exist: $a + b = 2$.
   >
   > **c)** $f(1) = a(1) + b = a + b = 3$. But the condition for the limit to exist requires $a + b = 2$.  
   > Contradiction: if $f(1) = 3$ and the limit at $x=1$ equals $2$, the limit **exists** (equals $2$) but $f(1) \neq \lim_{x\to 1}f(x)$, so $f$ **would not be continuous** at $x=1$.  
   > To have $a + b = 2$ with $f(1) = 3$: this is impossible with this definition of $f$, since $f(1) = a + b$.  
   > Conclusion: if we require both that $\lim_{x\to 1}f(x)$ exists AND $f(1) = 3$ simultaneously, we need $a + b = 2$ and $a + b = 3$, which is **incompatible**. Only one of the two requirements can be satisfied.

**Multiple Choice Test**

6. For $\displaystyle\lim_{x \to a} f(x)$ to exist, the necessary and sufficient condition is that:
   - a) $f(a)$ is defined
   - b) The one-sided limits exist and are equal
   - c) $f$ is continuous at $a$
   - d) $f'(a)$ exists

   > **Correct answer: b)** The limit at a point exists if and only if the left-hand and right-hand lateral limits both exist and are equal to each other.

7. If $\displaystyle\lim_{x \to 2^-} f(x) = 3$ and $\displaystyle\lim_{x \to 2^+} f(x) = -3$, then:
   - a) $\displaystyle\lim_{x \to 2} f(x) = 0$
   - b) $\displaystyle\lim_{x \to 2} f(x) = 3$
   - c) The limit at $x = 2$ does not exist
   - d) $f(2) = 0$

   > **Correct answer: c)** Since the one-sided limits are different ($3 \neq -3$), the overall limit at $x = 2$ does not exist.

---

#### 6.1.4 Existence of the limit: condition of equality of one-sided limits

**Worked Example**

Determine for which values of the parameter $k$ the limit $\displaystyle\lim_{x \to 2} f(x)$ exists, where $f(x) = \begin{cases} kx^2 - 1 & \text{if } x < 2 \\ 3x + k & \text{if } x \geq 2 \end{cases}$.

**Solution:**

We calculate the one-sided limits as a function of $k$:

**Left-hand limit:**
$$\lim_{x \to 2^-}(kx^2 - 1) = k(4) - 1 = 4k - 1$$

**Right-hand limit:**
$$\lim_{x \to 2^+}(3x + k) = 6 + k$$

For the overall limit to exist, we must equate:
$$4k - 1 = 6 + k$$
$$3k = 7$$
$$k = \frac{7}{3}$$

**Verification:** With $k = \frac{7}{3}$:
- Left-hand limit: $4 \cdot \frac{7}{3} - 1 = \frac{28}{3} - 1 = \frac{25}{3}$
- Right-hand limit: $6 + \frac{7}{3} = \frac{18+7}{3} = \frac{25}{3}$ ✓

For $k = \dfrac{7}{3}$, $\displaystyle\lim_{x \to 2} f(x) = \dfrac{25}{3}$.

---

**Exercises with Solutions**

**Basic Level:**

1. Check whether $\displaystyle\lim_{x \to 0} f(x)$ exists for $f(x) = \begin{cases} 2x + 3 & \text{if } x < 0 \\ 3 - x & \text{if } x \geq 0 \end{cases}$.

   > **Solution:**  
   > $\displaystyle\lim_{x \to 0^-}(2x+3) = 3$  
   > $\displaystyle\lim_{x \to 0^+}(3-x) = 3$  
   > The one-sided limits are equal: $\displaystyle\lim_{x \to 0} f(x) = 3$.

2. Determine whether $\displaystyle\lim_{x \to 1} g(x)$ exists for $g(x) = \begin{cases} x^2 & \text{if } x \leq 1 \\ 2x - 1 & \text{if } x > 1 \end{cases}$.

   > **Solution:**  
   > $\displaystyle\lim_{x \to 1^-} x^2 = 1$  
   > $\displaystyle\lim_{x \to 1^+}(2x-1) = 1$  
   > The one-sided limits coincide: $\displaystyle\lim_{x \to 1} g(x) = 1$.

**Intermediate Level:**

3. Find the values of $a$ and $b$ such that $\displaystyle\lim_{x \to 1} f(x)$ exists and equals $4$, where:
   $$f(x) = \begin{cases} ax + b & \text{if } x < 1 \\ x^2 + 3 & \text{if } x \geq 1 \end{cases}$$

   > **Solution:**  
   > $\displaystyle\lim_{x \to 1^+}(x^2+3) = 4$, so the limit must be $4$.  
   > $\displaystyle\lim_{x \to 1^-}(ax+b) = a+b = 4$.  
   > With $a + b = 4$ the limit exists and equals $4$. For example: $a = 1, b = 3$ or $a = 2, b = 2$.

4. Determine for which values of $k$ the limit $\displaystyle\lim_{x \to 0} h(x)$ exists:
   $$h(x) = \begin{cases} \dfrac{\sin(kx)}{x} & \text{if } x \neq 0 \\ 2 & \text{if } x = 0 \end{cases}$$

   > **Solution:** For $x \neq 0$: $\displaystyle\lim_{x \to 0} \dfrac{\sin(kx)}{x} = \lim_{x \to 0} k \cdot \dfrac{\sin(kx)}{kx} = k \cdot 1 = k$.  
   > The limit exists and equals $k$ for any $k$. For it to also be continuous at $0$, we would need $k = 2$. The limit exists for all $k \in \mathbb{R}$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let the function:
   $$f(x) = \begin{cases} x^2 + ax & \text{if } x < -1 \\ b & \text{if } x = -1 \\ 2x + 3 & \text{if } x > -1 \end{cases}$$

   a) Calculate $\displaystyle\lim_{x \to -1^+} f(x)$.  
   b) Find the value of $a$ for which $\displaystyle\lim_{x \to -1} f(x)$ exists.  
   c) With that value of $a$, is there a value of $b$ that makes $f$ continuous at $x = -1$? Justify.

   > **Solution:**
   >
   > **a)** $\displaystyle\lim_{x \to -1^+}(2x+3) = -2+3 = 1$
   >
   > **b)** $\displaystyle\lim_{x \to -1^-}(x^2 + ax) = 1 + a(-1) = 1 - a$.  
   > For the limit to exist: $1 - a = 1 \Rightarrow a = 0$.  
   > With $a = 0$: $\displaystyle\lim_{x \to -1} f(x) = 1$.
   >
   > **c)** With $a = 0$, the limit at $x = -1$ equals $1$. For $f$ to be continuous at $x = -1$, we need $f(-1) = \lim_{x \to -1} f(x)$, i.e., $b = 1$. **Yes it exists**: $b = 1$ makes $f$ continuous at $x = -1$.

**Multiple Choice Test**

6. If $\displaystyle\lim_{x\to a^-} f(x) = L$ and $\displaystyle\lim_{x\to a^+} f(x) = L$, then it is **certain** that:
   - a) $f(a) = L$
   - b) $f$ is continuous at $a$
   - c) $\displaystyle\lim_{x\to a} f(x) = L$
   - d) $f$ is differentiable at $a$

   > **Correct answer: c)** The equality of the one-sided limits guarantees the existence of the overall limit equal to $L$. Nothing can be concluded about $f(a)$ or continuity without additional information.

7. For $f(x) = \begin{cases} 3 & \text{if } x < 2 \\ x + 1 & \text{if } x \geq 2 \end{cases}$, the value of $\displaystyle\lim_{x \to 2} f(x)$:
   - a) Is $3$
   - b) Is $4$  
   - c) Does not exist
   - d) Depends on which branch is taken

   > **Correct answer: c)** $\lim_{x\to 2^-}f(x) = 3$ and $\lim_{x\to 2^+}f(x) = 3$... wait: $\lim_{x\to 2^+}(x+1)=3$. Then both equal $3$, so the limit does exist and equals $3$.  
   > **Corrected answer: a)** $\lim_{x\to 2^-}f(x)=3$ and $\lim_{x\to 2^+}f(x)=2+1=3$. Both equal $3$, therefore $\lim_{x\to 2}f(x)=3$.

---

#### 6.1.5 Operational properties of limits (algebra of limits)

**Worked Example**

Given $\displaystyle\lim_{x \to 3} f(x) = 4$ and $\displaystyle\lim_{x \to 3} g(x) = -2$, calculate:
a) $\displaystyle\lim_{x \to 3}[3f(x) - g(x)]$
b) $\displaystyle\lim_{x \to 3}[f(x) \cdot g(x)]$
c) $\displaystyle\lim_{x \to 3}\dfrac{f(x)}{g(x)}$
d) $\displaystyle\lim_{x \to 3}\sqrt{f(x) + 5}$

**Solution:**

Applying the properties of the algebra of limits (where $L = \lim f$ and $M = \lim g$):

**a)** Linearity:
$$\lim_{x \to 3}[3f(x) - g(x)] = 3\lim_{x \to 3}f(x) - \lim_{x \to 3}g(x) = 3(4) - (-2) = 12 + 2 = 14$$

**b)** Limit of the product:
$$\lim_{x \to 3}[f(x) \cdot g(x)] = \lim_{x \to 3}f(x) \cdot \lim_{x \to 3}g(x) = 4 \cdot (-2) = -8$$

**c)** Limit of the quotient (the denominator does not vanish):
$$\lim_{x \to 3}\frac{f(x)}{g(x)} = \frac{\lim_{x \to 3}f(x)}{\lim_{x \to 3}g(x)} = \frac{4}{-2} = -2$$

**d)** Limit of the square root (the argument is positive):
$$\lim_{x \to 3}\sqrt{f(x)+5} = \sqrt{\lim_{x \to 3}[f(x)+5]} = \sqrt{4+5} = \sqrt{9} = 3$$

---

**Exercises with Solutions**

**Basic Level:**

1. If $\displaystyle\lim_{x \to 2} f(x) = 6$ and $\displaystyle\lim_{x \to 2} g(x) = 3$, calculate $\displaystyle\lim_{x \to 2}\left[\frac{f(x)}{g(x)} + f(x) - g(x)^2\right]$.

   > **Solution:** $\dfrac{6}{3} + 6 - 9 = 2 + 6 - 9 = -1$

2. Calculate $\displaystyle\lim_{x \to 1}(x^3 - 2x^2 + 5)$ using the operational properties.

   > **Solution:** As it is a polynomial, we apply the limit by substitution:  
   > $\displaystyle\lim_{x \to 1}x^3 - 2\lim_{x \to 1}x^2 + 5 = 1 - 2 + 5 = 4$

**Intermediate Level:**

3. If $\displaystyle\lim_{x \to a}f(x) = 2$ and $\displaystyle\lim_{x \to a}g(x) = 0$, analyse whether $\displaystyle\lim_{x \to a}\dfrac{f(x)}{g(x)}$ can be calculated.

   > **Solution:** The quotient property requires that the limit of the denominator be **non-zero**. Since $\lim g(x) = 0$, the property **cannot be applied directly**. The quotient may tend to $\pm\infty$ or may present an indeterminate form requiring specific techniques. We cannot assert that the limit does not exist without further information.

4. Given $\displaystyle\lim_{x\to 0^+}f(x) = +\infty$ and $\displaystyle\lim_{x\to 0^+}g(x) = 3$, what is $\displaystyle\lim_{x\to 0^+}[f(x)+g(x)]$?

   > **Solution:** When one summand tends to $+\infty$ and the other has a finite limit:  
   > $\displaystyle\lim_{x\to 0^+}[f(x)+g(x)] = +\infty + 3 = +\infty$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f$ and $g$ be functions such that $\displaystyle\lim_{x \to 2} f(x) = 3$ and $\displaystyle\lim_{x \to 2} g(x) = 0$.

   a) Calculate $\displaystyle\lim_{x \to 2}[f(x)^2 - 2g(x) + 1]$.  
   b) Calculate $\displaystyle\lim_{x \to 2}\sqrt{2f(x) - g(x)}$.  
   c) Can $\displaystyle\lim_{x \to 2} \dfrac{g(x)}{f(x) - 3}$ be calculated? Justify.

   > **Solution:**
   >
   > **a)** $\lim[f^2 - 2g + 1] = 3^2 - 2(0) + 1 = 9 + 0 + 1 = 10$
   >
   > **b)** $\sqrt{2(3) - 0} = \sqrt{6}$
   >
   > **c)** $\lim[f(x)-3] = 3-3 = 0$ and $\lim g(x) = 0$: indeterminate form $\dfrac{0}{0}$. Without knowing the explicit expressions of $f$ and $g$, **we cannot calculate this limit** with algebraic properties. It would require additional information about how the numerator and denominator vanish.

**Multiple Choice Test**

6. If $\displaystyle\lim_{x\to a} f(x) = 2$ and $\displaystyle\lim_{x\to a} g(x) = -1$, then $\displaystyle\lim_{x\to a} [f(x)]^{g(x)}$ equals:
   - a) $-2$
   - b) $2$
   - c) $\frac{1}{2}$
   - d) $-\frac{1}{2}$

   > **Correct answer: c)** $\lim [f(x)]^{g(x)} = \left(\lim f(x)\right)^{\lim g(x)} = 2^{-1} = \dfrac{1}{2}$ (valid when the base is positive and the limits exist).

7. The property $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)} = \frac{\lim_{x\to a}f(x)}{\lim_{x\to a}g(x)}$ can be applied whenever:
   - a) $\displaystyle\lim_{x\to a} f(x) \neq 0$
   - b) $\displaystyle\lim_{x\to a} g(x) \neq 0$
   - c) $f(a) \neq 0$
   - d) $g(a) \neq 0$

   > **Correct answer: b)** The necessary condition to apply the quotient property is that the limit of the **denominator** is non-zero.

---

## 6.2 Calculation of limits and indeterminate forms

---

#### 6.2.1 Direct limits and limits by substitution

**Worked Example**

Calculate $\displaystyle\lim_{x \to 2}\frac{x^3 + 3x - 1}{x^2 + 1}$.

**Solution:**

We attempt direct substitution $x = 2$:

$$\lim_{x \to 2}\frac{x^3 + 3x - 1}{x^2 + 1} = \frac{2^3 + 3(2) - 1}{2^2 + 1} = \frac{8 + 6 - 1}{4 + 1} = \frac{13}{5}$$

There is no indeterminate form: the denominator does not vanish at $x = 2$ (it equals $5 \neq 0$) and both numerator and denominator are polynomials (continuous). Direct substitution is valid.

$$\lim_{x \to 2}\frac{x^3 + 3x - 1}{x^2 + 1} = \frac{13}{5}$$

---

**Exercises with Solutions**

**Basic Level:**

1. Calculate by direct substitution: $\displaystyle\lim_{x \to -1}(x^4 - 3x^2 + 2x - 5)$.

   > **Solution:** $(-1)^4 - 3(-1)^2 + 2(-1) - 5 = 1 - 3 - 2 - 5 = -9$

2. Calculate: $\displaystyle\lim_{x \to \pi} \dfrac{\cos x + 2}{\sin x + 3}$.

   > **Solution:** $\dfrac{\cos\pi + 2}{\sin\pi + 3} = \dfrac{-1+2}{0+3} = \dfrac{1}{3}$

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x \to 0} \dfrac{e^x + \ln(x+1)}{x^2 + 2}$.

   > **Solution:** At $x = 0$: $\dfrac{e^0 + \ln 1}{0 + 2} = \dfrac{1 + 0}{2} = \dfrac{1}{2}$

4. Calculate $\displaystyle\lim_{x \to 1} \dfrac{\sqrt{x+3} - x^2}{x + 1}$.

   > **Solution:** $\dfrac{\sqrt{1+3} - 1}{1+1} = \dfrac{2 - 1}{2} = \dfrac{1}{2}$

**EVAU Level:**

5. **(EVAU Madrid style)** Calculate the following limits justifying the method:

   a) $\displaystyle\lim_{x \to 3} \dfrac{x^2 - 2x + 1}{x^3 - 1}$  
   b) $\displaystyle\lim_{x \to 0} \dfrac{\sqrt{4+x} \cdot e^x}{\cos x + 1}$  
   c) $\displaystyle\lim_{x \to 2} \dfrac{x^2 - 3x + 2}{x - 2}$

   > **Solution:**
   >
   > **a)** Denominator at $x=3$: $27 - 1 = 26 \neq 0$. Direct substitution:  
   > $\dfrac{9-6+1}{27-1} = \dfrac{4}{26} = \dfrac{2}{13}$
   >
   > **b)** Denominator at $x=0$: $\cos 0 + 1 = 2 \neq 0$. Direct substitution:  
   > $\dfrac{\sqrt{4}\cdot e^0}{1+1} = \dfrac{2\cdot1}{2} = 1$
   >
   > **c)** At $x=2$: numerator $= 4-6+2=0$, denominator $= 0$: indeterminate form $\dfrac{0}{0}$.  
   > Factoring: $\dfrac{(x-1)(x-2)}{x-2} = x-1 \to 2-1 = 1$.

**Multiple Choice Test**

6. When can a limit be calculated by direct substitution?
   - a) Always
   - b) Only when the function is polynomial
   - c) When the function is continuous at the point being considered
   - d) Only when the limit is a real number

   > **Correct answer: c)** Direct substitution is valid when the function is continuous at the point. This includes polynomials, but also rational, trigonometric, exponential functions, etc., evaluated at points in their domain where there are no discontinuities.

7. When calculating $\displaystyle\lim_{x\to 2}\dfrac{x-2}{x^2-4}$ by direct substitution, we obtain $\dfrac{0}{0}$. This means:
   - a) The limit is $0$
   - b) The limit is infinite
   - c) The limit does not exist
   - d) There is an indeterminate form that requires another method

   > **Correct answer: d)** The form $\dfrac{0}{0}$ is an indeterminate form: the result cannot be determined directly. We must factor: $\dfrac{x-2}{(x-2)(x+2)} = \dfrac{1}{x+2} \to \dfrac{1}{4}$.

---

#### 6.2.2 Indeterminate form 0/0: factoring, rationalisation and substitutions

**Worked Example**

Calculate $\displaystyle\lim_{x \to 3} \dfrac{x^2 - 9}{x^2 - 5x + 6}$.

**Solution:**

We check that there is an indeterminate form: $x = 3$ makes both numerator ($9-9=0$) and denominator ($9-15+6=0$) vanish. Form: $\dfrac{0}{0}$.

**Step 1: Factor**
- Numerator: $x^2 - 9 = (x-3)(x+3)$
- Denominator: $x^2 - 5x + 6 = (x-3)(x-2)$ (roots: $x=3$ and $x=2$)

**Step 2: Simplify and calculate**
$$\lim_{x \to 3} \frac{x^2 - 9}{x^2 - 5x + 6} = \lim_{x \to 3} \frac{(x-3)(x+3)}{(x-3)(x-2)} = \lim_{x \to 3} \frac{x+3}{x-2} = \frac{3+3}{3-2} = \frac{6}{1} = 6$$

The factor $(x-3)$ cancels (recalling that $x \neq 3$ in the limit), and direct substitution is now valid.

---

**Exercises with Solutions**

**Basic Level:**

1. Calculate $\displaystyle\lim_{x \to 1}\dfrac{x^2 - 1}{x - 1}$.

   > **Solution:** $\dfrac{0}{0}$. Factoring: $\dfrac{(x-1)(x+1)}{x-1} = x+1 \to 2$.

2. Calculate $\displaystyle\lim_{x \to 2}\dfrac{\sqrt{x} - \sqrt{2}}{x - 2}$.

   > **Solution:** $\dfrac{0}{0}$. Rationalising (multiplying by $\dfrac{\sqrt{x}+\sqrt{2}}{\sqrt{x}+\sqrt{2}}$):  
   > $\dfrac{(\sqrt{x}-\sqrt{2})(\sqrt{x}+\sqrt{2})}{(x-2)(\sqrt{x}+\sqrt{2})} = \dfrac{x-2}{(x-2)(\sqrt{x}+\sqrt{2})} = \dfrac{1}{\sqrt{x}+\sqrt{2}} \to \dfrac{1}{2\sqrt{2}} = \dfrac{\sqrt{2}}{4}$

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x \to 4}\dfrac{x - 4}{\sqrt{x} - 2}$.

   > **Solution:** Form $\dfrac{0}{0}$. Multiplying by $\dfrac{\sqrt{x}+2}{\sqrt{x}+2}$:  
   > $\dfrac{(x-4)(\sqrt{x}+2)}{(\sqrt{x}-2)(\sqrt{x}+2)} = \dfrac{(x-4)(\sqrt{x}+2)}{x-4} = \sqrt{x}+2 \to \sqrt{4}+2 = 4$

4. Calculate $\displaystyle\lim_{x \to 0}\dfrac{\sqrt{1+x} - \sqrt{1-x}}{x}$.

   > **Solution:** Form $\dfrac{0}{0}$. Rationalise by multiplying by $\dfrac{\sqrt{1+x}+\sqrt{1-x}}{\sqrt{1+x}+\sqrt{1-x}}$:  
   > $\dfrac{(1+x)-(1-x)}{x(\sqrt{1+x}+\sqrt{1-x})} = \dfrac{2x}{x(\sqrt{1+x}+\sqrt{1-x})} = \dfrac{2}{\sqrt{1+x}+\sqrt{1-x}} \to \dfrac{2}{1+1} = 1$

**EVAU Level:**

5. **(EVAU Madrid style)** Calculate the following limits with indeterminate form $\dfrac{0}{0}$:

   a) $\displaystyle\lim_{x \to -2}\dfrac{x^3 + 8}{x^2 + 3x + 2}$  
   b) $\displaystyle\lim_{x \to 1}\dfrac{\sqrt{x+3} - 2}{x - 1}$  
   c) $\displaystyle\lim_{x \to 0}\dfrac{(1+x)^2 - 1}{x}$

   > **Solution:**
   >
   > **a)** $x = -2$: numerator $= -8+8=0$, denominator $= 4-6+2=0$. Form $\dfrac{0}{0}$.  
   > $x^3+8 = (x+2)(x^2-2x+4)$; $x^2+3x+2 = (x+2)(x+1)$.  
   > $\displaystyle\lim_{x\to-2}\dfrac{(x+2)(x^2-2x+4)}{(x+2)(x+1)} = \dfrac{4+4+4}{-2+1} = \dfrac{12}{-1} = -12$
   >
   > **b)** At $x=1$: $\sqrt{4}-2 = 0$ and $0$. Form $\dfrac{0}{0}$.  
   > Multiply by $\dfrac{\sqrt{x+3}+2}{\sqrt{x+3}+2}$:  
   > $\dfrac{(x+3)-4}{(x-1)(\sqrt{x+3}+2)} = \dfrac{x-1}{(x-1)(\sqrt{x+3}+2)} = \dfrac{1}{\sqrt{x+3}+2} \to \dfrac{1}{4}$
   >
   > **c)** $(1+x)^2 - 1 = 1+2x+x^2-1 = 2x+x^2 = x(2+x)$.  
   > $\dfrac{x(2+x)}{x} = 2+x \to 2$

**Multiple Choice Test**

6. To resolve the indeterminate form $\dfrac{0}{0}$ in $\displaystyle\lim_{x\to a}\dfrac{f(x)}{g(x)}$ when $f(x)$ contains a square root, the most common method is:
   - a) L'Hôpital
   - b) Cramer's rule
   - c) Rationalisation of the numerator
   - d) Taylor series expansion

   > **Correct answer: c)** When square roots appear in the numerator, rationalisation (multiplying by the conjugate) eliminates the root and allows us to cancel the factor producing the indeterminate form.

7. $\displaystyle\lim_{x \to 3}\dfrac{x^2 - 9}{x - 3}$ equals:
   - a) $0$
   - b) $3$
   - c) $6$
   - d) Does not exist

   > **Correct answer: c)** $\dfrac{(x-3)(x+3)}{x-3} = x+3 \to 6$.

---

#### 6.2.3 Indeterminate form k/0 and infinite limits

**Worked Example**

Calculate $\displaystyle\lim_{x \to 2} \dfrac{3x - 1}{(x-2)^2}$ and $\displaystyle\lim_{x \to 1^+} \dfrac{x+2}{x-1}$.

**Solution:**

**First limit:** At $x = 2$: numerator $= 6-1 = 5 \neq 0$, denominator $= 0$. Form $\dfrac{k}{0}$ with $k = 5$.

When $(x-2)^2 \to 0^+$ (the square is always positive) and the numerator tends to $5 > 0$:
$$\lim_{x \to 2} \frac{3x - 1}{(x-2)^2} = +\infty$$

The denominator $(x-2)^2$ is always $\geq 0$, so the quotient tends to $+\infty$ from both sides.

**Second limit:** At $x = 1$: numerator $= 3 > 0$, denominator $= 0$.

For $x \to 1^+$: $x > 1$, so $x - 1 > 0$ and tends to $0^+$:
$$\lim_{x \to 1^+} \frac{x+2}{x-1} = \frac{3^+}{0^+} = +\infty$$

(For $x \to 1^-$: $x - 1 < 0$, so the limit would be $-\infty$.)

---

**Exercises with Solutions**

**Basic Level:**

1. Calculate $\displaystyle\lim_{x \to 0^+} \dfrac{1}{x}$ and $\displaystyle\lim_{x \to 0^-} \dfrac{1}{x}$.

   > **Solution:**  
   > $\displaystyle\lim_{x \to 0^+} \dfrac{1}{x} = +\infty$ (positive denominator tending to $0$)  
   > $\displaystyle\lim_{x \to 0^-} \dfrac{1}{x} = -\infty$ (negative denominator tending to $0$)

2. Calculate $\displaystyle\lim_{x \to 3^-} \dfrac{x+1}{3-x}$.

   > **Solution:** Numerator at $x=3$: $4 > 0$. For $x \to 3^-$: $3 - x > 0$ and tends to $0^+$.  
   > $\displaystyle\lim_{x \to 3^-} \dfrac{x+1}{3-x} = +\infty$

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x \to -1} \dfrac{x^2 + 2x + 1}{x + 1}$ or state whether it does not exist.

   > **Solution:** Numerator: $x^2+2x+1 = (x+1)^2$. At $x=-1$: both vanish. Form $\dfrac{0}{0}$.  
   > $\dfrac{(x+1)^2}{x+1} = x+1 \to 0$. This is not $\dfrac{k}{0}$, but $\dfrac{0}{0}$ with result $0$.

4. Study $\displaystyle\lim_{x \to 2} \dfrac{x^2 - 4}{(x-2)^3}$.

   > **Solution:** $x^2-4 = (x-2)(x+2)$, so $\dfrac{(x-2)(x+2)}{(x-2)^3} = \dfrac{x+2}{(x-2)^2}$.  
   > At $x=2$: numerator $= 4 > 0$, denominator $= 0^+$. Limit $= +\infty$.

**EVAU Level:**

5. **(EVAU Madrid style)** For $f(x) = \dfrac{x^2 - 1}{(x-1)^2(x+2)}$:

   a) Determine the points where the denominator vanishes.  
   b) Calculate the one-sided limits at $x = 1$.  
   c) Calculate the limit at $x = -2$ if it exists.

   > **Solution:**
   >
   > **a)** $(x-1)^2(x+2) = 0 \Rightarrow x = 1$ (double) or $x = -2$.
   >
   > **b)** We simplify: $x^2-1 = (x-1)(x+1)$, so:  
   > $\dfrac{(x-1)(x+1)}{(x-1)^2(x+2)} = \dfrac{x+1}{(x-1)(x+2)}$  
   > For $x \to 1^+$: numerator $\to 2$, $(x-1) \to 0^+$, $(x+2) \to 3$.  
   > $\displaystyle\lim_{x\to 1^+} = +\infty$  
   > For $x \to 1^-$: $(x-1) \to 0^-$, numerator $\to 2 > 0$, $(x+2) \to 3 > 0$.  
   > $\displaystyle\lim_{x\to 1^-} = -\infty$
   >
   > **c)** At $x = -2$: $\dfrac{x+1}{(x-1)(x+2)}$, numerator $= -1 \neq 0$, denominator $\to 0$.  
   > For $x \to -2^+$: $(x+2) \to 0^+$, $(x-1) \to -3$, numerator $\to -1$.  
   > $\dfrac{-1}{(-3)(0^+)} = \dfrac{-1}{0^-} = +\infty$.  
   > For $x \to -2^-$: $(x+2) \to 0^-$, $\dfrac{-1}{(-3)(0^-)} = \dfrac{-1}{0^+} = -\infty$.  
   > The limit at $x = -2$ **does not exist** (infinite one-sided limits with different signs).

**Multiple Choice Test**

6. The limit $\displaystyle\lim_{x\to 0}\dfrac{1}{x^2}$ equals:
   - a) $0$
   - b) $-\infty$
   - c) $+\infty$
   - d) Does not exist

   > **Correct answer: c)** $x^2 > 0$ for all $x \neq 0$, and tends to $0^+$. Therefore $\dfrac{1}{x^2} \to +\infty$.

7. If $f(x) \to 3$ and $g(x) \to 0^-$ as $x \to a$, then $\displaystyle\lim_{x\to a}\dfrac{f(x)}{g(x)}$ equals:
   - a) $0$
   - b) $+\infty$
   - c) $-\infty$
   - d) $3$

   > **Correct answer: c)** A positive numerator ($3$) divided by a negative denominator tending to zero gives $-\infty$.

---

#### 6.2.4 Indeterminate form ∞ − ∞: resolution techniques

**Worked Example**

Calculate $\displaystyle\lim_{x \to +\infty}\left(\sqrt{x^2 + 3x} - x\right)$.

**Solution:**

Form $+\infty - \infty$. We rationalise by multiplying by the conjugate:

$$\lim_{x \to +\infty}\left(\sqrt{x^2+3x}-x\right) \cdot \frac{\sqrt{x^2+3x}+x}{\sqrt{x^2+3x}+x} = \lim_{x \to +\infty}\frac{(x^2+3x)-x^2}{\sqrt{x^2+3x}+x} = \lim_{x \to +\infty}\frac{3x}{\sqrt{x^2+3x}+x}$$

We divide numerator and denominator by $x > 0$:

$$= \lim_{x \to +\infty}\frac{3}{\sqrt{1+\frac{3}{x}}+1} = \frac{3}{\sqrt{1+0}+1} = \frac{3}{2}$$

---

**Exercises with Solutions**

**Basic Level:**

1. Calculate $\displaystyle\lim_{x \to 1}\left(\dfrac{1}{x-1} - \dfrac{2}{x^2-1}\right)$.

   > **Solution:** Form $\infty - \infty$. We reduce to common denominator $x^2-1 = (x-1)(x+1)$:  
   > $\dfrac{x+1}{(x-1)(x+1)} - \dfrac{2}{(x-1)(x+1)} = \dfrac{x+1-2}{(x-1)(x+1)} = \dfrac{x-1}{(x-1)(x+1)} = \dfrac{1}{x+1} \to \dfrac{1}{2}$

2. Calculate $\displaystyle\lim_{x \to +\infty}(\sqrt{x+1} - \sqrt{x})$.

   > **Solution:** Rationalising: $\dfrac{(x+1)-x}{\sqrt{x+1}+\sqrt{x}} = \dfrac{1}{\sqrt{x+1}+\sqrt{x}} \to 0$.

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x \to 2}\left(\dfrac{3}{x^2-4} - \dfrac{1}{x-2}\right)$.

   > **Solution:** $x^2-4=(x-2)(x+2)$. Reducing to common denominator $(x-2)(x+2)$:  
   > $\dfrac{3}{(x-2)(x+2)} - \dfrac{x+2}{(x-2)(x+2)} = \dfrac{3-(x+2)}{(x-2)(x+2)} = \dfrac{1-x}{(x-2)(x+2)}$  
   > At $x=2$: numerator $\to -1$, denominator $\to 0$. We analyse the sign:  
   > For $x\to 2^+$: $(x-2)\to 0^+$, $(x+2)\to 4$, numerator $\to -1$: limit $= -\infty$.  
   > For $x\to 2^-$: $(x-2)\to 0^-$: limit $= +\infty$. **The limit does not exist**.

4. Calculate $\displaystyle\lim_{x \to +\infty}\left(\sqrt{x^2+x} - \sqrt{x^2-x}\right)$.

   > **Solution:** Rationalising:  
   > $\dfrac{(x^2+x)-(x^2-x)}{\sqrt{x^2+x}+\sqrt{x^2-x}} = \dfrac{2x}{\sqrt{x^2+x}+\sqrt{x^2-x}}$  
   > Dividing by $x$: $\dfrac{2}{\sqrt{1+1/x}+\sqrt{1-1/x}} \to \dfrac{2}{1+1} = 1$

**EVAU Level:**

5. **(EVAU Madrid style)** Calculate:

   a) $\displaystyle\lim_{x \to 0}\left(\dfrac{1}{x} - \dfrac{1}{\sin x}\right)$  
   b) $\displaystyle\lim_{x \to +\infty}\left(x - \sqrt{x^2 - 4x + 1}\right)$

   > **Solution:**
   >
   > **a)** Form $\infty - \infty$. Reducing: $\dfrac{\sin x - x}{x \sin x}$.  
   > Numerator: $\sin x - x \to 0$; denominator: $x\sin x \to 0$. Form $\dfrac{0}{0}$.  
   > Using the equivalent $\sin x \approx x - \dfrac{x^3}{6}$ near $0$:  
   > $\sin x - x \approx -\dfrac{x^3}{6}$; $x\sin x \approx x^2$.  
   > Limit $= \displaystyle\lim_{x\to 0} \dfrac{-x^3/6}{x^2} = \lim_{x\to 0}\dfrac{-x}{6} = 0$
   >
   > **b)** Rationalising:  
   > $\dfrac{x^2-(x^2-4x+1)}{x+\sqrt{x^2-4x+1}} = \dfrac{4x-1}{x+\sqrt{x^2-4x+1}}$  
   > Dividing by $x$: $\dfrac{4-1/x}{1+\sqrt{1-4/x+1/x^2}} \to \dfrac{4}{1+1} = 2$

**Multiple Choice Test**

6. The indeterminate form $\infty - \infty$ arises when:
   - a) Both summands tend to the same number
   - b) One tends to $+\infty$ and the other to $-\infty$, or both to $+\infty$
   - c) Both tend to zero
   - d) The numerator tends to infinity

   > **Correct answer: b)** The form $\infty - \infty$ occurs when both terms tend to infinity (of the same or different signs) creating uncertainty about the result.

7. To resolve $\displaystyle\lim_{x\to+\infty}(\sqrt{x+a}-\sqrt{x})$, the most effective method is:
   - a) Direct substitution
   - b) L'Hôpital directly
   - c) Multiply by the conjugate
   - d) Factor the denominator

   > **Correct answer: c)** Rationalisation (multiplying and dividing by the conjugate $\sqrt{x+a}+\sqrt{x}$) transforms the difference of roots into a manageable quotient.

---

#### 6.2.5 Indeterminate form 0·∞: transformation to 0/0 or ∞/∞

**Worked Example**

Calculate $\displaystyle\lim_{x \to 0^+} x \cdot \ln x$.

**Solution:**

Form $0 \cdot \infty$: when $x \to 0^+$, $x \to 0$ and $\ln x \to -\infty$.

We transform to the form $\dfrac{\infty}{\infty}$: we write $x = \dfrac{1}{1/x}$:

$$\lim_{x \to 0^+} x \cdot \ln x = \lim_{x \to 0^+} \frac{\ln x}{1/x}$$

Now it is the form $\dfrac{-\infty}{+\infty}$. We apply L'Hôpital:

$$= \lim_{x \to 0^+} \frac{(\ln x)'}{(1/x)'} = \lim_{x \to 0^+} \frac{1/x}{-1/x^2} = \lim_{x \to 0^+} \frac{x^2}{-x} \cdot \frac{1}{1} = \lim_{x \to 0^+}(-x) = 0$$

**Result:** $\displaystyle\lim_{x \to 0^+} x \ln x = 0$

(The logarithm grows more slowly than any positive power of $x$.)

---

**Exercises with Solutions**

**Basic Level:**

1. Transform the indeterminate form $0 \cdot \infty$ into $\dfrac{0}{0}$ or $\dfrac{\infty}{\infty}$ for $\displaystyle\lim_{x\to 0^+}\sqrt{x}\cdot\ln x$.

   > **Solution:** Form $0\cdot(-\infty)$. We transform: $\sqrt{x}\cdot\ln x = \dfrac{\ln x}{1/\sqrt{x}} = \dfrac{\ln x}{x^{-1/2}}$. Form $\dfrac{-\infty}{+\infty}$.  
   > L'Hôpital: $\dfrac{1/x}{-\frac{1}{2}x^{-3/2}} = \dfrac{1/x}{-\frac{1}{2x^{3/2}}} = \dfrac{-2x^{3/2}}{x} = -2\sqrt{x} \to 0$.  
   > Therefore: $\displaystyle\lim_{x\to 0^+}\sqrt{x}\ln x = 0$.

2. Calculate $\displaystyle\lim_{x\to+\infty}x\cdot e^{-x}$.

   > **Solution:** Form $+\infty \cdot 0$. We transform: $\dfrac{x}{e^x}$. Form $\dfrac{+\infty}{+\infty}$.  
   > L'Hôpital: $\dfrac{1}{e^x} \to 0$.  
   > $\displaystyle\lim_{x\to+\infty}x e^{-x} = 0$.

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x\to 0^+}x^2\ln x$.

   > **Solution:** $\dfrac{\ln x}{x^{-2}} \xrightarrow{\text{L'H}} \dfrac{1/x}{-2x^{-3}} = \dfrac{-x^3}{2x} = \dfrac{-x^2}{2} \to 0$.

4. Calculate $\displaystyle\lim_{x\to+\infty}(x^3+2x)e^{-2x}$.

   > **Solution:** Form $\infty\cdot 0$. Transform: $\dfrac{x^3+2x}{e^{2x}}$. Form $\dfrac{\infty}{\infty}$.  
   > L'Hôpital (three times if necessary):  
   > $\dfrac{3x^2+2}{2e^{2x}} \xrightarrow{\text{L'H}} \dfrac{6x}{4e^{2x}} \xrightarrow{\text{L'H}} \dfrac{6}{8e^{2x}} \to 0$.

**EVAU Level:**

5. **(EVAU Madrid style)** Calculate:

   a) $\displaystyle\lim_{x\to 0^+}x\ln(x^2)$  
   b) $\displaystyle\lim_{x\to\frac{\pi}{2}^-}(\pi - 2x)\tan x$

   > **Solution:**
   >
   > **a)** $x\ln(x^2) = 2x\ln x$. By the result of the worked example: $2\displaystyle\lim_{x\to 0^+}x\ln x = 2\cdot 0 = 0$.
   >
   > **b)** We make the substitution $t = \dfrac{\pi}{2} - x$, so $x = \dfrac{\pi}{2} - t$, $t\to 0^+$.  
   > $\pi - 2x = \pi - 2(\frac{\pi}{2}-t) = 2t$.  
   > $\tan x = \tan(\frac{\pi}{2}-t) = \cot t = \dfrac{\cos t}{\sin t}$.  
   > Limit $= \displaystyle\lim_{t\to 0^+}2t\cdot\dfrac{\cos t}{\sin t} = 2\lim_{t\to 0^+}\dfrac{t}{\sin t}\cdot\cos t = 2\cdot 1\cdot 1 = 2$.

**Multiple Choice Test**

6. The indeterminate form $0\cdot\infty$ can be transformed into:
   - a) Only $\dfrac{0}{0}$
   - b) Only $\dfrac{\infty}{\infty}$
   - c) Either one: $\dfrac{0}{0}$ or $\dfrac{\infty}{\infty}$
   - d) $\infty - \infty$

   > **Correct answer: c)** If the product is $f(x)\cdot g(x)$ with $f\to 0$ and $g\to\infty$, we can write $\dfrac{f(x)}{1/g(x)}$ (form $\dfrac{0}{0}$) or $\dfrac{g(x)}{1/f(x)}$ (form $\dfrac{\infty}{\infty}$).

7. $\displaystyle\lim_{x\to 0^+}x\ln x$ equals:
   - a) $-\infty$
   - b) $1$
   - c) $0$
   - d) $+\infty$

   > **Correct answer: c)** Although $\ln x\to -\infty$, the rate at which $x\to 0$ dominates: $x\ln x\to 0$.

---

#### 6.2.6 Indeterminate form 1^∞: exponential technique

**Worked Example**

Calculate $\displaystyle\lim_{x \to 0}(1 + 3x)^{1/x}$.

**Solution:**

Form $1^\infty$: when $x \to 0$, the base $1+3x \to 1$ and the exponent $1/x \to \infty$.

**Exponential method:** We write $(1+3x)^{1/x} = e^{\frac{1}{x}\ln(1+3x)}$.

We calculate the limit of the exponent:
$$\lim_{x \to 0} \frac{\ln(1+3x)}{x}$$

Form $\dfrac{0}{0}$. We apply L'Hôpital (or use the fundamental limit $\ln(1+u) \approx u$ for $u \to 0$):

$$\lim_{x \to 0} \frac{\ln(1+3x)}{x} = \lim_{x \to 0} \frac{3/(1+3x)}{1} = 3$$

Therefore:
$$\lim_{x \to 0}(1+3x)^{1/x} = e^3$$

---

**Exercises with Solutions**

**Basic Level:**

1. Calculate $\displaystyle\lim_{x \to \infty}\left(1 + \dfrac{1}{x}\right)^x$ (fundamental limit of $e$).

   > **Solution:** Form $1^\infty$. Exponent: $x\cdot\ln(1+1/x) = \dfrac{\ln(1+1/x)}{1/x}$.  
   > With $u = 1/x \to 0$: $\dfrac{\ln(1+u)}{u} \to 1$. Therefore: $e^1 = e$.

2. Calculate $\displaystyle\lim_{x\to 0}(1+5x)^{2/x}$.

   > **Solution:** Exponent: $\dfrac{2}{x}\ln(1+5x) = 2\cdot\dfrac{\ln(1+5x)}{x} \to 2\cdot 5 = 10$.  
   > Result: $e^{10}$.

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x \to +\infty}\left(\dfrac{x+2}{x-1}\right)^x$.

   > **Solution:** Form $1^\infty$. We write $\dfrac{x+2}{x-1} = 1 + \dfrac{3}{x-1}$.  
   > Exponent: $x\ln\left(1+\dfrac{3}{x-1}\right) \approx x\cdot\dfrac{3}{x-1} = \dfrac{3x}{x-1} \to 3$.  
   > Result: $e^3$.

4. Calculate $\displaystyle\lim_{x \to 0}\left(\cos x\right)^{1/x^2}$.

   > **Solution:** Exponent: $\dfrac{\ln(\cos x)}{x^2}$. Form $\dfrac{0}{0}$.  
   > L'Hôpital: $\dfrac{-\sin x/\cos x}{2x} = \dfrac{-\tan x}{2x} \to \dfrac{-1}{2}$.  
   > Result: $e^{-1/2} = \dfrac{1}{\sqrt{e}}$.

**EVAU Level:**

5. **(EVAU Madrid style)** Calculate the following limits with indeterminate form $1^\infty$:

   a) $\displaystyle\lim_{x\to\infty}\left(1 - \dfrac{2}{x}\right)^{3x}$  
   b) $\displaystyle\lim_{x\to 0}\dfrac{(1+x)^{1/x} - e}{x}$ (Only calculate the limit of the internal $1^\infty$ form)

   > **Solution:**
   >
   > **a)** Exponent: $3x\ln\left(1-\dfrac{2}{x}\right)$.  
   > With $u = -2/x \to 0$: $3x\ln(1+u) \approx 3x\cdot u = 3x\cdot(-2/x) = -6$.  
   > Result: $e^{-6}$.
   >
   > **b)** To calculate $(1+x)^{1/x}$ when $x\to 0$: exponent $= \dfrac{\ln(1+x)}{x}$.  
   > Expanding $\ln(1+x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \cdots$:  
   > $\dfrac{\ln(1+x)}{x} = 1 - \dfrac{x}{2} + O(x^2)$.  
   > $(1+x)^{1/x} = e^{1 - x/2 + O(x^2)} = e\cdot e^{-x/2+O(x^2)} \approx e(1 - x/2 + \cdots)$.  
   > $\dfrac{(1+x)^{1/x}-e}{x} \approx \dfrac{e(1-x/2)-e}{x} = \dfrac{-ex/2}{x} = -\dfrac{e}{2}$.  
   > Therefore: $\displaystyle\lim_{x\to 0}\dfrac{(1+x)^{1/x}-e}{x} = -\dfrac{e}{2}$.

**Multiple Choice Test**

6. To calculate a limit of the form $\displaystyle\lim f(x)^{g(x)}$ with form $1^\infty$, the correct procedure begins by:
   - a) Taking natural logarithms and calculating $\displaystyle\lim g(x)\ln f(x)$
   - b) Raising $f$ and $g$ separately
   - c) Applying L'Hôpital directly to $f^g$
   - d) Substituting directly

   > **Correct answer: a)** We write $f^g = e^{g\ln f}$ and calculate the limit of the exponent $g\ln f$, which usually gives the form $\infty\cdot 0$.

7. $\displaystyle\lim_{x\to\infty}\left(1+\dfrac{a}{x}\right)^x = $
   - a) $a$
   - b) $e^a$
   - c) $1$
   - d) $e$

   > **Correct answer: b)** This is the generalisation of the fundamental limit: $\left(1+\dfrac{a}{x}\right)^x \to e^a$.

---

## 6.3 Limits at infinity and asymptotes

---

#### 6.3.1 Limit of a function as x → ±∞

**Worked Example**

Calculate $\displaystyle\lim_{x \to +\infty}\dfrac{3x^2 - 2x + 1}{x^2 + 5x - 3}$ and $\displaystyle\lim_{x \to -\infty}\dfrac{2x^3 - 1}{x^2 + 1}$.

**Solution:**

**First limit:** Form $\dfrac{\infty}{\infty}$. We divide numerator and denominator by the highest power ($x^2$):

$$\lim_{x \to +\infty}\frac{3x^2-2x+1}{x^2+5x-3} = \lim_{x \to +\infty}\frac{3 - 2/x + 1/x^2}{1 + 5/x - 3/x^2} = \frac{3-0+0}{1+0-0} = 3$$

**Second limit:** Form $\dfrac{-\infty}{\infty}$. We divide by $x^2$:

$$\lim_{x \to -\infty}\frac{2x^3-1}{x^2+1} = \lim_{x \to -\infty}\frac{2x - 1/x^2}{1+1/x^2} = \lim_{x \to -\infty}(2x) = -\infty$$

(The degree of the numerator exceeds that of the denominator.)

---

**Exercises with Solutions**

**Basic Level:**

1. Calculate $\displaystyle\lim_{x\to+\infty}\dfrac{5x+3}{2x-1}$.

   > **Solution:** Dividing by $x$: $\dfrac{5+3/x}{2-1/x} \to \dfrac{5}{2}$.

2. Calculate $\displaystyle\lim_{x\to-\infty}(3x^2 - 2x + 7)$.

   > **Solution:** The dominant term is $3x^2$. When $x\to-\infty$, $x^2\to+\infty$, so the limit is $+\infty$.

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x\to+\infty}\dfrac{4x^3-x}{2x^3+3x^2-1}$.

   > **Solution:** Same degree. Dividing by $x^3$: $\dfrac{4-1/x^2}{2+3/x-1/x^3} \to \dfrac{4}{2} = 2$.

4. Calculate $\displaystyle\lim_{x\to-\infty}\dfrac{x^2-1}{\sqrt{x^4+2}}$.

   > **Solution:** For $x\to-\infty$, $x^2 = |x|^2$. Dividing by $x^2$:  
   > $\dfrac{1-1/x^2}{\sqrt{1+2/x^4}} \to \dfrac{1}{\sqrt{1}} = 1$.

**EVAU Level:**

5. **(EVAU Madrid style)** Calculate, justifying each step:

   a) $\displaystyle\lim_{x\to+\infty}\dfrac{x^2+3x-1}{2x^2-x+4}$  
   b) $\displaystyle\lim_{x\to-\infty}\dfrac{x^3-2}{x^2+1}$  
   c) $\displaystyle\lim_{x\to+\infty}\left(\sqrt{x^2+x}-x\right)$

   > **Solution:**
   >
   > **a)** Same degree ($2$). Ratio of leading coefficients: $\dfrac{1}{2}$.
   >
   > **b)** Degree of numerator ($3$) $>$ degree of denominator ($2$). The dominant term is $\dfrac{x^3}{x^2} = x \to -\infty$.
   >
   > **c)** Form $\infty-\infty$. Rationalising:  
   > $\dfrac{(x^2+x)-x^2}{\sqrt{x^2+x}+x} = \dfrac{x}{\sqrt{x^2+x}+x}$. Dividing by $x>0$:  
   > $\dfrac{1}{\sqrt{1+1/x}+1} \to \dfrac{1}{2}$.

**Multiple Choice Test**

6. $\displaystyle\lim_{x\to+\infty}\dfrac{3x^4 - 2x}{x^4+1}$ equals:
   - a) $0$
   - b) $3$
   - c) $+\infty$
   - d) $-2$

   > **Correct answer: b)** Same degree in numerator and denominator: the limit is the ratio of the leading coefficients: $\dfrac{3}{1} = 3$.

7. If the degree of the numerator is less than the degree of the denominator in a rational function, the limit as $x\to\pm\infty$ is:
   - a) $\pm\infty$
   - b) The ratio of the leading coefficients
   - c) $0$
   - d) $1$

   > **Correct answer: c)** If $\deg(\text{num}) < \deg(\text{den})$, the numerator grows more slowly and the limit is $0$.

---

#### 6.3.2 Horizontal asymptote: definition and calculation

**Worked Example**

Find the horizontal asymptotes of $f(x) = \dfrac{2x^2 - 3}{x^2 + x + 1}$.

**Solution:**

A line $y = L$ is a **horizontal asymptote** if $\displaystyle\lim_{x\to+\infty}f(x) = L$ or $\displaystyle\lim_{x\to-\infty}f(x) = L$.

**As $x \to +\infty$:**
$$\lim_{x\to+\infty}\frac{2x^2-3}{x^2+x+1} = \lim_{x\to+\infty}\frac{2-3/x^2}{1+1/x+1/x^2} = \frac{2}{1} = 2$$

**As $x \to -\infty$:**
$$\lim_{x\to-\infty}\frac{2x^2-3}{x^2+x+1} = 2 \quad \text{(same calculation)}$$

The function has **a single horizontal asymptote**: $y = 2$.

**Verification:** Since the function is rational with numerator and denominator of the same degree, the limit in both infinities coincides with the ratio of the leading coefficients: $\dfrac{2}{1} = 2$.

---

**Exercises with Solutions**

**Basic Level:**

1. Find the horizontal asymptotes of $f(x) = \dfrac{x+1}{x-2}$.

   > **Solution:** $\displaystyle\lim_{x\to\pm\infty}\dfrac{x+1}{x-2} = 1$. Horizontal asymptote: $y = 1$.

2. Determine whether $f(x) = \dfrac{2x+1}{x^2+1}$ has a horizontal asymptote.

   > **Solution:** $\displaystyle\lim_{x\to\pm\infty}\dfrac{2x+1}{x^2+1} = 0$ (degree of num. $<$ degree of den.). Horizontal asymptote: $y = 0$ (the $x$-axis).

**Intermediate Level:**

3. Find the horizontal asymptotes of $f(x) = \dfrac{3x}{\sqrt{x^2+4}}$.

   > **Solution:**  
   > For $x\to+\infty$: $\sqrt{x^2+4} \approx x$, so $\dfrac{3x}{\sqrt{x^2+4}} \to 3$.  
   > For $x\to-\infty$: $\sqrt{x^2+4} = \sqrt{x^2}\sqrt{1+4/x^2} = |x|\sqrt{1+4/x^2} = -x\sqrt{1+4/x^2}$ (since $x < 0$), so $\dfrac{3x}{-x} = -3$.  
   > **Two horizontal asymptotes**: $y = 3$ (at $+\infty$) and $y = -3$ (at $-\infty$).

4. Calculate the horizontal asymptotes of $f(x) = \arctan x$.

   > **Solution:** $\displaystyle\lim_{x\to+\infty}\arctan x = \dfrac{\pi}{2}$ and $\displaystyle\lim_{x\to-\infty}\arctan x = -\dfrac{\pi}{2}$.  
   > **Two horizontal asymptotes**: $y = \dfrac{\pi}{2}$ and $y = -\dfrac{\pi}{2}$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \dfrac{x^2 - 4x + 3}{x^2 - 1}$.

   a) Calculate $\displaystyle\lim_{x\to\pm\infty}f(x)$ and state the horizontal asymptotes.  
   b) Simplify $f(x)$ for $x\neq\pm 1$ and determine whether the asymptote is reached.  
   c) For what values of $x$ is $f(x) = 1$?

   > **Solution:**
   >
   > **a)** $\displaystyle\lim_{x\to\pm\infty}\dfrac{x^2-4x+3}{x^2-1} = 1$. Horizontal asymptote: $y = 1$.
   >
   > **b)** $x^2-4x+3 = (x-1)(x-3)$ and $x^2-1 = (x-1)(x+1)$:  
   > $f(x) = \dfrac{(x-1)(x-3)}{(x-1)(x+1)} = \dfrac{x-3}{x+1}$ for $x\neq 1$.  
   > The asymptote $y=1$ is not reached (the function never equals $1$ in its domain, as we will see in c).
   >
   > **c)** $\dfrac{x-3}{x+1} = 1 \Rightarrow x-3 = x+1 \Rightarrow -3 = 1$: impossible. The function **never takes the value $1$**, confirming that the asymptote is not reached.

**Multiple Choice Test**

6. A rational function $\dfrac{p(x)}{q(x)}$ has a horizontal asymptote different from $0$ when:
   - a) $\deg p > \deg q$
   - b) $\deg p = \deg q$
   - c) $\deg p < \deg q$
   - d) $\deg p = 0$

   > **Correct answer: b)** If the degrees are equal, the horizontal asymptote is the ratio of the leading coefficients (different from $0$). If $\deg p < \deg q$, the asymptote is $y=0$.

7. The function $f(x) = e^{-x}$ has:
   - a) Horizontal asymptote $y = 0$ only at $+\infty$
   - b) Horizontal asymptote $y = 0$ at both infinities
   - c) Horizontal asymptote $y = 1$ at $+\infty$
   - d) No horizontal asymptotes

   > **Correct answer: a)** $\displaystyle\lim_{x\to+\infty}e^{-x} = 0$ (asymptote $y=0$) and $\displaystyle\lim_{x\to-\infty}e^{-x} = +\infty$ (no asymptote at $-\infty$).

---

#### 6.3.3 Vertical asymptote: definition and calculation

**Worked Example**

Determine the vertical asymptotes of $f(x) = \dfrac{x + 1}{x^2 - x - 6}$.

**Solution:**

Vertical asymptotes occur where the denominator vanishes (and the numerator does not).

**Step 1:** Factor the denominator: $x^2 - x - 6 = (x-3)(x+2)$. Roots: $x = 3$ and $x = -2$.

**Step 2:** Check that the numerator does not vanish at those points:
- At $x = 3$: numerator $= 4 \neq 0$ ✓
- At $x = -2$: numerator $= -1 \neq 0$ ✓

**Step 3:** Calculate one-sided limits:

At $x = 3$:
- $\displaystyle\lim_{x\to 3^+}\frac{x+1}{(x-3)(x+2)} = \frac{4}{0^+\cdot 5} = +\infty$
- $\displaystyle\lim_{x\to 3^-}\frac{x+1}{(x-3)(x+2)} = \frac{4}{0^-\cdot 5} = -\infty$

At $x = -2$:
- $\displaystyle\lim_{x\to -2^+}\frac{x+1}{(x-3)(x+2)} = \frac{-1}{(-5)\cdot 0^+} = +\infty$
- $\displaystyle\lim_{x\to -2^-}\frac{x+1}{(x-3)(x+2)} = \frac{-1}{(-5)\cdot 0^-} = -\infty$

**Conclusion:** The function has two vertical asymptotes: $x = 3$ and $x = -2$.

---

**Exercises with Solutions**

**Basic Level:**

1. Find the vertical asymptotes of $f(x) = \dfrac{1}{x^2-4}$.

   > **Solution:** Denominator $= 0 \Rightarrow x = \pm 2$. Numerator $= 1 \neq 0$ at both.  
   > Vertical asymptotes: $x = 2$ and $x = -2$.

2. Determine the vertical asymptotes of $g(x) = \tan x$ on $[-\pi, \pi]$.

   > **Solution:** $\tan x = \dfrac{\sin x}{\cos x}$. The denominator $\cos x = 0$ at $x = \pm\dfrac{\pi}{2}$.  
   > Vertical asymptotes: $x = \dfrac{\pi}{2}$ and $x = -\dfrac{\pi}{2}$.

**Intermediate Level:**

3. Find the vertical asymptotes of $h(x) = \dfrac{x^2-1}{x^2+x}$ and state whether there is a hole (removable discontinuity).

   > **Solution:** $x^2+x = x(x+1) = 0 \Rightarrow x = 0$ or $x = -1$.  
   > $x^2-1 = (x-1)(x+1)$.  
   > At $x = -1$: numerator $= 0$ also; we must simplify: $\dfrac{(x-1)(x+1)}{x(x+1)} = \dfrac{x-1}{x}$.  
   > $\displaystyle\lim_{x\to -1}\dfrac{x-1}{x} = \dfrac{-2}{-1} = 2$: **removable discontinuity** at $x=-1$ (hole).  
   > At $x = 0$: numerator $= -1\neq 0$. $\displaystyle\lim_{x\to 0}\dfrac{x-1}{x} = \pm\infty$: **vertical asymptote** $x=0$.

4. Determine the vertical asymptotes of $f(x) = \ln(x-2)$.

   > **Solution:** The domain is $x > 2$. $\displaystyle\lim_{x\to 2^+}\ln(x-2) = -\infty$. Vertical asymptote: $x = 2$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \dfrac{x^2+x-2}{x^2-3x+2}$.

   a) Factor numerator and denominator.  
   b) Find the domain of $f$.  
   c) Determine whether there are removable discontinuities or vertical asymptotes at each point where $f$ is undefined.

   > **Solution:**
   >
   > **a)** Numerator: $x^2+x-2 = (x+2)(x-1)$. Denominator: $x^2-3x+2 = (x-1)(x-2)$.
   >
   > **b)** Dom$(f) = \mathbb{R}\setminus\{1, 2\}$.
   >
   > **c)** At $x = 1$: numerator $= 0$ also. Simplifying: $\dfrac{(x+2)(x-1)}{(x-1)(x-2)} = \dfrac{x+2}{x-2}$.  
   > $\displaystyle\lim_{x\to 1}\dfrac{x+2}{x-2} = \dfrac{3}{-1} = -3$. **Removable discontinuity** at $x=1$ (hole at $y=-3$).  
   > At $x = 2$: simplified numerator $= x+2 = 4 \neq 0$. $\displaystyle\lim_{x\to 2^+}\dfrac{x+2}{x-2} = +\infty$; $\displaystyle\lim_{x\to 2^-}\dfrac{x+2}{x-2} = -\infty$. **Vertical asymptote** $x = 2$.

**Multiple Choice Test**

6. A rational function has a vertical asymptote at $x = a$ when:
   - a) The numerator vanishes at $x = a$
   - b) The denominator vanishes at $x = a$ and the numerator does not
   - c) Both numerator and denominator vanish at $x = a$
   - d) The function is not defined at $x = a$

   > **Correct answer: b)** If the numerator also vanishes, there may be a removable discontinuity (the factor is cancelled). A vertical asymptote only occurs when only the denominator vanishes.

7. If $\displaystyle\lim_{x\to a^+}f(x) = +\infty$ and $\displaystyle\lim_{x\to a^-}f(x) = +\infty$, then:
   - a) The line $x = a$ is a vertical asymptote
   - b) The line $y = a$ is a horizontal asymptote
   - c) $f(a) = +\infty$
   - d) $f$ has a maximum at $x = a$

   > **Correct answer: a)** The vertical line $x = a$ is a vertical asymptote of the function (both branches tend to $+\infty$, in this case from the same side).

---

#### 6.3.4 Oblique asymptote: existence condition and calculation of m and n

**Worked Example**

Find the oblique asymptote of $f(x) = \dfrac{x^2 - 3x + 2}{x + 1}$.

**Solution:**

A function has an oblique asymptote $y = mx + n$ when $\displaystyle\lim_{x\to\infty}[f(x) - (mx+n)] = 0$.

Oblique asymptotes exist when the degree of the numerator exceeds that of the denominator by exactly 1.

**Step 1:** Calculate $m$:
$$m = \lim_{x\to+\infty}\frac{f(x)}{x} = \lim_{x\to+\infty}\frac{x^2-3x+2}{x(x+1)} = \lim_{x\to+\infty}\frac{x^2-3x+2}{x^2+x} = 1$$

**Step 2:** Calculate $n$:
$$n = \lim_{x\to+\infty}[f(x) - mx] = \lim_{x\to+\infty}\left[\frac{x^2-3x+2}{x+1} - x\right] = \lim_{x\to+\infty}\frac{x^2-3x+2 - x(x+1)}{x+1}$$

$$= \lim_{x\to+\infty}\frac{x^2-3x+2 - x^2 - x}{x+1} = \lim_{x\to+\infty}\frac{-4x+2}{x+1} = -4$$

**Oblique asymptote:** $y = x - 4$

**Verification by division:** $\dfrac{x^2-3x+2}{x+1}$. Dividing: $x^2-3x+2 = (x+1)(x-4)+6$. So $f(x) = x-4+\dfrac{6}{x+1}$, which confirms the asymptote $y = x-4$.

---

**Exercises with Solutions**

**Basic Level:**

1. Find the oblique asymptote of $f(x) = \dfrac{x^2+1}{x}$.

   > **Solution:** Division: $\dfrac{x^2+1}{x} = x + \dfrac{1}{x}$. Oblique asymptote: $y = x$.

2. Determine the oblique asymptote of $g(x) = \dfrac{x^2-x+3}{x-2}$.

   > **Solution:** Polynomial division: $x^2-x+3 = (x-2)(x+1)+5$. So $g(x) = x+1+\dfrac{5}{x-2}$.  
   > Oblique asymptote: $y = x+1$.

**Intermediate Level:**

3. Find all asymptotes of $f(x) = \dfrac{x^2}{x+1}$.

   > **Solution:** VA: $x = -1$. HA: none (degree of num. $>$ degree of den.). OA: $m=1$, $n = \lim(f(x)-x)=\lim\dfrac{x^2-(x^2+x)}{x+1}=\lim\dfrac{-x}{x+1}=-1$. Oblique asymptote: $y=x-1$.

4. When does an oblique asymptote exist but not a horizontal asymptote in a rational function?

   > **Solution:** When the degree of the numerator exceeds that of the denominator by exactly $1$. In that case:  
   > - If $\deg(\text{num}) = \deg(\text{den})$: horizontal asymptote  
   > - If $\deg(\text{num}) = \deg(\text{den}) + 1$: oblique asymptote  
   > - If $\deg(\text{num}) > \deg(\text{den}) + 1$: neither HA nor OA

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \dfrac{2x^2-x+1}{x-1}$.

   a) Find the domain and vertical asymptotes.  
   b) Determine the oblique asymptotes (verify that there are no horizontal asymptotes).  
   c) Calculate $f'(x)$ and determine whether there are relative extrema.

   > **Solution:**
   >
   > **a)** Dom $= \mathbb{R}\setminus\{1\}$. VA: $x=1$ (num. at $x=1$: $2-1+1=2\neq 0$).
   >
   > **b)** Division: $2x^2-x+1 = (x-1)(2x+1)+2$. So $f(x) = 2x+1+\dfrac{2}{x-1}$.  
   > OA: $y = 2x+1$.  
   > There is no HA because the degree of the numerator ($2$) exceeds that of the denominator ($1$) by more than $0$.
   >
   > **c)** $f'(x) = \left(2x+1+\dfrac{2}{x-1}\right)' = 2 - \dfrac{2}{(x-1)^2}$.  
   > $f'(x) = 0 \Rightarrow 2 = \dfrac{2}{(x-1)^2} \Rightarrow (x-1)^2 = 1 \Rightarrow x = 0$ or $x = 2$.  
   > $f''(x) = \dfrac{4}{(x-1)^3}$. $f''(0) = \dfrac{4}{-1} = -4 < 0$: **relative maximum** at $x=0$, $f(0)=-1$.  
   > $f''(2) = \dfrac{4}{1} = 4 > 0$: **relative minimum** at $x=2$, $f(2)=5$.

**Multiple Choice Test**

6. The formula for calculating the slope $m$ of the oblique asymptote is:
   - a) $m = \displaystyle\lim_{x\to\infty}f(x)$
   - b) $m = \displaystyle\lim_{x\to\infty}\dfrac{f(x)}{x}$
   - c) $m = f'(0)$
   - d) $m = \displaystyle\lim_{x\to\infty}f'(x)$

   > **Correct answer: b)** The slope of the oblique asymptote is calculated as $m = \lim_{x\to\infty}\dfrac{f(x)}{x}$.

7. The function $f(x) = \dfrac{x^3+1}{x^2}$:
   - a) Has horizontal asymptote $y=0$
   - b) Has oblique asymptote $y=x$
   - c) Has neither oblique nor horizontal asymptotes
   - d) Has horizontal asymptote $y=1$

   > **Correct answer: b)** $f(x) = x + \dfrac{1}{x^2}$. The oblique asymptote is $y = x$ (the remainder $1/x^2\to 0$).

---

#### 6.3.5 Asymptotes of rational functions

**Worked Example**

Determine all asymptotes of $f(x) = \dfrac{x^2+2x}{x^2-1}$ and describe the behaviour of $f$ near each one.

**Solution:**

**Vertical asymptotes:** $x^2-1 = (x-1)(x+1) = 0 \Rightarrow x = 1, x = -1$.
- $x^2+2x = x(x+2)$: at $x=1$: $1\cdot3=3\neq0$; at $x=-1$: $(-1)(1)=-1\neq0$.
- VA: $x = 1$ and $x = -1$.

**Horizontal asymptote** (same degrees): $\displaystyle\lim_{x\to\pm\infty}\dfrac{x^2+2x}{x^2-1} = 1$. HA: $y = 1$.

(No OA because the horizontal limit exists with a finite value.)

**Behaviour near the VA:**
- Near $x=1$: $f(x) \approx \dfrac{3}{(x-1)\cdot 2}$. For $x\to1^+$: $+\infty$; for $x\to1^-$: $-\infty$.
- Near $x=-1$: $f(x) \approx \dfrac{-1}{(x+1)\cdot(-2)} = \dfrac{1}{2(x+1)}$. For $x\to-1^+$: $+\infty$; for $x\to-1^-$: $-\infty$.

---

**Exercises with Solutions**

**Basic Level:**

1. Find all asymptotes of $f(x) = \dfrac{1}{x-3}$.

   > **Solution:** VA: $x=3$. HA: $y=0$ (degree of num. $<$ degree of den.).

2. Determine the asymptotes of $g(x) = \dfrac{2x+1}{x+2}$.

   > **Solution:** VA: $x=-2$. HA: $y=2$ (same degrees; $2/1=2$).

**Intermediate Level:**

3. Find all asymptotes of $f(x) = \dfrac{x^2-4}{x-1}$.

   > **Solution:** VA: $x=1$ (num. at $x=1$: $1-4=-3\neq0$). No HA (degree of num. $>$ degree of den.).  
   > Division: $x^2-4 = (x-1)(x+1)-3$, so OA: $y=x+1$.

4. Analyse the asymptotes of $h(x) = \dfrac{x^3}{x^2-4}$.

   > **Solution:** VA: $x=2$ and $x=-2$. No HA. Degree of num. $-$ degree of den. $=1$: OA.  
   > $m = \lim\dfrac{x^3}{x(x^2-4)} = \lim\dfrac{x^2}{x^2-4} = 1$. $n = \lim(f(x)-x) = \lim\dfrac{x^3-x(x^2-4)}{x^2-4} = \lim\dfrac{4x}{x^2-4} = 0$.  
   > OA: $y = x$.

**EVAU Level:**

5. **(EVAU Madrid style)** Fully study the asymptotes of $f(x) = \dfrac{x^2-x-6}{x^2-4}$ and state what type of discontinuity it has at each singular point.

   > **Solution:**
   >
   > We factor: $x^2-x-6 = (x-3)(x+2)$ and $x^2-4 = (x-2)(x+2)$.
   >
   > Singular points: $x = 2$ and $x = -2$.
   >
   > **At $x = -2$:** Numerator $= 0$ also. $f(x) = \dfrac{(x-3)(x+2)}{(x-2)(x+2)} = \dfrac{x-3}{x-2}$ for $x\neq-2$.  
   > $\displaystyle\lim_{x\to-2}\dfrac{x-3}{x-2} = \dfrac{-5}{-4} = \dfrac{5}{4}$. **Removable discontinuity** (hole at $y=5/4$).
   >
   > **At $x = 2$:** Simplified numerator $= x-3 = -1\neq 0$. VA: $x=2$.  
   > $\displaystyle\lim_{x\to2^+}\dfrac{x-3}{x-2} = \dfrac{-1}{0^+} = -\infty$; $\displaystyle\lim_{x\to2^-}\dfrac{x-3}{x-2} = \dfrac{-1}{0^-} = +\infty$.
   >
   > **HA:** $\displaystyle\lim_{x\to\pm\infty}\dfrac{x-3}{x-2} = 1$. HA: $y=1$.
   >
   > **Summary:** VA: $x=2$; HA: $y=1$; removable discontinuity at $x=-2$.

**Multiple Choice Test**

6. An irreducible rational function (with no common factors between numerator and denominator) of degree $3$ in numerator and $3$ in denominator:
   - a) Has an oblique asymptote
   - b) Has horizontal asymptote $y=0$
   - c) Has a horizontal asymptote equal to the ratio of the leading coefficients
   - d) Has no asymptotes

   > **Correct answer: c)** Same degree: the horizontal asymptote is the ratio of the coefficients of the term with the highest degree.

7. If $f(x) = \dfrac{p(x)}{q(x)}$ with $\deg p = 4$ and $\deg q = 2$, then:
   - a) It has a horizontal asymptote
   - b) It has an oblique asymptote
   - c) It has no asymptotes at infinity
   - d) It has a quadratic oblique asymptote

   > **Correct answer: c)** With degree of numerator $= 4$ and denominator $= 2$, the difference is $2 > 1$, so **there is neither a horizontal nor an oblique asymptote** (the quotient grows without bound).

---

#### 6.3.6 Asymptotes of piecewise-defined functions

**Worked Example**

Determine the asymptotes of $f(x) = \begin{cases} \dfrac{x^2-1}{x+1} & \text{if } x < 1 \\ \dfrac{2x}{x-3} & \text{if } x \geq 1 \end{cases}$

**Solution:**

**Vertical asymptotes:**
- For $x < 1$: $\dfrac{x^2-1}{x+1} = \dfrac{(x-1)(x+1)}{x+1} = x-1$ (for $x \neq -1$). At $x = -1 < 1$: there is a removable discontinuity ($\lim = -2$, no VA).
- For $x \geq 1$: $\dfrac{2x}{x-3}$. At $x=3\geq 1$: numerator $= 6\neq 0$. **VA: $x = 3$**.

**Horizontal asymptotes:**
- When $x \to -\infty$ (branch $x<1$): $f(x) = x-1 \to -\infty$. No HA at $-\infty$.
- When $x \to +\infty$ (branch $x\geq 1$): $\displaystyle\lim_{x\to+\infty}\dfrac{2x}{x-3} = 2$. **HA: $y = 2$** at $+\infty$.

**Oblique asymptote (at $-\infty$):** The branch $x < 1$ is $f(x) = x - 1$ (a line). Strictly speaking, $y = x - 1$ **is itself the asymptote** (or more precisely: the function is a line for $x < 1$, not a separate asymptote from it).

---

**Exercises with Solutions**

**Basic Level:**

1. Find the horizontal asymptotes of $f(x) = \begin{cases} e^x & \text{if } x < 0 \\ \dfrac{x+1}{x+2} & \text{if } x \geq 0 \end{cases}$

   > **Solution:**  
   > $x\to-\infty$: $e^x\to 0$. HA: $y=0$ at $-\infty$.  
   > $x\to+\infty$: $\dfrac{x+1}{x+2}\to 1$. HA: $y=1$ at $+\infty$.

2. Determine whether $g(x) = \begin{cases} \ln x & \text{if } x > 0 \\ x^2 & \text{if } x \leq 0 \end{cases}$ has vertical asymptotes.

   > **Solution:** For $x\leq 0$: $x^2$ is continuous, with no singularities.  
   > For $x>0$: $\ln x$ with $\displaystyle\lim_{x\to 0^+}\ln x = -\infty$. **VA: $x=0$** (from the right).

**Intermediate Level:**

3. Find all asymptotes of $f(x) = \begin{cases} \dfrac{1}{x} & \text{if } x < -1 \\ 2 & \text{if } -1\leq x\leq 1 \\ \dfrac{x^2}{x+1} & \text{if } x > 1 \end{cases}$

   > **Solution:**  
   > **VA:** For $x<-1$: $1/x$ with no zeros in denominator. For $x>1$: $\dfrac{x^2}{x+1}$, den. $=0$ at $x=-1\notin(1,+\infty)$. No VA.  
   > **HA at $-\infty$:** $\lim_{x\to-\infty}1/x=0$. HA: $y=0$.  
   > **OA at $+\infty$:** $\dfrac{x^2}{x+1}=x-1+\dfrac{1}{x+1}$. OA: $y=x-1$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \begin{cases} \dfrac{x^2-4}{x-2} & \text{if } x < 0 \\ \dfrac{3x+a}{x+b} & \text{if } x \geq 0 \end{cases}$

   a) Simplify the first branch and find possible discontinuities for $x<0$.  
   b) Determine the horizontal asymptote of the second branch as $x\to+\infty$ as a function of $a$ and $b$.  
   c) If the HA of the second branch is required to be $y=3$, what condition does that impose?

   > **Solution:**
   >
   > **a)** $\dfrac{x^2-4}{x-2}=\dfrac{(x-2)(x+2)}{x-2}=x+2$ for $x\neq 2$. Since the branch is $x<0$, there are no problematic points (the hole would be at $x=2>0$, outside the domain of the branch). No discontinuities for $x<0$.
   >
   > **b)** $\displaystyle\lim_{x\to+\infty}\dfrac{3x+a}{x+b} = 3$ (same degrees, ratio of leading coefficients $=3/1=3$).
   >
   > **c)** Regardless of $a$ and $b$ (with $b\neq 0$ for the domain), the HA at $+\infty$ **is always $y=3$**. The condition is already satisfied for any $a, b$.

**Multiple Choice Test**

6. A piecewise-defined function can have:
   - a) At most one horizontal asymptote
   - b) At most one vertical asymptote
   - c) Different asymptotes at $+\infty$ and $-\infty$
   - d) Only horizontal asymptotes

   > **Correct answer: c)** Having different expressions for $x\to+\infty$ and $x\to-\infty$, it can have different horizontal asymptotes (or even an oblique asymptote on one side and a horizontal asymptote on the other).

7. If $f(x) = e^{-|x|}$, then:
   - a) It has a vertical asymptote at $x=0$
   - b) It has horizontal asymptote $y=0$ only at $+\infty$
   - c) It has horizontal asymptote $y=0$ at both infinities
   - d) It has an oblique asymptote

   > **Correct answer: c)** $e^{-|x|}\to 0$ both as $x\to+\infty$ ($|x|=x$) and as $x\to-\infty$ ($|x|=-x$).

---

## 6.4 Continuity of functions

---

#### 6.4.1 Definition of continuity at a point: the three conditions

**Worked Example**

Study the continuity of $f(x) = \begin{cases} \dfrac{x^2-4}{x-2} & \text{if } x \neq 2 \\ 5 & \text{if } x = 2 \end{cases}$ at $x = 2$.

**Solution:**

A function is continuous at $x = a$ if **the three conditions** are satisfied:
1. $f(a)$ exists (the function is defined at $a$)
2. $\displaystyle\lim_{x\to a}f(x)$ exists
3. $\displaystyle\lim_{x\to a}f(x) = f(a)$

**Condition 1:** $f(2) = 5$. ✓ (defined)

**Condition 2:** $\displaystyle\lim_{x\to 2}\dfrac{x^2-4}{x-2} = \lim_{x\to 2}\dfrac{(x-2)(x+2)}{x-2} = \lim_{x\to 2}(x+2) = 4$. ✓ (the limit exists and equals $4$)

**Condition 3:** $\displaystyle\lim_{x\to 2}f(x) = 4 \neq 5 = f(2)$. ✗

The function **is not continuous** at $x = 2$: the limit exists but does not coincide with the value of the function. This is a **removable discontinuity**.

---

**Exercises with Solutions**

**Basic Level:**

1. Check whether $f(x) = x^2 - 3x + 2$ is continuous at $x = 1$.

   > **Solution:** It is a polynomial, continuous on all $\mathbb{R}$.  
   > (1) $f(1) = 1-3+2 = 0$. (2) $\lim_{x\to1}f(x)=0$. (3) They are equal. **Continuous**.

2. Study the continuity of $g(x) = \dfrac{x+1}{x-3}$ at $x = 3$.

   > **Solution:** $g(3)$ is not defined (denominator $=0$). Condition 1 fails. **Discontinuous** at $x=3$.

**Intermediate Level:**

3. Study the continuity of $f(x) = \begin{cases} x+1 & \text{if } x<2 \\ 3 & \text{if } x=2 \\ 2x-1 & \text{if } x>2 \end{cases}$ at $x=2$.

   > **Solution:** (1) $f(2)=3$. (2) $\lim_{x\to2^-}(x+1)=3$ and $\lim_{x\to2^+}(2x-1)=3$: limit $=3$. (3) $3=3$. **Continuous** at $x=2$.

4. Determine the value of $k$ for which $f(x) = \begin{cases} kx+1 & \text{if } x\leq 2 \\ x^2-1 & \text{if } x>2 \end{cases}$ is continuous at $x=2$.

   > **Solution:** $\lim_{x\to2^-}(kx+1)=2k+1$; $\lim_{x\to2^+}(x^2-1)=3$; $f(2)=2k+1$.  
   > For continuity: $2k+1=3 \Rightarrow k=1$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \begin{cases} \dfrac{x^2-1}{x-1} & \text{if } x < 1 \\ a & \text{if } x = 1 \\ 2x - b & \text{if } x > 1 \end{cases}$

   a) Calculate $\displaystyle\lim_{x\to 1^-}f(x)$.  
   b) Calculate $\displaystyle\lim_{x\to 1^+}f(x)$ as a function of $b$.  
   c) Determine $a$ and $b$ so that $f$ is continuous at $x = 1$.

   > **Solution:**
   >
   > **a)** $\dfrac{x^2-1}{x-1} = x+1 \to 2$.
   >
   > **b)** $2(1)-b = 2-b$.
   >
   > **c)** For the limit to exist: $2 = 2-b \Rightarrow b=0$.  
   > For continuity: $f(1) = a = \lim_{x\to1}f(x) = 2 \Rightarrow a=2$.  
   > **$a = 2$, $b = 0$**.

**Multiple Choice Test**

6. The three conditions for continuity of $f$ at $x = a$ are:
   - a) $f(a)$ exists, the limit exists, and $f'(a)$ exists
   - b) $f(a)$ exists, $\lim_{x\to a}f(x)$ exists, and $\lim_{x\to a}f(x)=f(a)$
   - c) $f(a)$ exists and $f'(a)$ exists
   - d) $\lim_{x\to a^-}f(x)=f(a)$ only

   > **Correct answer: b)** These are exactly the three conditions that define continuity at a point.

7. If $f(a)$ exists but $\displaystyle\lim_{x\to a}f(x)\neq f(a)$, then $f$:
   - a) Is continuous at $a$
   - b) Has a jump discontinuity at $a$
   - c) Has a removable discontinuity at $a$
   - d) Has an asymptote at $a$

   > **Correct answer: c)** If the limit exists but does not coincide with $f(a)$ (or if $f(a)$ is not defined but the limit is), the discontinuity is **removable** (it suffices to redefine $f(a)=L$).

---

#### 6.4.2 Types of discontinuity: removable, finite jump, infinite jump (essential)

**Worked Example**

Classify the discontinuities of $f(x) = \dfrac{x^2-x-2}{x^2-3x+2}$.

**Solution:**

**Domain:** $x^2-3x+2=(x-1)(x-2)=0 \Rightarrow x=1,\, x=2$.

We factor the numerator: $x^2-x-2=(x-2)(x+1)$.

$$f(x) = \frac{(x-2)(x+1)}{(x-1)(x-2)} = \frac{x+1}{x-1} \quad (x\neq 2)$$

**At $x=2$:** Both factors vanish; simplifying, $\displaystyle\lim_{x\to2}\dfrac{x+1}{x-1}=\dfrac{3}{1}=3$. The limit exists and is finite. $\Rightarrow$ **Removable discontinuity** at $x=2$.

**At $x=1$:** Only the denominator vanishes ($x+1|_{x=1}=2\neq0$).
- $\displaystyle\lim_{x\to1^+}\dfrac{x+1}{x-1}=+\infty$, $\displaystyle\lim_{x\to1^-}\dfrac{x+1}{x-1}=-\infty$.
$\Rightarrow$ **Infinite jump discontinuity** (essential / vertical asymptote) at $x=1$.

---

**Exercises with Solutions**

**Basic Level:**

1. Classify the discontinuity of $f(x) = \begin{cases} x+1 & \text{if } x<0 \\ x-1 & \text{if } x\geq 0 \end{cases}$ at $x=0$.

   > **Solution:** $\lim_{x\to0^-}(x+1)=1$; $\lim_{x\to0^+}(x-1)=-1$. Different finite one-sided limits.  
   > **Finite jump discontinuity** (jump $= |1-(-1)|=2$).

2. Classify the discontinuity of $g(x) = \begin{cases} \dfrac{\sin x}{x} & \text{if } x\neq 0 \\ 2 & \text{if } x=0 \end{cases}$

   > **Solution:** $\lim_{x\to0}\dfrac{\sin x}{x}=1$, but $g(0)=2\neq1$. The limit exists, but $\neq g(0)$.  
   > **Removable discontinuity** (it would suffice to define $g(0)=1$).

**Intermediate Level:**

3. Classify all discontinuities of $h(x) = \dfrac{x^2-4}{x(x-2)}$.

   > **Solution:** Denominator $=0$ at $x=0$ and $x=2$. $x^2-4=(x-2)(x+2)$.  
   > $h(x)=\dfrac{(x-2)(x+2)}{x(x-2)}=\dfrac{x+2}{x}$ for $x\neq2$.  
   > At $x=2$: $\lim=\dfrac{4}{2}=2$: **removable discontinuity**.  
   > At $x=0$: $\lim_{x\to0^+}\dfrac{x+2}{x}=+\infty$, $\lim_{x\to0^-}=-\infty$: **essential discontinuity** (infinite jump).

4. Can a function have a limit at $x=a$ and still be discontinuous? Give an example.

   > **Solution:** Yes. For example $f(x)=\begin{cases}x^2&x\neq1\\ 5&x=1\end{cases}$:  
   > $\lim_{x\to1}f(x)=1$ but $f(1)=5\neq1$. The limit exists but does not coincide with the value. **Removable discontinuity**.

**EVAU Level:**

5. **(EVAU Madrid style)** Classify all discontinuities of:
   $$f(x) = \begin{cases} \dfrac{1}{x+1} & \text{if } x < 0 \\ x^2 - 1 & \text{if } 0 \leq x < 2 \\ \dfrac{x-2}{x^2-4} & \text{if } x \geq 2 \end{cases}$$

   > **Solution:**
   >
   > **At $x=0$ (branch change):**  
   > $\lim_{x\to0^-}\dfrac{1}{x+1}=1$; $\lim_{x\to0^+}(x^2-1)=-1$; $f(0)=0-1=-1$.  
   > Different one-sided limits: **finite jump discontinuity** at $x=0$.
   >
   > **At $x=-1$** (den. $=0$ in the first branch for $x<0$):  
   > $\lim_{x\to-1}\dfrac{1}{x+1}=\pm\infty$: **essential discontinuity** at $x=-1$.
   >
   > **At $x=2$ (branch change and singular point):**  
   > Third branch: $\dfrac{x-2}{x^2-4}=\dfrac{x-2}{(x-2)(x+2)}=\dfrac{1}{x+2}$ for $x\neq2$.  
   > $\lim_{x\to2^+}\dfrac{1}{x+2}=\dfrac{1}{4}$; second branch: $\lim_{x\to2^-}(x^2-1)=3$; $f(2)=\dfrac{1}{4}$.  
   > Different one-sided limits: **finite jump discontinuity** at $x=2$ (jump $= |3-1/4|=11/4$).

**Multiple Choice Test**

6. A removable discontinuity at $x=a$ means that:
   - a) The function tends to $\pm\infty$ at $a$
   - b) The limit does not exist at $a$
   - c) The limit exists but $f(a)$ is not defined or does not coincide with it
   - d) The one-sided limits are different and finite

   > **Correct answer: c)** A removable discontinuity is characterised by the fact that $\lim_{x\to a}f(x)$ exists (finite), but either $f(a)$ is not defined, or $f(a)\neq\lim f$.

7. A finite jump discontinuity at $x=a$ occurs when:
   - a) $\lim_{x\to a}f(x) = \pm\infty$
   - b) The one-sided limits exist, are finite, but are different
   - c) $f(a)$ is not defined and the limit does not exist either
   - d) The function is periodic

   > **Correct answer: b)** The finite "jump" implies that the one-sided limits are different real numbers: $\lim_{x\to a^-}f(x)\neq\lim_{x\to a^+}f(x)$, both finite.

---

#### 6.4.3 Continuity of elementary functions and continuity on an interval

**Worked Example**

Determine the domain of continuity of $f(x) = \dfrac{\ln(x-1)}{x^2 - 5x + 6}$.

**Solution:**

The function is a quotient of elementary functions. It is continuous where:
1. It is defined (natural domain)
2. The denominator does not vanish

**Natural domain:**
- $\ln(x-1)$ requires $x - 1 > 0 \Rightarrow x > 1$
- $x^2-5x+6 = (x-2)(x-3) \neq 0 \Rightarrow x \neq 2, x \neq 3$

**Dom$(f) = (1, 2) \cup (2, 3) \cup (3, +\infty)$**

On this entire domain, $f$ is continuous (as a quotient of functions continuous in the domain, with non-vanishing denominator).

At $x = 2$ and $x = 3$: infinite jump discontinuities (vertical asymptotes).
At $x = 1$: does not belong to the domain; $\displaystyle\lim_{x\to1^+}\ln(x-1) = -\infty$ (vertical asymptote at $x=1$).

**Conclusion:** $f$ is continuous on $(1,2)\cup(2,3)\cup(3,+\infty)$.

---

**Exercises with Solutions**

**Basic Level:**

1. State the intervals of continuity of $f(x) = \sqrt{x^2-4}$.

   > **Solution:** $x^2-4\geq0 \Rightarrow x\leq-2$ or $x\geq2$. Dom $= (-\infty,-2]\cup[2,+\infty)$.  
   > $f$ is continuous on $(-\infty,-2)\cup(2,+\infty)$ (interior of the domain) and also at the endpoints $\pm2$ (one-sided continuity).

2. Where is $g(x) = \dfrac{1}{x^2-1}$ continuous?

   > **Solution:** Den. $=0$ at $x=\pm1$. Dom $= \mathbb{R}\setminus\{-1,1\}$.  
   > $g$ is continuous on $(-\infty,-1)\cup(-1,1)\cup(1,+\infty)$.

**Intermediate Level:**

3. Determine the intervals of continuity of $h(x) = \arcsin(2x-1)$.

   > **Solution:** $\arcsin(u)$ is continuous for $u\in[-1,1]$. We need $-1\leq 2x-1\leq1 \Rightarrow 0\leq x\leq1$.  
   > $h$ is continuous on $[0,1]$.

4. Justify that every polynomial function is continuous on $\mathbb{R}$.

   > **Solution:** A polynomial $p(x) = a_nx^n+\cdots+a_0$ is a sum of monomials $a_kx^k$. The function $x^k$ is continuous (product of continuous functions), and the sum of continuous functions is continuous. Moreover, for polynomials we can substitute directly: $\lim_{x\to a}p(x)=p(a)$ for all $a\in\mathbb{R}$. Therefore $p$ is continuous on all $\mathbb{R}$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \dfrac{\sqrt{x+2}}{(x-1)(x+3)}$.

   a) Determine the domain of $f$.  
   b) Study continuity at boundary points of the domain or discontinuities.  
   c) State the intervals of continuity.

   > **Solution:**
   >
   > **a)** $\sqrt{x+2}$ requires $x\geq-2$; den. $\neq0\Rightarrow x\neq1,-3$.  
   > Since $-3<-2$, the restriction $x\geq-2$ already excludes $x=-3$.  
   > Dom $= [-2,1)\cup(1,+\infty)$.
   >
   > **b)** At $x=-2$: $\displaystyle\lim_{x\to-2^+}f(x) = \dfrac{0}{(-3)(1)} = 0$: continuous at $x=-2$ (endpoint of domain).  
   > At $x=1$: den. $=0$, num. $=\sqrt{3}\neq0$. VA: essential discontinuity.
   >
   > **c)** $f$ is continuous on $[-2,1)\cup(1,+\infty)$.

**Multiple Choice Test**

6. Which of these statements about continuity of elementary functions is CORRECT?
   - a) $\ln x$ is continuous on $\mathbb{R}$
   - b) $\sin x$ is continuous only on $[-\pi,\pi]$
   - c) $e^x$ is continuous on $\mathbb{R}$
   - d) $\sqrt{x}$ is continuous on $\mathbb{R}$

   > **Correct answer: c)** $e^x$ is continuous on all $\mathbb{R}$. $\ln x$ is only continuous on $(0,+\infty)$; $\sin x$ is continuous on $\mathbb{R}$; $\sqrt{x}$ only on $[0,+\infty)$.

7. We say that $f$ is continuous on the closed interval $[a,b]$ if:
   - a) It is continuous on $(a,b)$, right-continuous at $a$ and left-continuous at $b$
   - b) It is continuous on $(a,b)$ only
   - c) $f(a)=f(b)$
   - d) It is differentiable on $[a,b]$

   > **Correct answer: a)** Continuity on $[a,b]$ requires continuity in the interior $(a,b)$ plus one-sided continuity at the endpoints: $\lim_{x\to a^+}f(x)=f(a)$ and $\lim_{x\to b^-}f(x)=f(b)$.

---

#### 6.4.4 Study of continuity of piecewise-defined functions

**Worked Example**

Study the continuity of:
$$f(x) = \begin{cases} x^2 - 2 & \text{if } x < -1 \\ x + 1 & \text{if } -1 \leq x \leq 2 \\ \dfrac{x^2-4}{x-2} & \text{if } x > 2 \end{cases}$$

**Solution:**

The problematic points are the branch changes: $x = -1$ and $x = 2$.

**At $x = -1$:**
- $\displaystyle\lim_{x\to-1^-}(x^2-2) = 1-2 = -1$
- $\displaystyle\lim_{x\to-1^+}(x+1) = 0$
- $f(-1) = -1+1 = 0$

The one-sided limits are $-1 \neq 0$: **finite jump discontinuity** at $x = -1$.

**At $x = 2$:**
- $\displaystyle\lim_{x\to2^-}(x+1) = 3$
- $\dfrac{x^2-4}{x-2} = x+2$ for $x\neq2$, so $\displaystyle\lim_{x\to2^+}(x+2) = 4$
- $f(2) = 2+1 = 3$

The one-sided limits are $3 \neq 4$: **finite jump discontinuity** at $x = 2$.

**Within each branch:** the functions $x^2-2$, $x+1$ and $\dfrac{x^2-4}{x-2}$ are continuous on their respective intervals.

**Conclusion:** $f$ is continuous on $\mathbb{R}\setminus\{-1, 2\}$.

---

**Exercises with Solutions**

**Basic Level:**

1. Study the continuity of $f(x) = \begin{cases} 2x+1 & \text{if } x\leq1 \\ x^2+2 & \text{if } x>1 \end{cases}$ at $x=1$.

   > **Solution:** $\lim_{x\to1^-}(2x+1)=3$; $\lim_{x\to1^+}(x^2+2)=3$; $f(1)=3$.  
   > All equal: **continuous** at $x=1$.

2. Study the continuity of $g(x)=\begin{cases} 3 & \text{if } x<0 \\ x+3 & \text{if } x\geq0 \end{cases}$ at $x=0$.

   > **Solution:** $\lim_{x\to0^-}3=3$; $\lim_{x\to0^+}(x+3)=3$; $f(0)=3$.  
   > All equal: **continuous** at $x=0$.

**Intermediate Level:**

3. Study the complete continuity of $f(x)=\begin{cases}|x|+1&\text{if }x\leq0\\x^2-x+1&\text{if }x>0\end{cases}$.

   > **Solution:** Only change point: $x=0$.  
   > $\lim_{x\to0^-}(|x|+1)=\lim_{x\to0^-}(-x+1)=1$; $\lim_{x\to0^+}(x^2-x+1)=1$; $f(0)=1$.  
   > **Continuous** at $x=0$ (and on all $\mathbb{R}$ by the continuity of each branch).

4. Find the points of discontinuity of $f(x) = \begin{cases} \frac{1}{x} & \text{if } x<-1 \text{ or } x>1 \\ x^2 & \text{if } -1\leq x\leq1 \end{cases}$.

   > **Solution:** Change points: $x=-1$ and $x=1$.  
   > At $x=-1$: $\lim_{x\to-1^-}\frac{1}{x}=-1$; $\lim_{x\to-1^+}x^2=1$; $f(-1)=1$. Different limits: **finite jump**.  
   > At $x=1$: $\lim_{x\to1^-}x^2=1$; $\lim_{x\to1^+}\frac{1}{x}=1$; $f(1)=1$. **Continuous** at $x=1$.

**EVAU Level:**

5. **(EVAU Madrid style)** $f(x) = \begin{cases}\dfrac{\sqrt{x+4}-2}{x} & \text{if }x\neq0 \\ k & \text{if }x=0\end{cases}$

   a) Calculate $\displaystyle\lim_{x\to0}f(x)$.  
   b) For what value of $k$ is $f$ continuous at $x=0$?  
   c) State the type of discontinuity if $k=1$.

   > **Solution:**
   >
   > **a)** Form $\dfrac{0}{0}$. Rationalising: $\dfrac{(\sqrt{x+4}-2)(\sqrt{x+4}+2)}{x(\sqrt{x+4}+2)} = \dfrac{x+4-4}{x(\sqrt{x+4}+2)} = \dfrac{1}{\sqrt{x+4}+2} \to \dfrac{1}{4}$.
   >
   > **b)** For continuity: $k = \dfrac{1}{4}$.
   >
   > **c)** With $k=1$: the limit is $\dfrac{1}{4}$ but $f(0)=1\neq\dfrac{1}{4}$. **Removable discontinuity**.

**Multiple Choice Test**

6. To study the continuity of a piecewise-defined function, the points that must always be analysed are:
   - a) The zeros of the function
   - b) The points where the expression of the function changes
   - c) The points where the derivative vanishes
   - d) The endpoints of the domain

   > **Correct answer: b)** The only points where there can be a discontinuity are the expression changes (and points where any branch is not continuous, such as singularities of rational functions).

7. If at a branch change point $x=c$, both one-sided limits equal $L$ and $f(c)=L$, then:
   - a) The function has a removable discontinuity at $c$
   - b) The function has a jump discontinuity at $c$
   - c) The function is continuous at $c$
   - d) The function is differentiable at $c$

   > **Correct answer: c)** All three conditions for continuity are satisfied: the limit exists, $f(c)$ exists, and they are equal.

---

#### 6.4.5 Calculation of parameters for a piecewise function to be continuous

**Worked Example**

Determine the values of $a$ and $b$ for the function to be continuous on all $\mathbb{R}$:
$$f(x) = \begin{cases} ax + 2 & \text{if } x < 1 \\ b & \text{if } x = 1 \\ x^2 + bx - a & \text{if } x > 1 \end{cases}$$

**Solution:**

For continuity at $x = 1$ the three conditions must be satisfied. The limit must exist and equal $f(1)$.

**Left-hand limit:**
$$\lim_{x\to1^-}(ax+2) = a+2$$

**Right-hand limit:**
$$\lim_{x\to1^+}(x^2+bx-a) = 1+b-a$$

**Value at $x=1$:** $f(1) = b$

**Equality of one-sided limits:**
$$a + 2 = 1 + b - a$$
$$2a - b = -1 \quad (1)$$

**Equality of the limit with $f(1)$:**
$$a + 2 = b$$
$$b = a + 2 \quad (2)$$

**Substituting (2) into (1):**
$$2a - (a+2) = -1 \Rightarrow a - 2 = -1 \Rightarrow a = 1$$

**From (2):** $b = 1 + 2 = 3$

**Verification:** With $a=1$, $b=3$:
- Left-hand limit: $1+2=3$ ✓
- Right-hand limit: $1+3-1=3$ ✓
- $f(1)=3$ ✓

**Answer:** $a = 1$, $b = 3$.

---

**Exercises with Solutions**

**Basic Level:**

1. Find $k$ so that $f(x)=\begin{cases}kx-1&\text{if }x\leq2\\x^2-1&\text{if }x>2\end{cases}$ is continuous at $x=2$.

   > **Solution:** $\lim_{x\to2^-}(kx-1)=2k-1$; $\lim_{x\to2^+}(x^2-1)=3$; $f(2)=2k-1$.  
   > $2k-1=3\Rightarrow k=2$.

2. Determine $m$ so that $g(x)=\begin{cases}mx^2&\text{if }x<1\\ 2x-1&\text{if }x\geq1\end{cases}$ is continuous on $\mathbb{R}$.

   > **Solution:** We only need to study $x=1$:  
   > $\lim_{x\to1^-}mx^2=m$; $\lim_{x\to1^+}(2x-1)=1$; $f(1)=1$. $m=1$.

**Intermediate Level:**

3. Find $a$ and $b$ so that $f(x)=\begin{cases}x^2+a&\text{if }x<0\\2&\text{if }x=0\\bx+3&\text{if }x>0\end{cases}$ is continuous at $x=0$.

   > **Solution:** $\lim_{x\to0^-}(x^2+a)=a$; $\lim_{x\to0^+}(bx+3)=3$; $f(0)=2$.  
   > For the limit to exist: $a=3$. For continuity: $a=2$. Contradiction: $a=3$ and $a=2$.  
   > Rephrasing: the equality of the limit implies $a=3$ and $f(0)=2\neq3$: **it cannot be made continuous** at $x=0$ for any value of $b$ (since $f(0)=2$ is fixed). Unless $f(0)$ is allowed to be free.  
   > If $f(0)$ could be free: we would need $a=3$ and $b$ can be any value. With $a=3$: $f(0)=2\neq3$: removable discontinuity at $x=0$ for any $b$ (limit $=3$, $f(0)=2$).

4. Determine $a$ and $b$ so that $h(x)=\begin{cases}3x+a&x\leq0\\ bx^2+2&x>0\end{cases}$ is continuous on $\mathbb{R}$, given that $h(-1)=2$.

   > **Solution:** $h(-1)=3(-1)+a=2\Rightarrow a=5$.  
   > Continuity at $x=0$: $\lim_{x\to0^-}(3x+5)=5$; $\lim_{x\to0^+}(bx^2+2)=2$.  
   > $5=2$: impossible. The condition $h(-1)=2$ leads to $a=5$, but continuity at $x=0$ would require $5=2$. **There is no solution** with $h(-1)=2$.

**EVAU Level:**

5. **(EVAU Madrid style)** $f(x)=\begin{cases}\dfrac{x^2+ax+b}{x-1}&\text{if }x<1\\ x^2-2x+1&\text{if }x\geq1\end{cases}$

   For $f$ to be continuous at $x=1$:  
   a) Calculate $\displaystyle\lim_{x\to1^+}f(x)$.  
   b) What condition must $\displaystyle\lim_{x\to1^-}\dfrac{x^2+ax+b}{x-1}$ satisfy for it to exist and be finite?  
   c) Find $a$ and $b$.

   > **Solution:**
   >
   > **a)** $\lim_{x\to1^+}(x^2-2x+1)=1-2+1=0$.
   >
   > **b)** For $\displaystyle\lim_{x\to1^-}\dfrac{x^2+ax+b}{x-1}$ to be finite, the numerator must vanish at $x=1$ (otherwise it would be $\pm\infty$). Condition: $1+a+b=0$, i.e., $a+b=-1$.
   >
   > **c)** With $a+b=-1$: $x^2+ax+b = (x-1)(x+c)$ for some $c$.  
   > Expanding: $(x-1)(x+c)=x^2+(c-1)x-c$. Comparing: $a=c-1$, $b=-c$.  
   > $\displaystyle\lim_{x\to1^-}\dfrac{(x-1)(x+c)}{x-1}=1+c$.  
   > For continuity: $1+c=0\Rightarrow c=-1$.  
   > Then $a=c-1=-2$ and $b=-c=1$.  
   > **$a=-2$, $b=1$** (verification: $x^2-2x+1=(x-1)^2$, limit $=0=f(1^+)$ ✓).

**Multiple Choice Test**

6. For a piecewise-defined function to be continuous at the change point $x=c$, one needs:
   - a) Only that the one-sided limits are equal
   - b) Only that $f(c)$ is defined
   - c) That the one-sided limits are equal to each other and to $f(c)$
   - d) That $f'(c)$ exists

   > **Correct answer: c)** All three conditions must be satisfied simultaneously.

7. If there is a parameter in both branches of the piecewise function, the system of equations for continuity has:
   - a) Always a unique solution
   - b) The same number of equations as unknowns, so it may have 0, 1 or infinitely many solutions
   - c) Always infinitely many solutions
   - d) Always no solution

   > **Correct answer: b)** Each change point provides one equation. With two unknowns and two change points, a $2\times2$ system is obtained which may be compatible determinate, compatible indeterminate or incompatible.

---

## 6.5 Continuity theorems

---

#### 6.5.1 Bolzano's Theorem: statement and application to existence of roots

**Worked Example**

Prove that the equation $x^3 - x - 2 = 0$ has at least one root in the interval $[1, 2]$.

**Solution:**

**Bolzano's Theorem:** If $f$ is continuous on $[a,b]$ and $f(a)\cdot f(b) < 0$ (opposite signs), then there exists at least one $c \in (a,b)$ such that $f(c) = 0$.

Let $f(x) = x^3 - x - 2$.

**Conditions:**
1. $f$ is a polynomial $\Rightarrow$ continuous on all $\mathbb{R}$, in particular on $[1,2]$. ✓

2. We calculate the values at the endpoints:
   - $f(1) = 1 - 1 - 2 = -2 < 0$
   - $f(2) = 8 - 2 - 2 = 4 > 0$

3. $f(1) \cdot f(2) = (-2)(4) = -8 < 0$. ✓

**Conclusion:** By Bolzano's Theorem, there exists $c \in (1, 2)$ such that $f(c) = 0$, i.e., the equation has at least one root in $(1, 2)$.

**Bounding:** Since $f(1) < 0$ and $f(1{,}5) = 3{,}375 - 1{,}5 - 2 = -0{,}125 < 0$, and $f(2) > 0$, the root lies in $(1{,}5, 2)$.

---

**Exercises with Solutions**

**Basic Level:**

1. Verify using Bolzano that $f(x) = x^2 - 5$ has a root in $[2, 3]$.

   > **Solution:** $f(2) = 4-5 = -1 < 0$; $f(3) = 9-5 = 4 > 0$. Product $< 0$, $f$ continuous. By Bolzano, there is a root in $(2,3)$.  
   > (In fact $c = \sqrt{5} \approx 2{,}236$.)

2. Use Bolzano to prove that $e^x - 3x = 0$ has a solution in $[0, 1]$.

   > **Solution:** $f(x)=e^x-3x$. $f(0)=1>0$; $f(1)=e-3\approx-0{,}282<0$. Product $<0$, $f$ continuous. By Bolzano, there is a root in $(0,1)$.

**Intermediate Level:**

3. Bound the root of $x^3+x-1=0$ in an interval of length $0{,}25$ using iterated Bolzano.

   > **Solution:** $f(x)=x^3+x-1$.  
   > $f(0)=-1<0$; $f(1)=1>0$: root in $(0,1)$.  
   > $f(0{,}5)=0{,}125+0{,}5-1=-0{,}375<0$: root in $(0{,}5,1)$.  
   > $f(0{,}75)=0{,}422+0{,}75-1=0{,}172>0$: root in $(0{,}5,0{,}75)$.  
   > The root lies in $(0{,}5, 0{,}75)$, an interval of length $0{,}25$.

4. Prove that $\cos x = x$ has at least one solution in $[0, \pi/2]$.

   > **Solution:** $f(x)=\cos x - x$. $f(0)=1-0=1>0$; $f(\pi/2)=0-\pi/2\approx-1{,}57<0$.  
   > Product $<0$, $f$ continuous. By Bolzano, there exists $c\in(0,\pi/2)$ with $\cos c = c$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = x^4 - 5x^2 + 4$.

   a) Factor $f(x)$ and find its exact roots.  
   b) Without knowing the roots, apply Bolzano to prove that there is at least one root in $[0, 2]$.  
   c) Determine the total number of real roots of $f$.

   > **Solution:**
   >
   > **a)** $t=x^2$: $t^2-5t+4=(t-1)(t-4)=0\Rightarrow t=1,4$.  
   > $x^2=1\Rightarrow x=\pm1$; $x^2=4\Rightarrow x=\pm2$.  
   > Roots: $x=-2, -1, 1, 2$.
   >
   > **b)** $f(0)=4>0$; $f(2)=16-20+4=0$. Not valid ($f(2)=0$, but Bolzano gives a root at the endpoint).  
   > Better: $f(0)=4>0$; $f(1{,}5)=5{,}0625-11{,}25+4=-2{,}1875<0$. Product $<0$: root in $(0,1{,}5)\subset[0,2]$.
   >
   > **c)** $f$ has four real roots: $-2, -1, 1, 2$.

**Multiple Choice Test**

6. To apply Bolzano's Theorem to $f$ on $[a,b]$, it is necessary that:
   - a) $f(a)=0$ or $f(b)=0$
   - b) $f$ is continuous on $[a,b]$ and $f(a)\cdot f(b) < 0$
   - c) $f$ is differentiable on $(a,b)$
   - d) $f$ is monotone on $[a,b]$

   > **Correct answer: b)** The conditions of the theorem are: continuity on $[a,b]$ and that $f$ takes values of different signs at the endpoints.

7. Bolzano's Theorem guarantees:
   - a) The uniqueness of the root
   - b) That the root is exactly $\frac{a+b}{2}$
   - c) The existence of at least one root in $(a,b)$
   - d) That the function is increasing on $(a,b)$

   > **Correct answer: c)** Bolzano only guarantees **existence** (at least one root), not uniqueness or exact location.

---

#### 6.5.2 Darboux's Intermediate Value Theorem: statement and applications

**Worked Example**

Prove that $f(x) = x^2 - 3x + 1$ takes the value $-1$ on the interval $[0, 3]$.

**Solution:**

**Intermediate Value Theorem (Darboux):** If $f$ is continuous on $[a,b]$, then $f$ takes all values between $f(a)$ and $f(b)$.

**Data:**
- $f(0) = 0 - 0 + 1 = 1$
- $f(3) = 9 - 9 + 1 = 1$

**Note:** In this case $f(0) = f(3) = 1$. The theorem would say it takes all values between $1$ and $1$... but we know $f$ has a minimum.

**Correct procedure:** We calculate $f$ at the vertex: $f'(x) = 2x-3 = 0 \Rightarrow x=3/2$.
$f(3/2) = 9/4 - 9/2 + 1 = -5/4 < -1$.

Applying the IVT on $[0, 3/2]$: $f(0)=1 > -1 > -5/4 = f(3/2)$. Since $f$ is continuous and $-1$ lies between $f(0)$ and $f(3/2)$, by the IVT there exists $c\in(0,3/2)$ with $f(c)=-1$.

**Direct verification:** $x^2-3x+1=-1 \Rightarrow x^2-3x+2=0 \Rightarrow (x-1)(x-2)=0 \Rightarrow x=1$ or $x=2$.  
Indeed $x=1\in(0,3/2)$. ✓

---

**Exercises with Solutions**

**Basic Level:**

1. Use the IVT to prove that $f(x) = x^3$ takes the value $4$ on $[1, 2]$.

   > **Solution:** $f(1)=1<4<8=f(2)$. $f$ continuous on $[1,2]$. By the IVT, $\exists c\in(1,2)$: $c^3=4$, i.e. $c=\sqrt[3]{4}\approx1{,}587$.

2. Does $f(x)=\sin x$ take the value $0{,}5$ on $[0, \pi]$? Justify.

   > **Solution:** $f(0)=0<0{,}5<1=f(\pi/2)$... better: $f$ continuous, $f(0)=0$ and $f(\pi)=0$, with $f(\pi/6)=0{,}5$.  
   > Yes, by the IVT (more directly: $f(\pi/6)=0{,}5$ is the exact value).

**Intermediate Level:**

3. Prove that $f(x)=e^x - 2$ takes all real values on $(-\infty,+\infty)$.

   > **Solution:** $\lim_{x\to-\infty}e^x-2=-2$ (tends to $-2$ from above); more precisely $\lim_{x\to-\infty}f(x)=-2$ (since $e^x>0$).  
   > More precisely: $f$ continuous on $\mathbb{R}$, $\lim_{x\to-\infty}f(x)=-2$, $\lim_{x\to+\infty}f(x)=+\infty$. $f$ takes all values in $(-2,+\infty)$.

4. Prove that $f(x)=x^5-3x$ takes the value $10$ at some real point.

   > **Solution:** $f(2)=32-6=26>10$; $f(1)=1-3=-2<10$.  
   > $f$ continuous, $-2<10<26=f(2)$. By the IVT on $[1,2]$: $\exists c\in(1,2)$ with $f(c)=10$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x) = \dfrac{x^2+1}{x-2}$.

   a) State the intervals of continuity of $f$.  
   b) Can the IVT be applied to $f$ on the interval $[0, 4]$? Why?  
   c) Prove that $f$ takes the value $0$ on some interval where the IVT can be applied.

   > **Solution:**
   >
   > **a)** Dom $=\mathbb{R}\setminus\{2\}$. $f$ continuous on $(-\infty,2)\cup(2,+\infty)$.
   >
   > **b)** No, because $f$ is discontinuous at $x=2\in[0,4]$. The IVT requires continuity on the entire interval.
   >
   > **c)** We take $[3,5]$: $f(3)=\dfrac{10}{1}=10>0$ and $f(5)=\dfrac{26}{3}>0$. Both positive, does not work.  
   > We take $[0, 1]$: $f(0)=\dfrac{1}{-2}=-\dfrac{1}{2}<0$ and $f(1)=\dfrac{2}{-1}=-2<0$. Both negative, does not work.  
   > The function does not take the value $0$ (since $x^2+1>0$ always). **It cannot be applied** with the IVT for the value $0$ because $f(x)\neq0$ for all $x$.

**Multiple Choice Test**

6. The IVT6. The Intermediate Value Theorem (Darboux) guarantees that if $f$ is continuous on $[a,b]$ and $k$ lies between $f(a)$ and $f(b)$, then:
   - a) $f$ is differentiable on $(a,b)$
   - b) there exists $c\in(a,b)$ such that $f(c)=k$
   - c) $f$ has an extremum on $[a,b]$
   - d) $k=\dfrac{f(a)+f(b)}{2}$

   > **Correct answer:** b) The conclusion of the IVT is exactly the existence of $c\in(a,b)$ with $f(c)=k$.

7. Let $f$ be continuous on $[0,1]$ with $f(0)=3$ and $f(1)=-1$. By the IVT:
   - a) $f$ has a maximum in $(0,1)$
   - b) $f$ has no roots
   - c) there exists $c\in(0,1)$ such that $f(c)=0$
   - d) $f$ is differentiable in $(0,1)$

   > **Correct answer:** c) Since $f(0)=3>0>-1=f(1)$ and $f$ is continuous, the IVT guarantees the existence of a root in $(0,1)$.

---

#### 6.5.3 Application of Bolzano for bounding and separation of roots

**Worked Example**

Let $f(x) = x^3 - 2x^2 - x + 1$. Locate and separate the real roots of $f$ in intervals of length 1.

**Step 1 — Verify that $f$ is continuous:** $f$ is a polynomial, continuous on $\mathbb{R}$.

**Step 2 — Evaluate at consecutive integers:**

$$f(-2)=(-8)-8+2+1=-13<0$$
$$f(-1)=(-1)-2+1+1=-1<0$$
$$f(0)=0-0-0+1=1>0$$
$$f(1)=1-2-1+1=-1<0$$
$$f(2)=8-8-2+1=-1<0$$
$$f(3)=27-18-3+1=7>0$$

**Step 3 — Apply Bolzano:**

- On $[-1, 0]$: $f(-1)=-1<0<1=f(0)$ → **sign change** → $\exists c_1\in(-1,0)$ root.
- On $[0, 1]$: $f(0)=1>0>-1=f(1)$ → **sign change** → $\exists c_2\in(0,1)$ root.
- On $[2, 3]$: $f(2)=-1<0<7=f(3)$ → **sign change** → $\exists c_3\in(2,3)$ root.

**Conclusion:** $f$ has exactly 3 real roots (a degree-3 polynomial has at most 3) in the intervals $(-1,0)$, $(0,1)$ and $(2,3)$.

**Exercises with Solutions**

**Basic Level:**

1. Prove that $f(x) = x^2 - 5$ has a root in $(2, 3)$.

   > **Solution:** $f(2)=4-5=-1<0$ and $f(3)=9-5=4>0$. $f$ continuous (polynomial). By Bolzano, $\exists c\in(2,3)$ with $f(c)=0$, i.e. $c=\sqrt{5}\approx2{,}236$.

2. Separate the roots of $g(x)=x^3-x-1$ in intervals $[n,n+1]$ with $n$ integer.

   > **Solution:** $g(-1)=-1+1-1=-1<0$, $g(0)=-1<0$, $g(1)=1-1-1=-1<0$, $g(2)=8-2-1=5>0$.  
   > Sign change on $[1,2]$: by Bolzano, there is a root in $(1,2)$.  
   > (The polynomial has only 1 real root, since the discriminant is negative for the other two roots, which are complex.)

**Intermediate Level:**

3. Locate three roots of $h(x)=\cos x - x$ in intervals of length 1 (in radians).

   > **Solution:** $h$ is continuous. $h(0)=1>0$; $h(1)=\cos1-1\approx0{,}54-1=-0{,}46<0$.  
   > Sign change on $[0,1]$: root in $(0,1)$. (This is the only real root of $\cos x=x$, the so-called "Dottie point".)  
   > To verify, $h(-\pi/2)=\cos(-\pi/2)+\pi/2=\pi/2>0$; $h(\pi)=\cos\pi-\pi=-1-\pi<0$. The unique sign change is confirmed.

4. Let $f(x)=e^x - 3x$. Find two intervals of length 1 that contain roots.

   > **Solution:** $f(0)=1>0$; $f(1)=e-3\approx-0{,}28<0$ → sign change on $[0,1]$: root $c_1\in(0,1)$.  
   > $f(1)\approx-0{,}28<0$; $f(2)=e^2-6\approx7{,}39-6=1{,}39>0$ → sign change on $[1,2]$: root $c_2\in(1,2)$.

**EVAU Level:**

5. **(EVAU Madrid style)** Let $f(x)=x^3-3x^2+1$.

   a) Calculate $f(-1)$, $f(0)$, $f(1)$, $f(2)$ and $f(3)$.  
   b) Use Bolzano's Theorem to separate all roots of $f$ in intervals of length 1.  
   c) How many real roots does $f$ have? Justify your answer.

   > **Solution:**
   >
   > **a)** $f(-1)=(-1)^3-3(-1)^2+1=-1-3+1=-3$.  
   > $f(0)=0-0+1=1$.  
   > $f(1)=1-3+1=-1$.  
   > $f(2)=8-12+1=-3$.  
   > $f(3)=27-27+1=1$.
   >
   > **b)** Sign changes:
   > - $f(-1)=-3<0<1=f(0)$: root in $(-1,0)$.
   > - $f(0)=1>0>-1=f(1)$: root in $(0,1)$.
   > - $f(2)=-3<0<1=f(3)$: root in $(2,3)$.
   >
   > **c)** $f$ has degree 3, so it has at most 3 real roots. We have detected 3 sign changes, so $f$ has **exactly 3 real roots**, one in each of the intervals $(-1,0)$, $(0,1)$ and $(2,3)$.

**Multiple Choice Test**

6. To apply Bolzano's Theorem to $f$ on $[a,b]$ and guarantee a root, one needs:
   - a) That $f$ be differentiable on $[a,b]$
   - b) That $f$ be continuous on $[a,b]$ and that $f(a)\cdot f(b)<0$
   - c) That $f(a)=0$ or $f(b)=0$
   - d) That $f'(x)\neq0$ on $(a,b)$

   > **Correct answer:** b) Bolzano requires continuity on $[a,b]$ and a sign change at the endpoints ($f(a)\cdot f(b)<0$).

7. In how many intervals $[n, n+1]$ (with $n\in\mathbb{Z}$) does Bolzano guarantee roots for $f(x)=x^3-7x+6$?

   $(f(-3)=-27+21+6=0)$, $(f(-2)=-8+14+6=12)$, $(f(0)=6)$, $(f(1)=0)$, $(f(2)=8-14+6=0)$.

   - a) 1
   - b) 2
   - c) 3
   - d) 0

   > **Correct answer:** d) Bolzano requires $f(a)\cdot f(b)<0$. Here the 3 roots are exactly at $x=-3, 1, 2$, which are integers; there is no strict sign change on any interval $[n,n+1]$. (Bolzano cannot be applied directly, but the roots are $-3, 1, 2$.)

---

# CHAPTER 7 — DERIVATIVES AND APPLICATIONS

---

#### 7.1.1 Average and instantaneous rate of change

**Worked Example**

Let $f(x)=x^2+1$. Calculate the average rate of change of $f$ on the interval $[1, 3]$ and the instantaneous rate of change at $x=1$.

**Step 1 — Average rate of change (ARC):**

$$\text{ARC}_{[1,3]} = \frac{f(3)-f(1)}{3-1} = \frac{(9+1)-(1+1)}{2} = \frac{10-2}{2} = \frac{8}{2} = 4$$

Interpretation: between $x=1$ and $x=3$, $f$ grows on average 4 units per unit of $x$.

**Step 2 — Instantaneous rate of change (IRC at $x=1$):**

$$\text{IRC}_{x=1} = \lim_{h\to 0}\frac{f(1+h)-f(1)}{h} = \lim_{h\to 0}\frac{(1+h)^2+1-(2)}{h}$$

$$= \lim_{h\to 0}\frac{1+2h+h^2+1-2}{h} = \lim_{h\to 0}\frac{2h+h^2}{h} = \lim_{h\to 0}(2+h) = 2$$

**Conclusion:** The instantaneous rate of change at $x=1$ is $2 = f'(1)$.

**Exercises with Solutions**

**Basic Level:**

1. Calculate the ARC of $f(x)=3x-2$ on the interval $[0, 4]$.

   > **Solution:** $\text{ARC}=\dfrac{f(4)-f(0)}{4-0}=\dfrac{10-(-2)}{4}=\dfrac{12}{4}=3$.  
   > (Consistent: the slope of $f(x)=3x-2$ is always $3$.)


2. An object moves according to $s(t)=t^2+2t$ (metres, $t$ in seconds). Calculate the average velocity between $t=1$ and $t=3$.

   > **Solution:** $s(1)=1+2=3$; $s(3)=9+6=15$.  
   > Average velocity $=\dfrac{15-3}{3-1}=\dfrac{12}{2}=6$ m/s.

**Intermediate Level:**

3. Calculate the ARC of $f(x)=x^3$ on $[1, 1+h]$ and simplify.

   > **Solution:** $\dfrac{f(1+h)-f(1)}{h}=\dfrac{(1+h)^3-1}{h}=\dfrac{1+3h+3h^2+h^3-1}{h}=\dfrac{h(3+3h+h^2)}{h}=3+3h+h^2$.  
   > As $h\to 0$, IRC $= 3 = f'(1)$.

4. The position of a vehicle is $s(t)=5t^2-2t+1$ (m). Calculate the instantaneous velocity at $t=2$ using the definition of the derivative.

   > **Solution:** $f'(2)=\lim_{h\to0}\dfrac{s(2+h)-s(2)}{h}$.  
   > $s(2)=20-4+1=17$. $s(2+h)=5(2+h)^2-2(2+h)+1=5(4+4h+h^2)-4-2h+1=20+20h+5h^2-3-2h=17+18h+5h^2$.  
   > $\dfrac{17+18h+5h^2-17}{h}=18+5h \to 18$ m/s.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\dfrac{1}{x}$ defined on $(0,+\infty)$.

   a) Calculate the average rate of change on the interval $[1, 3]$.  
   b) Calculate the instantaneous rate of change at $x=2$ using the limit of the difference quotient.  
   c) Interpret geometrically the result of part b).

   > **Solution:**
   >
   > **a)** $\text{ARC}=\dfrac{f(3)-f(1)}{3-1}=\dfrac{\frac{1}{3}-1}{2}=\dfrac{-\frac{2}{3}}{2}=-\dfrac{1}{3}$.
   >
   > **b)** $f'(2)=\lim_{h\to0}\dfrac{\dfrac{1}{2+h}-\dfrac{1}{2}}{h}=\lim_{h\to0}\dfrac{\dfrac{2-(2+h)}{2(2+h)}}{h}=\lim_{h\to0}\dfrac{-h}{2h(2+h)}=\lim_{h\to0}\dfrac{-1}{2(2+h)}=\dfrac{-1}{4}$.
   >
   > **c)** The instantaneous rate of change at $x=2$ is the slope of the tangent line to $f(x)=\dfrac{1}{x}$ at the point $(2, \frac{1}{2})$. Since it is negative ($-\frac{1}{4}$), the function is decreasing at that point.

**Multiple Choice Test**

6. The average rate of change of $f(x)=x^2$ on $[a, a+h]$ is:
   - a) $2a$
   - b) $2a+h$
   - c) $a+h$
   - d) $h$

   > **Correct answer:** b) $\dfrac{(a+h)^2-a^2}{h}=\dfrac{2ah+h^2}{h}=2a+h$.

7. The instantaneous rate of change at a point is:
   - a) The average value of the function on an interval
   - b) The slope of the secant between two points
   - c) The limit of the average rate of change as the increment tends to zero
   - d) The difference $f(b)-f(a)$

   > **Correct answer:** c) The IRC is $\lim_{h\to0}\dfrac{f(a+h)-f(a)}{h}$, i.e., the limit of the ARC as $h\to0$.

---

#### 7.1.2 Definition of the derivative as the limit of the difference quotient

**Worked Example**

Calculate $f'(x)$ for $f(x)=\sqrt{x}$ using the definition of the derivative.

**Step 1 — Write the difference quotient:**

$$\frac{f(x+h)-f(x)}{h} = \frac{\sqrt{x+h}-\sqrt{x}}{h}$$

**Step 2 — Rationalise by multiplying by the conjugate:**

$$= \frac{(\sqrt{x+h}-\sqrt{x})(\sqrt{x+h}+\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})} = \frac{(x+h)-x}{h(\sqrt{x+h}+\sqrt{x})} = \frac{h}{h(\sqrt{x+h}+\sqrt{x})} = \frac{1}{\sqrt{x+h}+\sqrt{x}}$$

**Step 3 — Take the limit:**

$$f'(x) = \lim_{h\to 0}\frac{1}{\sqrt{x+h}+\sqrt{x}} = \frac{1}{2\sqrt{x}}$$

**Exercises with Solution**

**Basic Level:**

1. Calculate $f'(x)$ for $f(x)=5x+3$ using the definition.

   > **Solution:** $\dfrac{f(x+h)-f(x)}{h}=\dfrac{5(x+h)+3-(5x+3)}{h}=\dfrac{5h}{h}=5$.  
   > $f'(x)=\lim_{h\to0}5=5$.

2. Calculate $f'(2)$ for $f(x)=x^2-3x$ using the definition.

   > **Solution:** $\dfrac{f(2+h)-f(2)}{h}=\dfrac{(2+h)^2-3(2+h)-(4-6)}{h}=\dfrac{4+4h+h^2-6-3h+2}{h}=\dfrac{h^2+h}{h}=h+1$.  
   > $f'(2)=\lim_{h\to0}(h+1)=1$.

**Intermediate Level:**

3. Calculate $f'(x)$ for $f(x)=x^3$ using the definition.

   > **Solution:** $\dfrac{(x+h)^3-x^3}{h}=\dfrac{x^3+3x^2h+3xh^2+h^3-x^3}{h}=3x^2+3xh+h^2 \to 3x^2$.

4. Calculate $f'(x)$ for $f(x)=\dfrac{1}{x+1}$ using the definition.

   > **Solution:** $\dfrac{\dfrac{1}{x+1+h}-\dfrac{1}{x+1}}{h}=\dfrac{\dfrac{(x+1)-(x+1+h)}{(x+1+h)(x+1)}}{h}=\dfrac{-h}{h(x+1+h)(x+1)}=\dfrac{-1}{(x+1+h)(x+1)}$.  
   > $\to \dfrac{-1}{(x+1)^2}$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=x^2-2x$.

   a) Using the definition of the derivative, calculate $f'(x)$.  
   b) Find the point on the graph where the tangent is horizontal.  
   c) Calculate the equation of the tangent line at $x=3$.

   > **Solution:**
   >
   > **a)** $\dfrac{(x+h)^2-2(x+h)-(x^2-2x)}{h}=\dfrac{2xh+h^2-2h}{h}=2x+h-2 \to 2x-2$.
   >
   > **b)** Horizontal tangent $\Leftrightarrow f'(x)=0$: $2x-2=0 \Rightarrow x=1$. Point: $(1, -1)$.
   >
   > **c)** $f'(3)=4$; $f(3)=9-6=3$. Tangent: $y-3=4(x-3)$, i.e. $y=4x-9$.

**Multiple Choice Test**

6. The derivative of $f$ at $x=a$ is defined as:
   - a) $\lim_{h\to\infty}\dfrac{f(a+h)-f(a)}{h}$
   - b) $\lim_{h\to 0}\dfrac{f(a+h)-f(a)}{h}$
   - c) $\dfrac{f(a+1)-f(a)}{1}$
   - d) $\lim_{x\to a}f(x)$

   > **Correct answer:** b) The derivative is the limit of the difference quotient as $h\to0$.

7. If the limit $\lim_{h\to0}\dfrac{f(a+h)-f(a)}{h}$ exists and is finite, then:
   - a) $f$ is continuous at $a$ but not necessarily differentiable
   - b) $f$ is differentiable at $a$, and therefore also continuous at $a$
   - c) $f$ may be discontinuous at $a$
   - d) $f'(a)=0$ necessarily

   > **Correct answer:** b) The existence of the limit of the difference quotient defines differentiability, and every differentiable function is continuous.

---

#### 7.1.3 Derivative as the slope of the tangent line: geometric interpretation

**Worked Example**

Let $f(x)=x^2-4x+3$. Find the equation of the tangent line at the point with $x$-coordinate $x=1$ and interpret geometrically.

**Step 1 — Calculate $f'(x)$:**

$$f'(x) = 2x-4$$

**Step 2 — Slope of the tangent at $x=1$:**

$$m = f'(1) = 2(1)-4 = -2$$

**Step 3 — Point of tangency:**

$$f(1) = 1-4+3 = 0 \quad \Rightarrow \quad \text{Point: } (1, 0)$$

**Step 4 — Equation of the tangent line:**

$$y - 0 = -2(x-1) \quad \Rightarrow \quad y = -2x+2$$

**Interpretation:** The tangent line at $(1,0)$ has slope $-2$, indicating that the function is decreasing at that point with an inclination of $2$ units per horizontal unit (angle with the $x$-axis: $\arctan(2)\approx 63.4°$ downward).

**Exercises with Solution**

**Basic Level:**

1. Let $f(x)=3x^2$. What is the slope of the tangent line at $x=2$?

   > **Solution:** $f'(x)=6x$. $f'(2)=12$. The slope is $m=12$.

2. At what point of $f(x)=x^2+x$ does the tangent line have slope $5$?

   > **Solution:** $f'(x)=2x+1=5 \Rightarrow x=2$. Point: $(2, f(2))=(2, 6)$.

**Intermediate Level:**

3. Find the equation of the tangent line to $f(x)=\sqrt{x}$ at $x=4$.

   > **Solution:** $f'(x)=\dfrac{1}{2\sqrt{x}}$, $f'(4)=\dfrac{1}{4}$. $f(4)=2$. Tangent: $y-2=\dfrac{1}{4}(x-4)$, i.e. $y=\dfrac{x}{4}+1$.

4. Find the equation of the tangent line to $f(x)=\ln x$ at $x=e$.

   > **Solution:** $f'(x)=\dfrac{1}{x}$, $f'(e)=\dfrac{1}{e}$. $f(e)=1$. Tangent: $y-1=\dfrac{1}{e}(x-e)=\dfrac{x}{e}-1$, i.e. $y=\dfrac{x}{e}$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=e^x$.

   a) Write the equation of the tangent line to $f$ at the point $(0,1)$.  
   b) Check whether this tangent passes through the origin.  
   c) Are there other tangent lines to $f$ that pass through the origin? Justify.

   > **Solution:**
   >
   > **a)** $f'(x)=e^x$, $f'(0)=1$. Tangent at $(0,1)$: $y-1=1\cdot(x-0) \Rightarrow y=x+1$.
   >
   > **b)** At $(0,0)$: $0=0+1=1$ → Does not pass through the origin. (The tangent is $y=x+1$, which does not pass through $(0,0)$.)
   >
   > **c)** We seek the tangent at point $(a, e^a)$ that passes through $(0,0)$: slope from origin $=\dfrac{e^a}{a}$; slope of tangent $=e^a$. Setting equal: $\dfrac{e^a}{a}=e^a \Rightarrow a=1$. Tangent at $x=1$: $y-e=e(x-1) \Rightarrow y=ex$. Passes through $(0,0)$: $0=e\cdot0=0$ ✓. **Yes**, there exists a tangent line to $f$ that passes through the origin: $y=ex$, at the point $(1,e)$.

**Multiple Choice Test**

6. The slope of the tangent line to $f(x)=x^3$ at $x=2$ is:
   - a) $8$
   - b) $6$
   - c) $12$
   - d) $4$

   > **Correct answer:** c) $f'(x)=3x^2$, $f'(2)=12$.

7. If $f'(a)=0$, the tangent line to $f$ at $x=a$:
   - a) Has infinite slope
   - b) Is perpendicular to the $x$-axis
   - c) Is horizontal (parallel to the $x$-axis)
   - d) Does not exist

   > **Correct answer:** c) Slope $0$ means a horizontal tangent, parallel to the $x$-axis.

---

#### 7.1.4 Derivative function: definition and notation (Lagrange, Leibniz, Newton)

**Worked Example**

Let $f(x)=2x^3-5x+1$. Express its derivative function using the three main notations and calculate $f'(2)$.

**Derivative function:** Applying standard differentiation rules,

$$f'(x) = 6x^2 - 5$$

**Equivalent notations:**

| Notation | Expression |
|----------|------------|
| Lagrange | $f'(x) = 6x^2-5$ |
| Leibniz  | $\dfrac{dy}{dx} = 6x^2-5$ or $\dfrac{d}{dx}(2x^3-5x+1)=6x^2-5$ |
| Newton   | $\dot{f} = 6x^2-5$ (used in Physics) |

**Calculation of $f'(2)$:**

$$f'(2) = 6(4)-5 = 24-5 = 19$$

**Exercises with Solution**

**Basic Level:**

1. Write the derivative function of $f(x)=x^4-3x^2+7$ in Lagrange and Leibniz notation.

   > **Solution:** $f'(x)=4x^3-6x$ (Lagrange). $\dfrac{dy}{dx}=4x^3-6x$ (Leibniz).

2. Given $f'(x)=3x^2-2$, calculate $f'(0)$, $f'(1)$ and $f'(-1)$.

   > **Solution:** $f'(0)=-2$; $f'(1)=1$; $f'(-1)=1$.

**Intermediate Level:**

3. Find the derivative function of $g(x)=\dfrac{2}{x}-x^2$ and calculate $g'(-2)$.

   > **Solution:** $g(x)=2x^{-1}-x^2$. $g'(x)=-2x^{-2}-2x=-\dfrac{2}{x^2}-2x$.  
   > $g'(-2)=-\dfrac{2}{4}-2(-2)=-\dfrac{1}{2}+4=\dfrac{7}{2}$.

4. If $\dfrac{dy}{dx}=2e^x-\dfrac{1}{x}$, what is the value of the derivative at $x=1$?

   > **Solution:** $\dfrac{dy}{dx}\bigg|_{x=1}=2e-1\approx 4.44$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=x^2\cdot e^x$.

   a) Find $f'(x)$, stating the differentiation rule used.  
   b) Calculate $f'(0)$ and $f'(1)$.  
   c) Find the points where $f'(x)=0$.

   > **Solution:**
   >
   > **a)** Product rule: $f'(x)=(x^2)'e^x+x^2(e^x)'=2x\cdot e^x+x^2\cdot e^x=e^x(2x+x^2)=xe^x(x+2)$.
   >
   > **b)** $f'(0)=0\cdot e^0\cdot(2)=0$; $f'(1)=1\cdot e\cdot 3=3e$.
   >
   > **c)** $f'(x)=0 \Leftrightarrow xe^x(x+2)=0$. Since $e^x>0$ always, $x=0$ or $x=-2$.

**Multiple Choice Test**

6. The notation $\dfrac{dy}{dx}$ for the derivative was introduced by:
   - a) Newton
   - b) Lagrange
   - c) Leibniz
   - d) Euler

   > **Correct answer:** c) The differential notation $\dfrac{dy}{dx}$ is due to Leibniz. Newton used $\dot{y}$ and Lagrange used $f'(x)$.

7. If $f'(x)=4x^3$, then $f'(-1)=$:
   - a) $4$
   - b) $-4$
   - c) $12$
   - d) $-12$

   > **Correct answer:** b) $f'(-1)=4(-1)^3=4\cdot(-1)=-4$.

---

#### 7.1.5 Higher-order derivatives: $f''$, $f'''$ and the $n$-th order derivative

**Worked Example**

Let $f(x)=x^4-6x^2+2x-1$. Calculate $f'(x)$, $f''(x)$, $f'''(x)$ and $f^{(4)}(x)$. Interpret $f''$.

**Successive derivatives:**

$$f'(x) = 4x^3-12x+2$$

$$f''(x) = 12x^2-12$$

$$f'''(x) = 24x$$

$$f^{(4)}(x) = 24$$

$$f^{(n)}(x) = 0 \quad \text{for } n\geq 5$$

**Interpretation of $f''$:** The second derivative measures the rate of change of the slope (acceleration of the function). If $f''(x)>0$, the curve is concave upward; if $f''(x)<0$, it is concave downward.

**Exercises with Solution**

**Basic Level:**

1. Calculate $f''(x)$ for $f(x)=3x^3-2x^2+x-5$.

   > **Solution:** $f'(x)=9x^2-4x+1$. $f''(x)=18x-4$.

2. If the position of a moving object is $s(t)=2t^3-3t$, calculate its acceleration at $t=1$.

   > **Solution:** Velocity: $v(t)=s'(t)=6t^2-3$. Acceleration: $a(t)=s''(t)=12t$.  
   > $a(1)=12$ m/s².

**Intermediate Level:**

3. Calculate $f^{(n)}(x)$ for $f(x)=e^{2x}$.

   > **Solution:** $f'(x)=2e^{2x}$; $f''(x)=4e^{2x}$; $f^{(n)}(x)=2^n e^{2x}$.

4. Find $f''(x)$ for $f(x)=x\ln x$ and determine its sign.

   > **Solution:** $f'(x)=\ln x + x\cdot\dfrac{1}{x}=\ln x+1$. $f''(x)=\dfrac{1}{x}$.  
   > For $x>0$ (domain): $f''(x)=\dfrac{1}{x}>0$ → the function is always concave upward on its domain.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\sin x$.

   a) Calculate $f'(x)$, $f''(x)$, $f'''(x)$ and $f^{(4)}(x)$.  
   b) Deduce a general expression for $f^{(n)}(x)$.  
   c) Calculate $f^{(100)}(0)$.

   > **Solution:**
   >
   > **a)** $f'(x)=\cos x$; $f''(x)=-\sin x$; $f'''(x)=-\cos x$; $f^{(4)}(x)=\sin x$.
   >
   > **b)** The cycle repeats with period 4:  
   > $f^{(4k)}(x)=\sin x$, $f^{(4k+1)}(x)=\cos x$, $f^{(4k+2)}(x)=-\sin x$, $f^{(4k+3)}(x)=-\cos x$.
   >
   > **c)** $100=4\cdot25$, so $f^{(100)}(x)=\sin x$. Therefore $f^{(100)}(0)=\sin 0=0$.

**Multiple Choice Test**

6. If $f(x)=x^5$, then $f^{(5)}(x)=$:
   - a) $5x^4$
   - b) $120x$
   - c) $120$
   - d) $0$

   > **Correct answer:** c) $f'=5x^4$, $f''=20x^3$, $f'''=60x^2$, $f^{(4)}=120x$, $f^{(5)}=120$.

7. The second derivative of a function at a point can be interpreted as:
   - a) The slope of the tangent
   - b) The instantaneous velocity
   - c) The curvature or rate of change of the slope
   - d) The value of the function at that point

   > **Correct answer:** c) $f''$ measures how the slope varies; in kinematics it corresponds to acceleration.

---

#### 7.2.1 Derivatives of elementary functions

**Worked Example**

Calculate the derivatives of the following elementary functions and justify each result with the corresponding formula:

$$f_1(x)=x^5, \quad f_2(x)=e^{3x}, \quad f_3(x)=\ln(2x), \quad f_4(x)=\sin(4x), \quad f_5(x)=\cos(x^2)$$

**Solution:**

$f_1'(x)=5x^4$ (power rule: $(x^n)'=nx^{n-1}$)

$f_2'(x)=3e^{3x}$ ($(e^{ax})'=ae^{ax}$; here $a=3$)

$f_3'(x)=\dfrac{1}{2x}\cdot 2=\dfrac{1}{x}$ ($(\ln u)'=\dfrac{u'}{u}$; $u=2x$, $u'=2$)

$f_4'(x)=4\cos(4x)$ ($(\sin u)'=u'\cos u$; $u=4x$)

$f_5'(x)=-2x\sin(x^2)$ ($(\cos u)'=-u'\sin u$; $u=x^2$, $u'=2x$)

**Exercises with Solution**

**Basic Level:**

1. Differentiate: $f(x)=x^7$, $g(x)=e^x$, $h(x)=\ln x$, $p(x)=\sin x$, $q(x)=\cos x$.

   > **Solution:** $f'=7x^6$; $g'=e^x$; $h'=\dfrac{1}{x}$; $p'=\cos x$; $q'=-\sin x$.

2. Differentiate: $f(x)=\sqrt[3]{x^2}=x^{2/3}$.

   > **Solution:** $f'(x)=\dfrac{2}{3}x^{-1/3}=\dfrac{2}{3\sqrt[3]{x}}$.

**Intermediate Level:**

3. Differentiate: $f(x)=\tan x$. (Use $\tan x=\dfrac{\sin x}{\cos x}$.)

   > **Solution:** $f'(x)=\dfrac{\cos x\cdot\cos x-\sin x\cdot(-\sin x)}{\cos^2 x}=\dfrac{\cos^2 x+\sin^2 x}{\cos^2 x}=\dfrac{1}{\cos^2 x}=\sec^2 x$.

4. Differentiate: $f(x)=a^x$ where $a>0, a\neq1$.

   > **Solution:** $f(x)=a^x=e^{x\ln a}$. $f'(x)=e^{x\ln a}\cdot\ln a=a^x\ln a$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Calculate the derivatives of:

   a) $f(x)=x^3-2\sqrt{x}+\dfrac{1}{x}$  
   b) $g(x)=3e^x-5\ln x+\cos x$  
   c) $h(x)=\tan x - x$

   > **Solution:**
   >
   > **a)** $f(x)=x^3-2x^{1/2}+x^{-1}$. $f'(x)=3x^2-\dfrac{1}{\sqrt{x}}-\dfrac{1}{x^2}$.
   >
   > **b)** $g'(x)=3e^x-\dfrac{5}{x}-\sin x$.
   >
   > **c)** $h'(x)=\sec^2 x-1=\tan^2 x$.

**Multiple Choice Test**

6. The derivative of $f(x)=\ln(x)$ is:
   - a) $x$
   - b) $\dfrac{1}{x}$
   - c) $e^x$
   - d) $\ln(x-1)$

   > **Correct answer:** b) $(\ln x)'=\dfrac{1}{x}$ for $x>0$.

7. The derivative of $\cos x$ is:
   - a) $\sin x$
   - b) $-\sin x$
   - c) $\cos x$
   - d) $-\cos x$

   > **Correct answer:** b) $(\cos x)'=-\sin x$.

---

#### 7.2.2 Linearity: derivative of sums and scalar multiples

**Worked Example**

Differentiate $f(x) = 4x^3 - 7x^2 + 2x - 9$ applying the linearity of the derivative.

**Linearity property:** $(af+bg)' = af'+bg'$ for constants $a, b$.

$$f'(x) = 4\cdot(x^3)' - 7\cdot(x^2)' + 2\cdot(x)' - (9)' = 4\cdot3x^2 - 7\cdot2x + 2\cdot1 - 0 = 12x^2-14x+2$$

**Exercises with Solution**

**Basic Level:**

1. Differentiate $f(x)=5x^4-3x^2+7$.

   > **Solution:** $f'(x)=20x^3-6x$.

2. Differentiate $g(x)=3\sin x+2\cos x - e^x$.

   > **Solution:** $g'(x)=3\cos x-2\sin x-e^x$.

**Intermediate Level:**

3. Differentiate $h(x)=\dfrac{x^3}{3}-\dfrac{x^2}{2}+x-\ln x$.

   > **Solution:** $h'(x)=x^2-x+1-\dfrac{1}{x}$.

4. Differentiate $f(x)=2\sqrt{x}+\dfrac{3}{x^2}-5e^x+\ln 2$.

   > **Solution:** $f(x)=2x^{1/2}+3x^{-2}-5e^x+\ln 2$.  
   > $f'(x)=\dfrac{1}{\sqrt{x}}-\dfrac{6}{x^3}-5e^x$. (The constant $\ln 2$ differentiates to $0$.)

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=ax^3+bx^2+cx+d$ with $f(0)=1$, $f'(0)=2$, $f''(0)=-6$, $f'''(0)=6$.

   a) Determine the values of $a$, $b$, $c$, $d$.  
   b) Write the explicit expression for $f(x)$ and $f'(x)$.

   > **Solution:**
   >
   > **a)** $f(0)=d=1$. $f'(x)=3ax^2+2bx+c$; $f'(0)=c=2$.  
   > $f''(x)=6ax+2b$; $f''(0)=2b=-6 \Rightarrow b=-3$.  
   > $f'''(x)=6a$; $f'''(0)=6a=6 \Rightarrow a=1$.
   >
   > **b)** $f(x)=x^3-3x^2+2x+1$; $f'(x)=3x^2-6x+2$.

**Multiple Choice Test**

6. If $f(x)=3x^2+5$ and $g(x)=2x-1$, then $(f+g)'(x)=$:
   - a) $6x+2$
   - b) $6x$
   - c) $6x-1$
   - d) $3x^2+2x+4$

   > **Correct answer:** a) $(f+g)'=f'+g'=6x+2$.

7. The derivative of a constant is:
   - a) The constant itself
   - b) $1$
   - c) $0$
   - d) Undefined

   > **Correct answer:** c) The derivative of any constant is $0$.

---

#### 7.2.3 Product rule

**Worked Example**

Differentiate $f(x)=(x^2+1)(3x-2)$ applying the product rule.

**Product rule:** $(u\cdot v)' = u'v + uv'$

Let $u=x^2+1$ and $v=3x-2$. Then $u'=2x$ and $v'=3$.

$$f'(x) = (2x)(3x-2) + (x^2+1)(3) = 6x^2-4x + 3x^2+3 = 9x^2-4x+3$$

**Verification** by expanding: $f(x)=3x^3-2x^2+3x-2$. $f'(x)=9x^2-4x+3$ ✓.

**Exercises with Solution**

**Basic Level:**

1. Differentiate $f(x)=x\cdot e^x$.

   > **Solution:** $u=x$, $v=e^x$; $u'=1$, $v'=e^x$.  
   > $f'(x)=1\cdot e^x+x\cdot e^x=e^x(1+x)$.

2. Differentiate $g(x)=(x+1)\sin x$.

   > **Solution:** $g'(x)=1\cdot\sin x+(x+1)\cos x=\sin x+(x+1)\cos x$.

**Intermediate Level:**

3. Differentiate $h(x)=x^2\ln x$.

   > **Solution:** $h'(x)=2x\cdot\ln x+x^2\cdot\dfrac{1}{x}=2x\ln x+x=x(2\ln x+1)$.

4. Differentiate $f(x)=(3x^2-x)(e^x+\ln x)$.

   > **Solution:** $u'=6x-1$; $v'=e^x+\dfrac{1}{x}$.  
   > $f'(x)=(6x-1)(e^x+\ln x)+(3x^2-x)(e^x+\dfrac{1}{x})$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=x^2\sin x$.

   a) Calculate $f'(x)$.  
   b) Find the points where $f'(x)=0$ in $[0, 2\pi]$.  
   c) Determine whether those points are maxima or minima using $f''$.

   > **Solution:**
   >
   > **a)** $f'(x)=2x\sin x+x^2\cos x=x(2\sin x+x\cos x)$.
   >
   > **b)** $f'(x)=0$ if $x=0$ or $2\sin x+x\cos x=0$.  
   > For $x\in(0,2\pi]$: $2\tan x=-x \Rightarrow \tan x=-x/2$. This equation has no simple closed-form solution; it is acceptable to state that there are transcendental solutions to be found numerically.  
   > At $x=0$: $f'(0)=0$.
   >
   > **c)** $f''(x)=2\sin x+2x\cos x+2x\cos x-x^2\sin x=2\sin x+4x\cos x-x^2\sin x$.  
   > $f''(0)=0$, not conclusive. Analysing the sign of $f'$ near $0$: $f'(x)\approx x(2x)=2x^2>0$ for small $x\neq0$, so $x=0$ is a local minimum.

**Multiple Choice Test**

6. Applying the product rule to $f(x)=x\cdot\cos x$:
   - a) $f'(x)=\cos x$
   - b) $f'(x)=-x\sin x$
   - c) $f'(x)=\cos x-x\sin x$
   - d) $f'(x)=\cos x+x\sin x$

   > **Correct answer:** c) $(x)'\cos x+x(\cos x)'=\cos x-x\sin x$.

7. If $f(x)=u(x)\cdot v(x)$, then $f'(x)=$:
   - a) $u'(x)\cdot v'(x)$
   - b) $u'(x)\cdot v(x)+u(x)\cdot v'(x)$
   - c) $u(x)\cdot v'(x)$
   - d) $u'(x)+v'(x)$

   > **Correct answer:** b) This is the product rule (Leibniz rule).

---

#### 7.2.4 Quotient rule

**Worked Example**

Differentiate $f(x)=\dfrac{x^2-1}{x+3}$ applying the quotient rule.

**Quotient rule:** $\left(\dfrac{u}{v}\right)' = \dfrac{u'v - uv'}{v^2}$

Let $u=x^2-1$, $v=x+3$. Then $u'=2x$, $v'=1$.

$$f'(x) = \frac{(2x)(x+3)-(x^2-1)(1)}{(x+3)^2} = \frac{2x^2+6x-x^2+1}{(x+3)^2} = \frac{x^2+6x+1}{(x+3)^2}$$

**Exercises with Solution**

**Basic Level:**

1. Differentiate $f(x)=\dfrac{3x}{x+1}$.

   > **Solution:** $u=3x$, $v=x+1$, $u'=3$, $v'=1$.  
   > $f'(x)=\dfrac{3(x+1)-3x\cdot1}{(x+1)^2}=\dfrac{3}{(x+1)^2}$.

2. Differentiate $g(x)=\dfrac{x^2+1}{x}=x+\dfrac{1}{x}$ in two ways.

   > **Solution 1 (quotient rule):** $g'=\dfrac{2x\cdot x-(x^2+1)\cdot1}{x^2}=\dfrac{2x^2-x^2-1}{x^2}=\dfrac{x^2-1}{x^2}$.  
   > **Solution 2 (simplifying):** $g'=1-\dfrac{1}{x^2}=\dfrac{x^2-1}{x^2}$ ✓.

**Intermediate Level:**

3. Differentiate $h(x)=\dfrac{e^x}{x^2+1}$.

   > **Solution:** $h'(x)=\dfrac{e^x(x^2+1)-e^x\cdot2x}{(x^2+1)^2}=\dfrac{e^x(x^2-2x+1)}{(x^2+1)^2}=\dfrac{e^x(x-1)^2}{(x^2+1)^2}$.

4. Differentiate $f(x)=\dfrac{\ln x}{x}$.

   > **Solution:** $f'(x)=\dfrac{\frac{1}{x}\cdot x-\ln x\cdot1}{x^2}=\dfrac{1-\ln x}{x^2}$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\dfrac{x^2-x+1}{x-1}$.

   a) Calculate $f'(x)$.  
   b) Find the points where $f'(x)=0$.  
   c) Determine on which intervals $f$ is increasing and decreasing.

   > **Solution:**
   >
   > **a)** $f'(x)=\dfrac{(2x-1)(x-1)-(x^2-x+1)\cdot1}{(x-1)^2}=\dfrac{2x^2-3x+1-x^2+x-1}{(x-1)^2}=\dfrac{x^2-2x}{(x-1)^2}=\dfrac{x(x-2)}{(x-1)^2}$.
   >
   > **b)** $f'(x)=0 \Leftrightarrow x=0$ or $x=2$.
   >
   > **c)** Sign table of $f'(x)=\dfrac{x(x-2)}{(x-1)^2}$:
   > - $(-\infty,0)$: $(-)(-)/(+)>0$ → increasing
   > - $(0,1)$: $(+)(-)/(+)<0$ → decreasing
   > - $(1,2)$: $(+)(-)/(+)<0$ → decreasing
   > - $(2,+\infty)$: $(+)(+)/(+)>0$ → increasing
   >
   > Local minimum at $x=2$; local maximum at $x=0$.

**Multiple Choice Test**

6. The derivative of $f(x)=\dfrac{1}{x^2}$ is:
   - a) $-\dfrac{2}{x^3}$
   - b) $\dfrac{2}{x^3}$
   - c) $-\dfrac{1}{x^3}$
   - d) $2x$

   > **Correct answer:** a) $f'(x)=-2x^{-3}=-\dfrac{2}{x^3}$.

7. If $f(x)=\dfrac{u}{v}$, then $f'=$:
   - a) $\dfrac{u'v+uv'}{v^2}$
   - b) $\dfrac{u'v-uv'}{v^2}$
   - c) $\dfrac{u'}{v'}$
   - d) $\dfrac{u'v-uv'}{v}$

   > **Correct answer:** b) This is the quotient rule.

---

#### 7.2.5 Chain rule (composite function)

**Worked Example**

Differentiate $f(x)=\sin(x^3+2x)$ using the chain rule.

**Chain rule:** $(f\circ g)'(x)=f'(g(x))\cdot g'(x)$

Let the outer function be $f(u)=\sin u$ and the inner function $g(x)=x^3+2x$.

$$f'(u)=\cos u, \qquad g'(x)=3x^2+2$$

$$\frac{d}{dx}\sin(x^3+2x) = \cos(x^3+2x)\cdot(3x^2+2)$$

**Exercises with Solution**

**Basic Level:**

1. Differentiate $f(x)=(3x+1)^5$.

   > **Solution:** $f'(x)=5(3x+1)^4\cdot3=15(3x+1)^4$.

2. Differentiate $g(x)=e^{x^2}$.

   > **Solution:** $g'(x)=e^{x^2}\cdot2x=2xe^{x^2}$.

**Intermediate Level:**

3. Differentiate $h(x)=\ln(\sin x)$.

   > **Solution:** $h'(x)=\dfrac{1}{\sin x}\cdot\cos x=\dfrac{\cos x}{\sin x}=\cot x$.

4. Differentiate $f(x)=\sqrt{x^2+4x-1}$.

   > **Solution:** $f'(x)=\dfrac{2x+4}{2\sqrt{x^2+4x-1}}=\dfrac{x+2}{\sqrt{x^2+4x-1}}$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=e^{\sin x}$.

   a) Calculate $f'(x)$, justifying the rule used.  
   b) Find $f'(0)$ and $f'(\pi/2)$.  
   c) Find the points $x\in[0,2\pi]$ where $f'(x)=0$.

   > **Solution:**
   >
   > **a)** Chain rule: outer function $e^u$ ($u=\sin x$), inner function $\sin x$.  
   > $f'(x)=e^{\sin x}\cdot\cos x$.
   >
   > **b)** $f'(0)=e^0\cdot\cos0=1\cdot1=1$. $f'(\pi/2)=e^1\cdot\cos(\pi/2)=e\cdot0=0$.
   >
   > **c)** $f'(x)=0 \Leftrightarrow e^{\sin x}\cdot\cos x=0$. Since $e^{\sin x}>0$, we need $\cos x=0$.  
   > In $[0,2\pi]$: $x=\dfrac{\pi}{2}$ and $x=\dfrac{3\pi}{2}$.

**Multiple Choice Test**

6. The derivative of $f(x)=(2x+3)^4$ is:
   - a) $4(2x+3)^3$
   - b) $8(2x+3)^3$
   - c) $4(2x+3)^3\cdot4$
   - d) $(2x+3)^3$

   > **Correct answer:** b) $4(2x+3)^3\cdot2=8(2x+3)^3$.

7. To differentiate $f(x)=\ln(x^2+1)$ using the chain rule, we obtain:
   - a) $\dfrac{1}{x^2+1}$
   - b) $\dfrac{2x}{x^2+1}$
   - c) $\dfrac{1}{2x}$
   - d) $\ln(2x)$

   > **Correct answer:** b) $f'(x)=\dfrac{1}{x^2+1}\cdot2x=\dfrac{2x}{x^2+1}$.

---

#### 7.2.6 Logarithmic differentiation: technique and applications

**Worked Example**

Calculate the derivative of $f(x)=x^x$ (for $x>0$) using logarithmic differentiation.

**Step 1 — Take natural logarithms on both sides:**

$$\ln f(x)=\ln(x^x)=x\ln x$$

**Step 2 — Differentiate implicitly with respect to $x$:**

$$\frac{f'(x)}{f(x)} = \ln x + x\cdot\frac{1}{x} = \ln x+1$$

**Step 3 — Solve for $f'(x)$:**

$$f'(x) = f(x)\cdot(\ln x+1) = x^x(\ln x+1)$$

**Exercises with Solution**

**Basic Level:**

1. Use logarithmic differentiation to differentiate $f(x)=x^3(x+1)^2$.

   > **Solution:** $\ln f=3\ln x+2\ln(x+1)$. $\dfrac{f'}{f}=\dfrac{3}{x}+\dfrac{2}{x+1}$.  
   > $f'=x^3(x+1)^2\left(\dfrac{3}{x}+\dfrac{2}{x+1}\right)=3x^2(x+1)^2+2x^3(x+1)=x^2(x+1)(5x+3)$.

2. Differentiate $g(x)=\dfrac{(x+1)^2}{(x-1)^3}$ by logarithmic differentiation.

   > **Solution:** $\ln g=2\ln(x+1)-3\ln(x-1)$. $\dfrac{g'}{g}=\dfrac{2}{x+1}-\dfrac{3}{x-1}=\dfrac{2(x-1)-3(x+1)}{(x+1)(x-1)}=\dfrac{-x-5}{x^2-1}$.  
   > $g'=\dfrac{(x+1)^2}{(x-1)^3}\cdot\dfrac{-x-5}{x^2-1}=\dfrac{-(x+5)(x+1)}{(x-1)^4}$.

**Intermediate Level:**

3. Differentiate $f(x)=(x+1)^{\sin x}$ for $x>-1$.

   > **Solution:** $\ln f=\sin x\cdot\ln(x+1)$.  
   > $\dfrac{f'}{f}=\cos x\cdot\ln(x+1)+\dfrac{\sin x}{x+1}$.  
   > $f'=(x+1)^{\sin x}\left(\cos x\cdot\ln(x+1)+\dfrac{\sin x}{x+1}\right)$.

4. Differentiate $h(x)=\dfrac{x^2\sqrt{x+1}}{e^x}$ using logarithmic differentiation.

   > **Solution:** $\ln h=2\ln x+\dfrac{1}{2}\ln(x+1)-x$.  
   > $\dfrac{h'}{h}=\dfrac{2}{x}+\dfrac{1}{2(x+1)}-1$.  
   > $h'=\dfrac{x^2\sqrt{x+1}}{e^x}\left(\dfrac{2}{x}+\dfrac{1}{2(x+1)}-1\right)$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\left(\dfrac{x+1}{x-1}\right)^x$ for $x>1$.

   a) Calculate $f'(x)$ using logarithmic differentiation.  
   b) Calculate $f'(2)$.

   > **Solution:**
   >
   > **a)** $\ln f=x\left[\ln(x+1)-\ln(x-1)\right]$.  
   > $\dfrac{f'}{f}=\ln\dfrac{x+1}{x-1}+x\left[\dfrac{1}{x+1}-\dfrac{1}{x-1}\right]=\ln\dfrac{x+1}{x-1}+x\cdot\dfrac{-2}{x^2-1}=\ln\dfrac{x+1}{x-1}-\dfrac{2x}{x^2-1}$.  
   > $f'=\left(\dfrac{x+1}{x-1}\right)^x\left(\ln\dfrac{x+1}{x-1}-\dfrac{2x}{x^2-1}\right)$.
   >
   > **b)** $f(2)=\left(\dfrac{3}{1}\right)^2=9$. $f'(2)=9\left(\ln3-\dfrac{4}{3}\right)=9\ln3-12$.

**Multiple Choice Test**

6. Logarithmic differentiation is especially useful for functions of the type:
   - a) High-degree polynomials
   - b) Products and quotients of many functions, and variable-exponent powers
   - c) Simple trigonometric functions
   - d) Sums of elementary functions

   > **Correct answer:** b) Logarithmic differentiation greatly simplifies expressions with many factors multiplied/divided and powers with variable exponents.

7. The derivative of $f(x)=x^x$ is:
   - a) $x\cdot x^{x-1}$
   - b) $x^x\ln x$
   - c) $x^x(\ln x+1)$
   - d) $x^{x-1}$

   > **Correct answer:** c) By logarithmic differentiation: $f'(x)=x^x(\ln x+1)$.

---

#### 7.3.1 One-sided derivatives: definition and calculation

**Worked Example**

Let $f(x)=|x-2|$. Calculate the one-sided derivatives at $x=2$ and determine whether $f$ is differentiable at that point.

**Right-hand derivative:**

$$f'_+(2) = \lim_{h\to 0^+}\frac{f(2+h)-f(2)}{h} = \lim_{h\to 0^+}\frac{|h|-0}{h} = \lim_{h\to 0^+}\frac{h}{h} = 1$$

(For $h>0$: $|h|=h$.)

**Left-hand derivative:**

$$f'_-(2) = \lim_{h\to 0^-}\frac{f(2+h)-f(2)}{h} = \lim_{h\to 0^-}\frac{|-h|}{h} = \lim_{h\to 0^-}\frac{-h}{h} = -1$$

(For $h<0$: $|h|=-h$.)

**Conclusion:** $f'_+(2)=1\neq-1=f'_-(2)$, therefore $f$ **is not differentiable** at $x=2$.

**Exercises with Solution**

**Basic Level:**

1. Let $f(x)=|3x|$. Calculate $f'_+(0)$ and $f'_-(0)$.

   > **Solution:** For $h>0$: $f'_+(0)=\lim_{h\to0^+}\dfrac{3h}{h}=3$. For $h<0$: $f'_-(0)=\lim_{h\to0^-}\dfrac{-3h}{h}=-3$.  
   > Not differentiable at $x=0$.

2. Calculate $f'_+(1)$ and $f'_-(1)$ for $f(x)=x^2$.

   > **Solution:** $f'(x)=2x$ at all points, so $f'_+(1)=f'_-(1)=2$. $f$ is differentiable at $x=1$.

**Intermediate Level:**

3. Let $f(x)=\begin{cases}x^2 & x\leq1 \\ 2x-1 & x>1\end{cases}$. Calculate $f'_+(1)$ and $f'_-(1)$.

   > **Solution:** $f'_-(1)=\lim_{h\to0^-}\dfrac{(1+h)^2-1}{h}=\lim_{h\to0^-}(2+h)=2$.  
   > $f'_+(1)=\lim_{h\to0^+}\dfrac{2(1+h)-1-1}{h}=\lim_{h\to0^+}\dfrac{2h}{h}=2$.  
   > $f'_+(1)=f'_-(1)=2$ → $f$ is differentiable at $x=1$ with $f'(1)=2$.

4. Let $f(x)=\begin{cases}\sin x & x\geq0 \\ x & x<0\end{cases}$. Is $f$ differentiable at $x=0$?

   > **Solution:** $f'_-(0)=\lim_{h\to0^-}\dfrac{h-0}{h}=1$. $f'_+(0)=\lim_{h\to0^+}\dfrac{\sin h}{h}=1$.  
   > $f'_+(0)=f'_-(0)=1$ → $f$ is differentiable at $x=0$ with $f'(0)=1$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\begin{cases}x^2+ax & x<2 \\ bx+1 & x\geq2\end{cases}$.

   a) Find the values of $a$ and $b$ for $f$ to be continuous at $x=2$.  
   b) With those values, study whether $f$ is differentiable at $x=2$.

   > **Solution:**
   >
   > **a)** Continuity at $x=2$: $\lim_{x\to2^-}f(x)=4+2a$ and $\lim_{x\to2^+}f(x)=2b+1$, $f(2)=2b+1$.  
   > Condition: $4+2a=2b+1 \Rightarrow 2a-2b=-3$ ... (*)
   >
   > **b)** One-sided derivatives:  
   > $f'_-(2)=(x^2+ax)'|_{x=2}=2x+a|_{x=2}=4+a$.  
   > $f'_+(2)=(bx+1)'=b$.  
   > For differentiability: $4+a=b$ ... (**)  
   > From (*): $2a-2b=-3 \Rightarrow a-b=-\dfrac{3}{2}$. From (**): $a-b=-4$.  
   > $-4=-\dfrac{3}{2}$ → contradiction. With the differentiability conditions, there are no values of $a, b$ that make $f$ both continuous and differentiable simultaneously.  
   > **If only continuity is required** (without specifying $b$): there are infinitely many parametric solutions. To obtain a specific solution an additional value is needed (e.g. $b=3$, then $a=-\frac{1}{2}$).

**Multiple Choice Test**

6. The one-sided derivatives of $f(x)=|x|$ at $x=0$ are:
   - a) $f'_+(0)=0$, $f'_-(0)=0$
   - b) $f'_+(0)=1$, $f'_-(0)=1$
   - c) $f'_+(0)=1$, $f'_-(0)=-1$
   - d) $f'_+(0)=-1$, $f'_-(0)=1$

   > **Correct answer:** c) For $h>0$: $|h|/h=1$. For $h<0$: $|h|/h=-h/h=-1$.

7. A function is differentiable at $x=a$ if and only if:
   - a) It is continuous at $x=a$
   - b) Its one-sided derivatives are equal and finite
   - c) $f(a)=0$
   - d) $f'(a)>0$

   > **Correct answer:** b) Differentiability requires $f'_+(a)=f'_-(a)$ and both must be finite.

---

#### 7.3.2 Differentiability at a point: condition of equal one-sided derivatives

**Worked Example**

Determine whether $f(x)=\begin{cases}x^2-1 & x\leq1 \\ 2x-2 & x>1\end{cases}$ is differentiable at $x=1$.

**Step 1 — Verify continuity** (necessary condition):

$\lim_{x\to1^-}(x^2-1)=0$; $f(1)=0$; $\lim_{x\to1^+}(2x-2)=0$. All three are equal → $f$ is continuous at $x=1$.

**Step 2 — Calculate one-sided derivatives:**

$$f'_-(1) = (x^2-1)'|_{x=1} = 2x|_{x=1} = 2$$

$$f'_+(1) = (2x-2)'|_{x=1} = 2|_{x=1} = 2$$

**Step 3 — Conclusion:**

$f'_-(1)=2=f'_+(1)$ → $f$ **is differentiable** at $x=1$ with $f'(1)=2$.

**Exercises with Solution**

**Basic Level:**

1. Determine whether $f(x)=\begin{cases}3x & x\leq0\\x^2 & x>0\end{cases}$ is differentiable at $x=0$.

   > **Solution:** Continuity: $f(0)=0$; $\lim_{x\to0^+}x^2=0$ ✓.  
   > $f'_-(0)=3$; $f'_+(0)=0$. Since they differ, $f$ **is not differentiable** at $x=0$.

2. Determine whether $g(x)=x|x|$ is differentiable at $x=0$.

   > **Solution:** $g(x)=\begin{cases}-x^2 & x<0\\x^2 & x\geq0\end{cases}$.  
   > $g'_-(0)=-2\cdot0=0$; $g'_+(0)=2\cdot0=0$. Equal → $g$ **is differentiable** at $x=0$ with $g'(0)=0$.

**Intermediate Level:**

3. Find the value of $a$ so that $f(x)=\begin{cases}ax^2+1 & x\leq1\\3x-1 & x>1\end{cases}$ is differentiable at $x=1$.

   > **Solution:** Continuity: $a+1=2 \Rightarrow a=1$.  
   > $f'_-(1)=2ax|_{x=1}=2a=2$; $f'_+(1)=3$.  
   > For differentiability: $2a=3 \Rightarrow a=\dfrac{3}{2}$, but this contradicts $a=1$ from continuity.  
   > **No value** of $a$ makes $f$ simultaneously continuous and differentiable at $x=1$.

4. Prove that $f(x)=x^{1/3}$ is not differentiable at $x=0$.

   > **Solution:** $\dfrac{f(0+h)-f(0)}{h}=\dfrac{h^{1/3}}{h}=h^{-2/3}=\dfrac{1}{h^{2/3}}\to+\infty$ as $h\to0$.  
   > The limit is not finite → $f$ **is not differentiable** at $x=0$ (there is a vertical tangent).

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\begin{cases}ax+b & x<1\\x^2+2 & x\geq1\end{cases}$.

   a) Find $a$ and $b$ so that $f$ is differentiable at $x=1$.  
   b) Write $f'(x)$ for each piece with those values.  
   c) Calculate $f'(0)$ and $f'(2)$.

   > **Solution:**
   >
   > **a)** Continuity: $\lim_{x\to1^-}(ax+b)=a+b=f(1)=3 \Rightarrow a+b=3$.  
   > Differentiability: $f'_-(1)=a$ and $f'_+(1)=2x|_{x=1}=2$. For differentiability: $a=2$.  
   > Then $b=3-2=1$.
   >
   > **b)** $f'(x)=\begin{cases}2 & x<1\\2x & x>1\end{cases}$ (at $x=1$: $f'(1)=2$).
   >
   > **c)** $f'(0)=2$; $f'(2)=4$.

**Multiple Choice Test**

6. If $f$ is differentiable at $a$, then:
   - a) $f$ is continuous at $a$, but not vice versa
   - b) $f$ is continuous at $a$ and vice versa
   - c) $f$ need not be continuous at $a$
   - d) $f'(a)$ is necessarily positive

   > **Correct answer:** a) Differentiability implies continuity, but continuity does not imply differentiability (counterexample: $|x|$ at $x=0$).

7. A function continuous at $a$ is:
   - a) Always differentiable at $a$
   - b) Never differentiable at $a$
   - c) Not necessarily differentiable at $a$
   - d) Differentiable if and only if $f(a)=0$

   > **Correct answer:** c) Continuity is a necessary but not sufficient condition for differentiability.

---

#### 7.3.3 Relationship between differentiability and continuity

**Worked Example**

Formally prove that if $f$ is differentiable at $a$, then $f$ is continuous at $a$.

**Proof:**

Suppose $f'(a)$ exists (is finite). We want to show that $\lim_{x\to a}f(x)=f(a)$, equivalently $\lim_{h\to0}f(a+h)=f(a)$.

We write:

$$f(a+h)-f(a) = \frac{f(a+h)-f(a)}{h}\cdot h$$

Taking the limit as $h\to0$:

$$\lim_{h\to0}\left[f(a+h)-f(a)\right] = \lim_{h\to0}\frac{f(a+h)-f(a)}{h}\cdot\lim_{h\to0}h = f'(a)\cdot 0 = 0$$

Therefore $\lim_{h\to0}f(a+h)=f(a)$, which proves the continuity of $f$ at $a$. $\blacksquare$

**Counterexample of the converse:** $f(x)=|x|$ is continuous at $0$ but not differentiable at $0$.

**Exercises with Solution**

**Basic Level:**

1. Give an example of a function that is continuous at $x=0$ but not differentiable at $x=0$.

   > **Solution:** $f(x)=|x|$. Continuous at $0$ ($f(0)=0$, limit $0$), but $f'_+(0)=1\neq-1=f'_-(0)$ → not differentiable.

2. Is $f(x)=\sqrt[3]{x}$ continuous at $x=0$? Is it differentiable?

   > **Solution:** Continuous ($f(0)=0$, $\lim_{x\to0}\sqrt[3]{x}=0$). Not differentiable: $f'(x)=\dfrac{1}{3}x^{-2/3}\to\infty$ as $x\to0$.

**Intermediate Level:**

3. Classify as "true" or "false" and justify: "If $f$ is not continuous at $a$, then it is not differentiable at $a$."

   > **Solution:** **True.** The contrapositive of the theorem: differentiable $\Rightarrow$ continuous, is equivalent to: not continuous $\Rightarrow$ not differentiable.

4. Give an example of a function that is not continuous at $a=1$. Verify that it is not differentiable there.

   > **Solution:** $f(x)=\dfrac{x^2-1}{x-1}$ (for $x\neq1$) with $f(1)=0$.  
   > $\lim_{x\to1}f(x)=2\neq0=f(1)$ → removable discontinuity at $x=1$ → not differentiable.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\begin{cases}\dfrac{x^2-4}{x-2} & x\neq2 \\ k & x=2\end{cases}$.

   a) Determine the value of $k$ for $f$ to be continuous at $x=2$.  
   b) With that value, is $f$ differentiable at $x=2$?  
   c) Calculate $f'(2)$ if it exists.

   > **Solution:**
   >
   > **a)** $\lim_{x\to2}\dfrac{x^2-4}{x-2}=\lim_{x\to2}\dfrac{(x-2)(x+2)}{x-2}=\lim_{x\to2}(x+2)=4$.  
   > For continuity: $k=4$.
   >
   > **b)** With $k=4$, $f(x)=x+2$ for $x\neq2$ and $f(2)=4=2+2$. So $f(x)=x+2$ for all reals → a polynomial, differentiable everywhere.
   >
   > **c)** $f'(x)=1$ for all $x$, in particular $f'(2)=1$.

**Multiple Choice Test**

6. The function $f(x)=|x-3|$ at $x=3$:
   - a) Is continuous and differentiable
   - b) Is not continuous and not differentiable
   - c) Is continuous but not differentiable
   - d) Is not continuous but is differentiable

   > **Correct answer:** c) $|x-3|$ is continuous everywhere (in particular at $x=3$), but not differentiable at $x=3$ (one-sided derivatives are $1$ and $-1$).

7. The implication "differentiable at $a$ $\Rightarrow$ continuous at $a$":
   - a) Is false
   - b) Is true, and its converse is also true
   - c) Is true, but its converse is false in general
   - d) Is only valid for polynomial functions

   > **Correct answer:** c) Every differentiable function is continuous, but not every continuous function is differentiable.

---

#### 7.3.4 Study of differentiability of piecewise-defined functions

**Worked Example**

Study the differentiability of $f(x)=\begin{cases}x^3-x & x<0\\x^2 & 0\leq x\leq2\\4x-4 & x>2\end{cases}$ at the points $x=0$ and $x=2$.

**At $x=0$:**

*Continuity:* $\lim_{x\to0^-}(x^3-x)=0$; $f(0)=0$; $\lim_{x\to0^+}x^2=0$ ✓ continuous.

*One-sided derivatives:*
$$f'_-(0)=(x^3-x)'|_{x=0}=(3x^2-1)|_{x=0}=-1$$
$$f'_+(0)=(x^2)'|_{x=0}=2x|_{x=0}=0$$

Since $-1\neq0$, **$f$ is not differentiable at $x=0$**.

**At $x=2$:**

*Continuity:* $\lim_{x\to2^-}x^2=4$; $f(2)=4$; $\lim_{x\to2^+}(4x-4)=4$ ✓ continuous.

*One-sided derivatives:*
$$f'_-(2)=2x|_{x=2}=4$$
$$f'_+(2)=4$$

Since $4=4$, **$f$ is differentiable at $x=2$** with $f'(2)=4$.

**Exercises with Solution**

**Basic Level:**

1. Study the differentiability of $f(x)=\begin{cases}2x & x\leq1\\x^2+1 & x>1\end{cases}$ at $x=1$.

   > **Solution:** Continuity: $f(1)=2$; $\lim_{x\to1^+}(x^2+1)=2$ ✓. Derivatives: $f'_-(1)=2$; $f'_+(1)=2$ ✓.  
   > $f$ **is differentiable** at $x=1$.

2. Study the differentiability of $g(x)=\begin{cases}x+1 & x\leq2\\x^2-1 & x>2\end{cases}$ at $x=2$.

   > **Solution:** Continuity: $g(2)=3$; $\lim_{x\to2^+}(x^2-1)=3$ ✓. Derivatives: $g'_-(2)=1$; $g'_+(2)=2\cdot2=4$.  
   > $1\neq4$ → $g$ **is not differentiable** at $x=2$.

**Intermediate Level:**

3. Find $a$ and $b$ so that $f(x)=\begin{cases}x^2+ax & x\leq1\\bx+2 & x>1\end{cases}$ is differentiable at $x=1$.

   > **Solution:** Continuity: $1+a=b+2 \Rightarrow a-b=1$ ... (1).  
   > Differentiability: $f'_-(1)=2x+a|_{x=1}=2+a$; $f'_+(1)=b$.  
   > $2+a=b$ ... (2). From (1) and (2): $b=a-1$ and $b=2+a$. Then $a-1=2+a \Rightarrow -1=2$ → **no solution exists**. Both conditions are incompatible.

4. Study the continuity and differentiability of $f(x)=\begin{cases}e^x & x\leq0\\\cos x & x>0\end{cases}$ at $x=0$.

   > **Solution:** Continuity: $f(0)=e^0=1$; $\lim_{x\to0^+}\cos x=1$ ✓.  
   > Derivatives: $f'_-(0)=e^0=1$; $f'_+(0)=-\sin0=0$. $1\neq0$ → **not differentiable** at $x=0$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\begin{cases}x^2-1 & x<0\\ax+b & 0\leq x<3\\x^2-6x+k & x\geq3\end{cases}$.

   Determine $a$, $b$, $k$ so that $f$ is differentiable at $x=0$ and $x=3$.

   > **Solution:**
   >
   > **At $x=0$:**  
   > Continuity: $\lim_{x\to0^-}(x^2-1)=-1=f(0)=b \Rightarrow b=-1$.  
   > Differentiability: $f'_-(0)=2\cdot0=0$; $f'_+(0)=a$. So $a=0$.
   >
   > **At $x=3$** (with $a=0$, $b=-1$, middle piece $f(x)=-1$):  
   > Continuity: $f(3^-)=0\cdot3-1=-1$; $f(3^+)=9-18+k=k-9$. So $k-9=-1 \Rightarrow k=8$.  
   > Differentiability: $f'_-(3)=a=0$; $f'_+(3)=(2x-6)|_{x=3}=0$ ✓.
   >
   > **Result:** $a=0$, $b=-1$, $k=8$.

**Multiple Choice Test**

6. To study the differentiability of a piecewise-defined function at the junction point $x=a$, one must:
   - a) Only verify that $f(a)$ exists
   - b) Calculate the ordinary derivative at $x=a$
   - c) Verify continuity and then equate the one-sided derivatives of each piece at $x=a$
   - d) Check that both pieces are polynomials

   > **Correct answer:** c) First continuity, then equality of the one-sided derivatives calculated from each piece.

7. If a piecewise function is continuous but not differentiable at the junction point, the graph has:
   - a) A jump
   - b) An asymptote
   - c) A corner or "peak" (abrupt change of slope)
   - d) An inflection point

   > **Correct answer:** c) Non-differentiability with continuity indicates an abrupt change of direction (corner or vertex) in the graph.

---

#### 7.3.5 Finding parameters for a function to be differentiable

**Worked Example**

Find $a$ and $b$ so that $f(x)=\begin{cases}ax^2+bx & x\leq2\\x^3-5x & x>2\end{cases}$ is differentiable at $x=2$.

**Step 1 — Continuity (necessary condition):**

$$\lim_{x\to2^-}(ax^2+bx)=4a+2b$$
$$\lim_{x\to2^+}(x^3-5x)=8-10=-2$$

$4a+2b=-2$ → $2a+b=-1$ ... (I)

**Step 2 — Differentiability:**

$$f'_-(2)=(2ax+b)|_{x=2}=4a+b$$
$$f'_+(2)=(3x^2-5)|_{x=2}=12-5=7$$

$4a+b=7$ ... (II)

**Step 3 — Solve the system:**

From (II)$-$(I): $(4a+b)-(2a+b)=7-(-1) \Rightarrow 2a=8 \Rightarrow a=4$

Substituting into (I): $8+b=-1 \Rightarrow b=-9$

**Conclusion:** $a=4$, $b=-9$.

**Exercises with Solution**

**Basic Level:**

1. Find $a$ so that $f(x)=\begin{cases}ax+1 & x\leq3\\x^2-8 & x>3\end{cases}$ is continuous at $x=3$.

   > **Solution:** $3a+1=9-8=1 \Rightarrow 3a=0 \Rightarrow a=0$.

2. Find $a$ so that $f(x)=\begin{cases}x^2 & x\leq1\\ax+2 & x>1\end{cases}$ is continuous and differentiable at $x=1$.

   > **Solution:** Continuity: $1=a+2 \Rightarrow a=-1$. Differentiability: $f'_-(1)=2$; $f'_+(1)=a=-1$. $2\neq-1$ → **no value** of $a$ satisfies both conditions.
**Intermediate Level:**

3. Find $a$ and $b$ so that $f(x)=\begin{cases}x^2+1 & x\leq1\\ax+b & x>1\end{cases}$ is differentiable at $x=1$.

   > **Solution:** Continuity: $2=a+b$ ... (I). Differentiability: $f'_-(1)=2$; $f'_+(1)=a$. So $a=2$, $b=0$.

4. Let $f(x)=\begin{cases}\ln(x+1)+a & x>0\\bx^2+x & x\leq0\end{cases}$. Find $a$ and $b$ so that $f$ is differentiable at $x=0$.

   > **Solution:** Continuity: $f(0^-)=0$; $f(0^+)=\ln1+a=a$. So $a=0$.  
   > Derivatives: $f'_-(0)=(2bx+1)|_{x=0}=1$.  
   > $f'_+(0)=\dfrac{1}{0+1}=1$. Both equal $1$ for any $b$. So $a=0$ and $b$ can be any value.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\begin{cases}x^2+ax+b & x\leq1\\x^3-x+c & x>1\end{cases}$.

   Find the values of $a$, $b$, $c$ so that $f$ is differentiable at $x=1$ and $f(0)=3$.

   > **Solution:**
   > $f(0)=0+0+b=b=3 \Rightarrow b=3$.  
   > Continuity at $x=1$: $1+a+3=1-1+c \Rightarrow 4+a=c$ ... (I).  
   > Differentiability at $x=1$: $f'_-(1)=2x+a|_{x=1}=2+a$; $f'_+(1)=3x^2-1|_{x=1}=2$. So $2+a=2 \Rightarrow a=0$.  
   > From (I): $c=4$.
   >
   > **Result:** $a=0$, $b=3$, $c=4$.

**Multiple Choice Test**

6. For a piecewise function to be differentiable at the junction point, the number of conditions that must be satisfied is:
   - a) 1 (only the derivative)
   - b) 2 (continuity and equal one-sided derivatives)
   - c) 3 (left limit, right limit and the value)
   - d) Depends on the degree of the polynomials

   > **Correct answer:** b) Continuity (one condition) and equality of one-sided derivatives (another condition): 2 conditions in total.

7. If there are two parameters $a$ and $b$, the system for differentiability at a junction point typically has:
   - a) Always a unique solution
   - b) Always infinitely many solutions
   - c) A unique solution, no solution, or infinitely many, depending on the system
   - d) A solution only if both pieces are polynomials of equal degree

   > **Correct answer:** c) A $2\times2$ system may have a unique solution, be inconsistent, or be underdetermined.

---

#### 7.4.1 Equation of the tangent line to a curve at a point

**Worked Example**

Find the equation of the tangent line to $f(x)=x^3-3x+2$ at the point with $x$-coordinate $x=1$.

**Step 1 — Calculate the point of tangency:**

$$f(1) = 1-3+2 = 0 \quad \Rightarrow \quad P=(1,0)$$

**Step 2 — Calculate the slope (derivative at $x=1$):**

$$f'(x) = 3x^2-3 \quad \Rightarrow \quad f'(1)=3-3=0$$

**Step 3 — Equation of the tangent line** (slope $0$ → horizontal tangent):

$$y - 0 = 0\cdot(x-1) \quad \Rightarrow \quad \boxed{y=0}$$

The tangent at $(1,0)$ is the $x$-axis itself.

**Exercises with Solution**

**Basic Level:**

1. Find the tangent line to $f(x)=x^2$ at $x=-2$.

   > **Solution:** $f(-2)=4$, $f'(x)=2x$, $f'(-2)=-4$.  
   > Tangent: $y-4=-4(x+2) \Rightarrow y=-4x-4$.

2. Find the tangent line to $f(x)=\sqrt{x}$ at $x=9$.

   > **Solution:** $f(9)=3$, $f'(x)=\dfrac{1}{2\sqrt{x}}$, $f'(9)=\dfrac{1}{6}$.  
   > Tangent: $y-3=\dfrac{1}{6}(x-9) \Rightarrow y=\dfrac{x}{6}+\dfrac{3}{2}$.

**Intermediate Level:**

3. Find the tangent line to $f(x)=e^x$ that is parallel to $y=e^2\cdot x$.

   > **Solution:** The slope of the tangent must be $e^2$. $f'(x)=e^x=e^2 \Rightarrow x=2$. Point: $(2, e^2)$.  
   > Tangent: $y-e^2=e^2(x-2) \Rightarrow y=e^2x-e^2$.

4. Find the tangent line to $f(x)=\ln x$ at the point where the slope is $\dfrac{1}{3}$.

   > **Solution:** $f'(x)=\dfrac{1}{x}=\dfrac{1}{3} \Rightarrow x=3$. $f(3)=\ln3$.  
   > Tangent: $y-\ln3=\dfrac{1}{3}(x-3) \Rightarrow y=\dfrac{x}{3}-1+\ln3$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\dfrac{x^2}{x-1}$.

   a) Find $f'(x)$.  
   b) Determine the equation of the tangent at $x=2$.  
   c) Determine at which points the tangent is horizontal.

   > **Solution:**
   >
   > **a)** $f'(x)=\dfrac{2x(x-1)-x^2\cdot1}{(x-1)^2}=\dfrac{x^2-2x}{(x-1)^2}=\dfrac{x(x-2)}{(x-1)^2}$.
   >
   > **b)** $f(2)=4$; $f'(2)=\dfrac{2\cdot0}{1}=0$. Tangent: $y=4$ (horizontal).
   >
   > **c)** $f'(x)=0 \Leftrightarrow x=0$ or $x=2$.  
   > Points: $(0, 0)$ and $(2, 4)$.

**Multiple Choice Test**

6. The equation of the tangent line to $y=f(x)$ at the point $(a, f(a))$ is:
   - a) $y=f'(a)$
   - b) $y=f'(a)(x-a)$
   - c) $y-f(a)=f'(a)(x-a)$
   - d) $y=f(a)x+f'(a)$

   > **Correct answer:** c) The point-slope equation with point $(a,f(a))$ and slope $f'(a)$.

7. If the tangent line to $f(x)=x^2+bx$ at $x=1$ has slope $5$, then $b=$:
   - a) $3$
   - b) $5$
   - c) $1$
   - d) $-1$

   > **Correct answer:** a) $f'(x)=2x+b$; $f'(1)=2+b=5 \Rightarrow b=3$.

---

#### 7.4.2 Equation of the normal line to a curve at a point

**Worked Example**

Find the equation of the normal line to $f(x)=x^2-4$ at the point $(2, 0)$.

**Step 1 — Slope of the tangent:**

$$f'(x)=2x \quad \Rightarrow \quad f'(2)=4$$

**Step 2 — Slope of the normal** (perpendicular to the tangent):

$$m_n = -\frac{1}{m_t} = -\frac{1}{4}$$

**Step 3 — Equation of the normal:**

$$y-0=-\frac{1}{4}(x-2) \quad \Rightarrow \quad y=-\frac{x}{4}+\frac{1}{2}$$

**Exercises with Solution**

**Basic Level:**

1. Find the normal line to $f(x)=x^3$ at $x=1$.

   > **Solution:** $f(1)=1$; $f'(1)=3$. Normal: slope $m_n=-\dfrac{1}{3}$.  
   > $y-1=-\dfrac{1}{3}(x-1) \Rightarrow y=-\dfrac{x}{3}+\dfrac{4}{3}$.

2. Find the normal line to $f(x)=\sin x$ at $x=0$.

   > **Solution:** $f(0)=0$; $f'(0)=\cos0=1$. Normal: $m_n=-1$.  
   > $y=-x$.

**Intermediate Level:**

3. Find the normal line to $f(x)=e^x$ at the point where $f'=e$.

   > **Solution:** $f'(x)=e^x=e \Rightarrow x=1$; $f(1)=e$. Normal: $m_n=-\dfrac{1}{e}$.  
   > $y-e=-\dfrac{1}{e}(x-1) \Rightarrow y=-\dfrac{x}{e}+\dfrac{1}{e}+e$.

4. Find the equations of the tangent and normal lines to $f(x)=\ln x$ at $x=1$.

   > **Solution:** $f(1)=0$; $f'(1)=1$. Tangent: $y=x-1$. Normal: $m_n=-1$; $y=-(x-1)=-x+1$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\sqrt{4-x^2}$ (upper semicircle of radius 2).

   a) Calculate $f'(x)$ for $x\in(-2,2)$.  
   b) Find the tangent and normal at the point $(\sqrt{2}, \sqrt{2})$.  
   c) Interpret the normal line geometrically.

   > **Solution:**
   >
   > **a)** $f'(x)=\dfrac{-2x}{2\sqrt{4-x^2}}=\dfrac{-x}{\sqrt{4-x^2}}$.
   >
   > **b)** At $x=\sqrt{2}$: $f'(\sqrt{2})=\dfrac{-\sqrt{2}}{\sqrt{2}}=-1$.  
   > Tangent: $y-\sqrt{2}=-1(x-\sqrt{2}) \Rightarrow y=-x+2\sqrt{2}$.  
   > Normal: $m_n=1$; $y-\sqrt{2}=x-\sqrt{2} \Rightarrow y=x$.
   >
   > **c)** The normal line $y=x$ passes through the origin $(0,0)$, which is the centre of the circle. Geometrically, the normal at any point of a circle passes through its centre.

**Multiple Choice Test**

6. If the tangent line to $f$ at a point has slope $m\neq0$, the normal line has slope:
   - a) $m$
   - b) $-m$
   - c) $\dfrac{1}{m}$
   - d) $-\dfrac{1}{m}$

   > **Correct answer:** d) Two perpendicular lines satisfy $m_1\cdot m_2=-1$, so $m_n=-\dfrac{1}{m_t}$.

7. If the tangent line to $f$ at a point is horizontal ($m_t=0$), the normal line is:
   - a) Horizontal
   - b) Vertical
   - c) With slope $1$
   - d) With slope $-1$

   > **Correct answer:** b) If $m_t=0$, the normal is perpendicular to the horizontal, i.e. vertical.

---

#### 7.4.3 Points of the curve with horizontal tangent or given slope

**Worked Example**

Find all points of $f(x)=x^3-6x^2+9x+1$ where the tangent line is horizontal.

**Horizontal tangent** ↔ $f'(x)=0$.

$$f'(x)=3x^2-12x+9=3(x^2-4x+3)=3(x-1)(x-3)$$

$$f'(x)=0 \Leftrightarrow x=1 \quad \text{or} \quad x=3$$

**Points on the curve:**

$$f(1)=1-6+9+1=5 \quad \Rightarrow \quad P_1=(1,5)$$
$$f(3)=27-54+27+1=1 \quad \Rightarrow \quad P_2=(3,1)$$

**Exercises with Solution**

**Basic Level:**

1. Find the points of $f(x)=x^2-4x+3$ where the tangent is horizontal.

   > **Solution:** $f'(x)=2x-4=0 \Rightarrow x=2$. Point: $(2, -1)$.

2. Find the points of $f(x)=\sin x$ on $[0, 2\pi]$ where the slope of the tangent is $0$.

   > **Solution:** $f'(x)=\cos x=0 \Rightarrow x=\dfrac{\pi}{2}$ and $x=\dfrac{3\pi}{2}$.  
   > Points: $\left(\dfrac{\pi}{2},1\right)$ and $\left(\dfrac{3\pi}{2},-1\right)$.

**Intermediate Level:**

3. Find the points of $f(x)=x^3-3x$ where the tangent has slope $9$.

   > **Solution:** $f'(x)=3x^2-3=9 \Rightarrow x^2=4 \Rightarrow x=\pm2$.  
   > Points: $(2, 2)$ and $(-2, -2)$.

4. Find the points of $f(x)=x^4-8x^2$ where the tangent is parallel to $y=-8x$.

   > **Solution:** Desired slope: $-8$. $f'(x)=4x^3-16x=-8 \Rightarrow 4x^3-16x+8=0 \Rightarrow x^3-4x+2=0$.  
   > No obvious rational roots; the cubic has three real roots that must be found numerically. (It is acceptable to leave the answer in implicit form.)

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=x^3-3x^2$.

   a) Calculate $f'(x)$.  
   b) Find the points where the tangent is horizontal and state whether they are local maxima or minima.  
   c) Write the equation of the tangent at $x=-1$.

   > **Solution:**
   >
   > **a)** $f'(x)=3x^2-6x=3x(x-2)$.
   >
   > **b)** $f'(x)=0 \Leftrightarrow x=0$ or $x=2$.  
   > $f''(x)=6x-6$: $f''(0)=-6<0$ → local maximum at $(0, 0)$.  
   > $f''(2)=6>0$ → local minimum at $(2, -4)$.
   >
   > **c)** $f(-1)=-1-3=-4$; $f'(-1)=3+6=9$. Tangent: $y+4=9(x+1) \Rightarrow y=9x+5$.

**Multiple Choice Test**

6. At points where the tangent to $f$ is horizontal, necessarily:
   - a) $f$ has a local maximum or minimum
   - b) $f'=0$, but an inflection point may also occur
   - c) $f$ is constant
   - d) $f''=0$

   > **Correct answer:** b) $f'(x)=0$ is a necessary condition for a relative extremum, but can also occur at an inflection point (e.g. $f(x)=x^3$ at $x=0$).

7. If $f'(2)=3$, the tangent line at $x=2$ has:
   - a) Slope $3$ and intersects the $y$-axis at $3$
   - b) Slope $3$ and passes through $(2, f(2))$
   - c) Slope $\dfrac{1}{3}$
   - d) Equation $y=3x$

   > **Correct answer:** b) The tangent at $x=2$ has slope $f'(2)=3$ and passes through the point $(2, f(2))$.

---

#### 7.5.1 L'Hôpital's rule: statement (forms $0/0$ and $\infty/\infty$)

**Worked Example**

Calculate $\displaystyle\lim_{x\to 0}\frac{\sin x}{x}$ using L'Hôpital's rule.

**Verify the indeterminate form:**

$$\lim_{x\to 0}\frac{\sin x}{x} = \frac{\sin 0}{0} = \frac{0}{0} \quad \checkmark$$

**Apply L'Hôpital** (differentiate numerator and denominator separately):

$$\lim_{x\to 0}\frac{\sin x}{x} \stackrel{L'H}{=} \lim_{x\to 0}\frac{(\sin x)'}{(x)'} = \lim_{x\to 0}\frac{\cos x}{1} = \cos 0 = 1$$

**Note:** This is the **fundamental trigonometric limit**, confirmed by L'Hôpital.

**Exercises with Solution**

**Basic Level:**

1. Calculate $\displaystyle\lim_{x\to1}\dfrac{x^2-1}{x-1}$ using L'Hôpital.

   > **Solution:** $\dfrac{0}{0}$. L'H: $\lim_{x\to1}\dfrac{2x}{1}=2$.  
   > (Direct verification: $\dfrac{(x-1)(x+1)}{x-1}=x+1\to2$.)

2. Calculate $\displaystyle\lim_{x\to0}\dfrac{e^x-1}{x}$.

   > **Solution:** $\dfrac{0}{0}$. L'H: $\lim_{x\to0}\dfrac{e^x}{1}=e^0=1$.

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x\to+\infty}\dfrac{\ln x}{x}$.

   > **Solution:** $\dfrac{\infty}{\infty}$. L'H: $\lim_{x\to\infty}\dfrac{1/x}{1}=\lim_{x\to\infty}\dfrac{1}{x}=0$.

4. Calculate $\displaystyle\lim_{x\to0}\dfrac{1-\cos x}{x^2}$.

   > **Solution:** $\dfrac{0}{0}$. L'H: $\lim_{x\to0}\dfrac{\sin x}{2x}$. Again $\dfrac{0}{0}$. L'H again: $\lim_{x\to0}\dfrac{\cos x}{2}=\dfrac{1}{2}$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Calculate the following limits, stating the indeterminate form and the method:

   a) $\displaystyle\lim_{x\to0}\dfrac{\tan x - x}{x^3}$  
   b) $\displaystyle\lim_{x\to+\infty}\dfrac{e^x}{x^2}$  
   c) $\displaystyle\lim_{x\to0}\dfrac{\ln(1+x)}{x}$

   > **Solution:**
   >
   > **a)** $\dfrac{0}{0}$. L'H: $\lim\dfrac{\sec^2x-1}{3x^2}=\lim\dfrac{\tan^2x}{3x^2}$. Using $\tan^2x\approx x^2$ near $0$: $\lim\dfrac{x^2}{3x^2}=\dfrac{1}{3}$.  
   > Result: $\dfrac{1}{3}$.
   >
   > **b)** $\dfrac{\infty}{\infty}$. L'H: $\lim\dfrac{e^x}{2x}$. $\dfrac{\infty}{\infty}$. L'H: $\lim\dfrac{e^x}{2}=+\infty$.
   >
   > **c)** $\dfrac{0}{0}$. L'H: $\lim_{x\to0}\dfrac{\frac{1}{1+x}}{1}=\dfrac{1}{1}=1$.

**Multiple Choice Test**

6. L'Hôpital's rule can be applied when the limit presents the form:
   - a) $0+\infty$
   - b) $\dfrac{0}{0}$ or $\dfrac{\infty}{\infty}$
   - c) $0\cdot0$
   - d) $1+\infty$

   > **Correct answer:** b) L'Hôpital applies directly to the indeterminate forms $\dfrac{0}{0}$ and $\dfrac{\infty}{\infty}$.

7. When applying L'Hôpital to $\lim\dfrac{f(x)}{g(x)}$, one differentiates:
   - a) The entire quotient $\dfrac{f}{g}$
   - b) The numerator $f$ and denominator $g$ separately, forming $\dfrac{f'}{g'}$
   - c) Only the numerator
   - d) The quotient using the quotient rule

   > **Correct answer:** b) L'Hôpital states that $\lim\dfrac{f(x)}{g(x)}=\lim\dfrac{f'(x)}{g'(x)}$, differentiating numerator and denominator separately.

---

#### 7.5.2 Iterated application of L'Hôpital's rule

**Worked Example**

Calculate $\displaystyle\lim_{x\to0}\frac{e^x-1-x}{x^2}$ applying L'Hôpital as many times as needed.

**First application** (form $\frac{0}{0}$):

$$\lim_{x\to0}\frac{e^x-1-x}{x^2} \stackrel{L'H}{=} \lim_{x\to0}\frac{e^x-1}{2x}$$

**Second application** (still $\frac{0}{0}$):

$$\lim_{x\to0}\frac{e^x-1}{2x} \stackrel{L'H}{=} \lim_{x\to0}\frac{e^x}{2} = \frac{e^0}{2} = \frac{1}{2}$$

**Exercises with Solution**

**Basic Level:**

1. Apply L'Hôpital twice to calculate $\displaystyle\lim_{x\to0}\dfrac{x-\sin x}{x^3}$.

   > **Solution:** L'H$_1$: $\lim\dfrac{1-\cos x}{3x^2}$ ($\frac{0}{0}$). L'H$_2$: $\lim\dfrac{\sin x}{6x}$ ($\frac{0}{0}$). L'H$_3$: $\lim\dfrac{\cos x}{6}=\dfrac{1}{6}$.

2. Calculate $\displaystyle\lim_{x\to+\infty}\dfrac{x^2}{e^x}$.

   > **Solution:** $\dfrac{\infty}{\infty}$. L'H: $\lim\dfrac{2x}{e^x}$. L'H: $\lim\dfrac{2}{e^x}=0$.

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x\to0}\dfrac{e^x - 1 - x - \frac{x^2}{2}}{x^3}$.

   > **Solution:** Applying L'Hôpital three times:  
   > L'H$_1$: $\lim\dfrac{e^x-1-x}{3x^2}$. L'H$_2$: $\lim\dfrac{e^x-1}{6x}$. L'H$_3$: $\lim\dfrac{e^x}{6}=\dfrac{1}{6}$.

4. Calculate $\displaystyle\lim_{x\to+\infty}\dfrac{(\ln x)^3}{x}$.

   > **Solution:** $\dfrac{\infty}{\infty}$. L'H: $\lim\dfrac{3(\ln x)^2\cdot\frac{1}{x}}{1}=\lim\dfrac{3(\ln x)^2}{x}$.  
   > L'H again: $\lim\dfrac{6\ln x\cdot\frac{1}{x}}{1}=\lim\dfrac{6\ln x}{x}$. L'H: $\lim\dfrac{6/x}{1}=0$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Calculate:

   a) $\displaystyle\lim_{x\to0}\dfrac{x^2}{1-\cos x}$  
   b) $\displaystyle\lim_{x\to0}\dfrac{\sin x - x\cos x}{x^3}$

   > **Solution:**
   >
   > **a)** $\dfrac{0}{0}$. L'H: $\lim\dfrac{2x}{\sin x}$ ($\dfrac{0}{0}$), L'H: $\lim\dfrac{2}{\cos x}=\dfrac{2}{1}=2$.
   >
   > **b)** $\dfrac{0}{0}$. L'H: $\lim\dfrac{\cos x - (\cos x - x\sin x)}{3x^2}=\lim\dfrac{x\sin x}{3x^2}=\lim\dfrac{\sin x}{3x}$.  
   > L'H: $\lim\dfrac{\cos x}{3}=\dfrac{1}{3}$.

**Multiple Choice Test**

6. If after applying L'Hôpital once the limit is still $\frac{0}{0}$ or $\frac{\infty}{\infty}$:
   - a) The limit does not exist
   - b) L'Hôpital can be applied again
   - c) The result is $0$
   - d) Another method must be used

   > **Correct answer:** b) L'Hôpital can be applied iteratively as long as the indeterminate form persists.

7. $\displaystyle\lim_{x\to0}\dfrac{\sin x - x}{x^3}$ using L'Hôpital gives:
   - a) $0$
   - b) $1$
   - c) $-\dfrac{1}{6}$
   - d) $\dfrac{1}{6}$

   > **Correct answer:** c) After three applications of L'Hôpital we obtain $\lim_{x\to0}\dfrac{-\cos x}{6}=-\dfrac{1}{6}$.

---

#### 7.5.3 Resolving $0\cdot\infty$, $\infty-\infty$ and exponential indeterminate forms using L'Hôpital

**Worked Example**

Calculate $\displaystyle\lim_{x\to 0^+}x\ln x$ (form $0\cdot\infty$).

**Transform to the form $\frac{0}{0}$ or $\frac{\infty}{\infty}$:**

$$x\ln x = \frac{\ln x}{1/x}$$

As $x\to0^+$: numerator $\to-\infty$, denominator $\to+\infty$ → form $\frac{-\infty}{+\infty}$.

**Apply L'Hôpital:**

$$\lim_{x\to 0^+}\frac{\ln x}{1/x} \stackrel{L'H}{=} \lim_{x\to 0^+}\frac{1/x}{-1/x^2} = \lim_{x\to 0^+}(-x) = 0$$

**Result:** $\displaystyle\lim_{x\to 0^+}x\ln x = 0$.

**Exercises with Solution**

**Basic Level:**

1. Calculate $\displaystyle\lim_{x\to+\infty}xe^{-x}$ (form $\infty\cdot0$).

   > **Solution:** $\dfrac{x}{e^x}$ ($\dfrac{\infty}{\infty}$). L'H: $\lim\dfrac{1}{e^x}=0$.

2. Calculate $\displaystyle\lim_{x\to+\infty}(\sqrt{x+1}-\sqrt{x})$ (form $\infty-\infty$).

   > **Solution:** Rationalise: $\dfrac{(x+1)-x}{\sqrt{x+1}+\sqrt{x}}=\dfrac{1}{\sqrt{x+1}+\sqrt{x}}\to0$.

**Intermediate Level:**

3. Calculate $\displaystyle\lim_{x\to1^-}\left(\frac{1}{\ln x}+\frac{1}{x-1}\right)$ (form $\infty-\infty$ or $-\infty+\infty$).

   > **Solution:** $\dfrac{(x-1)+\ln x}{(x-1)\ln x}$. As $x\to1$: $\dfrac{0}{0}$. L'H: $\dfrac{1+1/x}{\ln x+1}$ → at $x=1$: $\dfrac{2}{0+1}=2$.

4. Calculate $\displaystyle\lim_{x\to0^+}(1+x)^{1/x}$ (form $1^\infty$).

   > **Solution:** Let $L=\lim(1+x)^{1/x}$. $\ln L=\lim\dfrac{\ln(1+x)}{x}$. L'H: $\lim\dfrac{1/(1+x)}{1}=1$. So $L=e^1=e$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Calculate:

   a) $\displaystyle\lim_{x\to+\infty}\left(1+\dfrac{2}{x}\right)^x$ (form $1^\infty$)  
   b) $\displaystyle\lim_{x\to0^+}x^x$ (form $0^0$)  
   c) $\displaystyle\lim_{x\to+\infty}x\cdot\ln\left(1+\dfrac{1}{x}\right)$ (form $\infty\cdot0$)

   > **Solution:**
   >
   > **a)** $\ln L=\lim x\ln\left(1+\dfrac{2}{x}\right)=\lim\dfrac{\ln(1+2/x)}{1/x}$. L'H: $\lim\dfrac{\frac{-2/x^2}{1+2/x}}{-1/x^2}=\lim\dfrac{2}{1+2/x}=2$. $L=e^2$.
   >
   > **b)** $\ln L=\lim_{x\to0^+}x\ln x=0$ (calculated above). $L=e^0=1$.
   >
   > **c)** $\dfrac{\ln(1+1/x)}{1/x}$. L'H: $\dfrac{\frac{-1/x^2}{1+1/x}}{-1/x^2}=\dfrac{1}{1+1/x}\to1$.

**Multiple Choice Test**

6. To calculate $\lim_{x\to0^+}x^x$ (form $0^0$), the technique used is:
   - a) Rationalisation
   - b) L'Hôpital directly
   - c) Take logarithms and then L'Hôpital
   - d) Substitution $t=1/x$

   > **Correct answer:** c) Write $y=x^x$, take $\ln y=x\ln x$ and calculate the limit of $x\ln x$ (form $0\cdot\infty$) with L'Hôpital.

7. $\displaystyle\lim_{x\to0^+}x\ln x$ equals:
   - a) $-\infty$
   - b) $1$
   - c) $0$
   - d) $e$

   > **Correct answer:** c) As calculated, $\lim_{x\to0^+}x\ln x=0$.

---

#### 7.6.1 Rolle's theorem: statement, conditions and geometric interpretation

**Worked Example**

Verify that $f(x)=x^3-3x$ satisfies the hypotheses of Rolle's theorem on $[-\sqrt{3},\sqrt{3}]$ and find the guaranteed point $c$.

**Verification of hypotheses:**

1. **Continuity on $[-\sqrt{3},\sqrt{3}]$:** $f$ is a polynomial → continuous on $\mathbb{R}$.

2. **Differentiability on $(-\sqrt{3},\sqrt{3})$:** $f$ is a polynomial → differentiable on $\mathbb{R}$.

3. **Equal values at the endpoints:**
$$f(-\sqrt{3})=(-\sqrt{3})^3-3(-\sqrt{3})=-3\sqrt{3}+3\sqrt{3}=0$$
$$f(\sqrt{3})=(\sqrt{3})^3-3\sqrt{3}=3\sqrt{3}-3\sqrt{3}=0$$
$f(-\sqrt{3})=f(\sqrt{3})=0$ ✓

**Conclusion of Rolle's theorem:** There exists $c\in(-\sqrt{3},\sqrt{3})$ such that $f'(c)=0$.

**Find $c$:**

$$f'(x)=3x^2-3=0 \Rightarrow x^2=1 \Rightarrow x=\pm1$$

Both $\pm1\in(-\sqrt{3},\sqrt{3})$ ✓. The values are $c=-1$ and $c=1$.

**Geometric interpretation:** At the points $(-1, 2)$ and $(1, -2)$, the tangent to the curve is horizontal (parallel to the chord joining the endpoints, which is also horizontal).

**Exercises with Solution**

**Basic Level:**

1. Can Rolle's theorem be applied to $f(x)=x^2-4$ on $[-2,2]$? If so, find $c$.

   > **Solution:** $f(-2)=0=f(2)$, $f$ continuous and differentiable. Yes. $f'(x)=2x=0 \Rightarrow c=0\in(-2,2)$ ✓.

2. Can Rolle's theorem be applied to $g(x)=|x|$ on $[-1,1]$?

   > **Solution:** $g(-1)=1=g(1)$, $g$ continuous on $[-1,1]$. But $g$ **is not differentiable** at $x=0\in(-1,1)$. The hypotheses of Rolle **are not satisfied**; it cannot be applied directly.

**Intermediate Level:**

3. Verify that $f(x)=\sin x$ satisfies Rolle's theorem on $[0,\pi]$ and find $c$.

   > **Solution:** $f(0)=0=f(\pi)$, $\sin$ continuous and differentiable. $f'(x)=\cos x=0 \Rightarrow x=\pi/2\in(0,\pi)$. $c=\pi/2$.

4. Prove that $f(x)=e^x\sin x$ has at least one zero of $f'$ in $(0,\pi)$.

   > **Solution:** $f(0)=0$ and $f(\pi)=e^\pi\sin\pi=0$. $f$ continuous and differentiable. By Rolle, $\exists c\in(0,\pi)$: $f'(c)=0$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=x^3-x^2-x+1$.

   a) Factorise $f(x)$ or find its roots.  
   b) Verify that the hypotheses of Rolle's theorem hold between two consecutive roots.  
   c) Find the values of $c$ guaranteed by Rolle between each pair of roots.

   > **Solution:**
   >
   > **a)** $f(1)=1-1-1+1=0$, $f(-1)=-1-1+1+1=0$. Roots: $x=1$ and $x=-1$.  
   > $f(x)=(x-1)(x+1)(x-1)=(x-1)^2(x+1)$. Roots: $x=-1$ (simple) and $x=1$ (double).
   >
   > **b)** On $[-1,1]$: $f(-1)=0=f(1)$, $f$ continuous and differentiable (polynomial). Rolle's hypotheses satisfied ✓.
   >
   > **c)** $f'(x)=3x^2-2x-1=(3x+1)(x-1)=0 \Rightarrow x=-\dfrac{1}{3}$ or $x=1$.  
   > $c=-\dfrac{1}{3}\in(-1,1)$ ✓ (the other value $x=1$ is the endpoint, not interior).

**Multiple Choice Test**

6. Rolle's theorem guarantees the existence of $c\in(a,b)$ with $f'(c)=0$ if:
   - a) $f(a)=f(b)$, $f$ continuous on $[a,b]$ and differentiable on $(a,b)$
   - b) $f(a)\neq f(b)$ and $f$ is differentiable
   - c) $f'(a)=f'(b)=0$
   - d) $f$ is increasing on $(a,b)$

   > **Correct answer:** a) These are exactly the three hypotheses of Rolle's theorem.

7. If $f$ satisfies the hypotheses of Rolle on $[a,b]$, then there exists at least one $c\in(a,b)$ with:
   - a) $f(c)=0$
   - b) $f(c)=\dfrac{f(a)+f(b)}{2}$
   - c) $f'(c)=0$
   - d) $f''(c)=0$

   > **Correct answer:** c) The conclusion of Rolle is the existence of a point with zero derivative, not the zero value of the function.
---

#### 7.6.2 Lagrange's mean value theorem: statement and applications

**Worked Example**

Apply the mean value theorem (Lagrange) to $f(x)=x^3$ on $[0,2]$: verify the hypotheses and find $c$.

**Hypotheses:**

1. $f$ continuous on $[0,2]$ ✓ (polynomial)
2. $f$ differentiable on $(0,2)$ ✓

**Lagrange's conclusion:** $\exists c\in(0,2)$ such that:

$$f'(c) = \frac{f(2)-f(0)}{2-0} = \frac{8-0}{2} = 4$$

**Find $c$:**

$$f'(x)=3x^2=4 \Rightarrow x^2=\frac{4}{3} \Rightarrow x=\frac{2}{\sqrt{3}}=\frac{2\sqrt{3}}{3}\approx1.15$$

Since $\dfrac{2\sqrt{3}}{3}\approx1.15\in(0,2)$ ✓.

**Interpretation:** At $c=\dfrac{2\sqrt{3}}{3}$, the slope of the tangent to $x^3$ equals the slope of the chord joining $(0,0)$ and $(2,8)$.

**Exercises with Solution**

**Basic Level:**

1. Apply Lagrange to $f(x)=x^2+1$ on $[1,3]$ and find $c$.

   > **Solution:** $\dfrac{f(3)-f(1)}{3-1}=\dfrac{10-2}{2}=4=f'(c)=2c$. So $c=2\in(1,3)$ ✓.

2. Can Lagrange's theorem be applied to $f(x)=|x|$ on $[-1,1]$?

   > **Solution:** $f$ is continuous on $[-1,1]$ but not differentiable at $x=0\in(-1,1)$. Lagrange's hypotheses **are not satisfied** (differentiability on $(-1,1)$ is missing).

**Intermediate Level:**

3. Apply Lagrange to $f(x)=\ln x$ on $[1,e]$ and find $c$.

   > **Solution:** $\dfrac{f(e)-f(1)}{e-1}=\dfrac{1-0}{e-1}=\dfrac{1}{e-1}=f'(c)=\dfrac{1}{c}$. So $c=e-1\approx1.72\in(1,e)$ ✓.

4. Use Lagrange's theorem to prove that $|\sin a - \sin b|\leq|a-b|$ for all $a,b\in\mathbb{R}$.

   > **Solution:** Applying Lagrange to $f(x)=\sin x$ on $[a,b]$ (or $[b,a]$):  
   > $\exists c$ between $a$ and $b$ such that $\sin a-\sin b=\cos c\cdot(a-b)$.  
   > $|\sin a-\sin b|=|\cos c|\cdot|a-b|\leq1\cdot|a-b|=|a-b|$. $\blacksquare$

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=e^x$.

   a) State the mean value theorem (Lagrange).  
   b) Apply it to $f$ on the interval $[0,1]$ and find $c$.  
   c) Interpret the result geometrically.

   > **Solution:**
   >
   > **a)** If $f$ is continuous on $[a,b]$ and differentiable on $(a,b)$, then there exists $c\in(a,b)$ such that $f'(c)=\dfrac{f(b)-f(a)}{b-a}$.
   >
   > **b)** $\dfrac{f(1)-f(0)}{1-0}=e-1=f'(c)=e^c$. So $e^c=e-1 \Rightarrow c=\ln(e-1)\approx\ln(1.718)\approx0.541\in(0,1)$ ✓.
   >
   > **c)** At $c=\ln(e-1)$, the tangent line to $e^x$ is parallel to the chord joining $(0,1)$ and $(1,e)$.

**Multiple Choice Test**

6. Lagrange's (mean value) theorem guarantees the existence of $c\in(a,b)$ such that $f'(c)$ equals:
   - a) $\dfrac{f(a)+f(b)}{2}$
   - b) $\dfrac{f(b)-f(a)}{b-a}$
   - c) $\dfrac{f'(a)+f'(b)}{2}$
   - d) $f(b)-f(a)$

   > **Correct answer:** b) The slope of the chord is $\dfrac{f(b)-f(a)}{b-a}$, which equals the slope of some interior tangent.

7. Rolle's theorem is a special case of Lagrange when:
   - a) $f(a)=f(b)=0$
   - b) $f(a)=f(b)$
   - c) $f'(a)=f'(b)$
   - d) $a=-b$

   > **Correct answer:** b) If $f(a)=f(b)$, the chord is horizontal (slope $0$), and Lagrange guarantees $f'(c)=0$, which is exactly Rolle.

---

#### 7.6.3 Consequences: functions with zero derivative, functions with the same derivative

**Worked Example**

Prove that if $f'(x)=0$ for all $x\in(a,b)$, then $f$ is constant on $[a,b]$. Apply this to $f(x)=\sin^2x+\cos^2x$.

**Proof:**

Let $x_1, x_2\in[a,b]$ with $x_1<x_2$. Applying Lagrange to $f$ on $[x_1,x_2]$:

$$\exists c\in(x_1,x_2): \quad f(x_2)-f(x_1)=f'(c)(x_2-x_1)=0\cdot(x_2-x_1)=0$$

Therefore $f(x_2)=f(x_1)$ for every pair of points → $f$ is constant. $\blacksquare$

**Application:** $f(x)=\sin^2x+\cos^2x$. $f'(x)=2\sin x\cos x+2\cos x(-\sin x)=0$ for all $x$. By the theorem, $f$ is constant on $\mathbb{R}$, and since $f(0)=0+1=1$, we have $\sin^2x+\cos^2x=1$ for all $x$.

**Exercises with Solution**

**Basic Level:**

1. If $f'(x)=g'(x)$ for all $x\in\mathbb{R}$, what is the relationship between $f$ and $g$?

   > **Solution:** $(f-g)'(x)=f'(x)-g'(x)=0$. By the theorem, $f(x)-g(x)=C$ (constant), i.e. $f(x)=g(x)+C$.

2. Find all functions whose derivative is $f'(x)=3x^2$.

   > **Solution:** Any antiderivative of $3x^2$ is $x^3+C$ ($C\in\mathbb{R}$). By the zero-derivative theorem applied to the difference, all solutions differ by a constant.

**Intermediate Level:**

3. Prove that $f(x)=\arcsin x+\arccos x$ is constant using the derivative.

   > **Solution:** $f'(x)=\dfrac{1}{\sqrt{1-x^2}}+\left(-\dfrac{1}{\sqrt{1-x^2}}\right)=0$ for $x\in(-1,1)$.  
   > By the theorem, $f$ is constant. $f(0)=0+\pi/2=\pi/2$. So $\arcsin x+\arccos x=\dfrac{\pi}{2}$.

4. Does there exist a function $f$ such that $f'(x)=f(x)$ for all $x$ with $f(0)=1$? Justify.

   > **Solution:** Yes: $f(x)=e^x$. If there were another solution $g$ with $g'=g$ and $g(0)=1$, then $(g/e^x)'=\dfrac{g'e^x-ge^x}{e^{2x}}=0$, so $g/e^x=C=1$ and $g=e^x$. The solution is unique.

**EVAU Level:**

5. **(EVAU Madrid Style)**

   a) State the consequence of Lagrange's theorem relating to functions with zero derivative.  
   b) Use this result to prove that if $f'(x)>0$ on $(a,b)$, then $f$ is strictly increasing on $(a,b)$.  
   c) Apply part b) to verify that $f(x)=e^x$ is increasing on $\mathbb{R}$.

   > **Solution:**
   >
   > **a)** If $f'(x)=0$ for all $x\in(a,b)$ and $f$ is continuous on $[a,b]$, then $f$ is constant on $[a,b]$.
   >
   > **b)** Let $x_1<x_2$ in $(a,b)$. By Lagrange: $f(x_2)-f(x_1)=f'(c)(x_2-x_1)$ with $c\in(x_1,x_2)$.  
   > Since $f'(c)>0$ and $x_2-x_1>0$: $f(x_2)-f(x_1)>0$, i.e. $f(x_2)>f(x_1)$ → $f$ is strictly increasing.
   >
   > **c)** $(e^x)'=e^x>0$ for all $x\in\mathbb{R}$. By part b), $e^x$ is strictly increasing on $\mathbb{R}$.

**Multiple Choice Test**

6. If $f'(x)=g'(x)$ for all real $x$, then:
   - a) $f(x)=g(x)$ for all $x$
   - b) $f(x)=g(x)+C$ for some constant $C$
   - c) $f$ and $g$ are equal if $f(0)=0$
   - d) $f(x)=g(x)\cdot C$ for some constant $C$

   > **Correct answer:** b) If two functions have the same derivative on an interval, they differ by an additive constant.

7. The proof that $f'=0$ implies constancy uses:
   - a) Bolzano's theorem
   - b) Lagrange's mean value theorem
   - c) The definition of limit
   - d) L'Hôpital's rule

   > **Correct answer:** b) Lagrange is applied to show that $f(x_2)-f(x_1)=f'(c)\cdot(x_2-x_1)=0$.

---

#### 7.7.1 Relative extrema: necessary condition and second derivative criterion

**Worked Example**

Find the relative extrema of $f(x)=x^4-4x^3+4x^2$ using the necessary condition and the second derivative criterion.

**Step 1 — First derivative:**

$$f'(x) = 4x^3-12x^2+8x = 4x(x^2-3x+2) = 4x(x-1)(x-2)$$

**Step 2 — Critical points** ($f'=0$): $x=0$, $x=1$, $x=2$.

**Step 3 — Second derivative:**

$$f''(x) = 12x^2-24x+8$$

**Step 4 — Second derivative criterion:**

| $x$ | $f'(x)=0$ | $f''(x)$ | Type |
|-----|-----------|-----------|------|
| $0$ | ✓ | $f''(0)=8>0$ | Relative minimum |
| $1$ | ✓ | $f''(1)=12-24+8=-4<0$ | Relative maximum |
| $2$ | ✓ | $f''(2)=48-48+8=8>0$ | Relative minimum |

**Values:** $f(0)=0$, $f(1)=1-4+4=1$, $f(2)=16-32+16=0$.

**Exercises with Solution**

**Basic Level:**

1. Find the extrema of $f(x)=x^2-6x+5$.

   > **Solution:** $f'(x)=2x-6=0 \Rightarrow x=3$. $f''(3)=2>0$ → relative minimum at $(3,-4)$.

2. Find the extrema of $g(x)=-x^3+3x$.

   > **Solution:** $g'(x)=-3x^2+3=0 \Rightarrow x=\pm1$. $g''(x)=-6x$.  
   > $g''(1)=-6<0$ → maximum at $(1,2)$. $g''(-1)=6>0$ → minimum at $(-1,-2)$.

**Intermediate Level:**

3. Find the extrema of $h(x)=xe^{-x}$.

   > **Solution:** $h'(x)=e^{-x}-xe^{-x}=e^{-x}(1-x)=0 \Rightarrow x=1$ (since $e^{-x}>0$).  
   > $h''(x)=-e^{-x}(1-x)+e^{-x}(-1)=e^{-x}(x-2)$.  
   > $h''(1)=e^{-1}(-1)<0$ → relative maximum at $(1,e^{-1})$.

4. Find the extrema of $f(x)=\ln x - x$ for $x>0$.

   > **Solution:** $f'(x)=\dfrac{1}{x}-1=0 \Rightarrow x=1$.  
   > $f''(x)=-\dfrac{1}{x^2}$; $f''(1)=-1<0$ → relative maximum at $(1,-1)$. (Note: $f(1)=\ln1-1=-1$.)

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=\dfrac{x^2}{e^x}$.

   a) Find $f'(x)$ and the critical points.  
   b) Classify the extrema using the second derivative criterion.  
   c) Determine the maximum/minimum values.

   > **Solution:**
   >
   > **a)** $f'(x)=\dfrac{2x\cdot e^x-x^2\cdot e^x}{e^{2x}}=\dfrac{e^x\cdot x(2-x)}{e^{2x}}=\dfrac{x(2-x)}{e^x}$.  
   > $f'(x)=0 \Leftrightarrow x=0$ or $x=2$.
   >
   > **b)** $f''(x)=\dfrac{(2-2x)e^x-x(2-x)e^x}{e^{2x}}=\dfrac{2-2x-2x+x^2}{e^x}=\dfrac{x^2-4x+2}{e^x}$.  
   > $f''(0)=\dfrac{2}{1}=2>0$ → relative minimum at $x=0$.  
   > $f''(2)=\dfrac{4-8+2}{e^2}=\dfrac{-2}{e^2}<0$ → relative maximum at $x=2$.
   >
   > **c)** $f(0)=0$ (relative minimum); $f(2)=\dfrac{4}{e^2}$ (relative maximum).

**Multiple Choice Test**

6. The condition $f'(a)=0$ at an interior point of the domain is:
   - a) Sufficient for $a$ to be a relative extremum
   - b) Necessary but not sufficient for $a$ to be a relative extremum
   - c) Necessary and sufficient for a relative extremum
   - d) Unnecessary for studying extrema

   > **Correct answer:** b) $f'(a)=0$ is a necessary condition; it can also occur at inflection points (e.g. $f(x)=x^3$ at $x=0$).

7. If $f'(a)=0$ and $f''(a)>0$, then $f$ has at $x=a$:
   - a) A relative maximum
   - b) A relative minimum
   - c) An inflection point
   - d) An asymptote

   > **Correct answer:** b) By the second derivative criterion, $f''(a)>0$ indicates a relative minimum.

---

#### 7.7.2 Extrema at the boundary of the domain and at points of non-differentiability

**Worked Example**

Find the absolute extrema of $f(x)=|x^2-4|$ on $[-3,3]$.

**Step 1 — Interior critical points:**

$f(x)=|x^2-4|=\begin{cases}x^2-4 & |x|\geq2\\4-x^2 & |x|<2\end{cases}$

In the interior: non-differentiable points at $x=\pm2$ (corners) and critical point of each piece:

- For $|x|>2$: $f'(x)=2x=0\Rightarrow x=0$ (outside this piece's domain).
- For $|x|<2$: $f'(x)=-2x=0\Rightarrow x=0$. At $x=0$: $f(0)=4$.
- At $x=\pm2$: $f(\pm2)=0$.

**Step 2 — Boundary values:** $f(-3)=|9-4|=5$; $f(3)=5$.

**Step 3 — Table of candidates:**

| $x$ | $f(x)$ |
|-----|--------|
| $-3$ | $5$ |
| $-2$ | $0$ |
| $0$ | $4$ |
| $2$ | $0$ |
| $3$ | $5$ |

**Absolute extrema:** Absolute maximum $5$ at $x=\pm3$; absolute minima $0$ at $x=\pm2$.

**Exercises with Solution**

**Basic Level:**

1. Find the absolute extrema of $f(x)=x^2-2x$ on $[0,3]$.

   > **Solution:** $f'(x)=2x-2=0 \Rightarrow x=1$. $f(0)=0$; $f(1)=-1$; $f(3)=3$. Absolute minimum: $-1$ at $x=1$; absolute maximum: $3$ at $x=3$.

2. Find the absolute extrema of $g(x)=\sin x$ on $[0, 2\pi]$.

   > **Solution:** $g'=\cos x=0 \Rightarrow x=\pi/2, 3\pi/2$. $g(0)=0$; $g(\pi/2)=1$; $g(3\pi/2)=-1$; $g(2\pi)=0$.  
   > Absolute maximum: $1$ at $x=\pi/2$; absolute minimum: $-1$ at $x=3\pi/2$.

**Intermediate Level:**

3. Find the absolute extrema of $h(x)=x^3-3x$ on $[-2,2]$.

   > **Solution:** $h'=3x^2-3=0 \Rightarrow x=\pm1$. $h(-2)=-2$; $h(-1)=2$; $h(1)=-2$; $h(2)=2$.  
   > Absolute maxima: $2$ (at $x=-1$ and $x=2$); absolute minima: $-2$ (at $x=1$ and $x=-2$).

4. Determine whether $f(x)=x^{2/3}$ has an extremum at $x=0$ even though it is not differentiable there.

   > **Solution:** $f'(x)=\dfrac{2}{3}x^{-1/3}$ does not exist at $x=0$. But for $x<0$: $f'<0$; for $x>0$: $f'>0$. There is a sign change from $-$ to $+$ → minimum at $x=0$, $f(0)=0$.

**EVAU Level:**

5. **(EVAU Madrid Style)** Let $f(x)=2x^3-3x^2-12x+1$ on $[-2,3]$.

   a) Find the interior critical points.  
   b) Evaluate $f$ at the critical points and at the endpoints of the interval.  
   c) State the absolute extrema of $f$ on $[-2,3]$.

   > **Solution:**
   >
   > **a)** $f'(x)=6x^2-6x-12=6(x^2-x-2)=6(x-2)(x+1)=0 \Rightarrow x=-1$ and $x=2$.
   >
   > **b)** $f(-2)=2(-8)-3(4)-12(-2)+1=-16-12+24+1=-3$.  
   > $f(-1)=2(-1)-3(1)-12(-1)+1=-2-3+12+1=8$.  
   > $f(2)=2(8)-3(4)-12(2)+1=16-12-24+1=-19$.  
   > $f(3)=2(27)-3(9)-12(3)+1=54-27-36+1=-8$.
   >
   > **c)** Absolute maximum: $8$ at $x=-1$. Absolute minimum: $-19$ at $x=2$.

**Multiple Choice Test**

6. To find the absolute extremum of a continuous function on $[a,b]$, one evaluates $f$ at:
   - a) Only the points where $f'=0$
   - b) The endpoints of the interval and the interior critical points (where $f'=0$ or does not exist)
   - c) The midpoint of the interval
   - d) Only the endpoints of the interval

   > **Correct answer:** b) The candidates for absolute extremum are the interior critical points and the endpoints of the interval.

7. If $f$ is not differentiable at $x=c\in(a,b)$ but is continuous, the point $c$:
   - a) Cannot be a relative extremum
   - b) May be a relative extremum
   - c) Is necessarily an absolute extremum
   - d) Is an inflection point

   > **Correct answer:** b) Points of non-differentiability are candidates for extrema. Example: $|x|$ at $x=0$ has a minimum even though it is not differentiable there.

---

#### 7.7.3 Setting up and solving optimisation problems in real-world contexts

**Worked Example**

A rectangular farm is to be fenced using $120$ m of fencing. One side borders a river and needs no fence. What dimensions maximise the area?

**Variables:** Let $x$ be the side perpendicular to the river (two sides) and $y$ the side parallel to the river (one side).

**Constraint:** $2x+y=120 \Rightarrow y=120-2x$.

**Objective function (area):**

$$A(x) = x\cdot y = x(120-2x) = 120x-2x^2, \quad x\in(0,60)$$

**Optimise:**

$$A'(x) = 120-4x = 0 \Rightarrow x=30$$

$$A''(x)=-4<0 \quad \Rightarrow \quad x=30 \text{ is a maximum.}$$

**Optimal dimensions:** $x=30$ m, $y=120-60=60$ m. **Maximum area:** $A=30\times60=1800$ m².

**Exercises with Solution**

**Basic Level:**

1. The sum of two positive numbers is $20$. What is the maximum of their product?

   > **Solution:** Let $x$ and $y=20-x$. $P=x(20-x)=20x-x^2$.  
   > $P'=20-2x=0 \Rightarrow x=10$. $P(10)=100$. Maximum product: $100$ (when $x=y=10$).

2. A cubic box of volume $8$ m³ is to be built. Minimise the total surface area.

   > **Solution:** Cube of side $a$: $V=a^3=8 \Rightarrow a=2$. Surface $=6a^2=24$ m². (The constraint fixes $a=2$, giving a single value.)

**Intermediate Level:**

3. Find the rectangle of perimeter $P=40$ cm with maximum area.

   > **Solution:** $2(x+y)=40$, $y=20-x$. $A=x(20-x)=20x-x^2$. $A'=20-2x=0\Rightarrow x=10$. Square of side $10$, area $100$ cm².

4. A cable of length $L$ is cut into two pieces; one is bent into a square and the other into a circle. How should it be cut to minimise the total area?

   > **Solution:** Let $x$ be the side of the square: $4x+2\pi r=L$, $r=\dfrac{L-4x}{2\pi}$.  
   > $A=x^2+\pi r^2=x^2+\dfrac{(L-4x)^2}{4\pi}$.  
   > $A'=2x-\dfrac{2(L-4x)}{\pi}=0$.  
   > $\pi x=(L-4x) \Rightarrow x(\pi+4)=L \Rightarrow x=\dfrac{L}{\pi+4}$.

**EVAU Level:**

5. **(EVAU Madrid Style)** A cylindrical soft-drink can has volume $330$ cm³. Find the dimensions of the cylinder (radius $r$ and height $h$) that minimise the amount of material (total surface area).

   **Note:** $V=\pi r^2 h=330$; $S=2\pi r^2+2\pi rh$.

   > **Solution:**
   >
   > From the constraint: $h=\dfrac{330}{\pi r^2}$.
   >
   > $S(r)=2\pi r^2+2\pi r\cdot\dfrac{330}{\pi r^2}=2\pi r^2+\dfrac{660}{r}$.
   >
   > $S'(r)=4\pi r-\dfrac{660}{r^2}=0 \Rightarrow 4\pi r^3=660 \Rightarrow r^3=\dfrac{165}{\pi} \Rightarrow r=\sqrt[3]{\dfrac{165}{\pi}}\approx3.74$ cm.
   >
   > $h=\dfrac{330}{\pi r^2}\approx\dfrac{330}{\pi\cdot13.98}\approx7.51$ cm.
   >
   > Verification: $h\approx2r$ (height equals diameter, the classic optimal can result). $S''=4\pi+\dfrac{1320}{r^3}>0$ → minimum ✓.

**Multiple Choice Test**

6. In an optimisation problem, the "objective function" is:
   - a) The constraint of the problem
   - b) The function to be maximised or minimised
   - c) The derivative of the area
   - d) The limit of the function at the endpoints

   > **Correct answer:** b) The objective function is the one to be optimised; the constraint establishes the condition linking the variables.

7. In the problem of an open-top box of fixed volume $V=1$, the minimum surface area is obtained when:
   - a) The box is a cube
   - b) The base is a square and $h=\dfrac{a}{2}$ (half the side length)
   - c) The box is taller than wide
   - d) The ratio $h/a=1$ (cube)

   > **Correct answer:** b) For an open-top box with square base, the minimum material is obtained when $h=a/2$, i.e. the height is half the side of the base.

---

#### 7.7.4 Geometric optimisation: minimum distances, extreme areas and volumes

**Worked Example**

Find the point of the parabola $y=x^2$ closest to the point $A=(0,1)$.

**Squared distance** (more convenient than the distance directly):

$$D(x)=x^2+(x^2-1)^2=x^2+x^4-2x^2+1=x^4-x^2+1$$

**Minimise $D$:**

$$D'(x)=4x^3-2x=2x(2x^2-1)=0 \Rightarrow x=0 \quad \text{or} \quad x^2=\frac{1}{2} \Rightarrow x=\pm\frac{1}{\sqrt{2}}$$

**Analysis:** $D''(x)=12x^2-2$.

- $D''(0)=-2<0$ → maximum at $x=0$.
- $D''\!\left(\pm\dfrac{1}{\sqrt{2}}\right)=6-2=4>0$ → minima at $x=\pm\dfrac{1}{\sqrt{2}}$.

**Closest points:** $\left(\pm\dfrac{1}{\sqrt{2}},\dfrac{1}{2}\right)$. Minimum squared distance: $D=\dfrac{1}{4}-\dfrac{1}{2}+1=\dfrac{3}{4}$, so $d=\dfrac{\sqrt{3}}{2}$.

**Exercises with Solution**

**Basic Level:**

1. Find the point of the line $y=2x+1$ closest to the origin.

   > **Solution:** Squared distance: $D(x)=x^2+(2x+1)^2=5x^2+4x+1$. $D'=10x+4=0\Rightarrow x=-\frac{2}{5}$.  
   > Point: $\left(-\frac{2}{5},\frac{1}{5}\right)$. Distance: $\dfrac{|0-0+1|}{\sqrt{5}}=\dfrac{1}{\sqrt{5}}=\dfrac{\sqrt{5}}{5}$.

2. Find the maximum area of a right triangle with hypotenuse $10$.

   > **Solution:** Legs $a$ and $b$ with $a^2+b^2=100$. $A=\dfrac{ab}{2}$. By AM-GM: $ab\leq\dfrac{a^2+b^2}{2}=50$, with equality when $a=b=5\sqrt{2}$. Maximum area: $\dfrac{50}{2}=25$.

**Intermediate Level:**

3. Inscribe the rectangle of maximum area in a semicircle of radius $R$.

   > **Solution:** Vertices at $(x,0)$, $(-x,0)$, $(-x,y)$, $(x,y)$ with $x^2+y^2=R^2$.  
   > $A=2x\cdot y=2x\sqrt{R^2-x^2}$. $A^2=4x^2(R^2-x^2)$.  
   > $(A^2)'=4(2xR^2-4x^3)=0\Rightarrow x^2=R^2/2\Rightarrow x=\dfrac{R}{\sqrt{2}}$, $y=\dfrac{R}{\sqrt{2}}$. Area: $R^2$.

4. Find the cylinder of maximum volume inscribed in a sphere of radius $R$.

   > **Solution:** Cylinder with radius $r$ and half-height $h$: $r^2+h^2=R^2$.  
   > $V=\pi r^2(2h)=2\pi(R^2-h^2)h$. $V'=2\pi(R^2-3h^2)=0\Rightarrow h=\dfrac{R}{\sqrt{3}}$.  
   > $r^2=R^2-\dfrac{R^2}{3}=\dfrac{2R^2}{3}$. $V_{\max}=\dfrac{4\pi R^3}{3\sqrt{3}}$.

**EVAU Level:**

5. **(EVAU Madrid Style)** A window is to be built in the shape of a rectangle topped by a semicircle. The total perimeter is $P=6$ m. Find the dimensions that maximise the area of the window.

   > **Solution:**
   >
   > Let $2r$ be the width (diameter of semicircle = width of rectangle) and $h$ the height of the rectangle.
   >
   > **Perimeter:** $2h+2r+\pi r=6 \Rightarrow h=\dfrac{6-2r-\pi r}{2}=3-r-\dfrac{\pi r}{2}$.
   >
   > **Area:** $A=2rh+\dfrac{\pi r^2}{2}=2r\left(3-r-\dfrac{\pi r}{2}\right)+\dfrac{\pi r^2}{2}=6r-2r^2-\pi r^2+\dfrac{\pi r^2}{2}=6r-2r^2-\dfrac{\pi r^2}{2}$.
   >
   > $A'=6-4r-\pi r=6-r(4+\pi)=0 \Rightarrow r=\dfrac{6}{4+\pi}\approx0.84$ m.
   >
   > $h=3-r\left(1+\dfrac{\pi}{2}\right)=3-\dfrac{6}{4+\pi}\cdot\dfrac{2+\pi}{2}=3-\dfrac{3(2+\pi)}{4+\pi}=\dfrac{3(4+\pi)-3(2+\pi)}{4+\pi}=\dfrac{6}{4+\pi}=r$.
   >
   > Therefore $h=r=\dfrac{6}{4+\pi}\approx0.84$ m. The width is $2r\approx1.68$ m.

**Multiple Choice Test**

6. To minimise the distance from a point $P$ to a curve, it is convenient to minimise:
   - a) The distance directly
   - b) The squared distance (to avoid the square root)
   - c) The tangent to the curve
   - d) The inverse function of the curve

   > **Correct answer:** b) Minimising $d^2$ is equivalent to minimising $d$ (since $d\geq0$), but algebraically simpler as it eliminates the square root.

7. The rectangle of maximum area inscribed in a circle is:
   - a) Any rectangle
   - b) The square
   - c) The rectangle with sides in ratio $1:2$
   - d) The equilateral triangle

   > **Correct answer:** b) By symmetry and optimisation calculus, the rectangle of maximum area inscribed in a circle is the square.

---

#### 7.7.5 Optimisation in motion and physics problems (velocity, acceleration)

**Worked Example**

The position of a projectile as a function of time is $s(t)=-5t^2+20t+1$ (m), for $t\geq0$.

a) Find the maximum velocity. When is it reached?  
b) Find the maximum height.  
c) When does it return to the ground?

**a) Velocity:**

$$v(t)=s'(t)=-10t+20$$

The velocity is maximum at the start ($t=0$): $v(0)=20$ m/s. Velocity decreases linearly (constant acceleration $a=-10$ m/s²). The velocity equals zero (highest point) when:

$$v(t)=0 \Rightarrow -10t+20=0 \Rightarrow t=2 \text{ s}$$

**b) Maximum height** (at $t=2$):

$$s(2)=-5(4)+20(2)+1=-20+40+1=21 \text{ m}$$

**c) Return to the ground** ($s=0$):

$$-5t^2+20t+1=0 \Rightarrow t=\frac{-20\pm\sqrt{400+20}}{-10}=\frac{-20\pm\sqrt{420}}{-10}$$

$t=\dfrac{20\pm\sqrt{420}}{10}=2\pm\dfrac{\sqrt{420}}{10}$. Since $t>0$: $t=2+\dfrac{\sqrt{420}}{10}\approx2+2.05=4.05$ s.

**Exercises with Solution**

**Basic Level:**

1. The position of a car is $s(t)=3t^2-12t+5$. At what instant is the velocity zero? Is that a minimum or maximum of position?

   > **Solution:** $v(t)=6t-12=0 \Rightarrow t=2$ s. $s''(t)=6>0$ → minimum of position at $t=2$.  
   > $s(2)=12-24+5=-7$ m.

2. A ball rises with $v(t)=10-2t$ m/s. At what instant is the velocity zero? What is the maximum height if $s(0)=0$?

   > **Solution:** $v(t)=0 \Rightarrow t=5$ s.  
   > $s(t)=\int v\,dt=10t-t^2+C$; $s(0)=0 \Rightarrow C=0$.  
   > Maximum height: $s(5)=50-25=25$ m.

**Intermediate Level:**

3. The temperature of a cooling object follows $T(t)=70e^{-0.1t}+20$ (°C), for $t\geq0$. Find the maximum cooling rate (in absolute value) and the instant at which it occurs.

   > **Solution:** $T'(t)=-7e^{-0.1t}$.  
   > $|T'(t)|=7e^{-0.1t}$ is strictly decreasing. The maximum value occurs at $t=0$: $|T'(0)|=7$ °C/s.  
   > Cooling is fastest at the initial instant.

4. The height of a rocket is $h(t)=-t^3+9t^2$ for $0\leq t\leq9$. Find the maximum positive velocity and acceleration.

   > **Solution:** $v(t)=h'(t)=-3t^2+18t$; $a(t)=v'(t)=-6t+18$.  
   > **Maximum velocity:** $v'(t)=0 \Rightarrow t=3$. $v(3)=-27+54=27$ m/s.  
   > **Maximum positive acceleration:** $a(t)>0$ for $t<3$. The maximum of $a$ on $[0,9]$ is at $t=0$: $a(0)=18$ m/s².

**EVAU Level:**

5. **(EVAU Madrid Style)** A particle moves in a straight line with position $s(t) = 2t^3 - 9t^2 + 12t$ (metres), $t\geq0$ (seconds).

   a) Find the velocity $v(t)$ and acceleration $a(t)$.  
   b) When is the particle at rest?  
   c) When is the velocity maximum? What is that value?  
   d) In which intervals does the particle move forward? In which does it move backward?

   > **Solution:**
   >
   > **a)** $v(t)=s'(t)=6t^2-18t+12=6(t^2-3t+2)=6(t-1)(t-2)$.  
   > $a(t)=v'(t)=12t-18=6(2t-3)$.
   >
   > **b)** $v(t)=0 \Rightarrow t=1$ s and $t=2$ s.
   >
   > **c)** $v'(t)=a(t)=0 \Rightarrow 12t-18=0 \Rightarrow t=\dfrac{3}{2}$ s.  
   > $v''(t)=12>0$ → minimum of $v$. So velocity has a **local minimum** at $t=3/2$ (not a maximum in the strict sense).  
   > For $t\geq0$: $v(0)=12$ m/s, $v\to+\infty$ as $t\to+\infty$. There is no global maximum. The local minimum is $v(3/2)=6\cdot(9/4-9/2+2)=6\cdot(-1/4)=-3/2$ m/s.
   >
   > **d)** $v(t)=6(t-1)(t-2)$:  
   > - $v>0$ for $t\in[0,1)$: **moves forward**.  
   > - $v<0$ for $t\in(1,2)$: **moves backward**.  
   > - $v>0$ for $t\in(2,+\infty)$: **moves forward**.

**Multiple Choice Test**

6. A particle has position $s(t)=t^3-6t^2$. The acceleration is zero when:
   - a) $t=0$
   - b) $t=2$
   - c) $t=4$
   - d) $t=6$

   > **Correct answer:** b) $s'(t)=3t^2-12t$; $s''(t)=6t-12=0 \Rightarrow t=2$.

7. If the velocity of an object is $v(t)=4t-8$, the object is at rest at:
   - a) $t=0$
   - b) $t=1$
   - c) $t=2$
   - d) $t=4$

   > **Correct answer:** c) $v(t)=0 \Rightarrow 4t-8=0 \Rightarrow t=2$ s.

---

## Summary of Chapters 6 and 7

This file contains complete exercises for:

**Chapter 6 — Limits and Continuity:**
- 6.1 Limit of a function at a point (5 subsections)
- 6.2 Limit calculation and indeterminate forms (6 subsections)
- 6.3 Limits at infinity and asymptotes (6 subsections)
- 6.4 Continuity of functions (5 subsections)
- 6.5 Continuity theorems (3 subsections)

**Chapter 7 — Derivatives and Applications:**
- 7.1 Concept of derivative (5 subsections)
- 7.2 Differentiation rules (6 subsections)
- 7.3 Differentiability (5 subsections)
- 7.4 Tangent and normal lines (3 subsections)
- 7.5 L'Hôpital's rule (3 subsections)
- 7.6 Mean value theorems (3 subsections)
- 7.7 Optimisation (5 subsections)

**Total exercises per subsection:** 1 Worked Example + 2 Basic + 2 Intermediate + 1 EVAU + 2 Multiple Choice = 8 items.

*Mathematics II — Year 2 of Upper Secondary (Bachillerato) · Community of Madrid · EVAU-style LOMLOE*
