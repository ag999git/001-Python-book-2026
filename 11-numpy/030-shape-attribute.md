
# Chapter 11 — The `shape` Attribute

## About this chapter

Every NumPy array carries its own description of how its numbers are
arranged. That description is the **`shape`** attribute, and almost
everything else in this chapter depends on reading it correctly.
Broadcasting works by comparing shapes. The `axis` argument only makes
sense once you can see the shape. Matrix multiplication refuses to run if
two shapes do not fit together. Most of the error messages a beginner meets
in NumPy are, underneath, a complaint about shape.

This page is short on purpose. It does one thing: it makes `shape`
completely clear before you meet it everywhere else.

By the end of this page you should be able to:

- Read an array's shape and say how many numbers it holds and how they are laid out.
- Explain why `(3,)`, `(1, 3)` and `(3, 1)` are three different things holding the same three numbers.
- Use `reshape()` confidently, including the `-1` shortcut.
- Recognise the two commonest shape error messages and know what to do about them.
- Use `shape` to decide which `axis` you want.

> **Glossary of common terms**
> - **Axis** — one "direction" along which the numbers are arranged. A list
>   of numbers has one axis; a table has two (rows and columns). See the
>   [NumPy beginner's guide](https://numpy.org/doc/stable/user/absolute_beginners.html).
> - **Shape** — a [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
>   giving the array's size along each axis, longest axis first. `(2, 3)`
>   means two rows of three.
> - **`ndim`** — the number of axes. It is always the same as the length of
>   the shape tuple.
> - **`size`** — the total number of items, which is the shape's numbers
>   multiplied together.
> - **[`reshape()`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html)**
>   — rearranges the same numbers into a different shape. It never changes
>   the numbers and never changes how many there are.
> - **View** — a second array that shares the first one's memory. Change one
>   and the other changes too.

---

## 1. Shape, `ndim` and `size`

These three attributes describe the same thing from three angles, so it is
worth meeting them together.

```python
import numpy as np

# Step 1 - a plain list of three numbers
a = np.array([10, 20, 30])
print("Step 1 - the array:", a)
print("Step 2 - shape:", a.shape)
print("Step 3 - type of shape:", type(a.shape))
print("Step 4 - number of axes (ndim):", a.ndim)
print("Step 5 - total number of items (size):", a.size)
print("Step 6 - len(a.shape) is the same as a.ndim:", len(a.shape), a.ndim)
print()

# Step 7 - a table: two rows of three
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Step 7 - a 2D array:\n", b)
print("Step 8 - shape:", b.shape, " ndim:", b.ndim, " size:", b.size)
print()

# Step 9 - two stacked tables
c = np.arange(8).reshape(2, 2, 2)
print("Step 9 - a 3D array:\n", c)
print("Step 10 - shape:", c.shape, " ndim:", c.ndim, " size:", c.size)
print()

# Step 11 - a single number, held as an array
s = np.array(7)
print("Step 11 - a 0D array (just one number):", s)
print("Step 12 - shape:", s.shape, " ndim:", s.ndim, " size:", s.size)
```

**Output**

```text
Step 1 - the array: [10 20 30]
Step 2 - shape: (3,)
Step 3 - type of shape: <class 'tuple'>
Step 4 - number of axes (ndim): 1
Step 5 - total number of items (size): 3
Step 6 - len(a.shape) is the same as a.ndim: 1 1

Step 7 - a 2D array:
 [[1 2 3]
 [4 5 6]]
Step 8 - shape: (2, 3)  ndim: 2  size: 6

Step 9 - a 3D array:
 [[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
Step 10 - shape: (2, 2, 2)  ndim: 3  size: 8

Step 11 - a 0D array (just one number): 7
Step 12 - shape: ()  ndim: 0  size: 1
```

Three things to take from this.

**The shape is a tuple, not a list.** That is why a one-dimensional array
prints `(3,)` with a trailing comma: in Python, `(3)` is just the number 3,
and the comma is what makes it a tuple of one item. The comma is not a typing
mistake, and it is the quickest way to tell a 1D array from anything else.

**`ndim` is the length of the shape.** A shape of `(2, 3)` has two numbers
in it, so the array has two axes. You never need to remember `ndim`
separately; count the numbers in the shape.

**`size` is the shape multiplied out.** `(2, 2, 2)` gives 8 items, `(2, 3)`
gives 6. This is worth knowing because `reshape()` can only produce shapes
that multiply to the same total.

---

## 2. `(3,)`, `(1, 3)` and `(3, 1)` are not the same

This is the point of the page. All three hold the numbers 10, 20 and 30.
They behave quite differently.

```python
import numpy as np

a = np.array([10, 20, 30])
row = a.reshape(1, 3)      # one row of three
col = a.reshape(3, 1)      # three rows of one

# Step 1 - the same numbers, three arrangements
print("Step 1 - flat, shape", a.shape, ":", a)
print("Step 2 - row, shape", row.shape, ":\n", row)
print("Step 3 - column, shape", col.shape, ":\n", col)
print("Step 4 - all three hold the same three numbers:", a.size, row.size, col.size)
print()

# Step 5 - adding a row to a row gives a row
print("Step 5 - row + row, shape", (row + row).shape, ":\n", row + row)

# Step 6 - adding a row to a column gives a 3 by 3 grid, not a mistake
print("Step 6 - row + column, shape", (row + col).shape, ":\n", row + col)
```

**Output**

```text
Step 1 - flat, shape (3,) : [10 20 30]
Step 2 - row, shape (1, 3) :
 [[10 20 30]]
Step 3 - column, shape (3, 1) :
 [[10]
 [20]
 [30]]
Step 4 - all three hold the same three numbers: 3 3 3

Step 5 - row + row, shape (1, 3) :
 [[20 40 60]]
Step 6 - row + column, shape (3, 3) :
 [[20 30 40]
 [30 40 50]
 [40 50 60]]
```

Step 6 catches nearly everyone the first time. Adding three numbers to three
numbers gave nine numbers. Nothing went wrong: NumPy **broadcast** the row
across the column, pairing every value with every other, exactly as it is
designed to. The result is right for the shapes it was given — the shapes
were simply not the ones the programmer had in mind.

Whenever a NumPy result comes out surprisingly large, print the shapes of
both operands first. The answer is almost always there. The
[broadcasting page](050-ch11-broadcasting.md) explains the rules in full,
and the
[row vectors and column vectors page](040-row-column-vector.md) explains
why linear algebra prefers columns.

---

## 3. Changing the shape with `reshape()`

`reshape()` rearranges the same numbers. It never adds, removes or alters a
single value.

```python
import numpy as np

d = np.arange(12)
print("Step 1 - twelve numbers, shape", d.shape, ":", d)

# Step 2 - three rows of four
print("Step 2 - reshape(3, 4), shape", d.reshape(3, 4).shape, ":\n", d.reshape(3, 4))

# Step 3 - -1 means "you work this one out"
print("Step 3 - reshape(3, -1) lets NumPy work out the 4:", d.reshape(3, -1).shape)
print("Step 4 - reshape(-1, 6) lets NumPy work out the 2:", d.reshape(-1, 6).shape)

# Step 5 - any number of axes is allowed, as long as the total matches
print("Step 5 - reshape(2, 2, 3), shape", d.reshape(2, 2, 3).shape)

# Step 6 - a shape whose numbers do not multiply to 12 is refused
try:
    d.reshape(5, 3)
except ValueError as error:
    print("Step 6 - ValueError:", error)
```

**Output**

```text
Step 1 - twelve numbers, shape (12,) : [ 0  1  2  3  4  5  6  7  8  9 10 11]
Step 2 - reshape(3, 4), shape (3, 4) :
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Step 3 - reshape(3, -1) lets NumPy work out the 4: (3, 4)
Step 4 - reshape(-1, 6) lets NumPy work out the 2: (2, 6)
Step 5 - reshape(2, 2, 3), shape (2, 2, 3)
Step 6 - ValueError: cannot reshape array of size 12 into shape (5,3)
```

**The `-1` shortcut.** You may write `-1` for exactly one of the numbers,
and NumPy fills it in from the total. `d.reshape(3, -1)` says "three rows,
and as many columns as that takes". It saves arithmetic and it saves the
code from breaking when the amount of data changes.

**The error message tells you everything.** `cannot reshape array of size 12
into shape (5,3)` is saying that 5 times 3 is 15, and there are only 12
numbers. Check the size, not the code around it.

---

## 4. A reshaped array usually shares its memory

This follows on from the view-and-copy question raised on the
[conceptual questions page](130-ch11-conceptual-qa.md), and it surprises
people who expect `reshape()` to hand back something separate.

```python
import numpy as np

b = np.array([[1, 2, 3], [4, 5, 6]])
print("Step 1 - the original, shape", b.shape, ":\n", b)

# Step 2 - reshape returns a VIEW of the same memory wherever it can
v = b.reshape(3, 2)
print("Step 2 - reshaped to", v.shape, ":\n", v)

# Step 3 - so changing the new array changes the old one
v[0, 0] = 99
print("Step 3 - changing the reshaped array changed the original too:\n", b)

# Step 4 - flatten() always makes a copy, so the original is safe
b[0, 0] = 1
f = b.flatten()
f[0] = -1
print("Step 4 - flatten() makes a copy, so the original is untouched:", b[0, 0])

# Step 5 - ravel() flattens too, but returns a view when it can
r = b.ravel()
r[0] = -5
print("Step 5 - ravel() gives a view here, so the original did change:", b[0, 0])
```

**Output**

```text
Step 1 - the original, shape (2, 3) :
 [[1 2 3]
 [4 5 6]]
Step 2 - reshaped to (3, 2) :
 [[1 2]
 [3 4]
 [5 6]]
Step 3 - changing the reshaped array changed the original too:
 [[99  2  3]
 [ 4  5  6]]
Step 4 - flatten() makes a copy, so the original is untouched: 1
Step 5 - ravel() gives a view here, so the original did change: -5
```

The rule to carry away: **`reshape()` and `ravel()` give you a view when
they can, and `flatten()` always gives you a copy.** If you are about to
change the values and want the original left alone, call `.copy()` and be
certain.

---

## 5. Shape is how you choose an `axis`

Once you can read a shape, the `axis` argument stops being guesswork.

```python
import numpy as np

# Four students, three subjects each
scores = np.array([[70, 65, 80],
                   [90, 85, 75],
                   [60, 72, 88],
                   [95, 91, 89]])

print("Step 1 - four students, three subjects. Shape:", scores.shape)
print("Step 2 - shape[0] is the number of rows (students):", scores.shape[0])
print("Step 3 - shape[1] is the number of columns (subjects):", scores.shape[1])

# Step 4 - axis=0 collapses the rows, leaving one value per subject
print("Step 4 - average per subject, shape", scores.mean(axis=0).shape, ":", scores.mean(axis=0))

# Step 5 - axis=1 collapses the columns, leaving one value per student
print("Step 5 - average per student, shape", scores.mean(axis=1).shape, ":", scores.mean(axis=1))

# Step 6 - transposing swaps the two axes round
print("Step 6 - transposed, shape:", scores.T.shape)

# Step 7 - the shape is a tuple, so it unpacks like any other
rows, cols = scores.shape
print(f"Step 7 - unpacking the tuple: {rows} rows and {cols} columns")
```

**Output**

```text
Step 1 - four students, three subjects. Shape: (4, 3)
Step 2 - shape[0] is the number of rows (students): 4
Step 3 - shape[1] is the number of columns (subjects): 3
Step 4 - average per subject, shape (3,) : [78.75 78.25 83.  ]
Step 5 - average per student, shape (4,) : [71.66666667 83.33333333 73.33333333 91.66666667]
Step 6 - transposed, shape: (3, 4)
Step 7 - unpacking the tuple: 4 rows and 3 columns
```

**The trick for remembering `axis`.** The axis you name is the one that
disappears. Here the shape is `(4, 3)`. Naming `axis=0` removes the 4 and
leaves `(3,)`, one number per subject. Naming `axis=1` removes the 3 and
leaves `(4,)`, one number per student. The
[3D arrays and axis operations page](045-ch11-3d-array-axis-ops.md) takes
this further into three dimensions.

---

## Summary table

| Written as | Means | `ndim` | `size` | Everyday name |
| --- | --- | --- | --- | --- |
| `()` | one number, held as an array | 0 | 1 | scalar |
| `(3,)` | three numbers in a line | 1 | 3 | 1D array |
| `(1, 3)` | one row of three | 2 | 3 | row vector |
| `(3, 1)` | three rows of one | 2 | 3 | column vector |
| `(2, 3)` | two rows of three | 2 | 6 | matrix, or table |
| `(2, 2, 2)` | two stacked 2 by 2 grids | 3 | 8 | 3D array, or tensor |

| If you see this | It means | What to do |
| --- | --- | --- |
| `cannot reshape array of size 12 into shape (5,3)` | the new shape's numbers do not multiply to the number of items | check `size` against the shape you asked for |
| a result far larger than expected | two shapes were broadcast together | print `.shape` of both operands before the operation |
| `(3,)` where you expected a column | a 1D array is neither a row nor a column | `reshape(3, 1)`, or `reshape(-1, 1)` |

---

## Complete practice script

Everything above in one block, ready to copy and run.

```python
import numpy as np

# Step 1 - shape, ndim and size for arrays of different dimensions
for name, arr in [("1D", np.array([10, 20, 30])),
                  ("2D", np.array([[1, 2, 3], [4, 5, 6]])),
                  ("3D", np.arange(8).reshape(2, 2, 2)),
                  ("0D", np.array(7))]:
    print(f"{name}: shape {arr.shape}, ndim {arr.ndim}, size {arr.size}")

# Step 2 - the same three numbers in three shapes
a = np.array([10, 20, 30])
print("\nflat  ", a.shape, " row", a.reshape(1, 3).shape, " column", a.reshape(3, 1).shape)

# Step 3 - reshape, including the -1 shortcut
d = np.arange(12)
print("reshape(3, 4) ->", d.reshape(3, 4).shape,
      " reshape(3, -1) ->", d.reshape(3, -1).shape,
      " reshape(-1, 6) ->", d.reshape(-1, 6).shape)

# Step 4 - a reshape that cannot work
try:
    d.reshape(5, 3)
except ValueError as error:
    print("reshape(5, 3) ->", error)

# Step 5 - shape drives the axis argument
scores = np.array([[70, 65, 80], [90, 85, 75], [60, 72, 88], [95, 91, 89]])
print("\nscores", scores.shape,
      "  mean(axis=0)", scores.mean(axis=0).shape,
      "  mean(axis=1)", scores.mean(axis=1).shape,
      "  transposed", scores.T.shape)
```

**Output**

```text
1D: shape (3,), ndim 1, size 3
2D: shape (2, 3), ndim 2, size 6
3D: shape (2, 2, 2), ndim 3, size 8
0D: shape (), ndim 0, size 1

flat   (3,)  row (1, 3)  column (3, 1)
reshape(3, 4) -> (3, 4)  reshape(3, -1) -> (3, 4)  reshape(-1, 6) -> (2, 6)
reshape(5, 3) -> cannot reshape array of size 12 into shape (5,3)

scores (4, 3)   mean(axis=0) (3,)   mean(axis=1) (4,)   transposed (3, 4)
```

---

## Follow-up questions for practice

1. An array has shape `(4, 5)`. How many numbers does it hold? Name three
   other shapes the same numbers could be reshaped into, and one that they
   could not.
2. `np.arange(6).reshape(2, 3)` and `np.arange(6).reshape(3, 2)` hold the
   same six numbers. Write down, without running anything, what each one
   prints. Then check.
3. Why does `np.array([1, 2, 3]).shape` print `(3,)` rather than `(3)`?
   What would `(3)` mean in ordinary Python?
4. Take the `scores` array from section 5. Which `axis` would you use to
   find each student's *highest* mark? What shape would the answer have?
5. `x = np.arange(10)`. What does `x.reshape(-1, 1).shape` give, and why is
   that a useful thing to be able to write when you do not know how many
   numbers `x` holds?
6. Create a `(2, 3)` array, reshape it to `(3, 2)`, and change one value in
   the reshaped version. Does the original change? Now do the same with
   `.flatten()` instead. Explain the difference in your own words.
