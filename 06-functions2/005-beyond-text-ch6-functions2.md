# Beyond the Text: Extended Research Tasks for Chapter 6 (Functions)

The main chapter on functions introduced you to `*args` and `**kwargs`, default arguments, and general function design. This section pushes past the basics with eight self-contained "research tasks" — short investigations that connect what you've learned about functions to real libraries (Matplotlib), to how computers actually store data (endianness), and to a handful of classic algorithms and Python idioms (pseudo-random number generation, iterable unpacking, and brute-force string search).

Each task follows the same pattern: a research question, followed by a model answer with explanation, tables, and a runnable script. You don't need to complete them in order — pick whichever concept you want to explore, work through the question yourself first, and then compare your answer with the model solution given here. Tasks 6 onward use ideas (classes, in Task 6) that are covered later in the book, so feel free to revisit those tasks after finishing the relevant chapter.

---

## Task 1 — Investigate a Real Python Library Function

The plotting function in **Matplotlib** has the following simplified signature:

```python
plot(x, y, *args, **kwargs)
```

### Research Question

Why did the designers of Matplotlib choose `*args` and `**kwargs` here, instead of listing out every possible parameter explicitly? Your explanation should address:

1. What are the **mandatory arguments** in `plot()`?
2. What kinds of values can be passed using **`*args`**?
3. What kinds of options are typically passed using **`**kwargs`**?
4. Why is this design useful when a library **adds new features in later versions**?
5. How does this design help **old programs keep running without modification**?

### Model Answer

You can browse the official signature and options in the [Matplotlib documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html).

#### A. Mandatory arguments

The only two arguments `plot()` truly requires are:

- `x` → the x-coordinates of the points to plot
- `y` → the y-coordinates of the points to plot

```python
plt.plot(x, y)
```

These specify the **data that must be plotted** — without them, there's nothing to draw.

#### B. What `*args` is used for

`*args` collects any extra **positional** arguments. In Matplotlib, this is almost always a single compact **formatting string** that controls color, marker style, and line style all at once:

```python
plt.plot(x, y, "ro--")
```

| Symbol | Meaning |
| --- | --- |
| `r` | red color |
| `o` | circle marker |
| `--` | dashed line |

`*args` is entirely **optional** — if you don't supply one, Matplotlib falls back to its default style (a solid blue line).

#### C. What `**kwargs` is used for

`**kwargs` collects **keyword** arguments — named settings you can mix and match freely:

```python
plt.plot(x, y, color="green", linewidth=3, marker="o")
```

| Parameter | Purpose |
| --- | --- |
| `color` | Line color |
| `linewidth` | Line thickness |
| `marker` | Marker shape |
| `linestyle` | Line pattern |
| `label` | Text shown in the legend |

This is what makes the plot **highly customizable** without needing a separate named parameter for every possible option.

#### D. Why this helps when the library adds new features

Suppose a later version of Matplotlib introduces a brand-new option, say `alpha=0.5` (controlling transparency). Because `plot()` accepts `**kwargs`, it can absorb this new keyword automatically — **no change to the function's signature is required**. Existing code such as:

```python
plt.plot(x, y)
```

keeps working exactly as before, while new code can immediately start using `alpha=0.5` the moment it's documented.

#### E. How this helps backward compatibility

**Backward compatibility** means old programs keep running correctly after a library is updated. Because every new option arrives as an *optional* keyword argument tucked inside `**kwargs`, adding features never breaks a function's existing call sites — it only ever adds new, opt-in behavior on top of what already works.

> **Takeaway:** `*args` and `**kwargs` aren't just a convenience for writing less code — they're a deliberate design choice that lets a library's public API grow over time without ever forcing existing users to rewrite their code.

---

## Task 2 — Documentation Investigation

Visit the official documentation page for `matplotlib.pyplot.plot()` ([link](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)) and find **five keyword arguments** it accepts.

### Model Solution

