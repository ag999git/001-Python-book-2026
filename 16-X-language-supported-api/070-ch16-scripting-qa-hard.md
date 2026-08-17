






## Chapter 16 — Scripting Questions
Python Libraries for Data Structures and Algorithms
These 20 scripting questions are drawn directly from the topics in Chapter 17. Full answer scripts are provided below each question and are intended for the accompanying online resource. 

Tip: For each answer script, copy the code to a .py file and run it to see the output.

Part A — Searching Algorithms
#### Q1. 
Implement both `linear_search` and `binary_search`. Time each against list sizes [1K–1M] using `time.perf_counter()`. Print a table showing n, linear time, binary time, and speedup factor.

#### Answer script:

Q1 Answer: 
Linear Search vs Binary Search — O(n) vs O(log n)  This script builds two search functions, times them against the same list sizes, and prints a side-by-side comparison table. Key ideas:   - Linear search checks every element   → O(n)   - Binary search halves the search space → O(log n)   - Binary search REQUIRES a sorted list

```python
# Step 1 — Import required modules
import time, random

# Step 2 — Implement linear search (no sorting needed)
def linear_search(data, target):
    """Return True if target found, else False. Checks every item."""
    for item in data:
        if item == target:
            return True
    return False

# Step 3 — Implement binary search (list MUST be sorted first)
def binary_search(data, target):
    """Return True if target found using divide-and-conquer."""
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2   # Safe in Python — no integer overflow
        if data[mid] == target:
            return True
        elif target > data[mid]:
            left = mid + 1           # Discard left half
        else:
            right = mid - 1          # Discard right half
    return False

# Step 4 — Define test sizes and run timing experiment
sizes = [1_000, 10_000, 100_000, 500_000, 1_000_000]
target = -1   # Guaranteed NOT in data → worst-case scenario for both

print(f"{'n':>10} | {'Linear (s)':>12} | {'Binary (s)':>12} | {'Speedup':>10}")
print("-" * 52)

for n in sizes:
    data = [random.randint(1, 1_000_000) for _ in range(n)]
    sorted_data = sorted(data)   # Binary search needs sorted input

    # Time linear search
    t0 = time.perf_counter()
    linear_search(data, target)
    t_linear = time.perf_counter() - t0

    # Time binary search
    t1 = time.perf_counter()
    binary_search(sorted_data, target)
    t_binary = time.perf_counter() - t1

    speedup = t_linear / t_binary if t_binary > 0 else float('inf')
    print(f"{n:>10} | {t_linear:>12.6f} | {t_binary:>12.6f} | {speedup:>9.0f}x")

# Step 5 — Print Big-O summary
print()
print("Big-O reminder:")
print("  Linear  Search: O(n)     — comparisons grow with n")
print("  Binary  Search: O(log n) — 1,000,000 items ≈ only 20 comparisons")

```

```python
         n |   Linear (s) |   Binary (s) |    Speedup
----------------------------------------------------
      1000 |     0.000560 |     0.000006 |        93x
     10000 |     0.000192 |     0.000006 |        33x
    100000 |     0.003666 |     0.000008 |       447x
    500000 |     0.013425 |     0.000011 |      1178x
   1000000 |     0.025914 |     0.000010 |      2591x

Big-O reminder:
  Linear  Search: O(n)     — comparisons grow with n
  Binary  Search: O(log n) — 1,000,000 items ≈ only 20 comparisons

```



Part A — Sorting Algorithms
#### Q2. 
Code `bubble_sort` with an `already_sorted` early-exit flag. Run it on a worst-case (reverse-sorted) and best-case (sorted) list. Count and print total comparisons for various n to verify O(n²).
#### Answer script:

Q2 Answer: Bubble Sort — implementation with early-exit optimisation  Bubble sort compares neighbouring elements and swaps them if out of order. After each pass the largest unsorted element 'bubbles' to its correct position.  
Worst case:  O(n²) — list is reverse-sorted 
Best  case:  O(n)  — list is already sorted (with early-exit flag)  This script adds an 'already_sorted' flag that stops early when no swaps occurred in a pass — turning best-case into O(n). 

```python
# Step 1 — Bubble sort with early-exit optimisation
def bubble_sort(numbers):
    n = len(numbers)
    for pass_no in range(n - 1):
        already_sorted = True          # Assume sorted until a swap occurs
        # Inner loop: compare neighbours; stop early for already-sorted portion
        for i in range(n - pass_no - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]  # swap
                already_sorted = False # A swap happened → not sorted yet
        if already_sorted:             # No swaps in this pass → done early
            print(f"  Early exit after pass {pass_no + 1}")
            break
    return numbers

# Step 2 — Demonstrate on worst-case (reverse sorted) input
data_worst = [6, 5, 4, 3, 2, 1]
print("Worst case (reverse sorted):")
print("  Input: ", data_worst)
print("  Output:", bubble_sort(data_worst.copy()))

# Step 3 — Demonstrate on best-case (already sorted) input
data_best = [1, 2, 3, 4, 5, 6]
print("Best case (already sorted):")
print("  Input: ", data_best)
print("  Output:", bubble_sort(data_best.copy()))

# Step 4 — Count total comparisons to verify O(n²) derivation
def bubble_sort_count(numbers):
    """Returns (sorted list, total comparisons made)."""
    n = len(numbers)
    count = 0
    for pass_no in range(n - 1):
        for i in range(n - pass_no - 1):
            count += 1
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers, count

for size in [5, 10, 20]:
    import random
    sample = random.sample(range(100), size)
    _, comparisons = bubble_sort_count(sample)
    theoretical = size * (size - 1) // 2   # n*(n-1)/2 formula
    print(f"n={size}: actual comparisons={comparisons}, formula n(n-1)/2={theoretical}")
```

#### Output

```python
Worst case (reverse sorted):
  Input:  [6, 5, 4, 3, 2, 1]
  Output: [1, 2, 3, 4, 5, 6]
Best case (already sorted):
  Input:  [1, 2, 3, 4, 5, 6]
  Early exit after pass 1
  Output: [1, 2, 3, 4, 5, 6]
n=5: actual comparisons=10, formula n(n-1)/2=10
n=10: actual comparisons=45, formula n(n-1)/2=45
n=20: actual comparisons=190, formula n(n-1)/2=190

```


#### Q3. 
Implement `insertion_sort` using the shift (not swap) approach. Count shifts vs swaps compared to `bubble_sort` on the same random list. Explain why fewer writes matter in practice.
#### Answer script:

Q3 Answer: Insertion Sort — card-analogy implementation  Insertion sort works like sorting playing cards in your hand:   - Pick the next card   - Slide it left past any larger cards (shifting, not swapping)   - Place it in the correct position  Although worst-case is still O(n²), insertion sort:   1. Makes fewer writes than bubble sort (shifts, not swaps)   2. Is O(n) for nearly-sorted data   3. Is stable — equal elements keep their original order 

