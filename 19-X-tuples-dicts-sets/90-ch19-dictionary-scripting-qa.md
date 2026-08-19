



**Q1. Create dict of 3 fruits→colours. Print colour of "banana" (safe, no error). Also try missing key "grape", default "Unknown".**
```python
# Step 1: Create a dictionary mapping fruit names to their colours
fruit_colors = {"apple": "red", "banana": "yellow", "mango": "orange"}
 
# Step 2: Safely access the value for "banana" using get()
# get() returns None (never a KeyError) if the key is missing
print("Banana:", fruit_colors.get("banana"))
 
# Step 3: Access a key that does NOT exist ("grape")
# supply a default as the second argument to get() so nothing crashes
print("Grape:", fruit_colors.get("grape", "Unknown"))
```

Explanation:
- Pattern used: safe access with `get()` instead of `fruit_colors["grape"]`. 
- Direct indexing (`fruit_colors["grape"]`) would raise `KeyError` since `"grape"` is not a `key`. 
- `get(key, default)` (Step 3) sidesteps that entirely by returning a fallback value, which is why it is the recommended way to read a dictionary whenever a key's presence isn't guaranteed.

**Q2. Build dict from a list of `(subject, marks)` tuples using `dict()`. Separately, build a student dict `(roll, name, age)` using keyword arguments.**

```python
# Step 1: A list of (subject, marks) tuples -- the raw data source
subject_marks = [("Maths", 90), ("Science", 85), ("English", 88)]
 
# Step 2: Convert the list of tuples directly into a dictionary
# dict() accepts any iterable of 2-element pairs
marks_dict = dict(subject_marks)
print("From tuples:", marks_dict)
 
# Step 3: Build a dictionary using keyword arguments instead
# each keyword becomes a string key automatically
student = dict(roll=101, name="Ann", age=20)
print("From keywords:", student)
```

Explanation:
- Pattern used: two variants of the `dict()` constructor. 
- Step 2 shows `dict()` consuming a sequence of pairs (useful when data already exists in list/tuple form, e.g. from a file or API). 
- Step 3 shows `dict()` consuming keyword arguments (useful for quick, hand-typed dictionaries); note that keyword names automatically become str keys.
- 
**Q3. Initialise a dict of 4 days ("Mon".."Thu") all marked "Absent", in one line. No curly-brace literal, no loop.**

```python
# Step 1: List of keys that all need the same starting value
days = ["Mon", "Tue", "Wed", "Thu"]
 
# Step 2: dict.fromkeys(keys, default) assigns the SAME value
# to every key in one call -- no loop needed
attendance = dict.fromkeys(days, "Absent")
print(attendance)
# Output: {'Mon': 'Absent', 'Tue': 'Absent', 'Wed': 'Absent', 'Thu': 'Absent'}
```

Explanation:
- Pattern used: bulk initialisation with `dict.fromkeys()`. 
- This is the idiomatic way to give many keys one shared default value -- writing `{"Mon": "Absent", "Tue": "Absent", ...}` by hand, or looping with `attendance[day] = "Absent"`, would work too but is more typing and more error-prone for larger key lists.

**Q4. Given dict of item→price, print each as `"item : ₹price"` using the traversal method that gives both key and value directly.**

```python
# Step 1: Sample dictionary of item -> price
cart = {"Pen": 10, "Notebook": 40, "Eraser": 5}
 
# Step 2: Traverse using .items(), which unpacks each entry
# directly into (item, price) -- no separate lookup needed
for item, price in cart.items():
    print(f"{item} : Rs.{price}")
```

Explanation:
- Pattern used: .items() traversal. 
- This is preferred over `for item in cart: print(item, cart[item])` because it retrieves the key and value together in a single step, without a second dictionary lookup for every entry -- the Pythonic and more efficient choice whenever both pieces are needed.

**Q5. Given dict of subject→marks, find total and average marks. Use the traversal method that gives only values.**

```python
# Step 1: Sample dictionary of subject -> marks
marks = {"Maths": 90, "Science": 78, "English": 85, "History": 67}
 
# Step 2: .values() gives only the numbers, ignoring the keys,
# since the subject names are not needed for this calculation
total = sum(marks.values())
 
# Step 3: Average = total marks / number of subjects
average = total / len(marks)
 
print("Total:", total)
print("Average:", average)
```

Explanation:
- Pattern used: `.values()` traversal combined with `sum()`. 
- Since the calculation only needs the numbers, not which subject each number belongs to, iterating over `.values()` (rather than `.items()` or the keys) is the leaner choice. 
- `len(marks)` (Step 3) reuses the dictionary's own pair count instead of a separately tracked counter.