| Keyword Argument | Purpose |
| --- | --- |
| `color` | Sets the color of the line |
| `linewidth` | Controls the thickness of the line |
| `marker` | Specifies the marker symbol drawn at each data point |
| `linestyle` | Defines the pattern of the line (solid, dashed, dotted, ...) |
| `label` | Provides the text used in the legend |
| `alpha` | Controls transparency (0 = fully transparent, 1 = fully opaque) |
| `markersize` | Controls the size of the markers |
| `markerfacecolor` | Sets the fill color inside each marker |

Example combining several of these:

```python
plt.plot(x, y, color="red", linewidth=2, marker="o")
```

---

## Task 3 — Programming Experiment

Write a program that calls `plot()` in three different ways — using only mandatory arguments, using `*args`, and using `**kwargs` — and observe how each changes the appearance of the plot.

### Model Solution

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

# Case 1: Mandatory arguments only (x, y) — uses Matplotlib's defaults
plt.plot(x, y)

# Case 2: *args — a compact formatting string
# "r" = red, "o" = circle markers, "--" = dashed line
plt.plot(x, y, "ro--")

# Case 3: **kwargs — explicit, named keyword options
plt.plot(x, y, color="green", linewidth=3)

plt.show()
```

*Note: in a real script, each `plot()` call would normally target a separate figure (or use `plt.figure()` between them) so the three styles don't overlap on the same axes — they're shown together here purely to compare the syntax.*

### Explanation

| Case | Code | Result |
| --- | --- | --- |
| 1 | `plt.plot(x, y)` | Default solid blue line, no markers |
| 2 | `plt.plot(x, y, "ro--")` | Red dashed line with circle markers |
| 3 | `plt.plot(x, y, color="green", linewidth=3)` | Thick solid green line |

**Observations:**
- `*args` is best for **quick, compact style shorthand** you can type in a hurry.
- `**kwargs` is best for **precise, self-documenting customization** — `color="green"` is clearer to a reader than a cryptic formatting code.

---

## Task 4 — API Design Thinking

Suppose you're designing a plotting library function yourself. You could write it in two different styles:

**Version A (Rigid) — every option is a named parameter:**

```python
def plot(x, y, color="blue", linewidth=1, marker=None,
         linestyle="-", label=None, grid=False):
    ...
```

**Version B (Flexible) — options are absorbed by `*args`/`**kwargs`:**

```python
def plot(x, y, *args, **kwargs):
    ...
```

### Question

Explain why **Version B is usually preferred in large libraries**, considering flexibility, future extension, backward compatibility, and documentation readability.

### Model Solution

| Feature | Version A (Rigid) | Version B (Flexible) |
| --- | --- | --- |
| Flexibility | Limited to the parameters listed | Very high — accepts anything the implementation chooses to handle |
| Adding new options later | Requires editing the function signature | New options are simply read out of `**kwargs` — no signature change |
| Backward compatibility | Risk of breaking old calls if parameters are reordered or renamed | Old calls are unaffected, since new options are always optional |
| Parameter count | Fixed at design time | Effectively unlimited |
| Documentation readability | Every parameter is visible directly in the signature — easy to read at a glance | The signature alone doesn't show what's accepted; you must consult the docs |

**The trade-off:** Version A is more *discoverable* — an IDE's autocomplete can show you every valid parameter immediately. Version B is more *extensible* — it can absorb new features for years without ever changing its outward signature. This is exactly why large, evolving libraries like Matplotlib favor Version B for their most-used functions, while smaller, stable utility functions in your own code are often better off as Version A, where explicit parameters make misuse easier to catch.

---

## Task 5 — Endianness in Computer Systems

**Endianness** describes the order in which the individual bytes of a multi-byte value (such as a 32-bit integer) are stored in memory. There are two common conventions:

- **Big-endian** — the most significant byte (MSB) is stored first.
- **Little-endian** — the least significant byte (LSB) is stored first.

### Tasks

1. Study big-endian and little-endian byte ordering.
2. Explain the difference with an example — how would `0x12345678` be stored under each convention?
3. Use Python's `sys` module to determine your own system's endianness.
4. Write a script that prints the system's byte order and demonstrates storing a number both ways.

> **Hint:** the `sys` module has an attribute called `sys.byteorder`.

### Model Answer

#### A. Conceptual explanation

When a computer stores a number that's larger than a single byte, it has to decide **which byte to place first in memory**. Consider the 32-bit hexadecimal number:

```
0x12345678
```

This value is made up of four separate bytes: `12`, `34`, `56`, and `78`.

#### B. Big-endian representation

In a big-endian system, the **most significant byte comes first**:

```
Memory order:  12  34  56  78
```

This ordering is sometimes called **network byte order**, because it's the standard used by most network protocols (TCP/IP included).

#### C. Little-endian representation

In a little-endian system, the **least significant byte comes first**:

```
Memory order:  78  56  34  12
```

Most modern desktop and laptop processors — including Intel and AMD x86/x86-64 chips — use little-endian format.

#### D. Detecting endianness in Python

Python exposes this directly through:

```python
sys.byteorder
```

which returns either `"little"` or `"big"`, depending on the machine Python is running on.

#### E. Demonstration script

```python
# Demonstration of endianness in Python.
# Endianness determines the order in which the individual bytes
# of a multi-byte number are stored in memory.

