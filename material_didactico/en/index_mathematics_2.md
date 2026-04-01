# Mathematics II — Table of Contents

**Year:** 2nd Year Upper Secondary (Bachillerato) — Science and Technology Track  
**Region:** Comunidad de Madrid (Spain)  
**Regulatory framework:** Decreto 64/2022 (LOMLOE) / FUHEM Curriculum Plan 2025-26  
**Assessment periods:** 1st term (chapters 1–5) · 2nd term (chapters 6–9) · 3rd term (chapters 10–11)

> **Curriculum mapping note:** Every subsection (x.y.z) includes a bracketed tag showing the official "saberes básicos" block it corresponds to, using the format `[Block: Sense name > Descriptor]`. The original Spanish block names are preserved in parentheses for traceability.

---

## Chapter 1. Matrices

### 1.1 Concept and types of matrices
- 1.1.1 Definition of a matrix. Elements, order, and notation `[Block: Algebraic sense > Matrix algebra]`
- 1.1.2 Types of matrices: zero, identity, diagonal, triangular, symmetric, skew-symmetric, transpose `[Block: Algebraic sense > Matrix algebra]`
- 1.1.3 Matrix equality `[Block: Algebraic sense > Matrix algebra]`

### 1.2 Matrix operations
- 1.2.1 Matrix addition and subtraction: definition and properties `[Block: Algebraic sense > Matrix algebra]`
- 1.2.2 Scalar multiplication of a matrix `[Block: Algebraic sense > Matrix algebra]`
- 1.2.3 Matrix multiplication: definition, existence condition, and algorithm `[Block: Algebraic sense > Matrix algebra]`
- 1.2.4 Properties of matrix multiplication: associativity, distributivity, non-commutativity `[Block: Algebraic sense > Matrix algebra]`
- 1.2.5 Transpose of a product and further transpose properties `[Block: Algebraic sense > Matrix algebra]`

### 1.3 Powers of a matrix
- 1.3.1 Definition of non-negative integer powers of a square matrix `[Block: Algebraic sense > Matrix algebra]`
- 1.3.2 Computing powers via diagonalisation (intuitive introduction) `[Block: Algebraic sense > Matrix algebra]`
- 1.3.3 Matrix powers in cyclic situations: detecting the cycle and efficient computation `[Block: Algebraic sense > Matrix algebra]`

### 1.4 Algebraic structure of matrix sets
- 1.4.1 The set M_{m×n}(ℝ) as a vector space: axioms and examples `[Block: Algebraic sense > Algebraic structures]`
- 1.4.2 The set M_n(ℝ) as a ring: properties of multiplication `[Block: Algebraic sense > Algebraic structures]`

### 1.5 Inverse matrix
- 1.5.1 Definition of regular matrix and inverse matrix. Uniqueness `[Block: Algebraic sense > Matrix algebra]`
- 1.5.2 Computing the inverse by the Gauss-Jordan method `[Block: Algebraic sense > Matrix algebra]`
- 1.5.3 Computing the inverse via determinants (adjugate matrix formula) `[Block: Algebraic sense > Matrix algebra]`
- 1.5.4 Properties of the inverse: inverse of a product, transpose, and power `[Block: Algebraic sense > Matrix algebra]`

### 1.6 Applications of matrices
- 1.6.1 Representing graphs and networks with adjacency matrices `[Block: Algebraic sense > Algebraic modelling]`
- 1.6.2 Cyclic evolution models (elementary Markov chains) `[Block: Algebraic sense > Algebraic modelling]`
- 1.6.3 Computational thinking: algorithmic analysis of matrix product and inverse `[Block: Algebraic sense > Computational thinking]`

---

## Chapter 2. Determinants

### 2.1 Definition and computation of determinants
- 2.1.1 Second-order determinant: definition and rule `[Block: Algebraic sense > Matrix algebra]`
- 2.1.2 Third-order determinant: Sarrus' rule and cofactor expansion `[Block: Algebraic sense > Matrix algebra]`
- 2.1.3 Fourth-order determinant: cofactor expansion and reduction strategies `[Block: Algebraic sense > Matrix algebra]`

