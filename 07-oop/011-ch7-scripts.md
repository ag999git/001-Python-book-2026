
# Chapter 7 — OOP Scripting Exercises

## What this page covers

This page is a set of hands-on coding exercises for Chapter 7 (Object-Oriented Programming). Where the previous page ("OOP Conceptual Questions and Answers") tested *definitions* — what a class is, what encapsulation means — this page tests whether you can actually **write** the code: constructors, methods, class variables, private attributes, and a few small real-world-style classes like `Car`, `Bank`, and `Temperature`.

**A quick note before you start:** if any of the terms below (constructor, class variable, private attribute, static method, operator overloading) are unfamiliar, they're all covered in more depth on the previous page, "OOP Conceptual Questions and Answers," which this page assumes you've read.

---

**Q1. Create a class `Car` with a constructor that takes `brand` and `model`. Instantiate two different cars.**

**Approach:** A constructor is just the `__init__` method — it runs automatically when a new object is created, and its job here is to store `brand` and `model` onto the new object. "Instantiate" simply means "create an object from the class."

```python
class Car:
    def __init__(self, brand, model):
        # Step 1: Save the two arguments as attributes on THIS object (self).
        self.brand = brand
        self.model = model

# Step 2: Create two separate Car objects, each with its own brand and model.
car1 = Car("Tata", "Nexon")
car2 = Car("Mahindra", "XUV700")

# Step 3: Confirm each object stored its own data correctly.
print(f"Car 1: {car1.brand} {car1.model}")
print(f"Car 2: {car2.brand} {car2.model}")
```

---

**Q2. Add a class variable `wheels = 4` to the `Car` class and print it using the Class name.**

**Approach:** A class variable is written directly inside the class body (not inside `__init__`), and belongs to the class itself rather than to any one object — so it can be read via the class name, with no object required at all.

```python
class Car:
    # Step 1: A class variable, shared by every Car object (and even
    # accessible with no Car object created at all).
    wheels = 4

# Step 2: Access it directly through the class name.
print(Car.wheels)   # -> 4
```

---

**Q3. Write a method `start_engine` that prints "The [brand] [model] engine is running."**

**Approach:** This is a regular instance method — it needs `self` so it can read the specific object's own `brand` and `model` when building its message.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        # Step 1: Use self.brand and self.model -- the values belonging
        # to whichever Car object called this method.
        print(f"The {self.brand} {self.model} engine is running.")

# Step 2: Create a Car and call the method on it.
my_car = Car("Toyota", "Camry")
my_car.start_engine()   # -> The Toyota Camry engine is running.
```

---

**Q4. Create a `Student` class where the `age` has a default value of 18.**

**Approach:** Giving a constructor parameter a default value (`age=18`) means callers can leave it out entirely, and Python will use 18 automatically — but they can also still override it by passing their own value.

```python
class Student:
    def __init__(self, name, age=18):
        # Step 1: If the caller doesn't supply 'age', Python uses 18
        # automatically. If they do supply it, their value is used instead.
        self.name = name
        self.age = age

s1 = Student("Anil")          # age not given -> uses the default, 18
s2 = Student("Sunita", 20)    # age given -> overrides the default with 20

print(f"{s1.name} is {s1.age}")   # -> Anil is 18
print(f"{s2.name} is {s2.age}")   # -> Sunita is 20
```

---

**Q5. Implement a `Bank` class with a private attribute `__balance`. Create a method to check the balance.**

**Approach:** Prefixing an attribute with a double underscore (`__balance`) triggers Python's name mangling, making it awkward to access directly from outside the class (see the previous page's Q4/Q19 for the full explanation). Instead, we provide a controlled method, `get_balance`, as the intended way to read it.

```python
class Bank:
    def __init__(self, amount):
        # Step 1: Store the balance as a "private" attribute. This
        # signals that outside code shouldn't reach in and change it
        # directly -- it should only be read through the method below.
        self.__balance = amount

    def get_balance(self):
        # Step 2: Provide a controlled, read-only way to check the balance.
        return f"Current Balance: {self.__balance}"

