



**Q1. What makes a dictionary a "mapping" rather than a "sequence," and how does this affect the way you access its elements?**

- A dictionary is a container that groups multiple values together, but unlike a list, string, or tuple, it is not a sequence. 
- A sequence stores items in a fixed, numbered order and lets you retrieve them using integer indices (e.g. `my_list[0]`). 
- A dictionary instead stores data as key-value pairs, and you retrieve a value using its associated key (e.g. `my_dict['name']`), not a positional index. 
- So while every sequence is also a container, not every container is a sequence -- dictionaries fall into the "container but not sequence" category.
- Practically, this means `my_dict[0]` does not fetch the "first item" unless the integer 0 happens to be an explicitly defined key; if it is not, Python raises a `KeyError`, not an IndexError. 
- This is one of the most common early misconceptions for students moving from lists to dictionaries.

**Q2. Contrast dictionaries and lists on: 
(a) access method, 
(b) lookup time, 
(c) when you would prefer one over the other.**

- A list is a sequence: elements are accessed via numerical position/index (`list[0]`), and finding a value by content requires an `O(n)` linear search -- Python checks items one at a time. 
- A dictionary is a mapping: elements are accessed via a unique key (`dict['key']`), and this lookup is optimized to be `O(1)` on average, using an internal hash table, regardless of how many items the dictionary holds.

