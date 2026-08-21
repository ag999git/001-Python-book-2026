# Advanced Concepts of Generators

This section builds on the earlier introduction to `yield` and generator functions, and assumes you're already comfortable with the basic idea: a generator is a function that produces a sequence of values one at a time, pausing at each `yield` instead of computing everything up front. Here, we go one level deeper — what actually happens when a generator runs out of values, how a `for` loop uses generators under the hood, and two classic examples (Fibonacci numbers and prime numbers) that show why generators are so well suited to sequences that are large, or even infinite. Understanding this "under the hood" behavior matters because generators are everywhere in real Python code — file reading, database queries, and many library functions all return generator-like objects rather than full lists, precisely for the memory reasons covered at the end of this section.

---

## 1. What Happens When a Generator Finishes?

When a generator has no more values left to produce, Python signals this by raising a special exception called `StopIteration`.

This is **not an error in your program** — it's a normal, expected signal that simply means *"there is nothing left to yield."* Every iterator in Python (not just generators) uses this same mechanism to announce that it's exhausted.

The diagram below shows the flow of control as a generator function runs, pauses at each `yield`, and eventually raises `StopIteration` once its body finishes:

![StopIteration Diagram](https://github.com/ag999git/001-Python-book-2026/blob/main/resources/ch6-generators-stopiteration.png)

### Script Demonstrating `StopIteration`

```python
# Demonstration of a simple generator and StopIteration.
#
# This generator function has three yield statements, plus print
# statements before/after each one, so we can clearly see WHEN the
# function's code actually runs relative to each next() call.

def simple_generator():
    """Generator with three yield statements."""

    print("Generator started")

    yield "yielding 1"     # Pauses here and hands back "yielding 1"
    print("Resuming after first yield")

    yield "yielding 2"     # Pauses here and hands back "yielding 2"
    print("Resuming after second yield")

    yield "yielding 3"     # Pauses here and hands back "yielding 3"
    print("Generator is about to finish")
    # No more yield statements after this point --
    # once execution reaches the end of the function body,
    # the generator is considered exhausted.


# ---- Step 1: create the generator object ----
# IMPORTANT: calling simple_generator() does NOT run any of its code yet.
# It only creates a generator object, ready to be advanced with next().
gen = simple_generator()
print("Generator object created\n")


# ---- Step 2: manually retrieve values with next() ----
print("First next() call:")
print(next(gen))   # NOW the function body starts running, up to the first yield

print("Second next() call:")
print(next(gen))   # Resumes right after the first yield, runs to the second

print("Third next() call:")
print(next(gen))   # Resumes right after the second yield, runs to the third


# ---- Step 3: the generator is now exhausted ----
# There are no more yield statements left to reach, so the NEXT call
# to next() causes the function to run off its end -- and Python
# turns that into a StopIteration exception.
print("Fourth next() call:")
try:
    print(next(gen))
except StopIteration:
    print("StopIteration raised -> no more values left in the generator!")


# ---- Step 4: using a generator inside a for loop ----
print("\nUsing generator in a for-loop:")

for value in simple_generator():   # a fresh generator object, starting from scratch
    print(value)

print("In a for-loop, StopIteration happens internally and is NOT shown.")
```

**Output:**

```
Generator object created

First next() call:
Generator started
yielding 1
Second next() call:
Resuming after first yield
yielding 2
Third next() call:
Resuming after second yield
yielding 3
Fourth next() call:
Generator is about to finish
StopIteration raised -> no more values left in the generator!

Using generator in a for-loop:
Generator started
yielding 1
Resuming after first yield
yielding 2
Resuming after second yield
yielding 3
Generator is about to finish
In a for-loop, StopIteration happens internally and is NOT shown.
```

> **Key thing to notice:** each `next()` call runs the generator's code only until the *next* `yield` is reached — not to the end of the function. This is what "pausing" really means: local variables, the current position in the code, and everything else about the function's state is frozen in place until the following `next()` call resumes it exactly where it left off.

---

## 2. How a `for` Loop Handles Generators

A `for` loop over a generator is really just convenient shorthand for a loop that calls `next()` repeatedly and catches `StopIteration` for you. Internally, it does roughly this:

1. Call `next()` on the generator to get the next value.
2. Run the loop body using that value.
3. Repeat from step 1.
4. When `next()` raises `StopIteration`, the loop catches it silently and simply ends — **no exception is ever shown to you**.

That's why this code:

```python
for value in simple_generator():
    print(value)
```

never needs a `try`/`except` block of its own — the `for` loop is already handling `StopIteration` behind the scenes, exactly as it does for ordinary lists, tuples, and every other iterable.

---

## 3. Fibonacci Generator

Generators are a natural fit for sequences like the Fibonacci numbers, where each value depends only on the previous two, and the sequence can in principle continue **forever**. A generator lets you express "produce Fibonacci numbers, one at a time, for as long as someone keeps asking" without ever needing to decide in advance how many to compute.

```python
# Fibonacci generator: produces the Fibonacci sequence one number
# at a time, indefinitely.

def fibonacci_generator():
    a, b = 0, 1  # the first two Fibonacci numbers

    while True:  # runs forever -- the generator itself never "decides" to stop
        yield a
        a, b = b, a + b  # advance both values by one step in the sequence


fib = fibonacci_generator()

# We choose how many values to take by only calling next() 10 times --
# the infinite while loop inside the generator is perfectly safe here,
# because we control how far we advance it from the outside.
for _ in range(10):  # '_' is the conventional name for a loop variable we don't use
    print(next(fib))
```

**Output:** `0 1 1 2 3 5 8 13 21 34`

> **Why not just build a list?** You could write a function that returns a list of the first *N* Fibonacci numbers, but that forces you to decide *N* in advance, and to hold every value in memory at once. The generator version separates those two concerns: it only knows how to produce the *next* value, and the caller decides when to stop asking.

---

## 4. Generator Example — Prime Numbers

This example builds a generator that produces an endless stream of prime numbers greater than some starting value — another sequence where you rarely know in advance how many values you'll actually need.

```python
# Generator for prime numbers greater than a given starting value.

def is_prime(num):
    """Return True if num is a prime number, False otherwise."""

    if num <= 1:            # 0, 1, and negative numbers are never prime
        return False

    # A number only needs to be checked for factors up to its square
    # root -- if it had a factor larger than that, it would necessarily
    # also have a matching factor smaller than the square root, which
    # we'd have already found.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:    # found a factor -- num is not prime
            return False

    return True


def next_prime_generator(start):
    """Yield an endless sequence of primes, each greater than 'start'."""

    num = start + 1

    while True:              # keeps searching forever, one number at a time
        if is_prime(num):
            yield num         # pause here and hand back this prime
        num += 1              # on resume, move on to check the next number


# Create a generator that will produce primes greater than 100.
# Nothing is computed yet -- calling the function just creates the
# generator object, exactly as with fibonacci_generator() above.
prime_gen = next_prime_generator(100)

# Pull out the first 10 primes greater than 100, one at a time.
for _ in range(10):
    print(next(prime_gen))
```

**Output:** `101 103 107 109 113 127 131 137 139 149`

> **Notice the pattern:** both this example and the Fibonacci generator share the same shape — an infinite `while True:` loop with a `yield` inside it. This is a very common and perfectly safe generator pattern in Python, *because* nothing forces the loop to actually run forever: it only advances one step every time something calls `next()` on it. The generator does exactly as much work as the caller asks for, and no more.

---

## 5. Advantages of Generators

| Advantage | Explanation |
| --- | --- |
| Memory efficient | Values are produced one at a time, on demand — nothing is held in memory beyond the current value and whatever state the generator needs to compute the next one. |
| Well suited to large or infinite sequences | Since a generator never needs to know its total length in advance, it can represent sequences (like the primes above) that would be impossible to store as a complete list. |
| Faster to get started | The first value is available as soon as it's computed, without waiting for the rest of the sequence to be built — useful when you might only need the first few results. |
| State preserved automatically | Local variables (like `a, b` in the Fibonacci example) stay exactly as they were when the function paused — you don't need to manually track progress between calls. |
| Integrates naturally with loops | A generator can be used directly in a `for` loop, in `list()`, in `sum()`, and anywhere else an iterable is expected, since `StopIteration` is handled automatically. |

> **A trade-off worth knowing:** the flip side of "compute only what's needed" is that a generator **can only be iterated through once**. Once it's exhausted (or once you stop pulling values from it), there's no way to "rewind" it — you'd need to call the generator function again to get a fresh one, as the `for`-loop example in Section 1 does with `simple_generator()`.

