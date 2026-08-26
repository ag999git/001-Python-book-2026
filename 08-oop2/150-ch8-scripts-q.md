


# Chapter 8.150 — 20 Programming Script Questions & Answers

## What this page covers

This page is a hands-on companion to the two "Conceptual Questions" review pages earlier in this chapter — where those pages tested *definitions*, this page tests whether you can actually **write the code** behind each concept: inheritance patterns, MRO, composition, abstraction, properties, custom containers, and `__slots__`, all in short, focused scripts.

Each of the twenty questions below keeps the code from the original assignment, with a short plain-language explanation added before it, fuller step comments added inside it, and — for scripts that didn't originally show their output — the expected output added so you can check your own run against it.

---

**1. Create a `Vehicle` parent class and a `Car` child class. Use the `pass` keyword to demonstrate "Implicit Is-A" inheritance.**

This is the simplest possible form of inheritance: `Car` adds nothing of its own at all, so it behaves as an exact copy of `Vehicle`.

```python
class Vehicle:
    def move(self):
        print("This vehicle is moving")

# Step 1: 'pass' means Car adds NOTHING new -- it inherits move()
# completely unchanged from Vehicle.
class Car(Vehicle):
    pass

c = Car()
c.move()   # -> This vehicle is moving
```

---

**2. Write a script that uses `isinstance()` to check if a `Puppy` object is an instance of `Dog` and an instance of `Pet`.**

This demonstrates **transitivity** (covered on the earlier "30 Conceptual Questions" page, Q6): `Puppy` inherits from `Dog`, which inherits from `Pet`, so a `Puppy` object correctly counts as *both*.

```python
class Pet: pass
class Dog(Pet): pass
class Puppy(Dog): pass

p = Puppy()

# Step 1: isinstance() checks the FULL ancestry chain, not just the
# immediate parent -- that's exactly what transitivity means in practice.
print(f"Is p a Dog? {isinstance(p, Dog)}")   # -> True
print(f"Is p a Pet? {isinstance(p, Pet)}")   # -> True
```

---

**3. Demonstrate the `__mro__` attribute by creating a three-level hierarchy: `Animal -> Mammal -> Cat`.**

```python
class Animal: pass
class Mammal(Animal): pass
class Cat(Mammal): pass

# Step 1: __mro__ shows the exact order Python would search through
# this hierarchy when looking for a method.
print(Cat.__mro__)
# Output: (<class '__main__.Cat'>, <class '__main__.Mammal'>,
#          <class '__main__.Animal'>, <class 'object'>)
```

---

**4. Create a class where the child class's `__init__` explicitly calls the parent's `__init__` using `super()`.**

This is **constructor chaining** — see the earlier chapter pages on inheritance and `super()` for the full picture.

```python
class Bird:
    def __init__(self, species):
        self.species = species

class Parrot(Bird):
    def __init__(self, species, color):
        # Step 1: Reuse Bird's own setup logic for 'species', instead
        # of duplicating "self.species = species" here.
        super().__init__(species)
        self.color = color   # Step 2: Parrot-specific attribute.

p = Parrot("Parrot", "Green")
print(p.species, p.color)   # -> Parrot Green
```

---

**5. Write a script that creates a class attribute and an instance attribute, then prints the `__dict__` of both the class and the instance.**

See the earlier "`__dict__`" chapter page for the full explanation of why these two dictionaries look so different from each other.

```python
class Robot:
    laws = "Protect humans"   # Class attribute -- lives in Robot's own __dict__.

    def __init__(self, name):
        self.name = name   # Instance attribute -- lives in THIS object's __dict__.

r = Robot("R2D2")

print("Class Dict:", Robot.__dict__)
# Output (abbreviated): {'__module__': '__main__', 'laws': 'Protect humans', ...}

print("Instance Dict:", r.__dict__)
# Output: {'name': 'R2D2'}
# Notice 'laws' does NOT appear here -- it lives only on the class.
```

---

**6. Use multiple inheritance to create a `FlyingFish` class that inherits from both `Bird` (for flying) and `Fish` (for swimming).**

```python
class Bird:
    def fly(self): print("Flying...")

class Fish:
    def swim(self): print("Swimming...")

# Step 1: FlyingFish combines behaviour from BOTH parents at once --
# this is multiple inheritance, covered fully in the earlier
# "Diamond Problem" chapter page.
class FlyingFish(Bird, Fish):
    pass

ff = FlyingFish()
ff.fly()    # -> Flying...
ff.swim()   # -> Swimming...
```

---

**7. Demonstrate "Method Overriding" by creating a parent class `Shape` with a `draw()` method and a child class `Circle` that changes the `draw()` message.**

