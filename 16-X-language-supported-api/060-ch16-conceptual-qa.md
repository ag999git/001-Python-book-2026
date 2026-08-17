



# Chapter 16: Python Libraries for Data Structures and Algorithms

## Conceptual Questions with Answers

*Questions: printed in book | Answers: available in this online resource*

**Q1. Linear vs Binary Search: prerequisites, complexity, and trade-offs.**

### (a) What prerequisite does binary search need that linear search does not?

**(b) Why is binary search O(log n)? Show with numbers: 1,000 items vs 1,000,000 items.** 
**(c ) If data changes frequently, is binary search always the better choice? Why/why not?**

### Answer:

(a) Binary search requires the list to be sorted before the search begins. Linear search works on any list - sorted or unsorted - because it checks every item one by one without making any assumptions about order. This makes linear search universally applicable but slower for large datasets. 

(b) Binary search is `O(log n)` because after every comparison it discards exactly half of the remaining search space. Starting with n items:

- After 1 comparison: n/2 items remain
- After 2 comparisons: n/4 items remain
- After k comparisons:  (n/k²) items remain The search ends when 1 item remains: (n/k²)  = 1, so k = log₂(n). For 1,000 items: log₂(1000) ≈ 10 comparisons. For 1,000,000 items: log₂(1,000,000) ≈ 20 comparisons. Doubling the data only adds one more comparison - the growth is extraordinarily slow. 

(c ) Not necessarily. If data changes frequently (items are inserted, deleted, or modified regularly), the list must be re-sorted before each binary search. The cost of re-sorting - `O(n log n)` for Python's `Timsort` - can easily outweigh the speed advantage of binary search over linear search. In such cases, either accept linear search `O(n)`, or use a data structure that maintains sorted order automatically on insertion, such as the bisect module's `insort()` function or a balanced BST.

**Q2. Bubble Sort mechanics and the O(n²) derivation - explain the two loops, derive the total comparison formula, and state when O(n) is achievable.**

### Answer:

Bubble sort uses two nested loops because it has two separate jobs. The outer loop controls how many passes are made through the list. The inner loop does the actual work - comparing each neighbouring pair and swapping them if they are in the wrong order.

#### Outer loop: for pass_no in `range(n - 1)`

After each complete pass, the largest remaining item has bubbled to its final position at the right end. So the total number of passes needed is n - 1 (the last item automatically falls into place).

#### Inner loop: `for i in range(n - pass_no - 1)`

After each pass, the rightmost pass\_no items are already sorted and never need to be compared again. So the inner loop shrinks by one each time.

#### Deriving the total comparisons:

Pass 0: n-1 comparisons. 

Pass 1: n-2 comparisons. 

Pass 2: n-3 comparisons … 

Last pass: 1 comparison.

Total = (n-1) + (n-2) + (n-3) + … + 1 = n(n-1)/2 = (n² - n)/2. 

In Big-O notation, only the dominant term matters, so: Bubble Sort = `O(n²)`.

#### When is `O(n)` achievable?

Only with the optimised version that includes an `is_swapped` flag. If a complete pass produces zero swaps, the list is already sorted and the outer loop exits immediately. For an already-sorted list this requires only one pass of `n-1` comparisons = `O(n)`. The basic implementation shown without the flag is always `O(n²)` regardless of input order.

**Q3. Insertion Sort: card analogy, shift vs swap, and why it outperforms Bubble Sort in practice despite identical O(n²) worst-case.**

### Answer:

Insertion Sort is best understood through the card-dealing analogy. Imagine being dealt cards one at a time into your left hand. Each new card (the 'key') is compared against the cards already in your hand. Larger cards slide one space to the right to make room, and the new card is inserted into the correct gap. The left hand always holds a sorted partial list.

### Shift vs Swap - the critical performance difference:

Bubble Sort and Selection Sort use swaps. A swap requires 3 memory write operations: a temporary variable stores one value, then both values are exchanged. Insertion Sort uses shifts - each item simply copies one position to the right, requiring only 1 memory write per item moved. Example: moving the value 1 from the back to the front of a 10-item list:

- Bubble Sort: 9 swaps × 3 writes = 27 memory writes
- Insertion Sort: 9 shifts × 1 write = 9 memory writes 

