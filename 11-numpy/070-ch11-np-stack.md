


# Chapter 11 — Project: Combining Arrays into a New Dimension with `np.stack()`

## About this chapter

This project looks at `np.stack()` — a NumPy function that behaves quite
differently from the joining tools covered earlier in this chapter
(`concatenate()`, `hstack()`, `vstack()`). Those tools combine arrays
**within their existing number of dimensions**: two 2D arrays joined with
`vstack()` stay 2D. `np.stack()` does something more interesting: it
**adds a brand-new dimension**, one that didn't exist in the original
arrays at all.

This matters in practice more than it might sound like at first. It's
exactly the tool used, for example, to combine many individual images into
one "batch" for a machine-learning model, or to combine several days' data
into one month's worth of readings — in both cases, you want to keep each
original piece identifiable as its own "layer," not blended together.
That's precisely what a new dimension gives you.

> **Glossary of terms**
> - **Dimension / axis** — a "direction" along which an array's data is
>   arranged. A 2D array has 2 axes; a 3D array has 3.
> - **Shape** — a tuple describing an array's size along each axis, e.g.
>   `(2, 2, 2)` means 2 along each of 3 axes.
> - **Tensor** — a general term for an array of any number of dimensions;
>   you'll often see 3D-and-higher arrays called "tensors," especially in
>   machine-learning contexts. See the
>   [NumPy basics guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
>   for more on array dimensionality.
> - **Batch** (in machine learning) — a group of individual data samples
>   (e.g. images) combined into one array so a model can process them
>   together, rather than one at a time.

---

## Project / Research Question

> "In Machine Learning, we often need to combine multiple independent 2D
> datasets (like images or classroom records) into a single 3D structure
> without losing the identity of the original groups. Investigate the
> `np.stack()` function in NumPy. Explain how it differs from traditional
> joining methods like `vstack` and `hstack`. Demonstrate, through a Python
> script, how to create a 3D 'Data Cube' from 2D sources, and discuss the
> architectural implications of stacking along different axes (Axis 0 vs.
> Axis 1)."

---

# Answer & Technical Note: Understanding `np.stack()`

## 1. The Core Concept

Standard joining functions (`concatenate()`, `vstack()`, `hstack()`) work
**within existing dimensions** — if you join two 2D arrays with any of
these, the result is still 2D.

`np.stack()`, by contrast, is a **dimension upgrader**. It takes a
sequence of arrays that all share the *same* shape, and joins them along a
**new axis** that didn't exist before.

- Stack two 1D vectors → you get a 2D matrix.
- Stack two 2D matrices → you get a 3D tensor.

**Analogy:**

- **`vstack()`** — taping two pages together end-to-end to make one longer
  page. You still have one page; it's just bigger.
- **`stack()`** — placing one page on top of another to start a book. You
  now have a "page number" dimension that simply didn't exist before.


![Flowchart](/resources/ch-11-numpy-august-2026-combining-arrays-into-new-dimensions-2.png)




---

## 2. Common Use Cases

*(Slightly more advanced context — safe to skim on a first read.)*

- **Image batching (AI):** combining 32 individual images (each `28 x 28`
  pixels) into a single "batch" array of shape `(32, 28, 28)` for a neural
  network to process together.
- **Time-series data:** stacking daily sales reports (each 2D) into one
  monthly report (3D), with each day kept as its own identifiable layer.
- **Multi-sensor data:** stacking readings from "Sensor A" and "Sensor B"
  while keeping each sensor's data separate but aligned, position for
  position.

---

## 3. Comparative Table: `vstack` vs. `hstack` vs. `stack`

| Feature | `np.vstack()` | `np.hstack()` | `np.stack()` |
| --- | --- | --- | --- |
| Dimension change | Stays the same (e.g. 2D stays 2D) | Stays the same (e.g. 2D stays 2D) | Increases (e.g. 2D → 3D) |
| What it does | Adds more rows | Adds more columns | Adds a brand-new axis |
| Analogy | A longer list | A wider table | A stack of separate papers |
| Shape requirement | Columns must match | Rows must match | Every input array's shape must be **identical** |

---

## 4. Do's and Don'ts, and Common Errors

**DO:**

- Use `np.stack()` when you want to keep the original arrays as distinct,
  individually addressable "sub-entities" — e.g. `stacked[0]` is Class A,
  `stacked[1]` is Class B.
- Make sure every input array has the **exact same shape** before stacking.

**DON'T:**

- Use `stack()` if you simply want to append data onto an existing array —
  use `vstack()` or `concatenate()` for that instead.
- Forget to check the `axis` parameter. Stacking along `axis=0` versus
  `axis=1` produces genuinely different 3D structures (this is the main
  focus of Section 6, below).

**Common errors:**

- `ValueError: all input arrays must have the same shape` — happens if,
  say, Array A is shape `(3, 4)` and Array B is shape `(3, 5)`. Unlike
  `hstack()`, `stack()` requires every input to match exactly, with no
  exceptions.
- `IndexError` — happens if you try to access, say, `axis=2` on an array
  that only has 2 axes to begin with.

---

## 5. A First, Simple Script

Before tackling a full "data cube," here's the smallest possible
demonstration: stacking two 1D vectors, once along `axis=0` and once along
`axis=1`.

```python
import numpy as np

# Step 1 - Create two simple 1D arrays to stack.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Step 2 - Stack along axis=0: the new axis is inserted FIRST,
# so a and b each become one ROW of the result.
result = np.stack((a, b), axis=0)
print(result.shape)   # (2, 3)
print(result)
# Output:
# [[1 2 3]
#  [4 5 6]]
# Two 1D arrays became 2 rows.

# Step 3 - Stack along axis=1: the new axis is inserted SECOND,
# so a and b are instead interleaved element-by-element as COLUMNS.
result2 = np.stack((a, b), axis=1)
print(result2.shape)   # (3, 2)
print(result2)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
# Two 1D arrays became 2 columns.
```

---

## 6. Understanding `axis` — the essential part

### The rule

**`axis` tells `np.stack()` *where* the new dimension gets inserted.**

### Example: `axis=0`

```python
np.stack((a, b), axis=0)

# Result:
# [[1 2 3]
#  [4 5 6]]
#
# Shape: (2, 3)
# The new axis is added at position 0 -> the two arrays become rows.
```

### Example: `axis=1`

```python
np.stack((a, b), axis=1)

# Result:
# [[1 4]
#  [2 5]
#  [3 6]]
#
# Shape: (3, 2)
# The new axis is added at position 1 -> the two arrays become columns.
```

### Visual intuition

![Flowchart](/resources/ch-11-numpy-august-2026-combining-arrays-into-new-dimensions-3.png)

---

## 7. Building a 3D "Data Cube": Two Classes, Two Students, Two Subjects

This section directly answers the project's request to build a 3D "data
cube" from 2D sources, and to compare stacking along `axis=0` vs. `axis=1`
(with `axis=-1` shown as a bonus third option).

```python
# SCRIPT: Understanding np.stack() with a real "data cube" example
import numpy as np

# -----------------------------------------------------------------
# STEP 1 - Create two classes' worth of marks, in 2 subjects (Math, Science).
# Each class has 2 students and 2 subjects, so each class's shape is (2, 2).
#
#           Math   Science
# Student 1:  80,     85
# Student 2:  70,     75
# -----------------------------------------------------------------
class_a = np.array([[80, 85],
                     [70, 75]])   # 2 students x 2 subjects

class_b = np.array([[95, 90],
                     [60, 65]])

print("Shape of one class:", class_a.shape)   # (2, 2)


# -----------------------------------------------------------------
# STEP 2 - Stack along axis=0: the new axis is inserted FIRST.
# Interpretation of the resulting shape: [Class, Student, Subject]
# -----------------------------------------------------------------
school_axis0 = np.stack((class_a, class_b), axis=0)   # shape: (2, 2, 2)

print("\nAxis 0 (Class first)")
print(school_axis0)
# Output:
# [[[80 85]
#   [70 75]]
#  [[95 90]
#   [60 65]]]

print("Shape:", school_axis0.shape)   # (2, 2, 2)

print("Class A:\n", school_axis0[0])
# Output: Class A:
# [[80 85]
#  [70 75]]

print("Class B:\n", school_axis0[1])
# Output: Class B:
# [[95 90]
#  [60 65]]


# -----------------------------------------------------------------
# STEP 3 - Stack along axis=1: the new axis is inserted in the MIDDLE.
# Interpretation of the resulting shape: [Student, Class, Subject]
# -----------------------------------------------------------------
school_axis1 = np.stack((class_a, class_b), axis=1)   # shape: (2, 2, 2)

print("\nAxis 1 (Student first)")
print(school_axis1)
# Output:
# [[[80 85] [95 90]]
#  [[70 75] [60 65]]]

print("Shape:", school_axis1.shape)   # (2, 2, 2)

print("Student 0 from both classes:\n", school_axis1[0])
# Output: Student 0 from both classes:
# [[80 85]
#  [95 90]]

print("Student 1 from both classes:\n", school_axis1[1])
# Output: Student 1 from both classes:
# [[70 75]
#  [60 65]]


# -----------------------------------------------------------------
# STEP 4 - Stack along axis=-1 (the LAST axis): a bonus third option.
# Interpretation of the resulting shape: [Student, Subject, Class]
# This groups each student's SAME subject across both classes together —
# handy for directly comparing one subject, side by side, class vs class.
# -----------------------------------------------------------------
school_last = np.stack((class_a, class_b), axis=-1)   # shape: (2, 2, 2)

print("\nAxis -1 (Subject comparison)")
print(school_last)
# Output:
# [[[80 95]
#   [85 90]]
#  [[70 60]
#   [75 65]]]

print("Shape:", school_last.shape)   # (2, 2, 2)

print("Student 0, Subject 0 (Math) comparison:\n", school_last[0, 0])
# Output: [80 95] -> Student 0's Math score in Class A, then Class B

print("Student 0, Subject 1 (Science) comparison:\n", school_last[0, 1])
# Output: [85 90]

print("Student 1, Subject 0 (Math) comparison:\n", school_last[1, 0])
# Output: [70 60]

print("Student 1, Subject 1 (Science) comparison:\n", school_last[1, 1])
# Output: [75 65]
```

### Reading the three results at a glance

| Stacked along | Resulting shape | How to read `result[i]` | Best suited for |
| --- | --- | --- | --- |
| `axis=0` | `(2, 2, 2)` — `[Class, Student, Subject]` | "Everything about Class `i`" | Comparing whole classes to each other |
| `axis=1` | `(2, 2, 2)` — `[Student, Class, Subject]` | "Everything about Student `i`, across both classes" | Comparing one student's performance across classes |
| `axis=-1` | `(2, 2, 2)` — `[Student, Subject, Class]` | "Student/Subject combination, compared class by class" | Comparing one subject's score directly, class vs. class |

**Beginner tip:** all three results have the *identical* shape, `(2, 2,
2)` — the numbers stored are the same too, just arranged differently. What
changes is *which question your indexing answers most naturally*. Choosing
the right axis is really about choosing what you want `result[0]`,
`result[1]`, etc. to mean for your particular problem.

---

## Flowchart

The following flowchart visualizes the script above and shows the three
possible ways `np.stack()` was used:


![Diagram](/resources/ch11-np-stack.png)



## Another flowchart
![Flowchart](/resources/ch-11-numpy-august-2026-combining-arrays-into-new-dimensions-1.png)

---

## 8. Do Arrays Need to Be the Same Shape?

**Yes — every input array must have exactly the same shape.**

**Why?** Because `np.stack()` does **not** stretch, reshape, or broadcast
its inputs the way some other NumPy operations do. It simply places
matching-sized blocks one after another along a new axis — think of
placing identically-sized building blocks on top of each other. If the
blocks are different sizes, there's no sensible way to stack them.

**Example (this raises an error):**

```python
import numpy as np

a = np.array([1, 2, 3])   # length 3
b = np.array([4, 5])      # length 2

np.stack((a, b))
# ValueError: all input arrays must have the same shape
```

**Reason for the error:** `a` has length `3`, `b` has length `2` — there's
no way to line them up element-by-element, so `np.stack()` refuses rather
than guessing.

---

## 9. Architectural Implications: Axis 0 vs. Axis 1

The project question specifically asks about the *architectural*
consequences of choosing `axis=0` vs. `axis=1` when designing a data
structure — in other words, not just "what shape do I get," but "what does
that shape choice mean for how I'll use the data afterward."

- **`axis=0` ("Class first")** treats each original 2D array as a
  complete, self-contained **unit**. This is the natural choice when your
  code will mostly operate on *one whole group at a time* — e.g. "run this
  analysis on Class A's data, then separately on Class B's."
- **`axis=1` ("Student first")** instead treats matching *positions*
  across the original arrays as the natural unit. This is the better
  choice when your code will mostly operate *across* groups for the same
  entity — e.g. "compare Student 0's performance across every class."

Neither choice is "more correct" in general — the right axis depends
entirely on which direction you'll be slicing and iterating through the
data most often in the code that comes afterward. Choosing the axis that
matches your most common access pattern up front can save you from writing
extra `.transpose()` calls throughout the rest of your program.

---

## Summary

| Concept | Key takeaway |
| --- | --- |
| `np.stack()` vs. `vstack()`/`hstack()`/`concatenate()` | Stack **adds** a new dimension; the others work within existing dimensions |
| Shape requirement | All input arrays must have the exact same shape — no broadcasting |
| `axis` parameter | Controls *where* the new dimension is inserted, which changes how you index the result afterward |
| Common use cases | Image batching, time-series stacking, multi-sensor data |
| Choosing an axis | Match it to how you'll most often slice/access the data afterward |

---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing.)*

1. Using `class_a` and `class_b` from Section 7, what would
   `school_axis0[0][1]` give you? Predict it in words before running the
   code (hint: think through the `[Class, Student, Subject]` ordering).
2. If you had **three** classes instead of two, all shaped `(2, 2)`, what
   would the resulting shape be after `np.stack((class_a, class_b,
   class_c), axis=0)`? Try it and confirm.
3. Using the error example in Section 8, what change would you need to
   make to `b = np.array([4, 5])` so that `np.stack((a, b))` succeeds
   without changing `a`?
4. In Section 9, if your code was going to loop "for each subject, compare
   both classes," which axis choice (`axis=0`, `axis=1`, or `axis=-1`)
   would make that loop the most natural to write? Explain your reasoning
   using the table in Section 7.





