# Chapter 7 — Proving That `self` Is Just the Object Itself

## What this page covers

This page is a short, hands-on experiment for Chapter 7 (Object-Oriented Programming). It answers a question almost every beginner asks sooner or later: **"What actually *is* `self`?"**

Many beginners are told to treat `self` as a fixed rule — "just always write `self` as the first parameter of a method" — without ever being shown *why*. This page removes the mystery using Python's built-in `id()` function: it shows, with real output, that `self` inside a method and the object you called that method on are, quite literally, the exact same thing in memory. Once this clicks, a lot of other OOP behaviour (why `self.name` works, why every object keeps its own data, why methods can tell objects apart) starts to make a lot more sense.

By the end of this page you should be able to:
- Explain what `id()` returns and why it's useful for this experiment.
- Explain, in your own words, why `id(p1) == id(self)` inside `p1.show_id()`.
- Predict what would happen if you ran the same experiment with a third object.

---

## 1. Background: what does `id()` actually return?

Every object you create in Python — a number, a string, a list, or an instance of your own class — is stored somewhere in the computer's memory. Python's built-in `id()` function returns a number that identifies *where* that object lives, for as long as the object exists. Think of it as the object's **home address**: two different objects (almost) always have two different addresses, and the same object always has the same address, no matter how many names or variables point to it.

> **Note for beginners:** the exact number `id()` returns isn't something you should ever rely on in real programs — it can differ every time you run your code, and even between different Python implementations. What *is* reliable, and what this experiment is really about, is the **relationship** between the addresses: whether two things share the same address or not.

## 2. The experiment, in plain English

1. We create an object, `p1 = Pet("Tiger")`, and print `id(p1)` — this is the object's address as seen **from outside** the class.
2. We then call a method on that same object, `p1.show_id()`, and inside the method we print `id(self)` — this is the address as seen **from inside** the class.
3. If `self` really is just another name for "the object this method was called on," then these two addresses must match exactly.
4. We repeat the whole thing with a second, completely separate object, `p2 = Pet("Kittie")`, to prove this isn't a coincidence — each object has its own unique address, and `self` always tracks whichever object is "currently acting."

| Step | What we check | What it proves |
|---|---|---|
| `id(p1)` outside the class | The address Python gave to the `p1` object | A baseline "home address" for `p1` |
| `id(self)` inside `p1.show_id()` | The address Python sees `self` pointing to, during that call | `self` refers to the exact same object as `p1` |
| `id(p2)` outside the class | The address Python gave to the `p2` object | A different, independent "home address" for `p2` |
| `id(self)` inside `p2.show_id()` | The address Python sees `self` pointing to, during that call | `self` now refers to `p2` — it always matches whichever object made the call |

## 3. The script

```python
# This script demonstrates that the 'self' parameter inside a class method
# is not a special keyword — it is simply a reference to whichever object
# called that method. We prove this by comparing id(self) inside the method
# to id(object) taken from outside the class.

class Pet:
    def __init__(self, name):
        # __init__ runs automatically when a new Pet object is created.
        # 'self' here refers to the new (still being built) object,
        # and self.name = name stores 'name' as an attribute on that object.
        self.name = name

    def show_id(self):
        # 'self' is automatically passed in whenever you call
        # something.show_id() — Python fills it in for you.
        # It always refers to the specific object the method was called on.
        print(f"Inside method for {self.name}, id(self) is: {id(self)}")


# --- Creating two separate objects ---
p1 = Pet("Tiger")    # creates the first Pet object and stores it in p1
p2 = Pet("Kittie")   # creates a second, independent Pet object in p2

# --- Checking Pet 1 ---
print(f"Outside class, id(p1) is: {id(p1)}")
# id() here reports p1's memory address, seen from outside the class.

p1.show_id()
# Python translates this call into Pet.show_id(p1) behind the scenes,
# so inside the method, self *is* p1 — hence id(self) == id(p1).

print("-" * 30)   # just a visual separator in the printed output

# --- Checking Pet 2 ---
print(f"Outside class, id(p2) is: {id(p2)}")
# A different address, because p2 is a completely separate object.

p2.show_id()
# This time self refers to p2, so id(self) == id(p2) — not id(p1).
```

### Expected output (the exact numbers will differ on your machine)

```text
Outside class, id(p1) is: 140312831234576
Inside method for Tiger, id(self) is: 140312831234576
------------------------------
Outside class, id(p2) is: 140312831239120
Inside method for Kittie, id(self) is: 140312831239120
```

Notice the pattern: **the first pair of numbers matches, the second pair of numbers matches, but the two pairs don't match each other.** That's the whole experiment, confirmed in four lines of output.

## 4. Why this matters

Once you've seen `id(p1) == id(self)` with your own eyes, several ideas about classes stop being "rules to memorize" and start being obvious consequences:

- **`self.name = name` inside `__init__` really does store data on that specific object** — because `self` *is* that object, not a copy of it.
- **Every object keeps its own independent data.** `p1.name` and `p2.name` don't clash, because `p1` and `p2` are different objects at different addresses, each with its own copy of `name`.
- **`self` is just a naming convention, not a keyword.** Python doesn't require the name `self` — you could technically call it `this` or `me` — but every Python programmer uses `self` by convention, so method definitions are consistent and readable across any codebase.
- **`obj.method()` is shorthand for `Class.method(obj)`.** Python automatically passes the object as the first argument, which is exactly why every regular method needs `self` as its first parameter.

## 5. Try it yourself

To make the idea stick, try extending the script:
- Add a third object, `p3 = Pet("Rex")`, and confirm `id(p3)` behaves the same way.
- Add a second method, say `compare_with(self, other_pet)`, that prints whether `self` and `other_pet` share the same `id()` — then call `p1.compare_with(p1)` and `p1.compare_with(p2)` to see the difference.

