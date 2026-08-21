# Functional Tools in Python: `zip()`, `lambda`, `map()`, and `filter()`

This section introduces four tools that go hand in hand once you're comfortable with functions: `zip()` for walking through several sequences together, `lambda` for writing tiny throwaway functions inline, and `map()` and `filter()` for transforming and selecting data without writing an explicit loop. These four are used constantly in real Python code — especially together, since `lambda` is most often seen *inside* a call to `map()`, `filter()`, or `sorted()` rather than on its own. By the end of this section you should be comfortable recognizing this style of "functional" Python and choosing between it and a plain `for` loop.

---

## 1. `zip()` Function

### Concept

`zip()` combines elements from **two or more iterables** into tuples, pairing up elements that share the **same position** across all the inputs. It **stops as soon as the shortest iterable runs out**, so it's the natural tool whenever you want to **iterate over multiple sequences in parallel** — for example, walking through a list of names and a list of ages together.

### Syntax

```python
zip(*iterables)
```

Where:

- `iterables` can be any mix of lists, tuples, strings, ranges, or other iterables.
- The result is a **zip object** — a memory-efficient iterator, not a list. Wrap it in `list()` to see its contents directly, or loop over it directly in a `for` loop (see Example 4 below).

### Key Properties

| Feature | Description |
| --- | --- |
| Works with | any iterable — lists, tuples, strings, ranges, and more |
| Returns | a `zip` iterator object |
| Output format | tuples, one per matched position |
| Stops when | the **shortest** input iterable is exhausted |
| Common use | parallel iteration; building dictionaries; "unzipping" paired data |

### Script Demonstrating `zip()`

```python
# Demonstration of the zip() function in Python

# ---- Example 1: zipping two lists ----
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

z = zip(list1, list2)
print("Type of result:", type(z))  # <class 'zip'> -- zip() returns an iterator, not a list

# An iterator is "used up" once you read from it, so we convert
# it to a list here purely to display its contents.
print("Zipped result:", list(z))  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

print("-----------------------------------")

# ---- Example 2: zipping sequences of unequal length ----
a = [10, 20, 30, 40]
b = ['x', 'y']

# zip() pairs elements up until the SHORTER list (b) runs out,
# then stops -- the extra elements in 'a' are simply ignored.
result = list(zip(a, b))
print(result)  # [(10, 'x'), (20, 'y')]

print("-----------------------------------")

# ---- Example 3: zipping three sequences at once ----
names = ["Alice", "Bob", "Charlie"]
ages = [21, 22, 23]
cities = ["Delhi", "Mumbai", "Kolkata"]

# zip() isn't limited to two iterables -- any number can be combined
combined = list(zip(names, ages, cities))
print(combined)
# [('Alice', 21, 'Delhi'), ('Bob', 22, 'Mumbai'), ('Charlie', 23, 'Kolkata')]

print("-----------------------------------")

# ---- Example 4: iterating directly with zip (no list() needed) ----
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']

# A for loop can consume the zip iterator directly --
# there's no need to convert it to a list first.
for n, l in zip(numbers, letters):
    print(n, l)
# Output:
# 1 A
# 2 B
# 3 C

print("-----------------------------------")

# ---- Example 5: "unzipping" paired data back into separate sequences ----
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# The * operator unpacks the list of tuples into separate positional
# arguments, i.e. zip(*pairs) is the same as zip((1,'a'), (2,'b'), (3,'c')).
# zip() then re-groups them BY POSITION, effectively reversing the
# original zipping -- this is why the trick is called "unzipping".
x, y = zip(*pairs)

print("Numbers:", x)  # (1, 2, 3)
print("Letters:", y)  # ('a', 'b', 'c')

print("-----------------------------------")

# ---- Example 6: building a dictionary from two parallel lists ----
keys = ['name', 'age', 'city']
values = ['Rahul', 25, 'Delhi']

# zip() pairs each key with its matching value; dict() then turns
# those pairs directly into key-value entries.
dictionary = dict(zip(keys, values))
print(dictionary)  # {'name': 'Rahul', 'age': 25, 'city': 'Delhi'}
```

