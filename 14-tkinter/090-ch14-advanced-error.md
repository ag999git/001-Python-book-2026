

# Research / Project Question

## Professional Error Handling in Tkinter

Modern GUI applications should be able to:

-   validate user input automatically,
-   record errors for debugging,
-   safely handle unexpected failures.

Tkinter supports these features using: `loggingsys.excepthooktrace_add()`


## Part A — Theory

Research and explain the following:

### 1. What is: `logging` and why is it used instead of: `print()`?

### 2. What is: `sys.excepthook` and what is its purpose?

### 3. What is: `trace_add()` and why is it useful with: `StringVar()`?

### 4. Explain: `live validation` with one example.

### 5. Why do professional applications log errors instead of only displaying them?


## Part B — Script Writing

Write a Tkinter program that:

1.  Creates an Entry widget for numeric input.
2.  Validates input while typing using: `trace_add()`
3.  Shows: `Valid input` or `Numbers only` in real time.

4.  Logs activity into: `app_log.txt` 

5.  Uses: `sys.excepthook` for global exception handling.

6.  Adds a button: `Trigger Error` to deliberately create an uncaught error.

7.  Shows a friendly popup instead of crashing.

----------

# Theory Solution

## 1. What is `logging`?

Logging means:

> recording program activity and errors in a file.

Example:

```python
logging.info("User clicked")
```

Unlike:

```python
print()
```

logs remain saved after the program closes.


## 2. What is `sys.excepthook`?

`sys.excepthook` is Python’s:

> global exception handler

It controls what Python does when: `uncaught exception` happens.

Normally the sequence of execution is as follows:

```python
Error
↓
Traceback shown
↓
Program crashes
```

But: `sys.excepthook =handle_error` changes the route.

Now the sequence is as follows:

```python
Error
↓
Custom function runs
↓
Popup + log
```

This improves application safety.

----------

## 3. What is `trace_add()`?

`trace_add()` monitors a Tkinter variable.

Example:

```python
name_var.trace_add("write", validate)
# Meaning: Whenever variable changes,run validate()
```

It is commonly used with: `StringVar()` because Entry widgets use variables.

----------

## 4. What is Live Validation?

Live validation means:

> checking input while the user is typing.

Example:

Instead of waiting for: `Submit button` program checks immediately.

  -  Suppose we have incorrect Input: `abc`, we immediately get an Output: `Numbers only` 

  -  Suppose we have correct Input: `25` we get Output: `Valid input` 

This improves user experience.


## 5. Why Do Professional Apps Log Errors?

Errors may happen unexpectedly.
Examples of unexpected errors are:
```python
user enters bad data
network fails
program bug appears
```
A popup helps the user. But developers also need technical details.

Logs help programmers:

-   debug problems,
-   understand failures,
-   improve software.

----------

## Script 3 — Advanced Tkinter Safety

Research / Project Question
Professional Error Handling in Tkinter
Modern GUI applications should be able to:
  -  validate user input automatically,
  -  record errors for debugging,
  -  safely handle unexpected failures.
  -  Tkinter supports these features using: loggingsys.excepthooktrace_add()

## Part A — Theory
### Research and explain the following:

1. What is: logging and why is it used instead of: print()?
2. What is: sys.excepthook and what is its purpose?
3. What is: trace_add() and why is it useful with: StringVar()?
4. Explain: live validation with one example.
5. Why do professional applications log errors instead of only displaying them?

### Part B — Script Writing
Write a Tkinter program that:
  -  Creates an Entry widget for numeric input.
  -  Validates input while typing using: trace_add()
  -  Shows: Valid input or Numbers only in real time.
  -  Logs activity into: app_log.txt
  -  Uses: sys.excepthook for global exception handling.
  -  Adds a button: Trigger Error to deliberately create an uncaught error.
  -  Shows a friendly popup instead of crashing.

## Theory Solution
### 1. What is logging?
Logging means:
>recording program activity and errors in a file.

```python
# Example:
logging.info("User clicked") # logs remain saved after the program closes.
# However 
print() # logs not saved
```


Why not print()?
print()	logging

| print() | logging |
| --- | --- |
| Temporary | Permanent |
| Screen only | Saved to file |
| Hard to debug later | Useful for debugging |

### 2. What is sys.excepthook?
sys.excepthook is Python’s:

global exception handler

It controls what Python does when: uncaught exception happens.

Normally the sequence of execution is as follows:

```python
Error
↓
Traceback shown
↓
Program crashes
```
But: sys.excepthook =handle_error changes the route.

Now the sequence is as follows:

```python
Error
↓
Custom function runs
↓
Popup + log
```
This improves application safety.

### 3. What is trace_add()?
trace_add() monitors a Tkinter variable.

Example:

`name_var.trace_add("write", validate)`
Meaning: Whenever variable changes,run validate()
It is commonly used with: StringVar() because Entry widgets use variables.

### 4. What is Live Validation?
Live validation means:

checking input while the user is typing.

Example:

Instead of waiting for: Submit button program checks immediately.

Suppose we have incorrect Input: abc, we immediately get an Output: Numbers only

Suppose we have correct Input: 25 we get Output: Valid input

This improves user experience.

### 5. Why Do Professional Apps Log Errors?
Errors may happen unexpectedly.
Examples of unexpected errors are:

