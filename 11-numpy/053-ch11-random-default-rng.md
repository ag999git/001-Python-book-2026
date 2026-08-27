



# Chapter 11.53 — Project: Modern Random Number Generation in NumPy

## What this page covers

This page is a research and practical project on how NumPy generates random numbers — and, more specifically, on a genuinely important shift in how NumPy recommends doing it. For a long time, the standard approach was `np.random.seed(...)` plus functions like `np.random.rand()`. NumPy now recommends a newer approach built around `np.random.default_rng()`. This page investigates *why* that recommendation exists, and what concrete problems the older approach can cause.

This matters well beyond NumPy itself: the underlying idea — a single shared, hidden piece of global state versus separate, independent objects each managing their own state — is a pattern that shows up throughout programming (it's closely related to why global variables in general are often risky, as covered in the earlier chapter page on the LEGB rule). Understanding it here, in a concrete, visual way with random numbers, makes the more abstract version of the same lesson easier to recognize elsewhere.

**A few terms used throughout, explained simply:**
- **Seed** — a starting value that fully determines a "random" sequence. The numbers that come out aren't truly random at all — they're calculated by a formula, and the seed is the starting input to that formula. The same seed always produces exactly the same sequence. ([NumPy docs: Random sampling](https://numpy.org/doc/stable/reference/random/index.html))
- **Global state** — data that's shared and accessible from anywhere in a program, rather than being contained within one specific object. Covered more generally in the earlier LEGB chapter page.
- **Reproducibility** — the ability to run the same code again and get exactly the same result, which matters enormously for testing, debugging, and sharing scientific or machine-learning results with others.

---

## Task

*(Kept exactly as set in the assignment.)*

### Part A — Conceptual Study

Investigate the following:
1. What is the difference between `np.random.seed()` and `np.random.default_rng(seed)`?
2. Why does NumPy recommend using `default_rng()` in modern applications?
3. What problems can arise from using global random state?
4. Explain the role of randomness in simulations, machine learning, and data analysis.

### Part B — Practical Task

Write a Python program that:
1. Creates random arrays using both the old API (`np.random`) and the new API (`default_rng()`)
2. Uses the following distributions: uniform, normal, integers
3. Demonstrates reproducibility using seeds, and independence of generators
4. Compares outputs and documents observations

### Expected Outcome

You should be able to explain why modern random generators are preferred, when reproducibility matters, and how different distributions behave.

### A follow-up question worth exploring

The theory below demonstrates the old API's "order matters" problem using two calls to `np.random.rand()`. As a follow-up exercise: **does the same "order matters" problem affect the new API if you create just one single `default_rng()` generator and call it twice, in different orders?** Try it yourself before reading further — the answer reveals an important nuance: independence comes from having *separate generator objects*, not merely from using the new function name. A single `rng` object, called multiple times, still produces its results in the order you call it, exactly as you'd expect from any stateful object — the real fix is creating separate `rng` objects when you specifically need independence.

---

## ANSWER — Theory

### 1. Global vs. Local Random State

- `np.random.seed()` sets a **global state** — one single, shared, hidden random generator used by the entire program.
- Every call to `np.random.rand()`, `np.random.randint()`, and similar old-API functions anywhere in your program draws from this *same* shared generator.
- This can cause unintended interference: two completely unrelated functions, each using randomness for their own purposes, can accidentally affect each other's results, simply because they're both drawing numbers from the same underlying sequence.

### 2. The Generator-Based Approach

`np.random.default_rng()` creates an **independent generator object** — think of it as your own personal random-number machine, rather than sharing one machine with the entire program.

- Each generator keeps its own separate internal state.
- This makes it safer for experiments — one part of your code can't accidentally disturb another's random sequence.
- It's also better suited to parallel computing (running multiple pieces of code at the same time), since each parallel task can be given its own independent generator, with no risk of one interfering with another.

### 3. Why the Modern API Is Preferred

| Feature | Old API (`np.random.seed`) | New API (`default_rng`) |
|---|---|---|
| State | Global — shared across the whole program | Local — owned by one specific generator object |
| Control | Limited | High |
| Reproducibility | Risky — depends on call order, which can be easy to accidentally change | Reliable — each generator's sequence depends only on its own seed, not on anything else happening in the program |
| Parallel use | Poor — a shared global generator can't safely be used by multiple parallel tasks at once | Strong — each task can have its own independent generator |

### 4. The Role of Randomness

- **Simulations** — modeling real-world uncertainty (weather, traffic, physical processes) by generating many random scenarios and observing the range of outcomes.
- **Machine learning** — used for things like the random initial values a model's internal parameters start with, before training adjusts them ("weight initialization").
- **Statistics / data analysis** — used for sampling: picking a smaller, random subset of a large dataset to analyze, in a way that fairly represents the whole.

---

## Detailed explanation: old API vs. new API

### 1. What does "same seed" actually mean?

A **seed** fixes the exact starting point of a random sequence. The same seed always produces the same sequence — this is true for *both* the old and new API, without exception.

```python
import numpy as np

# Step 1: Using the OLD API twice, with the same seed.
np.random.seed(0)
print(np.random.rand(3))

np.random.seed(0)
print(np.random.rand(3))
# Both lines print the EXACT SAME three numbers -- the seed guarantees this.

# Step 2: Using the NEW API twice, with the same seed.
rng1 = np.random.default_rng(0)
rng2 = np.random.default_rng(0)

print(rng1.random(3))
print(rng2.random(3))
# Both lines ALSO print the same three numbers as each other.
```

*(The exact numbers you see will depend on your installed NumPy version and the specific algorithm it uses internally, but running each pair of lines above will always show two identical results within that pair.)*

**So far, no difference at all between the two approaches.**

### 2. Where the real difference actually shows up

The difference isn't in "same seed gives same sequence" (both APIs agree on that) — it's in **how the sequence is managed and shared** afterward.

#### Old API → one shared, global generator

There is exactly **one** hidden random generator for the entire program. Every single call to a `np.random.*` function, anywhere in your code, uses this same shared generator.

```python
import numpy as np

np.random.seed(0)

a = np.random.rand(3)   # Step 1: the FIRST call, using the global generator
b = np.random.rand(3)   # Step 2: the SECOND call -- continues from where 'a' left off

print(a)
print(b)
```

The crucial, easy-to-miss detail: **`b`'s values depend on the fact that `a` was generated first.** The global generator doesn't reset between these two calls — `b` simply continues the same underlying sequence from wherever `a` left it.

**Proof — reversing the order changes the results:**

```python
np.random.seed(0)

b = np.random.rand(3)   # Now this runs FIRST
a = np.random.rand(3)   # And this runs SECOND

print(a)
print(b)
# The VALUES stored in 'a' and 'b' are now DIFFERENT from the previous
# example -- even though the seed is identical, simply swapping which
# line runs first changes which numbers end up in which variable.
```

![Flowchart](/resources/ch-11-numpy-august-2026-prng1.png)



**This is the core problem with the old API:** a shared global sequence means the *order* in which different parts of your program happen to call random functions can change your results — a subtle, easy-to-introduce bug, especially in larger programs where you might not even realize two unrelated functions are both quietly drawing from the same global sequence.

#### New API → independent generators

Each `rng` object created with `default_rng()` is its own, completely separate random-number machine.

```python
rng1 = np.random.default_rng(0)
rng2 = np.random.default_rng(0)

a = rng1.random(3)
b = rng2.random(3)

print(a)
print(b)
# 'a' and 'b' are IDENTICAL here, because rng1 and rng2 started with
# the SAME seed and are each being asked for their very FIRST 3 numbers.
```

```python
# Continuing to draw from each generator independently:
a_next = rng1.random(3)
b_next = rng2.random(3)

print(a_next)
print(b_next)
# STILL identical to each other -- rng1 and rng2 remain in perfect
# sync, because each one only ever tracks its OWN separate progress,
# completely unaffected by anything happening to the other generator.
```

![Flowchart](/resources/ch-11-numpy-august-2026-prng2.png)




**Key insight:** each generator runs its own, completely independent sequence — nothing that happens to `rng2` can ever affect `rng1`, and vice versa, no matter what order you call them in, or how many other generators exist elsewhere in your program.

---

## Part B: A complete practical solution

```python
import numpy as np

# ============================================================
# STEP 1: Random arrays using the OLD API
# ============================================================
np.random.seed(42)   # Fix the global state for reproducibility.

old_uniform = np.random.rand(5)              # Uniform distribution, range [0, 1)
old_normal = np.random.randn(5)              # Standard normal (bell curve) distribution
old_integers = np.random.randint(1, 100, 5)  # Random integers, from 1 up to (not including) 100

print("OLD API results:")
print("Uniform:", old_uniform)
print("Normal:", old_normal)
print("Integers:", old_integers)


# ============================================================
# STEP 2: Random arrays using the NEW API
# ============================================================
rng = np.random.default_rng(42)   # An independent generator, seeded the same way.

new_uniform = rng.uniform(0, 1, 5)     # Uniform distribution, explicit range
new_normal = rng.normal(0, 1, 5)       # Normal distribution, explicit mean=0 and std-dev=1
new_integers = rng.integers(1, 100, 5) # Random integers, from 1 up to (not including) 100

print("\nNEW API results:")
print("Uniform:", new_uniform)
print("Normal:", new_normal)
print("Integers:", new_integers)


# ============================================================
# STEP 3: Reproducibility using seeds (new API)
# ============================================================
rng_a = np.random.default_rng(123)
rng_b = np.random.default_rng(123)

print("\nReproducibility check (same seed, new API):")
print("rng_a:", rng_a.random(3))
print("rng_b:", rng_b.random(3))
print("Are they identical?", np.array_equal(rng_a.random(3), rng_b.random(3)))
# Note: this final comparison draws a THIRD set of numbers from each
# generator (their second call) -- since both generators are still
# perfectly in sync, this remains True.


# ============================================================
# STEP 4: Independence of generators
# ============================================================
rng_x = np.random.default_rng(7)
rng_y = np.random.default_rng(99)   # A DIFFERENT seed on purpose.

print("\nIndependence check (different seeds):")
print("rng_x:", rng_x.random(3))
print("rng_y:", rng_y.random(3))
# These will almost certainly be DIFFERENT from each other, since they
# started from different seeds -- and critically, calling rng_x does
# NOT change anything about what rng_y will produce, or vice versa.


# ============================================================
# STEP 5: Documenting observations
# ============================================================
print("\n--- Observations ---")
print("1. Both APIs support reproducibility when given the same seed.")
print("2. The OLD API shares ONE global generator -- call order matters.")
print("3. The NEW API gives each generator its OWN independent state.")
print("4. Different distributions (uniform, normal, integers) simply")
print("   call different METHODS on the same underlying generator object.")
```

### Comparing the distributions used above

| Distribution | Old API function | New API method | What it produces |
|---|---|---|---|
| Uniform | `np.random.rand(n)` | `rng.uniform(low, high, n)` | Every value in the range is equally likely |
| Normal | `np.random.randn(n)` | `rng.normal(mean, std, n)` | Values cluster around a mean, in the classic "bell curve" shape |
| Integers | `np.random.randint(low, high, n)` | `rng.integers(low, high, n)` | Whole numbers only, evenly spread across the given range |

*(Notice the new API's methods generally take the distribution's actual parameters — like `low`/`high` for uniform, or `mean`/`std` for normal — directly and explicitly, whereas some old-API functions like `rand()`/`randn()` have more fixed, less flexible defaults.)*

---

## Quick recap

- **A seed fully determines a random sequence** — the same seed always produces the same sequence, in both the old and new API. This part isn't where the two approaches differ.
- **The real difference is state management**: the old API (`np.random.seed`) uses one single, shared, global generator for the entire program, while the new API (`np.random.default_rng()`) gives you independent generator objects, each with their own private state.
- **Shared global state creates an "order matters" risk** — two unrelated pieces of code drawing from the same global generator can silently affect each other's results, simply based on which one happens to run first.
- **Independent generators eliminate that risk entirely** — as long as you create a genuinely separate `default_rng()` object for each independent task, nothing that happens to one can ever influence another, regardless of call order.
- **As the follow-up question highlights**, independence comes specifically from using *separate generator objects* — reusing a single `rng` object multiple times still produces results in the order you call it, exactly like any other stateful object would.