```python
# Step 1 — Implement insertion sort
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]          # The 'card' we are about to insert
        j = i - 1
        # Step 1a: Shift larger elements one position to the right
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]   # Shift (not swap — faster)
            j -= 1
        # Step 1b: Place the key in its correct position
        numbers[j + 1] = key
    return numbers

# Step 2 — Test with sample data
sample = [29, 10, 14, 37, 13]
print("Input: ", sample)
print("Sorted:", insertion_sort(sample.copy()))

# Step 3 — Compare shift count vs swap count
def insertion_sort_shifts(numbers):
    shifts = 0
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
            shifts += 1
        numbers[j + 1] = key
    return shifts

def bubble_sort_swaps(numbers):
    swaps = 0
    n = len(numbers)
    for _ in range(n - 1):
        for i in range(n - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swaps += 1
    return swaps

import random
test = random.sample(range(50), 10)
print(f"\nList: {test}")
print(f"Insertion sort shifts: {insertion_sort_shifts(test.copy())}")
print(f"Bubble    sort swaps:  {bubble_sort_swaps(test.copy())}")
print("Fewer writes → insertion sort faster in practice despite same O(n²)")
```

#### Output
```python
Input:  [29, 10, 14, 37, 13]
Sorted: [10, 13, 14, 29, 37]

List: [41, 14, 0, 49, 22, 36, 24, 48, 12, 46]
Insertion sort shifts: 20
Bubble    sort swaps:  20
Fewer writes → insertion sort faster in practice despite same O(n²)
```


Part A — Stacks and Queues (Manual Implementation)
#### Q4. 
Build a `Stack` class (LIFO) using a plain `list`. Simulate an undo-button. Then benchmark `list.pop(0)` vs `deque.popleft()` for N=100,000 front-removals and print the speedup.
#### Answer script:

Q4 Answer: Stack (LIFO) and the `pop(0)` performance trap  A Stack follows Last-In First-Out (LIFO) order. Built with a plain Python list:   push  → list.append()   O(1)   pop   → list.pop()      O(1)  ← from the END  Common mistake: list.pop(0) removes from the FRONT → O(n) because Python must shift every remaining element one place to the left.  Solution: collections.deque — a doubly-linked deque with O(1) appendleft() and popleft().

```python
from collections import deque
import time

# Step 1 — Stack using list (correct: push/pop at END)
class Stack:
    def __init__(self):
        self._data = []
    def push(self, item):
        self._data.append(item)    # O(1)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._data.pop()    # O(1) — removes from END
    def peek(self):
        return self._data[-1]
    def is_empty(self):
        return len(self._data) == 0
    def __repr__(self):
        return f"Stack({self._data})"

# Step 2 — Demonstrate undo-button simulation using a stack
actions = Stack()
actions.push("Type 'Hello'")
actions.push("Bold text")
actions.push("Insert image")
print("After 3 actions:", actions)
print("Undo:", actions.pop())   # Most recent first
print("Undo:", actions.pop())
print("After 2 undos:", actions)

# Step 3 — Prove pop(0) is O(n) — benchmark list.pop(0) vs deque.popleft()
N = 100_000

# Fill both structures
lst = list(range(N))
dq  = deque(range(N))

t0 = time.perf_counter()
for _ in range(N):
    lst.pop(0)               # O(n) — shifts all remaining items
t_list = time.perf_counter() - t0

dq = deque(range(N))         # Refill deque
t1 = time.perf_counter()
for _ in range(N):
    dq.popleft()             # O(1) — no shifting needed
t_deque = time.perf_counter() - t1

print(f"\nRemoving {N} items from the front:")
print(f"  list.pop(0):      {t_list:.4f} s  ← O(n) per call!")
print(f"  deque.popleft():  {t_deque:.4f} s  ← O(1) per call")
print(f"  Deque is {t_list/t_deque:.0f}x faster for front removal")
```

#### Output

```python
After 3 actions: Stack(["Type 'Hello'", 'Bold text', 'Insert image'])
Undo: Insert image
Undo: Bold text
After 2 undos: Stack(["Type 'Hello'"])

Removing 100000 items from the front:
  list.pop(0):      1.1456 s  ← O(n) per call!
  deque.popleft():  0.0561 s  ← O(1) per call
  Deque is 20x faster for front removal
```

#### Q5. 
Implement a FIFO queue using `deque`. Then build a producer-consumer simulation using `queue.Queue` with a `None` sentinel to signal end-of-work across two threads.
#### Answer script:

Q5 Answer: Queue (FIFO) — deque for single-thread, queue.Queue for threads  Queue = First-In First-Out (FIFO).   - Single-threaded programs: use collections.deque (fast, simple)   - Multi-threaded programs: MUST use queue.Queue (thread-safe blocking)  The None-sentinel pattern signals workers that no more items are coming.

```python
from collections import deque
from queue import Queue
import threading, time

# ─── Part A: FIFO Queue with deque (single-threaded) ───────────────────────
class FIFOQueue:
    def __init__(self):
        self._data = deque()
    def enqueue(self, item):
        self._data.append(item)       # Add to RIGHT (rear)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.popleft()   # Remove from LEFT (front) — O(1)
    def is_empty(self):
        return len(self._data) == 0
    def __repr__(self):
        return f"Queue(front→ {list(self._data)} ←rear)"

# Simulate a print spooler
spooler = FIFOQueue()
spooler.enqueue("Report.pdf")
spooler.enqueue("Invoice.docx")
spooler.enqueue("Photo.png")
print("Print queue:", spooler)
print("Printing:", spooler.dequeue())   # First job goes first
print("Printing:", spooler.dequeue())
print("Remaining:", spooler)

# ─── Part B: Thread-safe queue with None-sentinel pattern ──────────────────
print("\n--- Multi-threaded producer/consumer ---")

job_queue = Queue()

def producer():
    jobs = ["job-A", "job-B", "job-C"]
    for job in jobs:
        time.sleep(0.1)
        job_queue.put(job)
        print(f"  Produced: {job}")
    job_queue.put(None)   # Sentinel: tells consumer 'no more jobs'

def consumer():
    while True:
        item = job_queue.get()   # Blocks until item available
        if item is None:         # Sentinel received → stop
            print("  Consumer done.")
            break
        print(f"  Consumed: {item}")
        job_queue.task_done()

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start(); t2.start()
t1.join();  t2.join()
```
#### Output
```python
Print queue: Queue(front→ ['Report.pdf', 'Invoice.docx', 'Photo.png'] ←rear)
Printing: Report.pdf
Printing: Invoice.docx
Remaining: Queue(front→ ['Photo.png'] ←rear)

--- Multi-threaded producer/consumer ---
  Produced: job-A
  Consumed: job-A
  Produced: job-B  Consumed: job-B

  Produced: job-C
  Consumed: job-C
  Consumer done.
```

Part B — collections Module
#### Q6. 
Use `Counter` to find word frequencies in a sentence and the top-3 words. Use `defaultdict(list)` to group students by grade. Use `ChainMap` to layer session → user → default config settings.
#### Answer script:

Q6 Answer: collections — Counter, defaultdict, and ChainMap  collections module solves three common grouping/counting patterns:   Counter     — count occurrences of elements              (→ most_common)   defaultdict — auto-initialize missing keys               (→ no KeyError)   ChainMap    — merge multiple dicts without copying them  (→ layered lookup)

