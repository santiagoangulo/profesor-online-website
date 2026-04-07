# Mathematics Applied to the Social Sciences II
## Year 2 of Bachillerato — Comunidad de Madrid
### Curriculum: Decreto 64/2022 (LOMLOE)

**Description:** A complete thematic index organized into didactic chapters with three-level numbering. Each subsection includes a reference to the official "saberes básicos" block from Decreto 64/2022 (Comunidad de Madrid). Examples and applications are oriented toward the Social Sciences context (economics, political science, sociology, demography). This course consolidates and extends the content of CCSS I, with particular emphasis on matrix algebra, calculus (derivatives and integrals) and statistical inference.

---

## TABLE OF CONTENTS

1. [Matrices](#cap1)
2. [Determinants](#cap2)
3. [Systems of Linear Equations](#cap3)
4. [Linear Programming](#cap4)
5. [Limits, Continuity and Differentiability](#cap5)
6. [Derivatives and Applications](#cap6)
7. [Curve Sketching and Function Analysis](#cap7)
8. [Integrals](#cap8)
9. [Probability](#cap9)
10. [Probability Distributions](#cap10)
11. [Statistical Inference](#cap11)

---

## Chapter 1. Matrices {#cap1}

### 1.1 Concept and types of matrices

#### 1.1.1 Definition of a matrix: entries, rows, columns and size
`[Block: Algebra (1st term) > Matrices for systems of linear equations and graphs; Block: Numbers and Operations > Addition and product of matrices]`
Formal definition $A = (a_{ij})$ of size $m \times n$. Notation. Square, rectangular, row, column matrices. Applications: representing tabular data in social sciences (contingency tables, input-output matrices).

#### 1.1.2 Special types of matrices: identity, zero, diagonal, triangular, symmetric
`[Block: Numbers and Operations > Addition and product of matrices, properties]`
Characterization of each type. Relevant properties. The identity matrix $I_n$ and its role in matrix algebra.

#### 1.1.3 Transpose of a matrix: definition and properties
`[Block: Numbers and Operations > Addition and product of matrices, properties]`
Definition $A^T = (a_{ji})$. Properties: $(A^T)^T = A$, $(A+B)^T = A^T + B^T$, $(AB)^T = B^T A^T$. Symmetric and skew-symmetric matrices.

### 1.2 Matrix operations

#### 1.2.1 Matrix addition and subtraction: definition and properties
`[Block: Numbers and Operations > Addition and product of matrices, properties]`
Conformability condition (same size). Commutativity, associativity, neutral element (zero matrix), additive inverse. Applications: adding statistical data tables.

#### 1.2.2 Scalar multiplication of a matrix
`[Block: Numbers and Operations > Addition and product of matrices, properties]`
Definition. Distributive properties. Applications: data scaling, pricing models with a parameter.

#### 1.2.3 Matrix multiplication: conformability condition, definition and calculation
`[Block: Numbers and Operations > Addition and product of matrices, properties]`
Condition: number of columns of $A$ = number of rows of $B$. Definition $c_{ij} = \sum_k a_{ik} b_{kj}$. Step-by-step calculation. Size of the resulting matrix.

#### 1.2.4 Properties of matrix multiplication: associativity, distributivity and NON-commutativity
`[Block: Numbers and Operations > Addition and product of matrices, properties]`
Counterexamples of non-commutativity. Properties that do hold. Algebraic consequences: $AB = 0 \not\Rightarrow A = 0$ or $B = 0$.

#### 1.2.5 Powers of square matrices
`[Block: Numbers and Operations > Addition and product of matrices, properties]`
Definition of $A^k$ for $k \in \mathbb{N}$. $A^0 = I$. Computing powers. Applications: Markov chains, state-transition models (demography, voting behaviour).

#### 1.2.6 Matrices and graphs: adjacency matrix
`[Block: Algebra (1st term) > Matrices for systems of linear equations and graphs]`
Representing a graph through its adjacency matrix. Relationship between $A^k$ and paths of length $k$. Applications: social contact networks, influence analysis in networks.

### 1.3 Computational thinking with matrices

#### 1.3.1 Using technology (spreadsheet, GeoGebra) to operate with matrices
`[Block: Algebra (1st term) > Computational thinking with matrices/systems]`
Entering matrices in a spreadsheet. Matrix multiplication (MMULT), transposition (TRANSPOSE) and inverse (MINVERSE) functions. Automatic verification of results.

---

## Chapter 2. Determinants {#cap2}

### 2.1 Determinants of order 2 and order 3

#### 2.1.1 Determinant of a 2×2 matrix: definition and calculation
`[Block: Numbers and Operations > Determinants: Sarrus' rule]`
Formula $\det A = a_{11}a_{22} - a_{12}a_{21}$. Geometric interpretation (area of the parallelogram). Applications: checking linear independence.

#### 2.1.2 Determinant of a 3×3 matrix: Sarrus' rule
`[Block: Numbers and Operations > Determinants: Sarrus' rule]`
Sarrus' rule: diagonal expansion. Systematic step-by-step calculation. Examples with coefficient matrices from economic systems.

#### 2.1.3 Cofactor expansion: any order
`[Block: Numbers and Operations > Determinants: Sarrus' rule]`
Minor $M_{ij}$. Cofactor $A_{ij} = (-1)^{i+j} M_{ij}$. Expansion along any row or column. Strategy: choosing the most convenient row or column.

### 2.2 Properties of determinants

#### 2.2.1 Elementary properties: zero row, identical rows, row swap, common factor
`[Block: Numbers and Operations > Determinants: Sarrus' rule; Block: Algebra > Sets of matrices, determinants, inverse matrix]`
The fundamental properties of determinants. Strategic use to simplify calculations. Consequences for the invertibility of the matrix.

#### 2.2.2 Multiplicative property: det(AB) = det(A)·det(B)
`[Block: Algebra (1st term) > Sets of matrices, determinants, inverse matrix]`
Intuitive proof. Consequences: $\det(A^k) = [\det(A)]^k$, $\det(A^{-1}) = 1/\det(A)$. Applications in verifying calculations.

### 2.3 Inverse matrix via determinants

#### 2.3.1 Concept of the inverse matrix: existence condition and uniqueness
`[Block: Numbers and Operations > Inverse of a square matrix via determinants]`
Definition: $A \cdot A^{-1} = A^{-1} \cdot A = I$. Necessary and sufficient condition: $\det(A) \neq 0$. Regular (invertible) vs. singular matrix.

#### 2.3.2 Computing the inverse matrix using the adjugate matrix
`[Block: Numbers and Operations > Inverse of a square matrix via determinants]`
Cofactor matrix. Adjugate matrix $\text{adj}(A)$. Formula $A^{-1} = \frac{1}{\det A} \cdot \text{adj}(A)^T$. Complete calculation for 2×2 and 3×3 matrices.

#### 2.3.3 Verifying the inverse and properties
`[Block: Algebra (1st term) > Sets of matrices, determinants, inverse matrix]`
Check: $A \cdot A^{-1} = I$. Properties: $(AB)^{-1} = B^{-1}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$. Calculation with technological tools.

---

## Chapter 3. Systems of Linear Equations {#cap3}

### 3.1 Matrix representation and rank

#### 3.1.1 Linear system in matrix form: $Ax = b$ and augmented matrix
`[Block: Algebra (1st term) > Matrices for systems of linear equations; Block: Algebra > Systems of equations: modelling]`
Matrix form of a system. Coefficient matrix $A$, unknown vector $x$, constant vector $b$. Augmented matrix $(A|b)$.

#### 3.1.2 Rank of a matrix: definition via determinants
`[Block: Algebra (1st term) > Rank of a matrix with parameters (determinants, order ≤3)]`
Definition of rank as the order of the largest non-zero minor. Computing rank for matrices of order ≤ 3 using determinants. Relationship to linear independence of rows/columns.

#### 3.1.3 Rank of a matrix with parameters: case analysis
`[Block: Algebra (1st term) > Rank of a matrix with parameters (determinants, order ≤3)]`
Computing rank as a function of a parameter $\lambda$. Values that annul determinants. Case table. Applications: models with a free parameter (economic policy, planning).

### 3.2 Rouché-Frobenius theorem

#### 3.2.1 Statement of the Rouché-Frobenius theorem
`[Block: Algebra (1st term) > Rouché-Frobenius theorem with parameter]`
Complete statement: the system is consistent if and only if $\text{rank}(A) = \text{rank}(A|b)$. Classification: unique solution (rank = number of unknowns), infinite solutions (rank < unknowns), no solution (ranks differ).

#### 3.2.2 Discussing systems with a parameter using Rouché-Frobenius
`[Block: Algebra (1st term) > Rouché-Frobenius theorem with parameter]`
Complete methodology: compute $\det(A)$, analyse cases, compute $\text{rank}(A|b)$ for each case, classify. Examples with parameter $\lambda$ in 3×3 matrices. Applications: modelling economic equilibria under parametric uncertainty.

### 3.3 Solution methods

#### 3.3.1 Gaussian elimination: row-reducing the augmented matrix
`[Block: Algebra (1st term) > Matrices for systems of linear equations]`
Elementary row operations. Reduction to echelon form. Back substitution. Applications: flow distribution in input-output models.

#### 3.3.2 Cramer's rule for 2×2 and 3×3 systems
`[Block: Algebra (1st term) > Cramer's rule (up to 3×3)]`
Statement of Cramer's rule. Formula $x_i = \det(A_i)/\det(A)$. Building matrices $A_i$. Limitations (only for unique-solution systems, computationally expensive for higher orders). Practical examples.

#### 3.3.3 Solving via the inverse matrix: $x = A^{-1}b$
`[Block: Algebra (1st term) > Matrix equations]`
Condition: $\det(A) \neq 0$. Calculation process. Advantage for multiple systems with the same coefficient matrix. Applications: solving linear economic models.

#### 3.3.4 Matrix equations: solving $AX = B$, $XA = B$, $AXB = C$
`[Block: Algebra (1st term) > Matrix equations]`
Left- and right-multiplication by the inverse. Importance of order (non-commutativity). Exercises to determine unknown matrices.

---

## Chapter 4. Linear Programming {#cap4}

### 4.1 Modelling linear problems

#### 4.1.1 Decision variables, objective function and constraints
`[Block: Algebra (1st term) > Linear programming: modelling, feasible region, vertices, optimal solution]`
Identifying decision variables in a social science problem. Objective function (maximizing profit / minimizing cost). Formulating constraints as linear inequalities. Non-negativity constraints.

#### 4.1.2 Modelling examples in Social Sciences contexts
`[Block: Algebra (1st term) > Linear programming: modelling]`
Production problems, budget allocation, advertising campaign planning, distribution of public resources. Translating verbal statements into mathematical models.

### 4.2 Graphical solution

#### 4.2.1 Representing constraints: half-planes and feasible region
`[Block: Algebra (1st term) > Linear programming: modelling, feasible region, vertices, optimal solution]`
Graphical representation of each inequality. Intersection of half-planes: convex feasible region polygon. Bounded and unbounded feasible region. Empty feasible region.

#### 4.2.2 Calculating the vertices of the feasible region
`[Block: Algebra (1st term) > Linear programming: modelling, feasible region, vertices, optimal solution]`
Intersection of pairs of boundary lines. Algebraic resolution. Verifying that the vertex belongs to the feasible region.

#### 4.2.3 Corner-point theorem: statement and intuitive justification
`[Block: Algebra (1st term) > Linear programming: modelling, feasible region, vertices, optimal solution]`
Statement: the optimum of a linear function over a convex feasible region is attained at a vertex. Justification via level lines (iso-cost / iso-profit lines).

#### 4.2.4 Determining the optimal solution: evaluating the objective function at vertices
`[Block: Algebra (1st term) > Linear programming: modelling, feasible region, vertices, optimal solution]`
Evaluating the objective function at all vertices. Selecting the maximum or minimum. Special cases: unbounded solution (unbounded region) and non-unique solution (objective function parallel to an edge).

#### 4.2.5 Elementary sensitivity analysis: varying the coefficients
`[Block: Algebra (1st term) > Linear programming: modelling]`
Effect of changes in the objective function coefficients or right-hand side values. Economic interpretation: shadow price, bottlenecks.

---

## Chapter 5. Limits, Continuity and Differentiability {#cap5}

### 5.1 Limits: review and deepening

#### 5.1.1 Limit at a point: calculation and one-sided limits (review from CCSS I)
`[Block: Measurement and Geometry (Change) > Limit at a point: indeterminate forms (0/0, k/0, ∞–∞, 1∞)]`
Review of the concept of a limit. One-sided limits and existence of the two-sided limit. Piecewise functions and absolute value functions.

#### 5.1.2 Indeterminate forms in finite limits: 0/0, k/0, ∞–∞, 1^∞
`[Block: Measurement and Geometry (Change) > Limit at a point: indeterminate forms (0/0, k/0, ∞–∞, 1∞)]`
Resolving 0/0 by factoring and simplification. k/0: infinite limits. ∞–∞: rationalization. $1^\infty$: exponential form and the number $e$.

#### 5.1.3 Limits at infinity: hierarchy of infinities and asymptotes
`[Block: Measurement and Geometry (Change) > Limit at infinity, asymptotes (rational and piecewise)]`
Asymptotic behaviour of polynomials, rational, exponential and logarithmic functions. Horizontal, vertical and oblique asymptotes of rational and piecewise functions. Complete calculation.

#### 5.1.4 L'Hôpital's rule: statement, conditions and application
`[Block: Measurement and Geometry (Change) > Derivatives: interpretation, computing limits, L'Hôpital]`
Conditions for application: form 0/0 or ∞/∞. Theorem statement. Iterated application when the indeterminate form persists. Forms reducible to 0/0 or ∞/∞ (0·∞, ∞–∞, 0^0, ∞^0, 1^∞). Examples in analysing economic growth models.

### 5.2 Continuity

#### 5.2.1 Definition of continuity: review, verification and types of discontinuities
`[Block: Measurement and Geometry (Change) > Continuity, discontinuities]`
Continuity conditions. Types: removable, finite jump, infinite jump. Graphical representation. Examples with piecewise economic functions.

#### 5.2.2 Continuity of piecewise functions: determining parameters
`[Block: Measurement and Geometry (Change) > Continuity, discontinuities]`
Process for studying continuity at breakpoints. Determining constants to ensure continuity. Examples: cost functions, progressive income tax brackets.

#### 5.2.3 Theorems for continuous functions: Bolzano, Rolle and Mean Value
`[Block: Measurement and Geometry (Change) > Theorems of Bolzano, Rolle, Mean Value]`
Statement and hypotheses of each theorem. Bolzano's IVT: existence of roots. Rolle's theorem: conditions for $f'(c) = 0$. Lagrange's Mean Value Theorem: $f'(c) = [f(b)-f(a)]/(b-a)$. Applications in economics: existence of equilibrium points, average rate of change.

### 5.3 Differentiability

#### 5.3.1 Definition of the derivative: review of the difference quotient and instantaneous rate
`[Block: Measurement and Geometry (Change) > Derivatives: interpretation, computing limits, L'Hôpital]`
Review of the limit definition. Interpretation as the slope of the tangent and instantaneous rate of change in economic models.

#### 5.3.2 Differentiability: one-sided derivatives and the differentiability condition
`[Block: Measurement and Geometry (Change) > Differentiability, relationship between differentiability and continuity]`
Right-hand and left-hand derivatives. Condition: equal one-sided derivatives. Study at corner points (piecewise functions, absolute value). Detailed examples.

#### 5.3.3 Differentiability and continuity: implication and non-reciprocity
`[Block: Measurement and Geometry (Change) > Differentiability, relationship between differentiability and continuity]`
Differentiability $\Rightarrow$ continuity. Counterexamples of continuity without differentiability. Absolute value function at $x = 0$.

---

## Chapter 6. Derivatives and Applications {#cap6}

### 6.1 Differentiation rules

#### 6.1.1 Derivatives of elementary functions: complete review table
`[Block: Measurement and Geometry (Change) > Differentiation of functions (all rules + chain rule)]`
Comprehensive table: powers, exponential ($e^x$, $a^x$), logarithmic ($\ln x$, $\log_a x$), basic trigonometric (introduction). Direct application.

#### 6.1.2 Algebraic rules: sum, difference, product and quotient rules
`[Block: Measurement and Geometry (Change) > Differentiation of functions (all rules + chain rule)]`
All rules with brief proofs. Intensive practice with complex functions. Applications: total cost, revenue, profit functions and their marginals.

#### 6.1.3 Chain rule: differentiating composite functions
`[Block: Measurement and Geometry (Change) > Differentiation of functions (all rules + chain rule)]`
$(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$. Common cases: $e^{g(x)}$, $\ln(g(x))$, $[g(x)]^n$, $a^{g(x)}$, $\log_a(g(x))$. Multiple chains.

#### 6.1.4 Higher-order derivatives: second derivative and concavity
`[Block: Measurement and Geometry (Change) > Extrema, inflection points, growth/decay, concavity/convexity]`
Definition of $f''$, $f'''$, etc. Interpretation of $f''$: concave up ($f'' > 0$) and concave down ($f'' < 0$). Relationship to the rate of change of marginal quantities in economics.

### 6.2 Tangent and normal lines

#### 6.2.1 Equation of the tangent line at a point
`[Block: Measurement and Geometry (Change) > Tangent line, computing coefficients]`
$y - f(x_0) = f'(x_0)(x - x_0)$. Computing $f'(x_0)$ and building the equation. Interpretation as a local linear approximation.

#### 6.2.2 Equation of the normal line and computing its coefficients
`[Block: Measurement and Geometry (Change) > Tangent line, computing coefficients]`
Slope of the normal: $-1/f'(x_0)$. Normal line equation. Applications: analysis of level curves in economics.

#### 6.2.3 Finding points on a curve with a given tangent
`[Block: Measurement and Geometry (Change) > Tangent line, computing coefficients]`
Finding $x_0$ such that $f'(x_0) = m$ (given slope) or such that the tangent passes through an external point. Solving the resulting equation.

### 6.3 Analysing functions with derivatives

#### 6.3.1 Monotonicity: increasing and decreasing intervals via $f'$
`[Block: Measurement and Geometry (Change) > Extrema, inflection points, growth/decay, concavity/convexity]`
Criterion: $f'(x) > 0 \Rightarrow$ increasing; $f'(x) < 0 \Rightarrow$ decreasing. Sign table of $f'$. Interpretation in economic models: growth and recession phases.

#### 6.3.2 Relative extrema: first derivative test (sign change)
`[Block: Measurement and Geometry (Change) > Extrema, inflection points, growth/decay, concavity/convexity]`
Critical points ($f' = 0$, $f'$ undefined). Classification by the sign change of $f'$: local maximum ($+ \to -$), local minimum ($- \to +$), neither.

#### 6.3.3 Relative extrema: second derivative test
`[Block: Measurement and Geometry (Change) > Extrema, inflection points, growth/decay, concavity/convexity]`
$f''(x_0) < 0$: maximum; $f''(x_0) > 0$: minimum; $f''(x_0) = 0$: inconclusive. Advantages and limitations. Applications: profit function.

#### 6.3.4 Concavity, convexity and inflection points
`[Block: Measurement and Geometry (Change) > Extrema, inflection points, growth/decay, concavity/convexity]`
Concave up ($f'' > 0$) and concave down ($f'' < 0$). Inflection point: change of concavity where $f'' = 0$ (with verification). Applications: inflection point on the Laffer curve, analysis of diminishing returns.

### 6.4 Optimization

#### 6.4.1 Unconstrained optimization: absolute maxima and minima
`[Block: Measurement and Geometry (Change) > Optimization]`
Absolute extrema on $\mathbb{R}$: only relative extrema + behaviour at $\pm\infty$. Absolute extrema on $[a, b]$: interior relative extrema + endpoint values.

#### 6.4.2 Modelling and solving optimization problems in Social Sciences
`[Block: Measurement and Geometry (Change) > Optimization]`
Method: define the variable, express the quantity to optimize as a function of one variable, differentiate and set to zero, verify with $f''$ or sign table. Applications: economic profit maximization, production cost minimization, tax revenue maximization (Laffer), optimal price for a good.

#### 6.4.3 Price elasticity of demand: interpretation using derivatives
`[Block: Measurement and Geometry (Change) > Derivatives: interpretation]`
Definition of price elasticity of demand $\varepsilon = (dQ/dp) \cdot (p/Q)$. Elastic, inelastic and unit-elastic demand. Relationship to marginal revenue. Advanced application of derivatives in economic analysis.

---

## Chapter 7. Curve Sketching and Function Analysis {#cap7}

### 7.1 Complete analytical study of functions

#### 7.1.1 Domain: polynomial, rational, irrational, exponential, logarithmic and piecewise functions
`[Block: Algebra (1st term) > Representation and study of functions (polynomial, rational, exponential, logarithmic, piecewise)]`
Systematic method for each function type. Domain of piecewise functions. Interval notation.

#### 7.1.2 Symmetry: even, odd and asymmetric functions
`[Block: Algebra (1st term) > Representation and study of functions]`
Algebraic verification: $f(-x) = f(x)$ (even), $f(-x) = -f(x)$ (odd). Graphical implications.

#### 7.1.3 Intercepts with the axes
`[Block: Algebra (1st term) > Representation and study of functions]`
y-intercept: $f(0)$. x-intercepts: roots of $f(x) = 0$. Solving the associated equations.

#### 7.1.4 Asymptotes: vertical, horizontal and oblique
`[Block: Measurement and Geometry (Change) > Limit at infinity, asymptotes (rational and piecewise)]`
Systematic calculation of all types of asymptotes. Rational and piecewise functions. Incorporating into the function diagram.

#### 7.1.5 Monotonicity and relative extrema via the first derivative
`[Block: Algebra (1st term) > Representation and study of functions; Measurement and Geometry (Change) > Extrema, growth/decay]`
Sign table of $f'$. Critical points. Classifying extrema. Increasing and decreasing intervals.

#### 7.1.6 Concavity, convexity and inflection points via the second derivative
`[Block: Measurement and Geometry (Change) > Extrema, inflection points, concavity/convexity]`
Sign table of $f''$. Inflection points. Concave up and concave down intervals.

#### 7.1.7 Graphical representation: synthesis and final sketch
`[Block: Algebra (1st term) > Representation and study of functions]`
Integrating all elements of the study. Constructing the sketch with appropriate scale. Consistency between the analytical analysis and the resulting graph.

### 7.2 Types of functions — complete study

#### 7.2.1 Polynomial functions of degree 3 and above: complete analytical study
`[Block: Algebra (1st term) > Representation and study of functions (polynomial)]`
Domain $\mathbb{R}$, no asymptotes. Complete analysis with derivatives. Applications: cubic profit curves, total cost functions.

#### 7.2.2 Rational functions: complete analytical study
`[Block: Algebra (1st term) > Representation and study of functions (rational)]`
Domain, intercepts, vertical and horizontal/oblique asymptotes, monotonicity and extrema, concavity. Examples: average productivity, average cost.

#### 7.2.3 Exponential and logarithmic functions: complete analytical study
`[Block: Algebra (1st term) > Representation and study of functions (exponential, logarithmic)]`
Study of $f(x) = e^{g(x)}$ and $f(x) = \ln(g(x))$ with polynomial $g$. Horizontal asymptote. Applications: economic growth models.

#### 7.2.4 Piecewise functions: complete analytical study (continuity, differentiability, representation)
`[Block: Algebra (1st term) > Representation and study of functions (piecewise)]`
Analysis on each piece. Continuity and differentiability at breakpoints. Global representation. Applications: cost functions with economies of scale, progressive tax brackets.

---

## Chapter 8. Integrals {#cap8}

### 8.1 Antiderivatives and indefinite integration

#### 8.1.1 Concept of an antiderivative: definition and non-uniqueness
`[Block: Measurement and Geometry (Change) > Simple and composite immediate antiderivatives, Barrow's rule]`
Definition: $F$ is an antiderivative of $f$ if $F' = f$. Family of antiderivatives $F(x) + C$. Uniqueness up to the constant of integration. Meaning in social science contexts: total cost function from marginal cost.

#### 8.1.2 Table of basic immediate antiderivatives
`[Block: Measurement and Geometry (Change) > Simple and composite immediate antiderivatives]`
Complete table: powers $x^n$ ($n \neq -1$), $1/x$, $e^x$, $a^x$, $\ln|x|$, basic trigonometric functions. Direct application.

#### 8.1.3 Composite immediate antiderivatives: reverse chain rule
`[Block: Measurement and Geometry (Change) > Simple and composite immediate antiderivatives]`
Integration of $f(ax+b)$: correction by the factor $1/a$. Cases: $[g(x)]^n g'(x)$, $e^{g(x)} g'(x)$, $g'(x)/g(x)$. Practical examples with composite functions.

#### 8.1.4 Integration by parts: $\int u\, dv = uv - \int v\, du$ (introduction)
`[Block: Measurement and Geometry (Change) > Simple and composite immediate antiderivatives]`
Integration by parts formula. Choosing $u$ and $dv$ (LIATE rule). Application to $\int x e^x dx$, $\int x \ln x\, dx$, etc. Relevant cases in social sciences.

### 8.2 The definite integral

#### 8.2.1 Definite integral as a limit of sums: Riemann sums (intuitive introduction)
`[Block: Measurement and Geometry (Change) > Definite integral as area under the curve]`
Motivation: area under a curve as a sum of rectangles. Partition of the interval. Riemann sum. Passing to the limit. Applications: area between supply and demand curves (consumer/producer surplus).

#### 8.2.2 Definite integral as area under the curve: geometric interpretation
`[Block: Measurement and Geometry (Change) > Definite integral as area under the curve]`
$\int_a^b f(x)\, dx$ as signed area. Positive area (positive function) and negative area (negative function). Area between two curves. Applications: consumer and producer surplus.

#### 8.2.3 Barrow's rule: the Fundamental Theorem of Calculus
`[Block: Measurement and Geometry (Change) > Simple and composite immediate antiderivatives, Barrow's rule]`
Statement of the Fundamental Theorem of Calculus. Barrow's rule: $\int_a^b f(x)\, dx = F(b) - F(a)$. Condition: $f$ continuous on $[a, b]$. Calculation process.

#### 8.2.4 Properties of the definite integral
`[Block: Measurement and Geometry (Change) > Definite integral as area under the curve]`
Linearity. Additivity with respect to the interval. Sign change when reversing limits. Zero when $a = b$. Comparing integrals. Applications to social science problems.

### 8.3 Applications of the definite integral

#### 8.3.1 Calculating areas under a curve (positive function on $[a,b]$)
`[Block: Measurement and Geometry (Change) > Definite integral as area under the curve]`
Systematic method: find roots, integrate with the correct sign on each sub-interval. Examples with polynomial and rational functions.

#### 8.3.2 Area between two curves: intersection, calculation and applications
`[Block: Measurement and Geometry (Change) > Definite integral as area under the curve]`
$A = \int_a^b [f(x) - g(x)]\, dx$ with $f \geq g$ on $[a,b]$. Locating intersection points. Applications: consumer surplus (area between demand curve and market price) and producer surplus.

#### 8.3.3 Consumer and producer surplus: economic application
`[Block: Measurement and Geometry (Change) > Definite integral as area under the curve]`
Economic definition of consumer and producer surplus. Supply and demand model. Calculating each surplus using definite integrals. Interpreting the area as welfare.

---

## Chapter 9. Probability {#cap9}

### 9.1 Foundations of probability

#### 9.1.1 Review of probability interpretations: classical, frequentist and subjective
`[Block: Measurement and Geometry (Change) > Probability: subjective, classical, frequentist interpretations]`
Review of the three perspectives. Applications: frequentist probability in market research, classical in lotteries, subjective in electoral predictions (Bayesian models).

#### 9.1.2 Review of algebra of events, Laplace's rule and Kolmogorov's axioms
`[Block: Statistics (2nd term) > Conditional probability and independence]`
Consolidation of the foundations from CCSS I. Checking axiomatic coherence. Derived properties.

### 9.2 Conditional probability and independence

#### 9.2.1 Conditional probability: definition, calculation and updating
`[Block: Statistics (2nd term) > Conditional probability and independence]`
$P(A|B) = P(A \cap B)/P(B)$. Reducing the sample space. Updating probabilities with information. Contingency tables for computing conditional probabilities.

#### 9.2.2 Contingency tables: probabilistic reading and interpretation
`[Block: Statistics (2nd term) > Tree diagrams, contingency tables]`
Building and interpreting two-way tables. Marginal, joint and conditional probabilities from the table. Applications: opinion polls, health surveys.

#### 9.2.3 Statistical independence: definition, criterion and verification
`[Block: Statistics (2nd term) > Conditional probability and independence]`
Criterion: $P(A|B) = P(A)$ or equivalently $P(A \cap B) = P(A) \cdot P(B)$. Verification with contingency tables. Importance in survey and experiment design.

#### 9.2.4 Tree diagrams for compound experiments
`[Block: Statistics (2nd term) > Tree diagrams, contingency tables]`
Building two- and three-stage trees. Multiplication rule along branches. Summing probabilities of favourable events (tree paths). Applications: sampling with and without replacement.

### 9.3 Total probability and Bayes' theorem

#### 9.3.1 Partition of the sample space and complete system of events
`[Block: Statistics (2nd term) > Total probability and Bayes]`
Definition of a partition $\{H_1, \ldots, H_k\}$. Conditions of exhaustiveness and mutual exclusivity. Examples: population segments.

#### 9.3.2 Law of total probability: formula and applications
`[Block: Statistics (2nd term) > Total probability and Bayes]`
$P(A) = \sum_i P(A|H_i) \cdot P(H_i)$. Calculation process with tree or table. Applications: overall unemployment rate from sectoral rates, stratified credit-risk analysis.

#### 9.3.3 Bayes' theorem: inverting conditional probability
`[Block: Statistics (2nd term) > Total probability and Bayes]`
$P(H_i|A) = \frac{P(A|H_i) \cdot P(H_i)}{P(A)}$. Prior and posterior probabilities. Bayesian interpretation. Applications: epidemiological diagnosis, reliability of stratified polls, analysis of electoral surveys.

---

## Chapter 10. Probability Distributions {#cap10}

### 10.1 Random variables: review and deepening

#### 10.1.1 Discrete random variables: mass function, cumulative distribution, expected value and variance
`[Block: Statistics (2nd term) > Binomial and normal distributions]`
Review of concepts from CCSS I. Computing $E(X)$ and $Var(X)$. Properties of expected value and variance.

#### 10.1.2 Continuous random variables: density function and cumulative distribution
`[Block: Statistics (2nd term) > Binomial and normal distributions]`
Concept of density function $f(x) \geq 0$ with $\int_{-\infty}^{+\infty} f(x)\, dx = 1$. Probability as area. Distribution function $F(x) = P(X \leq x)$.

### 10.2 Binomial distribution

#### 10.2.1 Binomial distribution $B(n, p)$: conditions, mass function and parameters
`[Block: Statistics (2nd term) > Binomial and normal distributions]`
Bernoulli trial conditions. Mass function $P(X = k) = \binom{n}{k}p^k(1-p)^{n-k}$. Parameters $n$ and $p$. Applications: modelling sample proportions (voting intention, product acceptance).

#### 10.2.2 Expected value and variance: $E(X) = np$, $Var(X) = np(1-p)$
`[Block: Statistics (2nd term) > Binomial and normal distributions]`
Formulas. Interpretation. Computing exact and cumulative probabilities with calculator or table. Exercises in social science contexts.

#### 10.2.3 Computing cumulative probabilities with the binomial
`[Block: Statistics (2nd term) > Binomial and normal distributions]`
$P(X \leq k)$, $P(X \geq k)$, $P(X = k)$ with technological tools. Using binomial tables. Exercises: probability that in an electoral sample at least $k$ people support a candidate.

### 10.3 Normal distribution

#### 10.3.1 Normal distribution $N(\mu, \sigma)$: parameters, Gaussian bell curve and properties
`[Block: Statistics (2nd term) > Binomial and normal distributions]`
Density function (analytical form). Bell curve: symmetric around $\mu$, inflection points at $\mu \pm \sigma$. Empirical rule 68-95-99.7. Applications: income distribution, sampling errors.

#### 10.3.2 Standardization: transforming to $N(0,1)$ and using tables
`[Block: Statistics (2nd term) > Binomial and normal distributions]`
$Z = (X - \mu)/\sigma$. Interpreting $Z$. Using the table $\Phi(z)$. Computing probabilities: $P(X < a)$, $P(X > a)$, $P(a < X < b)$. Inverse calculation: given $p$, find $x$.

#### 10.3.3 Computing probabilities with the normal distribution: complete exercises
`[Block: Statistics (2nd term) > Binomial and normal distributions]`
Exercise series in social science contexts: wage distribution, exam scores, waiting times in public services. Using a scientific calculator.

### 10.4 Normal approximation to the binomial

#### 10.4.1 Conditions for the approximation: $np \geq 5$ and $n(1-p) \geq 5$
`[Block: Statistics (2nd term) > Normal approximation to the binomial]`
Justification via the Central Limit Theorem (intuitive). Sufficient conditions. Parameters of the approximating normal: $\mu = np$, $\sigma = \sqrt{np(1-p)}$.

#### 10.4.2 Continuity correction in the approximation
`[Block: Statistics (2nd term) > Normal approximation to the binomial]`
Justification of the $\pm 0.5$ correction. Application when computing $P(X = k)$, $P(X \leq k)$, $P(X \geq k)$. Comparison with the exact binomial result.

#### 10.4.3 Problems using the normal approximation in electoral and social contexts
`[Block: Statistics (2nd term) > Normal approximation to the binomial]`
Complete exercises: in a sample of 1000 voters where 42% support party A, what is the probability that between 400 and 440 supporters appear in the sample? Other social contexts.

---

## Chapter 11. Statistical Inference {#cap11}

### 11.1 Fundamentals of inference

#### 11.1.1 Population and sample: population parameters and sample statistics
`[Block: Statistics (2nd term) > Inference: population and sample, population/sample parameters]`
Distinction between parameters ($\mu, \sigma, p$) and their estimators ($\bar{x}, s, \hat{p}$). Importance of inference when the entire population cannot be studied. Applications: electoral polls, market research.

#### 11.1.2 Sampling techniques: simple random, systematic, stratified and cluster
`[Block: Statistics (2nd term) > Sampling techniques, representativeness]`
Detailed description of each method. Criteria for choosing a sampling type. Representativeness and potential biases. Technical survey report: what it must include.

#### 11.1.3 Technical survey report: components and critical reading
`[Block: Statistics (2nd term) > Technical survey report]`
Components: universe, sample size, sampling method, margin of error, confidence level, date and organization. Reading and critically interpreting reports from real surveys (CIS, Metroscopia, etc.).

### 11.2 Sampling distributions

#### 11.2.1 Sampling distribution of the sample mean $\bar{X}$: Central Limit Theorem
`[Block: Statistics (2nd term) > Sampling distribution of mean and proportion]`
CLT statement: if $n$ is large enough, $\bar{X} \sim N(\mu, \sigma/\sqrt{n})$ approximately, regardless of the population distribution. Standard error $\sigma/\sqrt{n}$. Implications for estimation.

#### 11.2.2 Sampling distribution of the sample proportion $\hat{P}$
`[Block: Statistics (2nd term) > Sampling distribution of mean and proportion]`
If $X \sim B(n, p)$ with large $n$, $\hat{P} = X/n \sim N(p, \sqrt{p(1-p)/n})$ approximately. Application conditions. Interpreting the standard error of the proportion.

### 11.3 Point estimation

#### 11.3.1 Concept of an estimator and desirable properties: unbiasedness and efficiency
`[Block: Statistics (2nd term) > Point and interval estimation]`
Definition of a point estimator. Unbiasedness: $E(\hat{\theta}) = \theta$. Efficiency: smallest variance among unbiased estimators. $\bar{x}$ as an unbiased estimator of $\mu$. $\hat{p}$ as an unbiased estimator of $p$.

#### 11.3.2 Point estimation of the mean and proportion
`[Block: Statistics (2nd term) > Point and interval estimation]`
Computing $\bar{x}$ and $\hat{p}$ from sample data. Interpretation. Limitation of point estimation: it does not quantify uncertainty.

### 11.4 Confidence interval estimation

#### 11.4.1 Concept of a confidence interval: confidence level and significance level
`[Block: Statistics (2nd term) > Confidence intervals (normal distribution): construction, analysis]`
Definition: the CI is random; the parameter is fixed. Frequentist interpretation: $(1-\alpha) \cdot 100\%$ of intervals built from repeated samples will contain the parameter. Common confidence levels: 90%, 95%, 99%.

#### 11.4.2 Critical value $z_{\alpha/2}$: reading it from the standard normal table
`[Block: Statistics (2nd term) > Confidence intervals (normal distribution): construction, analysis]`
Definition of $z_{\alpha/2}$ as a quantile of the standard normal. Common values: $z_{0.025} = 1.96$ (95%), $z_{0.05} = 1.645$ (90%), $z_{0.005} = 2.576$ (99%). Reading from the table.

#### 11.4.3 Confidence interval for the mean with known $\sigma$
`[Block: Statistics (2nd term) > Confidence interval for the mean (known standard deviation)]`
$CI_{1-\alpha}(\mu) = \left(\bar{x} - z_{\alpha/2} \dfrac{\sigma}{\sqrt{n}},\; \bar{x} + z_{\alpha/2} \dfrac{\sigma}{\sqrt{n}}\right)$. Condition: $\sigma$ known or large $n$. Step-by-step construction. Interpretation. Applications: estimating the mean income of a population.

#### 11.4.4 Confidence interval for a population proportion
`[Block: Statistics (2nd term) > Confidence intervals (normal distribution): construction, analysis]`
$CI_{1-\alpha}(p) = \left(\hat{p} - z_{\alpha/2} \sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}},\; \hat{p} + z_{\alpha/2} \sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}\right)$. Application conditions ($n$ large, $n\hat{p} \geq 5$). Applications: estimating voting intention, proportion of satisfied users.

#### 11.4.5 Margin of error of an estimate
`[Block: Statistics (2nd term) > Relationship between confidence, error and sample size]`
Definition: $E = z_{\alpha/2} \cdot \sigma/\sqrt{n}$ (mean) or $E = z_{\alpha/2} \cdot \sqrt{\hat{p}(1-\hat{p})/n}$ (proportion). Reading the margin of error in survey reports. Relationship between margin of error, confidence level and sample size.

### 11.5 Sample size determination

#### 11.5.1 Minimum sample size for a mean with a maximum admissible error
`[Block: Statistics (2nd term) > Minimum sample size]`
Solving for $n$ in the margin-of-error formula: $n \geq \left(\dfrac{z_{\alpha/2} \cdot \sigma}{E}\right)^2$. Always round up. Applications: determining sample size in social science studies.

#### 11.5.2 Minimum sample size for a proportion with a maximum admissible error
`[Block: Statistics (2nd term) > Minimum sample size]`
$n \geq \left(\dfrac{z_{\alpha/2}}{E}\right)^2 p(1-p)$. Worst case $p = 0.5$: $n \geq \left(\dfrac{z_{\alpha/2}}{2E}\right)^2$. Applications: electoral polls, citizen satisfaction studies.

#### 11.5.3 Confidence-error-sample size relationship: analysis and interpretation
`[Block: Statistics (2nd term) > Relationship between confidence, error and sample size]`
Effects of increasing confidence level (increases $n$ or increases error). Effect of reducing margin of error (increases $n$ or decreases confidence level). Cost-precision trade-off in survey design. Critical reading of real technical reports.

### 11.6 Linear regression (in the inference context)

#### 11.6.1 Review of linear regression: regression lines and the coefficient of determination
`[Block: Statistics (2nd term) > Linear regression]`
Consolidation of content from CCSS I. Regression lines of $Y/X$ and $X/Y$. Coefficient of determination $R^2$ and its interpretation as goodness of fit.

#### 11.6.2 Prediction and interpolation from the regression model
`[Block: Statistics (2nd term) > Linear regression]`
Using the regression line to predict values. Extrapolation and its risks. Interpreting the regression coefficients in substantive social science terms. Applications: predicting consumption from income, estimating electoral participation.

---

*End of index — Mathematics Applied to the Social Sciences II (Year 2 of Bachillerato)*
*Comunidad de Madrid — Decreto 64/2022 (LOMLOE)*