Insertion Sort does roughly 3 times less writing to memory, which makes it significantly faster in practice even though both algorithms are O(n²) in Big-O terms. Big-O analysis ignores constant factors; real hardware performance does not.

### Best case O(n):

When the list is already sorted, the while condition (numbers[position] > key) fails immediately on every pass - no shifts occur at all. Each pass requires exactly one comparison and zero writes. Total work = `n-1` comparisons = O(n). This makes Insertion Sort the algorithm of choice for nearly-sorted data, which is why Python's own `Timsort` uses it internally for small chunks.

**Q4. `pop(0)` on a list is a performance trap - explain why, what O(n) means physically, and how deque solves it. Include the `appendleft()` vs `insert(0,...)` distinction.**

### Answer:

A Python list stores items in contiguous memory - each item occupies a specific position immediately adjacent to the next. This layout is what makes indexing (`list[i]`) O(1) and appending to the end O(1). However, it creates a fundamental problem for front removal.

### Why `pop(0)` is `O(n)`:

When you call `list.pop(0)`, Python removes the item at index 0 but cannot leave an empty gap in memory - all subsequent items must be shifted one position to the left to close the hole. For a list of 10,000 items, removing one item from the front requires 9,999 memory write operations. Called in a loop, this produces `O(n²)` total behaviour - exactly the performance disaster you were trying to avoid by using a queue.


### How deque solves it:

`collections.deque` uses a doubly-linked internal structure rather than contiguous memory. Each end of the deque has a direct pointer to the next node. Adding or removing from either end requires only updating two pointers - `O(1)` regardless of how many items the deque contains. No shifting ever occurs.

**`appendleft()` vs `insert(0,...)` on a deque:**

deque does have an `insert()` method, but `insert(0, item)` is O(n) even on a deque because it is a general-purpose method that navigates to an arbitrary position. `appendleft(item)` is a dedicated O(1) method that goes directly to the front. Always use `appendleft()` and `popleft()` for front operations on a deque - never `insert(0,...)` or `pop(0)`.

**Q5. `Counter`, `defaultdict`, and `ChainMap` from `collections` - what problem does each solve? When would you use `defaultdict(list)` vs `defaultdict(int)` vs `Counter`?** 
**Answer:**

### Counter:

Counter is a specialised dictionary for counting occurrences. Given any iterable, it produces a frequency map in a single line. Its most useful extra capability is `.most_common(n)`, which returns the `n` most frequent items without requiring a manual sort. Use Counter when your sole goal is counting.

**`defaultdict`:**

`defaultdict` is a dictionary that automatically creates a default value for any missing key, eliminating the need for an if-key-not-in-dict guard before every insertion. The type you pass determines the default:

 - `defaultdict(list)` creates `[]` for new keys (best for grouping items into categories), 
  - `defaultdict(int)` creates `0` (best for counting with additional logic in the same loop), 
  - `defaultdict(set)` creates `set()` (best for grouping while eliminating duplicates). 
 
 Use `defaultdict(int)` when you need counting combined with other
   operations; 
Use Counter when counting alone is sufficient.

### `ChainMap`:

`ChainMap` groups multiple dictionaries into a single view without merging or copying them. Lookups search left to right, stopping at the first match. Writes always go to the first dictionary only. It is memory-efficient (no data is duplicated) and live - if the original dictionaries change, the `ChainMap` reflects those changes immediately. The canonical use case is layered settings: user preferences override application defaults, which override system defaults, without any dictionary being modified.

**Q6. `namedtuple` vs `dataclass` - compare immutability, default values, type hints, and when to choose each. What does `frozen=True` do in a `dataclass`?**

### Answer:

Both `namedtuple` and `dataclass` create structured data containers with named fields accessible by dot notation. They differ significantly in flexibility and capability.

| Feature | namedtuple | dataclass |
| --- | --- | --- |
| Mutability | Always immutable — values cannot be changed after creation | Mutable by default; `frozen=True` makes it immutable |
| Default values | Not supported directly (workaround: `__new__` override) | Fully supported: `age: int = 18` |
| Type hints | Not required — field names only | Required — `@dataclass` reads annotations to identify fields |
| Memory | Slightly more efficient — inherits from tuple | Slightly more overhead but negligible for most uses |
| Methods auto-generated | `__repr__`, `__eq__` only | `__init__`, `__repr__`, `__eq__`, and optionally `__lt__`, `__hash__` |
| Inheritance | Creates a tuple subclass | Normal class inheritance |
| Best for | Lightweight, immutable records; replacing plain tuples | Structured data with defaults, validation, and optional mutability |





