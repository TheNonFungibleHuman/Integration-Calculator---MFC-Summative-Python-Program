# Integration Calculator - MFC Pyth

A Python program that computes exact antiderivatives and evaluates definite integrals using symbolic algebra. Built as a summative project exploring integration as a core concept in calculus.

---

## What It Does

You type a function of `x`. The program returns its exact antiderivative — no approximations, no rounding. Optionally, you provide an interval `[a, b]` and it evaluates the definite integral using the Fundamental Theorem of Calculus, giving both the exact value and a decimal.

---

## Mathematics Behind It

**Indefinite integral:**
```
∫ f(x) dx = F(x) + C
```
where F'(x) = f(x) and C is the constant of integration.

**Definite integral (Fundamental Theorem of Calculus):**
```
∫[a to b] f(x) dx = F(b) - F(a)
```

The program handles polynomials, trigonometric functions, exponentials, logarithms, and more — anything SymPy can integrate symbolically.

---

## Sample Run

```
=======================================================
       SYMBOLIC INTEGRATION CALCULATOR
=======================================================
Supported operators:  + - * / ** (power)
Supported functions:  sin, cos, tan, exp, log, sqrt
Variable: x
-------------------------------------------------------

Enter a function of x (e.g. x**2 + 3*x - 5): x**2 + 3*x - 5

-------------------------------------------------------
  INDEFINITE INTEGRAL RESULT
-------------------------------------------------------
  f(x)        =  x**2 + 3*x - 5
  ∫ f(x) dx   =  x**3/3 + 3*x**2/2 - 5*x  + C
-------------------------------------------------------

Would you like to evaluate a definite integral? (yes / no): yes
Enter the limits of integration.
  Lower limit a: 0
  Upper limit b: 2

-------------------------------------------------------
  DEFINITE INTEGRAL RESULT
-------------------------------------------------------
  ∫[0 to 2] x**2 + 3*x - 5 dx
  Exact value   =  -4/3
  Decimal value ≈  -1.333333
-------------------------------------------------------
```

---

## Getting Started

**Requirements:** Python 3.7+

**Install the dependency:**
```bash
pip install sympy
```

**Run the program:**
```bash
python integration_calculator.py
```

---

## Supported Input Syntax

| Math notation | Type this |
|---|---|
| x² + 3x | `x**2 + 3*x` |
| sin(x) | `sin(x)` |
| eˣ | `exp(x)` |
| ln(x) | `log(x)` |
| √x | `sqrt(x)` |
| π (as a limit) | `pi` |

---

## File Structure

```
integration-calculator/
├── integration_calculator.py   # Main program
└── README.md                   # This file
```

---
