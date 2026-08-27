


# Chapter 11 — 1D Arrays: `hstack()`, `vstack()`, and `concatenate()`

## About this chapter

Once you have two separate NumPy arrays, a very common next step is joining
them together. NumPy gives you three tools for this — `np.hstack()`,
`np.vstack()`, and `np.concatenate()` — and at first glance they can seem
interchangeable. This chapter focuses specifically on what happens when you
apply them to **1D arrays** (plain, flat lists of numbers with no separate
row/column structure), because this is exactly the case where their
behaviour quietly diverges in a way that trips up a lot of beginners.

Note that for 1D arrays, `hstack()` and
`vstack()` are *not* simply "horizontal" and "vertical" versions of the
same operation. One of them secretly changes the number of dimensions your
data has; the other doesn't.

> **Quick glossary, before we start**
> - **Axis** — a "direction" along which an array's values are arranged.
>   A 1D array has only one axis, `axis=0`. A 2D array has two: `axis=0`
>   (down the rows) and `axis=1` (across the columns).
> - **Shape** — a tuple describing an array's size along each axis. `(4,)`
>   means a flat array of 4 values; `(2, 2)` means 2 rows and 2 columns.
> - **`concatenate()`** — NumPy's general-purpose joining function; you
>   tell it explicitly which axis to join along.
> - **`hstack()` / `vstack()`** — convenience shortcuts built on top of
>   `concatenate()`, covering the two most common cases ("horizontal" and
>   "vertical" joining) without you needing to specify an axis yourself.
> - **Reshape** — rearranging the same values into a different shape,
>   without changing the values themselves. See the
>   [NumPy reshape documentation](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html).

## Key points to remember

- **`np.concatenate()` is the foundation** — you control the axis manually.
- **`np.hstack()` and `np.vstack()` are shortcuts** built on top of it.
- **`hstack` = horizontal (joins along columns); `vstack` = vertical (joins along rows).**
- **For 1D arrays specifically, `vstack()` adds a new dimension, while `hstack()` does not.** This last point is worthg noting .

---

## Step-by-Step Visualization

We start with two 1D arrays in NumPy:

```python
x = np.array([1, 2])
y = np.array([3, 4])
```

### Step 1: How NumPy "sees" 1D arrays

A 1D array has **shape `(2,)`**, meaning it's a flat list of values with no
row/column structure at all:

For `x`:

```
     x → [1   2]
          ↑   ↑
    index 0,  1
```

For `y`:

```
     y → [3   4]
          ↑   ↑
    index 0,  1
```

👉 **Important:**

- There is **no row/column distinction yet** — a 1D array is neither a row
  nor a column, it's simply a flat sequence.
- Since there's only one dimension, there's only **one axis**: `axis=0`.
  A 1D array has no `axis=1` to speak of — this single fact is the root
  cause of the different behaviour you're about to see.

![Flowchart](/resources/ch-11-numpy-august-2026-hstack-vstack.png)



---

### Step 2: `np.hstack((x, y))`

**Operation:** "join along the existing axis."

Since a 1D array only has `axis=0` to begin with, `hstack()` simply joins
the two flat sequences end-to-end along that one axis:

```
[1   2]  +  [3   4]
 ↓           ↓
Concatenate along axis 0
```

**Result:**

```
[1   2   3   4]
```

**Shape:** `(4,)` — still flat, just longer.

---

### Step 3: `np.concatenate((x, y), axis=0)`

This is **exactly the same operation** as Step 2, just spelled out
explicitly:

```
[1   2]  +  [3   4]
 ↓           ↓
axis = 0
```

**Result:**

```
[1   2   3   4]
```

**Key insight:**

> For 1D arrays, **`hstack()` is identical to `concatenate(axis=0)`.**

![Flowchart](/resources/ch-11-numpy-august-2026-hstack-vstack--2.png)



---

### Step 4: `np.vstack((x, y))`

Here's where things change.

#### Step 4A: The hidden reshaping step

`vstack()` first **silently converts** each 1D array into a 2D **row
vector**, before doing anything else:

```
x → [[1   2]]   shape (1, 2)   -- 1 row, 2 columns
y → [[3   4]]   shape (1, 2)   -- 1 row, 2 columns
```

