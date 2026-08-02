



## Advanced Guide to Complex Numbers in Python

### Table of Contents
* [1. Representation of Complex Numbers](004-ch2-complex-numbers-advanced.md#1-representation-of-complex-numbers)
* [2. Creating Complex Numbers](004-ch2-complex-numbers-advanced.md#2-creating-complex-numbers)
* [3. Basic Operations](004-ch2-complex-numbers-advanced.md#3-basic-operations)
* [4. Euler's Formula and Polar Representation](004-ch2-complex-numbers-advanced.md#4-eulers-formula-and-polar-representation)
* [5. IEEE-754 Behavior and Edge Cases](004-ch2-complex-numbers-advanced.md#5-ieee-754-behavior-and-edge-cases)
* [6. Comparison of Complex Numbers](004-ch2-complex-numbers-advanced.md#6-comparison-of-complex-numbers)
* [7. Useful Scientific Applications](004-ch2-complex-numbers-advanced.md#7-useful-scientific-applications)
* [8. Performance Notes](004-ch2-complex-numbers-advanced.md#8-performance-notes)
* []()

Python provides **built-in support** for complex numbers.  
Unlike many languages where complex numbers require external libraries, Python includes a full complex number type in the core language.  
This guide covers complex numbers from basics to advanced internals, IEEE-754 behavior, edge cases, and scientific computing applications.

---

### 1. Representation of Complex Numbers

A complex number in Python is written as:

```
x + yj
```

Where:

- **x** = real part (int or float)  
- **y** = imaginary part (int or float)  
- **j** = imaginary unit √(-1)

Python uses **j** instead of mathematical **i**.

#### Example
```python
z = 3 + 4j
z.real   # 3.0
z.imag   # 4.0
```

Internally, Python stores complex numbers as **two 64-bit floats**, making them efficient and precise.

---
[Back to the Table of Contents](004-ch2-complex-numbers-advanced.md#table-of-contents)

### 2. Creating Complex Numbers

#### 2.1 Direct literal
```python
z = 3 + 4j
```

#### 2.2 Using the complex() constructor
```python
complex(3, 4)   # same as 3+4j
```

#### 2.3 Imaginary-only values
```python
z = 5j
```

---

[Back to the Table of Contents](004-ch2-complex-numbers-advanced.md#table-of-contents)
### 3. Basic Operations

Python supports all common arithmetic operators:

```python
(3 + 4j) + (1 + 2j)
(3 + 4j) - (1 + 2j)
(3 + 4j) * (1 + 2j)
(3 + 4j) / (1 + 2j)
```

#### Magnitude (absolute value)
```python
abs(3 + 4j)   # 5.0
```

#### Conjugate
```python
(3 + 4j).conjugate()   # 3 - 4j
```

---

### 4. Euler's Formula and Polar Representation

Python supports polar operations using cmath:

```python
import cmath

r, phi = cmath.polar(3 + 4j)
z = cmath.rect(r, phi)   # converts back to rectangular form
```

---
[Back to the Table of Contents](004-ch2-complex-numbers-advanced.md#table-of-contents)

### 5. IEEE-754 Behavior and Edge Cases

Because complex numbers use **double-precision floats**, they inherit float-related behavior:

- **inf + infj**
- **nan values**
- **underflow/overflow**

Example:
```python
complex(float('inf'), 2)
complex(1, float('nan'))
```

You can check:
```python
math.isinf(z.real)
math.isnan(z.imag)
```

---
[Back to the Table of Contents](004-ch2-complex-numbers-advanced.md#table-of-contents)

### 6. Comparison of Complex Numbers

Python **does not** allow ordering comparisons:

```python
3+4j < 2+1j   # TypeError
```

But equality works:

```python
(3+4j) == (3+4j)  # True
```

---

### 7. Useful Scientific Applications

Complex numbers appear in:

- Electrical engineering (impedance)
- Signal processing (FFT)
- Quantum mechanics
- Control systems
- Fractals (Mandelbrot set)
- Machine learning algorithms

Example: FFT uses complex numbers heavily:

```python
import numpy as np
np.fft.fft([1,2,3])
```

---
[Back to the Table of Contents](004-ch2-complex-numbers-advanced.md#table-of-contents)

### 8. Performance Notes

Complex math is implemented in C within CPython → **fast**.  
NumPy uses **vectorized** complex operations → **extremely fast** for scientific workloads.

---

### 9. Summary Table

| Operation         | Python Code                     |
|------------------|--------------------------------|
| Create           | `3+4j`, `complex(3,4)`         |
| Real part        | `z.real`                       |
| Imag part        | `z.imag`                       |
| Conjugate        | `z.conjugate()`                |
| Magnitude        | `abs(z)`                       |
| Polar form       | `cmath.polar(z)`               |
| Rectangular form | `cmath.rect(r,phi)`            |





[Back to the Table of Contents](004-ch2-complex-numbers-advanced.md#table-of-contents)

### Advanced Complex Number Examples in Python

#### 1. Euler's Formula

```python
import cmath

theta = cmath.pi / 3
value = cmath.exp(1j * theta)
print("exp(iθ) ->", value)
# (0.5000000000000001+0.8660254037844386j)

print("cosθ + i sinθ ->", cmath.cos(theta) + 1j*cmath.sin(theta))
# (0.5000000000000001+0.8660254037844386j)
```

#### 2. Polar and Rectangular Forms

```python
z = 4 + 4j

r, ang = cmath.polar(z)
print("polar(z) ->", (r, ang))
# (5.656854249492381, 0.7853981633974483)

z2 = cmath.rect(r, ang)
print("rect(r, ang) ->", z2)
# (4.000000000000001+4.000000000000001j)
```

#### 3. IEEE‑754 Special Values (inf, nan)

```python
a = complex(float("inf"), 5)
b = complex(3, float("nan"))

print("a ->", a)
# (inf+5j)

print("b ->", b)
# (3+nanj)

print("a + b ->", a + b)
# (inf+nanj)

print("abs(a) ->", abs(a))
# inf
```

#### 4. NumPy Complex Arithmetic

```python
import numpy as np

arr1 = np.array([1+2j, 3+4j, -2+5j])
arr2 = np.array([2-1j, 0+3j, 4+4j])

print("arr1 + arr2 ->", arr1 + arr2)
# [ 3.+1.j  3.+7.j  2.+9.j]

print("arr1 * arr2 ->", arr1 * arr2)
# [  4. +3.j -12.+21.j -28. +6.j]

print("np.abs(arr1) ->", np.abs(arr1))
# [2.23606798 5.         5.38516481]

print("FFT ->", np.fft.fft([1,2,3]))
# [ 6.+0.j        -1.+1.73205081j -1.-1.73205081j]
```

[Back to the Table of Contents](004-ch2-complex-numbers-advanced.md#table-of-contents)
