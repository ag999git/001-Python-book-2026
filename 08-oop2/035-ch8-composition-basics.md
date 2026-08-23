


# Chapter 8 — Has-A Relationships: Composition, Aggregation, and Dependency

## What this page covers

The earlier pages in this chapter focused entirely on **Is-A relationships** — inheritance, where a `Dog` *is a* `Pet`. This page introduces the other major way classes relate to each other in object-oriented design: **Has-A relationships**, where one object is *built using* other objects, rather than being a specialized type of something else.

This distinction matters immensely in real Python programs, because not every relationship between two classes should be modeled with inheritance. A `Car` isn't a type of `Engine` — but a `Car` definitely *has* an `Engine`. Recognising which kind of relationship you actually have — and which of the three flavours of Has-A relationship covered here fits best — is one of the more important design skills in OOP, and gets easier to spot the more examples you see.

**A few terms used throughout, explained simply:**
- **Ownership** — whether one object controls the existence of another. Strong ownership means "if I go, you go too"; weak ownership means "we're associated, but you can outlive me."
- **Object lifetime** — how long an object exists in memory before it's cleaned up (see the earlier chapter page on `del` and `__del__()` for the mechanics of how Python actually manages this).
- **Coupling** — how tightly two pieces of code depend on each other. High coupling means changes to one are likely to require changes to the other; low coupling means they can change more independently. ([Wikipedia: Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming)))

---

## 1. Introduction

In object-oriented design, not every relationship between classes is hierarchical. Inheritance (Is-A) answers the question *"what type of thing is this?"* — but very often, the real question is instead *"what is this thing made of?"* That second question leads to **Has-A relationships**: cases where one object is built by containing, referencing, or temporarily using other objects.

Not all Has-A relationships behave the same way, though. They differ along four dimensions:

| Dimension | The question it answers |
|---|---|
| **Ownership** | Does the containing object truly *own* the contained one? |
| **Object creation** | Is the contained object built *inside* the container, or handed to it from *outside*? |
| **Object lifetime** | Does the contained object's life depend on the container's life, or is it independent? |
| **Degree of dependency** | Is the relationship permanent, long-term, or just momentary? |

These four questions are exactly what distinguish the three kinds of Has-A relationship covered below: **Composition**, **Aggregation**, and **Dependency**, ordered from strongest to weakest.

![Flowchart](/resources/ch-8-august-2026-3-types-of-has-a-relationship.png)




---

## 2. The Three Types of Has-A Relationships

### 2.1 Composition (Strong Has-A Relationship)

**Definition:** Composition is a relationship where one class **strongly owns** another class, and the contained object **cannot logically exist independently** of the owner.

**Key characteristics:**
- The contained object is **created inside** the owning class (usually inside `__init__`)
- Strong ownership
- Not shared with other objects
- Lifetime is **dependent on the owner**
- Represents a **whole–part relationship**

**Conceptual example:** *A Dog has a Collar.* The collar is tightly linked to a specific dog — if that `Dog` object is removed, its `Collar` conceptually goes with it. In a strong Has-A relationship, the `Collar` object is created *inside* the `Dog` object, and its lifetime is entirely tied to it.

- Whole (`Dog`) **controls the lifecycle** of the part (`Collar`)
- The part has **no independent identity** — it wasn't created before the `Dog`, and doesn't outlive it
- **Tight coupling** — a `Collar` in this design doesn't make sense without its `Dog`

**Interpretation:** *"Built inside, owned completely."*

```python
class Collar:
    def __init__(self, color):
        self.color = color
        print(f"A {self.color} collar has been made.")


class Dog:
    def __init__(self, name, collar_color):
        self.name = name
        # COMPOSITION: the Collar object is created INSIDE Dog's own
        # constructor. Nothing outside Dog ever creates a Collar, and
        # no other Dog can ever use THIS particular Collar object.
        # Its entire existence is tied to this one Dog.
        self.collar = Collar(collar_color)
        print(f"{self.name} now has a collar.")


# Creating a Dog automatically creates its Collar as a side effect --
# you never interact with Collar directly from outside.
d = Dog("Tommy", "Red")
print(f"{d.name}'s collar color: {d.collar.color}")

# If 'd' is deleted, its Collar has no other reference keeping it
# alive anywhere else in the program -- it becomes eligible for
# garbage collection right along with Tommy (see the earlier chapter
# page on 'del' and reference counting for exactly how this works).
del d
```

---

### 2.2 Aggregation (Weak Has-A Relationship)

**Definition:** Aggregation is a relationship where one class **uses or contains** another class, but the contained object **exists independently**.

**Key characteristics:**
- The contained object is **created outside** the containing class
- Weak ownership
- Can be **shared** among multiple objects
- Lifetime is **independent** of the container
- Represents a **container–content relationship**

**Conceptual example:** *A Dog has a Toy.* Unlike the collar, the toy exists independently of any one dog — the same toy could be handed to a different dog tomorrow. In a weak Has-A relationship, the `Toy` object's existence doesn't depend on the `Dog` object at all; it doesn't "die" when the dog does.

- The whole (`Dog`) does **not control** the part's (`Toy`'s) lifecycle
- The part has an **independent identity** — it existed before being given to the dog, and continues existing afterward
- **Loose coupling**

**Interpretation:** *"Received from outside, not owned."*

**When to use aggregation:** when objects are loosely related, and reuse/sharing between multiple owners is genuinely needed.

