



# Chapter 8.120 — Project: Property Decorators (`@property`)

## What this page covers

The earlier "OOP Conceptual Questions" page (Q22) briefly introduced `@property` as a way to combine attribute-style access with the control of a method. This page goes much deeper: it explains exactly what a `property` object *is* internally, how `@property` and `@age.setter` connect to each other, and then applies all of that in a full project — adding validated encapsulation to a `Pet` class's `age` attribute.

This is one of the most practically useful patterns in everyday Python: it lets you start with a plain, simple attribute, and later add validation or other logic *without ever changing how the rest of your code accesses it* — `obj.age` and `obj.age = value` keep working exactly the same, even after a property quietly starts running extra logic behind the scenes.

---

<details>
<summary>Understanding the three attributes <code>fget</code>, <code>fset</code>, and <code>fdel</code> (every property object has these) — click ► to expand</summary>

### Before we proceed further, we need to understand `fget`, `fset`, and `fdel`

**What is `fset` in `Pet.age.fset(p, 10)`?**

`fset` is the **setter function** associated with the property. So `Pet.age.fset(p, 10)` means: *"call the setter function of the property `age` manually."*

#### Step-by-step understanding

**1. What is `Pet.age` actually?**

```python
class Pet:
    @property
    def age(self):
        return self._age
```

Once decorated with `@property`, `age` is **not a normal method anymore** — it becomes a **property object**.

```python
print(type(Pet.age))
```
Output: `<class 'property'>`

**2. What does a property object contain?**

A property internally stores three important functions:

| Attribute | Meaning |
|---|---|
| `fget` | The getter function |
| `fset` | The setter function |
| `fdel` | The deleter function |

**3. What your class internally becomes**

Your code:
```python
class Pet:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
```

...is internally equivalent to:
```python
class Pet:
    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    age = property(get_age, set_age)
```

**What happens in `Pet.age.fset(p, 10)`, step by step:**

1. `Pet.age` → the property object itself
2. `.fset` → its stored setter function
3. `(p, 10)` → call that setter function directly, with `self = p` and `value = 10`

So this ultimately executes: `p._age = 10`.

**Key takeaways:**
- Every property has `fget`, `fset`, and `fdel` — though any of them may be `None` if you never defined that part.
- These are **not** dunder methods — they don't start and end with double underscores.
- They belong to the **property object itself**, not directly to the class.
- They store the *actual functions* used for controlling attribute access.

</details>

<details>
<summary>Discussion on <code>@property</code> and <code>@age.setter</code> — click ► to expand</summary>

Before taking up the project, it's worth understanding exactly how `@property` and `@age.setter` work together.

### A. `@property`

**The core idea:** `@property` **converts a method into something that behaves like an attribute.**

Without `@property`, you'd have to call it like an ordinary method:
```python
def age(self):
    return self._age

print(p.age())   # must call it like a function, with parentheses
```

With `@property`, the same method can be accessed without parentheses at all:
```python
@property
def age(self):
    return self._age

print(p.age)   # looks and behaves exactly like a plain attribute
```

**So:** `@property` allows a method to behave like a variable, from the caller's point of view.

### B. `@age.setter`

**The core idea:** it defines what should happen when you *assign* a value, e.g. `p.age = 10`.

Internally, Python converts that assignment into: `Pet.age.fset(p, 10)`, which in turn calls your actual setter method, `def age(self, value):`.

**So:** `@age.setter` defines exactly how assignment is handled.

### C. The link between `@property` and `@age.setter`

This is the single most important concept on this page.

1. **`@property` creates a property object.** Writing `@property` above `def age(self):` is equivalent to `age = property(getter_function)`.
2. **`@age.setter` attaches a setter to that *same* property object**, rather than creating a second, separate one. Writing `@age.setter` above a second `def age(self, value):` modifies the existing property, effectively becoming `age = property(getter, setter)`.
3. **So both the getter and setter belong to one single property object.** You can visualize this as:

```text
age (property object)
├── getter -> returns _age
└── setter -> validates and sets _age
```

### D. Where are `@property` and `@age.setter` actually defined?

They're **built into Python itself** — no import is needed. Internally, `property` is simply a built-in class, and `@property` (along with `@age.setter`) is just convenient syntactic sugar layered on top of it.

</details>

![Flowchart](/resources/ch-8-august-2026-property-decorator.png)





---

## Project / Assignment Task

*(Kept exactly as set in the assignment.)*

Modify a `Pet` class to implement **encapsulation using property decorators**.

### Instructions

- Use attribute: `_age`
- Provide: Getter, Setter, and (optionally) a Deleter