import sys

# sys.byteorder reports the NATIVE byte order of the machine
# this script is currently running on ('little' or 'big').
print("System Byte Order:", sys.byteorder)
print("-" * 40)

# Example integer (fits within 4 bytes / 32 bits)
number = 0x12345678
print("Original number (hex):", hex(number))

# int.to_bytes(length, byteorder) converts an integer into its raw
# byte representation. We ask for 4 bytes since 0x12345678 needs
# exactly 4 bytes (32 bits) to represent it fully.
big_endian_bytes = number.to_bytes(4, byteorder="big")
little_endian_bytes = number.to_bytes(4, byteorder="little")

# In big-endian, the most significant byte (0x12) is stored first.
print("Big-endian byte order:")
print(list(big_endian_bytes))   # [18, 52, 86, 120]  -> 0x12, 0x34, 0x56, 0x78

# In little-endian, the least significant byte (0x78) is stored first.
print("Little-endian byte order:")
print(list(little_endian_bytes))  # [120, 86, 52, 18] -> 0x78, 0x56, 0x34, 0x12

# .hex() gives a compact hexadecimal string view of the same bytes
print("Big-endian (hex):", big_endian_bytes.hex())       # 12345678
print("Little-endian (hex):", little_endian_bytes.hex()) # 78563412
```

> **Why this matters in practice:** endianness becomes important whenever raw bytes cross a boundary — reading a binary file created on a different machine, parsing network packets, or working with low-level formats like images and audio. Get the byte order wrong, and a perfectly valid number turns into nonsense.

---

## Task 6 — Implementing a Pseudo-Random Number Generator

*(This task uses the `class` keyword from Python's Object-Oriented Programming chapter — feel free to return to it after covering OOP if you haven't yet.)*

Most languages' "random" numbers aren't truly random — they're produced by a **Pseudo-Random Number Generator (PRNG)**, a deterministic algorithm that produces a sequence which merely *looks* statistically random. One of the oldest and simplest PRNGs is the **Linear Congruential Generator (LCG)**, defined by the recurrence:

$$X_{n+1} = (a \cdot X_n + c) \bmod m$$

where:

| Symbol | Meaning |
| --- | --- |
| $X_n$ | the current value in the sequence |
| $a$ | the multiplier ($0 < a < m$) |
| $c$ | the increment ($0 < c < m$) |
| $X_0$ | the seed — the starting value |
| $m$ | the modulus, which bounds the range of generated values |

A commonly used set of parameters (borrowed from older C standard libraries) is $m = 2^{31}$, $a = 1103515245$, $c = 12345$.

### Tasks

1. Study PRNGs and how the LCG produces its sequence.
2. Write a Python class that stores the seed and generates the next value via the LCG formula.
3. Add a method that scales the integer output into a float in $[0, 1)$.
4. Demonstrate the generator by printing a few values.

**Questions to think about:** What happens if you change the seed? Why are these numbers called *pseudo*-random rather than truly random?

### Model Solution

```python
# Linear Congruential Generator (LCG) — a simple pseudo-random
# number generator based on the recurrence:
#     X(n+1) = (a * X(n) + c) mod m


