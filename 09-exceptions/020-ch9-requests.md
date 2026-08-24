


# Reading Files from the Internet with `requests`

The previous section showed how to read data from the internet using Python's built-in `urllib` library. This section covers `requests` — a hugely popular alternative that does the same basic job, but with a much friendlier, more readable API. Almost every real-world Python project that talks to the internet (calling a web API, downloading a file, checking a website) uses `requests` rather than `urllib`, so this section is really about meeting the tool you're most likely to actually reach for once you're writing programs outside this book.

It also continues the running theme from the exceptions chapter: anything that depends on a network connection can fail in several distinct ways, and `requests` gives each kind of failure its own clearly-named exception, which makes writing precise error handling considerably easier than it is with `urllib`.

---

## Part 1: Research Question

*(This is the original research question from the printed book, kept exactly as written. A short set of optional follow-up questions has been added after the model answer.)*

> Study the Python `requests` library and explain how it simplifies reading files/data from the internet compared to `urllib`.

### Instructions

1. What is the `requests` library?
2. How is it different from `urllib`?
3. Study the following:
   - `requests.get()`
   - `response.text`
   - `response.content`
   - `response.status_code`
4. What is:
   - `raise_for_status()`?
5. Identify common exceptions:
   - `RequestException`
   - `HTTPError`
   - `ConnectionError`
   - `Timeout`
6. Write a small script to:
   - Read and display the first 100 characters from a GitHub file

---

## Answer

### Step 1: What is `requests`?

`requests` is a **third-party library** — meaning, unlike `urllib`, it doesn't come built into Python and must be installed first, with:

```
pip install requests
```

Once installed, it lets you fetch data from a URL in just one line, using an API that most people find far more readable than `urllib`'s.

