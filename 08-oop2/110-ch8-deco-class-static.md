

# Chapter 8.110 — Instance Methods, Class Methods, and Static Methods

## What this page covers

This page is a design assignment for Chapter 8 that clarifies a distinction beginners often gloss over: not every method inside a class behaves the same way. Python actually offers **three** kinds of methods — instance methods (the familiar kind, using `self`), class methods (using `cls`, decorated with `@classmethod`), and static methods (using neither, decorated with `@staticmethod`) — and choosing the right one for a given job is a small but genuinely important design decision.

This matters in everyday Python code more than it might first appear: class methods are the standard way to build **alternative constructors** (a very common real-world pattern, demonstrated below by parsing a formatted string into a `Pet` object), and static methods are the standard way to group a small utility function inside a class for organisational purposes, without pretending it needs access to any specific object's data.

*(The earlier "OOP Conceptual Questions" page, Q8, briefly introduced static vs. instance methods; this page covers all three kinds together, in depth, with a full worked example.)*

---

## Design a `Pet` class to demonstrate

- Instance Method
- Class Method (Factory Method)
- Static Method (Utility Function)

### Instructions

1. Create a class named `Pet`
2. Use variables: `name`, `age`, `species = "Animal"`

### Required methods

| Method Name | Type |
|---|---|
| `show()` | Instance |
| `create_from_string()` | Class Method |
| `is_valid_age()` | Static Method |

### Hints

- Use the `@classmethod` and `@staticmethod` decorators
- Input format for the factory method: `"Tommy-5"`

### Dos and don'ts

- **Do** use `cls` as the first parameter in a class method
- **Do** use no automatic first parameter in a static method — only whatever real inputs it actually needs
- **Don't** use `self` in a static method

### A follow-up question worth exploring

The assignment's `create_from_string()` factory method assumes the input string is always well-formed (`"name-age"`, with the age portion always a valid number). As a follow-up exercise: **what happens if you call `Pet.create_from_string("Tommy")` (no hyphen at all), or `Pet.create_from_string("Tommy-five")` (a non-numeric age)?** Try both and observe the resulting errors — then think about how you might use `is_valid_age()` *inside* `create_from_string()` itself, to reject bad input more gracefully than letting Python's raw error surface. This connects the two custom methods together in a way the original assignment doesn't explicitly ask for, but which is good practice in real code.

---

## Answer / Explanation

- **Instance methods** operate on a specific object's own data, using `self` to access it.
- **Class methods** operate on the *class itself*, using `cls`, and are the standard tool for building alternative ways to create objects (**factory methods**).
- **Static methods** are simple utility functions that don't depend on either the class or any specific object — they're placed inside the class purely for logical organisation.

### Comparison table

| Method type | First parameter | Purpose | Example from the script |
|---|---|---|---|
| Instance | `self` | Works on one specific object's own data | `show()` |
| Class | `cls` | Factory creation — an alternative way to build objects | `create_from_string()` |
| Static | *(none — plain parameters only)* | A general utility function, logically grouped with the class | `is_valid_age()` |


![Flowchart](/resources/ch-8-august-2026-instance-methods-class-methods-etc.png)






---

## The script

```python
# ============================================================
# A. THE Pet CLASS
# ============================================================
class Pet:
    species = "Animal"   # A class attribute, shared by every Pet.

    def __init__(self, name, age):
        # Step 1: The regular constructor, used by the NORMAL way of
        # creating a Pet -- Pet("Tommy", 5).
        self.name = name
        self.age = age

    def show(self):
        # Step 2: INSTANCE METHOD -- uses 'self' to read data that
        # belongs to ONE specific Pet object.
        print(f"{self.name}, {self.age}, {Pet.species}")

    @classmethod
    def create_from_string(cls, data):
        # Step 3: CLASS METHOD -- receives 'cls' (the Pet class
        # itself) instead of 'self'. This is what lets it act as a
        # FACTORY: an alternative way to build a Pet object, starting
        # from a differently-shaped input (a single formatted string,
        # rather than separate name/age arguments).
        name, age = data.split("-")
        # Step 4: 'age' is still a STRING at this point (e.g. "5"),
        # since split() always returns strings -- it must be converted
        # to an int before being used as a real age.
        return cls(name, int(age))
        # Step 5: "cls(name, int(age))" is exactly equivalent to
        # writing "Pet(name, int(age))" here -- but using 'cls'
        # instead of hardcoding "Pet" means this method would still
        # work correctly even on a SUBCLASS of Pet, without needing
        # to be rewritten (see the earlier chapter pages on inheritance).

    @staticmethod
    def is_valid_age(age):
        # Step 6: STATIC METHOD -- no 'self', no 'cls' at all. This
        # method doesn't need to know about any specific Pet object,
        # or even about the Pet class itself -- it's simply a small,
        # self-contained utility function that happens to live inside
        # Pet for logical organisation.
        return age >= 0


# ============================================================
# B. TESTING
# ============================================================

# --- Using the NORMAL constructor ---
p1 = Pet("Tommy", 5)
p1.show()   # -> Tommy, 5, Animal

# --- Using the FACTORY (class) method instead ---
p2 = Pet.create_from_string("Bruno-3")
p2.show()   # -> Bruno, 3, Animal
# Notice: p2 is a completely normal Pet object, indistinguishable from
# p1 -- create_from_string() is just a different DOOR into the same
# house; both ultimately call Pet's real constructor.

# --- Using the STATIC method, directly on the class ---
print(Pet.is_valid_age(5))    # -> True
print(Pet.is_valid_age(-1))   # -> False
# Notice: no Pet object was ever created to make these two calls --
# is_valid_age() works perfectly well called directly on the class itself.
```

---

## Step-by-step summary

1. **The constructor (`__init__`) initializes an object** — the normal, direct way of building a `Pet`.
2. **The instance method (`show()`) accesses one specific object's own data**, using `self`.
3. **The class method (`create_from_string()`) acts as a factory** — it parses an input string, then uses `cls` to build and return a genuine new object, without ever needing to hardcode the class's name.
4. **The static method (`is_valid_age()`) validates an age completely independently** — it doesn't touch `self` or `cls` at all, and works exactly the same whether called on the class or (less commonly) on an instance.

---

## Quick recap

- Python has **three distinct kinds of methods**, distinguished by what their first parameter receives (or doesn't): `self` (instance), `cls` (class), or nothing special at all (static).
- **Class methods are the standard tool for alternative constructors** — `create_from_string()` here provides a second, more convenient "door" into creating a `Pet`, without duplicating `__init__`'s own logic.
- **Static methods are just organisation** — `is_valid_age()` could technically exist as a completely standalone function outside the class, but grouping it inside `Pet` communicates that it's conceptually related to pets, even though it needs no pet-specific data to do its job.
- **Using `cls` instead of hardcoding the class name inside a class method** (as in `cls(name, int(age))`) is good practice, because it keeps the method correct even if the class is later subclassed — a subtlety worth remembering as you build more complex class hierarchies.
- As the follow-up question above highlights, a well-designed factory method often benefits from validating its own input (potentially using another method on the same class, like `is_valid_age()`) rather than assuming the input will always be well-formed.