**`frozen=True` in `dataclass`:**

`@dataclass(frozen=True)` makes all fields read-only after the object is created. Any attempt to assign a new value raises `FrozenInstanceError`. It also makes the object hashable (since it is immutable), allowing it to be used as a dictionary key or in a set. This is similar to namedtuple but with the full power of dataclass (default values, complex types, field() options).

**`field()` and mutable defaults:**

A common mistake is writing subjects: `list = []` in a dataclass. This creates one shared list for all instances. The correct approach is `subjects: list = field(default_factory=list)`, which creates a fresh empty list for each new object.

**Q7. `heapq` module - what is a min-heap? How is it stored in Python? How do you simulate a maxheap? Show with a priority queue example using tuples. Answer:**

A heap is a binary tree with one strict rule: every parent node is smaller than (or equal to) both its children. This is called the min-heap property. The `root (top)` of the tree always contains the smallest value in the entire structure, making it instantly available without searching.

### How Python stores a heap:

Python does not use an actual tree data structure. It stores the heap as a plain list using a mathematical index relationship: for any item at `index i`, its left child is at `2i+1` and its right child at `2i+2`. This makes the tree structure implicit - no node objects, no pointers, just a list with a guaranteed ordering.

### Max-heap simulation (negation trick):

Python's `heapq` only provides min-heap behaviour. To always retrieve the largest item first, store every value as its negative. The min-heap surfaces the most negative value first; negating it on the way out gives the original largest value.

```python
import heapq
tasks = []
heapq.heappush(tasks, (-10, 'Critical')) # store -10 for priority 10
heapq.heappush(tasks, (-3, 'Low'))
heapq.heappush(tasks, (-7, 'Important'))
priority, task = heapq.heappop(tasks)
print(-priority, task) # Output: 10 Critical
```

-----

The tuple form `(priority, item_name)` is the standard pattern. When two items have equal priority, Python compares the second element of the tuple - so item names must be comparable (both strings or both numbers) to avoid `TypeError`.

**Q8. bisect module - what is its purpose? Explain `bisect_left` vs `bisect_right`, and `insort()`. Why is it faster than searching a plain list?**

### Answer:

The `bisect` module maintains sorted lists efficiently. It provides two kinds of operations: finding the correct insertion position for a new value (without inserting), and actually inserting the value at that position - both using binary search internally, so both are `O(log n)` rather than `O(n)`.

**`bisect_left()` vs `bisect_right()`:**

Both functions find the position where a value should be inserted to keep the list sorted. The difference matters only when the value already exists in the list: 
`bisect_left(list, value)`: returns the position immediately before any existing equal values (leftmost valid insertion point). 

`bisect\_right(list, value):`returns the position immediately after any existing equal values (rightmost valid insertion point). This is the default for `bisect.bisect()` with no suffix.

```python
import bisect
scores = [50, 60, 60, 70, 80]
print(bisect.bisect_left(scores, 60)) # Output: 1
print(bisect.bisect_right(scores, 60)) # Output: 3
```

**`insort()`:**

`insort_left()` and `insort_right()` find the correct position using bisect and then insert the value there in a single operation. This is far more efficient than appending and re-sorting: insertion is `O(log n)` for finding the position + O(n) for the actual list shift, but it avoids the full `O(n log n)` re-sort. For lists that receive new items frequently, this is the right approach.

### Why faster than plain list search:

A plain list's in operator uses linear search: `O(n)`. bisect uses binary search: `O(log n)`. For a list of 1,000,000 items, linear search may check up to 1,000,000 items; `bisect` checks at most 20.

**Q9. queue module vs `collections.deque` - both provide queues. What is thread-safety? When must you use `queue.Queue` over deque? Explain the `None` sentinel pattern.**

### Answer: Thread-safety defined:

A thread is a unit of work that can run concurrently with other threads inside the same program. When two threads share a data structure and try to modify it simultaneously, a race condition can occur - both threads read the same state, both make a change, and one change overwrites the other, corrupting the data. A thread-safe data structure prevents this by ensuring that only one thread can modify it at any given moment, even if multiple threads attempt to do so simultaneously. 