### 2.2 Properties of determinants
- 2.2.1 Effect of elementary row/column operations on the determinant `[Block: Algebraic sense > Matrix algebra]`
- 2.2.2 Determinants of triangular, diagonal, zero, and identity matrices `[Block: Algebraic sense > Matrix algebra]`
- 2.2.3 Determinant of a product: |AB| = |A|·|B| `[Block: Algebraic sense > Matrix algebra]`
- 2.2.4 Determinant of the transpose and of the inverse `[Block: Algebraic sense > Matrix algebra]`
- 2.2.5 Regularity criterion via the determinant `[Block: Algebraic sense > Matrix algebra]`

### 2.3 Cofactors and applications
- 2.3.1 Minors and cofactors: definition and computation `[Block: Algebraic sense > Matrix algebra]`
- 2.3.2 Adjugate (classical adjoint) matrix `[Block: Algebraic sense > Matrix algebra]`
- 2.3.3 Inverse via the formula A⁻¹ = (1/|A|)·Adj(A) `[Block: Algebraic sense > Matrix algebra]`

### 2.4 Rank of a matrix
- 2.4.1 Definition of rank: largest non-zero minor `[Block: Algebraic sense > Matrix algebra]`
- 2.4.2 Computing rank via determinants for matrices of order ≤ 4 `[Block: Algebraic sense > Matrix algebra]`
- 2.4.3 Computing rank via Gaussian elimination (elementary transformations) `[Block: Algebraic sense > Matrix algebra]`
- 2.4.4 Rank of matrices with parameters: case analysis `[Block: Algebraic sense > Matrix algebra]`
- 2.4.5 Computational thinking: algorithm for computing rank `[Block: Algebraic sense > Computational thinking]`

---

## Chapter 3. Systems of Linear Equations

### 3.1 Linear systems: fundamental concepts
- 3.1.1 Definition of a linear system. Solution, consistent, and inconsistent systems `[Block: Algebraic sense > Algebraic modelling]`
- 3.1.2 Geometric interpretation in 2D and 3D `[Block: Algebraic sense > Algebraic modelling]`
- 3.1.3 Matrix form: A·x = b `[Block: Algebraic sense > Matrix algebra]`

### 3.2 Rouché-Frobenius theorem
- 3.2.1 Statement of the theorem: consistency condition via ranks `[Block: Algebraic sense > Algebraic modelling]`
- 3.2.2 System classification: inconsistent, uniquely determined, and underdetermined `[Block: Algebraic sense > Algebraic modelling]`
- 3.2.3 Discussion of systems with one parameter: technique and cases `[Block: Algebraic sense > Algebraic modelling]`

### 3.3 Solution methods
- 3.3.1 Gaussian elimination: row operations and row echelon form `[Block: Algebraic sense > Algebraic modelling]`
- 3.3.2 Cramer's rule for systems of order ≤ 3 with a unique solution `[Block: Algebraic sense > Algebraic modelling]`
- 3.3.3 Solving via the inverse matrix: x = A⁻¹·b `[Block: Algebraic sense > Matrix algebra]`
- 3.3.4 Homogeneous systems: trivial solution and non-trivial solutions `[Block: Algebraic sense > Algebraic modelling]`

### 3.4 Matrix equations
- 3.4.1 Equations of the form AX = B, XA = B, AXB = C `[Block: Algebraic sense > Matrix algebra]`
- 3.4.2 Converting a matrix equation into a linear system `[Block: Algebraic sense > Matrix algebra]`
- 3.4.3 Solving matrix equations using the inverse and operations `[Block: Algebraic sense > Matrix algebra]`

### 3.5 Modelling with systems of equations
- 3.5.1 Formulating and solving real-context problems with 2×2 and 3×3 systems `[Block: Algebraic sense > Algebraic modelling]`
- 3.5.2 Network flow models and mass balance `[Block: Algebraic sense > Algebraic modelling]`
- 3.5.3 Computational thinking: Gaussian algorithm and parametric systems `[Block: Algebraic sense > Computational thinking]`

---

## Chapter 4. Vectors in Space

### 4.1 Vectors in ℝ³: basic concepts
- 4.1.1 Definition of a vector in space. Magnitude, direction, and sense `[Block: Spatial sense > Vectors and modelling]`
- 4.1.2 Basic operations: addition, subtraction, scalar multiplication and their properties `[Block: Spatial sense > Vectors and modelling]`
- 4.1.3 Representation of vectors in Cartesian coordinates `[Block: Spatial sense > Vectors and modelling]`