```python
from collections import Counter, defaultdict, ChainMap

# ─── Part A: Counter — word frequency ──────────────────────────────────────
# Step 1: Count words in a sentence
sentence = "to be or not to be that is the question to be"
word_count = Counter(sentence.split())
print("Word frequencies:")
print(word_count)

# Step 2: most_common() returns top-n most frequent elements
print("Top 3 words:", word_count.most_common(3))

# Step 3: Counter arithmetic — combine two counters
c1 = Counter("aabbcc")
c2 = Counter("bbccdd")
print("Union (c1 + c2):", c1 + c2)
print("Difference (c1 - c2):", c1 - c2)

# ─── Part B: defaultdict — group students by grade ─────────────────────────
""" defaultdict(list) creates an empty list automatically for each new key. Without it you would write:     if grade not in grade_groups:         grade_groups[grade] = []     grade_groups[grade].append(name) defaultdict removes that boilerplate entirely. """
students = [("Alice","A"), ("Bob","B"), ("Carol","A"), ("Dave","B"), ("Eve","A")]

grade_groups = defaultdict(list)  # Missing key → auto-create empty list
for name, grade in students:
    grade_groups[grade].append(name)

print("\nStudents by grade:")
for grade, names in sorted(grade_groups.items()):
    print(f"  Grade {grade}: {names}")

# defaultdict(int) → missing key starts at 0 (useful for counting)
char_count = defaultdict(int)
for ch in "mississippi":
    char_count[ch] += 1   # No KeyError even first time
print("\nChar count:", dict(char_count))

# ─── Part C: ChainMap — configuration layering ─────────────────────────────
defaults = {"theme": "light", "lang": "en", "font": "Arial"}
user_prefs = {"theme": "dark", "font": "Consolas"}
session   = {"lang": "fr"}

# ChainMap searches left-to-right; first match wins
config = ChainMap(session, user_prefs, defaults)
print("\nEffective configuration:")
for key in ["theme", "lang", "font"]:
    print(f"  {key}: {config[key]}")

# Writes go to the FIRST map only
config["theme"] = "high-contrast"
print("After update — session:", dict(session))
print("user_prefs unchanged:  ", dict(user_prefs))
```
#### Output

```python
Word frequencies:
Counter({'to': 3, 'be': 3, 'or': 1, 'not': 1, 'that': 1, 'is': 1, 'the': 1, 'question': 1})
Top 3 words: [('to', 3), ('be', 3), ('or', 1)]
Union (c1 + c2): Counter({'b': 4, 'c': 4, 'a': 2, 'd': 2})
Difference (c1 - c2): Counter({'a': 2})

Students by grade:
  Grade A: ['Alice', 'Carol', 'Eve']
  Grade B: ['Bob', 'Dave']

Char count: {'m': 1, 'i': 4, 's': 4, 'p': 2}

Effective configuration:
  theme: dark
  lang: fr
  font: Consolas
After update — session: {'lang': 'fr', 'theme': 'high-contrast'}
user_prefs unchanged:   {'theme': 'dark', 'font': 'Consolas'}
```

Part B — heapq Module
#### Q7. 
Using `heapq`, build a min-heap from a list of marks and pop all elements in ascending order. Simulate a max-heap using negation. Build a priority task queue using `(priority, task)` tuples.
#### Answer script:

Q7 Answer: heapq — min-heap and max-heap priority queues  A heap is a tree stored as a plain Python list where:   heap[0]           is always the SMALLEST element (min-heap)   parent of i       is at index (i-1) // 2   children of i     are at 2i+1 and 2i+2  Python's heapq module implements a MIN-heap. To simulate a MAX-heap, store values as negatives.  Common use: priority queues (process highest-priority task first).

```python
import heapq

# ─── Part A: Min-heap basics ────────────────────────────────────────────────
# Step 1: Build heap from a list
marks = [55, 92, 73, 41, 88, 60]
heapq.heapify(marks)    # Rearranges in-place → O(n)
print("Min-heap after heapify:", marks)
print("Smallest element (heap[0]):", marks[0])

# Step 2: Push a new element
heapq.heappush(marks, 35)
print("After pushing 35:", marks)
print("New minimum:", marks[0])

# Step 3: Pop elements in sorted (ascending) order
print("Popping all in ascending order:", end=" ")
temp = marks[:]
while temp:
    print(heapq.heappop(temp), end=" ")
print()

# ─── Part B: Max-heap using negation trick ──────────────────────────────────
"""
Max-heap trick: store every value as its negative.
  push max-heap: heappush(h, -value)
  peek max:      -h[0]
  pop  max:      -heappop(h)
"""
scores = [55, 92, 73, 41, 88]
max_heap = []
for score in scores:
    heapq.heappush(max_heap, -score)   # Negate before pushing

print("\nTop 3 scores (max-heap):")
for _ in range(3):
    print(" ", -heapq.heappop(max_heap))   # Negate when popping

# ─── Part C: Priority queue with tuples ─────────────────────────────────────
# Tuple: (priority, task_name) — heapq sorts by first element
task_queue = []
heapq.heappush(task_queue, (3, "Send email"))
heapq.heappush(task_queue, (1, "Fix crash bug"))    # Highest priority
heapq.heappush(task_queue, (2, "Write unit tests"))

print("\nProcessing tasks by priority:")
while task_queue:
    priority, task = heapq.heappop(task_queue)
    print(f"  Priority {priority}: {task}")

```

#### Output
```python
Min-heap after heapify: [41, 55, 60, 92, 88, 73]
Smallest element (heap[0]): 41
After pushing 35: [35, 55, 41, 92, 88, 73, 60]
New minimum: 35
Popping all in ascending order: 35 41 55 60 73 88 92 

Top 3 scores (max-heap):
  92
  88
  73

Processing tasks by priority:
  Priority 1: Fix crash bug
  Priority 2: Write unit tests
  Priority 3: Send email

```


Part B — bisect Module
#### Q8. 
Use `bisect.bisect_left` and `bisect_right` on a sorted list with duplicates. Use `insort()` to maintain a sorted leaderboard. Build a grade-boundary lookup table using `bisect` on threshold lists.
#### Answer script:

Q8 Answer: bisect — maintaining a sorted list without re-sorting  bisect keeps a sorted list sorted using binary search:   bisect_left(a, x)  — index where x would go (left of equal items)   bisect_right(a, x) — index where x would go (right of equal items)   insort(a, x)       — insert x at the correct position in O(n) total                        (O(log n) to find, O(n) to shift, but no full re-sort)  Use case: leaderboards, grade thresholds, real-time sorted streams. 

```python
import bisect

# ─── Part A: bisect_left vs bisect_right ────────────────────────────────────
scores = [10, 20, 30, 30, 30, 40, 50]

pos_left  = bisect.bisect_left(scores, 30)
pos_right = bisect.bisect_right(scores, 30)
print(f"Sorted list:  {scores}")
print(f"bisect_left (30):  index {pos_left}  → insert BEFORE existing 30s")
print(f"bisect_right(30):  index {pos_right}  → insert AFTER  existing 30s")

# ─── Part B: insort — insert while keeping list sorted ──────────────────────
leaderboard = [45, 60, 72, 88, 95]
print(f"\nLeaderboard before: {leaderboard}")
bisect.insort(leaderboard, 78)   # No need to sort again
print(f"After insort(78):   {leaderboard}")
bisect.insort(leaderboard, 55)
print(f"After insort(55):   {leaderboard}")

# ─── Part C: Grade boundary lookup using bisect ─────────────────────────────
"""
Classic bisect pattern: map a numeric score to a letter grade.
breakpoints = thresholds; grades = labels.
bisect.bisect(breakpoints, score) gives the correct label index.
"""
breakpoints = [40, 55, 65, 75, 85]
grades      = ["F", "D", "C", "B", "A-", "A"]

test_scores = [35, 50, 63, 74, 80, 92]
print("\nGrade lookup using bisect:")
for s in test_scores:
    grade = grades[bisect.bisect(breakpoints, s)]
    print(f"  Score {s:3d} → Grade {grade}")
```