**Q6. Given dict of student→marks, remove all students scoring below 40. Must not raise `RuntimeError`.**
```python
# Step 1: Sample dictionary of student -> marks
marks = {"Ann": 55, "Bob": 30, "Cid": 38, "Dev": 72}
 
# Step 2: DO NOT loop over marks directly while deleting --
# that raises: RuntimeError: dictionary changed size during iteration
# Instead, loop over a SNAPSHOT of the keys using list()
for student in list(marks.keys()):
    if marks[student] < 40:
        del marks[student]
 
print(marks)
# Output: {'Ann': 55, 'Dev': 72}
```

Explanation:
- Pattern used: safe deletion via a key snapshot. 
- `list(marks.keys())` (Step 2) is evaluated once, before the loop starts, producing an independent list that is unaffected by later del calls on the live dictionary -- this is the standard technique for removing entries while "iterating" without triggering `RuntimeError`.

**Q7. Using one dict comprehension: map numbers 1–10 to their cubes, but keep only even numbers.**

```python
# Step 1 & 2 combined in a single dictionary comprehension:
# key_expression = n, value_expression = n ** 3,
# iterable = range(1, 11), condition = n % 2 == 0
even_cubes = {n: n ** 3 for n in range(1, 11) if n % 2 == 0}
 
print(even_cubes)
# Output: {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000}
```

Explanation:
- Pattern used: dictionary comprehension with a filter. 
- The if `n % 2 == 0` clause is evaluated for every n before it is added to the result -- odd numbers are simply skipped, so no separate if/else block or manual loop with `.append()`-style logic is required.

**Q8. Given dict of name→roll_no, build a new dict swapping keys and values. One comprehension line.**

```python
# Step 1: Original dictionary, name -> roll number
name_to_roll = {"Ann": 1, "Bob": 2, "Cid": 3}
 
# Step 2: Swap using .items() to get (name, roll) pairs,
# then flip the order to roll: name in the comprehension
roll_to_name = {roll: name for name, roll in name_to_roll.items()}
 
print(roll_to_name)
# Output: {1: 'Ann', 2: 'Bob', 3: 'Cid'}
```

Explanation:
- Pattern used: reversing a dictionary via comprehension. 
- `.items()` supplies both parts of each entry; 
- the comprehension simply writes the value first and the key second `(roll: name)` instead of `name: roll`. 
- This only works safely if the original values (here, roll numbers) are themselves unique and hashable -- otherwise some entries would silently overwrite each other in the new dictionary.

**Q9. Write is_valid_key(k) returning `True/False` if `k` can be used as a dict key. Test on `5`, `"hi", (1,2), [1,2], {1:2}`.**

```python
def is_valid_key(k):
    # Step 1: A value is usable as a dictionary key only if it is
    # hashable -- try hashing it and see if Python objects
    try:
        hash(k)           # Step 2: attempt to compute a hash value
        return True        # Step 3: success -> hashable -> valid key
    except TypeError:
        return False       # Step 4: TypeError -> unhashable -> invalid key
 
# Step 5: Test with a mix of hashable and unhashable values
for value in [5, "hi", (1, 2), [1, 2], {1: 2}]:
    print(value, "->", is_valid_key(value))
```

Explanation:
- Pattern used: `try/except TypeError` around `hash()`, 
- since this is exactly the error Python raises for unhashable (mutable) objects. 5, "hi", and (1, 2) are hashable (int, str, and a tuple of hashable items) and return True; [1, 2] and {1: 2} are mutable and return False, matching the chapter's hashability rules.

**Q10. Given dict of employee→salary, check if "Ravi" and "Sunita" exist as keys. Print message for each.**

```python
# Step 1: Sample dictionary of employee -> salary
salary = {"Ravi": 45000, "Meena": 52000}
 
# Step 2: "in" checks only the KEYS of the dictionary
if "Ravi" in salary:
    print("Ravi is on record.")
else:
    print("Ravi not found.")
 
# Step 3: "not in" is the negated membership test
if "Sunita" not in salary:
    print("Sunita not found.")
else:
    print("Sunita is on record.")
```

Explanation:
- Pattern used: membership testing with `in` / `not in`. 
- Both operators check only against the dictionary's keys, never its values -- so this technique cannot be used to test whether some salary amount exists in the dictionary, only whether an employee name does.
- 
Q11. Two dicts: Jan sales and Feb sales by product. Merge Feb into Jan with `update()` (overlaps must update, not add duplicates).

```python
# Step 1: Sample monthly sales dictionaries
jan_sales = {"Pen": 100, "Notebook": 50}
feb_sales = {"Notebook": 70, "Eraser": 30}
 
# Step 2: update() merges feb_sales into jan_sales IN PLACE
# -- "Notebook" already exists, so its value is overwritten (70),
# not added as a second entry; "Eraser" is new, so it is inserted
jan_sales.update(feb_sales)
 
print(jan_sales)
# Output: {'Pen': 100, 'Notebook': 70, 'Eraser': 30}
```

