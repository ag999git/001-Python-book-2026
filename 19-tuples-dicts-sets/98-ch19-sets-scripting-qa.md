


**Q1. Write script: (a) `x = {}` — print its type. (b) Create empty set correctly. (c) Add `"Delhi", "Mumbai", "Pune"` to it. (d) Print type before and after adding.**

```python
# Step 1: The classic trap - {} does not make an empty set
x = {}
print("Type of x:", type(x))          # <class 'dict'> -- not a set
 
# Step 2: The correct way to make an empty set is the set() constructor
cities = set()
print("Type before adding:", type(cities))   # <class 'set'>
 
# Step 3: Add elements one at a time using .add()
cities.add("Delhi")
cities.add("Mumbai")
cities.add("Pune")
 
# Step 4: Confirm type is still 'set' after adding elements
print("Type after adding:", type(cities))    # <class 'set'>
print("Final set:", cities)
```

**Concept applied: Constructor-over-Literal Pattern.**

This script deliberately contrasts two ways of "making an empty collection" to expose a real ambiguity in Python's syntax. 
Lines 2–3 show the trap: because `{}` is *reserved* for an empty dictionary (curly braces are shared between dict and set literals, and with nothing inside them Python has no way to know you meant a set), `type(x)` prints `dict`, not `set`. 

Lines 6–7 show the fix: the `set()` constructor is unambiguous — it always produces a set, empty or not — so it is the only reliable way to create an *empty* set. 

Lines 10–12 then populate that correctly-typed set using `.add()`, and 

Line 15 confirms that the type never changes just because elements were added. 

The pattern to remember: whenever you need to start with nothing and build up, prefer the explicit constructor `set()` over the ambiguous literal `{}`.


**Q2. Roll numbers list has repeats: `[101,102,101,103,104,102,105]`. Script to: get unique roll numbers, print original count vs unique count.**

```python
# Step 1: Original list of roll numbers, with duplicates
roll_numbers = [101, 102, 101, 103, 104, 102, 105]
 
# Step 2: Convert the list to a set -- duplicates are dropped automatically
unique_roll_numbers = set(roll_numbers)
 
# Step 3: Compare counts using len()
print("Original list:", roll_numbers)
print("Original count:", len(roll_numbers))          # 7
print("Unique roll numbers:", unique_roll_numbers)
print("Unique count:", len(unique_roll_numbers))      # 5
```
**Concept applied: Convert-to-Deduplicate Pattern.**

This is the single most common real-world reason to use a set. 

Line 5, `set(roll_numbers)`, is where the actual work happens: passing any iterable to the `set()` constructor hashes every element and inserts it, and because a set structurally cannot hold two elements that compare equal, the second `101` and the second `102` are silently discarded rather than causing an error. 

Lines 8–11 then use `len()` on both the original list and the resulting set to make the deduplication visible as a plain number (7 vs 5) rather than just visually scanning the printed output.

This one-line — `set(some_list)` — is worth noting as the standard, Pythonic way to strip duplicates out of any list.

**Q3. Given `words = ["cat","dog","elephant","ox","tiger","ant"]`. Script: set comprehension to collect lengths of words having more than 2 letter**s.
```python

# Step 1: Starting list of words
words = ["cat", "dog", "elephant", "ox", "tiger", "ant"]
 
# Step 2: Set comprehension - keep the LENGTH of each word,
# but only for words having more than 2 letters (the filter)
long_word_lengths = {len(word) for word in words if len(word) > 2}
 
print("Words:", words)
print("Lengths of words > 2 letters:", long_word_lengths)
# "ox" (length 2) is excluded by the filter
# "cat"(3) and "dog"(3) both produce length 3, which appears only ONCE
```
**Concept applied: Filter-Transform Comprehension Pattern.**

Line 6 combines three separate ideas into one expression. These 3 ideas are:  
1. `len(word)` is the *transform* — it's what actually gets stored in the resulting set, not the word itself. 
2. `for word in words` is the *loop* that walks through every item of the source list. 
3. `if len(word) > 2` is the *filter* — it runs before the transform is stored, and any word that fails this test ("ox", with length 2) is skipped entirely. 

Because the destination is a *set* rather than a list, the fact that `"cat"` and `"dog"` both transform to the same length (3) doesn't produce two separate 3s in the output — the set automatically keeps only one. 