### 4.2 Linear dependence and independence
- 4.2.1 Definition of linear combination of vectors `[Block: Algebraic sense > Matrix algebra]`
- 4.2.2 Linear dependence and independence: definition and determinant criterion `[Block: Algebraic sense > Matrix algebra]`
- 4.2.3 Basis and dimension of ℝ³. Standard basis `[Block: Algebraic sense > Algebraic structures]`

### 4.3 Dot product
- 4.3.1 Analytic and geometric definition of the dot product in ℝ³ `[Block: Numerical sense > Dot product and cross product]`
- 4.3.2 Properties of the dot product: commutativity, distributivity, bilinearity `[Block: Numerical sense > Dot product and cross product]`
- 4.3.3 Magnitude of a vector and distance between points using the dot product `[Block: Numerical sense > Dot product and cross product]`
- 4.3.4 Angle between two vectors: formula and special cases (orthogonality) `[Block: Numerical sense > Dot product and cross product]`
- 4.3.5 Projection of one vector onto another `[Block: Numerical sense > Dot product and cross product]`

### 4.4 Cross product
- 4.4.1 Definition of the cross product via the formal determinant `[Block: Numerical sense > Dot product and cross product]`
- 4.4.2 Properties of the cross product: anti-commutativity, distributivity, magnitude `[Block: Numerical sense > Dot product and cross product]`
- 4.4.3 Geometric interpretation: perpendicular vector and area of the parallelogram `[Block: Numerical sense > Dot product and cross product]`
- 4.4.4 Applications: area of triangles and collinearity test `[Block: Numerical sense > Dot product and cross product]`

### 4.5 Scalar triple product
- 4.5.1 Definition of the scalar triple product of three vectors `[Block: Numerical sense > Dot product and cross product]`
- 4.5.2 Computation as a 3×3 determinant `[Block: Numerical sense > Dot product and cross product]`
- 4.5.3 Properties: sign change under cyclic permutation `[Block: Numerical sense > Dot product and cross product]`
- 4.5.4 Geometric interpretation: volume of the parallelepiped and coplanarity `[Block: Numerical sense > Dot product and cross product]`
- 4.5.5 Applications: volume of tetrahedra and coplanarity test for four points `[Block: Numerical sense > Dot product and cross product]`

---

## Chapter 5. Analytic Geometry in Space

### 5.1 Equations of a line in space
- 5.1.1 Vector equation of a line `[Block: Spatial sense > Analytic geometry in space]`
- 5.1.2 Parametric equations of a line `[Block: Spatial sense > Analytic geometry in space]`
- 5.1.3 Symmetric (continuous) equations of a line `[Block: Spatial sense > Analytic geometry in space]`
- 5.1.4 Converting between different forms of the line equation `[Block: Spatial sense > Analytic geometry in space]`

### 5.2 Equations of a plane in space
- 5.2.1 Vector equation of a plane `[Block: Spatial sense > Analytic geometry in space]`
- 5.2.2 General (implicit) equation of a plane. Normal vector `[Block: Spatial sense > Analytic geometry in space]`
- 5.2.3 Finding the equation of a plane given three points `[Block: Spatial sense > Analytic geometry in space]`
- 5.2.4 Planes parallel to coordinate axes and planes parallel to each other `[Block: Spatial sense > Analytic geometry in space]`

### 5.3 Relative positions
- 5.3.1 Relative position of two lines: intersecting, parallel, coincident, skew `[Block: Spatial sense > Analytic geometry in space]`
- 5.3.2 Relative position of line and plane: intersection, parallel, line contained in plane `[Block: Spatial sense > Analytic geometry in space]`
- 5.3.3 Relative position of two planes: intersection, parallel, coincident `[Block: Spatial sense > Analytic geometry in space]`
- 5.3.4 Relative position of three planes (connection to 3×3 systems) `[Block: Spatial sense > Analytic geometry in space]`