```python
class Shape:
    def draw(self):
        print("Drawing a generic shape")

class Circle(Shape):
    def draw(self):
        # Step 1: This completely REPLACES Shape's version of draw()
        # for any Circle object -- no super() call here at all.
        print("Drawing a circle")

c = Circle()
c.draw()   # -> Drawing a circle
```

---

**8. Write a script showing "Cooperative Inheritance" where a child method calls `super().speak()` and then adds its own text.**

Unlike Question 7, this one *builds on* the parent's logic rather than replacing it — see the earlier "30 Conceptual Questions" page, Q15 and Q24, for the "Cooperative Is-A" pattern this demonstrates.

```python
class Person:
    def speak(self):
        print("Hello", end=" ")   # end=" " avoids a line break, so the
                                    # next print continues on the same line.

class Student(Person):
    def speak(self):
        # Step 1: Run the PARENT's logic first...
        super().speak()
        # Step 2: ...then add the child's own extra behaviour on top.
        print("I am a student.")

s = Student()
s.speak()   # -> Hello I am a student.
```

---

**9. Create a "Has-A" relationship (Composition) between a `CPU` class and a `Computer` class.**

See the earlier "Has-A Relationships" chapter page for the full comparison between Composition, Aggregation, and Dependency.

```python
class CPU:
    def __init__(self, brand):
        self.brand = brand

class Computer:
    def __init__(self, name, cpu_brand):
        self.name = name
        # Step 1: Composition -- the CPU object is created RIGHT HERE,
        # inside Computer's own constructor. No CPU exists independently
        # of its Computer, and it isn't shared with any other Computer.
        self.processor = CPU(cpu_brand)

pc = Computer("MyPC", "Intel")
print(f"{pc.name} has an {pc.processor.brand} CPU")   # -> MyPC has an Intel CPU
```

![Flowchart](/resources/ch-8-august-2026-scripting-question-09.png)

---

**10. Implement an abstract method using `NotImplementedError` in a class `ElectronicDevice`, and implement it in a `Phone` class.**

This is the "informal" style of abstraction — see the earlier "30 More Conceptual Questions" page, Q21, for how this compares to a formal `ABC`-based abstract method.

```python
class ElectronicDevice:
    def power_on(self):
        # Step 1: A placeholder -- this is only "abstract" by
        # convention; nothing stops ElectronicDevice itself from being
        # instantiated directly (unlike a true ABC).
        raise NotImplementedError("Must implement power_on in subclass")

class Phone(ElectronicDevice):
    def power_on(self):
        # Step 2: The REAL implementation, replacing the placeholder.
        print("Phone screen lights up")

p = Phone()
p.power_on()   # -> Phone screen lights up
```

---

**11. Write a script that uses `locals()` inside a function to show the names and values of local variables.**

See the earlier LEGB chapter page for the full explanation of `locals()` and `globals()`.

```python
def my_function():
    a = 10
    b = "hello world"
    # Step 1: locals() returns a REAL dictionary of every local
    # variable currently defined inside this function, at this exact point.
    print(locals())

my_function()
# Output: {'a': 10, 'b': 'hello world'}
```

---

**12. Demonstrate the "Diamond Problem" in multiple inheritance and show the resulting MRO.**

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

# Step 1: D inherits from BOTH B and C, and both B and C independently
# inherit from A -- this is the classic diamond shape.
print(D.__mro__)
# Output: (<class '__main__.D'>, <class '__main__.B'>,
#          <class '__main__.C'>, <class '__main__.A'>,
#          <class 'object'>)
# Notice 'A' appears only ONCE, at the very end -- Python's C3
# Linearization (see the earlier "30 More Conceptual Questions" page,
# Q10) guarantees this, even though A is reachable through two
# separate paths (via B and via C).
```

![Flowchart](/resources/ch-8-august-2026-scripting-question-12.png)

---

**13. Create a class `Account` and manually add an attribute to its instance using the `__dict__` dictionary.**

```python
class Account:
    def __init__(self, owner):
        self.owner = owner

acc = Account("Anurag")

# Step 1: Adding a new key directly into acc's __dict__ is exactly
# equivalent to writing "acc.balance = 5000" -- both insert the same
# key into the same underlying dictionary (see the earlier __dict__
# chapter page for the full explanation).
acc.__dict__['balance'] = 5000

print(f"Owner: {acc.owner}, Balance: {acc.balance}")
# -> Owner: Anurag, Balance: 5000
```

---

**14. Write a script that defines a global variable and a function, then uses `globals()` to check if they exist in the global namespace.**

```python
top_score = 100