`collections.deque` provides `O(1)` front/back operations and is thread-safe for simple append and pop operations at the ends. However, it does not provide higher-level coordination features like blocking until an item is available or signalling that a task is complete. `queue.Queue` adds these capabilities.

### When to use `queue.Queue`:

Use `queue.Queue` when:
  - (1) multiple threads share the same queue, 
  - (2) worker threads should block and wait when the queue is empty rather than spinning, 
  - (3) you need `task_done()` and `join()` to coordinate when all work is finished. Use `collections.deque` for single-threaded programs - it is faster and simpler.

### `None` as sentinel:

Worker threads typically run an infinite loop (`while True: task = queue.get()`). They need a signal to stop. The standard convention is to put `None` into the queue - each worker that receives None exits its loop. One `None` must be added per worker thread, so each thread receives exactly one stop signal.

```python
for _ in range(num_workers):
    task_queue.put(None) # one stop signal per worker
```

This approach requires no extra shared variables or flags, works reliably, and is easy to understand. `task_done()` must be called after processing each non-None task so that `queue.join()` can correctly detect when all work is complete.

**Q10. `lru_cache` - what is memoisation? Explain cache hits vs misses. What does `cache_info()` report? Compare `@lru_cache(maxsize=None)` vs `@cache` (Python 3.9+).**

### Answer:

Memoisation is an optimisation technique where a function remembers the results of previous calls. If the function is called again with the same arguments, it returns the stored result immediately instead of recalculating. This trades memory for speed - the function uses more memory (storing past results) but saves computation time.

### Why Fibonacci is the classic example:

The naive recursive `fib(n)` calls itself twice per invocation, producing an exponential call tree. `fib(32)` triggers roughly 2³² individual calls = `O(2ⁿ)`. With `@lru_cache`, each unique value of n is calculated only once and cached. `fib(32)` requires 33 calculations - one per unique n from 0 to 32 - reducing complexity to `O(n)`.

**cache\_info() fields:**

| Field | Meaning |
|---|---|
| hits | Times the result was found in the cache and returned instantly |
| misses | Times the result was not cached and had to be calculated fresh |
| maxsize | Maximum cache capacity (None = unlimited) |
| currsize | Number of results currently stored in the cache |

### `@lru_cache(maxsize=None)` vs `@cache`:

In Python 3.9+, `functools.cache` was introduced as a simpler alias for `@lru\_cache(maxsize=None)`. Both provide unlimited caching with no eviction. `@lru_cache` with a finite maxsize (e.g. maxsize=128) uses a Least Recently Used eviction policy - when the cache is full, the least recently accessed result is discarded to make room. Use `@cache` for simplicity when unlimited caching is acceptable; use `@lru_cache(maxsize=N)` when memory is constrained.


**Q11. `functools.partial()` - what problem does it solve? Explain with the tax calculator example. When is partial() preferred over a `lambda`?**


### Answer:

`partial()` solves the problem of argument repetition. When one argument to a function is always the same in a particular context, `partial()` creates a new function with that argument permanently fixed, so you never have to pass it again. This is called partial application.

### Tax calculator example:

```python
from functools import partial
def calculate_tax(amount, rate):
    return amount * rate

# GST on electronics is always 18% - fix rate
electronics_tax = partial(calculate_tax, rate=0.18)
print(electronics_tax(10000)) # Output: 1800.0
```

`electronics_tax` is a new function that only needs the amount argument. The `rate=0.18` is baked in. This is cleaner than passing `rate=0.18` every single call, and safer than using a global variable.

**`partial()` vs `lambda`:**

Both can fix arguments, but they differ in readability and capability. A lambda equivalent would be: `lambda amount: calculate_tax(amount, 0.18)`. For simple cases both work. `partial()` is preferred when: 
  - (1) you need to fix multiple arguments, 
  - (2) you are passing the function as an argument to another function and need a clean signature, 
  - (3) the fixed argument has a meaningful name (`rate=0.18` is self-documenting in a way that 0.18 alone is not). Lambdas are more flexible for applying arbitrary transformations, but `partial()` is more explicit about what it is doing.

**Q12. itertools: compare `chain()`, `islice()`, `groupby()`, `combinations()`, and `permutations()` - purpose, key behaviour, and a use case for each.**

### Answer:

  