This combination of transform + filter + automatic is exactly why set comprehensions are preferred over writing an equivalent explicit loop when the goal is a collection of unique derived values.

**Q4. `exam_scores = [[78,85,90],[85,92,78],[60,90,100]]`. Script: (a) nested set comprehension to get unique scores. (b) same result using explicit nested for loop. (c) confirm both are equal.**
```python

# Step 1: Nested list -- one sub-list of scores per student
exam_scores = [[78, 85, 90], [85, 92, 78], [60, 90, 100]]
 
# Step 2 (a): Nested set comprehension -- flattens AND deduplicates in one line
# Reading rule: for-clauses run left to right, so 'for row in exam_scores'
# is the OUTER loop, and 'for score in row' is the INNER loop
unique_via_comprehension = {score for row in exam_scores for score in row}
 
# Step 3 (b): The same logic written as an explicit nested loop
unique_via_loop = set()
for row in exam_scores:          # outer loop
    for score in row:            # inner loop
        unique_via_loop.add(score)
 
# Step 4 (c): Confirm both approaches give the identical set
print("Via comprehension:", unique_via_comprehension)
print("Via explicit loop :", unique_via_loop)
print("Are they equal?", unique_via_comprehension == unique_via_loop)   # True
```
**Concept applied: Loop-Flattening Pattern.**

The exercise deliberately builds the same result two ways so the comprehension's shorthand becomes transparent. 

-  Line 7 is the compact form; 

-  lines 11–13 are its literal expansion, written out as a real nested for loop with an explicit `.add()` call. 

Comparing them side by side shows exactly what the comprehension is doing internally: the outer for row in `exam_scores` visits each student's score-list in turn, and for each row, the inner for score in row visits every individual score, which then gets added to the (initially empty) result set. 

Because `85` appears twice, `90` appears twice, and `78` appears twice across the three rows, both approaches end up with the same 6 unique scores — and line 20's equality check confirms the comprehension is not just shorter to type, it is behaviorally identical to the explicit loop.

**Q5. `data = [1, True, 0, False, 2, "1"]`. Script: build a set from data using comprehension, print it, explain length in a comme**nt.
```python
# Step 1: Mixed list containing ints, booleans, and one string
data = [1, True, 0, False, 2, "1"]
 
# Step 2: Build a set using a comprehension
result = {value for value in data}
 
print("Original data:", data)
print("Resulting set:", result)
 
# Step 3: Explanation of the length
# In Python, True == 1 and False == 0, and equal values collapse to ONE
# entry in a set. So 1 and True count as the same element; 0 and False
# count as the same element. The string "1" is a DIFFERENT type and never
# collides with the number 1. Result has only 4 unique entries, not 6:
# one of {1, True}, one of {0, False}, the number 2, and the string "1"
```
**Concept applied: Type-Coercion Awareness Pattern.**

This script is written to produce a surprising result on purpose, so students learn to predict it rather than be confused by it later. 

The comprehension on line 5 looks completely ordinary, but the printed set has 4 elements, not 6, because Python booleans are internally a subtype of integer — `True == 1` and `False == 0` both evaluate to `True`. 

Since a set treats any two elements that compare equal as "the same," whichever of the pair (`1, True`) is encountered first is kept, and the second is silently treated as a duplicate and dropped — likewise for (`0, False`). The string `"1"`, however, is a completely different type from the integer `1` and is never considered equal to it, so it survives as its own separate element. 

The lesson: never assume a set's length will match the number of items you put in, if the source data mixes booleans with integers.

**Q6. Script: (a) try adding a list `[1,2]` as a set element, catch the error. (b) fix it by converting to tuple, add successfully. Print set after each step.**

```python

# Step 1: Start with a simple set
my_set = {10, 20}
print("Before:", my_set)
 
# Step 2 (a): Attempt to add a LIST -- lists are mutable, hence unhashable
try:
    my_set.add([1, 2])
except TypeError as e:
    print("Error caught:", e)              # unhashable type: 'list'
 
# Step 3 (b): Fix -- convert the list to a TUPLE first (tuples are immutable)
my_set.add(tuple([1, 2]))
print("After fix:", my_set)                # {10, 20, (1, 2)}
```