Explanation:
- Pattern used: dictionary merging with `update()`. 
- `update()` never creates duplicate keys -- for a key that exists in both dictionaries 
- ("Notebook"), the incoming value simply replaces the old one. 
- `update()` modifies `jan_sales` directly and returns `None`, so the merged result must be read from `jan_sales` itself, not from the return value of the call.

**Q12. Given dict of room bookings, `pop()` `"Room101"` and print it. Then try `pop()` on missing `"Room999"` without crashing.**

```python
# Step 1: Sample dictionary of room -> guest name
bookings = {"Room101": "Mr. Rao", "Room102": "Ms. Iyer"}
 
# Step 2: pop() removes the key AND returns its value
removed_guest = bookings.pop("Room101")
print("Removed:", removed_guest)
print("Remaining:", bookings)
 
# Step 3: pop() on a missing key with NO default raises KeyError.
# Supplying a second argument avoids the crash entirely
result = bookings.pop("Room999", "No such booking")
print(result)
```

Explanation:
- Pattern used: `pop(key)`for remove-and-retrieve, and `pop(key, default) `for safe removal. 
- Step 2's single-argument form assumes the key exists (it does, so it returns the guest name and deletes the entry). 
- Step 3's two-argument form guards against a missing key by returning the supplied default instead of raising `KeyError`.

**Q13. Empty dict category→list. Given list of `(category, item)` tuples, group items under categories using `setdefault()` — no manual if key in dict check.**

```python
# Step 1: Raw data -- (category, item) pairs
records = [("Fruit", "Apple"), ("Veg", "Carrot"),
           ("Fruit", "Mango"), ("Veg", "Peas")]
 
# Step 2: Start with an empty grouping dictionary
grouped = {}
 
# Step 3: For each record, setdefault() either returns the
# existing list for that category, or creates a new empty list
# and returns THAT -- either way we get a list back to append to
for category, item in records:
    grouped.setdefault(category, []).append(item)
 
print(grouped)
# Output: {'Fruit': ['Apple', 'Mango'], 'Veg': ['Carrot', 'Peas']}
```

Explanation:
- Pattern used: grouping with setdefault(). 
- Step 3 replaces the longer beginner pattern of `if category not in grouped: grouped[category] = []` followed by `grouped[category].append(item) -- setdefault(category, [])` does both jobs (insert-if-absent, then return) in one call, which is then immediately followed by `.append(item)`.

**Q14. Given dict of settings, `copy()` it, change one value in the copy -- prove original unaffected. Add a nested list value; mutate it via the copy -- show original is affected (shallow copy).**

```python
# Step 1: Original dictionary, including one nested mutable value
settings = {"theme": "light", "recent_scores": [10, 20]}
 
# Step 2: Make a shallow copy
settings_copy = settings.copy()
 
# Step 3: Changing a TOP-LEVEL value in the copy does NOT affect original
settings_copy["theme"] = "dark"
print("Original theme:", settings["theme"])        # still "light"
print("Copy theme:", settings_copy["theme"])        # "dark"
 
# Step 4: But the nested list is SHARED between original and copy --
# mutating it through the copy also changes the original
settings_copy["recent_scores"].append(30)
print("Original scores:", settings["recent_scores"])   # [10, 20, 30] !
print("Copy scores:", settings_copy["recent_scores"])
```

Explanation:
- Pattern used: demonstrating the shallow-copy limitation of `copy()`. 
- Step 3 (reassigning `settings_copy["theme"]`) only affects the copy, because it replaces what the copy's "theme" key points to. 
- Step 4 (`.append(30)`) does not reassign anything -- it mutates the same list object that both `settings["recent_scores"]` and `settings_copy["recent_scores"]` point to, so the change is visible through either dictionary.
- 
**Q15. Store `keys_view = d.keys()` before adding a new key to `d`. Print `keys_view` before and after, to show it updates live.**

```python
# Step 1: Sample dictionary and a keys view taken from it
d = {"a": 1, "b": 2}
keys_view = d.keys()
 
# Step 2: Print the view BEFORE any change
print("Before:", keys_view)   # dict_keys(['a', 'b'])
 
# Step 3: Add a new key to the dictionary
d["c"] = 3
 
# Step 4: Print the SAME view object again -- no re-fetching --
# it reflects the dictionary's current state automatically
print("After:", keys_view)    # dict_keys(['a', 'b', 'c'])
```

