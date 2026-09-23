


## Beyond Text

In this project, we move from theory to practical application. Singular Value Decomposition (SVD) is an efficient algorithm for "Dimension Reduction." and can be used to perform **Digital Image Compression.** Think of an image not as a picture, but as a massive grid of numbers—a matrix. By decomposing this matrix into its fundamental "singular values," one can identify which parts of the image are essential structure and which are mere noise.

"How much information is required to recognize an image? Investigate the relationship between the 'Rank' of a matrix and visual clarity. Using Singular Value Decomposition (SVD), decompose a high-resolution image into its constituent U, **Σ**, and $V^T$ components. Conduct an experiment to determine the 'Critical Compression Threshold'—the point where the number of singular values (k) is reduced so much that the image becomes unrecognizable. Your project must compare the original RGB data, a grayscale baseline, and a reconstructed low-rank matrix version."

### The Workflow

1.  **Acquisition:** Fetch an image from a web URL or your local drive.
2.  **Preprocessing:** Convert the colorful image data into a 2D grayscale matrix using the **Pillow (PIL)** library.
3.  **Decomposition:** Use np.linalg.svd() to break your image into three components: $U$, $Σ$ and $V^T$
4.  **Compression:** Trim the singular values. In this experiment, we start by keeping only **1/20th** of the original data.
5.  **Reconstruction:** Use matrix multiplication to re-assemble the image and visualize the results side-by-side using Matplotlib.

