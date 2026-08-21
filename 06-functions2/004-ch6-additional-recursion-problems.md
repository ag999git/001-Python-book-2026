# Additional Problems on Recursion

This chapter builds on the introduction to recursion given earlier in the book. There, you learned the two ingredients every recursive function needs — a **base case** (the condition that stops the recursion) and a **recursive case** (where the function calls itself on a smaller version of the problem).

Here, that idea is applied to five classic problems: computing powers, checking palindromes, finding the GCD, solving the Tower of Hanoi, and testing whether a number is even. Each problem is solved two ways where useful — a recursive way (to build your understanding of recursion) and the simple, everyday Python way (so you know what to actually use in real code). Working through all five will make the *pattern* of recursive thinking — reduce the problem, trust the smaller call, combine the results — feel natural well beyond these specific examples.

---

## 1. Recursive Function to Compute $a^b$

A natural example of recursion is computing $a^{b}$, where $a$ (the base) and $b$ (a non-negative integer exponent).

For example:

$$2^5 = 2 \times 2 \times 2 \times 2 \times 2 = 32$$

The recursive definition mirrors the mathematical one exactly:

$$
a^b =
\begin{cases}
1 & \text{if } b = 0 \\
a \times a^{(b-1)} & \text{if } b > 0
\end{cases}
$$

In words: *"a to the power b" is just a multiplied by "a to the power (b − 1)"* — a smaller version of the same problem — and the recursion bottoms out when the exponent hits 0.

**Key components of the recursive algorithm**

| Component | Description |
| --- | --- |
| Base case | When $b = 0$, return 1 |
| Recursive case | Multiply $a$ by the result of $a^{(b-1)}$ |
| Progress toward base case | The exponent decreases by 1 on every call |

```python
# Recursive function to compute a^b (base raised to exponent).
# The exponent is reduced by 1 on every recursive call,
# until the base case (exponent = 0) is reached.

def power_recursive(base, exponent):
    """Return base raised to the power exponent, using recursion."""

    # ---------- BASE CASE ----------
    # Any number raised to the power 0 is equal to 1
    if exponent == 0:
        print("Reached base case: exponent = 0 -> returning 1")
        return 1

    # ---------- RECURSIVE CASE ----------
    # Call the function again with the exponent reduced by 1
    print(f"Computing {base}^{exponent} -> calling {base}^{exponent - 1}")
    partial_result = power_recursive(base, exponent - 1)

    # Multiply base by the value returned from the recursive call
    result = base * partial_result

    # Show the computation as the recursion "unwinds" (returns)
    print(f"Returning: {base}^{exponent} = {base} x {partial_result} = {result}")
    return result


# Test cases: each tuple holds (base, exponent)
test_cases = [
    (2, 5),   # 2^5 = 32
    (3, 4),   # 3^4 = 81
    (5, 0),   # 5^0 = 1
    (7, 1),   # 7^1 = 7
    (4, 3),   # 4^3 = 64
]

for base, exponent in test_cases:
    print("\n----------------------------------")
    print(f"Computing {base}^{exponent}")
    result = power_recursive(base, exponent)
    print(f"Final Result: {base}^{exponent} = {result}")
```

> **In real code:** Python already gives you this via the built-in `base ** exponent` or `pow(base, exponent)`. Writing `power_recursive()` is a learning exercise, not something you'd use in production — but the pattern (multiply by a smaller version of the same call) reappears constantly in recursive algorithms.

---

## 2. Using Recursion to Check Whether a String Is a Palindrome

A **palindrome** is a word, phrase, or sequence of characters that reads the same forwards and backwards — for example `madam`, `level`, and `racecar`.

**Idea behind the recursive solution:** a string is a palindrome if

1. its first and last characters match, **and**
2. the substring left after removing those two characters is *also* a palindrome.

Tracing `"madam"`:

```
madam
 ↑   ↑        first ('m') == last ('m')  →  check the middle: "ada"

 ada
  ↑           first ('a') == last ('a')  →  check the middle: "d"

 d             length 1 → automatically a palindrome (base case)
```

**Recursive logic**

| Condition | Result |
| --- | --- |
| Length ≤ 1 | Palindrome (base case) |
| First character ≠ last character | Not a palindrome |
| First character = last character | Recursively check the inner substring |

The recursion keeps shrinking the string by one character from each end until it becomes empty or a single character — at which point it's trivially a palindrome.