class LinearCongruentialGenerator:
    """
    Implements the Linear Congruential Generator algorithm.

    Formula:
        X(n+1) = (a * X(n) + c) mod m

    where:
        X(n) = current internal state (starts at the seed)
        a    = multiplier
        c    = increment
        m    = modulus (bounds every generated value to [0, m))
    """

    def __init__(self, seed=1):
        """Store the LCG parameters and the initial seed."""

        # Standard parameters used in many historical C libraries.
        # Changing these changes the statistical properties of the
        # sequence — they are not arbitrary.
        self.a = 1103515245   # multiplier
        self.c = 12345        # increment
        self.m = 2 ** 31      # modulus

        # 'state' holds the current value in the sequence.
        # It starts out equal to the seed, and is updated
        # every time next_int() is called.
        self.state = seed

    def next_int(self):
        """Generate and return the next integer in the sequence,
        updating the generator's internal state in the process."""

        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def next_float(self):
        """Generate the next value, scaled to a float in [0, 1)."""

        value = self.next_int()
        # Dividing by m maps any value in [0, m) down to [0, 1)
        return value / self.m


# ---------------- Demonstration ----------------

print("Demonstrating Linear Congruential Generator")

# Two independent generators with different seeds
lcg = LinearCongruentialGenerator(seed=123456)
lcg2 = LinearCongruentialGenerator(seed=100)

print("\nFirst 5 pseudorandom integers (seed=123456):")
for i in range(5):
    print(f"X_{i + 1} =", lcg.next_int())

print("\nFirst 5 pseudorandom floats in [0, 1) (seed=100):")
for i in range(5):
    print(round(lcg2.next_float(), 6))
```

### Key Concepts

#### A. Deterministic randomness

Given the **same seed**, an LCG always produces the **exact same sequence** of numbers. `LinearCongruentialGenerator(seed=10)` will output identical values every single time it's run — this is what makes the sequence *reproducible*, which is invaluable for debugging and for scientific results that need to be repeatable.

#### B. Why it's called "pseudo-random"

The output *looks* statistically random — it passes many simple randomness tests — but it's actually generated by a completely deterministic formula. Anyone who knows the seed and the formula can predict every future value exactly. True randomness (e.g. from atmospheric noise or radioactive decay) has no such formula behind it.

#### C. Role of each parameter

| Parameter | Role |
| --- | --- |
| `seed` | The starting value; changing it produces a completely different (but still reproducible) sequence |
| `a` | The multiplier — strongly affects the statistical quality of the sequence |
| `c` | The increment — added on every step |
| `m` | The modulus — controls the range of possible output values |

> **A caution for real use:** the classic LCG shown here is fine for demonstrations, but it is **not suitable for cryptography or security-sensitive randomness** — its output is predictable once a few values are known. For everyday non-cryptographic use, Python's built-in `random` module (based on the far stronger Mersenne Twister algorithm) is the right tool; for anything security-related, use the `secrets` module instead.

---

## Task 7 — Unpacking of Iterables in Python

Python lets you unpack the elements of an iterable (a list, tuple, etc.) directly into separate variables. Normally, the number of variables must match the number of elements exactly. **Partial unpacking**, using a starred (`*`) variable, relaxes that rule by letting one variable absorb *all* the leftover elements — as a list.

### A. Important characteristics

1. A variable prefixed with `*` collects **multiple elements** at once.
2. Those collected elements are always stored as a **list**, regardless of the original iterable's type.
3. Only **one** starred variable is allowed per unpacking statement.
4. It can appear at the **beginning**, **middle**, or **end** of the assignment.

### B. Research Tasks

1. Study how iterable unpacking works.
2. Explain partial unpacking with `*`.
3. Write examples capturing elements at the end, in the middle, and at the beginning.
4. Observe the type of the variable that collects the leftover elements.

### C. Demonstration Script

```python
# Demonstration of partial unpacking of iterables in Python.

