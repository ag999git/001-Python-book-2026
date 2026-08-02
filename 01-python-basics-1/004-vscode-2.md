# VS Code Part 2

The table below provides direct access to our course resources: (1) The full repository on GitHub, (2) Interactive labs via Google Colab, (3) VS Code for local development, and (4) Jupyter Notebooks for local server-based execution.

| Source                                                                                                                                                                              | Run (Cloud)                                                                                                                                       | Local IDE                                                                                                                                                                    | Notebook                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [![GitHub](https://img.shields.io/badge/GitHub-Repo-3776AB?style=for-the-badge\&logo=github\&logoColor=white\&labelColor=555555)](https://github.com/ag999git/001-Python-book-2026) | [![Colab](https://img.shields.io/badge/Colab-Labs-FFD700?style=for-the-badge\&logo=googlecolab\&logoColor=white\&labelColor=228B22)](../colab-nb) | [![VS Code](https://img.shields.io/badge/IDE-VS_Code-007ACC?style=for-the-badge\&logo=visualstudiocode\&logoColor=white\&labelColor=2C2C32)](https://code.visualstudio.com/) | [![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?style=for-the-badge\&logo=jupyter\&logoColor=white\&labelColor=333333)](https://jupyter.org/) |

### VS Code + Python + Jupyter — Complete Setup Guide on Windows

This guide explains how to install VS Code, configure Python/Jupyter inside it, select interpreters, create virtual environments, and run notebooks inside VS Code.

## Table of contents

***

**PART 1 — Install VS Code**

**Step 1: Download VS Code**

1. Go to: https://code.visualstudio.com
2. Click **Download for Windows** (blue button)

**Step 2: Install VS Code**

1. Double-click `VSCodeUserSetup-x64-xxxx.exe`
2. Click **Next**
3. Accept the License Agreement → **Next**
4. Important: Enable these:
   * Add “Open with Code” (file context menu)
   * Add “Open with Code” (folder context menu)
   * Add to `PATH`
5. Click **Next** → **Install**
6. Click **Finish**

VS Code will launch.

***

**PART 2 — Install Required Extensions**

**Step 1: Open Extensions Panel**

Click the **Extensions icon** (left toolbar, looks like 4 squares)\
Or press:

```
Ctrl + Shift + X
```

**Step 2: Install Python Extension**

Search:

```
Python
```

Install:

* **Python — by Microsoft**\
  (Blue/yellow Python logo)

**Step 3: Install Jupyter Extension**

Search:

```
Jupyter
```

Install:

* **Jupyter — by Microsoft**\
  (Orange circular icon)

***

**PART 3 — Open Your Project Folder**

You must open a FOLDER, not individual files.

Steps:

1. Click **File → Open Folder…**
2. Browse to:

```
C:\python-projects\my_project
```

3. Click **Select Folder**

Your folder appears on the left sidebar (Explorer).

***

**PART 4 — Select the Correct Python Interpreter**

The most important step.

**Step 1: Open Command Palette**

```
Ctrl + Shift + P
```

**Step 2: Type**

```
Python: Select Interpreter
```

Click the option.

**Step 3: Choose the correct interpreter**

Pick one of:

* **Python 3.12.x 64-bit** (recommended)
* **Python 3.12 (.venv)** if inside virtual environment

Interpreter shows in the bottom-right corner in VS Code.

***

**PART 5 — Create a Virtual Environment (Recommended)**

**Step 1: Open VS Code terminal**

Top menu:

```
Terminal → New Terminal
```

Terminal opens at bottom.

**Step 2: Create venv**

```
python -m venv .venv
```

A folder named `.venv` appears on the left.

**Step 3: Activate venv**

```
.\.venv\Scripts\activate
```

Prompt becomes:

```
(.venv) C:\python-projects\my_project>
```

**Step 4: Install Jupyter in venv**

```
pip install notebook jupyterlab ipykernel
```

***

**PART 6 — Create a Python File in VS Code**

1. In Explorer (left), click **New File** icon\
   (looks like a piece of paper)
2. Name it:

```
test.py
```

3. Add code:

```python
print("Hello from VS Code!")
```

4. Run using **Run button** at top-right\
   OR

```
Ctrl + F5
```

***

**PART 7 — Jupyter Notebooks Inside VS Code**

**Option A — Create a new notebook**

1. Press:

```
Ctrl + Shift + P
```

2. Type:

```
Jupyter: Create New Jupyter Notebook
```

A new notebook opens:

```
Untitled.ipynb
```

**Option B — Open existing notebook**

Just click any `.ipynb` file in the Explorer sidebar.

***

**Running Notebook Cells**

* Click the **Run (▶)** button to the left of the cell
* OR press:

```
Shift + Enter
```

***

**Selecting the Jupyter Kernel (IMPORTANT)**

Top-right corner shows:

```
Select Kernel
```

Click it → choose:

* **Python 3.12 (Main)**\
  or
* **Python 3.12 (.venv)**

***

**PART 8 — Launch Jupyter in Browser (Optional)**

From terminal:

**Classic notebook:**

```
jupyter notebook
```

**JupyterLab:**

```
jupyter lab
```

Opens browser at:

```
http://localhost:8888/
```

***

**PART 9 — Common Problems & Fixes**

**VS Code shows wrong Python version**

Fix:

```
Ctrl + Shift + P → Python: Select Interpreter
```

Choose Python 3.12.

***

**Jupyter cannot find kernel**

Install kernel:

```
python -m ipykernel install --user --name py312
```

***

**Notebook inside VS Code uses wrong environment**

Activate the environment:

```
.\.venv\Scripts\activate
pip install ipykernel
```

Restart VS Code.

***

**PART 10 — Summary Checklist**

| Step | What to Do                          |
| ---- | ----------------------------------- |
| 1    | Install VS Code                     |
| 2    | Install Python + Jupyter extensions |
| 3    | Open a folder (not just files)      |
| 4    | Select Python 3.12 interpreter      |
| 5    | Create and activate `.venv`         |
| 6    | Install Jupyter inside venv         |
| 7    | Create notebooks or scripts         |
| 8    | Select the correct kernel           |
| 9    | Run code                            |

***

#### Setup Complete!

You now have a fully working environment for Python + Jupyter inside VS Code on Windows.