#### Output
```python
Sorted list:  [10, 20, 30, 30, 30, 40, 50]
bisect_left (30):  index 2  → insert BEFORE existing 30s
bisect_right(30):  index 5  → insert AFTER  existing 30s

Leaderboard before: [45, 60, 72, 88, 95]
After insort(78):   [45, 60, 72, 78, 88, 95]
After insort(55):   [45, 55, 60, 72, 78, 88, 95]

Grade lookup using bisect:
  Score  35 → Grade F
  Score  50 → Grade D
  Score  63 → Grade C
  Score  74 → Grade B
  Score  80 → Grade A-
  Score  92 → Grade A
```


Part B — collections.OrderedDict
Q9. Demonstrate all extra methods `OrderedDict` provides over a plain `dict` (`move_to_end`, `popitem`). Build a working LRU cache class using `OrderedDict` with a fixed capacity and eviction on overflow.
Answer script:

Q9 Answer: OrderedDict — move_to_end and LRU Cache simulation  In Python 3.7+ regular dicts ALREADY preserve insertion order. OrderedDict still exists because it provides two extra methods:   move_to_end(key, last=True)  — move a key to the end (or front)   popitem(last=True)           — remove and return the last (or first) item  Classic use case: Least-Recently-Used (LRU) cache. 

```python
from collections import OrderedDict

# ─── Part A: move_to_end demonstration ──────────────────────────────────────
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print("Original order:", list(od.keys()))

od.move_to_end('b')              # Move 'b' to the LAST position
print("After move_to_end('b'):", list(od.keys()))

od.move_to_end('d', last=False)  # Move 'd' to the FIRST position
print("After move_to_end('d', last=False):", list(od.keys()))

# ─── Part B: LRU Cache simulation with OrderedDict ──────────────────────────
"""
LRU (Least Recently Used) Cache:
  - Stores up to 'capacity' items
  - When full: evict the LEAST recently used item
  - On access: move the item to 'most recently used' end
"""
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)   # Mark as most recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Evict LRU (oldest/first item)

    def __repr__(self):
        return f"LRU{list(self.cache.items())}"

lru = LRUCache(3)
lru.put("page1", "Home")
lru.put("page2", "About")
lru.put("page3", "Contact")
print("\nCache:", lru)

lru.get("page1")                  # Access page1 → moves to end (MRU)
lru.put("page4", "Products")     # Cache full → evicts page2 (LRU)
print("After accessing page1 and adding page4:", lru)
```
#### Output
```python
Original order: ['a', 'b', 'c', 'd']
After move_to_end('b'): ['a', 'c', 'd', 'b']
After move_to_end('d', last=False): ['d', 'a', 'c', 'b']

Cache: LRU[('page1', 'Home'), ('page2', 'About'), ('page3', 'Contact')]
After accessing page1 and adding page4: LRU[('page3', 'Contact'), ('page1', 'Home'), ('page4', 'Products')]
```

Part B — collections.namedtuple
#### Q10. 
Create a `namedtuple` called `Student`. Show field access by name and index. Use `_asdict()`, `_replace()`, and tuple unpacking. Print the MRO with `__mro__`. Compare memory size against an equivalent `dict`.
#### Answer script:

Q10 Answer: namedtuple — lightweight immutable records with named fields  namedtuple creates a class that is:   1. A subclass of tuple  (memory-efficient, immutable)   2. Fields accessed by NAME (readable) or index (compatible with tuple ops)  namedtuple('TypeName', ['field1', 'field2']) returns a CLASS (factory function). _asdict() converts an instance to an OrderedDict. _replace() returns a new instance with some fields changed. 

```python
from collections import namedtuple

# Step 1 — Create a namedtuple class (the 'factory')
# 'Student' appears twice: external class name, internal __name__ attribute
Student = namedtuple('Student', ['name', 'roll', 'marks', 'grade'])

# Step 2 — Create instances (immutable records)
s1 = Student(name="Anita",   roll=101, marks=88, grade="A")
s2 = Student(name="Pradeep", roll=102, marks=74, grade="B")

# Step 3 — Access fields by name (readable) or index (tuple-compatible)
print("Name:", s1.name)          # By name
print("Marks:", s1[2])           # By index (same as tuple)
print("Full record:", s1)

# Step 4 — _asdict(): convert to dict for JSON / display
print("As dict:", s1._asdict())

# Step 5 — _replace(): create modified copy (namedtuples are immutable)
s1_updated = s1._replace(marks=92, grade="A+")
print("Updated copy:", s1_updated)
print("Original unchanged:", s1)

# Step 6 — Tuple operations still work
print("Is tuple?", isinstance(s1, tuple))
name, roll, marks, grade = s1   # Unpacking
print(f"Unpacked — name={name}, roll={roll}")

# Step 7 — Memory efficiency vs dict
import sys
student_dict = {"name": "Anita", "roll": 101, "marks": 88, "grade": "A"}
print(f"\nnamedtuple size: {sys.getsizeof(s1)} bytes")
print(f"dict size:       {sys.getsizeof(student_dict)} bytes")

# Step 8 — __mro__ reveals inheritance chain
print("\nInheritance (MRO):", [c.__name__ for c in Student.__mro__])
# Output: ['Student', 'tuple', 'object']
```

#### Output
```python
Name: Anita
Marks: 88
Full record: Student(name='Anita', roll=101, marks=88, grade='A')
As dict: {'name': 'Anita', 'roll': 101, 'marks': 88, 'grade': 'A'}
Updated copy: Student(name='Anita', roll=101, marks=92, grade='A+')
Original unchanged: Student(name='Anita', roll=101, marks=88, grade='A')
Is tuple? True
Unpacked — name=Anita, roll=101

namedtuple size: 72 bytes
dict size:       184 bytes

Inheritance (MRO): ['Student', 'tuple', 'object']
```

Part B — dataclasses Module
#### Q11. 
Define a `@dataclass` `Student` with a default field. Add a `subjects` list using `field(default_factory=list)` and prove each instance gets its own list. Add a `password` field with `repr=False`. Make the class `frozen=True`.
#### Answer script:

Q11 Answer: dataclasses — auto-generated `__init__`, `__repr__`, and `__eq__`  @dataclass eliminates boilerplate. Python auto-generates:   `__init__`   — constructor from field annotations   
`__repr__`   — readable string representation
   `__eq__`     — equality comparison by field values  Key features demonstrated:     
   - default_factory — mutable defaults (lists, dicts) for each instance   
   - frozen=True     — immutable record (like namedtuple but with type hints)   
   - field(repr=False) — hide sensitive fields from print() 