> **Common pitfall:** because `zip()` silently stops at the shortest iterable (Example 2), mismatched-length inputs won't raise an error — they'll just quietly drop data. If your lists are *supposed* to be the same length, it's worth checking `len(a) == len(b)` before zipping, so a bug elsewhere in your program doesn't go unnoticed.

---

## 2. Lambda Functions

### Concept

A **lambda function** is a small, anonymous function — "anonymous" meaning it has no name of its own. Unlike a function defined with `def`, a lambda:

- has **no name** (unless you assign it to a variable, as in the examples below),
- is written as **a single expression** — no statements, no multiple lines, no `return` keyword,
- and **automatically returns** the value of that expression.

Lambdas exist for situations where you need a small, throwaway function — often just to pass as an argument to another function — and writing a full `def` block would be more ceremony than the task deserves.

### Syntax

```python
lambda arguments: expression
```

Example:

```python
lambda x: x * x
```

This is functionally equivalent to:

```python
def square(x):
    return x * x
```

### Key Characteristics

| Feature | Description |
| --- | --- |
| Anonymous | has no function name of its own |
| Body | a single expression only — no statements, loops, or `if`/`else` blocks (a conditional *expression* is allowed, though — see the tip below) |
| Return value | automatic — whatever the expression evaluates to |
| Most often used with | `map()`, `filter()`, `sorted()`, and similar functions that expect a small function as an argument |

### Script Demonstrating Lambda Functions

```python
# Demonstration of lambda functions

# ---- Example 1: an ordinary named function ----
def square(x):
    return x * x

print(square(5))  # 25

# ---- Example 2: the same logic as a lambda ----
# A lambda that squares its input, assigned to a variable so it
# can be called just like a normal function.
square_lambda = lambda x: x * x
print(square_lambda(6))  # 36

# ---- Example 3: a lambda with two arguments ----
add = lambda x, y: x + y
print(add(3, 4))  # 7

# ---- Example 4: a lambda with three arguments ----
sum_three = lambda a, b, c: a + b + c
print(sum_three(2, 3, 4))  # 9

# ---- Example 5: a lambda as a sort key ----
students = [("Alice", 23), ("Bob", 21), ("Charlie", 25)]

# 'key' tells sorted() WHAT to sort by, not how to compare it.
# Here, x[1] extracts each student's age, so the list is
# sorted by age rather than by name (the default for tuples).
sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)
# [('Bob', 21), ('Alice', 23), ('Charlie', 25)]
```

> **Tip:** although a lambda body must be a single *expression*, that expression can be a conditional one — for example `lambda x: "even" if x % 2 == 0 else "odd"` is perfectly valid, since Python's `A if condition else B` is itself an expression, not a statement.

> **Style note:** if a lambda is getting hard to read, or you find yourself wanting to give it a name and reuse it in several places, that's usually a sign it should be a regular `def` function instead. Lambdas are best kept short and used once, typically inline as an argument.

---

## 3. `map()` Function

### Concept

`map()` applies a given **function to every element** of one or more iterables, producing a new value for each one. It returns a **map object** — an iterator, not a list — so its results are typically wrapped in `list()` when you want to see or store them all at once.

### Syntax

```python
map(function, iterable)
```

`map()` can also work across **multiple iterables** at once, passing one element from each to the function on every step:

```python
map(function, iterable1, iterable2)
```

### Key Properties

| Feature | Description |
| --- | --- |
| Input | a function, plus one or more iterables |
| Output | a `map` iterator |
| Purpose | transform every element of an iterable |
| Works with | multiple iterables in parallel (like `zip()`) |

### Script Demonstrating `map()`