> **New term — "third-party library":** this just means a library written and maintained by someone other than the core Python team, which you install yourself (usually via `pip`, Python's package installer) rather than getting it automatically with Python. You can read more about installing packages in the [official `pip` documentation](https://pip.pypa.io/en/stable/).

### Step 2: How is `requests` different from `urllib`?

Both libraries do fundamentally the same thing — send a request to a URL and get back a response — but `requests` wraps the whole process in a much simpler, more forgiving interface. A few concrete differences:

| | `urllib` (built-in) | `requests` (third-party) |
| --- | --- | --- |
| Needs installing? | No — comes with Python | Yes — `pip install requests` |
| Getting text content | `response.read().decode("utf-8")` (two separate steps) | `response.text` (one step — decoding is automatic) |
| Checking for HTTP errors | You must check `response.status` yourself | `response.raise_for_status()` does it for you in one call |
| Error types | `URLError`, `HTTPError` | `ConnectionError`, `Timeout`, `HTTPError`, and more — each with a clearly matching name |
| General reputation | More verbose, but no installation needed | Widely considered friendlier and more "Pythonic" |

The short version: **`urllib` is what you reach for when you can't install anything extra; `requests` is what most Python developers actually reach for in everyday projects.**

### Step 3: The core building blocks

#### `requests.get()`

Sends an HTTP `GET` request — the standard way of *asking* a server for data (as opposed to sending it data) — to a URL, and returns a **response object**.

```python
import requests
response = requests.get("https://example.com")
```

#### `response.text`

Gives you the response content already decoded into a normal, readable Python string. Unlike `urllib`, there's no separate `.decode()` step — `requests` figures out the right encoding automatically in almost all cases.

#### `response.content`

Gives you the response content as raw **bytes**, without any decoding — the equivalent of `urllib`'s `.read()`. This is what you'd use for non-text content, such as downloading an image.

#### `response.status_code`

Gives you the numeric **HTTP status code** the server sent back — for example, `200` for success or `404` for "not found." (See the note on status codes in the previous section if this term is new to you.)

```python
print(response.status_code)   # e.g. 200
```

### Step 4: What does `raise_for_status()` do?

`response.raise_for_status()` is a convenience method that checks the response's status code for you, and — if it represents an error (any code in the 400s or 500s) — **raises an `HTTPError` exception automatically**. If the status code indicates success, it does nothing at all and simply lets your code continue.

```python
response = requests.get(url)
response.raise_for_status()   # raises HTTPError here if the request failed
```

This is one of the biggest conveniences `requests` offers over `urllib`: instead of manually checking `if response.status != 200: ...`, you get proper exception-based error handling in a single line.

### Step 5: Common exceptions in `requests`

All of the exceptions `requests` can raise share a common ancestor, `RequestException` — which matters for the same reason it did with `urllib.error.URLError` in the previous section (see Part 4 below for the full hierarchy).

| Exception | What causes it |
| --- | --- |
| `requests.exceptions.HTTPError` | The server responded, but with an error status code (e.g. 404, 500) — only raised if you call `raise_for_status()` |
| `requests.exceptions.ConnectionError` | The server couldn't be reached at all — bad domain name, no internet connection, refused connection |
| `requests.exceptions.Timeout` | The server took too long to respond (longer than the `timeout` value you specified) |
| `requests.exceptions.RequestException` | The base class for *every* exception `requests` can raise — catching this catches everything |

### Step 6: A small script to read the first 100 characters from a GitHub file

```python
import requests

# Step 1: choose a URL pointing directly at a raw text file on GitHub
url = "https://raw.githubusercontent.com/python/cpython/main/README.rst"

# Step 2: send a GET request to that URL, and wait up to 5 seconds for a reply
response = requests.get(url, timeout=5)

# Step 3: raise an error automatically if the server responded with a
# failure status code (like 404) -- if the request succeeded, this
# line simply does nothing and execution continues normally
response.raise_for_status()

# Step 4: response.text already gives us a normal, decoded string --
# no separate .decode() step needed, unlike urllib
content = response.text

# Step 5: display only the first 100 characters
print(content[:100])
```

Just like the equivalent `urllib` script in the previous section, this version has no error handling — it works fine when everything goes right, but will crash with an unhandled exception the moment anything goes wrong. Part 3 below builds a complete version that handles every failure case properly.

---

## Part 1 — Optional Follow-Up Questions

*(Additional questions, not part of the original printed book, for readers who want to explore further.)*

1. Try calling `response.json()` on a URL that returns JSON data (for example, `https://api.github.com`). What type of Python object does it give you back?
2. What happens if you *don't* call `raise_for_status()` after a failed request — does `requests.get()` raise an exception on its own for a 404 response? Try it and find out.
3. Look up the `requests` documentation for the `headers` parameter of `requests.get()`. Why might a program want to send custom headers along with its request?

---

## Part 2: Project Question (Applied Learning)

*(Original project task from the printed book.)*

> Develop a Python program using `requests` that:
> 1. Downloads a file from GitHub (raw URL)
> 2. Displays part of the content
> 3. Handles:
>    - Invalid URL
>    - Network failure
>    - Timeout
>    - HTTP errors (404, 500)
> 4. Demonstrates:
>    - Successful execution
>    - Multiple error scenarios

---

## Part 3: Script

```python
import requests


def read_online_file(url):
    """
    Attempt to read text content from a URL using requests,
    handling every category of failure covered in this section.

    Structure:
      try     -> the steps that might fail
      except  -> one block per specific kind of failure
      else    -> runs ONLY if nothing in try raised an exception
      finally -> always runs, success or failure
    """

    try:
        # Step 1: send the request, with a 5-second timeout.
        # This line alone can raise ConnectionError (server unreachable)
        # or Timeout (server too slow to respond).
        print("1. Sending request...")
        response = requests.get(url, timeout=5)

        # Step 2: check the response's status code, and raise
        # HTTPError automatically if it represents a failure
        # (e.g. 404 Not Found, 500 Internal Server Error).
        print("2. Checking response...")
        response.raise_for_status()

        # Step 3: read the already-decoded text content.
        # response.text handles the byte-to-string conversion
        # internally, so there's no separate .decode() call needed.
        print("3. Reading content...")
        content = response.text

    except requests.exceptions.HTTPError as e:
        # The server responded, but with an error status code.
        print("HTTP Error:", e)

    except requests.exceptions.ConnectionError:
        # The server could not be reached at all.
        print("Connection Error: Unable to connect")

    except requests.exceptions.Timeout:
        # The server took too long to respond.
        print("Timeout Error: Request took too long")

    except requests.exceptions.RequestException as e:
        # A catch-all for any OTHER requests-related problem not
        # already handled above. Kept LAST, since RequestException
        # is the parent of every exception type above it -- placing
        # it earlier would silently catch those more specific cases
        # too, and their dedicated messages above would never print.
        print("General Request Error:", e)

    else:
        # Runs only when the try block completed with no exceptions.
        print("4. Success! First 200 characters:\n")
        print(content[:200])

    finally:
        # Runs every time, regardless of what happened above --
        # useful for a final status message or cleanup code.
        print("5. Operation completed\n")


# ---------------- Test Cases ----------------

# Case 1: a valid URL that should succeed completely
print("Case 1: Valid URL")
read_online_file("https://raw.githubusercontent.com/python/cpython/main/README.rst")
# Flow: try -> else -> finally

# Case 2: a domain that doesn't exist -- triggers ConnectionError
print("Case 2: Invalid URL")
read_online_file("https://invalid-url.com/file.txt")
# Flow: try -> except(ConnectionError) -> finally

# Case 3: a real domain, but a file path that doesn't exist there --
# triggers HTTPError once raise_for_status() sees the 404
print("Case 3: HTTP Error (404)")
read_online_file("https://raw.githubusercontent.com/python/cpython/main/NOFILE.txt")
# Flow: try -> except(HTTPError) -> finally

# Case 4: a URL engineered to respond very slowly, longer than our
# 5-second timeout -- triggers Timeout
print("Case 4: Timeout simulation (very slow site)")
read_online_file("https://httpstat.us/200?sleep=7000")
# Flow: try -> except(Timeout) -> finally
```

### What Each Test Case Demonstrates

| Case | URL Type | Which `except` Block Runs | Demonstrates |
| --- | --- | --- | --- |
| 1 | A real, working file URL | *(none — the `else` block runs instead)* | Successful execution |
| 2 | A domain that doesn't exist | `except requests.exceptions.ConnectionError` | Network failure |
| 3 | A real domain, missing file | `except requests.exceptions.HTTPError` | Server-side error (404) |
| 4 | A deliberately slow-responding URL | `except requests.exceptions.Timeout` | Request taking too long |

---

## Part 4: Error Comparison Table

| Exception Type | Cause | How It's Handled |
| --- | --- | --- |
| `HTTPError` | Server responded with an error status (404, 500, etc.) | Specific `except requests.exceptions.HTTPError` block |
| `ConnectionError` | Network failure — server unreachable | Specific `except requests.exceptions.ConnectionError` block |
| `Timeout` | Server response took longer than the given `timeout` | Specific `except requests.exceptions.Timeout` block |
| `RequestException` | Base class covering *all* of the above, plus anything else | Generic `except requests.exceptions.RequestException` block, placed last |

---

## Part 5: Exception Hierarchy

Just as with `urllib.error.URLError` in the previous section, every specific exception `requests` can raise is a more precise version of a single shared parent class, `RequestException`. Here's the hierarchy as a simple tree:

```
RequestException
│
├── HTTPError
├── ConnectionError
├── Timeout
└── TooManyRedirects
```

The same relationship, as a flowchart 

![Flowchart](/resources/ch-9-exceptions-august-2026-exceptions-for-internet-project.png)


> **Why the order of `except` blocks still matters here too:** exactly as explained for `urllib` in the previous section, Python checks `except` blocks from top to bottom and stops at the first match. Since every exception in this tree — `HTTPError`, `ConnectionError`, `Timeout`, and `TooManyRedirects` — is *also* a `RequestException`, a generic `except requests.exceptions.RequestException:` block placed too early would catch all of them, and the more specific, more informative blocks below it would never run. That's why the script in Part 3 lists its `except` blocks from most specific to most general, with `RequestException` last.

---

## Part 6: Comparing `urllib` and `requests`

| Feature | `urllib` | `requests` |
| --- | --- | --- |
| Ease of use | Moderate — more manual steps | Very easy — fewer steps, more automatic |
| Readability | Lower — more boilerplate code | Higher — closer to plain English |
| Built into Python? | Yes | No — install with `pip install requests` |
| Getting text content | Two steps: `.read()` then `.decode()` | One step: `.text` |
| Checking for HTTP errors | Manual — check `response.status` yourself | One call: `.raise_for_status()` |
| Error handling | Works, but more verbose | Cleaner, more specific exception names |

**A practical rule of thumb:** if you're working in an environment where installing extra packages is difficult or not allowed, `urllib` gets the job done without any dependencies. Otherwise, for everyday projects, `requests` is generally the better choice — which is exactly why it remains one of the most widely used third-party libraries in the entire Python ecosystem.

---

## Quick Recap

| Step | What Happens | Function/Tool Used |
| --- | --- | --- |
| 1 | Send a request to a URL | `requests.get(url, timeout=...)` |
| 2 | Check for HTTP-level failure | `response.raise_for_status()` |
| 3 | Get the decoded text content | `response.text` |
| 4 | Handle problems, most specific first | `except HTTPError` → `except ConnectionError` → `except Timeout` → `except RequestException` |
| 5 | Always run cleanup/status code | `finally` |





