### Table of contents
- [Python example scripts showing the usage of float](#python-example-scripts-showing-the-usage-of-float)
  - [Block 1 — Basic floats & arithmetic](#block-1--basic-floats--arithmetic)
  - [Block 2 abs(), repr(), str()](#block-2-abs-repr-str)
  - [Block 3 — type(), isinstance(), format()](#block-3--type-isinstance-format)
  - [Block 4 — is_integer(), round()](#block-4--is_integer-round)
  - [Block 5 — pow() and infinity NaN/ Arithmetic](#block-5--pow-and-infinity-nan-arithmetic)
  - [Block 6 — sys.getsizeof() and hash() for floats](#block-6--sysgetsizeof-and-hash-for-floats)
  - [BLOCK 7 — float() Constructor + float.fromhex()](#block-7--float-constructor--floatfromhex)
  - [BLOCK 8 — Special float Methods: is_integer(), Final Tests](#block-8--special-float-methods-is_integer-final-tests)
- [Python float — Detailed Beginner + Advanced Notes](#python-float--detailed-beginner--advanced-notes)
  - [1. What is a Float?](#1-what-is-a-float)
  - [2. Writing Floats in Python](#2-writing-floats-in-python)
  - [3. Basic Float Operations](#3-basic-float-operations)
  - [4. Implicit Type Conversion (Type Promotion)](#4-implicit-type-conversion-type-promotion)
  - [5. Float Precision](#5-float-precision)
  - [6. Special Float Values (IEEE-754)](#6-special-float-values-ieee-754)
  - [7. Converting Other Types to Float](#7-converting-other-types-to-float)
  - [8. Floats vs Decimal vs Fraction (Advanced)](#8-floats-vs-decimal-vs-fraction-advanced)
  - [9. Common Float Pitfalls](#9-common-float-pitfalls)
  - [10. Best Practices for Students](#10-best-practices-for-students)
  - [11. Summary](#11-summary)
- [Quiz](#quiz)
  - [BEGINNER LEVEL (Q&A)](#beginner-level-qa)
  - [INTERMEDIATE LEVEL (Q&A)](#intermediate-level-qa)
  - [ADVANCED LEVEL (Q&A)](#advanced-level-qa)
  - [EXTRA CHALLENGE (Q&A)](#extra-challenge-qa)


### Python example scripts showing the usage of float
- Given below are 8 blocks showing usage of float data type in Python
- The output are given in hash comment (#) using format:- `# label-> actual_output`. The expected output is given below the code line in hash comment (#)
- Wherever necessary, inline comments using hash (#) are also added for explaining the output. These comments are added below the code line.
- Note that in some cases the output may vary from system to system.
- Some of the concepts/ methods/ functions used may be advanced which you may ignore.
- Ideally you should copy/ paste each of the code blocks and check the output for yourself.

#### Block 1 — Basic floats & arithmetic
- Literals
- Scientific notation
- Basic operators
- Floor division & modulus

```python
print("8.72->", 8.72)  # 8.72-> 8.72
print("-0.0045->", -0.0045)  # -0.0045-> -0.0045
print("4.0e2->", 4.0e2)  # 4.0e2-> 400.0
print("6.91E-3->", 6.91E-3)  # 6.91E-3-> 0.00691
print("1.8 + 3.7->", 1.8 + 3.7)  # 1.8 + 3.7-> 5.5
print("9.0 - 4.6->", 9.0 - 4.6)  # 9.0 - 4.6-> 4.4
print("3.5 * 2.0->", 3.5 * 2.0)  # 3.5 * 2.0-> 7.0
print("12.6 / 3.15->", 12.6 / 3.15)  # 12.6 / 3.15-> 4.0
# Division always produces float, even if result is whole number.
print("9.6 // 2.4->", 9.6 // 2.4)  # 9.6 // 2.4-> 4.0
# Floor division gives the floor of the result, but here the result is exact.
print("9.6 % 2.4->", 9.6 % 2.4)  # 9.6 % 2.4-> 0.0
# Because 2.4 * 4 = 9.6, remainder is exactly 0.0.

```



[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### Block 2 abs(), repr(), str()
- Show float formatting
- Demonstrate float rounding issue.
- NaN/infinity representations


```python

print("abs(-7.8)->", abs(-7.8))  # abs(-7.8)-> 7.8
print("abs(float('nan'))->", abs(float('nan')))  # abs(float('nan'))-> nan
# abs() of NaN is still NaN because NaN is “not a real number”

print("abs(float('-inf'))->", abs(float('-inf')))  # abs(float('-inf'))-> inf
# | -∞ | = ∞

print("repr(8.72)->", repr(8.72))  # repr(8.72)-> 8.72
print("repr(float('nan'))->", repr(float('nan')))  # repr(float('nan'))-> nan
print("repr(float('inf'))->", repr(float('inf')))  # repr(float('inf'))-> inf
print("repr(float('-inf'))->", repr(float('-inf')))  # repr(float('-inf'))-> -inf
print("repr(0.15 + 0.35)->", repr(0.15 + 0.35))  # repr(0.15 + 0.35)-> 0.5
# Here float rounding is exact — unlike the classic 0.1 + 0.2 case.

print("str(8.72)->", str(8.72))  # str(8.72)-> 8.72
print("str(float('nan'))->", str(float('nan')))  # str(float('nan'))-> nan
print("str(float('inf'))->", str(float('inf')))  # str(float('inf'))-> inf
print("str(float('-inf'))->", str(float('-inf')))  # str(float('-inf'))-> -inf

```

[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### Block 3 — type(), isinstance(), format()


```python
print("type(8.72)->", type(8.72))  # type(8.72)-> <class 'float'>
print("type(float('nan'))->", type(float('nan')))  # type(float('nan'))-> <class 'float'>
print("type(float('inf'))->", type(float('inf')))  # type(float('inf'))-> <class 'float'>
print("type(float('-inf'))->", type(float('-inf')))  # type(float('-inf'))-> <class 'float'>
print("isinstance(8.72, float)->", isinstance(8.72, float))  # isinstance(8.72, float)-> True
print("isinstance(15, float)->", isinstance(15, float))  # isinstance(15, float)-> False
# Integers are not floats.

print("isinstance(float('nan'), float)->", isinstance(float('nan'), float))  
# isinstance(float('nan'), float)-> True

print("isinstance(float('inf'), float)->", isinstance(float('inf'), float))  
# isinstance(float('inf'), float)-> True

print("isinstance(float('-inf'), float)->", isinstance(float('-inf'), float))  
# isinstance(float('-inf'), float)-> True

print("format(6.2831, '.2f')->", format(6.2831, '.2f'))  # format(6.2831, '.2f')-> 6.28
# Rounded to 2 decimal places.

print("format(4.8, 'e')->", format(4.8, 'e'))  # format(4.8, 'e')-> 4.800000e+00
# Scientific notation format.

print("format(float('inf'), 'f')->", format(float('inf'), 'f'))  # format(float('inf'), 'f')-> inf
print("format(float('-inf'), 'f')->", format(float('-inf'), 'f'))  # format(float('-inf'), 'f')-> -inf
print("format(float('nan'), 'f')->", format(float('nan'), 'f'))  # format(float('nan'), 'f')-> nan

```

[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### Block 4 — is_integer(), round()
- integer-like floats.
- rounding rules.
- banker’s rounding


```python
print("(5.0).is_integer()->", (5.0).is_integer())  # (5.0).is_integer()-> True
# 5.0 is exactly an integer value.

print("(5.67).is_integer()->", (5.67).is_integer())  # (5.67).is_integer()-> False
print("(0.0).is_integer()->", (0.0).is_integer())  # (0.0).is_integer()-> True
# Zero is considered an integer.

print("(-4.0).is_integer()->", (-4.0).is_integer())  # (-4.0).is_integer()-> True
print("(-4.75).is_integer()->", (-4.75).is_integer())  # (-4.75).is_integer()-> False

print("round(6.2831)->", round(6.2831))  # round(6.2831)-> 6
# Rounded to nearest integer.

print("round(6.2831, 2)->", round(6.2831, 2))  # round(6.2831, 2)-> 6.28
print("round(6.2831, 3)->", round(6.2831, 3))  # round(6.2831, 3)-> 6.283

print("round(-3.75)->", round(-3.75))  # round(-3.75)-> -4
# Python uses "Banker's rounding" (round half to even).  
# -3.75 is exactly halfway between -4 and -3 → rounds to -4 (the even number).

print("round(-3.75, 1)->", round(-3.75, 1))  # round(-3.75, 1)-> -3.8
# Rounded to 1 decimal place.

```
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### Block 5 — pow() and infinity NaN/ Arithmetic
- negative powers.
- infinity rules.
- negative infinity behavior


```python

# --- pow() function examples ---

print("pow(3.0, 4.0)->", pow(3.0, 4.0))  
# pow(3.0, 4.0)-> 81.0
# 3^4 = 81

print("pow(3.0, -4.0)->", pow(3.0, -4.0))  
# pow(3.0, -4.0)-> 0.012345679012345678
# Negative exponent → reciprocal of 3^4

print("pow(float('inf'), 2)->", pow(float('inf'), 2))  
# pow(float('inf'), 2)-> inf

print("pow(float('-inf'), 2)->", pow(float('-inf'), 2))  
# pow(float('-inf'), 2)-> inf
# Negative infinity squared becomes positive infinity.

print("pow(float('inf'), -1)->", pow(float('inf'), -1))  
# pow(float('inf'), -1)-> 0.0
# 1 / infinity → 0

print("pow(float('-inf'), -1)->", pow(float('-inf'), -1))  
# pow(float('-inf'), -1)-> -0.0
# 1 / (negative infinity) → negative zero (a valid IEEE-754 value)

# --- Infinity & NaN interactions ---

print("float('inf') + float('-inf')->", float('inf') + float('-inf'))  
# float('inf') + float('-inf')-> nan
# inf - inf is undefined → NaN.

print("float('inf') * 0->", float('inf') * 0)  
# float('inf') * 0-> nan
# Infinity times zero is undefined.

print("float('nan') + 1->", float('nan') + 1)  
# float('nan') + 1-> nan

print("float('nan') * 2->", float('nan') * 2)  
# float('nan') * 2-> nan

print("float('inf') / float('inf')->", float('inf') / float('inf'))  
# float('inf') / float('inf')-> nan

print("float('-inf') / float('-inf')->", float('-inf') / float('-inf'))  
# float('-inf') / float('-inf')-> nan

print("float('inf') - float('inf')->", float('inf') - float('inf'))  
# float('inf') - float('inf')-> nan

print("float('-inf') + float('inf')->", float('-inf') + float('inf'))  
# float('-inf') + float('inf')-> nan

print("float('nan') ** 2->", float('nan') ** 2)  
# float('nan') ** 2-> nan

print("float('nan') ** 0->", float('nan') ** 0)  
# float('nan') ** 0-> 1.0
# Any number (including NaN) raised to power 0 is 1 (IEEE-754 rule).

print("float('inf') ** 2->", float('inf') ** 2)  
# float('inf') ** 2-> inf

print("float('-inf') ** 2->", float('-inf') ** 2)  
# float('-inf') ** 2-> inf

print("float('inf') ** -1->", float('inf') ** -1)  
# float('inf') ** -1-> 0.0

print("float('-inf') ** -1->", float('-inf') ** -1)  
# float('-inf') ** -1-> -0.0
# Negative infinity with negative exponent produces -0.0 (IEEE-754 negative zero).

```
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### Block 6 — sys.getsizeof() and hash() for floats
- Explain why size never changes
- sys.getsizeof() (float memory size).
- hash() behavior for floats (including NaN).
- Negative zero hashing.
- IEEE-754 explanations where needed



```python

# --- Using sys.getsizeof() to examine memory consumption of floats ---

import sys

print("sys.getsizeof(0.1)->", sys.getsizeof(0.1))  
# sys.getsizeof(0.1)-> 24
# All Python floats take 24 bytes (CPython), regardless of value.

print("sys.getsizeof(0.0)->", sys.getsizeof(0.0))  
# sys.getsizeof(0.0)-> 24

print("sys.getsizeof(1.0)->", sys.getsizeof(1.0))  
# sys.getsizeof(1.0)-> 24

print("sys.getsizeof(9876543210.0)->", sys.getsizeof(9876543210.0))  
# sys.getsizeof(9876543210.0)-> 24
# Large floats don’t take extra space (unlike ints).

print("sys.getsizeof(-9876543210.0)->", sys.getsizeof(-9876543210.0))  
# sys.getsizeof(-9876543210.0)-> 24

print("sys.getsizeof(1.7976931348623157e+308)->", sys.getsizeof(1.7976931348623157e+308))  
# sys.getsizeof(1.7976931348623157e+308)-> 24
# Maximum finite IEEE-754 float.

print("sys.getsizeof(5e-324)->", sys.getsizeof(5e-324))  
# sys.getsizeof(5e-324)-> 24
# Smallest positive subnormal float.

# --- Using hash() on floats ---

print("hash(2.71)->", hash(2.71))  
# hash(2.71)-> <value may vary>  
# Hash values can differ between Python runs (hash randomization).

print("hash(float('nan'))->", hash(float('nan')))  
# hash(float('nan'))-> <value may vary>
# NaN is hashable but not equal to itself.

print("hash(float('inf'))->", hash(float('inf')))  
# hash(float('inf'))-> 314159  
# Typically stable across runs because inf is a special constant.

print("hash(float('-inf'))->", hash(float('-inf')))  
# hash(float('-inf'))-> -314159
# Negative infinity hashes to negative of infinity's hash.

```
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### BLOCK 7 — float() Constructor + float.fromhex()


```python

# --- Using float() constructor ---

print("float(12)->", float(12))  
# float(12)-> 12.0
# Integer → float conversion.

print("float('4.56789')->", float("4.56789"))  
# float('4.56789')-> 4.56789

print("float('nan')->", float('nan'))  
# float('nan')-> nan

print("float('inf')->", float('inf'))  
# float('inf')-> inf

print("float('-inf')->", float('-inf'))  
# float('-inf')-> -inf

print("float(True)->", float(True))  
# float(True)-> 1.0

print("float(False)->", float(False))  
# float(False)-> 0.0

print("float('1e309')->", float('1e309'))  
# float('1e309')-> inf
# Overflow → becomes positive infinity.

print("float('-1e309')->", float('-1e309'))  
# float('-1e309')-> -inf

# --- Comparing NaN and Infinity ---

print("float('nan') == float('nan')->", float('nan') == float('nan'))  
# float('nan') == float('nan')-> False
# NaN is never equal to anything, not even itself.

print("float('nan') != float('nan')->", float('nan') != float('nan'))  
# float('nan') != float('nan')-> True

print("float('inf') > 1e308->", float('inf') > 1e308)  
# float('inf') > 1e308-> True

print("float('-inf') < -1e308->", float('-inf') < -1e308)  
# float('-inf') < -1e308-> True

# --- Infinity arithmetic (continued) ---

print("float('inf') + float('-inf')->", float('inf') + float('-inf'))  
# float('inf') + float('-inf')-> nan

print("float('inf') * 0->", float('inf') * 0)  
# float('inf') * 0-> nan

print("float('nan') + 1->", float('nan') + 1)  
# float('nan') + 1-> nan

print("float('nan') * 2->", float('nan') * 2)  
# float('nan') * 2-> nan

print("float('inf') / float('inf')->", float('inf') / float('inf'))  
# float('inf') / float('inf')-> nan

# --- float.hex() ---

print("float.hex(4.56789)->", float.hex(4.56789))  
# float.hex(4.56789)-> Hexadecimal string representing same float.

print("float.hex(-3.25)->", float.hex(-3.25))  
# float.hex(-3.25)-> Hex representation of negative float.

print("float.hex(0.0)->", float.hex(0.0))  
# float.hex(0.0)-> 0x0.0p+0

print("float.hex(float('inf'))->", float.hex(float('inf')))  
# float.hex(float('inf'))-> inf

print("float.hex(float('-inf'))->", float.hex(float('-inf')))  
# float.hex(float('-inf'))-> -inf

print("float.hex(float('nan'))->", float.hex(float('nan')))  
# float.hex(float('nan'))-> nan

# --- float.fromhex() (Hex → Decimal float) ---

print("float.fromhex('0x1.91eb86p+1')->", float.fromhex('0x1.91eb86p+1'))  
# float.fromhex('0x1.91eb86p+1')-> 3.14159
# This hex literal encodes π approximately.

print("float.fromhex('-0x1.4p+2')->", float.fromhex('-0x1.4p+2'))  
# float.fromhex('-0x1.4p+2')-> -5.0

print("float.fromhex('0x0.0p+0')->", float.fromhex('0x0.0p+0'))  
# float.fromhex('0x0.0p+0')-> 0.0

# --- INVALID HEX FLOAT STRINGS (Kept as comments for teaching/ learning purpose) ---
# float.fromhex('0x1.0p+inf')   # Error: exponent cannot be 'inf'
# float.fromhex('-0x1.0p+inf')  # Error: exponent cannot be 'inf'
# float.fromhex('0x1.0p+nan')    # Error: exponent cannot be 'nan'
# float("abc")                  # Error: invalid literal
# float(None)                   # Error: None cannot convert to float
# float([])                     # Error: list cannot convert to float

```
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### BLOCK 8 — Special float Methods: is_integer(), Final Tests

```python

# --- is_integer() with special IEEE-754 values ---

print("float('nan').is_integer()->", float('nan').is_integer())  
# float('nan').is_integer()-> False
# NaN is not an integer.

print("float('inf').is_integer()->", float('inf').is_integer())  
# float('inf').is_integer()-> False
# Infinity is not an integer.

print("float('-inf').is_integer()->", float('-inf').is_integer())  
# float('-inf').is_integer()-> False

# --- float.hex() to view internal binary exponent/mantissa representation ---

print("float.hex(3.75)->", float.hex(3.75))  
# float.hex(3.75)-> 0x1.f000000000000p+1

print("float.hex(-7.5)->", float.hex(-7.5))  
# float.hex(-7.5)-> -0x1.e000000000000p+2

print("float.hex(0.0)->", float.hex(0.0))  
# float.hex(0.0)-> 0x0.0p+0

print("float.hex(float('inf'))->", float.hex(float('inf')))  
# float.hex(float('inf'))-> inf

print("float.hex(float('-inf'))->", float.hex(float('-inf')))  
# float.hex(float('-inf'))-> -inf

print("float.hex(float('nan'))->", float.hex(float('nan')))  
# float.hex(float('nan'))-> nan

# --- float.fromhex() tests (reverse conversion) ---

print("float.fromhex('0x1.f000000000000p+1')->", float.fromhex('0x1.f000000000000p+1'))  
# float.fromhex('0x1.f000000000000p+1')-> 3.75

print("float.fromhex('-0x1.e000000000000p+2')->", float.fromhex('-0x1.e000000000000p+2'))  
# float.fromhex('-0x1.e000000000000p+2')-> -7.5

print("float.fromhex('0x0.0p+0')->", float.fromhex('0x0.0p+0'))  
# float.fromhex('0x0.0p+0')-> 0.0

# --- Final demonstration: NaN propagation & special rules ---

print("float('nan') + 100->", float('nan') + 100)  
# float('nan') + 100-> nan

print("float('nan') - float('nan')->", float('nan') - float('nan'))  
# float('nan') - float('nan')-> nan

print("float('nan') * float('nan')->", float('nan') * float('nan'))  
# float('nan') * float('nan')-> nan

print("float('nan') / 5->", float('nan') / 5)  
# float('nan') / 5-> nan

print("float('inf') - float('inf')->", float('inf') - float('inf'))  
# float('inf') - float('inf')-> nan

print("float('-inf') + float('inf')->", float('-inf') + float('inf'))  
# float('-inf') + float('inf')-> nan

print("float('inf') * float('-inf')->", float('inf') * float('-inf'))  
# float('inf') * float('-inf')-> -inf
# Infinity * negative infinity = negative infinity (well-defined)

print("float('inf') ** 0->", float('inf') ** 0)  
# float('inf') ** 0-> 1.0
# ANY number^0 = 1 by rule (even inf).

print("float('nan') ** 0->", float('nan') ** 0)  
# float('nan') ** 0-> 1.0
# IEEE-754 rule: x**0 = 1 for all x (except maybe 0**0).

print("0.0 ** 0->", 0.0 ** 0)  
# 0.0 ** 0-> 1.0
# Python chooses mathematical convention: 0^0 = 1.

# --- End of all float demonstrations ---

```


[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)


### Python `float` — Detailed Beginner + Advanced Notes

The `float` type in Python represents **floating-point numbers**, i.e., real numbers that contain a decimal point or are written in scientific notation.

This document explains:
- What floats are
- How Python stores them
- Their precision limits
- Operations, conversions, pitfalls
- Advanced numerical behavior
- Best practices for students

---

#### 1. What is a Float?

- A `float` represents a **real number** (with fractional part).
- Examples:
  ```python
  3.14
  -0.5
  2.0
  ```

- Floating-point numbers follow the IEEE-754 **double-precision** format internally.
- This means floats are stored in **binary**, not decimal.

---

#### 2. Writing Floats in Python

##### Decimal notation:
```python
x = 3.75
y = 0.001
```

##### Scientific notation:
- Use `e` or `E` for `× 10^n`
```python
x = 3.5e2     # 3.5 × 10² = 350.0
y = 4.2e-3    # 4.2 × 10⁻³ = 0.0042
```

##### Integers with decimals automatically become float:
```python
5.0     # float
```

---
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### 3. Basic Float Operations

```python
a = 5.5
b = 2.0

print(a + b)    # 7.5
print(a - b)    # 3.5
print(a * b)    # 11.0
print(a / b)    # 2.75
print(a ** 2)   # 30.25
```

**Division always produces a float**, even for integers:
```python
5 / 2   # 2.5
```

---

#### 4. Implicit Type Conversion (Type Promotion)

When an `int` and `float` are used together:

- The `int` is converted to `float`
- Result is a `float`

```python
5 + 2.5    # 7.5
3 * 2.0    # 6.0
```

This follows the numeric tower:
```
int → float → complex
```

---

#### 5. Float Precision

- Python floats have **53 bits** of precision (about 15–17 decimal digits).
- After that range, rounding occurs.

Example:
```python
x = 1.234567890123456789
print(x)
```

Output:
```
1.2345678901234567
```

---
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### 6. Special Float Values (IEEE-754)

Python supports:

##### A. Infinity
```python
float('inf')
float('-inf')
```

##### B. Not-a-Number (NaN)
```python
float('nan')
```

NaN has special comparison rules:
```python
float('nan') == float('nan')   # False
```

---

#### 7. Converting Other Types to Float

##### int → float:
```python
float(5)   # 5.0
```

##### string → float:
```python
float("3.14")   # 3.14
float("2.5e3")  # 2500.0
```

##### bool → float:
```python
float(True)   # 1.0
float(False)  # 0.0
```

---
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### 8. Floats vs Decimal vs Fraction (Advanced)

Floats are fast but **not exact** for some values.

For exact decimal arithmetic, use:

##### `decimal.Decimal`:
```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.2')   # exact 0.3
```

For rational numbers, use:

##### `fractions.Fraction`:
```python
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)   # 1/2
```

---

#### 9. Common Float Pitfalls 

##### A. Precision issues
```python
0.1 * 3      # 0.30000000000000004
```

##### B. Accumulation errors in loops
```python
x = 0
for i in range(1000):
    x += 0.1
print(x)      # not exactly 100.0
```

##### C. Converting very large integers
```python
float(10**100)   # loses precision
```

---
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### 10. Best Practices for Students

- Use floats for:
  - physics, engineering, continuous math
  - percentages, interest calculations
  - measurements

- Use `Decimal` for:
  - money
  - banking systems
  - exact decimal math

- Use `Fraction` for:
  - exact rational arithmetic
  - symbolic math

- For float comparison, always prefer:
```python
math.isclose(a, b)
```

---

#### 11. Summary

- `float` stores real numbers using **binary floating-point** (IEEE-754).
- Supports decimals and scientific notation.
- Has **limited precision** (about 15–17 digits).
- Some decimal values cannot be represented exactly.
- Use `isclose`, `Decimal`, or `Fraction` to avoid precision problems.
- Ideal for real-world numerical computation, but not for exact arithmetic.

[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

### Quiz

### Python Float Quiz (Q&A Format)

This quiz includes beginner → intermediate → advanced questions, each followed immediately by the answer.

---

#### BEGINNER LEVEL (Q&A)

##### Q1. Which of the following are floats in Python?
a) `0.5`  
b) `5.0`  
c) `0.75`  
d) `2e3`  
e) All of the above  

**Answer:** e) All of the above  
- `0.5` , `5.0`, `0.75`, `2e3` are all floats.

---

##### Q2. What is the output of:
```python
print(3.0 + 2)
```

**Answer:** `5.0`  
The integer `2` is promoted to float → `2.0`.

---

##### Q3. How do you write “0.004” in scientific notation?* 
a) `0.4e-2`  
b) `4e-3`  
c) `4E-3`  
d) b and c  

**Answer:** d) b and c  
`0.004 = 4 × 10⁻³`.

---

##### Q4. What is the type of the result?
```python
x = 5 / 2
```
a) int  
b) float  
c) depends  

**Answer:** b) float  

---

##### Q5. Which expressions produce floats? 
a) `10 / 5`  
b) `10 // 5`  
c) `10.0 // 3`  
d) `10.0 / 3`  
e) `float(2)`  

**Answer:** a, d, e  
- `/` always gives float  
- `float(2)` is float  
- `10.0 // 3` → floor division → float? No, it returns **float only if any operand is float**, but here the result is still a float **representation**, e.g. `3.0`.  
(This is subtle but technically `//` with a float returns a float.)

---

##### Q6. What does the following print?
```python
x = 0.1
y = 0.2
print(x + y)
```

**Answer:** `0.30000000000000004`  
Because 0.1 and 0.2 cannot be represented exactly in binary floating-point.

---
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### INTERMEDIATE LEVEL (Q&A)

##### Q7. Predict output:
```python
print(3.5e2)
print(3.5e-2)
```

**Answer:**  
```
350.0
0.035
```

---

##### Q8. Convert the string `"2.75"` to float.

**Answer:**  
```python
float("2.75")
```

---

##### Q9. What does this print?
```python
print(float("nan") == float("nan"))
```

**Answer:** `False`  
NaN is never equal to anything—not even itself (IEEE-754 rule).

---

##### Q10. True or False? Floats can exactly represent all decimals.

**Answer:** **False**  
Binary floating-point cannot represent values like 0.1 exactly.

---

##### Q11. What is wrong with this?
```python
0.1 + 0.2 == 0.3
```

**Answer:** Floating-point rounding makes direct comparison unreliable.  
Correct method:
```python
import math
math.isclose(0.1 + 0.2, 0.3)
```

---

##### Q12. Fill in the blank:* 
Binary floating-point numbers cannot exactly represent __________.

**Answer:**  
**Most decimal fractions** (e.g., 0.1, 0.2, 0.3).

---
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

#### ADVANCED LEVEL (Q&A)

##### Q13. Why does Python use IEEE-754 double precision for floats?

**Answer:**  
- Standard across CPUs  
- Fast hardware implementations  
- Good balance of speed vs precision  
- Portable across platforms  

---

##### Q14. What happens when executing:
```python
x = float(10**100)
```

**Answer:**  
- Python converts huge integer into float  
- Precision is lost (float only stores ~15 digits)  
- The number becomes an approximation  
- Mantissa cannot hold all digits  

---

##### Q15. Difference between:
```python
float('inf')
float('-inf')
float('nan')
```

**Answer:**  
- `inf` = positive infinity  
- `-inf` = negative infinity  
- `nan` = Not-a-Number (invalid result, e.g. 0/0)

---

##### Q16. Evaluate:
```python
print(1e308 * 10)
print(1e-324 / 10)
```

**Answer:**  
- `1e308 * 10` → `inf` (overflow)  
- `1e-324 / 10` → `0.0` (underflow to zero)

---

##### Q17. Why is `0.3 - 0.2 == 0.1` sometimes True but `0.1 + 0.2 == 0.3` False?

**Answer:**  
Their internal binary approximations differ.  
Some operations accumulate rounding error differently.

---

##### Q18. Why is:
```python
float('nan') != float('nan')
```
always True?

**Answer:**  
IEEE-754 rule: NaN is **unordered** and never equal to anything, including itself.

---

##### Q19. Rewrite `0.1 + 0.2` exactly using Decimal.

**Answer:**
```python
from decimal import Decimal
Decimal('0.1') + Decimal('0.2')
```

---

##### Q20. Give an example of accumulated float error in loops.

**Answer:**
```python
x = 0
for i in range(1000):
    x += 0.1
print(x)
```

Output is not 100.0 because rounding error compounds.

---
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)

### EXTRA CHALLENGE (Q&A)

##### Q21. Write code to compare float addition, Decimal, and isclose().

**Answer:**
```python
from decimal import Decimal
import math

print(0.1 + 0.2)
print(Decimal('0.1') + Decimal('0.2'))
print(math.isclose(0.1 + 0.2, 0.3))
```

---

##### Q22. Why are floats stored in binary inside the CPU?

**Answer:**  
- Hardware supports binary arithmetic natively  
- Faster operations  
- Simpler circuitry than decimal floating-point  
- But leads to decimal representation issues  

---

##### Q23. Explain catastrophic cancellation with an example.

**Answer:**
```python
a = 1e16
b = 1
print(a + b - a)
```

Expected: `1`  
Actual: often `0.0` due to loss of low-order bits when adding a tiny number to a huge one.

---

##### Q24. What happens when converting a very large integer to float?

**Answer:**  
- Overflow to `inf` if too large  
- Otherwise, it becomes an imprecise approximation  
- Mantissa stores only first ~15 digits  

---

##### Q25. Show unsafe vs safe float summation.

**Answer:**
```python
import math

nums = [0.1] * 10000

print(sum(nums))       # unsafe: rounding accumulates
print(math.fsum(nums)) # safe: high-precision summation
```

---
[Back to the Table of Contents](002-ch2-float-data.md#table-of-contents)