| Function | Purpose | Key behaviour | Typical use case |
| --- | --- | --- | --- |
| chain(*iterables) | Join multiple iterables into one sequence | Produces items from each iterable in order without creating a new list in memory | Processing items from several lists as a single stream |
| islice(iterable, start, stop) | Slice an iterator without loading it into memory | Works on any iterator; does not support negative indices | Reading only the first N lines of a huge log file |
| groupby(iterable, key) | Group consecutive items with the same key | Data MUST be sorted by key first; creates new group each time key changes | Summarising records by category after sorting |
| combinations(iterable, r) | All ways to choose r items; order does not matter | No repetition; each item used once per combination | Generating all possible team pairings from a squad |
| permutations(iterable, r) | All ordered arrangements of r items | Order matters; same items in different order = different result | Generating all possible batting orders |






### Critical `groupby()` gotcha:

`groupby()` groups only consecutive equal keys. If data is `[A, A, B, A]`, it produces three groups: `A`, `B`, `A` - not two. Always sort by the key first if you want all items of the same category in one group. The group iterator returned by `groupby()` is consumed as you iterate - you must convert it to a list immediately if you need to use it more than once.

**Q13. `OrderedDict` - in Python 3.7+ regular dicts preserve insertion order. So why does `OrderedDict` still exist? What methods does it add that a plain dict cannot do?**

### Answer:

Since Python 3.7, the built-in dict guarantees insertion order as part of the language specification (not just as an implementation detail). For simple ordered storage, a plain dict is now sufficient and slightly faster than `OrderedDict`. However, `OrderedDict` still exists because it provides two additional methods that a plain dict cannot replicate without manual code:

**`move_to_end(key, last=True):`**

Moves an existing key to the very end of the dictionary (`last=True`, the default) or to the very beginning (`last=False`) in a single O(1) operation. With a plain dict, you must manually pop the key and re-insert it, which is three operations and creates a new key-value pair rather than moving the existing one.

**`popitem(last=True):`**

Removes and returns the last item (LIFO, `last=True`) or the first item (FIFO, `last=False`). Plain dict's `popitem()` always removes an arbitrary item in Python 3.7 and the last item from Python 3.8 - but it offers no option to remove the first item without converting to a list first.

### Equality semantics:

Two OrderedDicts with the same keys and values but in different insertion order are NOT equal. Two plain dicts with the same keys and values in different order ARE equal. This makes OrderedDict valuable when order is part of the data's meaning, not just a display preference. 

Summary: Use a plain dict (Python 3.7+) for all ordinary key-value storage. Switch to `OrderedDict` only when you need `move_to_end()`, order-sensitive equality comparisons, or `popitem(last=False)`.

**Q14. `enum` module - what are magic numbers and why are they harmful? How does Enum solve this? Show iteration and comparison. What does `auto()` do?** 

**Answer: Magic numbers:**

A magic number is an unexplained numeric (or string) literal used directly in code. For example: `if status == 2` - what does 2 mean? Is it 'shipped', 'cancelled', or something else? Anyone reading the code must hunt through comments or documentation to find out. Magic numbers make code fragile (change 2 to 3 in one place and forget another) and unreadable.

### How Enum solves this:

```python
from enum import Enum, auto
class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4

status = OrderStatus.SHIPPED
if status == OrderStatus.SHIPPED:
    print('Order is on the way')
```

Now `status == 2` is replaced by `status == OrderStatus.SHIPPED` - self-documenting, impossible to misread, and resistant to accidental reassignment (enum members are constants).

### Iteration:

An Enum is iterable. `for s in OrderStatus:` yields each member in definition order. Each member has `.name` (the string 'SHIPPED') and `.value` (the integer 2) attributes.

**`auto()`:**

`auto()` assigns values automatically in sequence starting from 1, so you do not need to number them manually. This prevents accidental duplicate values and makes adding new members simple - just add a new line without worrying about which number to assign.

**Q15. `reduce()` - how does it work step by step? Why did Python's creator move it to functools? When should a plain loop be preferred? Answer:**

`reduce(function, iterable)` repeatedly applies a two-argument function to collapse a sequence into a single value. It works left to right: take the first two items, apply the function, take the result and the next item, apply again, and so on until one value remains.

### Step-by-step trace for `reduce(multiply, [2, 3, 4, 5])`:

- Step 1: multiply(2, 3) = 6
- Step 2: multiply(6, 4) = 24
- Step 3: multiply(24, 5) = 120
- Result: 120

