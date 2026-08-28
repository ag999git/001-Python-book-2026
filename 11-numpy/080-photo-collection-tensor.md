

# Chapter 11 — Case Study: Organizing a Large Photo Archive into a Structured Tensor

## About this chapter

This case study ties together several NumPy ideas from earlier in this
chapter — arrays, shapes, and especially `np.stack()` — into one realistic,
end-to-end example: turning a messy folder of photos into a single, tidy
NumPy array that a machine-learning model could actually work with.

It's a deliberately practical scenario. Real photo collections aren't
naturally "array-shaped" — they're nested folders, inconsistent file
counts, and (usually) wildly different image sizes. This case study walks
through exactly what has to be true about your data before NumPy can
represent it as one clean structure, and then builds that structure up one
dimension at a time, so that by the end, a **6-dimensional array** (yes,
six!) feels like a natural, logical destination rather than an intimidating
wall of numbers.

> **Quick glossary, before we start**
> - **Tensor** — a general term for an array with any number of
>   dimensions; a photo collection organized as described here ends up
>   being a 6D tensor. See the
>   [NumPy basics guide](https://numpy.org/doc/stable/user/absolute_beginners.html).
> - **Dimension / axis** — one "direction" along which an array's data is
>   arranged; a 6D tensor has 6 such directions.
> - **RGB channel** — a digital image is usually stored as three separate
>   "layers" of brightness values — Red, Green, and Blue — which combine to
>   produce every visible colour. See
>   [a plain-language explanation of RGB colour](https://www.rapidtables.com/web/color/RGB_Color.html).
> - **`dtype` (data type)** — what *kind* of number an array stores.
>   `np.uint8` means "an unsigned 8-bit integer," i.e. a whole number from
>   `0` to `255` — exactly the range a single RGB colour channel needs.
> - **Simulated / random data** — since this case study is about
>   *structure*, not real photography, the actual pixel values are
>   generated randomly. The techniques shown work identically on real
>   image data loaded from disk.

---

## 1. Research Scenario


Alex, a field researcher and photographer, has collected thousands of
images over several years. His dataset includes photographs from different
domains such as:

### Collections (`C`)

1. **Wildlife Expedition**
2. **Family Events**
3. **Urban Landscapes**

### Categories within each collection (`K`)

**Wildlife Expedition**
- Safari (daytime animals)
- Night Watch (nocturnal animals)

**Family Events**
- Weddings
- Birthdays

**Urban Landscapes**
- Architecture
- Street Life

### Images within each category (`N`)

Each category contains multiple images. For example:

**Wildlife → Safari:**
- `lion_01.jpg`
- `elephant_02.jpg`
- `deer_03.jpg`
- `zebra_04.jpg`

**Urban → Street Life:**
- `market_01.jpg`
- `traffic_02.jpg`
- `vendor_03.jpg`
- `crowd_04.jpg`

---

## 2. Research Problem



> Alex wants to convert this unstructured collection of images into a
> structured format suitable for machine learning analysis.

---

## 3. Constraints



To process the data using NumPy, the dataset must satisfy:

- All images must have the **same resolution** → `(H, W)`
- All images must have **3 channels (RGB)**
- Each category must contain the **same number of images (N)**

**In plain terms:** NumPy arrays are rigid, regular grids — every "slot"
at a given level must be the same size and shape as every other slot at
that level. A folder of photos in the real world rarely satisfies this
automatically (some photos might be a different size, or one folder might
have three photos while another has five), so meeting these three
constraints is usually a genuine **preprocessing step** (resizing images,
discarding or padding to equalize counts) before this structure becomes
possible.

---

## 4. Target Tensor Structure



`(C, K, N, H, W, 3)`

| Symbol | Meaning |
| --- | --- |
| `C` | Collections |
| `K` | Categories per collection |
| `N` | Images per category |
| `H` | Height |
| `W` | Width |
| `3` | RGB channels |


![Flowchart](/resources/ch-11-numpy-august-2026-organizing-photo-collection-1.png)

---

## 5. Task

*(Reproduced from the printed book — unchanged.)*

### Objective

Convert the dataset into a **6D tensor** of shape:

`(3, 2, 4, 64, 64, 3)`

### Tasks

1. Assume:
   - 3 collections
   - 2 categories per collection
   - 4 images per category
   - Resolution = 64 × 64
   - RGB channels = 3
2. Simulate image data using random numbers
3. Build:
   - One collection → `(2, 4, 64, 64, 3)`
   - Multiple collections → stack into `(3, 2, 4, 64, 64, 3)`
4. Verify shapes at each step

---

## 6. Conceptual Theory (Step by Step)

*(Reproduced from the printed book — unchanged, with an added visual.)*

| Step | Level | Shape |
| --- | --- | --- |
| Step 1 | Pixel level | `[R, G, B]` |
| Step 2 | Image level | `(H, W, 3)` |
| Step 3 | Category level | `(N, H, W, 3)` |
| Step 4 | Collection level | `(K, N, H, W, 3)` |
| Step 5 | Dataset level | `(C, K, N, H, W, 3)` |

### Conceptual visualization

```
Dataset
│
├── Collection 1 (Wildlife)
│   ├── Safari
│   │   ├── lion_01
│   │   ├── elephant_02
│   │   └── ...
│   └── Night Watch
│
├── Collection 2 (Family)
│   ├── Wedding
│   └── Birthday
│
└── Collection 3 (Urban)
    ├── Architecture
    └── Street Life
```

Here's the same folder structure as flowchart:

![Flowchart](/resources/ch-11-numpy-august-2026-organizing-photo-collection-2.png)



**Beginner tip:** notice that Steps 1–5 above are simply the same tensor
structure from Section 4, but built up **one level at a time**. This is a
useful way to check your own understanding of any high-dimensional array:
if you can name what each single additional axis represents, in order, you
understand the structure — even if the total number of dimensions looks
intimidating at first glance.

---

## 7. Full Script with Explanation

### 7(A) How `np.random.randint()` creates a multi-dimensional tensor

Before building the full dataset, it helps to understand exactly how
NumPy turns a `size=` argument into a structured, multi-dimensional array
of random numbers:

```python
one_collection = np.random.randint(
    0, 256,
    size=(K, N, H, W, CH),
    dtype=np.uint8
)
```

**How it works, step by step:**

| Step | What happens |
| --- | --- |
| 1. Range of values | `0, 256` tells NumPy to generate whole numbers from **0 up to (not including) 256** — exactly the valid range for a single RGB colour channel |
| 2. Total element count | The `size=(K, N, H, W, CH)` tuple tells NumPy exactly how many random values to generate in total: `K × N × H × W × CH` |
| 3. Arranging into shape | NumPy then arranges that flat pool of random numbers into the requested multi-dimensional shape `(K, N, H, W, CH)` |
| 4. Interpretation | The result reads as: categories → images → pixel rows → pixel columns → RGB values, with `[R, G, B]` sitting at the very deepest level |
| 5. Data type | `dtype=np.uint8` stores each value as an 8-bit unsigned integer (0–255) — the standard, memory-efficient choice for image pixel data |

**Key insight:** `np.random.randint()` first generates one large, flat pool
of random numbers, and only afterward arranges them into whatever shape
you asked for via `size=`. The shape doesn't change *how many* numbers get
generated — only how they're organized once generated.

---

### 7(B) How five 5D tensors become one 6D tensor

Real datasets are often built up step by step, rather than all at once.
Here's exactly how that happens for this photo archive:

**Step 1 — Create one 5D tensor (one collection)**

A single collection — say, Wildlife — is represented as:

`(K, N, H, W, CH)`

**Step 2 — Store multiple collections in a plain Python list**

```python
collection_list = [collection1, collection2, collection3]
```

Each item in this list is itself a full 5D tensor of shape `(K, N, H, W,
CH)`. **Important:** at this point, `collection_list` is still just an
ordinary Python list of separate arrays — it is *not yet* a single 6D
tensor.

**Step 3 — Use `np.stack()` to introduce a new axis**

```python
dataset = np.stack(collection_list, axis=0)
```

`np.stack()` takes each item in the list and gives it a position along a
**brand-new axis**, then combines everything into one single array.

![Flowchart](/resources/ch-11-numpy-august-2026-organizing-photo-collection-3.png)



**Resulting shape:** `(C, K, N, H, W, CH)`, where `C` is simply the number
of collections in the original list.

**Key insight:** `np.stack()` uses each list item's **position (index)**
in the list to create the new dimension — `collection_list[0]` becomes
`dataset[0]`, `collection_list[1]` becomes `dataset[1]`, and so on. The
list index literally *becomes* `axis=0` in the resulting tensor.

**Summary of the whole process:** we first build individual 5D tensors, one
per collection; we collect those tensors into an ordinary Python list; and
`np.stack()` then converts that list into a single, higher-dimensional
tensor by introducing a new axis that corresponds exactly to each
collection's position in the list.

---

### 7(C) The complete script

Every stage below is labelled with a `# Step N -` comment, matching the
task list in Section 5, with extra explanation added wherever a beginner
is likely to pause and ask "wait, why that number?"

```python
import numpy as np

# ---------------------------------------------------
# Step 1 - Define the dataset's structure as plain numbers first.
# Naming each dimension up front makes the rest of the script much
# easier to follow, and matches the (C, K, N, H, W, CH) structure
# from Section 4.
# ---------------------------------------------------

C = 3    # Number of collections (Wildlife, Family, Urban) -> will become axis 0, added later via stacking
K = 2    # Categories per collection (e.g. Safari, Night Watch) -> axis 1
N = 4    # Images per category -> axis 2
H = 64   # Image height in pixels -> axis 3
W = 64   # Image width in pixels -> axis 4
CH = 3   # Colour channels (RGB) -> axis 5


# ---------------------------------------------------
# Step 2 - Create ONE collection, as a 5D tensor.
# This simulates a single collection (e.g. Wildlife), with shape:
# (categories, images, height, width, channels)
# ---------------------------------------------------

# np.random.randint(0, 256, ...) generates whole numbers from 0 up to
# (not including) 256 — the valid range for one RGB colour channel.
# dtype=np.uint8 stores each value as a memory-efficient 8-bit integer,
# the standard choice for image pixel data.
one_collection = np.random.randint(
    0, 256,
    size=(K, N, H, W, CH),
    dtype=np.uint8
)

print("One collection shape:", one_collection.shape)
# Output: One collection shape: (2, 4, 64, 64, 3)

print(f"Items in one collection: {one_collection.size}")
# Output: Items in one collection: 98304
# Sanity check: 2 categories x 4 images x 64 height x 64 width x 3 channels
#             = 2 x 4 x 64 x 64 x 3 = 98,304


# ---------------------------------------------------
# Step 3 - Create MULTIPLE collections, and collect them in a plain list.
# At this stage we have C separate 5D tensors, NOT yet a single 6D tensor.
# ---------------------------------------------------

collection_list = []

for i in range(C):
    # Simulate one more collection (e.g. Family, then Urban).
    collection = np.random.randint(
        0, 256,
        size=(K, N, H, W, CH),
        dtype=np.uint8
    )
    collection_list.append(collection)

print(f"Number of collections created: {len(collection_list)}")
# Output: Number of collections created: 3

print(f"Shape of each collection: {collection_list[0].shape}")
# Output: Shape of each collection: (2, 4, 64, 64, 3)
# Every collection in the list shares this same shape — a REQUIREMENT
# for np.stack() to work in the next step.


# ---------------------------------------------------
# Step 4 - Stack the collections into a single 6D tensor.
# np.stack() introduces a brand-new axis (axis=0), using each list
# item's position as the index along that new axis. This is exactly
# what turns "a list of 3 separate 5D tensors" into "one genuine 6D tensor."
# ---------------------------------------------------

dataset = np.stack(collection_list, axis=0)

print("Final dataset shape:", dataset.shape)
# Output: Final dataset shape: (3, 2, 4, 64, 64, 3)
# This matches the target shape from Section 5's Objective exactly.


# ---------------------------------------------------
# Step 5 - Verify the structure by checking each axis explicitly.
# ---------------------------------------------------

print("\nDataset interpretation:")
print(f"Collections (C): {dataset.shape[0]}")   # 3
print(f"Categories (K): {dataset.shape[1]}")    # 2
print(f"Images (N): {dataset.shape[2]}")        # 4
print(f"Height (H): {dataset.shape[3]}")        # 64
print(f"Width (W): {dataset.shape[4]}")         # 64
print(f"Channels: {dataset.shape[5]}")          # 3


# ---------------------------------------------------
# Step 6 - Access one specific image, to prove the structure works
# exactly like the folder hierarchy it represents.
# ---------------------------------------------------

# First collection -> first category -> first image
image = dataset[0, 0, 0]

print("\nSingle image shape:", image.shape)
# Output: Single image shape: (64, 64, 3)
# Exactly (H, W, CH) — a single, complete image.

print(f"Pixel value at (0,0) in this image: {image[0, 0]}")
# Output: Pixel value at (0,0) in this image: [R G B]
# Three numbers, each from 0-255, representing that single pixel's colour.
```

---

## Summary

| Level | Shape | What it represents |
| --- | --- | --- |
| Pixel | `[R, G, B]` | One colour value at one exact spot in one image |
| Image | `(H, W, 3)` | One complete photo |
| Category | `(N, H, W, 3)` | A group of same-sized photos (e.g. Safari) |
| Collection | `(K, N, H, W, 3)` | Several categories grouped together (e.g. all of Wildlife) |
| Dataset | `(C, K, N, H, W, 3)` | Every collection, stacked into one structured tensor |

| Concept | Key takeaway |
| --- | --- |
| Constraints matter | Real photo folders rarely satisfy NumPy's "everything must be the same shape" requirement without preprocessing first |
| Build up gradually | It's far easier to reason about one 5D tensor per collection, then `np.stack()` them, than to try to build the full 6D tensor in one step |
| `np.stack()`'s role | Converts a plain Python list of equally-shaped tensors into one higher-dimensional tensor, using each item's list position as the new axis |
| Indexing mirrors the folder structure | `dataset[collection, category, image]` reads exactly like navigating the original nested folders |

---

## Follow-up questions for practice

*(These are additional, optional questions for self-testing — they don't
replace or change the original research scenario, problem, or task above.)*

1. What would `dataset[1, 0]` give you, in terms of shape and meaning,
   using the collection/category/image structure described above? Predict
   it before checking with code.
2. Suppose the "Family Events" collection actually only had **3** images
   per category instead of 4, while every other collection had 4. Why
   would `np.stack(collection_list, axis=0)` fail in that case? Which of
   the three constraints in Section 3 does this violate?
3. Modify Step 3 of the script so that each collection has a **different**
   number of categories (`K`). What error do you get when you reach Step 4,
   and why does that error message make sense given what `np.stack()`
   requires?
4. If you wanted `dataset[0]` to represent "all photos of a single
   *category* across every collection" instead of "everything in one
   collection," which axis would you need to stack along instead of
   `axis=0`? (Hint: revisit the `np.stack()` axis discussion from Chapter
   11's earlier project on `np.stack()`.)