```python
from dataclasses import dataclass, field

# ─── Part A: Basic dataclass ─────────────────────────────────────────────────
@dataclass
class Student:
    name:  str
    roll:  int
    marks: float = 0.0            # Default value
    grade: str   = "N/A"

s1 = Student("Anita", 101, 88.5, "A")
s2 = Student("Pradeep", 102)     # Uses defaults for marks and grade
print(s1)   # __repr__ auto-generated
print(s2)
print("Equal?", s1 == Student("Anita", 101, 88.5, "A"))   # __eq__ by fields

# ─── Part B: Mutable default with default_factory ────────────────────────────
"""
WRONG:  subjects: list = []   ← All instances share the SAME list!
CORRECT: subjects: list = field(default_factory=list)
         ← Each instance gets its OWN fresh empty list
"""
@dataclass
class CourseRecord:
    student_name: str
    subjects: list = field(default_factory=list)  # Separate list per instance

r1 = CourseRecord("Anita")
r2 = CourseRecord("Pradeep")
r1.subjects.append("Python")
r1.subjects.append("Data Structures")
print("\nAnita's subjects:", r1.subjects)
print("Pradeep's subjects (unaffected):", r2.subjects)

# ─── Part C: Hidden field with repr=False ─────────────────────────────────────
@dataclass
class User:
    username: str
    password: str = field(repr=False)  # Not shown when printed

u = User("admin", "secret123")
print("\nUser record:", u)   # password NOT displayed

# ─── Part D: Frozen (immutable) dataclass ────────────────────────────────────
@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(3.0, 4.0)
print("\nPoint:", p)
try:
    p.x = 10   # Raises FrozenInstanceError
except Exception as e:
    print("Cannot modify frozen dataclass:", type(e).__name__)
```
#### Output

```python
Student(name='Anita', roll=101, marks=88.5, grade='A')
Student(name='Pradeep', roll=102, marks=0.0, grade='N/A')
Equal? True

Anita's subjects: ['Python', 'Data Structures']
Pradeep's subjects (unaffected): []

User record: User(username='admin')

Point: Point(x=3.0, y=4.0)
Cannot modify frozen dataclass: FrozenInstanceError
```
Part B — enum Module
#### Q12. 
Define an `Enum` `OrderStatus` with 5 states. Use `auto()` to assign values automatically. Show member access by `.name` and `.value`, comparison, iteration over all members, and lookup by integer value.
#### Answer script:

Q12 Answer: enum — replacing magic numbers with named constants  'Magic numbers' like if status == 3 make code unreadable and error-prone. enum.Enum replaces them with named, type-safe constants.  Features:   Enum       — basic named constants   auto()     — auto-assign integer values   IntEnum    — enum members compare equal to int values   Iteration  — loop over all members with list(MyEnum)

```python
from enum import Enum, auto, IntEnum

# ─── Part A: Basic Enum — order status ──────────────────────────────────────
class OrderStatus(Enum):
    PENDING   = 1
    CONFIRMED = 2
    SHIPPED   = 3
    DELIVERED = 4
    CANCELLED = 5

order = OrderStatus.SHIPPED
print("Current status:", order)          # OrderStatus.SHIPPED
print("Name:", order.name)               # SHIPPED
print("Value:", order.value)             # 3

# Step — comparison (compare to enum member, not raw int)
if order == OrderStatus.SHIPPED:
    print("Your order is on its way!")

# ─── Part B: auto() — values assigned automatically ────────────────────────
class Direction(Enum):
    NORTH = auto()   # → 1
    SOUTH = auto()   # → 2
    EAST  = auto()   # → 3
    WEST  = auto()   # → 4

print("\nDirections:")
for d in Direction:
    print(f"  {d.name} = {d.value}")

# ─── Part C: IntEnum — enum that IS an int (legacy API compatibility) ────────
class HttpStatus(IntEnum):
    OK        = 200
    NOT_FOUND = 404
    ERROR     = 500

code = 404
print(f"\nIs 404 NOT_FOUND? {code == HttpStatus.NOT_FOUND}")  # True (IntEnum)

# ─── Part D: Lookup by value ─────────────────────────────────────────────────
status_code = 3
status = OrderStatus(status_code)   # Convert int → enum member
print(f"\nStatus for code {status_code}: {status.name}")
```

#### Output

```python
Current status: OrderStatus.SHIPPED
Name: SHIPPED
Value: 3
Your order is on its way!

Directions:
  NORTH = 1
  SOUTH = 2
  EAST = 3
  WEST = 4

Is 404 NOT_FOUND? True

Status for code 3: SHIPPED
```
Part B — functools.lru_cache
#### Q13. 
Compare `fib(35)` (plain recursion) vs `fib_cached(35)` (with `@lru_cache`) using `time.perf_counter()`. Print speedup and explain every field in `cache_info()` output: hits, misses, maxsize, currsize.
#### Answer script:

Q13 Answer: functools.lru_cache — memoisation to eliminate repeated computation  Memoisation: remember (cache) results of expensive function calls. On repeated calls with the same arguments → return cached result instantly.  @lru_cache(maxsize=None) — unlimited cache size (@cache in Python 3.9+) cache_info() — shows hits, misses, maxsize, currsize  Classic example: Fibonacci — without cache, recursion is exponential O(2^n). With cache, each n is computed ONCE → O(n).

```python
from functools import lru_cache
import time

# ─── Part A: Without cache — exponential growth ──────────────────────────────
def fib(n):
    """Standard recursive Fibonacci — recomputes the same values repeatedly."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# ─── Part B: With lru_cache — each value computed only once ──────────────────
@lru_cache(maxsize=None)
def fib_cached(n):
    """Cached Fibonacci — result stored after first computation."""
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

# Step 1 — Benchmark both versions
N = 35

t0 = time.perf_counter()
result_plain = fib(N)
t_plain = time.perf_counter() - t0

t1 = time.perf_counter()
result_cached = fib_cached(N)
t_cached = time.perf_counter() - t1

print(f"fib({N}) = {result_plain}")
print(f"Without cache: {t_plain:.5f} s")
print(f"With    cache: {t_cached:.7f} s")
print(f"Speedup: ~{t_plain/t_cached:.0f}x faster")

# Step 2 — Inspect cache statistics
info = fib_cached.cache_info()
print(f"\nCache info: {info}")
print(f"  hits    = {info.hits}    (returned from cache — no recalculation)")
print(f"  misses  = {info.misses}   (computed fresh and stored)")
print(f"  currsize= {info.currsize} (unique values now stored in cache)")

# Step 3 — Confirm cache is working: second call is instant
t2 = time.perf_counter()
fib_cached(N)
t2_elapsed = time.perf_counter() - t2
print(f"\nSecond call for fib({N}): {t2_elapsed:.9f} s  (pure cache hit)")
```

#### Output

```python
fib(35) = 9227465
Without cache: 2.19690 s
With    cache: 0.0021043 s
Speedup: ~1044x faster

Cache info: CacheInfo(hits=33, misses=36, maxsize=None, currsize=36)
  hits    = 33    (returned from cache — no recalculation)
  misses  = 36   (computed fresh and stored)
  currsize= 36 (unique values now stored in cache)

Second call for fib(35): 0.000087100 s  (pure cache hit)
```

Part B — functools.partial and reduce
#### Q14. 
Use `partial()` to create `gst_electronics` (18%) and `gst_food` (5%) from a `calculate_tax(amount, rate)` function. Use `reduce()` to multiply [2,3,4,5] step by step and print each intermediate result. Show why a plain loop is often clearer.
#### Answer script:

Q14 Answer: functools.partial() and reduce()  partial() — pre-fill one or more arguments of a function,             creating a new function with a shorter signature.             Useful when passing a function as a callback but the             receiver expects fewer parameters.  reduce()   — repeatedly apply a two-argument function to combine              items in an iterable into a single value.              Moved from built-ins to functools in Python 3 (style decision). 

```python
from functools import partial, reduce

# ─── Part A: partial() — tax calculator ─────────────────────────────────────
def calculate_tax(amount, rate):
    """Return tax amount for a given purchase amount and tax rate."""
    return amount * rate

# Create specialised functions with rate permanently fixed
gst_electronics = partial(calculate_tax, rate=0.18)   # 18% GST
gst_food        = partial(calculate_tax, rate=0.05)   # 5% GST

amounts = [10_000, 25_000, 5_000]
print("Electronics tax (18% GST):")
for amt in amounts:
    print(f"  ₹{amt:,} → tax = ₹{gst_electronics(amt):,.2f}")

print("Food tax (5% GST):")
for amt in amounts:
    print(f"  ₹{amt:,} → tax = ₹{gst_food(amt):,.2f}")

# ─── Part B: partial() for sorting — key function with extra argument ────────
def compare_by_field(record, field):
    return record[field]

students = [{"name": "Anita", "marks": 88},
            {"name": "Bob",   "marks": 74},
            {"name": "Carol", "marks": 95}]

by_marks = partial(compare_by_field, field="marks")
students.sort(key=by_marks, reverse=True)
print("\nStudents sorted by marks (descending):")
for s in students:
    print(f"  {s['name']}: {s['marks']}")

# ─── Part C: reduce() — step-by-step ────────────────────────────────────────
def multiply(a, b):
    return a * b

data = [2, 3, 4, 5]
result = reduce(multiply, data)
# Working: 2*3=6 → 6*4=24 → 24*5=120
print(f"\nreduce(multiply, {data}) = {result}")

# Compare reduce vs plain loop (readability)
result_loop = 1
for n in data:
    result_loop *= n
print(f"Loop  result: {result_loop}  (usually clearer than reduce)")
```

#### Output

```python
Electronics tax (18% GST):
  ₹10,000 → tax = ₹1,800.00
  ₹25,000 → tax = ₹4,500.00
  ₹5,000 → tax = ₹900.00
Food tax (5% GST):
  ₹10,000 → tax = ₹500.00
  ₹25,000 → tax = ₹1,250.00
  ₹5,000 → tax = ₹250.00

Students sorted by marks (descending):
  Carol: 95
  Anita: 88
  Bob: 74

reduce(multiply, [2, 3, 4, 5]) = 120
Loop  result: 120  (usually clearer than reduce)

```

Part B — itertools (chain, islice, groupby)
#### Q15. 
Use `chain()` to merge two lists, a tuple, and a `range` into one iterable. Use `islice()` to take 10 items from an infinite generator. Use `groupby()` (with prior sort) to group employees by department.
#### Answer script:

Q15 Answer: itertools — chain(), islice(), and groupby()  itertools provides memory-efficient 'lazy' iterators — items are produced ONE AT A TIME rather than loading the whole collection.  chain()   — concatenate multiple iterables without creating a new list islice()  — slice an iterable without materialising it first groupby() — group CONSECUTIVE equal-key items (sort first!) 

```python
from itertools import chain, islice, groupby

# ─── Part A: chain() — combine multiple iterables ────────────────────────────
sem1 = ["Python", "Maths"]
sem2 = ("Physics", "Chemistry")
sem3 = range(1, 4)           # Range object

all_subjects = chain(sem1, sem2, sem3)
print("Chained subjects:", list(all_subjects))
# No new list created — items produced one by one

# chain.from_iterable — useful when you have a list of lists
nested = [["a", "b"], ["c", "d"], ["e"]]
flat = list(chain.from_iterable(nested))
print("Flattened:", flat)

# ─── Part B: islice() — lazy slicing ─────────────────────────────────────────
def infinite_counter(start=0):
    """An infinite generator — produces integers forever."""
    n = start
    while True:
        yield n
        n += 1

# Take only the first 10 from an infinite sequence
first_10 = list(islice(infinite_counter(100), 10))
print("\nFirst 10 from infinite counter:", first_10)

# islice with start, stop, step (like regular slice)
every_third = list(islice(range(50), 0, 20, 3))  # Start=0, stop=20, step=3
print("Every 3rd item (0 to 20):", every_third)

# ─── Part C: groupby() — group sorted data ───────────────────────────────────
"""
IMPORTANT: groupby() only groups CONSECUTIVE identical keys.
Always sort the data BEFORE calling groupby(), unless your data
is already sorted by the grouping key.
"""
employees = [
    {"name": "Alice",   "dept": "Engineering"},
    {"name": "Bob",     "dept": "Engineering"},
    {"name": "Carol",   "dept": "HR"},
    {"name": "Dave",    "dept": "HR"},
    {"name": "Eve",     "dept": "Finance"},
]

# Step 1: Sort by key BEFORE groupby
employees.sort(key=lambda e: e["dept"])

# Step 2: Group and display
print("\nEmployees by department:")
for dept, group in groupby(employees, key=lambda e: e["dept"]):
    names = [e["name"] for e in group]
    print(f"  {dept}: {names}")
```

#### Output

```python
Chained subjects: ['Python', 'Maths', 'Physics', 'Chemistry', 1, 2, 3]
Flattened: ['a', 'b', 'c', 'd', 'e']

First 10 from infinite counter: [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
Every 3rd item (0 to 20): [0, 3, 6, 9, 12, 15, 18]

Employees by department:
  Engineering: ['Alice', 'Bob']
  Finance: ['Eve']
  HR: ['Carol', 'Dave']
```

Part B — itertools (product, combinations, permutations)
#### Q16. 
Generate all `combinations(players, 3)` for a cricket team of 5. Generate all `permutations` of a top-3 batting order. Generate all 3-digit `product` PINs from digits [0,1,2]. Print the total count for each.
#### Answer script:

Q16 Answer: itertools — product(), combinations(), and permutations()  These three functions cover combinatorial generation:  combinations(items, r)      — choose r items; ORDER does NOT matter; no repetition permutations(items, r)      — all ordered arrangements; no repetition product(items, repeat=r)    — Cartesian product; ORDER matters; WITH repetition  Memory-efficient: all return iterators, not lists.

```python
from itertools import combinations, permutations, product

# ─── Part A: combinations — cricket team selection ────────────────────────────
players = ["Rohit", "Kohli", "Dhoni", "Bumrah", "Jadeja"]

# Choose 3 from 5 for a batting lineup (order does not matter)
teams = list(combinations(players, 3))
print(f"Possible batting combinations (C(5,3) = {len(teams)}):")
for t in teams:
    print(" ", t)

# ─── Part B: permutations — batting order ────────────────────────────────────
top3 = ["Rohit", "Kohli", "Dhoni"]
orders = list(permutations(top3))
print(f"\nBatting orders for top-3 (3! = {len(orders)}):")
for o in orders:
    print(" ", o)

# ─── Part C: product — PIN code generator ────────────────────────────────────
digits = [0, 1, 2]
pins = list(product(digits, repeat=3))   # 3-digit PINs from digits 0-2
print(f"\nAll 3-digit PINs from digits {digits} ({len(pins)} total):")
print(pins)

# ─── Part D: Summary table ────────────────────────────────────────────────────
print("""
┌─────────────────────────┬──────────────────┬───────────────────┐
│ Function                │ Order matters?   │ Items reused?     │
├─────────────────────────┼──────────────────┼───────────────────┤
│ combinations(items, r)  │ No               │ No                │
│ permutations(items, r)  │ Yes              │ No                │
│ product(items, repeat=r)│ Yes              │ Yes               │
└─────────────────────────┴──────────────────┴───────────────────┘
""")
```