user enters bad data
network fails
program bug appears
A popup helps the user. But developers also need technical details.

Logs help programmers:

debug problems,
understand failures,
improve software.
Script 3 — Advanced Tkinter Safety
Markdown 3076 bytes 461 words 163 lines Ln 157, Col 24HTML 2272 characters 393 words 85 paragraphs

## Script


```python
import tkinter as tk
from tkinter import messagebox
import logging
import sys

# 1. LOGGING SETUP
# Create log file: app_log.txt
# INFO means: (normal activity + errors)→ both will be saved.
logging.basicConfig(filename="app_log.txt", level=logging.INFO)

# 2. CREATE MAIN WINDOW
root = tk.Tk()
root.title("Advanced Validation")
root.geometry("420x320")

# 3. CREATE LOG PANEL
# Text widget acts like mini consolel. It shows: (1) what user typed, (2) program activity, (3) errors.
#tk.Text() creates a multi-line text area. height=8 means 8 lines tall, width=45 means 45 characters wide.
log_box = tk.Text(root, height=8, width=45)
log_box.pack(pady=10)

# 4. write_log()
# Shows message inside GUI and saves it to file.
def write_log(message):
    # Show in GUI
    log_box.insert(tk.END, message + "\n")
    # Auto-scroll
    log_box.see(tk.END)
    # Save to log file
    logging.info(message)
    # Also print to terminal for debugging purposes.
    print(message)

# 5. GLOBAL ERROR HANDLER
# Runs when uncaught error happens.
# exec_type, exc_value, exc_traceback are the error details that Python passes to this function 
# when an uncaught error occurs.
def handle_error(exc_type, exc_value, exc_traceback):
    # Create readable error message named error_msg from the error details.
    error_msg = (f"{exc_type.__name__}: "f"{exc_value}")
    # Show steps in log panel in the GUI window.
    write_log(f"ERROR → {error_msg}")
    # Show popup messagebox with error message.
    messagebox.showerror("Unexpected Error", error_msg)
    # Also save error to file named app_log.txt using logging.error()
    logging.error(error_msg)

# 6. OVERRIDE DEFAULT ROUTE
# Replace Python's default crash route.
sys.excepthook = handle_error
write_log("Global hook installed")

# 7. CREATE VARIABLE
# Stores Entry value.
# Whenever user types, validate() runs automatically.
# tk.StringVar() creates a special variable that can be attached to widgets. 
# When the value of the variable changes (e.g. when the user types in an Entry widget), 
# it can trigger a callback function. In this case, we will use input_var.trace_add() to 
# call the validate() function whenever the value of input_var changes.
input_var = tk.StringVar()

# 8. STATUS LABEL
status = tk.Label(root, text="Enter number")
status.pack()

# 9. VALIDATION FUNCTION
# Runs automatically whenever user types.
def validate(*args):
    # Get current text from input_var
    text = input_var.get()
    # Show what user typed in log panel in the GUI window.
    write_log(f"User typed: {text}")

    # If the input is empty, we consider it as waiting for input rather than invalid. 
    # So we update the status label to "Waiting..." and return without doing any further validation.
    if text == "":  
        status.config(text="Waiting...")
        return

    try:
        # Try to convert the input to an integer. If this fails, it will raise a ValueError 
        # which we will catch in the except block.
        number = int(text)  
        # If conversion is successful, we consider it valid input. We update the status label 
        # to "Valid input" and log this information.
        status.config(text="Valid input")
        # Also log that the input is valid. This will be saved to the app_log.txt file and 
        # also shown in the terminal for debugging purposes.
        write_log("Valid input")

    except ValueError:
        # If a ValueError occurs during the int() conversion, it means the input was not a 
        # valid integer.
        # We update the status label to "Numbers only" to inform the user about the validation
        status.config(text="Numbers only")
        # We also log that the input is invalid. This will be saved to the app_log.txt file and 
        # also shown in the terminal for debugging purposes.
        write_log("Invalid input")


# 10. ATTACH trace_add()
# trace_add() is a method of StringVar that allows us to specify a user defined callback function 
# here named (validate) that will be called whenever the value of the StringVar changes.
# "write" means that the callback will be triggered whenever the value is written to 
# (i.e. when the user types something in the Entry widget).
input_var.trace_add("write", validate)

# 11. ENTRY WIDGET
# This is where the user types their input. It is linked to input_var, so whenever the user 
# types something, input_var changes, which triggers the validate() function to run and perform 
# validation on the input.
entry = tk.Entry(root, textvariable=input_var)
entry.pack(pady=5)

# 12. DELIBERATE ERROR
# Used to test global exception handler.
def trigger_error():
    # Log that we are about to trigger an error. This will be shown in the log panel in the GUI 
    # and also saved to the app_log.txt file.
    write_log("Trigger Error clicked")
    # Deliberately trigger a NameError by trying to print an undefined variable. Since there is no 
    # try-except block to catch this error, it will be caught by our global error
    print(unknown_variable)

# 13. BUTTON
tk.Button(root, text="Trigger Error", command=trigger_error).pack(pady=10)

# 14. START GUI
root.mainloop()

```

## Flowchart
The flowchart shows steps in execution of the given script

![Flowchart](/resources/ch14-tkinter-professional-error-handling.png)