This reshape happens **automatically and invisibly** — it's the single
most important detail in this whole chapter, because it's exactly what
`hstack()` never does.

#### Step 4B: Stack the (now 2D) rows along axis 0

```
[[1   2]]
[[3   4]]
```

**Final result:**

```
[[1   2]
 [3   4]]
```

**Shape:** `(2, 2)` — a genuine 2D matrix now, with 2 rows and 2 columns.

![Flowchart](/resources/ch-11-numpy-august-2026-hstack-vstack--3.png)



---

### Side-by-Side Comparison

| Operation | Internal step | Result | Shape |
| --- | --- | --- | --- |
| `hstack((x, y))` | No reshape | `[1 2 3 4]` | `(4,)` |
| `concatenate((x, y), axis=0)` | No reshape | `[1 2 3 4]` | `(4,)` |
| `vstack((x, y))` | Reshape → `(1, 2)` each, then stack | `[[1 2], [3 4]]` | `(2, 2)` |

**Beginner tip:** if you ever get a result with an unexpected extra
dimension after using `vstack()`, this hidden reshaping step is almost
always why. `hstack()` on 1D arrays never adds a dimension; `vstack()` on
1D arrays always does.

---

## Script 1 — A 1D-array demonstration

The walkthrough above uses the 1D arrays `x = [1, 2]` and `y = [3, 4]`.
Here's a runnable script using exactly those arrays, so you can confirm
every result from the walkthrough for yourself.

```python
# Demonstrating hstack, vstack, and concatenate on genuine 1D arrays
import numpy as np

# Step 1 - Create two 1D arrays. Each has shape (2,) — a flat sequence,
# with no row/column distinction and only one axis: axis=0.
x = np.array([1, 2])
y = np.array([3, 4])
print("x shape:", x.shape, "| y shape:", y.shape)

# Step 2 - np.hstack(): joins end-to-end along the ONLY axis 1D arrays
# have (axis 0). No reshaping happens — the result stays 1D.
h_stack = np.hstack((x, y))
print(f"\nhstack result: {h_stack}")
print(f"hstack shape: {h_stack.shape}")   # (4,) — still flat

# Step 3 - np.concatenate(axis=0): does exactly the same thing as hstack
# here, because 1D arrays only have axis 0 to join along in the first place.
concat_result = np.concatenate((x, y), axis=0)
print(f"\nconcatenate(axis=0) result: {concat_result}")
print(f"concatenate(axis=0) shape: {concat_result.shape}")   # (4,) — same as hstack

# Step 4 - np.vstack(): FIRST silently reshapes each 1D array into a
# (1, 2) row vector, THEN stacks those rows. This is why the result
# gains an extra dimension that hstack() never introduces.
v_stack = np.vstack((x, y))
print(f"\nvstack result:\n{v_stack}")
print(f"vstack shape: {v_stack.shape}")   # (2, 2) — now genuinely 2D

# Step 5 - Confirm hstack and vstack really do behave differently on the
# SAME two 1D input arrays.
print("\n--- Summary ---")
print(f"hstack:      shape {h_stack.shape} -> {h_stack}")
print(f"concatenate: shape {concat_result.shape} -> {concat_result}")
print(f"vstack:      shape {v_stack.shape} ->\n{v_stack}")
```

**Expected output:**

```
x shape: (2,) | y shape: (2,)

hstack result: [1 2 3 4]
hstack shape: (4,)

concatenate(axis=0) result: [1 2 3 4]
concatenate(axis=0) shape: (4,)

vstack result:
[[1 2]
 [3 4]]
vstack shape: (2, 2)

--- Summary ---
hstack:      shape (4,) -> [1 2 3 4]
concatenate: shape (4,) -> [1 2 3 4]
vstack:      shape (2, 2) ->
[[1 2]
 [3 4]]
```

---

## Script 2 — The same three functions on 2D row vectors, for comparison

> **A note on this script:** unlike Script 1 above, the arrays here —
> `a = np.array([[1, 2]])` and `b = np.array([[3, 4]])` — are already **2D**
> row vectors with shape `(1, 2)`, not 1D arrays with shape `(2,)`. That's
> intentional: comparing this script against Script 1 is a good way to see
> that once your arrays already have two dimensions, `hstack()` gains
> access to `axis=1` (joining columns), which simply doesn't exist for a
> genuinely 1D array. This is exactly why `hstack()` behaves differently
> here than it did in Script 1.