### Why Guido van Rossum moved it to functools:

Python's creator wrote publicly that he found `reduce()` hard to read in most real uses. For anything beyond simple addition or multiplication, a reader must mentally simulate the step-by-step accumulation to understand what the code does. The move from built-ins to functools in Python 3 was a deliberate style signal: `reduce()` is available when genuinely needed, but it should not be the default approach.

### When to use a plain loop instead:

A plain loop is always clearer when the accumulation logic is non-trivial, when a conditional is involved, or when the operation is not naturally associative. Compare:

```python
# reduce() version - requires mental simulation
result = reduce(lambda a, b: a * b, [2, 3, 4, 5])

# Loop version - immediately readable
result = 1
for n in [2, 3, 4, 5]:
    result *= n
```

Both produce 120. The loop version is readable by any programmer. Use `reduce()` only when the operation is so naturally associative (products, maximum, GCD) that the `reduce()` form is genuinely cleaner, and always add a comment explaining what it computes.

-----

**Q16. pickle vs json - compare format, type support, cross-language compatibility, and safety. When should each be used? What is the security risk with pickle?**

### Answer:

| Feature | pickle | json |
|---|---|---|
| File format | Binary - unreadable in a text | Plain text - human-readable in any editor |
|  | editor |  |
| Python types supported | All Python objects including custom | str, int, float, list, dict, bool, None only |
|  | classes, dataclasses, sets |  |
| Cross-language | No - Python only | Yes - works with JavaScript, Java, C#, Go, |
|  |  | and most others |
| Safety | UNSAFE to load from untrusted | Safe to load |
|  | sources |  |
| File extension convention | .pkl | .json |
| Speed | Slightly faster for complex Python | Slightly slower; simpler types are |
|  | objects | comparable |
| Human debugging | Cannot inspect file contents directly | Open in any text editor; fully readable |

### Security risk with pickle:

This is the most important fact to understand about pickle: a malicious `.pkl` file can execute arbitrary Python code when loaded. The pickle format stores instructions for reconstructing Python objects, and those instructions can include calls to `os.system()`, subprocess, or any other Python function. Never use `pickle.load()` on a file received from an untrusted source - email attachment, downloaded file, API response, or user upload.

### Practical rule:

Use json by default. It is safe, readable, and accepted by virtually every system. Switch to pickle only when you need to save a Python-specific object that json cannot represent - such as a custom class instance, a set, or a numpy array - and only when the saved file will be read back by your own code on a trusted system.

**Q17. Selection Sort - explain the sorted/unsorted partition, why swap count is `O(n)` (not `O(n²)`), and when this makes it preferable despite `O(n²)` comparisons.**

### Answer:

Selection Sort divides the list conceptually into two parts at each step: a sorted portion on the left (growing by one item per pass) and an unsorted portion on the right (shrinking by one item per pass). In each pass, the algorithm scans the entire unsorted portion to find the smallest item, then swaps it into the correct position at the boundary between the two portions.

### Why swaps are `O(n)` not `O(n²)`:

In each of the `n-1` passes, at most one swap occurs - the minimum item is swapped into its final position. Even in the worst case, the total number of swaps is at most `n-1 = O(n)`. By contrast, Bubble Sort can perform `O(n²)` swaps in the worst case (every adjacent pair out of order on every pass), and Insertion Sort performs `O(n²)` shifts.


### When Selection Sort is preferable:

