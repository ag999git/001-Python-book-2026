
# The `math` Module

Python's built-in `math` module gives you fast, C-implemented functions for the number-crunching you'd otherwise have to write by hand: constants like π and e, rounding and sign helpers, powers and logarithms, trigonometry, and a few specialized statistical functions. Everything in this module works on plain `int` and `float` values — for lists or arrays of numbers, see the [Modern Alternatives to `math`](#modern-alternatives-to-math) section at the end of this chapter.

To use any function below, you first need to import the module:

```python
import math
```

---

## 1. Mathematical Constants

These are fixed attributes rather than functions — they take no parameters and aren't called with `()`.

| Constant | Value | Description | Example Usage |
| --- | --- | --- | --- |
| `math.pi` | 3.141592... | Ratio of a circle's circumference to its diameter | `area = math.pi * r ** 2` |
| `math.e` | 2.718281... | Base of natural logarithms | `val = math.e ** 2` |
| `math.tau` | 6.283185... | Full circle constant ($2\pi$) | `circ = math.tau * r` |
| `math.inf` | `inf` | Floating-point positive infinity | `my_inf = math.inf` |
| `math.nan` | `nan` | "Not a Number" (undefined result) | `if math.isnan(x):` |

---

## 2. Number-Theoretic & Representation Functions

These functions handle rounding, signs, and basic integer logic.

| Function | Input Parameters | Output | Simple Example |
| --- | --- | --- | --- |
| `math.ceil(x)` | Single number $x$ | Smallest integer $\geq x$ | `math.ceil(4.2)` → `5` |
| `math.floor(x)` | Single number $x$ | Largest integer $\leq x$ | `math.floor(4.8)` → `4` |
| `math.trunc(x)` | Single number $x$ | Integer part of $x$ (drops the decimal) | `math.trunc(4.8)` → `4` |
| `math.fabs(x)` | Single number $x$ | Absolute value (always a float) | `math.fabs(-5)` → `5.0` |
| `math.gcd(a, b)` | Two integers $a, b$ | Greatest Common Divisor | `math.gcd(12, 18)` → `6` |
| `math.factorial(n)` | Non-negative integer $n$ | $n!$ | `math.factorial(5)` → `120` |
| `math.isclose(a, b)` | Two floats $a, b$ | `True`/`False` — are they nearly equal? | `math.isclose(0.1 + 0.2, 0.3)` → `True` |

> **Why `math.isclose` matters:** floating-point numbers can't represent most decimals exactly, so `0.1 + 0.2 == 0.3` actually evaluates to `False`. `math.isclose()` compares numbers within a small tolerance instead of checking for exact equality — always prefer it over `==` when comparing floats.

---

## 3. Power and Logarithmic Functions

Essential for handling growth, roots, and scaling.

| Function | Input Parameters | Output | Simple Example |
| --- | --- | --- | --- |
| `math.sqrt(x)` | Single number $x$ | Square root of $x$ | `math.sqrt(25)` → `5.0` |
| `math.isqrt(n)` | Non-negative integer $n$ | Integer square root (floored) | `math.isqrt(28)` → `5` |
| `math.pow(x, y)` | Base $x$, Exponent $y$ | $x$ raised to power $y$ (always a float) | `math.pow(2, 3)` → `8.0` |
| `math.exp(x)` | Single number $x$ | $e$ raised to power $x$ | `math.exp(1)` → `2.718...` |
| `math.log(x, [base])` | Number $x$, optional base | Logarithm of $x$ (natural log if base omitted) | `math.log(100, 10)` → `2.0` |
| `math.log10(x)` | Single number $x$ | Base-10 logarithm | `math.log10(1000)` → `3.0` |

> **`math.pow` vs. `**`:** `math.pow(x, y)` always returns a `float`, while Python's built-in `**` operator returns an `int` if both operands are integers (e.g. `2 ** 3` → `8`, but `math.pow(2, 3)` → `8.0`). For most everyday code, `**` is the more natural choice.

---

## 4. Trigonometric & Angular Functions

Used for calculating angles and distances. **All trig functions expect — and return — angles in radians, not degrees.**

| Function | Input Parameters | Output | Simple Example |
| --- | --- | --- | --- |
| `math.sin(x)` | Angle $x$ in radians | Sine of $x$ | `math.sin(math.pi / 2)` → `1.0` |
| `math.cos(x)` | Angle $x$ in radians | Cosine of $x$ | `math.cos(0)` → `1.0` |
| `math.tan(x)` | Angle $x$ in radians | Tangent of $x$ | `math.tan(0)` → `0.0` |
| `math.hypot(x, y)` | Sides $x$ and $y$ | Hypotenuse $\sqrt{x^2 + y^2}$ | `math.hypot(3, 4)` → `5.0` |
| `math.degrees(x)` | Radians $x$ | Value converted to degrees | `math.degrees(math.pi)` → `180.0` |
| `math.radians(x)` | Degrees $x$ | Value converted to radians | `math.radians(180)` → `3.1415...` |

---

## 5. Hyperbolic & Special Functions

Advanced functions used in specialized engineering and statistics work.

| Function | Input Parameters | Output | Simple Example |
| --- | --- | --- | --- |
| `math.sinh(x)` | Single number $x$ | Hyperbolic sine | `math.sinh(0)` → `0.0` |
| `math.cosh(x)` | Single number $x$ | Hyperbolic cosine | `math.cosh(0)` → `1.0` |
| `math.gamma(x)` | Single number $x$ | Gamma function $\Gamma(x)$ | `math.gamma(5)` → `24.0` |
| `math.erf(x)` | Single number $x$ | Gaussian error function | `math.erf(0)` → `0.0` |

---

## Worked Problems

### Problem 1: Find the hypotenuse of a right triangle

**Formula:** $c = \sqrt{a^2 + b^2}$, where $a$ and $b$ are the two legs of the triangle and $c$ is the hypotenuse.

```python
import math

def calculate_hypotenuse(a, b):
    """Return the hypotenuse of a right triangle given its two legs."""
    return math.sqrt(a**2 + b**2)

# Example usage
leg_a = 3
leg_b = 4
hypotenuse_length = calculate_hypotenuse(leg_a, leg_b)
print(f"The length of the hypotenuse is: {hypotenuse_length}")
# Output: The length of the hypotenuse is: 5.0
```

*Tip: this is exactly what `math.hypot(a, b)` does in one call — try replacing the function body with `return math.hypot(a, b)` and confirm you get the same answer.*

### Problem 2: Find the area of a circle

**Formula:** $Area = \pi \times r^2$

```python
import math

radius = 5
area = math.pi * radius ** 2

print("Area of the circle with radius", radius, "is:", area)
# Output: Area of the circle with radius 5 is: 78.53981633974483
```

We use `math.pi` for an accurate value of π, and `**` for exponentiation to calculate $r^2$.

---

## Modern Alternatives to `math`

The `math` module works on one number at a time. When you need to process many numbers at once, or need a different kind of precision, these libraries pick up where it leaves off:

1. **NumPy** — the "gold standard" for numerical computing in Python. It does everything `math` does, but operates on entire arrays of numbers at once, which is far faster than looping.
2. **SciPy** — built on top of NumPy; adds tools for calculus, signal processing, and other advanced scientific computing.
3. **SymPy** — for *symbolic* math. Instead of collapsing `1/3` into `0.333...`, it can keep the exact fraction, letting you do algebra and calculus symbolically.
4. **`decimal` module** — for applications (like finance) that need exact decimal precision, avoiding classic floating-point quirks such as `0.1 + 0.2 != 0.3`.