```python
# Demonstrating hstack, vstack, and concatenate on 2D row-vector arrays
import numpy as np

# Step 1 - Create two 2D row vectors. Note the DOUBLE square brackets —
# each array already has shape (1, 2): 1 row, 2 columns.
a = np.array([[1, 2]])
b = np.array([[3, 4]])
print("a shape:", a.shape, "| b shape:", b.shape)

# Step 2 - Horizontal stack: since these are already 2D, hstack() joins
# them along axis=1 (side by side, adding columns).
h_stack = np.hstack((a, b))
print(f"\nHorizontal stack:->{h_stack} \nShape:-> {h_stack.shape}\n")
# Output:
# Horizontal stack:->[[1 2 3 4]]
# Shape:-> (1, 4)

# Step 3 - The equivalent explicit call using concatenate, specifying
# axis=1 directly (concatenate never guesses the axis for you).
h_stack_concat = np.concatenate((a, b), axis=1)
print(f"Horizontal stack using concatenate:->{h_stack_concat} \nShape:-> {h_stack_concat.shape}\n")
# Output:
# Horizontal stack using concatenate:->[[1 2 3 4]]
# Shape:-> (1, 4)

# Step 4 - Vertical stack: joins along axis=0 (stacked as new rows).
# Unlike the 1D case, no hidden reshape is needed here — a and b are
# already 2D row vectors, so vstack just stacks them as-is.
v_stack = np.vstack((a, b))
print(f"Vertical stack:->{v_stack} \nShape:-> {v_stack.shape}\n")
# Output:
# Vertical stack:->[[1 2]
#                   [3 4]]
# Shape:-> (2, 2)

# Step 5 - The equivalent explicit call using concatenate with axis=0.
# Note: concatenate() ALWAYS requires you to state the axis yourself —
# it has no built-in default the way hstack/vstack do.
v_stack_concat = np.concatenate((a, b), axis=0)
print(f"Vertical stack using concatenate:->{v_stack_concat} \nShape:-> {v_stack_concat.shape}\n")
# Output:
# Vertical stack using concatenate:->[[1 2]
#                                      [3 4]]
# Shape:-> (2, 2)
```

---

## Putting Script 1 and Script 2 side by side

| | Script 1 — genuine 1D arrays `(2,)` | Script 2 — 2D row vectors `(1, 2)` |
| --- | --- | --- |
| `hstack()` joins along | `axis=0` (the only axis available) | `axis=1` (columns) |
| Does `hstack()` reshape first? | No | No (already 2D) |
| `vstack()` joins along | `axis=0`, **after** an invisible reshape to `(1, 2)` | `axis=0` (no reshape needed — already 2D) |
| Result shape after `hstack()` | `(4,)` | `(1, 4)` |
| Result shape after `vstack()` | `(2, 2)` | `(2, 2)` |

**Beginner tip:** notice that `vstack()` produces the *same-looking*
`(2, 2)` result in both scripts — but for a genuinely 1D input, that shape
only appears because of the hidden reshape step from Step 4A above. Always
check `.shape` on your *inputs*, not just your output, if a stacking result
ever surprises you.

---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing.)*

1. What would `np.hstack((x, y))` do if `x` and `y` had different lengths,
   e.g. `x = np.array([1, 2, 3])` and `y = np.array([4, 5])`? Would it
   still work? Try it and check.
2. Using `x = np.array([1, 2])` and `y = np.array([3, 4])` from Script 1,
   what shape would `np.concatenate((x, y), axis=1)` produce — or does it
   raise an error? Predict it first, then check, and explain your result
   using what you know about 1D arrays only having `axis=0`.
3. Take `a = np.array([[1, 2]])` from Script 2 and check `a.ndim` (the
   number of dimensions). Compare it to `x.ndim` from Script 1. How does
   this connect to why `hstack()` behaves differently between the two
   scripts?
4. Using `np.array([1, 2]).reshape(1, 2)`, manually reproduce what
   `vstack()` does internally to a 1D array in Step 4A. Does the result
   match what the walkthrough describes?