Selection Sort is the right choice when the cost of writing (swapping) data is much higher than the cost of reading (comparing) it. Real scenarios include: writing to flash memory or EEPROM where each write operation degrades the storage medium, writing large records to disk where each swap involves significant I/O, or any embedded system where memory writes are slow and expensive. In these cases, minimising write operations (Selection Sort's O(n) swaps) is more important than minimising comparisons, making Selection Sort preferable despite its always-O(n²) comparison count.

**Q18. namedtuple deep-dive - what is a factory function? What does `__mro__` reveal? How does `_asdict()` work? Explain 'two names' in namedtuple('Student', [...]).**

### Answer: Factory function:

A factory function is a function that creates and returns a new class (or object). namedtuple() is a factory function because calling it produces a brand new class - not an instance of an existing class, but a class itself. This class is then used to create instances. The function 'manufactures' classes on demand.

### The two names:

```python
Record = namedtuple('Student', ['name', 'age'])
```

'`Student`' (the first argument) is the internal class name stored in `__name__`. `Record` (the variable) is the external reference by which the programmer accesses that class. Usually these match (`Student = namedtuple('Student', ...)`) for clarity. When they differ, the class still prints as `Student` but is accessed via `Record` - this can confuse debuggers and should generally be avoided.

### `__mro__` - Method Resolution Order:

`print(Student.__mro__)` 
outputs: (`<class '__main__.Student'>, <class 'tuple'>, <class 'object'>`). 

This confirms that Student inherits from the built-in tuple class. This is the meaning of 'tuple subclass' - namedtuple creates a new class that has all tuple behaviours (immutability, indexing, iteration, len()) plus named field access via dot notation.

### _asdict():

`_asdict()` converts a namedtuple instance into an `OrderedDict` (Python < 3.8) or a plain dict (Python 3.8+) mapping field names to values. This is the standard way to serialise a namedtuple to JSON or write it as a CSV row. Example:

```
s = Student(name='Anita', age=20)
print(s._asdict()) # {'name': 'Anita', 'age': 20}
```

**Q19. `time.perf_counter()` - why use it instead of `time.time()`? Why test with large inputs or loops? What does the timing graph shape reveal about O(n) vs O(log n) vs O(n²)?**

### Answer: `perf_counter()` vs `time.time()`:

`time.time()` returns the current wall-clock time (seconds since the Unix epoch). It has relatively low resolution and can be affected by system clock adjustments (NTP synchronisation, daylight saving changes).

`time.perf_counter()` returns a high-resolution performance counter with the highest resolution available on the platform. It is not affected by clock adjustments. Its absolute value is meaningless - only differences are used. For benchmarking code execution, `perf_counter()` is always preferred.


### Why large inputs or repeated loops:

A single operation often completes in microseconds or nanoseconds - far below the resolution of any timer. Measuring it directly would produce 0 or a meaningless result dominated by timer overhead. Two strategies solve this: 
  -  (1) test the operation on increasingly large inputs (as this chapter does, using sizes from 1,000 to 1,000,000), or 
  - (2) repeat a fast operation thousands of times and divide the total. 
 
 This chapter uses the first strategy - it plots search/sort time against input size to make the growth curve visible.

### What the graph shape reveals:

  

| Complexity | Graph shape | What you see |
| --- | --- | --- |
| O(n) | Straight line through origin | Time doubles when input doubles — linear growth |
| O(log n) | Curve that flattens sharply | Time barely increases even as input grows a thousandfold |
| O(n²) | Steep upward curve (parabola) | Time quadruples when input doubles — explosive growth |
| O(n log n) | Slightly curved line, just above O(n) | Near-linear but with a gentle upward bend |


**Q20. API and Standard Library - what is the 'batteries included' philosophy? How does importing work? Compare '`from module import X`' vs '`import module`' vs '`from module import *`', with best practice guidance.** 

**Answer: Batteries included:**

Python's 'batteries included' philosophy means that a standard Python installation comes with an extensive Standard Library covering most common programming needs - data structures, mathematics, file handling, networking, date/time, regular expressions, compression, cryptography, and much more. A programmer can accomplish a wide range of tasks without installing any third-party packages. The metaphor is that the device (Python) comes with its batteries (the Standard Library) already included - you do not need to buy them separately.

### How importing works:

The Standard Library is organised into modules - individual Python files containing related tools. A module is not available in your program until you explicitly import it. Three main forms:



  

| Import form | Example | What it does | Best practice verdict |
| --- | --- | --- | --- |
| import module | import collections | Makes the module available; access via module.ClassName | Good for clarity — reader sees where each name comes from |
| from module import X | from collections import Counter | Brings specific names directly into scope | Recommended — explicit, clear, avoids namespace pollution |
| from module import * | from collections import * | Imports everything in the module into current namespace | Avoid — pollutes namespace, makes origin of names unclear, can shadow existing names accidentally |



### Why `from module import *` is problematic:

If two modules both define a function called 'sort' and you do '`from moduleA import *` ' followed by '`from moduleB import *`', the second import silently overwrites the first. You now have moduleB's sort under the name sort and moduleA's is gone - with no error, no warning. In a large program this creates bugs that are very difficult to trace. The explicit form (from collections import Counter, deque) avoids this entirely by importing only what you specifically name.