```python
# Demonstration of the map() function

# ---- Example 1: map() with an ordinary named function ----
def cube(n):
    return n ** 3

numbers = [1, 2, 3, 4, 5]

# map() applies cube() to every element of 'numbers' in turn,
# without us having to write an explicit for loop.
cube_map = map(cube, numbers)
print(list(cube_map))  # [1, 8, 27, 64, 125]

print("-----------------------------------")

# ---- Example 2: map() with a lambda instead of a named function ----
# This is the most common style in real code -- define the
# transformation inline, right where it's used.
numbers = [1, 2, 3, 4, 5]
cubes = map(lambda x: x ** 3, numbers)
print(list(cubes))  # [1, 8, 27, 64, 125]

print("-----------------------------------")

# ---- Example 3: map() across two lists at once ----
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

# Each call combines one element from list1 with the element
# at the SAME position in list2 -- exactly like zip(), but the
# results are transformed by the lambda instead of just paired.
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # [11, 22, 33, 44]

print("-----------------------------------")

# ---- Example 4: converting a list of strings into integers ----
# Any function that takes one argument can be used with map() --
# not just lambdas. Here, the built-in int() itself is passed directly.
string_numbers = ["10", "20", "30"]
integers = map(int, string_numbers)
print(list(integers))  # [10, 20, 30]
```

> **`map()` vs. a list comprehension:** `list(map(lambda x: x ** 3, numbers))` and `[x ** 3 for x in numbers]` do exactly the same thing. Many Python programmers find comprehensions more readable for simple cases, and reach for `map()` mainly when the transformation function already exists and has a name (as in Example 4, `map(int, string_numbers)`), since `[int(x) for x in string_numbers]` doesn't offer much of an advantage there.

---

## 4. `filter()` Function

### Concept

`filter()` selects only the elements of an iterable that satisfy a **Boolean condition** — the given function is applied to each element in turn, and only the elements for which it returns `True` are kept.

### Syntax

```python
filter(function, iterable)
```

### Key Properties

| Feature | Description |
| --- | --- |
| Input | a function that returns `True`/`False`, plus an iterable |
| Output | a `filter` iterator |
| Purpose | select a subset of elements that meet some condition |

### Script Demonstrating `filter()`

```python
# Demonstration of the filter() function

# ---- Example 1: filtering even numbers ----
numbers = list(range(10))
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [0, 2, 4, 6, 8]

print("-----------------------------------")

# ---- Example 2: filtering out non-positive numbers ----
data = [-5, -2, 0, 3, 7, -1]
positive_numbers = filter(lambda x: x > 0, data)
print(list(positive_numbers))  # [3, 7]

print("-----------------------------------")

# ---- Example 3: filtering strings by length ----
words = ["cat", "elephant", "dog", "tiger"]
long_words = filter(lambda x: len(x) > 3, words)
print(list(long_words))  # ['elephant', 'tiger']

print("-----------------------------------")

# ---- Example 4: filter() with a named function instead of a lambda ----
def is_odd(n):
    return n % 2 != 0

numbers = list(range(10))
odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))  # [1, 3, 5, 7, 9]
```

> **`filter()` vs. a list comprehension:** just like with `map()`, `list(filter(lambda x: x % 2 == 0, numbers))` is equivalent to `[x for x in numbers if x % 2 == 0]`. Both are idiomatic Python — use whichever reads more clearly for the task at hand.

---

## Putting It Together: `map()`, `filter()`, and `lambda` Combined

Because `map()` and `filter()` both return iterators, they can be chained together directly — the output of one feeding straight into the next — without ever materializing an intermediate list:

```python
numbers = list(range(1, 11))

# First keep only the even numbers, then cube each of those that remain.
result = list(map(lambda x: x ** 3, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [8, 64, 216, 512, 1000]
```

This combination — `filter()` to select, `map()` to transform, `lambda` to define the logic inline — is a very common pattern in real-world Python code, and recognizing it will make other people's code (and library documentation) much easier to read.