**Concept applied: Try-Except Guard Pattern, followed by Type-Conversion Fix.**

Line 7's try block deliberately attempts an operation known to fail, 
so the `TypeError` on line 9 can be caught and displayed cleanly instead of crashing the whole program — this is the standard, defensive way to handle an operation whose failure is expected and recoverable. 

The *reason* it fails connects directly back to the chapter's core rule: every set element must be hashable, and lists are mutable, so Python refuses to store one directly. 

Line 12 supplies the actual fix: `tuple([1, 2])` converts the mutable list into an immutable tuple with the same values, and because tuples of hashable elements are themselves hashable, `.add()` now succeeds. 

The general takeaway worth reinforcing: whenever you hit unhashable type on a list, converting it to a tuple is almost always the correct first thing to try, provided the list's own contents are all hashable too.

**Q7. `t = (1, 2, [3, 4])`. Script: try to add t to a set, catch and print the specific error type, explain in comment why a tuple can still fail.**
```python

# Step 1: A tuple that LOOKS immutable but has a mutable element inside
t = (1, 2, [3, 4])
 
my_set = {100}
 
# Step 2: Attempt to add the tuple to the set
try:
    my_set.add(t)
except TypeError as e:
    print("Error type:", type(e).__name__)   # TypeError
    print("Error message:", e)                # unhashable type: 'list'
 
# Step 3: Explanation
# A tuple's OWN structure cannot change, but hashability is checked
# RECURSIVELY -- Python must also be able to hash every element INSIDE
# the tuple. Here, t contains a list, and lists can never be hashed.
# So even though t is technically "a tuple", it is NOT hashable overall,
# and cannot be stored in a set.
```
**Concept applied: Recursive Hashability Check Pattern.**

This exercise targets a subtle but important misconception: "tuples are immutable" does not automatically mean "tuples are always hashable." 

Line 2 sets up a tuple whose outer structure is fixed — you can never reassign `t[2]` — but whose third element is itself a mutable list. 

When line 9 attempts `.add(t)`, Python has to compute a hash for the tuple, which in turn requires computing a hash for every element inside it; the moment it reaches the nested list, hashing fails, and the error raised (line 11–12) still names 'list', not 'tuple' — confirming the *real* culprit is the object nested inside, not the tuple itself. 

The rule to note: a tuple is hashable only if every element it contains, all the way down, is also hashable — immutability of the outer container is necessary but not sufficient.

**Q8. Script: (a) create two frozensets from {1,2,3} and {3,4,5}. (b) try `.add()` on one, catch error. (c) put both frozensets into a set. (d) use one as a dictionary key.**

```python
# Step 1: Create two frozensets (immutable versions of a set)
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({3, 4, 5})
print("fs1:", fs1)
print("fs2:", fs2)
 
# Step 2 (b): Attempt to modify a frozenset -- this must fail
try:
    fs1.add(99)
except AttributeError as e:
    print("Error caught:", e)     # 'frozenset' object has no attribute 'add'
 
# Step 3 (c): Store both frozensets inside a regular set
# This is only legal because frozenset is HASHABLE (a plain set is not)
collection_of_sets = {fs1, fs2}
print("Set of frozensets:", collection_of_sets)
 
# Step 4 (d): Use a frozenset as a dictionary key
labels = {fs1: "Group A", fs2: "Group B"}
print("Label for fs1:", labels[fs1])   # Group A
```

**Concept applied: Immutable Wrapper Pattern.**

Each step demonstrates one consequence of the same underlying fact. 

Lines 2–3 create two frozensets — they behave like normal sets for reading, 

but line 9's attempt to call `.add()` on fs1 fails with an `AttributeError` (not a `TypeError`) because the mutating methods (`add, remove, discard, pop, clear`) simply don't exist on a frozenset at all — they were never defined, rather than being blocked at runtime. 

Because a frozenset's contents can never change, Python can compute one fixed hash value for it, which is exactly what makes lines 17 and 21 valid: 

A plain set could never be nested inside another set or used as a dict key (both require hashability), but a frozenset can be used in both roles precisely because it traded away mutability for hashability. 

Note: 
-  set for everyday mutable collections, 
- frozenset specifically when a set-like object needs to itself be hashable.

