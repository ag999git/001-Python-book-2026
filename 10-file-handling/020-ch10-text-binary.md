


# Chapter 10.20 — Text Files vs. Binary Files

## What this page covers

This page builds directly on the previous chapter page's concepts table, focusing in depth on one of its most fundamental distinctions: **text files vs. binary files**. Every single file on a computer is, at the most basic level, just a sequence of bytes — the difference between a "text file" and a "binary file" is really about *how those bytes are meant to be interpreted*, and Python needs to be told which interpretation to use, via the mode you pass to `open()`.

Getting this distinction right matters immediately and practically: opening an image file in text mode, or opening a genuinely text-based log file in binary mode, will either crash your program outright or silently produce garbled, unusable data. This page walks through the full comparison, then demonstrates the key differences with runnable code.

**A few terms used throughout, explained simply:**
- **Byte** — the basic unit of digital storage; a single byte can represent 256 different possible values (0–255). All files, text or binary, are ultimately just sequences of bytes.
- **Encoding** — the specific rulebook used to convert human-readable text characters into bytes, and back again. UTF-8 is the most common, broadly compatible choice today. ([Python docs: Unicode HOWTO](https://docs.python.org/3/howto/unicode.html))
- **Parsing** — the process of interpreting raw data (bytes, or text) according to some known structure or format, in order to extract meaningful information from it.

---

## Comparison table: Text files vs. Binary files

| # | Feature | Text File | Binary File |
|---|---|---|---|
| 1 | Data format | Characters (a string) | Raw bytes |
| 2 | Internal representation | Stored as readable text, via an encoding | Stored directly as byte sequences |
| 3 | Readability | Human-readable | Not human-readable |
| 4 | Line structure | Organized into lines, separated by `\n` | No concept of "lines" at all |
| 5 | Encoding required? | Yes (e.g. UTF-8, ASCII) | Not required |
| 6 | Processing complexity | Easy | More complex |
| 7 | File modes | `'r'`, `'w'`, `'a'` | `'rb'`, `'wb'`, `'ab'` |
| 8 | Data interpretation | Directly interpretable as text | Requires a specific program or format-specific logic to interpret |
| 9 | Size efficiency | Usually larger (encoding overhead) | More compact |
| 10 | Speed of processing | Slower | Faster |
| 11 | Portability | High — can be opened almost anywhere | Depends heavily on the specific format and having the right program |
| 12 | Modification | Easy to edit directly, in any text editor | Difficult to edit directly by hand |
| 13 | Error visibility | Errors are usually visible (garbled or broken text) | Errors are often silent, or only visible when the specialized program that reads the format fails |
| 14 | Examples | `.txt`, `.csv`, `.py`, `.log` | `.jpg`, `.mp3`, `.pdf`, `.exe` |
| 15 | Typical use cases | Logs, configuration files, source code | Images, audio/video, compiled programs |
| 16 | Data structure | Sequential characters | A structured binary format, specific to the file type |
| 17 | End-of-line handling | Important — `\n` (Unix/macOS) vs. `\r\n` (Windows) | Not applicable |
| 18 | Encoding issues | Possible (Unicode errors) | Not applicable — bytes are read exactly as stored |
| 19 | Precision (for numbers) | May lose precision, since numbers are stored as their text representation | Exact representation is possible (e.g. a genuine IEEE-754 float, stored bit for bit) |
| 20 | Parsing requirement | Minimal — text is usable more or less as-is | Requires deliberate decoding/parsing logic specific to the format |
| 21 | Human debugging | Easy — just open it and read it | Difficult — requires the right tool or program |
| 22 | Cross-platform compatibility | High | Depends on the specific file format |
| 23 | Typical Python handling | `open("file.txt", "r")` | `open("file.dat", "rb")` |

---

## Deciding which mode to use

![Flowchart](/resources/ch-10-august-2026-text-vs-binary.png)



A simple rule of thumb: if you'd expect to be able to open the file in a plain text editor and read something meaningful, it's a text file. If opening it in a text editor would show you a screen full of unreadable symbols, it's binary.

---

## Worked examples

### Text file: reading and writing

```python
# Step 1: Text mode ("w") expects and produces regular Python strings.
with open("diary.txt", "w", encoding="utf-8") as f:
    f.write("Day 1: Learned about file handling.\n")
    f.write("Day 2: Compared text and binary files.\n")

# Step 2: Reading it back gives you ordinary strings, line by line.
with open("diary.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())   # .strip() removes the trailing newline
# Output:
# Day 1: Learned about file handling.
# Day 2: Compared text and binary files.
```

### Binary file: reading and writing

```python
# Step 1: Binary mode ("wb") expects and produces bytes objects, NOT
# regular strings -- notice the "b" prefix before each string literal
# below, which makes it a bytes object instead of a str.
with open("data.bin", "wb") as f:
    f.write(b"\x00\x01\x02\x03")   # raw bytes, not human-readable text

# Step 2: Reading it back gives you a bytes object, not a string.
with open("data.bin", "rb") as f:
    raw_data = f.read()
    print(raw_data)         # -> b'\x00\x01\x02\x03'
    print(type(raw_data))   # -> <class 'bytes'>
```

### What goes wrong if you mix up the modes

```python
# Trying to open a genuinely binary file in TEXT mode usually raises
# an error, because the raw bytes often can't be decoded as valid
# text under the assumed encoding:
try:
    with open("data.bin", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError as e:
    print("Cannot read binary data as text:", e)

# Trying to write a regular STRING using a binary-mode file object
# also fails immediately, because binary mode expects bytes, not str:
try:
    with open("oops.bin", "wb") as f:
        f.write("This is a string, not bytes")   # TypeError!
except TypeError as e:
    print("Cannot write a string in binary mode:", e)
```

### Encoding in action

```python
# UTF-8 can represent virtually any character from any language --
# this is exactly why "always specify encoding='utf-8'" is good advice.
message = "Café résumé — 日本語"

with open("international.txt", "w", encoding="utf-8") as f:
    f.write(message)

with open("international.txt", "r", encoding="utf-8") as f:
    print(f.read())   # -> Café résumé — 日本語 (perfectly preserved)

# If you open the SAME file assuming the wrong encoding, you can get
# garbled output or an outright error -- this is exactly what row 18
# in the table above ("Encoding issues") refers to.
```

### Precision: text storage vs. binary storage of numbers (row 19)

```python
import struct

value = 0.1

# --- Storing as TEXT ---
with open("number_text.txt", "w") as f:
    f.write(str(value))   # stores the CHARACTERS "0.1"

with open("number_text.txt", "r") as f:
    recovered_text = float(f.read())   # parses "0.1" back into a float
    print(recovered_text == value)     # -> True (this simple case round-trips fine)

# --- Storing as BINARY (exact bit-for-bit representation) ---
with open("number_binary.dat", "wb") as f:
    # struct.pack converts the actual float into its raw 8-byte
    # binary representation -- not its text form at all.
    f.write(struct.pack("d", value))

with open("number_binary.dat", "rb") as f:
    raw = f.read()
    recovered_binary = struct.unpack("d", raw)[0]
    print(recovered_binary == value)   # -> True

# In this particular example both round-trip correctly, but text
# storage becomes riskier for numbers with many decimal digits or
# very large/small magnitudes, where the TEXT representation you
# choose to write might not capture every bit of precision the
# original float actually had -- binary storage avoids that risk
# entirely, since it stores the number's actual bit pattern.
```

### A follow-up question worth exploring

The table's row 9 states that text files are "usually larger" than binary files, due to encoding overhead. As a follow-up exercise: **write the number `1000000` to one file as plain text, and to another file as a 4-byte binary integer (using `struct.pack("i", 1000000)`), then compare the two files' sizes using `os.path.getsize()`.** You should see the binary version is smaller — try to explain *why*, based on how many characters `"1000000"` takes up as text versus how many bytes a 32-bit integer always takes up in binary, regardless of the number's actual value.

---

## Quick recap

- **Every file is really just bytes** — "text" and "binary" describe how those bytes are meant to be *interpreted*, not some fundamentally different kind of storage.
- **The mode you pass to `open()` must match the actual file type** — text mode (`'r'`/`'w'`/`'a'`) for genuinely text-based files, binary mode (`'rb'`/`'wb'`/`'ab'`) for everything else (images, audio, executables, and other non-text formats).
- **Text mode works with `str` objects; binary mode works with `bytes` objects** — mixing the two (writing a string in binary mode, or reading binary data in text mode) raises an immediate, clear error, as shown above.
- **Always specify an encoding explicitly** (`encoding="utf-8"` is the safe default) when working with text files, since relying on your operating system's assumed default can cause portability and Unicode issues later.
- **Binary storage preserves exact bit-for-bit precision**, while text storage represents a number as characters, which can be less exact for values with many decimal digits — the `struct` module (shown above) is the standard tool for reading and writing exact binary number representations.