### The Solution Script
This version uses modern NumPy conventions (np.asarray) which replaces the multi-step getdata() process (Note the earlier 2019 used the multi-step getdata() process , making the code much more efficient

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# --- 1. Load Image (Local Path or Web Link) ---
# Replace this URL with any image link (e.g., from Unsplash or GitHub)
url = "https://raw.githubusercontent.com/numpy/numpy/main/branding/logo/primary/numpylogo.png"

try:
    response = requests.get(url)  # Fetch image from the internet
    img = Image.open(BytesIO(response.content))  # raw data → image format
except:
    print("Web link failed, please check URL or internet connection.")
    # Fallback: create a dummy array if link fails
    img = Image.fromarray(np.uint8(np.random.rand(500,500)*255))

width, height = img.size
print(f"Original Dimensions: Width={width}, Height={height}")

# --- 2. Color Conversion ---
# 'L' mode converts image to grayscale (8-bit pixels, black and white)
img_gray = img.convert('L')

# --- 3. Matrix Conversion (The Modern Way) ---
# Instead of getdata() and lists, np.asarray() is much faster and more direct
img_mat = np.asarray(img_gray)

# --- 4. SVD Decomposition ---
# U: Left singular vectors (Rotations)
# S: Singular values (Importance/Energy of each feature)
# Vt: Right singular vectors (Rotations)
U, S, Vt = np.linalg.svd(img_mat, full_matrices=False)

# --- 5. Compression / Dimension Reduction ---
# We define 'k' as the number of singular values to keep.
# Let's use 1/20th (5%) of the available singular values.
k = int(len(S) / 20)
print(f"Total Singular Values: {len(S)} | Retained for Compression (k): {k}")

# Reconstruct the matrix using only the top 'k' components
# Formula: U_k * Sigma_k * Vt_k
img_compressed = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

# --- 6. Visualization ---
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Subplot 1: Original Color
axes[0].imshow(img)
axes[0].set_title("Original Color")
axes[0].axis('off')

# Subplot 2: Grayscale Baseline
axes[1].imshow(img_gray, cmap='gray')
axes[1].set_title("Grayscale (Uncompressed)")
axes[1].axis('off')

# Subplot 3: SVD Compressed
axes[2].imshow(img_compressed, cmap='gray')
axes[2].set_title(f"SVD Compressed (k={k})")
axes[2].axis('off')

plt.tight_layout()
plt.show()


```

### The (1) original image (2)  Its grey scale version and its (3) SVD compressed version are shown in figure below:

![SVD Image compression](../resources/ch11-svd-image-compression.png)



## Introduction to the Script

This script demonstrates how images can be treated as matrices and how we can use Singular Value Decomposition (SVD) to compress an image.

The idea is simple:

An image = a matrix of numbers
SVD breaks this matrix into components
We keep only the most important components
Rebuild the image → smaller size, slight loss in quality

This technique is widely used in:

Image compression
Machine learning
Data reduction (PCA)
📚 Libraries Used (Beginner-Friendly Explanation)
Library	Purpose	Key Functions Used
numpy	Numerical computations, arrays, matrices	np.asarray, np.linalg.svd, np.dot, np.diag
matplotlib.pyplot	Display images and plots	plt.imshow, plt.subplots, plt.show
PIL (Pillow)	Image processing	Image.open, convert
requests	Download data from internet	requests.get
io.BytesIO	Convert raw bytes into file-like object	BytesIO()


Step-by-Step Explanation of the Script

### Step 0: Import Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO
```
Explanation:
We import all required tools.
np → numerical operations
plt → visualization
Image → image handling
requests → download image
BytesIO → convert raw data to readable format

### Step 1: Load Image

```python
url = "https://raw.githubusercontent.com/numpy/numpy/main/branding/logo/primary/numpylogo.png"
```

This is the image source.

```python
response = requests.get(url)
# Fetch image from the internet
```
What happens here?
Sends a request to the internet
Downloads image data in binary format (bytes)
```python
img = Image.open(BytesIO(response.content))
```
Key Idea:
`response.content` → raw bytes
`BytesIO()` → converts bytes into file-like object
`Image.open()` → reads it as an image

Error Handling
```python
except:
    print("Web link failed...")
    img = Image.fromarray(np.uint8(np.random.rand(500,500)*255))
```

Explanation:
If internet fails: Then:- A random grayscale image is created. This ensures that the script never crashes
`width, height = img.size`
Extracts image dimensions
`print(f"Width={width}, Height={height}")`

### Step 2: Convert to Grayscale

`img_gray = img.convert('L')`
Explanation:
'L' = grayscale mode
Each pixel becomes a value from 0 to 255

Why?

SVD works on 2D matrices
Color images are 3D (RGB)

### Step 3: Convert Image to Matrix

`img_mat = np.asarray(img_gray)`
Key Idea:
Converts image into NumPy array

Example:

Pixel image → Matrix of numbers
### Step 4: Apply SVD

`U, S, Vt = np.linalg.svd(img_mat, full_matrices=False)`

What is happening?

SVD breaks matrix into:

1. 𝐴 = 𝑈 ⋅ Σ ⋅ 𝑉ᵀ
Component	Meaning
U	Row patterns
S	Importance (singular values)
Vᵀ	Column patterns


Important:
`full_matrices=False`
Makes computation faster and memory efficient

### Step 5: Compression
`k = int(len(S) / 20)`

Keep only 5% of information

`img_compressed = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :])))`
This is the MOST IMPORTANT LINE

Let’s break it:

Step 1:
`S[:k]`

Take top k singular values

Step 2:
`np.diag(S[:k])`

Convert into diagonal matrix

Step 3:
`U[:, :k]`

Take first k columns of U

Step 4:
```python

Vt[:k, :]
```


Take first k rows of Vt
Final formula:
$𝐴_k = U_k \cdot Σ_k \cdot V_k^T$




This reconstructs compressed image

Step 6: Visualization
`fig, axes = plt.subplots(1, 3, figsize=(15, 5))`

Create 3 side-by-side plots

Plot 1: Original
`axes[0].imshow(img)`

Plot 2: Grayscale
`axes[1].imshow(img_gray, cmap='gray')`

Plot 3: Compressed
`axes[2].imshow(img_compressed, cmap='gray')`

`plt.tight_layout()`
`plt.show()`

Display all images neatly

#### Concept Summary Table

  

| Step | Operation | Purpose |
| --- | --- | --- |
| 1 | Load Image | Get input |
| 2 | Grayscale | Reduce dimensions |
| 3 | Convert to array | Mathematical processing |
| 4 | SVD | Decompose matrix |
| 5 | Keep k values | Compression |
| 6 | Reconstruct | Approximate image |


Key Concepts Students Must Understand
1. Image = Matrix

Each pixel is a number

2. SVD = Decomposition

Break matrix into meaningful parts

3. Compression = Information Reduction

Keep only important features

4. Trade-off

  

| k value | Result |
| --- | --- |
| small k | high compression, low quality |
| large k | low compression, high quality |


#### SVD Image Compression Flow chart

![SVD Image Compression Flow Chart](../resources/ch11-svd-image-compression-2.png)



