```python
class Toy:
    def __init__(self, name):
        self.name = name


class Dog:
    def __init__(self, name):
        self.name = name
        self.toy = None   # No toy yet -- it will be assigned from outside.

    def receive_toy(self, toy):
        # AGGREGATION: the Toy object is created OUTSIDE this class,
        # and simply handed in and stored. Dog never builds its own
        # Toy -- it only ever receives one that already exists.
        self.toy = toy
        print(f"{self.name} now has the toy: {self.toy.name}")


# The Toy is created independently, BEFORE either Dog exists.
shared_ball = Toy("Squeaky Ball")

dog1 = Dog("Tommy")
dog2 = Dog("Rex")

# The SAME Toy object can be given to more than one Dog -- this
# sharing is only possible because Toy's lifetime is independent
# of any single Dog (unlike Collar in the Composition example).
dog1.receive_toy(shared_ball)
dog2.receive_toy(shared_ball)

# Even if BOTH dogs are deleted, the Toy object survives, as long as
# something else (like the 'shared_ball' variable here) still refers to it.
del dog1
del dog2
print(f"The toy still exists: {shared_ball.name}")
```

---

### 2.3 Dependency (Uses-A Relationship)

**Definition:** Dependency is a relationship where one class **temporarily uses** another class, without storing or owning it at all.

**Key characteristics:**
- The object is **used temporarily**
- Not stored as an attribute
- A **very weak** relationship — the weakest of the three
- Exists only **during method execution**
- No ownership whatsoever

**Conceptual example:** *A Dog uses a Toy to play.* Here, the toy is simply passed in as a parameter to a method, used briefly, and then forgotten — the `Dog` object never keeps a lasting reference to it.

**Interpretation:** *"Used when needed, then forgotten."*

**When to use dependency:** when an object is only needed for a single task, and storing it permanently would be unnecessary.

```python
class Toy:
    def __init__(self, name):
        self.name = name


class Dog:
    def __init__(self, name):
        self.name = name
        # Notice: Dog does NOT store a toy attribute at all here --
        # unlike both the Composition and Aggregation examples above.

    def play(self, toy):
        # DEPENDENCY: 'toy' is passed in as a plain method parameter.
        # It's used only for the duration of this one method call, and
        # is never saved anywhere on the Dog object (self.toy is never
        # set) -- once play() returns, Dog has no lasting connection
        # to this particular Toy at all.
        print(f"{self.name} is playing with {toy.name}!")


d = Dog("Tommy")
ball = Toy("Tennis Ball")
frisbee = Toy("Frisbee")

# The SAME Dog can be handed a DIFFERENT toy on every call, because
# nothing about the toy is ever remembered between calls.
d.play(ball)
d.play(frisbee)

# Confirm Dog never stored either toy:
print(hasattr(d, "toy"))   # -> False
```

---

## 3. Comparative table

| Feature | Composition (Strong) | Aggregation (Weak) | Dependency (Very Weak) |
|---|---|---|---|
| Relationship type | Strong Has-A | Weak Has-A | Uses-A |
| Ownership | Strong | Weak | None |
| Object creation | Inside the class | Outside the class | Outside the class |
| Lifetime dependency | Dependent on owner | Independent | Independent |
| Sharing | Not shared | Can be shared | Not relevant (never stored) |
| Storage | Stored as an attribute | Stored as an attribute | Not stored at all |
| Duration | Permanent (for the owner's lifetime) | Long-term | Temporary (one method call) |
| Coupling | High | Medium | Low |
| Example | Dog–Collar | Dog–Toy | Dog uses Toy to play |
| Destruction effect | Part is destroyed with the whole | Part survives independently | No effect either way |

---

## Choosing between the three: a quick mental checklist

When deciding how to model a relationship between two classes in your own code, these three questions usually settle it:

1. **Does the contained object's existence make sense without the container?** If no — it's **Composition**. If yes, move to the next question.
2. **Does this object need to be stored and reused across multiple method calls, possibly shared with other objects too?** If yes — it's **Aggregation**. If no, move to the next question.
3. **Is this object only ever needed briefly, for one specific task, and never stored?** If yes — it's a **Dependency**.

### A follow-up question worth exploring

The original material focuses on conceptual definitions and a single running example (`Dog`/`Collar`/`Toy`). As a follow-up exercise worth trying yourself: **can you think of a real-world class design where the same two classes could reasonably be modeled as either Composition or Aggregation, depending on the specific application?** (Hint: consider a `Car` and an `Engine` — in most everyday software, an `Engine` is tightly bound to one `Car` (Composition), but in a car-manufacturing simulation where engines are built on a separate line and later installed into different car bodies, the same pair of classes might be better modeled as Aggregation instead. The "correct" choice depends on what your program actually needs to represent, not on some fixed rule about the real-world objects themselves.)

---

## Quick recap

- **Has-A relationships** model "built from" rather than "is a type of" — they complement, rather than replace, the inheritance (Is-A) relationships covered earlier in this chapter.
- **Composition** is the strongest form: the contained object is created inside the owner, isn't shared, and its lifetime is tied directly to the owner's (Dog–Collar).
- **Aggregation** is weaker: the contained object is created independently, can be shared across multiple owners, and survives even if a particular owner is deleted (Dog–Toy).
- **Dependency** is the weakest: the object is only used briefly, passed in as a method parameter, and never stored at all (Dog uses Toy to play).
- In practice, the right choice between the three depends less on the real-world objects themselves and more on what your specific program actually needs them to do — as the `Car`/`Engine` follow-up question above illustrates.