account = Bank(5000)
print(account.get_balance())   # -> Current Balance: 5000
```

---

**Q6. Write a script to count how many `User` objects have been created using a class variable.**

**Approach:** Because a class variable (`count`) is shared across every object of the class, incrementing it inside `__init__` — which runs once per object created — gives us a running total of how many objects exist, no matter how many are created.

```python
class User:
    # Step 1: A class variable shared by ALL User objects, used here as
    # a running counter. It starts at 0 before any User is created.
    count = 0

    def __init__(self):
        # Step 2: Every time a new User is created, __init__ runs once,
        # and increases the SHARED class variable by 1.
        # (Using User.count, not self.count, updates the shared value
        # rather than creating a separate instance variable.)
        User.count += 1

u1 = User()
u2 = User()
print(f"Total Users: {User.count}")   # -> Total Users: 2
```

---

**Q7. Create a method `update_email` that takes a new email and updates the instance attribute.**

**Approach:** This is a straightforward "setter"-style method: it takes a new value as a parameter and overwrites the existing instance attribute with it.

```python
class User:
    def __init__(self, email):
        self.email = email

    def update_email(self, new_email):
        # Step 1: Overwrite the old email with the new one, on this object.
        self.email = new_email

user = User("test@old.com")
print(f"Before: {user.email}")   # -> Before: test@old.com

user.update_email("test@new.com")
print(f"After:  {user.email}")   # -> After:  test@new.com
```

---

**Q8. Script an example of Operator Overloading using `+` for two strings.**

**Approach:** "Operator overloading" means the same operator (here, `+`) does something different depending on the *type* of the values it's used on. Python's built-in string type already overloads `+` to mean "join these two strings together," which is different from what `+` means for numbers (addition). This exercise doesn't require writing any new code to make overloading happen — it's demonstrating overloading that Python's `str` type already provides.

```python
x, y = "Python", "999"

# Step 1: Because x and y are both strings, Python's built-in '+'
# operator is "overloaded" to mean concatenation (joining text together)
# here, rather than mathematical addition.
result = x + y

print(result)   # -> Python999
```

*(For comparison: `5 + 3` uses the exact same `+` symbol, but because both values are numbers, Python runs numeric addition instead — that's operator overloading in a nutshell: one operator, different behaviour, depending on the type of data involved.)*

---

**Q9. Create a static method `info()` that prints "This is a utility class for Math."**

**Approach:** A static method doesn't need access to `self` or to any particular object's data — it's really just a regular function that's logically grouped inside the class for organisation. The `@staticmethod` decorator tells Python not to automatically pass an object in as the first argument.

```python
class MyMath:
    @staticmethod
    def info():
        # Step 1: No 'self' parameter here -- this method doesn't need
        # any specific MyMath object to do its job.
        print("This is a utility class for Math.")

# Step 2: Called directly on the class -- no object needed at all.
MyMath.info()
```

---

**Q10. Use the `__dict__` attribute to print all attributes of a `Pet` object.**

**Approach:** Every regular Python object automatically keeps its instance attributes in a built-in dictionary, accessible as `object.__dict__`. This is a handy way to inspect everything currently stored on an object, without needing to know the attribute names in advance. (The original exercise assumes a `Pet` class already exists from earlier in the book — it's included below for completeness.)

```python
class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

p = Pet("Tiger", "Dog")