##### Recursive Python Implementation

```python
# Recursive function to check whether a string is a palindrome.
# A palindrome reads the same forward and backward.

def is_palindrome(text):
    """Return True if text is a palindrome, otherwise False."""

    # ---------- BASE CASE ----------
    # A string of length 0 or 1 is always a palindrome
    if len(text) <= 1:
        return True

    # ---------- MISMATCH CHECK ----------
    # If the outer characters differ, it can never be a palindrome,
    # so we can stop immediately without checking further
    if text[0] != text[-1]:
        return False

    # ---------- RECURSIVE CASE ----------
    # Outer characters match, so strip them off
    # and recursively test what's left in the middle
    inner_text = text[1:-1]
    return is_palindrome(inner_text)


# Testing the palindrome function
print(is_palindrome("level"))            # True
print(is_palindrome("madam"))            # True
print(is_palindrome("racecar"))          # True
print(is_palindrome("python"))           # False
print(is_palindrome("neveroddoreven"))   # True
print(is_palindrome(""))                 # True  (empty string)
print(is_palindrome("a"))                # True  (single character)
```

#### Optional Improvement (Often Done in Real Programs)

Real programs usually want to treat phrases like `"Never Odd Or Even"` as palindromes too, ignoring spaces and letter case. To do that, normalize the string *before* checking it:

```python
text = text.lower().replace(" ", "")   # lowercase + remove spaces
```

Add this line at the top of `is_palindrome()` (before the base-case check) if you want the function to ignore spacing and capitalization.

---

## 3. Recursive Function to Find the GCD (Greatest Common Divisor)

The **Greatest Common Divisor (GCD)** of two integers is the largest positive integer that divides both of them exactly.

For example, to find $\gcd(48, 18)$: the common divisors of 48 and 18 are $1, 2, 3, 6$ — and the largest of these is 6. So $\gcd(48, 18) = 6$.

##### Euclid's Algorithm

One of the most efficient ways to compute the GCD is **Euclid's Algorithm**, based on the identity:

$$\gcd(a, b) = \gcd(b, \ a \bmod b)$$

where $a \bmod b$ is the remainder when $a$ is divided by $b$. Each step replaces the pair $(a, b)$ with the smaller pair $(b, a \bmod b)$, and the recursion continues until the remainder becomes 0. At that point:

$$\gcd(a, 0) = a$$

This is the base case of the recursion.

**Worked example**

```
gcd(48, 18)
= gcd(18, 48 % 18)   = gcd(18, 12)
= gcd(12, 18 % 12)   = gcd(12, 6)
= gcd(6,  12 % 6)    = gcd(6, 0)

gcd(6, 0) = 6   →   GCD = 6
```

##### Recursive Python Implementation

```python
# Recursive function to compute the GCD of two integers
# using Euclid's Algorithm.

def gcd_recursive(a, b):
    """Return the greatest common divisor of a and b using recursion."""

    # ---------- BASE CASE ----------
    # When b becomes 0, a itself is the GCD
    if b == 0:
        print(f"Base case reached: gcd({a}, 0) = {a}")
        return a

    # ---------- RECURSIVE CASE ----------
    # Replace (a, b) with (b, a % b) and call the function again
    remainder = a % b
    print(f"gcd({a}, {b}) -> gcd({b}, {remainder})")
    return gcd_recursive(b, remainder)


# Test calls
print(f"GCD(48, 18) = {gcd_recursive(48, 18)}")   # 6
print(f"GCD(100, 75) = {gcd_recursive(100, 75)}")  # 25
print(f"GCD(17, 5)  = {gcd_recursive(17, 5)}")    # 1  (co-prime numbers)
```

> **In real code:** Python's standard library already provides this as `math.gcd(a, b)`. As with `power_recursive()` above, writing it yourself is valuable purely for understanding *how* Euclid's Algorithm works step by step.

The diagram below illustrates Euclid's Algorithm for computing $\gcd(48, 18)$, with numbered blocks so you can follow the flow step by step.