# ---- Example 1: catching elements at the end ----
print("Example 1: Catching elements at the end")

# The first two variables take the first two elements;
# the starred variable ('tail') soaks up everything left over.
first, second, *tail = [10, 20, 30, 40, 50]
print("first =", first, "second =", second, "tail =", tail)
# first = 10  second = 20  tail = [30, 40, 50]

print("-----------------------------------")

# ---- Example 2: catching elements in the middle ----
print("Example 2: Catching elements in the middle")

# 'start' takes the first element, 'last' takes the last element,
# and 'middle' collects everything in between.
start, *middle, last = [1, 2, 3, 4, 5, 6]
print("start =", start, "middle =", middle, "last =", last)
# start = 1  middle = [2, 3, 4, 5]  last = 6

print("-----------------------------------")

# ---- Example 3: catching elements at the beginning ----
print("Example 3: Catching elements at the beginning")

# The starred variable can just as easily appear first.
*beginning, second_last, last = [100, 200, 300, 400, 500]
print("beginning =", beginning, "second_last =", second_last, "last =", last)
# beginning = [100, 200, 300]  second_last = 400  last = 500

print("-----------------------------------")

# ---- Example 4: partial unpacking with tuples ----
print("Example 4: Using partial unpacking with tuples")

data = (11, 22, 33, 44, 55)
a, *b = data
print("a =", a, "b =", b)

# Even though 'data' is a tuple, the starred variable 'b' is
# still a list — partial unpacking ALWAYS produces a list,
# regardless of the source iterable's type.
print("Type of b:", type(b))

print("-----------------------------------")

# ---- Example 5: starred variable collecting zero elements ----
print("Example 5: Star variable collecting zero elements")

# There's nothing left over once x and y take their values,
# so 'rest' simply ends up as an empty list — not an error.
x, y, *rest = [5, 10]
print("x =", x, "y =", y, "rest =", rest)
# x = 5  y = 10  rest = []
```

> **Where this shows up in real code:** partial unpacking is especially handy when working with function results of unknown or variable length — for example, separating a header row from the rest of a dataset (`header, *rows = data`), or peeling off the first and last items from a sequence while ignoring the middle (`first, *_, last = values`, where `_` is a conventional "I don't care about this" name).

---

## Task 8 — The Brute-Force String Searching Algorithm

Finding a **pattern** (a short string) inside a larger **text** is one of the most common problems in computer science. The simplest approach is the **brute-force string search**: check every possible position where the pattern *could* start, comparing character by character, and move on as soon as a mismatch is found.

### Basic Idea

Let the text $T$ have length $m$ and the pattern $P$ have length $n$. The algorithm:

1. Aligns the start of $P$ with the first character of $T$.
2. Compares $P$ against the corresponding characters of $T$.
3. If every character matches → the pattern is found at this position.
4. If any character mismatches → slide $P$ one position to the right and try again.
5. Repeat until the pattern is found, or every possible starting position (from index 0 to $m - n$) has been tried.

### Tasks

1. Study the brute-force algorithm.
2. Explain how the pattern slides across the text.
3. Write a function `brute_force_search(text, pattern)` that returns the starting index of the first match, or `-1` if no match exists.
4. Test it on a few example strings.

### Worked Example

For `text1 = "acdabcdacabcd"` and `pattern1 = "cdac"`, here's every alignment the algorithm tries before it finds a match:

| Starting index | Aligned text characters | Match? |
| --- | --- | --- |
| 0 | `acda` vs `cdac` | No — mismatch at the very first character |
| 1 | `cdab` vs `cdac` | No — mismatches on the 4th character (`b` ≠ `c`) |
| 2 | `dabc` vs `cdac` | No — mismatch at the first character |
| 3 | `abcd` vs `cdac` | No — mismatch at the first character |
| 4 | `bcda` vs `cdac` | No — mismatch at the first character |
| 5 | `cdac` vs `cdac` | **Yes — full match** |

So `brute_force_search("acdabcdacabcd", "cdac")` should return `5`.

The following table shows the above process in more details:


  

| Index | Match found? | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| String |  | a | c | d | a | b | c | d | a | c | a | b | c | d |
| Pattern (Initially 0) | No | c | d | a | c |  |  |  |  |  |  |  |  |  |
| 1 | No |  | c | d | a | c |  |  |  |  |  |  |  |  |
| 2 | No |  |  | c | d | a | c |  |  |  |  |  |  |  |
| 3 | No |  |  |  | c | d | a | c |  |  |  |  |  |  |
| 4 | No |  |  |  |  | c | d | a | c |  |  |  |  |  |
| 5 | Yes |  |  |  |  |  | c | d | a | c |  |  |  |  |







### Model Solution

```python
# Brute-force string search algorithm.
# Tries every possible starting position of 'pattern' within 'text',
# comparing character by character and stopping at the first mismatch.