def play(): pass

# Step 1: globals() returns a dictionary of EVERYTHING currently
# defined at module level -- checking "in globals()" is really just
# checking whether a given key exists in that dictionary.
print('top_score' in globals())   # -> True
print('play' in globals())        # -> True
```

---

**15. Create a `Manager` class that inherits from `Employee` and adds a list of subordinates. Use `super()` in the constructor.**

```python
class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def __init__(self, name, staff_list):
        # Step 1: Reuse Employee's own setup for 'name'.
        super().__init__(name)
        # Step 2: Manager-specific attribute, added on top.
        self.subordinates = staff_list

m = Manager("Gupta", ["Alice", "Bob"])
print(m.name, "manages", m.subordinates)   # -> Gupta manages ['Alice', 'Bob']
```

---

**16. Demonstrate "Replacement Is-A" where a `SilentPet` class overrides `speak()` to do absolutely nothing.**

```python
class Pet:
    def speak(self):
        print("Some sound")

class SilentPet(Pet):
    def speak(self):
        # Step 1: 'pass' here means this method deliberately does
        # NOTHING -- it still fully overrides Pet's speak(), it just
        # replaces it with silence rather than a different message.
        pass

s = SilentPet()
s.speak()   # Nothing is printed at all.
```

---

**17. Use the `@property` decorator to create a "getter" for a `Circle` class that calculates area based on radius.**

See the earlier "`@property`" chapter page for the full explanation of how properties work internally.

```python
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        # Step 1: This is a CALCULATED attribute -- there's no
        # self._area stored anywhere; the value is computed fresh,
        # from self._radius, every single time c.area is read.
        return math.pi * (self._radius ** 2)

c = Circle(5)
print(f"Area: {c.area:.2f}")   # -> Area: 78.54
```

---

**18. Implement a "Custom Container" using `__getitem__` to allow square bracket access to a `PetBox` class.**

See the earlier "30 More Conceptual Questions" page, Q24–25, for the broader idea of custom containers.

```python
class PetBox:
    def __init__(self, pets):
        self.pets = pets

    def __getitem__(self, index):
        # Step 1: This is what makes "box[index]" work at all -- it
        # simply forwards the request to the real underlying list, self.pets.
        return self.pets[index]

box = PetBox(["Dog", "Cat", "Hamster"])
print(box[1])   # -> Cat
```

---

**19. Create a script that shows "Hierarchical Inheritance" with one parent `Weapon` and two children `Sword` and `Bow`.**

```python
class Weapon:
    def attack(self): print("Attacking!")

class Sword(Weapon): pass
class Bow(Weapon): pass

s = Sword()
b = Bow()
s.attack()   # -> Attacking!
b.attack()   # -> Attacking!
# Both children reuse the SAME parent method, completely unchanged --
# this is hierarchical inheritance: one parent, multiple independent children.
```

![Flowchart](/resources/ch-8-august-2026-scripting-question-19.png)


---

**20. Use `__slots__` to restrict a `Point` class to only have `x` and `y` attributes, preventing the creation of `__dict__`.**

See the earlier "`__slots__`" chapter page for the full memory-optimization project this connects to.

```python
class Point:
    # Step 1: Declaring __slots__ removes __dict__ entirely for
    # Point objects -- only 'x' and 'y' are allowed to ever exist on
    # any Point instance.
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(10, 20)
print(p.x, p.y)   # -> 10 20

# p.z = 30   # Uncommenting this raises: AttributeError: 'Point'
             # object has no attribute 'z' -- there's no __dict__ left
             # to add an unplanned attribute to.
```

---

## Quick recap

- These twenty scripts turn the conceptual definitions from the two earlier review pages into actual, runnable code — inheritance patterns (Q1, 2, 7, 8, 16, 19), MRO and multiple inheritance (Q3, 6, 12), constructors and `super()` (Q4, 15), namespaces (Q5, 11, 13, 14), and the more specialized tools covered later in the chapter — composition (Q9), abstraction (Q10), properties (Q17), custom containers (Q18), and `__slots__` (Q20).
- If any single script above still feels unclear, every question links back to the specific earlier chapter page that develops that exact idea in full depth, with additional diagrams and explanation.
- A good way to test your own understanding: for each script, try predicting the output *before* looking at the comment that shows it — and for the diamond-problem script (Q12) and the multiple-inheritance script (Q6), try changing the order of the parent classes and predicting how the `__mro__` output would change, exactly as the earlier "Diamond Problem" chapter page's `Dog1`/`Dog2` comparison demonstrated.