#### Output

```python
Possible batting combinations (C(5,3) = 10):
  ('Rohit', 'Kohli', 'Dhoni')
  ('Rohit', 'Kohli', 'Bumrah')
  ('Rohit', 'Kohli', 'Jadeja')
  ('Rohit', 'Dhoni', 'Bumrah')
  ('Rohit', 'Dhoni', 'Jadeja')
  ('Rohit', 'Bumrah', 'Jadeja')
  ('Kohli', 'Dhoni', 'Bumrah')
  ('Kohli', 'Dhoni', 'Jadeja')
  ('Kohli', 'Bumrah', 'Jadeja')
  ('Dhoni', 'Bumrah', 'Jadeja')

Batting orders for top-3 (3! = 6):
  ('Rohit', 'Kohli', 'Dhoni')
  ('Rohit', 'Dhoni', 'Kohli')
  ('Kohli', 'Rohit', 'Dhoni')
  ('Kohli', 'Dhoni', 'Rohit')
  ('Dhoni', 'Rohit', 'Kohli')
  ('Dhoni', 'Kohli', 'Rohit')

All 3-digit PINs from digits [0, 1, 2] (27 total):
[(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0), (2, 2, 1), (2, 2, 2)]

┌─────────────────────────┬──────────────────┬───────────────────┐
│ Function                │ Order matters?   │ Items reused?     │
├─────────────────────────┼──────────────────┼───────────────────┤
│ combinations(items, r)  │ No               │ No                │
│ permutations(items, r)  │ Yes              │ No                │
│ product(items, repeat=r)│ Yes              │ Yes               │
└─────────────────────────┴──────────────────┴───────────────────┘
```

Part A — Selection Sort
#### Q17. 
Implement `selection_sort` with a trace that prints which minimum was found and where it was placed each pass. Count swaps and compare against `bubble_sort` on the same random list. Explain why selection sort has O(n) swaps.
#### Answer script:

Q17 Answer: Selection Sort — O(n²) comparisons but only O(n) swaps  Selection sort maintains two partitions:   LEFT  — sorted partition (grows by 1 each pass)   RIGHT — unsorted partition (shrinks by 1 each pass)  Each pass: find the MINIMUM in the unsorted partition and swap it            to the boundary of the sorted partition.  Key advantage over Bubble Sort:   Bubble Sort: O(n²) swaps in worst case   Selection Sort: exactly n-1 swaps (each item moves to final place once)   → Better when writes are expensive (e.g., flash memory)

```python
# Step 1 — Selection sort with step-by-step trace
def selection_sort(data, trace=False):
    n = len(data)
    swap_count = 0
    for i in range(n - 1):
        # Find minimum in the unsorted portion [i .. n-1]
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        # Swap minimum into its final sorted position
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            swap_count += 1
        if trace:
            print(f"  Pass {i+1}: {data}  (min={data[i]} placed at index {i})")
    return data, swap_count

# Step 2 — Demonstrate with trace
sample = [64, 25, 12, 22, 11]
print("Input:", sample)
sorted_data, swaps = selection_sort(sample.copy(), trace=True)
print("Sorted:", sorted_data)
print(f"Total swaps: {swaps}  (max n-1 = {len(sample)-1})")

# Step 3 — Compare swap counts: Bubble vs Selection
import random

def bubble_swap_count(data):
    data = data[:]
    swaps = 0
    n = len(data)
    for _ in range(n - 1):
        for i in range(n - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swaps += 1
    return swaps

test = random.sample(range(100), 20)
_, sel_swaps = selection_sort(test.copy())
bub_swaps    = bubble_swap_count(test)

print(f"\nFor a random list of 20 elements:")
print(f"  Selection sort swaps: {sel_swaps}  (≤ n-1 = 19)")
print(f"  Bubble    sort swaps: {bub_swaps}  (can be much larger)")
```

#### Output
```python
Input: [64, 25, 12, 22, 11]
  Pass 1: [11, 25, 12, 22, 64]  (min=11 placed at index 0)
  Pass 2: [11, 12, 25, 22, 64]  (min=12 placed at index 1)
  Pass 3: [11, 12, 22, 25, 64]  (min=22 placed at index 2)
  Pass 4: [11, 12, 22, 25, 64]  (min=25 placed at index 3)
Sorted: [11, 12, 22, 25, 64]
Total swaps: 3  (max n-1 = 4)

For a random list of 20 elements:
  Selection sort swaps: 19  (≤ n-1 = 19)
  Bubble    sort swaps: 113  (can be much larger)
```
Part B — Data Serialisation (pickle and json)
#### Q18. 
Use `pickle` to save and load a dict containing a `datetime` object. Use `json` for the same dict (with datetime converted to string). Show what `json.dumps/loads` does on a plain dict. Demonstrate the `TypeError` when json encounters a datetime.
#### Answer script:

Q18 Answer: pickle vs json — serialisation, differences, and security  Serialisation: convert Python objects to bytes/text for storage or transfer.  pickle — binary, Python-only, supports ALL Python types json   — text, universal, limited to basic types (str/int/float/list/dict/bool)  SECURITY: Never unpickle data from untrusted sources.           pickle can execute arbitrary code during loading.           json is always safe to load.

```python
import pickle, json, os

# ─── Part A: Saving and loading with pickle ──────────────────────────────────
student = {
    "name":    "Anita",
    "age":     20,
    "marks":   [85, 90, 78],
    "active":  True
}

# Save (pickle.dump → binary file mode "wb")
with open("student.pkl", "wb") as f:
    pickle.dump(student, f)
print("Pickled successfully.")

# Load (pickle.load → binary file mode "rb")
with open("student.pkl", "rb") as f:
    loaded_pkl = pickle.load(f)
print("Unpickled:", loaded_pkl)

# ─── Part B: Saving and loading with json ────────────────────────────────────
with open("student.json", "w") as f:
    json.dump(student, f, indent=4)   # indent=4 → human-readable
print("\nJSON saved successfully.")

with open("student.json", "r") as f:
    loaded_json = json.load(f)
print("JSON loaded:", loaded_json)

# ─── Part C: json.dumps / json.loads (string, not file) ─────────────────────
json_string = json.dumps(student)
print("\nJSON string:", json_string)
parsed = json.loads(json_string)
print("Parsed back:", parsed)

# ─── Part D: What json CANNOT handle (but pickle can) ───────────────────────
from datetime import datetime
data_with_datetime = {"event": "Exam", "date": datetime(2025, 12, 1)}

# pickle handles datetime natively
pkl_bytes = pickle.dumps(data_with_datetime)
print("\nPickle handles datetime:", pickle.loads(pkl_bytes))

# json raises TypeError for datetime
try:
    json.dumps(data_with_datetime)
except TypeError as e:
    print("JSON cannot handle datetime:", e)

# Workaround: convert to string first
data_str_date = {"event": "Exam", "date": str(datetime(2025, 12, 1))}
print("JSON with date as string:", json.dumps(data_str_date))

# Cleanup
os.remove("student.pkl")
os.remove("student.json")
```