def brute_force_search(text, pattern):
    """
    Search for 'pattern' inside 'text' using the brute-force method.

    Parameters
    ----------
    text : str
        The larger string to search within.
    pattern : str
        The substring being searched for.

    Returns
    -------
    int
        The starting index of the first match, or -1 if the
        pattern does not occur anywhere in the text.
    """

    m = len(text)     # length of the text
    n = len(pattern)  # length of the pattern

    # The pattern can only start at indices 0 .. (m - n) inclusive —
    # beyond that point, there aren't enough characters left in the
    # text for the pattern to fit.
    for i in range(m - n + 1):

        print(f"\nChecking alignment starting at text index {i}")
        match = True  # assume a match until we find evidence otherwise

        # Compare the pattern against the text, one character at a time
        for j in range(n):
            print(f"Comparing text[{i + j}]='{text[i + j]}' "
                  f"with pattern[{j}]='{pattern[j]}'")

            if text[i + j] != pattern[j]:
                print("Mismatch found -> shift pattern to the right")
                match = False
                break  # no point checking the rest of this alignment

        # If the inner loop finished without ever setting match = False,
        # every character lined up — we've found the pattern.
        if match:
            print("Pattern found!")
            return i

    # We tried every possible alignment and never found a full match.
    return -1


# ---------------- Test ----------------

text1 = "acdabcdacabcd"
pattern1 = "cdac"

result = brute_force_search(text1, pattern1)

print("\nFinal Result:")
print("Pattern found at index:", result)
```

**Output:**

```
Checking alignment starting at text index 0
Comparing text[0]='a' with pattern[0]='c'
Mismatch found -> shift pattern to the right

Checking alignment starting at text index 1
Comparing text[1]='c' with pattern[0]='c'
Comparing text[2]='d' with pattern[1]='d'
Comparing text[3]='a' with pattern[2]='a'
Comparing text[4]='b' with pattern[3]='c'
Mismatch found -> shift pattern to the right

Checking alignment starting at text index 2
Comparing text[2]='d' with pattern[0]='c'
Mismatch found -> shift pattern to the right

Checking alignment starting at text index 3
Comparing text[3]='a' with pattern[0]='c'
Mismatch found -> shift pattern to the right

Checking alignment starting at text index 4
Comparing text[4]='b' with pattern[0]='c'
Mismatch found -> shift pattern to the right

Checking alignment starting at text index 5
Comparing text[5]='c' with pattern[0]='c'
Comparing text[6]='d' with pattern[1]='d'
Comparing text[7]='a' with pattern[2]='a'
Comparing text[8]='c' with pattern[3]='c'
Pattern found!

Final Result:
Pattern found at index: 5
```

> **Efficiency note:** in the worst case, brute-force search compares every pattern character against every text position, giving it $O(m \times n)$ time complexity — fine for short strings, but slow on large texts with a lot of repeated characters. Python's built-in `text.find(pattern)` uses a far more optimized algorithm internally and should always be preferred in real code; writing `brute_force_search()` yourself is valuable purely to understand *how* string searching works underneath the hood.

