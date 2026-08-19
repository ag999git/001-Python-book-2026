

Conceptual Questions — Pytest

**1. What is unit testing? Why do we test code even when the program runs correctly?**
Answer:
Unit testing means testing small independent parts of a program to check whether they behave as expected. A program may run successfully, but it may still contain hidden logical errors.
Testing helps us:
•	verify that functions return correct results
•	detect future changes that break old behaviour
•	check edge cases
•	confirm that error conditions are handled properly
A unit test usually follows this idea:
Arrange → Act → Assert
Example:
```python
# Arrange
number = 10

# Act
result = square(number)

# Assert
assert result == 100
```
The purpose of testing is not only finding current mistakes but also protecting the program from future mistakes.
________________________________________
**2. How does pytest discover test files and test functions automatically?**
Answer:
Pytest does not run every Python file. It follows naming rules to locate tests.
Typical rules:

| Item | Naming pattern |
| --- | --- |
| Test file | test_*.py or *_test.py |
| Test function | starts with test_ |
| Test class | starts with Test |


Example:
```python
project/
│
├── calculator.py
│
└── test_calculator.py
        |
        └── test_add()
 ```
Execution flow:
![Execution flow](/resources/ch16-pytest-100-conceptual-qa2.png)
This automatic discovery removes the need to manually call every test function.
________________________________________
**3. What is the role of assert in pytest? Why does pytest use normal Python assert?**
Answer:
In pytest, assertions are used to verify expected behaviour.
Example:
`assert result == expected`
If the condition is true:
•	test passes
If false:
•	test fails
Pytest improves normal Python assertions by rewriting them to give better failure messages.
Example:
```python
assert 5 == 7
```
Pytest shows:
```python
Expected 5
Actual 7
```
This makes debugging easier.
________________________________________
**4. What is a fixture in pytest? Why are fixtures preferred over creating objects inside every test?**
Answer:
A fixture is a function that prepares data or resources needed by tests.
Instead of writing:
```python
def test_one():
    db = Database()
```
and repeating it everywhere, we create:
```python
@pytest.fixture
def db():
    return Database()
```
Now tests simply request:
```python
def test_one(db):
    ...
```
Benefits:
•	removes repeated setup code
•	keeps tests cleaner
•	allows reuse
•	controls setup and cleanup
Fixtures separate:
```python
Preparation code
        +
Testing code
```
________________________________________
**5. Explain pytest dependency injection using fixtures. Why does the fixture name become the test parameter name?**
Answer:
Pytest uses the name of the test parameter to locate a matching fixture.
Example:
```python
@pytest.fixture
def database():
    return Database()


def test_connection(database):
    assert database.connect()
```
Execution:

![Flowchart](/resources/ch16-pytest-101-conceptual-qa5.png)

The parameter name is not a normal variable assignment. Pytest uses it as a request for a fixture.
________________________________________
**6. What is the difference between a fixture and a normal function?
Answer:**
A normal function runs only when called.
Example:
`create_database()`
A fixture is controlled by pytest.
Pytest decides:
•	when to create it
•	how long to keep it
•	when to destroy it
A fixture can also perform cleanup:
```python
@pytest.fixture
def resource():
    obj = create()
    yield obj
    cleanup()
```
The code before yield is setup.
The code after yield is teardown.
________________________________________
**7. What are fixture scopes? Why do they exist?**
Answer:
Fixture scope controls how often a fixture is created.
Common scopes:

| Scope | Lifetime |
| --- | --- |
| function | once per test |
| class | once per class |
| module | once per file |
| session | once per pytest run |



Example:
```python
@pytest.fixture(scope="session")
def connection():
    return create_connection()
```
A session fixture is useful for expensive resources.
Example:
•	database connection
•	browser
•	server
It avoids recreating the same resource repeatedly.
________________________________________
**8. What is the difference between function scope and session scope fixtures?**
Answer:
Function scope creates a new object for every test.
Example:
```python
test1 → object A
test2 → object B
test3 → object C
```
Session scope shares one object:
```python
test1
test2
test3
    |
    v
 same object
 ```
