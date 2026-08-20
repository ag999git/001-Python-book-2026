


## Exercise: Convert a NamedTuple into a Dictionary

Create a `Student` namedtuple with following 3 fields:

```python
name, age, course
```

Create a student record and convert it into a dictionary.

Example:

```python
s1 = Student("Anita", 20, "Python")
```
To create a dictionary whose keys are the field names `name, age, course` and whose values are `"Anita", 20, "Python"`
Expected output:

```python
{ 'name': 'Anita', 'age': 20, 'course': 'Python'}
```

**Hint:** Use `_fields` and `zip()`.



----------

## Solution Code

```python
from collections import namedtuple


# Create namedtuple class
Student = namedtuple(
    "Student",                 # Name of the namedtuple class
    ["name", "age", "course"]  # Adding fields "name", "age", and "course"
)


# Create object
s1 = Student(
    "Anita",
    20,
    "Python"
)


# Convert namedtuple to dictionary
# s1._fields returns a tuple of field names ('name', 'age', 'course')
# s1 is the namedtuple object, which can be treated like a tuple to get the values ('Anita', 20, 'Python')
student_dict = dict(
    zip(s1._fields, s1)
)


print(student_dict)
```

Output:

```
{'name': 'Anita','age': 20,'course': 'Python'}
```

----------

## Optional extension task

Add another student:

```python
Student("Rahul", 22, "Java")
```

Store both records in a list and convert each record into a dictionary.

Expected output:

```python
[ {'name':'Anita','age':20,'course':'Python'},
{'name':'Rahul','age':22,'course':'Java'}]
```

----------

This fits well after `_fields` because you can see a practical reason for a namedtuple to know its own structure.
