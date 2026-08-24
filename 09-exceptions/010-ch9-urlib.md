



# Reading Files from the Internet with `urllib`

Until now, most of the file-reading examples in this book have used `open()` to read files sitting on your own computer. But a huge amount of real-world Python code needs to read data that lives somewhere else entirely — a text file on GitHub, a page on a website, a data feed from an API. This section covers Python's built-in `urllib` library, which lets you do exactly that: open a connection to a web address (a **URL**, short for *Uniform Resource Locator* — the address you'd normally type into a browser, like `https://example.com/file.txt`) and read whatever it returns, just as if it were a local file.

This ties directly into the chapter on **exceptions**, because reading something over the internet can fail in ways that reading a local file never does — the network might be down, the address might not exist, or the website might send back something your program doesn't expect. So alongside `urllib` itself, this section is really a case study in *why* exception handling matters once your program starts depending on things outside your own computer.

---

## Project 1: Study Python's `urllib` Library and Explain How Files Can Be Read from the Internet

*(This is the original research question from the printed book. A few optional follow-up questions have been added at the end, for readers who want to dig a little deeper.)*

### Instructions

1. Explain:
   - What is `urllib`?
   - What is `urlopen()`?
2. Differentiate between:
   - Local file reading (`open`)
   - Internet file reading (`urlopen`)
3. Study:
   - `.read()`
   - `.decode()`
4. Identify possible errors:
   - `URLError`
   - `HTTPError`
5. Write a small script to:
   - Read the first 100 characters from a GitHub file

---

## Answer

### Step 1: What is `urllib`?

`urllib` is a library that comes built into Python — you don't need to install anything extra to use it. It bundles together several tools for working with URLs, and the piece we care about here is `urllib.request`, which is specifically for **opening and reading** the content found at a URL.

### Step 2: What is `urlopen()`?

`urlopen()` is the main function inside `urllib.request`. Think of it as the internet equivalent of `open()`:

- `open()` opens a **file on your computer** and gives you back a file object you can read from.
- `urlopen()` opens a **connection to a URL** and gives you back a *response object* you can read from, in much the same way.

```python
import urllib.request

response = urllib.request.urlopen("https://example.com")
```

At this point, `response` behaves a lot like the file object you'd get from `open()` — the next two steps show how to actually get data out of it.

### Step 3: Local files vs. internet files — what's different?

| | `open()` (local file) | `urlopen()` (internet file) |
| --- | --- | --- |
| What it reads | A file already sitting on your computer's disk | Content sent back by a remote web server |
| Can it fail because of your network connection? | No | Yes — the request travels over the internet, so it can fail in transit |
| Typical errors | `FileNotFoundError`, permission errors | `URLError`, `HTTPError` (explained in Step 5) |
| Speed | Very fast, essentially instant | Depends on your internet connection and the remote server's speed |
| What you get back | A file object | A response object (used very similarly to a file object) |

The big-picture idea: **reading from the internet is just like reading a file, except a lot more can go wrong along the way** — and that's exactly why the exception handling shown further down matters so much here.

### Step 4: `.read()` and `.decode()`

Once you have a response object from `urlopen()`, getting the actual content takes two steps:

1. **`.read()`** — reads the data sent back by the server. Importantly, this data comes back as **bytes** (raw 0s and 1s, not readable text) — see the note below if the word "bytes" is unfamiliar.
2. **`.decode()`** — converts those raw bytes into a normal, readable Python string, using a specified **encoding** (a set of rules for translating between bytes and text — `'utf-8'` is by far the most common one, and a safe default for most files you'll encounter).

```python
data = response.read()          # raw bytes, e.g. b'Hello World'
content = data.decode("utf-8")  # a normal string, e.g. 'Hello World'
```

> **New term — "bytes":** a `bytes` object is Python's way of representing raw binary data — the kind of data a computer actually stores and transmits, before it's been interpreted as text, an image, or anything else. You can usually spot one immediately in Python because it's printed with a `b` in front of it, like `b'Hello'`. For a deeper look, see the [official Python docs on bytes objects](https://docs.python.org/3/library/stdtypes.html#bytes-objects).

### Step 5: Errors that can happen when reading from a URL

Because a URL request depends on things outside your program's control — your internet connection, the remote server, the exact web address you typed — several new kinds of errors can occur that simply don't exist when reading a local file:

| Error | What causes it |
| --- | --- |
| `URLError` | A general connection problem — for example, the domain name doesn't exist, or there's no internet connection at all. |
| `HTTPError` | The connection to the server succeeded, but the server itself responded with an error — most commonly **404** ("page not found") or **500** ("server error"). |
| `UnicodeDecodeError` | The bytes received don't match the encoding you asked `.decode()` to use — this can happen if you try to `.decode("utf-8")` a file that isn't actually text at all (like an image). |

> **New terms:** an **HTTP status code** is a short number a web server sends back with every response, saying how the request went (`200` = success, `404` = not found, `500` = server error, and so on). You can see the [full list of HTTP status codes here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) if you'd like to explore further.

### Step 6: A small script to read the first 100 characters from a GitHub file

```python
import urllib.request

# Step 1: choose a URL pointing directly at a raw text file on GitHub
url = "https://raw.githubusercontent.com/gvanrossum/peps/refs/heads/master/pep-0020.txt"

# Step 2: open a connection to the URL, just like open() does for local files
response = urllib.request.urlopen(url)

# Step 3: read the raw bytes sent back by the server
data = response.read()

# Step 4: convert those bytes into a normal, readable string
content = data.decode("utf-8")

# Step 5: display only the first 100 characters
print(content[:100])
```

This version has no error handling at all — it will work fine as long as the URL is correct and the internet connection is working, but it will crash with an unhandled exception if anything goes wrong. The next section builds a more complete version that handles exactly that.

---

## Project 1 — Optional Follow-Up Questions

*(These are additional questions, not part of the original printed book, for readers who want to explore the topic a bit further.)*

1. What happens if you try `.decode("utf-8")` on the raw bytes of an image file? Try it, and explain the error you get.
2. `urlopen()` also lets you inspect the response's HTTP status code directly, via `response.status` (or `response.getcode()` in older code). Modify the script above to print this value.
3. Look up the difference between `http://` and `https://` in a URL. Which one does the example script use, and why might that matter?

---

## Part 2: Project Question (Applied Learning)

*(Original project task from the printed book.)*

> Write a Python program that:
> 1. Downloads a file from GitHub (or any URL)
> 2. Displays part of the content
> 3. Handles:
>    - Invalid URL
>    - Network failure
>    - Wrong encoding
> 4. Demonstrates:
>    - Error-free execution
>    - Error-prone execution

---

## Part 3: Script

Here's a program that fulfills all four requirements above — it wraps the read in a `try`/`except`/`else`/`finally` block, handling each kind of failure separately, and is then tested against four different URLs to show both the successful and the failing cases.

```python
import urllib.request
import urllib.error


def read_online_file(url):
    """Attempt to read text content from a URL, handling every
    kind of failure covered in this section along the way."""

    try:
        # Step 1: try to open a connection to the URL.
        # This is the step most likely to raise URLError -- for
        # example, if the domain name doesn't exist, or there's
        # no internet connection at all.
        print("1. Connecting...")
        response = urllib.request.urlopen(url)

        # Step 2: read the raw bytes the server sent back.
        # This is where HTTPError shows up -- the connection itself
        # succeeded, but the server responded with an error status
        # (like 404 Not Found).
        print("2. Reading data...")
        data = response.read()

        # Step 3: convert those raw bytes into a readable string.
        # This is where UnicodeDecodeError can occur, if the bytes
        # received don't actually represent utf-8 text.
        print("3. Decoding data...")
        content = data.decode("utf-8")

    except urllib.error.HTTPError as e:
        # The server was reachable, but returned an error status code
        # (e.g. 404 = page not found, 500 = server error).
        print("HTTP Error:", e.code)

    except urllib.error.URLError:
        # We couldn't reach the server at all -- e.g. the domain name
        # doesn't exist, or there's a network connectivity problem.
        print("URL Error: Cannot reach server")

    except UnicodeDecodeError:
        # The content we downloaded wasn't valid utf-8 text
        # (this often means we accidentally downloaded a non-text
        # file, like an image).
        print("Error: Cannot decode content")

    except Exception as e:
        # A catch-all for any other, unexpected problem -- always
        # keep this LAST, since Python checks except blocks in order
        # and a broad Exception placed earlier would swallow the more
        # specific errors above before they get a chance to run.
        print("Other Error:", e)

    else:
        # This block only runs if NO exception was raised above --
        # i.e. everything succeeded.
        print("4. Success! Showing first 1000 characters:\n")
        print(content[:1000])

    finally:
        # This block always runs, whether we succeeded or failed --
        # useful for a final status message, or for cleanup code.
        print("5. Operation completed\n")


# ---------------- Test Cases ----------------

# Case 1: a valid URL that should succeed completely
print("Case 1: Valid URL")
read_online_file(
    "https://raw.githubusercontent.com/gvanrossum/peps/refs/heads/master/pep-0020.txt"
)

# Case 2: a URL whose domain doesn't exist -- triggers URLError
print("Case 2: Invalid URL")
read_online_file("https://invalid-url.com/file.txt")

# Case 3: a real domain, but a file path that doesn't exist there --
# the server responds, but with a 404 status -- triggers HTTPError
print("Case 3: HTTP Error (404)")
read_online_file("https://raw.githubusercontent.com/python/cpython/main/NOFILE.txt")

# Case 4: a URL pointing at binary (non-text) content --
# .decode("utf-8") will fail on this -- triggers UnicodeDecodeError
print("Case 4: Encoding issue (rare but possible)")
read_online_file("https://example.com/binaryfile")
```

### What Each Test Case Demonstrates

| Case | URL Type | Which `except` Block Runs | Demonstrates |
| --- | --- | --- | --- |
| 1 | A real, working file URL | *(none — the `else` block runs instead)* | Error-free execution |
| 2 | A domain that doesn't exist | `except urllib.error.URLError` | Network/connection failure |
| 3 | A real domain, missing file | `except urllib.error.HTTPError` | Server-side error (404) |
| 4 | A URL returning non-text data | `except UnicodeDecodeError` | Wrong/incompatible encoding |

---

## Part 4: Error Comparison Table

| Error Type | Cause | How It's Handled |
| --- | --- | --- |
| `HTTPError` | The server was reached, but responded with an error status (e.g. 404 file not found) | A specific `except urllib.error.HTTPError` block |
| `URLError` | The server couldn't be reached at all (bad domain, no internet connection) | A specific `except urllib.error.URLError` block |
| `UnicodeDecodeError` | The downloaded bytes don't match the encoding used in `.decode()` | A specific `except UnicodeDecodeError` block |
| `Exception` | Anything else, unanticipated | A general `except Exception` block, placed last |

---

## Part 5: Exception Hierarchy

Python's exceptions are organized into a hierarchy — some exception types are more *specific* versions of a more *general* one. Understanding this hierarchy explains why the order of `except` blocks in the script above matters. Here it is as a simple tree:

```
Exception
│
├── URLError
│     └── HTTPError
│
├── UnicodeDecodeError
│
└── (all other exception types)
```

### The same relationship, drawn as a flowchart 

![Flowchart](/resources/ch-9-exceptions-august-2026-urlib-project.png)



### Important Note: Order Matters

`HTTPError` is a **subclass** of `URLError` — in other words, every `HTTPError` *is also* a `URLError`, but not the other way around. (A quick primer on this idea, if it's new to you: a "subclass" is a more specific version of a more general category — the same way "a poodle" is a specific kind of "a dog." The book's later chapter on Object-Oriented Programming covers this idea properly.)

This matters because Python checks `except` blocks **in the order they're written**, and stops at the *first* one that matches. So:

```python
# WRONG ORDER: URLError is checked first, and since HTTPError
# "is a" URLError, this block would catch HTTPError cases too --
# meaning the more specific except urllib.error.HTTPError block
# below it would NEVER actually run.
try:
    ...
except urllib.error.URLError:
    print("URL Error")
except urllib.error.HTTPError:
    print("HTTP Error")   # unreachable!
```

```python
# CORRECT ORDER: the more specific HTTPError is checked FIRST.
# Only genuine URLErrors (that are NOT also HTTPErrors) fall
# through to the second block.
try:
    ...
except urllib.error.HTTPError:
    print("HTTP Error")
except urllib.error.URLError:
    print("URL Error")
```

**The general rule, for any exception hierarchy:** always list your `except` blocks from **most specific to most general** — exactly the order used in the Part 3 script above (`HTTPError` → `URLError` → `UnicodeDecodeError` → `Exception`).

---

## Quick Recap

| Step | What Happens | Function/Tool Used |
| --- | --- | --- |
| 1 | Connect to a URL | `urllib.request.urlopen()` |
| 2 | Read the raw response | `.read()` |
| 3 | Convert bytes to text | `.decode("utf-8")` |
| 4 | Handle problems, most specific first | `except HTTPError` → `except URLError` → `except UnicodeDecodeError` → `except Exception` |
| 5 | Always run cleanup/status code | `finally` |