# Step 1: __dict__ returns a regular Python dictionary of every
# instance attribute currently stored on this object, as {name: value} pairs.
print(p.__dict__)   # -> {'name': 'Tiger', 'breed': 'Dog'}
```

---

**Q11. Write a class `Product` with `price` and a method `apply_discount(percent)` that changes the price.**

**Approach:** The method needs to calculate the discount amount (a percentage of the current price) and subtract it from `self.price`, permanently updating the object's stored price.

```python
class Product:
    def __init__(self, price):
        self.price = price

    def apply_discount(self, percent):
        # Step 1: Work out what the discount is worth in actual currency
        # (percent / 100 turns e.g. 10 into 0.10).
        # Step 2: Subtract that amount from the current price, updating
        # self.price permanently for this object.
        self.price -= self.price * (percent / 100)

p = Product(100)
p.apply_discount(10)
print(p.price)   # -> 90.0
```

---

**Q12. Demonstrate what happens when you redefine a function name in Python.**

**Approach:** This connects directly to the "no true function overloading" idea from the previous page's Q3. Defining a second function with the same name doesn't create two versions — it simply replaces the first one, which is then completely forgotten.

```python
def check():
    print("First")

def check():
    # Step 1: This second definition OVERWRITES the first one above.
    # Python doesn't keep both -- only the most recent 'check' survives.
    print("Second")

check()   # -> Second  (the "First" version no longer exists)
```

---

**Q13. Create a class `Circle` that takes `radius` and has a method `area`. (Use 3.14).**

**Approach:** Standard constructor-plus-method pattern: store `radius` in `__init__`, then use the classic area formula (π × r²) inside the `area` method, using `self.radius`.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Step 1: Standard area formula: pi * radius squared.
        # ** is Python's exponent operator, so radius ** 2 means radius squared.
        return 3.14 * (self.radius ** 2)

c = Circle(5)
print(c.area())   # -> 78.5
```

---

**Q14. Write a script where an object attribute is initialized inside `__init__` but not passed as a parameter.**

**Approach:** Not every attribute needs to come from the constructor's parameters — `__init__` can also set up attributes with a fixed starting value on its own, useful for things like counters or scores that should always start the same way for every new object.

```python
class Game:
    def __init__(self, player_name):
        self.player_name = player_name
        # Step 1: 'score' is never passed in as a parameter -- __init__
        # simply sets a sensible starting value for every new Game object.
        self.score = 0

g = Game("Arjun")
print(g.score)   # -> 0
```

---

**Q15. Create a class `Temperature` and use a setter method to ensure the temperature cannot be below Absolute Zero (-273.15°C).**

**Approach:** This is a validation pattern: instead of letting `__init__` set `self.celsius` directly, it routes the incoming value through a method (`set_temp`) that checks it first, so an invalid value (below Absolute Zero, the coldest temperature physically possible) is corrected before it's ever stored.

```python
class Temperature:
    def __init__(self, celsius):
        # Step 1: Route the starting value through set_temp() too,
        # rather than storing it directly -- so even the FIRST value
        # given gets validated, not just later updates.
        self.set_temp(celsius)

    def set_temp(self, celsius):
        # Step 2: Reject anything below Absolute Zero by silently
        # clamping it to the lowest possible valid value instead.
        if celsius < -273.15:
            self.celsius = -273.15
        else:
            self.celsius = celsius

t = Temperature(-500)
print(t.celsius)   # -> -273.15  (clamped, since -500 is impossible)
```

---

## Quick recap

| Pattern used in this chapter | Appears in |
|---|---|
| Constructor storing parameters as attributes | Q1, Q3, Q4, Q7, Q11, Q13 |
| Class variable (shared across all objects) | Q2, Q6 |
| Private attribute + controlled access method | Q5 |
| Default parameter values | Q4 |
| `__dict__` for inspecting an object's attributes | Q10 |
| Static method (`@staticmethod`) | Q9 |
| Setter method with built-in validation | Q15 |
| Operator behaviour depending on data type | Q8 |
| Redefining a function name (no true overloading) | Q12 |

If any single exercise above still feels unclear, it's worth re-reading the matching concept on the previous page, "OOP Conceptual Questions and Answers" — every script here is a direct, hands-on application of one of those ideas.