**Q9. Script: (a) `s1={"a"}`, do `s1.add("bc")`; print. (b) `s2={"a"}`, do `s2.update("bc")`; print. Explain difference in a comment.**

```python
# Step 1 (a): Using .add() with a two-character string
s1 = {"a"}
s1.add("bc")
print("After add('bc'):", s1)          # {'a', 'bc'}  -- "bc" is ONE element
 
# Step 2 (b): Using .update() with the SAME string
s2 = {"a"}
s2.update("bc")
print("After update('bc'):", s2)       # {'a', 'b', 'c'} -- each CHAR is an element
 
# Step 3: Explanation
# .add(x) always inserts x as ONE new element, no matter what x is.
# .update(iterable) walks through the argument and inserts each item
# it produces. A string IS an iterable of its own characters, so
# update("bc") inserts 'b' and 'c' separately, NOT the string "bc".
```
**Concept applied: Single-Element vs Iterable-Unpacking Pattern.**

The two nearly-identical calls on lines 3 and 8 produce visibly different results, and that gap is the entire point of the exercise. 

`.add("bc")` treats its argument as an atomic, single value to be inserted — Python does not look inside a string passed to `.add()`, so the two-character string becomes exactly one new set element. 

`.update("bc")`, by contrast, expects an *iterable* and inserts every element that iterable yields; since a string is iterable character-by-character, update walks through `"bc"` and inserts `'b'` and `'c'` as two separate elements. 

The pattern to remember when choosing between these two methods: 
- use `.add()` when you have exactly one new value to insert, and 
- `.update()` only when you deliberately want to merge in *every* element of another collection — being especially careful with strings, since they're iterable in a way that surprises many beginners.

**Q10. `langs = {"Python","Java","C++"}`. Script: (a) `.remove("Ruby")` — catch error. (b) `.discard("Ruby")` — show no error. (c) print set unchanged after both.**

```python

# Step 1: Starting set
langs = {"Python", "Java", "C++"}
print("Original:", langs)
 
# Step 2 (a): .remove() on a MISSING element -- raises KeyError
try:
    langs.remove("Ruby")
except KeyError as e:
    print("remove() failed with KeyError:", e)
 
# Step 3 (b): .discard() on the SAME missing element -- silent, no error
langs.discard("Ruby")
print("discard() completed with no error")
 
# Step 4 (c): Confirm the set is unchanged after both attempts
print("Final set:", langs)      # {'Python', 'Java', 'C++'} -- untouched
```
**Concept applied: Strict vs Safe Removal Pattern.**

The two removal attempts on the same missing element (`"Ruby"`) are placed back to back so the difference in behavior is unmistakable. 
-  Line 8's `.remove("Ruby")` raises a `KeyError` because `.remove()` is the *strict* form — it assumes the element should be present, and treats its absence as an error worth stopping the program for, which is why it's wrapped in a `try/except` here. 

-  Line 13's `.discard("Ruby")` is the *safe*, permissive form — if the element isn't there, it simply does nothing and execution continues normally, with no exception to catch at all. 

The rule for choosing between them: 
-  use `.remove()` when the element's absence would itself indicate a bug you want surfaced immediately; 
- use `.discard()` when "it might not be there, and that's fine" is a perfectly normal, expected case.

**Q11. `nums = {1,2,3}`. Script: (a) `.pop()` twice, print each removed item. (b) `.pop()` on the now-single-item set, then again on the resulting empty set — catch the error. (c) `.clear()` and print final set.**

```python

# Step 1: Starting set with 3 elements
nums = {1, 2, 3}
print("Start:", nums)
 
# Step 2 (a): pop() twice -- removes and RETURNS an arbitrary element each time
item1 = nums.pop()
print("Popped:", item1, "| Remaining:", nums)
item2 = nums.pop()
print("Popped:", item2, "| Remaining:", nums)      # only 1 element left
 
# Step 3 (b): pop() the last remaining element, then try again on an EMPTY set
item3 = nums.pop()
print("Popped:", item3, "| Remaining:", nums)      # set() -- now empty
 
try:
    nums.pop()                 # nothing left to remove
except KeyError as e:
    print("pop() on empty set failed:", e)          # 'pop from an empty set'
 
# Step 4 (c): clear() -- wipes everything, safe even if already empty
other = {5, 6, 7}
other.clear()
print("After clear():", other)     # set()
```
**Concept applied: Drain-Until-Empty Pattern.**

