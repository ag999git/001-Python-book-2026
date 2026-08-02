# Python Data Types

## Table of Contents
* [1. What Is a Python Integer?](001-ch2-python-data-types.md#1-what-is-a-python-integer)
* [2. Arbitrary Precision (Unlimited Size)](001-ch2-python-data-types.md#2-arbitrary-precision-unlimited-size)
* [3. Integer Operations](001-ch2-python-data-types.md#3-integer-operations)
* [4. Bitwise Operations (Advanced Feature)](001-ch2-python-data-types.md#4-bitwise-operations-advanced-feature)
* [5. Advance concept:- Explanation of Bitwise Operation: 10 << 3](001-ch2-python-data-types.md#5-advance-concept--explanation-of-bitwise-operation-10--3)
* [6. Advance concept:- Meaning of the Statement:- “Large integers can be shifted arbitrarily because Python supports arbitrary precision.”](001-ch2-python-data-types.md#6-advance-concept--meaning-of-the-statement--large-integers-can-be-shifted-arbitrarily-because-python-supports-arbitrary-precision)
* [7. Type Conversions](001-ch2-python-data-types.md#7-type-conversions)
* [8. Integer to other types:](001-ch2-python-data-types.md#8-integer-to-other-types)
* [9. Relationship of int with bool (Subclassing)](001-ch2-python-data-types.md#9-relationship-of-int-with-bool-subclassing)
* [10. Interactions of int with float and complex (Type Promotion)](001-ch2-python-data-types.md#10-interactions-of-int-with-float-and-complex-type-promotion)
* [12. Common Pitfalls](001-ch2-python-data-types.md#12-common-pitfalls)
* [13. Advance Concept:- Big Integer Mathematics](001-ch2-python-data-types.md#13-advance-concept--big-integer-mathematics)
* [14. Advance Concept:- Understanding Performance of Integer Operations in Python](001-ch2-python-data-types.md#14-advance-concept--understanding-performance-of-integer-operations-in-python)
*

## Discussion: Python Integers (`int`) (With some advance concepts included)

Python’s `int` type is one of the most powerful integer implementations among modern programming languages.\
Unlike C, C++, or Java, Python integers are **arbitrary-precision**, memory-managed objects with a well-defined internal representation.

This section covers Python `int` in depth.

***

### 1. What Is a Python Integer?

* Represents whole numbers (positive, negative, or zero).
* Entirely implemented in C (CPython) as a structure called `PyLongObject`.
* Immutable: any arithmetic operation creates a new integer object.

```python
x = 10
x = x + 5   # creates a new int object; the old one is unused
```

***
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 2. Arbitrary Precision (Unlimited Size)

Python’s `int` has **no fixed upper limit**.

* Grows automatically as needed.
* Limited only by available RAM.

Examples:

```python
x = 10 ** 1000
#print(x) # If uncommented will give a very large number
print(len(str(x))) # Will give the number of digits ie 1001
```

In languages like C, Java, C++, the size (32-bit, 64-bit) is fixed.\
Python internally uses a dynamic array of machine words to store large integers.

***
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 3. Integer Operations

#### Arithmetic

`+`, `-`, `*`, `//`, `/`, `%`, `**`

Example:

```python
a = 17
b = 5
print(a / b) # 3.4 This will print the float division result
print(a // b) # 3 Floor division.
```

### Floor division always rounds toward `negative infinity`:

```python
print(-15/4) # Output: -3.75
print(15/-4) # Output: -3.75
```

***
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 4. Bitwise Operations (Advanced Feature)

Python supports full bitwise operations:

| Operator | Meaning     |
| -------- | ----------- |
| `&`      | bitwise AND |
| \`       | \`          |
| `^`      | XOR         |
| `~`      | bitwise NOT |
| `<<`     | left shift  |
| `>>`     | right shift |

Example:

```python
print(10 << 3)    # 80
```

[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 5. Advance concept:- Explanation of Bitwise Operation: `10 << 3`

<details>

<summary>5. Advance concept:- Explanation of Bitwise Operation: `10 &#x3C;&#x3C; 3`</summary>

The operator `<<` is the **bitwise left shift** operator.\
It shifts the binary representation of a number **to the left** by a specified number of positions.

***

**Step 1: Convert 10 to binary**

```
10 (decimal) = 1010 (binary)
```

***

**Step 2: Shift left by 3 positions**

`10 << 3` means:

```
1010 << 3 = 1010 000
```

Three zeros are added on the right.

***

**Step 3: Convert result back to decimal**

Binary `1010000` equals:

```
1×64 + 1×16 = 80
```

So:

```
10 << 3 = 80
```

***

**Why it works**

Shifting left by `n` bits is equivalent to multiplying by `2ⁿ`:

```
10 << 3  =  10 × (2³)
         =  10 × 8
         =  80
```

***

**Final Answer**

```
10 << 3 = 80
```

</details>

[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 6. Advance concept:- Meaning of the Statement:- “Large integers can be shifted arbitrarily because Python supports arbitrary precision.”

<details>

<summary>6. Advance concept:- Meaning of the Statement:- “Large integers can be shifted arbitrarily because Python supports arbitrary precision.”</summary>

summary

***

**1. What is arbitrary precision?**

* In many languages (C, C++, Java), integers have a **fixed number of bits** (e.g., 32-bit or 64-bit).
* This means numbers have a maximum possible size.
* Shifting them too far can cause:
  * overflow
  * loss of bits
  * wrap-around
  * undefined behavior

Python is different:

* Python integers have **no fixed size limit**.
* They automatically grow to any size, limited only by available memory.

***

**2. What does “shifted arbitrarily” mean?**

* Bitwise left shift (`<<`) adds zeros to the right side of a binary number.
* In fixed-size languages, shifting too far is impossible or unsafe.
* **In Python, you can shift a number by any number of bits**, even thousands or millions.

Example:

```python
x = 5
y = x << 1000    # shift by 1000 bits
```

This works normally in Python.

***

**3. Example of a large shift**

```python
x = 1
y = x << 200
print(y)
```

Output (a very large integer):

```
1606938044258990275541962092341162602522202993782792835301376
```

Python handles this because it expands the integer size automatically.

***

**4. Why Python can do this**

* Bit shifts generate larger binary numbers.
* Python does not restrict integer size to 32 or 64 bits.
* It creates a larger integer object as needed.
* Therefore, no overflow occurs.

***

**5. Summary**

* Python integers can grow to any size → **arbitrary precision**.
* Bit shifting (`<<`) can be done a limitless number of times.
* Python will automatically allocate more memory to store the larger integer.
* This is why **large integers can be shifted arbitrarily** in Python.

***

</details>

[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 7. Type Conversions

#### Convert to int:

```python
int("123") # string to int because "123" is a valid integer representation
int(" 456 ") # string with whitespace to int
int(3.14) # float -> int (truncates) because 3.14 is a float
int(True) # 1 Since True is 1
int(False) # 0 Since False is 0
int("0b101", 2) # binary string to int because "0b101" is a valid binary representation
int("0o77", 8) # octal string to int because "0o77" is a valid octal representation
int("0x1A", 16) # hexadecimal string to int because "0x1A" is a valid hexadecimal representation
int("-42") # negative string to int because "-42" is a valid integer representation
int("+99") # positive string to int because "+99" is a valid integer representation
int("007") # string with leading zeros to int because "007" is a valid integer representation
int(1e3) # scientific notation float to int (truncates) because 1e3 is a float
# Following if uncommented will raise exception
#int("") # raises ValueError because empty string cannot be converted to int
#int("abc") # raises ValueError because "abc" is not a valid integer representation
#int(None) # raises TypeError because None cannot be converted to int
#int([]) # raises TypeError because empty list cannot be converted to int
#int([1, 2]) # raises TypeError because non-empty list cannot be converted to int

```

[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 8. Integer to other types:

```python
print(float(5)) # 5.0 because int can be converted to float
print(complex(3)) # (3+0j) # int promoted to complex
print(str(123)) # "123" # int to string
```

***

[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 9. Relationship of int with `bool` (Subclassing)

In Python:

```
bool is a subclass of int
```

```python
print(issubclass(bool, int)) # True Since bool is a subclass of int
print(isinstance(True, int)) # True Since True is an instance of int
print(isinstance(False, int)) # True Since False is an instance of int
print(True + 1) # 2 Since True is 1
print(False + 1) # 1 Since False is 0
print(True * 10) # 10 Since True is 1
print(False * 10) # 0 Since False is 0
print(int(True)) # 1 Since True is 1
print(int(False)) # 0 Since False is 0
print(bool(1)) # True Since 1 is non-zero
print(bool(0)) # False Since 0 is zero
print(bool(-1)) # True Since -1 is non-zero
print(bool(0.0)) # False Since 0.0 is zero
print(bool(0.1)) # True Since 0.1 is non-zero
print(bool([])) # False Since empty list is False
print(bool([1, 2, 3])) # True Since non-empty list is True
print(bool("")) # False Since empty string is False
print(bool("Hello")) # True Since non-empty string is True
print(bool(None)) # False Since None is False
print(bool(object())) # True Since object instance is True
print(True == 1) # True Since True is 1
print(False == 0) # True Since False is 0
print(True  is  1) # False Since True and 1 are different objects
print(False  is  0) # False Since False and 0 are different objects
print(True > False) # True Since True is greater than False
print(False < True) # True Since False is less than True
print(sum([True, False, True, True])) # 3 Since True is 1 and False is 0
print([True, False, True].count(True)) # 2 Count of True in the list
print([True, False, True].count(False)) # 1 Count of False in the list
print([True, False, True].index(False)) # 1 Index of first occurrence of False
print(True.__class__) # <class 'bool'> Since True is an instance of bool
print(False.__class__) # <class 'bool'> Since False is an instance of bool
print(repr(True)) # 'True' Since repr(True) returns the string 'True'
print(repr(False)) # 'False' Since repr(False) returns the string 'False'
print(str(True)) # 'True' Since str(True) returns the string 'True'
print(str(False)) # 'False' Since str(False) returns the string 'False'
print(hash(True)) # 1 Since hash(True) returns 1
print(hash(False)) # 0 Since hash(False) returns 0
print(bin(int(True))) # '0b1' Since bin(int(True)) returns the binary representation of 1
print(bin(int(False))) # '0b0' Since bin(int(False)) returns the binary representation of 0
print(hex(int(True))) # '0x1' Since hex(int(True)) returns the hexadecimal representation of 1
print(hex(int(False))) # '0x0' Since hex(int(False)) returns the hexadecimal representation of 0
print(oct(int(True))) # '0o1' Since oct(int(True)) returns the octal representation of 1
print(oct(int(False))) # '0o0' Since oct(int(False)) returns the octal representation of 0
print(True.__and__(False)) # False Since True AND False is False
print(True.__or__(False)) # True Since True OR False is True
print(True.__xor__(False)) # True Since True XOR False is True
print(False.__and__(True)) # False Since False AND True is False
print(False.__or__(True)) # True Since False OR True is True
print(False.__xor__(True)) # True Since False XOR True is True
print(True.bit_length()) # 1 Since bit length of 1 is 1
print(False.bit_length()) # 0 Since bit length of 0 is 0
print((True, False)) # (True, False) Since this is a tuple containing True and False
print([True, False]) # [True, False] Since this is a list containing True and False
print({True: "yes", False: "no"}) # {True: 'yes', False: 'no'} Since this is a dictionary with boolean keys
print({True, False}) # {False, True} Since this is a set containing True and False
print(len({True, False})) # 2 Since the set has two elements
print(sorted([False, True, True, False])) # [False, False, True, True] Since the list is sorted
print(all([True, True, True])) # True Since all elements are True
print(all([True, False, True])) # False Since not all elements are True
print(any([False, False, False])) # False Since no elements are True
print(any([False, True, False])) # True Since at least one element is True
print(map(int, [True, False, True])) # <map object> Since map returns a map object
print(list(map(int, [True, False, True]))) # [1, 0, 1] Since list converts map to a list
print(filter(bool, [0, 1, "", "Hello", [], [1]])) # <filter object> Since filter returns a filter object
print(list(filter(bool, [0, 1, "", "Hello", [], [1]]))) # [1, 'Hello', [1]] Since list converts filter to a list
print(zip([True, False], [1, 0])) # <zip object> Since zip returns a zip object
print(list(zip([True, False], [1, 0]))) # [(True, 1), (False, 0)] Since list converts zip to a list
print(divmod(5, True)) # (5, 0) Since divmod returns quotient and remainder
#print(divmod(5, False)) # Raises ZeroDivisionError Since dividing by False (zero) is not allowed
try:
    print(divmod(5, False))
except  ZeroDivisionError:
    print("Cannot divide by False (zero)")
 
print(pow(2, True)) # 2 Since 2 raised to the power of True (1) is 2
print(pow(2, False)) # 1 Since 2 raised to the power of False (0) is 1
print(abs(True)) # 1 Since absolute value of True (1) is 1
print(abs(False)) # 0 Since absolute value of False (0) is 0
print(round(True)) # 1 Since rounding True (1) is 1
print(round(False)) # 0 Since rounding False (0) is 0
print(float(True)) # 1.0 Since float conversion of True (1) is 1.0
print(float(False)) # 0.0 Since float conversion of False (0) is 0.0
print(complex(True)) # (1+0j) Since complex conversion of True (1) is (1+0j)
print(complex(False)) # 0j Since complex conversion of False (0) is 0j
print(divmod(5, True)) # (5, 0) Since divmod returns quotient and remainder
#print(divmod(5, False)) # Raises ZeroDivisionError Since dividing by False (zero) is not allowed

```

Meaning:

* `True` behaves as `1`
* `False` behaves as `0`

***
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 10. Interactions of int with float and complex (Type Promotion)

Python uses numeric tower widening:

```
int → float → complex
```

Examples:

```python
print(5 + 2.5) # 7.5 int promoted to float
print(5 + 2j) # (5+2j) int promoted to complex
```

#### 10.1 What is Numeric tower widening in Python?

> When Python performs arithmetic between numbers of **different types**, it automatically converts (“promotes”) the smaller, simpler type into the larger, more capable type **so that the operation makes sense and no information is lost**.

Python follows this hierarchy:

`int → float → complex`

This is called the **numeric tower**.

***

***
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### Advance Concept:- 11. Memory Usage

Memory increases with size of the integer.

Approximate formula:

```
24 bytes + 30 bits per digit (on 64-bit systems)
```

Example:

```python
import  sys
print(sys.getsizeof(10**100)) # Gives size of a large integer in bytes
print(sys.getsizeof(-10**100)) # Gives size of a large negative integer in bytes
print(10**1000) # Prints a very large integer
print(-10**1000) # Prints a very large negative integer
print(10**1000 + 10**999) # Addition of large integers
print(10**1000 - 10**999) # Subtraction of large integers
print(10**1000 * 10**999) # Multiplication of large integers
print(10**1000 // 10**999) # Floor division of large integers
print(10**1000 % 10**999) # Modulus of large integers
print(pow(10**100, 2)) # Power of a large integer
print(divmod(10**1000, 10**999)) # Divmod of large integers
print(10**1000 == 10**1000) # Equality comparison of large integers
print(10**1000 > 10**999) # Greater than comparison of large integers
print(10**1000 < 10**999) # Less than comparison of large integers
print(hash(10**1000)) # Hash of a large integer
print(abs(-10**1000)) # Absolute value of a large negative integer
print(bin(10**10)) # Binary representation of a large integer
print(oct(10**10)) # Octal representation of a large integer
print(hex(10**10)) # Hexadecimal representation of a large integer
print(int("123456789012345678901234567890")) # String to large int conversion
print(int("-123456789012345678901234567890")) # String to large negative int conversion
print(int(" 456789012345678901234567890 ")) # String with whitespace to large int conversion
print(int(1e20)) # Float to large int conversion (truncates)
print(int(True)) # True to int conversion
print(int(False)) # False to int conversion
print(int("0b" + "1"*100)) # Large binary string to int conversion
print(int("0o" + "7"*100)) # Large octal string to int conversion
print(int("0x" + "F"*100)) # Large hexadecimal string to int conversion
print(int("+" + "9"*100)) # Large positive string to int conversion
print(int("-" + "9"*100)) # Large negative string to int conversion
print(int("0"*100 + "1")) # Large string with leading zeros to int conversion
# The following lines would raise exceptions if uncommented
# print(int("")) # Raises ValueError
# print(int("abc")) # Raises ValueError
# print(int(None)) # Raises TypeError
# print(int([])) # Raises TypeError
# print(int([1, 2])) # Raises TypeError
print(sys.getsizeof(int("9"*1000))) # Size of a very large integer created from string
print(int("9"*1000) + 1) # Addition with a very large integer created from string
print(int("9"*1000) * 2) # Multiplication with a very large integer created from string
print(int("9"*1000) // 3) # Floor division with a very large integer created from string
print(int("9"*1000) % 7) # Modulus with a very large integer created from string
print(pow(int("9"*500), 2)) # Power of a very large integer created from string
print(divmod(int("9"*1000), 8)) # Divmod with a very large integer created from string
print(int("9"*1000) == int("9"*1000)) # Equality comparison of very large integers
print(int("9"*1000) > int("8"*1000)) # Greater than comparison of very large integers
print(int("9"*1000) < int("10"*999)) # Less than comparison of very large integers
print(hash(int("9"*1000))) # Hash of a very large integer created from string
print(abs(-int("9"*1000))) # Absolute value of a very large negative integer created from string
print(bin(int("9"*20))) # Binary representation of a very large integer created from string
print(oct(int("9"*20))) # Octal representation of a very large integer created from string
print(hex(int("9"*20))) # Hexadecimal representation of a very large integer created from string
# The following lines would raise exceptions if uncommented
# print(int("0b2", 2)) # Raises ValueError
# print(int("0o8", 8)) # Raises ValueError
# print(int("0xG", 16)) # Raises ValueError
# print(int("12AB", 10)) # Raises ValueError
# print(int("++123")) # Raises ValueError
# print(int("--123")) # Raises ValueError
# print(int("00A7")) # Raises ValueError
# print(int(1e400)) # Raises OverflowError
# print(int([])) # Raises TypeError
# print(int({1: 'a'})) # Raises TypeError
print(int("0b" + "1"*100, 2)) # Large binary string to int conversion with base
print(int("0o" + "7"*100, 8)) # Large octal string to int conversion with base
print(int("0x" + "F"*100, 16)) # Large hexadecimal string to int conversion with base
print(int("+" + "9"*100)) # Large positive string to int conversion
print(int("-" + "9"*100)) # Large negative string to int conversion
print(int("0"*100 + "1")) # Large string with leading zeros to int conversion
# The following lines would raise exceptions if uncommented
# print(int("0b2", 2)) # Raises ValueError
# print(int("0o8", 8)) # Raises ValueError
# print(int("0xG", 16)) # Raises ValueError
# print(int("12AB", 10)) # Raises ValueError
# print(int("++123")) # Raises ValueError
# print(int("--123")) # Raises ValueError
# print(int("00A7")) # Raises ValueError
```

***
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 12. Common Pitfalls

#### 12.1 Confusing `/` and `//`

```python
print(5 / 2) # 2.5 float
print(5 // 2) # 2 int
```

#### 12.2 Expecting fixed-size integers (Python does not overflow)

```python
print(2**200) #1606938044258990275541962092341162602522202993782792835301376
```

***
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### 13. Advance Concept:- Big Integer Mathematics

<details>

<summary>13. Advance Concept:- Big Integer Mathematics</summary>

Python’s `int` supports:

* exact big integer arithmetic
* modular arithmetic
* number-theoretic functions via libraries like `math` and `sympy`

Examples:

```python
pow(a, b, mod)  # fast modular exponentiation
```

***

**Summary**

* Python `int` is **arbitrary precision**, immutable, and extremely flexible.
* Implemented in C using dynamic arrays of machine words.
* Supports caching, bitwise arithmetic, type widening, and conversion.
* Much more powerful and safer than fixed-size integers in compiled languages.

***

</details>
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)


### 14. Advance Concept:- Understanding Performance of Integer Operations in Python

<details>

<summary>14. Advance Concept:- Understanding Performance of Integer Operations in Python</summary>

summary

Python's `int` is very powerful because it supports **arbitrary precision**—integers can grow to any size.\
However, performance differs between **small** and **large** integers because of how they are stored and processed internally.

***

**1. Small integers: Very fast due to caching**

* Python pre-allocates and stores (“caches”) all integers in the range **−5 to 256**.
* These integers are created once at startup and **reused** throughout the program.
* Any time you create an integer in this range, Python does **not** allocate new memory.

Example:

```python
a = 100
b = 100
a is b     # True — both refer to the same cached object
```

**Why this is fast:**

* No memory allocation.
* No object creation.
* Python simply returns a reference to the cached integer.

This makes operations on small integers extremely efficient.

***

**2. Large integers: Slower operations (O(n), O(n²), sometimes O(n log n))**

When integers get large (hundreds or thousands of digits):

* They no longer fit in a single machine word.
* Python must store them as **arrays of digits** (base 2³⁰ or 2¹⁵ chunks internally).
* Arithmetic must operate on **multiple chunks**, not one CPU instruction.

**Advance Concept:- Complexity overview**

| Operation                  | Time complexity                       | Reason                                                |
| -------------------------- | ------------------------------------- | ----------------------------------------------------- |
| Addition, subtraction      | **O(n)**                              | Must process all “digits” of large numbers            |
| Comparison                 | **O(n)**                              | Must compare digit-by-digit from most significant end |
| Multiplication             | **O(n²)** for normal method           | Every digit interacts with every digit                |
| Multiplication (optimized) | **O(n log n)** with better algorithms | Python switches for large values                      |

Where:

* **n = number of internal digits**, not decimal digits.

Thus, very large integers behave like big sequences, not like primitive machine integers.

***

**Advance Concept:- Multiplication uses optimized algorithms internally**

Python uses different multiplication algorithms depending on the size of the integers.

**a) Karatsuba algorithm (for medium-sized numbers)**

* Faster than the standard grade-school multiplication.
* Complexity: **O(n^1.585)**
* Used when integers have around **20–70 digits** (range varies).

Karatsuba divides numbers into parts and reduces the total multiplications needed.

**b) FFT-based multiplication (for extremely large numbers)**

When numbers become extremely large (thousands of digits), Python uses algorithms based on:

* **FFT (Fast Fourier Transform)**
* Schönhage–Strassen algorithm
* (Newer versions of Python may use Fürer-like algorithms)

Complexity: approximately **O(n log n)** or better.

These advanced algorithms treat multiplication like polynomial convolution using FFT.

***

</details>

[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

### Advance Concept:- Internal Representation (CPython)

CPython stores integers using a structure:

```
PyLongObject:
    - reference count
    - type information
    - number of "digits" in base 2^30 or 2^15 (depending on build)
```

Key notes:

* “digits” are base-2³⁰ chunks (on 64-bit systems).
* Large integers use multiple digits.
* Thus, computing with huge numbers is slower but exact (no overflow).

***

***
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)


### Summary of small versus large integer usage in Python

* **Small integers** are extremely fast because Python reuses them from a cache.
* **Large integers** require more memory and multi-chunk operations, leading to slower performance.
* Python automatically chooses optimal multiplication algorithms depending on size:
  * Standard or Karatsuba for mid-sized numbers
  * FFT-based algorithms for huge numbers
 
[Back to the Table of Contents](001-ch2-python-data-types.md#table-of-contents)

This combination allows Python to support massive integers while still keeping performance as efficient as possible.