Function scope gives better isolation.
Session scope gives better performance.
The choice depends on whether shared state is safe.
________________________________________
**9. Why can shared fixtures create problems?**
Answer:
When multiple tests share the same object, changes made by one test may affect another.
Example:
```python
@pytest.fixture(scope="session")
def account():
    return Account()
```
Test 1:
`account.balance = 0`
Test 2 may now receive:
`balance == 0`
This creates hidden dependency between tests.
A good test should usually be independent.
________________________________________
**10. What is mocking? Why do we replace real objects during testing?**
Answer:
Mocking means replacing a real dependency with a controlled fake object.
Real dependencies may be:
•	slow
•	unavailable
•	expensive
•	unpredictable
Examples:
•	internet APIs
•	databases
•	files
Instead of:

`Test → Real API → Internet`
we use:
`Test → Mock API`
Benefits:
•	faster tests
•	predictable results
•	no external failures
________________________________________
**11. What is the difference between a real object, simulated object, and mock object?**
Answer:
A real object performs the actual operation.
Example:
`Database()`
A simulation imitates behaviour using simplified code.
Example:
`FakeDatabase()`
A mock is created mainly for testing and controlling behaviour.
Example:
`Mock()`
Comparison:

| Object | Purpose |
| --- | --- |
| Real | Actual application work |
| Simulation | Demonstration/testing |
| Mock | Controlled replacement |



________________________________________
**12. How does pytest.raises() test exceptions?**
Answer:
Normally an exception stops program execution.
But during testing we may expect an error.
Example:
```python
with pytest.raises(ValueError):
    int("abc")
```
The test passes because the exception was expected.
The test fails if:
•	no exception occurs
•	wrong exception occurs
It verifies that the program handles invalid situations correctly.
________________________________________
**13. Why should exception messages sometimes be tested?**
Answer:
Checking only the exception type may not be enough.
Example:
```python
with pytest.raises(ValueError):
    process()
```
This confirms an error happened.
But:
```python
with pytest.raises(
    ValueError,
    match="invalid age"
):
    process()
```
also verifies that the correct error message was generated.
________________________________________
**14. What is parameterized testing? Why is it useful?**
Answer:
Parameterized testing runs the same test with multiple inputs.
Without parameterization:
```python
test_add_1()
test_add_2()
test_add_3()
```
With parameterization:
```python
@pytest.mark.parametrize(
"input,expected",
[
(1,2),
(3,4)
])
```
One test handles many cases.
Benefits:
•	less duplicate code
•	easier maintenance
•	better test coverage
________________________________________
**15. In parameterized testing, why does pytest show multiple tests?**
Answer:
Each parameter set becomes a separate test case.
Example:
```python
[
(1,2),
(3,4),
(5,6)
]
```
creates:
```python
test_add[1-2]
test_add[3-4]
test_add[5-6]
```
If one fails, the others can still execute.
________________________________________
**16. What is the difference between skipping and expected failure?**
Answer:
Skipping means:
>Do not run this test.
>
Example:
`@pytest.mark.skip`
Expected failure means:
>Run the test, but failure is acceptable.
>
Example:
`@pytest.mark.xfail
Use:`
Skip:
•	feature not available
xfail:
•	known bug exists
________________________________________
**17. What is the purpose of conftest.py?**
Answer:
conftest.py stores shared fixtures.
Instead of:
```python
test1.py
    fixture

test2.py
    same fixture
```
we put:
```python
conftest.py
    fixture
```
All tests can use it automatically.
Advantages:
•	avoids duplication
•	centralizes setup code
•	supports large projects
________________________________________
**18. Why should tests avoid depending on execution order?**
Answer:
Tests should be independent.
Bad:
```python
test_create_user()
        |
        v
test_delete_user()
```
If the first test fails, the second also fails.
Each test creates its own required state.
Advantages of Independent tests:
•	easier debugging
•	reliable execution
•	can run in any order
________________________________________
**19. What is the difference between testing application logic and testing resources?**
Answer:
Application logic is usually what we want to verify.
Example:
`calculate_discount()`
Resources are things needed to run.
Example:
•	database
•	file
•	API
Fixtures and mocks help manage resources while tests focus on logic.
________________________________________
**20. Why are pytest fixtures considered one of the most important pytest features?**
Answer:
Fixtures combine several testing ideas:
•	setup
•	cleanup
•	reuse
•	dependency injection
•	resource management
They allow tests to focus only on the actual behaviour being tested.
A well-designed pytest suite usually has:
```python
Fixtures → prepare environment

Tests → verify behaviour

Assertions → check results
```
This separation makes large test suites easier to maintain.