#### Output
```python
Pickled successfully.
Unpickled: {'name': 'Anita', 'age': 20, 'marks': [85, 90, 78], 'active': True}

JSON saved successfully.
JSON loaded: {'name': 'Anita', 'age': 20, 'marks': [85, 90, 78], 'active': True}

JSON string: {"name": "Anita", "age": 20, "marks": [85, 90, 78], "active": true}
Parsed back: {'name': 'Anita', 'age': 20, 'marks': [85, 90, 78], 'active': True}

Pickle handles datetime: {'event': 'Exam', 'date': datetime.datetime(2025, 12, 1, 0, 0)}
JSON cannot handle datetime: Object of type datetime is not JSON serializable
JSON with date as string: {"event": "Exam", "date": "2025-12-01 00:00:00"}
```


Part B — collections.deque
#### Q19. 
Demonstrate all key `deque` operations: `append`, `appendleft`, `pop`, `popleft`, `rotate(-1)` for round-robin scheduling, and `maxlen=5` for a sliding-window log. Benchmark `appendleft` vs `list.insert(0,x)` for N=200,000.
#### Answer script:

Q19 Answer: collections.deque — double-ended queue with O(1) ends  deque (Doubly-Ended QUEue) supports O(1) append/pop at BOTH ends. Key methods:   append(x)       — add to right   appendleft(x)   — add to left   pop()           — remove from right   popleft()       — remove from left   rotate(n)       — rotate right n steps (negative = left)   maxlen=N        — fixed-size sliding window; old items auto-discarded  This script demonstrates all key operations and the sliding-window pattern.

```python
from collections import deque

# ─── Part A: Basic deque operations ─────────────────────────────────────────
dq = deque([10, 20, 30])
dq.append(40)        # Right end
dq.appendleft(5)     # Left end — O(1), unlike list.insert(0, x) which is O(n)
print("After appends:", list(dq))   # [5, 10, 20, 30, 40]

dq.pop()             # Remove from right
dq.popleft()         # Remove from left
print("After pops:  ", list(dq))   # [10, 20, 30]

# ─── Part B: rotate() — circular buffer / round-robin simulation ─────────────
tasks = deque(["Task-A", "Task-B", "Task-C", "Task-D"])
print("\nRound-robin scheduling:")
for _ in range(6):
    current = tasks[0]
    print(f"  Processing: {current}")
    tasks.rotate(-1)  # Move current to the END (rotate left by 1)

# ─── Part C: maxlen — sliding window (last N log lines) ─────────────────────
"""
maxlen creates a bounded deque. When full, adding to the right
automatically removes from the left — perfect for a 'last N' window.
"""
log_window = deque(maxlen=5)   # Keep only the last 5 log entries

log_entries = [f"Log line {i}" for i in range(1, 11)]
for entry in log_entries:
    log_window.append(entry)

print("\nLast 5 log entries (sliding window):")
for line in log_window:
    print(" ", line)

# ─── Part D: Performance proof — appendleft vs insert(0) ────────────────────
import time
N = 200_000

lst = []
t0 = time.perf_counter()
for i in range(N):
    lst.insert(0, i)         # O(n) — shifts all existing elements
t_list = time.perf_counter() - t0

dq2 = deque()
t1 = time.perf_counter()
for i in range(N):
    dq2.appendleft(i)        # O(1) — no shifting needed
t_deque = time.perf_counter() - t1

print(f"\nFront-inserting {N} items:")
print(f"  list.insert(0,x): {t_list:.3f} s")
print(f"  deque.appendleft: {t_deque:.3f} s  (~{t_list/t_deque:.0f}x faster)")
```

#### Output
```python
After appends: [5, 10, 20, 30, 40]
After pops:   [10, 20, 30]

Round-robin scheduling:
  Processing: Task-A
  Processing: Task-B
  Processing: Task-C
  Processing: Task-D
  Processing: Task-A
  Processing: Task-B

Last 5 log entries (sliding window):
  Log line 6
  Log line 7
  Log line 8
  Log line 9
  Log line 10
```


Synthesis — Big-O Timing and Measurement
#### Q20. 
Time `linear_search` (O(n)), `binary_search` (O(log n)), and `bubble_sort` on 500 elements (O(n²)) across sizes [500–10K] using `time.perf_counter()`. Print a comparison table and include a Mermaid flowchart of the measurement methodology.
#### Answer script:

Q20 Answer: time.perf_counter() — measuring and comparing algorithm complexity  time.perf_counter() is a high-precision monotonic clock used to time code. It does NOT return wall-clock time — only differences are meaningful.  This script measures and compares O(n), O(log n), and O(n²) algorithms against increasing input sizes, then prints an ASCII plot and a Mermaid flowchart of the measurement methodology.

```python
import time, random, math

# ─── Step 1: Define one representative function for each complexity ───────────
def linear_search(data, target):       # O(n)
    for item in data:
        if item == target: return True
    return False

def binary_search(data, target):       # O(log n)  — data must be sorted
    lo, hi = 0, len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target: return True
        elif target > data[mid]: lo = mid + 1
        else: hi = mid - 1
    return False

def bubble_sort(data):                 # O(n²)
    data = data[:]
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# ─── Step 2: Run timing experiments ──────────────────────────────────────────
sizes = [500, 1_000, 2_000, 5_000, 10_000]
results = {"O(n)": [], "O(logn)": [], "O(n^2)": []}

for n in sizes:
    data   = [random.randint(1, n * 10) for _ in range(n)]
    sorted_data = sorted(data)
    target = -1   # Worst case: not found

    t0 = time.perf_counter()
    linear_search(data, target)
    results["O(n)"].append(time.perf_counter() - t0)

    t1 = time.perf_counter()
    binary_search(sorted_data, target)
    results["O(logn)"].append(time.perf_counter() - t1)

    t2 = time.perf_counter()
    bubble_sort(data[:500])   # Limit to 500 to avoid very long wait
    results["O(n^2)"].append(time.perf_counter() - t2)

# ─── Step 3: Print comparison table ──────────────────────────────────────────
print(f"{'n':>8} | {'O(n) s':>10} | {'O(logn) s':>12} | {'O(n²) s':>10}")
print("-" * 50)
for i, n in enumerate(sizes):
    print(f"{n:>8} | {results['O(n)'][i]:>10.6f} | "
          f"{results['O(logn)'][i]:>12.8f} | {results['O(n^2)'][i]:>10.6f}")
```

#### Output
```python
       n |     O(n) s |    O(logn) s |    O(n²) s
--------------------------------------------------
     500 |   0.000016 |   0.00000500 |   0.016795
    1000 |   0.000022 |   0.00000430 |   0.010956
    2000 |   0.000041 |   0.00000380 |   0.013063
    5000 |   0.000134 |   0.00000520 |   0.012631
   10000 |   0.000235 |   0.00000630 |   0.040842
```