This script walks a set down to nothing on purpose, to expose exactly where `.pop()` stops being safe. 

Lines 6 and 8 each call `.pop()`, which — unlike `.remove()` — takes no argument and instead removes and returns *some* element chosen arbitrarily, since a set has no defined "first" item to prefer. 

That's fine as long as elements remain, but line 17's third `.pop()` empties the set entirely, and the fourth attempt on line 20 has nothing left to remove, so it raises a `KeyError` rather than returning None or silently doing nothing — `.pop()` always expects to find *something*. 

Lines 25–26 contrast this with `.clear()`, which is unconditionally safe to call any time: it wipes every element in one step and returns `None`, and calling it on an already-empty set causes no error at all. 

The pattern worth remembering: 
-  `.pop()` is for removing items one at a time when you don't care which, but it must be guarded against an empty set; 
-  `.clear()` is for wiping everything at once and never needs guarding.

**Q12. Script: compare lookup time of 500000 in `a_list` vs 500000 in `a_set` for `range(0,1000000)`. Use `time.perf_counter()`. Print both timings with a comment on which is faster and why.**

```python

import time
 
# Step 1: Build a large list and an equivalent set with the same values
a_list = list(range(1000000))
a_set = set(a_list)
 
target = 500000
 
# Step 2: Time the membership test on the LIST
start = time.perf_counter()
target in a_list
list_time = time.perf_counter() - start
 
# Step 3: Time the membership test on the SET
start = time.perf_counter()
target in a_set
set_time = time.perf_counter() - start
 
# Step 4: Print and compare
print(f"List lookup time: {list_time:.6f} seconds")
print(f"Set lookup time : {set_time:.6f} seconds")
 
# The set is almost always much faster: a list performs a linear search
# (checks elements one by one -- O(n)), while a set uses hashing to jump
# directly to where the element should be (O(1) on average).
```
**Concept applied: Benchmark-Comparison Pattern.**

The script's structure — build two equivalent collections, then time the *identical* operation on each — is the standard way to make an abstract claim ("sets are faster") concretely visible. 

Lines 10–12 and 15–17 are deliberately symmetrical: same target value, same `time.perf_counter()` calls, same single in check, so the only variable being measured is the container type itself. 

The result reflects the two very different search strategies discussed in the chapter: 
-  list membership testing walks through elements one at a time until it finds a match or reaches the end (worst case, all million elements), 
-  while set membership testing computes hash(target) once and jumps straight to the expected location. 

This is exactly why in on a set is the standard tool of choice whenever a program needs to repeatedly ask "have I seen this value before?" against a large collection.

**Q13. `nums = {1,2,3,4,5,6,7,8}`. Script: (a) try removing even numbers while looping directly over nums — catch the resulting error. (b) fix using `.copy()`, print final set.**

```python

# Step 1: Starting set
nums = {1, 2, 3, 4, 5, 6, 7, 8}
 
# Step 2 (a): WRONG approach -- modifying the set while iterating over IT directly
try:
    for n in nums:
        if n % 2 == 0:
            nums.remove(n)          # changing size DURING iteration
except RuntimeError as e:
    print("Error caught:", e)        # Set changed size during iteration
 
# Step 3 (b): CORRECT approach -- iterate over a COPY, modify the ORIGINAL
nums = {1, 2, 3, 4, 5, 6, 7, 8}          # reset
for n in nums.copy():                     # safe: looping over an independent copy
    if n % 2 == 0:
        nums.remove(n)                    # modifying the original is now safe
 
print("Final set (odd numbers only):", nums)   # {1, 3, 5, 7}
```

**Concept applied: Copy-Before-Modify Pattern.**

This is one of the most important safety habits for working with sets (and dictionaries). 

Lines 6–8 attempt the naive approach — looping over `nums` with `for n in nums` while simultaneously calling `nums.remove(n)` inside that same loop — and Python deliberately raises a `RuntimeError` rather than allowing it, because changing a set's size mid-iteration can silently skip or repeat elements in ways the iterator cannot safely handle. 