### 5.4 Angles between geometric elements
- 5.4.1 Angle between two lines `[Block: Spatial sense > Measurement and analytic geometry]`
- 5.4.2 Angle between a line and a plane `[Block: Spatial sense > Measurement and analytic geometry]`
- 5.4.3 Angle between two planes (dihedral angle) `[Block: Spatial sense > Measurement and analytic geometry]`

### 5.5 Distances
- 5.5.1 Distance between two points `[Block: Spatial sense > Measurement and analytic geometry]`
- 5.5.2 Distance from a point to a line `[Block: Spatial sense > Measurement and analytic geometry]`
- 5.5.3 Distance from a point to a plane: analytic formula `[Block: Spatial sense > Measurement and analytic geometry]`
- 5.5.4 Distance between two parallel lines `[Block: Spatial sense > Measurement and analytic geometry]`
- 5.5.5 Distance between two skew lines: minimum distance `[Block: Spatial sense > Measurement and analytic geometry]`
- 5.5.6 Distance between two parallel planes `[Block: Spatial sense > Measurement and analytic geometry]`

### 5.6 Symmetries and projections
- 5.6.1 Symmetric point of a point with respect to another point `[Block: Spatial sense > Symmetries in space]`
- 5.6.2 Symmetric point of a point with respect to a plane `[Block: Spatial sense > Symmetries in space]`
- 5.6.3 Symmetric point of a point with respect to a line `[Block: Spatial sense > Symmetries in space]`
- 5.6.4 Symmetric line of a line with respect to a plane `[Block: Spatial sense > Symmetries in space]`
- 5.6.5 Orthogonal projection of a point onto a plane `[Block: Spatial sense > Symmetries in space]`
- 5.6.6 Orthogonal projection of a line onto a plane `[Block: Spatial sense > Symmetries in space]`

### 5.7 Three-dimensional objects and modelling
- 5.7.1 Tetrahedron: vertices, edges, faces, and properties in coordinates `[Block: Spatial sense > Three-dimensional objects]`
- 5.7.2 Parallelepiped: definition, edges, and diagonals in coordinates `[Block: Spatial sense > Three-dimensional objects]`
- 5.7.3 Solving length, area, and volume problems in Cartesian coordinates `[Block: Measurement sense > Metric geometry]`
- 5.7.4 Representation with digital tools (GeoGebra 3D or similar) `[Block: Spatial sense > Digital tools]`

---

## Chapter 6. Limits and Continuity

### 6.1 Limit of a function at a point
- 6.1.1 Intuitive concept of limit: graphical and tabular approach `[Block: Analytical sense > Limits and continuity]`
- 6.1.2 Formal definition of limit (ε-δ, introductory level) `[Block: Analytical sense > Limits and continuity]`
- 6.1.3 One-sided limits: left-hand and right-hand limits `[Block: Analytical sense > Limits and continuity]`
- 6.1.4 Existence of the limit: condition of equal one-sided limits `[Block: Analytical sense > Limits and continuity]`
- 6.1.5 Operational properties of limits (limit algebra) `[Block: Analytical sense > Limits and continuity]`

### 6.2 Computing limits and indeterminate forms
- 6.2.1 Direct limits and substitution `[Block: Analytical sense > Limits and continuity]`
- 6.2.2 Indeterminate form 0/0: factorisation, rationalisation, and substitution `[Block: Analytical sense > Limits and continuity]`
- 6.2.3 Indeterminate form k/0 and infinite limits `[Block: Analytical sense > Limits and continuity]`
- 6.2.4 Indeterminate form ∞ − ∞: resolution techniques `[Block: Analytical sense > Limits and continuity]`
- 6.2.5 Indeterminate form 0·∞: conversion to 0/0 or ∞/∞ `[Block: Analytical sense > Limits and continuity]`
- 6.2.6 Indeterminate form 1^∞: exponential technique `[Block: Analytical sense > Limits and continuity]`

### 6.3 Limits at infinity and asymptotes
- 6.3.1 Limit of a function as x → ±∞ `[Block: Analytical sense > Limits and continuity]`
- 6.3.2 Horizontal asymptote: definition and computation `[Block: Analytical sense > Limits and continuity]`
- 6.3.3 Vertical asymptote: definition and computation `[Block: Analytical sense > Limits and continuity]`
- 6.3.4 Oblique (slant) asymptote: existence condition and computation of m and n `[Block: Analytical sense > Limits and continuity]`
- 6.3.5 Asymptotes of rational functions `[Block: Analytical sense > Limits and continuity]`
- 6.3.6 Asymptotes of piecewise-defined functions `[Block: Analytical sense > Limits and continuity]`