### Hints

- Use `@property` and `@age.setter`
- Raise an error if `age < 0`

### Dos and don'ts

- **Do** use `_age` internally (see the earlier chapter page on encapsulation and name mangling for the general convention this follows)
- **Do** validate age
- **Don't** write `self.age = value` *inside* the setter itself (this would call the setter again, causing infinite recursion — see the follow-up question below)

### A follow-up question worth exploring

The "don't" above warns against writing `self.age = value` inside the setter. As a follow-up exercise: **try it yourself, deliberately, and observe what happens.** Change the setter's last line from `self._age = value` to `self.age = value`, then run the script. You should see a `RecursionError`. Before running it, try to predict *why* this happens, based on what you now know about how `@age.setter` and assignment are connected (Section B above is the key clue).

---

## Answer / Solution

- A **property** allows controlled access to an attribute, while still letting calling code use simple, ordinary attribute syntax.
- It **replaces** separate `get_age()`/`set_age()` methods with the same familiar `obj.age` / `obj.age = value` syntax.
- **Validation logic can be added invisibly** — none of the code that *uses* a `Pet` object needs to change, even after validation is added to the setter.

### Comparison table

| Feature | Traditional (getter/setter methods) | Property |
|---|---|---|
| Access | `get_age()` | `obj.age` |
| Modify | `set_age()` | `obj.age = value` |
| Validation | Manual — the caller must remember to call `set_age()` instead of setting an attribute directly | Built-in — ordinary assignment (`obj.age = value`) automatically runs the validation |

---

## Solution script

```python
# ============================================================
# A. THE Pet CLASS
# ============================================================
class Pet:
    def __init__(self, name, age):
        self.name = name
        # Step 1: Notice we assign to self._age here, NOT self.age --
        # this deliberately bypasses the property's setter during
        # initial construction... actually, in Python, assigning to
        # self._age directly is a plain, ordinary attribute assignment
        # (there's no property named "_age"), while self.age = age
        # WOULD go through the property setter below. Either works
        # here since the value is already valid, but going through
        # self._age keeps this line simple and explicit.
        self._age = age

    # ------------------------------------------------------------
    # B. GETTER -- makes age READABLE as a plain attribute
    # ------------------------------------------------------------
    @property
    def age(self):
        # Step 2: This turns "age" into a property object. From now
        # on, reading p.age (with no parentheses) calls this method
        # automatically and returns the real, stored value from _age.
        return self._age

    # ------------------------------------------------------------
    # C. SETTER -- makes age WRITABLE, but with validation
    # ------------------------------------------------------------
    @age.setter
    def age(self, value):
        # Step 3: This attaches a setter to the SAME property object
        # created above -- it does NOT create a second, separate
        # property. From now on, writing p.age = <value> calls this
        # method automatically, passing <value> as the 'value' parameter.
        if value < 0:
            # Step 4: Reject invalid input immediately, before it's
            # ever stored -- this is the entire point of using a
            # property instead of a plain public attribute.
            raise ValueError("Invalid age")
        self._age = value
        # Step 5: Store the validated value in the REAL underlying
        # attribute, _age -- never write "self.age = value" here, or
        # you would call this exact setter again, forever (see the
        # follow-up question above).


# ============================================================
# B. TESTING
# ============================================================
p = Pet("Tommy", 5)
print(p.age)   # -> 5
# This LOOKS like plain attribute access, but is secretly calling the
# getter method defined above.

p.age = 10
print(p.age)   # -> 10
# This LOOKS like plain attribute assignment, but is secretly calling
# the setter method, which validates 10 (>= 0) before storing it.

# p.age = -5   # Uncommenting this raises: ValueError: Invalid age
```

---

## Quick recap

- A **property object** bundles up to three functions — `fget`, `fset`, and (optionally) `fdel` — behind what looks, from the outside, like an ordinary attribute.
- **`@property` converts a method into a getter**, letting it be accessed without parentheses; **`@age.setter` attaches a setter to that *same* property**, letting assignment (`p.age = value`) run your own validation logic automatically.
- **This is entirely built into core Python** — no imports needed, and `@property`/`@x.setter` are just convenient syntax layered over the built-in `property` class.
- **The biggest pitfall** is writing `self.age = value` *inside* the setter itself — since that assignment is exactly what triggers the setter to run, doing so inside the setter creates infinite recursion. Always assign to the real underlying attribute (`self._age`) inside the setter instead.
- **The practical payoff**: adding a property to an existing class doesn't require changing any of the code that already uses `obj.age` or `obj.age = value` — validation and other logic can be added completely invisibly to the rest of your program.