The fix on lines 15–17 changes exactly one thing: `for n in nums.copy()` iterates over a brand-new, independent copy of the set, so removing elements from the *original* nums inside the loop body no longer disturbs the sequence currently being iterated. 

The general pattern — iterate over a copy, mutate the original — is the standard, idiomatic fix any time you need to filter or prune a set (or dict) in place while looping over it.

**Q14. `a = {1,2,3}`, `values = [3,4,5]`. Script: (a) try a & values — catch error. (b) fix using `.intersection(values)`. (c) fix using a & `set(values)`. Show all three attempts.**

```python

# Step 1: A set and a plain list with one overlapping value
a = {1, 2, 3}
values = [3, 4, 5]
 
# Step 2 (a): Operator form -- requires BOTH sides to already be sets
try:
    result = a & values
except TypeError as e:
    print("Operator failed:", e)      # unsupported operand type(s) for &
 
# Step 3 (b): Fix 1 -- use the named METHOD, which accepts any iterable
result_method = a.intersection(values)
print("Using .intersection():", result_method)     # {3}
 
# Step 4 (c): Fix 2 -- convert the list to a set FIRST, then use the operator
result_converted = a & set(values)
print("Using & after set(values):", result_converted)   # {3}
```

**Concept applied: Operator-Strictness vs Method-Flexibility Pattern.**

The script deliberately fails first, then shows two independent fixes, to make the operator/method distinction concrete rather than abstract. 

Line 7's a & values fails because mathematical operators (`|, &, -, ^`) demand that *both* operands already be genuine set objects — a list is rejected outright with a `TypeError`, regardless of what values it contains. 

Line 13's `.intersection(values)` succeeds because named methods are more forgiving: they accept *any* iterable and internally treat its elements as if they were a set, with no manual conversion required. 

Line 17's a & `set(values)` succeeds for a different reason — it doesn't change which syntax is used, it removes the actual problem by converting the list into a real set *before* the operator ever sees it. 

Either fix is valid; the method form is usually more convenient when one side isn't already a set, while the operator form reads more like ordinary math when both sides already are.

**Q15. Two classes: `python_club={"Aman","Riya","Zoya","Kabir"}`, `dance_club={"Zoya","Kabir","Neha","Omar"}`. Script: find (a) all students in at least one club (b) students in both (c) students only in `python_club` (d) students in exactly one club. Label each print.**

```python

# Step 1: Two clubs, represented as sets of student names
python_club = {"Aman", "Riya", "Zoya", "Kabir"}
dance_club = {"Zoya", "Kabir", "Neha", "Omar"}
 
# Step 2 (a): Union -- everyone in AT LEAST ONE club
at_least_one = python_club | dance_club
print("In at least one club:", at_least_one)
 
# Step 3 (b): Intersection -- everyone in BOTH clubs
in_both = python_club & dance_club
print("In both clubs:", in_both)                    # {'Zoya', 'Kabir'}
 
# Step 4 (c): Difference -- ONLY in python_club, not in dance_club
only_python = python_club - dance_club
print("Only in python_club:", only_python)           # {'Aman', 'Riya'}
 
# Step 5 (d): Symmetric Difference -- in EXACTLY ONE club, not both
exactly_one = python_club ^ dance_club
print("In exactly one club:", exactly_one)
```
**Concept applied: Venn-Diagram Computation Pattern.**

Each of the four operations answers a distinct, precise question about the same two groups, and the script deliberately labels each print statement so the mapping from operation to real-world meaning is unmistakable. 

Line 6's union (`|`) merges every name from either club, with the shared members Zoya and Kabir appearing only once. 

Line 10's intersection (`&`) keeps only names present in *both* sets — exactly the overlap region of a Venn diagram. 

Line 14's difference (`-`) is directional: it keeps what's in python_club but strips out anything also found in dance_club, leaving only the exclusively-Python members. 

Line 18's symmetric difference (`^`) keeps everyone who belongs to exactly one club — effectively the union with the overlap carved back out. 

Together these four lines demonstrate that Python's set operators are a direct, one-symbol-each translation of standard Venn-diagram set mathematics.

**Q16. `project_team={"Zoya","Kabir"}`, `python_club={"Aman","Riya","Zoya","Kabir"}`, `art_club={"Neha","Omar"}`. Script: check (a) project_team is subset of python_club (b) python_club is superset of project_team (c) python_club and art_club are disjoint.**