### 6.4 Continuity of functions
- 6.4.1 Definition of continuity at a point: the three conditions `[Block: Analytical sense > Limits and continuity]`
- 6.4.2 Types of discontinuity: removable, jump (finite), infinite (essential) `[Block: Analytical sense > Limits and continuity]`
- 6.4.3 Continuity of elementary functions and continuity on an interval `[Block: Analytical sense > Limits and continuity]`
- 6.4.4 Studying continuity of piecewise-defined functions `[Block: Analytical sense > Limits and continuity]`
- 6.4.5 Finding parameters so that a piecewise function is continuous `[Block: Analytical sense > Limits and continuity]`

### 6.5 Continuity theorems
- 6.5.1 Bolzano's theorem: statement and application to existence of roots `[Block: Analytical sense > Limits and continuity]`
- 6.5.2 Intermediate value theorem (Darboux): statement and applications `[Block: Analytical sense > Limits and continuity]`
- 6.5.3 Applying Bolzano's theorem to bound and separate roots `[Block: Analytical sense > Limits and continuity]`

---

## Chapter 7. Derivatives and Applications

### 7.1 Concept of derivative
- 7.1.1 Average and instantaneous rate of change `[Block: Analytical sense > Derivatives and applications]`
- 7.1.2 Definition of derivative as the limit of the difference quotient `[Block: Analytical sense > Derivatives and applications]`
- 7.1.3 Derivative as slope of the tangent line: geometric interpretation `[Block: Analytical sense > Derivatives and applications]`
- 7.1.4 Derivative function: definition and notation (Lagrange, Leibniz, Newton) `[Block: Analytical sense > Derivatives and applications]`
- 7.1.5 Higher-order derivatives: f'', f''' and the nth derivative `[Block: Analytical sense > Derivatives and applications]`

### 7.2 Differentiation rules
- 7.2.1 Derivatives of elementary functions: polynomials, roots, exponential, logarithmic, trigonometric `[Block: Analytical sense > Derivatives and applications]`
- 7.2.2 Linearity: derivative of a sum and of scalar multiplication `[Block: Analytical sense > Derivatives and applications]`
- 7.2.3 Product rule `[Block: Analytical sense > Derivatives and applications]`
- 7.2.4 Quotient rule `[Block: Analytical sense > Derivatives and applications]`
- 7.2.5 Chain rule (composite functions) `[Block: Analytical sense > Derivatives and applications]`
- 7.2.6 Logarithmic differentiation: technique and applications to products and powers `[Block: Analytical sense > Derivatives and applications]`

### 7.3 Differentiability
- 7.3.1 One-sided derivatives: definition and computation `[Block: Analytical sense > Derivatives and applications]`
- 7.3.2 Differentiability at a point: condition of equal one-sided derivatives `[Block: Analytical sense > Derivatives and applications]`
- 7.3.3 Relationship between differentiability and continuity (implication and counterexamples) `[Block: Analytical sense > Derivatives and applications]`
- 7.3.4 Studying differentiability of piecewise-defined functions `[Block: Analytical sense > Derivatives and applications]`
- 7.3.5 Finding parameters so that a function is differentiable `[Block: Analytical sense > Derivatives and applications]`

### 7.4 Tangent and normal lines
- 7.4.1 Equation of the tangent line to a curve at a point `[Block: Analytical sense > Derivatives and applications]`
- 7.4.2 Equation of the normal line to a curve at a point `[Block: Analytical sense > Derivatives and applications]`
- 7.4.3 Points on a curve with a horizontal tangent or a given slope `[Block: Analytical sense > Derivatives and applications]`

### 7.5 L'Hôpital's rule
- 7.5.1 Statement of L'Hôpital's rule (forms 0/0 and ∞/∞) `[Block: Analytical sense > Derivatives and applications]`
- 7.5.2 Iterated application of L'Hôpital's rule `[Block: Analytical sense > Derivatives and applications]`
- 7.5.3 Resolving 0·∞, ∞−∞, and exponential indeterminate forms via L'Hôpital `[Block: Analytical sense > Derivatives and applications]`

### 7.6 Mean value theorems
- 7.6.1 Rolle's theorem: statement, conditions, and geometric interpretation `[Block: Analytical sense > Derivatives and applications]`
- 7.6.2 Lagrange's mean value theorem: statement and applications `[Block: Analytical sense > Derivatives and applications]`
- 7.6.3 Consequences: functions with zero derivative, functions with equal derivatives `[Block: Analytical sense > Derivatives and applications]`

### 7.7 Optimisation
- 7.7.1 Relative extrema: necessary condition (zero derivative) and second derivative test `[Block: Analytical sense > Derivatives and applications]`
- 7.7.2 Extrema at domain endpoints and at non-differentiable points `[Block: Analytical sense > Derivatives and applications]`
- 7.7.3 Formulating and solving optimisation problems in real-world contexts `[Block: Analytical sense > Derivatives and applications]`
- 7.7.4 Geometric optimisation: minimum distances, extremal areas and volumes `[Block: Analytical sense > Derivatives and applications]`
- 7.7.5 Optimisation in kinematics problems (velocity, acceleration) `[Block: Analytical sense > Derivatives and applications]`

---

## Chapter 8. Curve Sketching

### 8.1 Domain and range
- 8.1.1 Finding the natural domain of elementary and composite functions `[Block: Analytical sense > Study and sketching of functions]`
- 8.1.2 Determining the range of a function `[Block: Analytical sense > Study and sketching of functions]`

### 8.2 Symmetry, periodicity, and intercepts
- 8.2.1 Even, odd, and asymmetric functions: criteria and examples `[Block: Analytical sense > Study and sketching of functions]`
- 8.2.2 Periodic functions: identification and period `[Block: Analytical sense > Study and sketching of functions]`
- 8.2.3 Axis intercepts: x-intercepts and y-intercept `[Block: Analytical sense > Study and sketching of functions]`

### 8.3 Asymptotes
- 8.3.1 Vertical asymptotes: detection and classification `[Block: Analytical sense > Study and sketching of functions]`
- 8.3.2 Horizontal asymptotes `[Block: Analytical sense > Study and sketching of functions]`
- 8.3.3 Oblique (slant) asymptotes `[Block: Analytical sense > Study and sketching of functions]`

### 8.4 Monotonicity and extrema
- 8.4.1 Intervals of increase and decrease via the sign of f' `[Block: Analytical sense > Study and sketching of functions]`
- 8.4.2 Relative extrema: local maxima and minima using first and second derivative tests `[Block: Analytical sense > Study and sketching of functions]`
- 8.4.3 Absolute extrema on a closed interval `[Block: Analytical sense > Study and sketching of functions]`

### 8.5 Curvature and inflection points
- 8.5.1 Concavity and convexity: criterion via the sign of f'' `[Block: Analytical sense > Study and sketching of functions]`
- 8.5.2 Inflection points: definition, necessary condition, and verification `[Block: Analytical sense > Study and sketching of functions]`

### 8.6 Complete graph sketching
- 8.6.1 Sketching protocol: ordering and synthesis of all elements `[Block: Analytical sense > Study and sketching of functions]`
- 8.6.2 Sketching polynomial functions `[Block: Analytical sense > Study and sketching of functions]`
- 8.6.3 Sketching rational functions `[Block: Analytical sense > Study and sketching of functions]`
- 8.6.4 Sketching exponential and logarithmic functions `[Block: Analytical sense > Study and sketching of functions]`
- 8.6.5 Sketching piecewise-defined functions `[Block: Analytical sense > Study and sketching of functions]`
- 8.6.6 Using digital tools (GeoGebra, Desmos) for verification and exploration `[Block: Analytical sense > Digital tools]`

### 8.7 Modelling with functions
- 8.7.1 Building models with complex functions from real data `[Block: Analytical sense > Functional modelling]`
- 8.7.2 Interpreting the model: domain of validity, extrema, and trends `[Block: Analytical sense > Functional modelling]`

---

## Chapter 9. Integrals

### 9.1 Antiderivatives and indefinite integrals
- 9.1.1 Concept of antiderivative: definition and uniqueness up to a constant `[Block: Measurement sense > Integral and applications]`
- 9.1.2 Indefinite integral: notation and linearity properties `[Block: Measurement sense > Integral and applications]`
- 9.1.3 Table of standard integrals: polynomials, exponentials, trigonometric, etc. `[Block: Measurement sense > Integral and applications]`
- 9.1.4 Immediate integrals of composite functions (reverse chain rule) `[Block: Measurement sense > Integral and applications]`

### 9.2 Integration techniques
- 9.2.1 Integration by substitution (change of variable) `[Block: Measurement sense > Integral and applications]`
- 9.2.2 Integration by parts: formula and the LIATE rule for choosing u and dv `[Block: Measurement sense > Integral and applications]`
- 9.2.3 Iterated and circular integration by parts `[Block: Measurement sense > Integral and applications]`
- 9.2.4 Integration of rational functions with denominator of degree ≤ 2: partial fraction decomposition `[Block: Measurement sense > Integral and applications]`
- 9.2.5 Integration of rational functions: case of real simple roots in the denominator `[Block: Measurement sense > Integral and applications]`
- 9.2.6 Integration of rational functions: case of complex conjugate roots or repeated real roots `[Block: Measurement sense > Integral and applications]`

### 9.3 Definite integral
- 9.3.1 Definition of the definite integral as a limit of Riemann sums `[Block: Measurement sense > Integral and applications]`
- 9.3.2 Geometric interpretation: signed area under a curve `[Block: Measurement sense > Integral and applications]`
- 9.3.3 Properties of the definite integral `[Block: Measurement sense > Integral and applications]`
- 9.3.4 Fundamental theorem of calculus (Barrow's rule): statement and application `[Block: Measurement sense > Integral and applications]`
- 9.3.5 Evaluating definite integrals using the fundamental theorem `[Block: Measurement sense > Integral and applications]`

### 9.4 Area calculations
- 9.4.1 Area between a curve and the x-axis over an interval `[Block: Measurement sense > Integral and applications]`
- 9.4.2 Handling sign changes: splitting the interval `[Block: Measurement sense > Integral and applications]`
- 9.4.3 Area between two curves: setup and computation `[Block: Measurement sense > Integral and applications]`
- 9.4.4 Finding intersection points before computing area between curves `[Block: Measurement sense > Integral and applications]`

### 9.5 Volumes of solids of revolution
- 9.5.1 Volume of revolution about the x-axis: Pappus-Cavalieri formula (disk method) `[Block: Measurement sense > Integral and applications]`
- 9.5.2 Volume of revolution about the y-axis `[Block: Measurement sense > Integral and applications]`
- 9.5.3 Volume between two surfaces of revolution `[Block: Measurement sense > Integral and applications]`

---

## Chapter 10. Probability

### 10.1 Foundations of probability
- 10.1.1 Random experiment, sample space, and events `[Block: Stochastic sense > Probability]`
- 10.1.2 Kolmogorov's axioms: axiomatic definition of probability `[Block: Stochastic sense > Probability]`
- 10.1.3 Properties derived from the axioms: complement, union, monotonicity `[Block: Stochastic sense > Probability]`
- 10.1.4 Venn diagrams: representation and probability calculations `[Block: Stochastic sense > Probability]`

### 10.2 Counting techniques
- 10.2.1 Multiplication and addition principles `[Block: Stochastic sense > Probability]`
- 10.2.2 Combinations, permutations, and arrangements: formulas and applications `[Block: Stochastic sense > Probability]`
- 10.2.3 Laplace's rule: probability in equiprobable spaces `[Block: Stochastic sense > Probability]`

### 10.3 Conditional probability and independence
- 10.3.1 Definition of conditional probability: P(A|B) `[Block: Stochastic sense > Conditional probability]`
- 10.3.2 Multiplication rule: P(A ∩ B) = P(A|B)·P(B) `[Block: Stochastic sense > Conditional probability]`
- 10.3.3 Independence of events: definition and criterion `[Block: Stochastic sense > Conditional probability]`
- 10.3.4 Mutual independence of three or more events `[Block: Stochastic sense > Conditional probability]`

### 10.4 Tree diagrams and contingency tables
- 10.4.1 Constructing and interpreting tree diagrams `[Block: Stochastic sense > Conditional probability]`
- 10.4.2 Computing compound probabilities using trees `[Block: Stochastic sense > Conditional probability]`
- 10.4.3 Contingency tables: construction and interpretation `[Block: Stochastic sense > Conditional probability]`
- 10.4.4 Extracting marginal, joint, and conditional probabilities from tables `[Block: Stochastic sense > Conditional probability]`

### 10.5 Total probability and Bayes' theorem
- 10.5.1 Partition of the sample space: complete system of events `[Block: Stochastic sense > Conditional probability]`
- 10.5.2 Total probability theorem: statement and application `[Block: Stochastic sense > Conditional probability]`
- 10.5.3 Bayes' theorem: statement and application to posterior probabilities `[Block: Stochastic sense > Conditional probability]`
- 10.5.4 Applications of Bayes in real contexts: diagnostic tests, reliability `[Block: Stochastic sense > Conditional probability]`

---

## Chapter 11. Probability Distributions

### 11.1 Random variables
- 11.1.1 Discrete random variable: definition, probability mass function, and distribution function `[Block: Stochastic sense > Probability distributions]`
- 11.1.2 Continuous random variable: probability density function and cumulative distribution function `[Block: Stochastic sense > Probability distributions]`
- 11.1.3 Expected value, variance, and standard deviation of a random variable `[Block: Stochastic sense > Probability distributions]`
- 11.1.4 Properties of expectation and variance: E(aX+b), Var(aX+b) `[Block: Stochastic sense > Probability distributions]`

### 11.2 Binomial distribution
- 11.2.1 Bernoulli trial: definition and parameter p `[Block: Stochastic sense > Probability distributions]`
- 11.2.2 Binomial distribution B(n, p): definition and conditions for use `[Block: Stochastic sense > Probability distributions]`
- 11.2.3 Probability mass function: P(X = k) = C(n,k)·p^k·(1−p)^(n−k) `[Block: Stochastic sense > Probability distributions]`
- 11.2.4 Parameters of the binomial: mean μ = np and standard deviation σ = √(np(1−p)) `[Block: Stochastic sense > Probability distributions]`
- 11.2.5 Computing binomial probabilities: exact, cumulative, and complementary `[Block: Stochastic sense > Probability distributions]`

### 11.3 Normal distribution
- 11.3.1 Normal curve: shape, symmetry, and parameters μ and σ `[Block: Stochastic sense > Probability distributions]`
- 11.3.2 Probability density function of the normal distribution N(μ, σ) `[Block: Stochastic sense > Probability distributions]`
- 11.3.3 Properties of the normal distribution: the 68-95-99.7 rule `[Block: Stochastic sense > Probability distributions]`
- 11.3.4 Standardisation: converting N(μ, σ) to N(0, 1) `[Block: Stochastic sense > Probability distributions]`
- 11.3.5 Using the standard normal table: P(Z ≤ z), P(a ≤ Z ≤ b) `[Block: Stochastic sense > Probability distributions]`
- 11.3.6 Computing probabilities with the normal distribution in real problems `[Block: Stochastic sense > Probability distributions]`

### 11.4 Normal approximation to the binomial
- 11.4.1 Conditions for the approximation: large n, np ≥ 5 and n(1−p) ≥ 5 `[Block: Stochastic sense > Probability distributions]`
- 11.4.2 Yates' continuity correction `[Block: Stochastic sense > Probability distributions]`
- 11.4.3 Solving problems using the binomial-to-normal approximation `[Block: Stochastic sense > Probability distributions]`

### 11.5 Elementary inference and use of technology
- 11.5.1 Concept of representative sample and sample statistics `[Block: Stochastic sense > Data analysis and inference]`
- 11.5.2 Analysing samples with digital tools: statistical software and spreadsheets `[Block: Stochastic sense > Data analysis and inference]`

---

*Document generated for the Mathematics II curriculum plan — 2nd Year Upper Secondary (Bachillerato), Science and Technology Track*  
*Comunidad de Madrid · Decreto 64/2022 (LOMLOE) · FUHEM Curriculum Plan 2025-26*