In terms of when to use which: 
- use a list when the position/order of items is meaningful and you will process them sequentially (e.g. a list of exam scores in the order recorded); 
- use a dictionary when you need to look up a value by some meaningful label rather than by position (e.g. looking up a student's marks by their name). 
- As a rule of thumb: if you find yourself using a list's index purely as an identifier (like `scores[0]` meaning "Alice's score"), that is usually a sign a dictionary would be a better fit.

**Q3. Dictionaries are mutable, yet their keys must be immutable. Explain this apparent contradiction, and list which built-in types can/cannot be used as keys.**

- There is no real contradiction -- mutability applies at two different levels. The dictionary container itself is mutable: you can add, remove, or update key-value pairs after creation without needing to build a new dictionary. 
- However, each individual key inside it must be immutable (and, more precisely, hashable). This is because Python locates entries internally using each key's hash value, computed once when the key is inserted. If a key's value could change afterward, its hash would also change, and Python would no longer be able to find it in its internal hash table -- silently breaking lookups.
- Values, by contrast, have no such restriction, since Python never needs to hash a value; values can be of any type, mutable or immutable, simple or deeply nested. 
- Allowed key types include int, float, str, and tuple (conditionally -- see hashability). Types that cannot be used as keys include list, dict, and set, because all three are mutable and therefore unhashable.

**Q4. What is a "hashable" object? State the three formal criteria an object must satisfy to be considered hashable.**

A hashable object is one that has a fixed integer "hash value" that never changes throughout its lifetime, computable using Python's built-in `hash()` function. Formally, an object must satisfy three criteria: 
- (1) Fixed Hash Value -- its hash value must remain the same every time hash() is called on it during a single program run; 
- (2) Equality Support -- it must support comparison with other objects using `==`; and 
- (3) Consistency between equality and hashing -- if two objects are equal (`a == b`), their hash values must also be equal (`hash(a) == hash(b)`).

- This last rule is crucial: it is what allows Python's dictionaries to correctly recognize "the same key" even if it is a different object in memory, as long as it is equal in value. 
- Only hashable objects are permitted as dictionary keys, since Python's internal implementation relies on the hash value to place and retrieve keys efficiently in its hash table.

**Q5. What happens when you call `hash()` on a mutable object like a list? Why does Python enforce this restriction?**

Calling `hash()` on a mutable object such as a list, set, or dict raises a `TypeError`, e.g. `TypeError: unhashable type: 'list'`. 

The same error occurs if you try to use such an object directly as a dictionary key, since dictionary keys are hashed internally the moment they are inserted.

Python enforces this restriction because mutable objects can change their contents after creation -- a list's elements can be appended, removed, or reassigned at any time. If such an object were allowed as a key, its hash value could change after insertion, and Python's internal hash table would then be unable to relocate it, effectively "losing" the entry or causing lookup inconsistencies. 

By disallowing mutable types as keys altogether, Python guarantees that every key's hash value -- and therefore its position inside the dictionary's internal structure -- remains stable for as long as it exists in the dictionary.

**Q6. Why does `hash("apple")` return the same value every time within one Python program run, but a different value if you restart Python or run it on another machine?**

- Within a single running Python process, `hash()` is deterministic -- calling `hash("apple")` multiple times in the same script always returns the identical integer, because the hashing algorithm and its internal seed value do not change mid-execution. 
- However, each time you start a new Python process, Python applies a security feature called hash seed randomization: it randomly picks a new starting "seed" for its string-hashing algorithm at interpreter startup. As a result, hash("apple") computed in one run of a script can differ from the value computed in the next run, or on a different machine.
- This is a deliberate security measure -- it prevents attackers from being able to predict hash values in advance and craft inputs designed to cause many keys to collide in the same hash bucket, which could otherwise be exploited to slow dictionary/set operations from `O(1)` to `O(n)` as part of a denial-of-service (DoS) attack.

**Q7. Tuples are described as "conditionally hashable." Explain what this means, with one example each of a hashable and an unhashable tuple.**

- Unlike `int`, `float`, or `str`, which are always hashable, a tuple is hashable if and only if every element it contains is itself hashable. 
- This is because Python computes a tuple's hash value by combining the hash values of its individual elements -- if even one element is unhashable (i.e. mutable), the tuple as a whole cannot be hashed either.
- For example, `(1, 2, "hello")` is hashable, since integers and strings are themselves hashable, so this tuple could safely be used as a dictionary key. 
- In contrast, `(1, 2, [3, 4])` is unhashable, because it contains a list -- attempting `hash((1, 2, [3, 4]))` or using it as a dictionary key raises `TypeError: unhashable type: 'list'.` 
- This distinguishes tuples from the other three "always hashable" simple types, and is a favourite trick question, since students often assume `"tuple = hashable"` unconditionally.

**Q8. Name and briefly describe the three ways to create a dictionary in Python. Give one example use-case for each.**

Python offers three main ways to build a dictionary.
- (1) Dictionary literals using curly braces {} -- the most common and readable approach, where you write out key-value pairs directly, e.g. `user_profile = {"name": "Alice", "age": 30}`; best used when you already know the exact keys and values at the time of writing the code.
- (2) The `dict()` constructor -- useful when converting existing data into dictionary form, for example turning a list of two-element tuples into a dictionary with `dict(pairs)`, or building one from keyword arguments like `dict(x=10, y=20)`; well suited to programmatic or dynamic construction.
- (3) Dictionary comprehensions -- a concise, single-line syntax for transforming an iterable into a dictionary, such as `{x: x**2 for x in range(5)}`; ideal when the keys and/or values need to be computed by applying some expression or filter to an existing sequence rather than typed out by hand.

**Q9. `dict.fromkeys()` is a special case among dictionary-creation methods. Explain what it does, its two parameters, and when you would reach for it over the other creation methods.**

`dict.fromkeys(keys, default)` creates a brand-new dictionary by taking an iterable of keys and assigning the same default value to every one of them. It takes two parameters: 
- keys, an iterable (such as a list) supplying the dictionary's keys, and 
- default, the value to be paired with each of those keys (`optional`; defaults to `None` if omitted). 
- For example, `dict.fromkeys(['task1', 'task2', 'task3'], "Done")` produces `{'task1': 'Done', 'task2': 'Done', 'task3': 'Done'}`.
- You would reach for this method specifically when you need to bulk-initialize many keys with one shared starting value -- a very common pattern for setting up counters, default statuses, or placeholder scores before filling them in with real data later, and it is noticeably more concise than writing out the same value against every key individually, or looping to build the dictionary manually. 
- Unlike the other two creation methods, it is called on the dict class itself rather than on curly braces or an existing dictionary object.

**Q10. Write out the general syntax of a dictionary comprehension and identify its four mandatory components plus the one optional component.**

The general syntax is:
```python
{key_expression: value_expression for variable in iterable if condition}
```

Four components are mandatory: 
(1) `key_expression` -- produces the dictionary key for each iteration, and must evaluate to something hashable, such as `x` or `word.lower()`; 
(2) `value_expression` -- produces the corresponding value, which may be any valid Python object, e.g. `x ** 2` or `len(word)`; 
(3) `for variable in` -- the loop clause that pulls one item at a time from the source; and 
(4) `iterable` -- the source data being looped over, such as a `list`, a `range()`, or even `my_dict.items()`.

The fifth, optional component is the `if` condition clause, which filters which items from the iterable are included in the resulting dictionary -- items for which the condition evaluates to False are simply skipped. Structurally this mirrors list comprehensions closely, except a `dict` comprehension always produces a `key: value` pair rather than a single expression per item.

**Q11. List and explain four common beginner pitfalls when writing dictionary comprehensions.**

(1) Duplicate keys silently overwrite earlier values -- if the source iterable produces the same key more than once, e.g. `{x: x * 10 for x in [1, 1, 2, 2, 3]}`, only the last value assigned to each duplicate key survives, giving `{1: 10, 2: 20, 3: 30}`, with no error or warning raised.

(2) Using an unhashable key expression -- writing something like `{[1, 2]: "value"}` raises `TypeError: unhashable type: 'list'`, since dictionary keys must be hashable, and this restriction applies inside comprehensions exactly as it does with literal dictionaries.

(3) Forgetting `.items()` when comprehending over an existing dictionary -- iterating over a dictionary directly yields only its keys, so `{k: v for k, v in student_marks}` fails with `ValueError: too many values to unpack`, because each `"item"` is a single key, not a `(key, value)` pair; the fix is `student_marks.items()`.

(4) Confusing dictionary comprehensions with set comprehensions -- both use curly braces, but a 
- set comprehension has only one expression per item (`{x ** 2 for x in range(5)}`), 
- while a dict comprehension always has a key: value pair (`{x: x ** 2 for x in range(5)}`); 
- mixing up the two silently produces the wrong kind of object, with no syntax error to flag the mistake.

**Q12. What are the three ways to traverse (iterate over) a dictionary, and when would you use each? Why is `.items()` considered the most Pythonic choice?**

Python offers three traversal patterns. 

(1) Iterating over the dictionary directly, `for key in my_dict:`, which yields only the keys -- this is the default behaviour when a dictionary is used in a for loop, and is appropriate when you only need the keys, or will manually look up values via `my_dict[key]` as needed. 

(2) Using `.values()`, 
example
`for value in my_dict.values():`, 
which yields only the values -- useful when you do not care which key each value belongs to, such as summing all the numeric values in a dictionary. 

(3) Using `.items(),` 
Example
`for key, value in my_dict.items():`

which yields each entry as a `(key, value)` pair that Python automatically unpacks into two loop variables.
`.items()` is considered the most Pythonic choice because it avoids the redundant, less efficient pattern of iterating over keys and then separately indexing back into the dictionary (`my_dict[key]`) to fetch each value -- it retrieves both directly and expresses the intent ("give me each key together with its value") more clearly, in a single loop.

**Q13. Since Python 3.7, dictionaries preserve insertion order. Does this mean a dictionary has become a sequence? Explain, and describe how this order-preservation affects traversal output.**

- No -- insertion-order preservation does not make a dictionary a sequence. 
- A dictionary still cannot be accessed by numeric position (`my_dict[0]` still raises a `KeyError` rather than returning the "first" item), and lookups are still performed exclusively via keys, not indices. 
- What changed in Python 3.7+ is simply that the dictionary now remembers the exact order in which key-value pairs were inserted, and any traversal (`for key in my_dict`, `.values()`, `.items()`) will visit the entries in that same order every time, rather than in some undefined internal order as in earlier Python versions.
- Practically, this makes program output predictable and reproducible -- if you insert keys in the order "a", "b", "c", printing or looping over the dictionary will always show them in that order, which is why many beginners are surprised (pleasantly) that their dictionary "prints back in the order I typed it." 
- It is worth remembering, however, that this ordering is a side-effect of insertion history, not of any indexing capability -- the two properties (ordering vs. sequence-style indexed access) remain independent of each other.

**Q14. What error occurs if you try to delete a key from a dictionary while directly looping over it, and what is the recommended safe technique to avoid it?**

Attempting to add or remove keys from a dictionary while directly iterating over it (e.g. calling `del my_dict[key]` inside a `for key in my_dict: loop)` raises `RuntimeError: dictionary changed size during iteration`. This happens because Python's iterator over a dictionary keeps track of its internal structure as it goes, and that structure is invalidated the moment an entry is added or removed mid-loop -- Python detects this and aborts with an error, rather than risking silently visiting the wrong entries or missing some altogether.
The recommended safe technique is to iterate over a snapshot of the keys rather than the live dictionary itself, **by wrapping the keys view in list() (or tuple())** before the loop begins:
```python
for key in list(my_dict.keys()):
    if my_dict[key] == 2:
        del my_dict[key]
```

Because `list(my_dict.keys())` creates an independent copy of the keys at that moment, deleting entries from the original dictionary during the loop no longer affects the (already-finished) snapshot being iterated over, so no error occurs.

**Q15. What is a dictionary "view object"? Name the three methods that return one, and describe two defining properties that distinguish it from a list.**

A dictionary view object is a special object returned by `.keys()`, `.values()`, and `.items()` that acts as a live window into the dictionary's current contents, rather than an independent snapshot of the data. The three methods that return view objects are 
- `my_dict.keys()` (returns a dict_keys object), 
- `my_dict.values()` (returns a dict_values object), and 
- `my_dict.items()` (returns a dict_items object containing (key, value) tuples).

Two defining properties set view objects apart from lists: 
- first, they are dynamic -- if the underlying dictionary is modified after the view is created (say, a new key is added), the view automatically reflects that change the next time it is inspected or iterated, without needing to be recreated. 
- Second, they are memory efficient -- a view does not store a separate copy of the dictionary's data at all; it simply references the dictionary and computes what to show on demand. A list, by contrast, is a static, independent copy: once created (e.g. via `list(my_dict.keys())`), it is frozen at that moment and will not update even if the original dictionary changes afterward.

**Q16. Using the "window vs. photograph" analogy, explain the practical difference between working with a view object and working with a list derived from it.**

- A view object can be thought of as looking through a window into the dictionary: whatever the dictionary currently contains is exactly what you see through that window, live and up to date, at every moment you look. 
- A list created from that view, by contrast, is like taking a photograph of the dictionary at one specific instant -- the photograph captures the state of the data at that moment, and no matter what happens to the dictionary afterward, the photograph itself never changes.
- Practically, this means: if you write `keys_view = my_dict.keys()` and later add a new key to `my_dict`, printing `keys_view` afterward will include that new key automatically. 
- But if you had instead written `keys_list = list(my_dict.keys())` before the addition, `keys_list` remains exactly as it was, frozen at the time `list()` was called, even though the dictionary itself has since grown. 
- Choosing between the two matters whenever your code both reads keys/values and modifies the dictionary in the same stretch of logic -- a view will silently pick up those modifications, while a list will not, and mixing the two up is a subtle but real source of bugs.

**Q17. (a) Explain the behaviour of `len()`, the `in` operator, and `==` when applied to a dictionary, and (b) explain the difference between comparing two dictionaries with `==` versus `is`.**

- `len(d)` returns the number of key-value pairs in the dictionary -- it counts entries, not keys and values as two separate counts, so a dictionary with three key-value pairs always reports 3, regardless of how large or complex each value is. 
- The `in` operator (`key in d`) tests only whether the given key exists among the dictionary's keys -- it does not search the values, so checking whether a value is present this way will not work as many beginners expect.
- The `==` operator compares two dictionaries by content: two dictionaries are considered equal if they contain exactly the same keys mapped to exactly the same values, regardless of the order in which those pairs were inserted -- insertion order is completely irrelevant to equality. 
- This is distinct from the `is` operator, which checks identity rather than content -- `d1 is d2` is `True` only if both names refer to the literal same object in memory. 
- So two separately-created dictionaries with identical contents will satisfy `d1 == d2` (`True`) but fail `d1 is d2` (`False`), since they are equal in value but are two distinct objects.

**Q18. Why is `dict.get(key, default)` generally preferred over `dict[key]` for reading values? Illustrate with what happens for a missing key in each case.**

- Directly indexing a dictionary with `dict[key]` requires the key to already exist -- if the key is absent, Python immediately raises a `KeyError` and, unless caught, the program crashes at that point. 
- `dict.get(key, default)`, on the other hand, is a safe accessor: if the key exists, it returns the associated value exactly like indexing would; but if the key is missing, instead of raising an error it simply returns the default value you supplied as the second argument (or `None` if no default was given).
- For example, `student.get("marks", 0)` returns the student's marks if that key is present, but harmlessly returns 0 if it is not -- no crash, no need for extra error-handling code. 
- This makes `.get()` the preferred choice whenever you cannot guarantee in advance that a key will exist, such as when working with user input, external data files, or optional configuration settings, since it lets your program supply a sensible fallback instead of having to wrap every lookup in a `try/except KeyError` block.

**Q19. Compare `update()`, `pop()`, `setdefault()`, and `clear()` in terms of what each does, what each returns, and whether each modifies the original dictionary.**

- `update(other)` merges another dictionary (or iterable of key-value pairs) into the current one: for any key already present, its value is overwritten with the new one; for any new key, it is simply added. It modifies the dictionary in place and returns `None` -- it does not return the updated dictionary, a common beginner mistake.
- `pop(key[, default])` removes the specified key from the dictionary and returns the value that was associated with it; if the key does not exist and no default was supplied, it raises `KeyError`, but if a default is supplied, that default is returned instead, avoiding the error -- it also modifies the dictionary by removing the entry.
- `setdefault(key[, default])` is a hybrid of reading and writing: if the key already exists, it simply returns the existing value and leaves the dictionary unchanged; if the key does not exist, it inserts that key with the given default value and returns that same default -- so it modifies the dictionary only when the key was previously absent.
- `clear()` removes every key-value pair from the dictionary, leaving it as an empty dictionary `{}`; it modifies the dictionary in place and, like update(), returns `None`.

**Q20. What does `dict.copy()` actually copy, and why is it described as a "shallow" copy? Give an example showing where this limitation causes unexpected behaviour.**

- `dict.copy()` creates a brand-new dictionary object containing the same keys, mapped to the same values, as the original -- modifying the copy by adding, removing, or reassigning a key at the top level does not affect the original dictionary, and vice versa. 
- However, it is called a shallow copy because it only duplicates the dictionary's own key-value structure -- it does not recursively duplicate any mutable objects stored as values. 
- If a value happens to be, say, a nested list, both the original dictionary and the copy end up holding a reference to the exact same list object in memory, rather than each having its own independent list.
- For example, given `original = {"scores": [10, 20, 30]}` and `copy = original.copy(),` calling `copy["scores"].append(40)` will unexpectedly also change `original["scores"]`, because both "scores" keys point to the identical list -- even though the two dictionaries themselves are independent objects. Avoiding this surprise requires a full "deep copy" (via `copy.deepcopy())`, which recursively duplicates nested mutable structures as well, not just the outer dictionary.