```python

# Step 1: Three groups
project_team = {"Zoya", "Kabir"}
python_club = {"Aman", "Riya", "Zoya", "Kabir"}
art_club = {"Neha", "Omar"}
 
# Step 2 (a): Is every project_team member also in python_club?
is_subset = project_team.issubset(python_club)
print("project_team subset of python_club?", is_subset)     # True
 
# Step 3 (b): Does python_club contain every project_team member?
is_superset = python_club.issuperset(project_team)
print("python_club superset of project_team?", is_superset)  # True
 
# Step 4 (c): Do python_club and art_club share ZERO members?
are_disjoint = python_club.isdisjoint(art_club)
print("python_club and art_club disjoint?", are_disjoint)    # True
```

**Concept applied: Relationship-Testing Pattern.**

All three checks answer a "containment" question, but each from a slightly different direction, which is exactly why the chapter treats them as a related family. 

Line 8's `.issubset()` asks the question from the *smaller* group's perspective — "is every one of my members also found in that bigger group?" — and returns True because both `Zoya` and `Kabir` appear in `python_club`. 

Line 12's `.issuperset()` asks the mirror-image question from the *larger* group's perspective — "do I contain every member of that smaller group?" — using the same two sets, just called from the other side; note that `project_team.issubset(python_club)` and `python_club.issuperset(project_team)` are logically equivalent statements, just phrased from opposite ends. 

Line 16's `.isdisjoint()` is a different kind of question entirely — not about one being contained in the other, but about whether they overlap *at all* — and returns `True` here because `python_club` and `art_club` share no names in common.

**Q17. `set_a={10,20,30}`, `set_b={20,30,40}`. Script: print `set_a` - `set_b` and `set_b - set_a`, explain in comment why results differ.**

```python

# Step 1: Two overlapping sets
set_a = {10, 20, 30}
set_b = {20, 30, 40}
 
# Step 2: Difference in BOTH directions
result_ab = set_a - set_b
result_ba = set_b - set_a
 
print("set_a - set_b =", result_ab)     # {10}  -- in A but not in B
print("set_b - set_a =", result_ba)     # {40}  -- in B but not in A
 
# Step 3: Explanation
# A - B keeps whatever is in A, EXCLUDING anything also found in B.
# Swapping the order changes WHICH set's exclusive elements you keep --
# so A - B and B - A are almost never the same. Set difference is
# therefore not commutative (unlike union or intersection, which give
# the same answer regardless of the order of operands).
```

**Concept applied: Order-Sensitive Operation Pattern.**

The script computes both directions of the same subtraction side by side specifically so the asymmetry is visible in the output rather than just stated in words. 

Line 7's `set_a - set_b` keeps `10` because it's the only element present in `set_a` that does *not* also appear in `set_b`; 

line 8's `set_b - set_a` keeps `40` for the mirror-image reason — it's the only element unique to `set_b`. 

Unlike union (`|`) and intersection (`&`), which always return the same result no matter which operand comes first, difference (`-`) is fundamentally directional: it always means "what's here, minus what's also over there," and swapping the operands swaps which set's exclusive elements survive.

Note: whenever a set operation involves -, always double-check which side of the expression represents the set you actually want to keep from.
 
**Q18. Same data `["Amit","Amit","Sneha","Ravi"]`. Script: store it as (a) a list, (b) a set, (c) a dict (using names as keys, value=1). Print all three and comment on what changed in each.**

```python

# Step 1: Same raw data, stored three different ways
data = ["Amit", "Amit", "Sneha", "Ravi"]
 
# Step 2 (a): As a LIST -- order preserved, duplicates preserved
as_list = list(data)
print("As list:", as_list)          # ['Amit', 'Amit', 'Sneha', 'Ravi']
 
# Step 3 (b): As a SET -- order NOT guaranteed, duplicates removed
as_set = set(data)
print("As set:", as_set)            # {'Amit', 'Sneha', 'Ravi'}
 
# Step 4 (c): As a DICT -- keys must be unique (acts like a set of keys),
# but each key now maps to a VALUE
as_dict = {name: 1 for name in data}
print("As dict:", as_dict)          # {'Amit': 1, 'Sneha': 1, 'Ravi': 1}
 
# Comment: the list keeps everything exactly as given (including the
# repeated "Amit"). The set silently drops the repeat and gives up
# ordering. The dict also drops the repeat (because keys must be
# unique) but additionally lets each name carry an associated value.
```