![GCD recursion flowchart](https://github.com/ag999git/001-Python-book-2026/raw/main/resources/ch-6-functions2-gcd-recursion.png)

**What each block in the flowchart does**

| Block No. | Block Description | What Happens in This Step | Example |
| --- | --- | --- | --- |
| 1 | Start | Begin the algorithm with two numbers `a` and `b` whose GCD we want to find. | `gcd(48, 18)` |
| 2 | Check if b = 0 | This is the base condition — if `b = 0`, the algorithm stops. | Check if `18 = 0` |
| 3 | Compute remainder | Calculate the remainder when `a` is divided by `b`, using the modulo operator `%`. | `48 % 18 = 12` |
| 4 | Recursive call | Replace `a` with `b`, and `b` with the remainder, then call the function again. | `gcd(18, 12)` |
| 5 | Repeat process | Keep repeating the same steps until `b` becomes 0. | `gcd(12, 6) → gcd(6, 0)` |
| 6 | Return result | When `b = 0`, the current value of `a` is the GCD. | `gcd(6, 0) = 6` |

---

## 4. Recursive Function to Implement the Tower of Hanoi

The full recursive solution to the Tower of Hanoi is explained in detail earlier in the book. This section adds a complete move-by-move trace and a line-by-line breakdown of the script, so you can see exactly how the recursion unfolds.

#### Complete Table of Tower of Hanoi States for 5 Disks

**Conventions used:**
- Source = A, Auxiliary = B, Destination = C
- Each list shows disks from **largest → smallest**, read **left → right**
- Move 0 = initial state, Move 31 = final solved state

| Move | Disk Moved | Direction | A (Source) | B (Aux) | C (Dest) |
| --- | --- | --- | --- | --- | --- |
| 0 | – | Initial | [5,4,3,2,1] | [] | [] |
| 1 | 1 | A→C | [5,4,3,2] | [] | [1] |
| 2 | 2 | A→B | [5,4,3] | [2] | [1] |
| 3 | 1 | C→B | [5,4,3] | [2,1] | [] |
| 4 | 3 | A→C | [5,4] | [2,1] | [3] |
| 5 | 1 | B→A | [5,4,1] | [2] | [3] |
| 6 | 2 | B→C | [5,4,1] | [] | [3,2] |
| 7 | 1 | A→C | [5,4] | [] | [3,2,1] |
| 8 | 4 | A→B | [5] | [4] | [3,2,1] |
| 9 | 1 | C→B | [5] | [4,1] | [3,2] |
| 10 | 2 | C→A | [5,2] | [4,1] | [3] |
| 11 | 1 | B→A | [5,2,1] | [4] | [3] |
| 12 | 3 | C→B | [5,2,1] | [4,3] | [] |
| 13 | 1 | A→C | [5,2] | [4,3] | [1] |
| 14 | 2 | A→B | [5] | [4,3,2] | [1] |
| 15 | 1 | C→B | [5] | [4,3,2,1] | [] |
| 16 | 5 | A→C | [] | [4,3,2,1] | [5] |
| 17 | 1 | B→A | [1] | [4,3,2] | [5] |
| 18 | 2 | B→C | [1] | [4,3] | [5,2] |
| 19 | 1 | A→C | [] | [4,3] | [5,2,1] |
| 20 | 3 | B→A | [3] | [4] | [5,2,1] |
| 21 | 1 | C→B | [3] | [4,1] | [5,2] |
| 22 | 2 | C→A | [3,2] | [4,1] | [5] |
| 23 | 1 | B→A | [3,2,1] | [4] | [5] |
| 24 | 4 | B→C | [3,2,1] | [] | [5,4] |
| 25 | 1 | A→C | [3,2] | [] | [5,4,1] |
| 26 | 2 | A→B | [3] | [2] | [5,4,1] |
| 27 | 1 | C→B | [3] | [2,1] | [5,4] |
| 28 | 3 | A→C | [] | [2,1] | [5,4,3] |
| 29 | 1 | B→A | [1] | [2] | [5,4,3] |
| 30 | 2 | B→C | [1] | [] | [5,4,3,2] |
| 31 | 1 | A→C | [] | [] | [5,4,3,2,1] |

Note that a 5-disk puzzle takes $2^5 - 1 = 31$ moves in total — which matches the last row above.

##### The Full Script

```python
# Tower of Hanoi, using three lists to represent towers A, B, and C.
# Each list behaves like a stack:
#   - the LEFTMOST item is the BOTTOM of the tower (the biggest disk)
#   - the RIGHTMOST item is the TOP of the tower (the smallest disk)
# The script also counts and displays the move number for each step.

def print_towers(towers):
    """Display the current state of all three towers."""
    print(f"A: {towers['A']}   B: {towers['B']}   C: {towers['C']}")
    print("-" * 40)


def move_disk(towers, source, target, move_counter):
    """Move the top disk from 'source' tower to 'target' tower,
    and update the shared move counter."""

    disk = towers[source].pop()      # Remove top disk from source
    towers[target].append(disk)      # Place it on top of target

    move_counter[0] += 1             # Increment the shared move count

    print(f"Move {move_counter[0]}: disk from {source} -> {target}")
    print_towers(towers)


def hanoi_recursive(n, source, target, auxiliary, towers, move_counter):
    """
    Recursive solution to the Tower of Hanoi.

    n            -> number of disks still to move
    source       -> tower the disks start on      (A/B/C)
    target       -> tower the disks must end up on (A/B/C)
    auxiliary    -> the spare tower used along the way (A/B/C)
    towers       -> dictionary storing the three towers
    move_counter -> single-item list used to track total moves
                    (see note below on why this is a list, not an int)
    """

    # -------- BASE CASE --------
    # Only one disk left: move it directly, no further recursion needed
    if n == 1:
        move_disk(towers, source, target, move_counter)
        return

    # -------- RECURSIVE CASE --------
    # Step 1: move the top (n - 1) disks out of the way, onto auxiliary
    hanoi_recursive(n - 1, source, auxiliary, target, towers, move_counter)

    # Step 2: move the single largest remaining disk to its final spot
    move_disk(towers, source, target, move_counter)

    # Step 3: move the (n - 1) disks from auxiliary onto target,
    #         completing the stack on top of the disk placed in Step 2
    hanoi_recursive(n - 1, auxiliary, target, source, towers, move_counter)


# ---------------- INITIAL SETUP ----------------

num_disks = 3

# Tower A starts with all disks, largest on the left (bottom)
# down to smallest on the right (top). B and C start empty.
initial_state_A = list(range(num_disks, 0, -1))
towers = {"A": initial_state_A, "B": [], "C": []}

# move_counter is a one-item list (not a plain int) so that every
# recursive call can update the *same* counter — see the explanation below.
move_counter = [0]

print("Initial State")
print_towers(towers)

# Solve the puzzle: move all disks from A to C, using B as the spare
hanoi_recursive(num_disks, "A", "C", "B", towers, move_counter)

print(f"Total moves required: {move_counter[0]}")
```

#### Line-by-Line Discussion of the Script

##### How the towers are represented

The towers are plain Python lists, where the **left side is the bottom** and the **right side is the top**:

```python
# Example initial state for 3 disks:
# A: [3, 2, 1]   ->  3 (largest, at the bottom)
#                    2
#                    1 (smallest, at the top)
# B: []
# C: []
```

They're grouped together in a dictionary so each tower can be referred to by name:

```python
towers = {"A": initial_state_A, "B": [], "C": []}
# Access individual towers as towers["A"], towers["B"], towers["C"]
```

##### `print_towers()`

Displays the current configuration of all three towers, so you can visually follow how the disks move after every step.

##### `move_disk()`

Moves exactly one disk from a `source` tower to a `target` tower, and updates the shared move counter.

| Parameter | Meaning |
| --- | --- |
| `towers` | dictionary containing the three towers |
| `source` | tower the disk is removed from |
| `target` | tower the disk is placed onto |
| `move_counter` | shared counter tracking the number of moves so far |

Since Python lists behave like stacks:
- `towers[source].pop()` removes and returns the **top** (last) item of the list — the smallest, topmost disk.
- `towers[target].append(disk)` places that disk on **top** of the target tower.

##### Why `move_counter` is a list, not a plain integer

`move_counter = [0]` looks unusual — why not just use an integer? The reason is that **integers are immutable** in Python: if you passed a plain `int` into a recursive function and incremented it there, each recursive call would get its *own* copy, and the changes wouldn't be visible to the other calls once they returned.

A **list is mutable**, so every recursive call receives a reference to the *same* list. When any call does `move_counter[0] += 1`, that change is visible to every other call sharing the same list — giving all of them a single, correctly-shared move count.

##### `hanoi_recursive()` — the core algorithm

| Parameter | Meaning |
| --- | --- |
| `n` | number of disks still to move |
| `source` | tower the disks start on |
| `target` | tower the disks must end up on |
| `auxiliary` | spare tower used temporarily during the move |
| `towers` | dictionary storing the towers |
| `move_counter` | shared counter tracking total moves |

**Base case:**

```python
if n == 1:
    move_disk(...)
```

If only one disk remains, it's moved directly from `source` to `target`, and the recursion for this branch stops.

**Recursive case — three steps:**

| Step | What Happens | Example (3 disks, A→C via B) |
| --- | --- | --- |
| 1 | Move the top $n-1$ disks from `source` to `auxiliary` (out of the way) | Move disks 1 and 2 from A → B |
| 2 | Move the single largest disk from `source` to `target` | Move disk 3 from A → C |
| 3 | Move the $n-1$ disks from `auxiliary` onto `target` | Move disks 1 and 2 from B → C |

##### Overall flow of the program

```
Initial state printed
        ↓
hanoi_recursive() called
        ↓
Problem repeatedly broken down (recursive Step 1, then Step 3)
        ↓
Each individual disk moved via move_disk() (recursive Step 2 / base case)
        ↓
Towers printed after every move
        ↓
Final state reached, all disks on tower C
        ↓
Total moves displayed
```

---

## 5. Recursive Function to Test Whether a Number Is Even (Not Very Efficient)

Even/odd testing can also be done recursively — mainly as an exercise in recursive thinking, not because it's a good way to solve the problem.

> **Tip:** This method is useful **for learning recursion**, not for efficiency. In real code, always use the modulus operator: `n % 2 == 0`.

**Idea behind the recursive method**

| Observation | Explanation |
| --- | --- |
| Even numbers differ from 0 by a multiple of 2 | Subtracting 2 repeatedly from an even number eventually reaches 0 |
| Odd numbers differ from 1 by a multiple of 2 | Subtracting 2 repeatedly from an odd number eventually reaches 1 |

The rules, in order:

1. If the number is **negative**, convert it to positive first (sign doesn't affect evenness/oddness).
2. If the number is **0**, it's **even**. *(base case)*
3. If the number is **1**, it's **odd**. *(base case)*
4. Otherwise, subtract **2** and repeat.

| Condition | Result |
| --- | --- |
| n = 0 | number is even |
| n = 1 | number is odd |
| n > 1 | check (n − 2) recursively |

```python
# Recursive function to determine whether a number is even.
# It repeatedly subtracts 2 from the number until it reaches
# one of the two base cases (0 or 1).

def is_even_recursive(n):
    """
    Return True if n is even, False if n is odd.
    Implemented recursively for demonstration purposes only —
    prefer 'n % 2 == 0' in real code (see note at the end).
    """

    # Normalize negative numbers to positive first,
    # since evenness/oddness doesn't depend on sign
    n = abs(n)

    # ---------- BASE CASES ----------
    if n == 0:
        return True     # 0 is even
    if n == 1:
        return False    # 1 is odd

    # ---------- RECURSIVE CASE ----------
    # Shrink the problem by subtracting 2, then recurse
    return is_even_recursive(n - 2)


# Example calls
print("-92 is even? ", is_even_recursive(-92))   # True  (-92 -> 92 -> even)
print("17 is even?  ", is_even_recursive(17))    # False (odd)
print("100 is even? ", is_even_recursive(100))   # True  (even)
```

##### Example Trace: Checking if 7 Is Even

| Step | Function Call |
| --- | --- |
| 1 | `is_even_recursive(7)` |
| 2 | `is_even_recursive(5)` |
| 3 | `is_even_recursive(3)` |
| 4 | `is_even_recursive(1)` |
| 5 | Base case reached → returns `False` |

```
is_even_recursive(7)
      ↓
is_even_recursive(5)
      ↓
is_even_recursive(3)
      ↓
is_even_recursive(1)
      ↓
Base case → return False
```

##### Why This Method Is Not Efficient

For large numbers, this recursive approach needs one function call for every 2 units of `n`. For example, `is_even_recursive(1_000_000)` would make roughly 500,000 recursive calls before reaching a base case — and Python's default recursion limit (around 1000) means it would actually crash with a `RecursionError` long before finishing.

Compare that to the direct approach:

```python
n % 2 == 0
```

which completes in a single step, regardless of how large `n` is. **This is the version you should actually use** — the recursive version above exists purely to practice thinking recursively.