Explanation:
- Pattern used: demonstrating that view objects are dynamic (live), not static copies. 
- `keys_view` in Step 4 is the exact same object created in Step 1 -- it was never reassigned or refreshed -- yet it shows the newly added `"c" `because a view is a window onto the dictionary's current contents, unlike `list(d.keys())`, which would have frozen at Step 1.
- 
**Q16. Count frequency of each character in "mississippi" using a dictionary, no library. Use `get()` with default `0`.**

```python
# Step 1: The string whose characters need counting
text = "mississippi"
 
# Step 2: Start with an empty frequency dictionary
freq = {}
 
# Step 3: For each character, get its current count (0 if new),
# then increment it by 1 and store it back
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
 
print(freq)
# Output: {'m': 1, 'i': 4, 's': 4, 'p': 2}
```

Explanation:
- Pattern used: counting with `get(key, 0)`. 
- Step 3's `freq.get(ch, 0)` avoids a manual if ch not in `freq: freq[ch] = 0` check before incrementing -- for a character seen for the first time it safely returns 0, and for one seen before it returns the running count, 
- so `+ 1` always works in a single line.

**Q17. Two separate lists — `names`, `marks` (same order). Combine into one dictionary using `zip()` and `dict()`.**

```python
# Step 1: Two parallel lists
names = ["Ann", "Bob", "Cid"]
marks = [90, 85, 78]
 
# Step 2: zip() pairs up corresponding elements: ('Ann', 90), ('Bob', 85)...
# dict() then converts that sequence of pairs into a dictionary
name_marks = dict(zip(names, marks))
 
print(name_marks)
# Output: {'Ann': 90, 'Bob': 85, 'Cid': 78}
```

Explanation:
- Pattern used: `zip()` + `dict()` combination. 
- `zip(names, marks)` (Step 2) walks both lists in lock-step, producing one tuple per position; wrapping that in dict() treats each tuple as a (key, value) pair -- the same underlying mechanism used earlier for building a dictionary from a list of tuples, just with the pairs generated on the fly instead of typed out.

**Q18. Two dicts with same key-value pairs, built in different insertion order. Print `==` and `is` results. Also print `id()` of both.**

```python
# Step 1: Two dictionaries with identical content, different order
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
 
# Step 2: == compares CONTENT only -- order of insertion is ignored
print("== result:", d1 == d2)      # True
 
# Step 3: is compares IDENTITY -- are they the same object in memory?
print("is result:", d1 is d2)      # False
 
# Step 4: id() confirms they are two separate objects
print("id(d1):", id(d1))
print("id(d2):", id(d2))
```

Explanation:
- Pattern used: contrasting `==` (equality) with `is` (identity). 
- Step 2 returns `True` because dictionary equality only checks that both dictionaries have the same keys mapped to the same values -- insertion order plays no role. 
- Step 3 returns `False`, 
- and Step 4's differing `id()` values confirm why: `d1` and `d2` are two distinct dictionary objects in memory that merely happen to hold equal content.

**Q19. Given a dict: print (a) pair `count` with `len()`, (b) whether `"score"` is a key with `in`, (c) the object's type with `type()`.**

```python
# Step 1: Sample dictionary
student = {"name": "Ann", "age": 20, "grade": "A"}
 
# Step 2 (a): len() counts key-value PAIRS, not keys and values separately
print("Pair count:", len(student))           # 3
 
# Step 3 (b): in checks only the keys
print("Has score?:", "score" in student)     # False
 
# Step 4 (c): type() confirms the object is a dict
print("Type:", type(student))                # <class 'dict'>
```

Explanation:
- Pattern used: the three core dictionary-inspection functions. 
- `len()` (Step 2), in (Step 3), and `type()` (Step 4) are all built-in functions rather than dictionary methods -- they work the same way on other Python container types too, which is why they're introduced together as "useful dictionary functions" rather than "dictionary methods".

**Q20. Given dict of cart items, make a `copy()`, `clear()` the copy to simulate emptying the cart. Prove original cart is untouched.**

```python
# Step 1: Original shopping cart
cart = {"Pen": 2, "Notebook": 1}
 
# Step 2: Make an independent copy to simulate a "checkout" cart
checkout_cart = cart.copy()
 
# Step 3: clear() empties the COPY completely, in place
checkout_cart.clear()
 
# Step 4: The original cart is unaffected, since copy() made it
# an independent dictionary at the TOP level
print("Original cart:", cart)               # {'Pen': 2, 'Notebook': 1}
print("Checkout cart:", checkout_cart)      # {}
```

Explanation:
- Pattern used: `copy()` followed by `clear()` to safely reset one dictionary without disturbing another. 
- Because `checkout_cart` was created with `.copy()` (Step 2), it is a fully separate top-level dictionary object; 
- calling `clear()` (Step 3) empties only that object, leaving the original cart dictionary from Step 1 completely intact.