**Concept applied: Structure Selection Pattern.**

Storing the *identical* input list three different ways is the clearest way to make each structure's defining trade-off visible in one glance. 

Line 6's list keeps `"Amit"` twice and preserves the exact original order — nothing is lost, but nothing is deduplicated either. 

Line 10's set drops the second `"Amit"` automatically (sets never allow duplicates) and gives no guarantee about the order in which the remaining names print. 

Line 15's dict comprehension also ends up with only one `"Amit"` — because dictionary keys, like set elements, must be unique — but unlike a set, each surviving name is now paired with an associated value (here, simply 1), which a set has no way to represent at all. 

The exercise reinforces the chapter's core comparison: reach for a list when order and repetition both matter, a set when you only care whether something is present, and a dict when you need to attach information to each unique item.

**Q19. `group1=frozenset({"Math","Physics"})`, `group2=frozenset({"Biology","Chemistry"})`. Script: (a) use both as dict keys mapping to room numbers. (b) print room for `group1`. (c) put both frozensets inside a regular set and print its length.**

```python

# Step 1: Two frozensets representing subject combinations
group1 = frozenset({"Math", "Physics"})
group2 = frozenset({"Biology", "Chemistry"})
 
# Step 2 (a): Use frozensets as dictionary KEYS -- legal because frozenset
# is immutable and therefore hashable (a regular set could NOT do this)
classrooms = {group1: "Room 101", group2: "Room 202"}
 
# Step 3 (b): Look up the room assigned to group1
print("Room for group1:", classrooms[group1])    # Room 101
 
# Step 4 (c): Store both frozensets inside an ordinary set
subject_groups = {group1, group2}
print("Number of subject groups:", len(subject_groups))   # 2
```

**Concept applied: Immutable-Key Mapping Pattern.**

This script demonstrates the one practical job that only a frozenset (never a plain set) can do. 

Line 8 builds a dictionary whose *keys* are frozensets — this is only legal because dictionary keys, like set elements, must be hashable, and a frozenset qualifies precisely because its contents can never change after creation, giving it one fixed, permanent hash value. 
A plain set in the same position would raise a `TypeError: unhashable type: 'set'`, because a mutable object's hash could change out from under the dictionary at any time. 

Line 11's lookup, `classrooms[group1]`, then works exactly like any other dictionary lookup — Python hashes group1 and jumps straight to its associated value, `"Room 101"`. 

Line 15 shows the second consequence of the same hashability: because frozensets are hashable, two of them can also live together inside an ordinary set, something two plain sets could never do.

**Q20. `fruits={"Apple","Banana","Cherry"}`. Script: (a) try `fruits.items()` — catch error. (b) correctly print each fruit using a for loop.**

```python

# Step 1: A set of fruit names
fruits = {"Apple", "Banana", "Cherry"}
 
# Step 2 (a): A set stores only VALUES -- it has no keys, so .items()
# (a dict-only method) does not exist for it
try:
    print(fruits.items())
except AttributeError as e:
    print("Error caught:", e)     # 'set' object has no attribute 'items'
 
# Step 3 (b): The correct way to visit every element of a set
for fruit in fruits:
    print(fruit)                  # Apple, Banana, Cherry (order may vary)
```

**Concept applied: Method-Availability Awareness Pattern.**

The error on line 9 is a useful diagnostic in its own right: it's an `AttributeError`, not a `TypeError`, which tells you the method genuinely doesn't exist on this type at all — `.items()`, `.keys()`, and `.values()` are dictionary-only methods that make sense only for a *key:value mapping*, and a set has no keys or values, only standalone elements, so none of the three exist for it. 

Line 13's fix doesn't try to work around this — it uses the one traversal tool every iterable, including a set, always supports: a plain for element in collection loop. 

The exercise reinforces a broader point worth remembering across the whole chapter: before reaching for a specific method on a collection, it helps to first ask *which* family of operations that type actually supports — sequence operations (indexing), mapping operations (`.items()/.keys()/.values()`), or the more limited value-only operations that a set provides.
