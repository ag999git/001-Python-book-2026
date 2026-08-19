




Part 1 (Questions 1–5)

### 1. Write a pytest script to test a simple function that returns the square of a number. Create a test function and verify the returned value.
Answer
```python
# square.py
# This is the application code that we want to test.

def square(number):
    # Step 1: Receive a number
    # Step 2: Multiply the number by itself
    # Step 3: Return the result

    return number * number

```

```python
# test_square.py

# Step 1: Import pytest
import pytest

# Step 2: Import the function to be tested
from square import square


# Step 3: Create a test function
def test_square():

    # Step 4: Call the application function
    result = square(5)

    # Step 5: Check the returned value
    assert result == 25
```
Explanation:
The test follows the basic pytest pattern:
1.	Arrange → Prepare the input 
2.	Act → Execute the function 
3.	Assert → Check the result 
The assert statement verifies whether the function behaved correctly.


### 2. Create a pytest fixture that creates a database object and injects it into two test functions.
Answer
```python
# database.py

class Database:

    def connect(self):

        # Step 1:
        # Simulate database connection

        print("[DB] connecting")

        return "connected"
```

```python
# test_database.py

import pytest

from database import Database


# Step 1:
# Create a fixture.
# The fixture creates the dependency object.

@pytest.fixture
def db():

    print("\n[FIXTURE] creating Database object")

    # Step 2:
    # Create Database object

    database = Database()

    # Step 3:
    # Return object to test

    return database



# Step 4:
# pytest sees parameter db
# It automatically calls the fixture named db
# The returned Database object is injected here.

def test_connection(db):

    print("[TEST] test_connection")

    result = db.connect()

    assert result == "connected"



def test_object_type(db):

    print("[TEST] test_object_type")

    assert isinstance(db, Database)
```
Important concept:
The name db has two roles:
1.	Fixture function name 
`def db():`
2.	Test parameter receiving the object 
`def test_connection(db):`
pytest connects these automatically.
________________________________________
### 3. Modify the fixture example to use session scope so that the object is created only once for all tests.
Answer
```python
# test_session_fixture.py

import pytest


class Database:

    def connect(self):

        print("[DB] connecting")

        return "connected"



# Step 1:
# Create a session-scoped fixture

@pytest.fixture(scope="session")
def db():

    print("\n[FIXTURE] session setup")

    # Step 2:
    # Create object once

    database = Database()

    database.connect()


    # Step 3:
    # Provide object to all tests

    yield database


    # Step 4:
    # Runs after all tests finish

    print("\n[FIXTURE] session teardown")



def test_one(db):

    print("[TEST] one")

    assert isinstance(db, Database)



def test_two(db):

    print("[TEST] two")

    assert isinstance(db, Database)



def test_three(db):

    print("[TEST] three")

    assert db.connect() == "connected"
```
Expected execution order:
```python
Fixture setup
      |
      v
Test 1
      |
Test 2
      |
Test 3
      |
      v
Fixture teardown
```
The setup and teardown happen only once.

### 4. Write a pytest script demonstrating dependency injection. Show how pytest injects a fixture object into a test function parameter.
Answer
```python
# test_injection.py

import pytest


class User:

    def __init__(self):

        self.name = "Alex"



# Step 1:
# Fixture function creates User object

@pytest.fixture
def user():

    print("\n[FIXTURE] creating User object")

    return User()



# Step 2:
# The test requests "user"
# pytest finds fixture named user
# pytest calls it
# pytest injects returned object

def test_user_injection(user):

    print("[TEST] received object")

    print(type(user))


    # Step 3:
    # Verify injected object

    assert user.name == "Alex"
```
Flow:
```python
test_user_injection(user)

        |
        v

pytest searches fixture "user"

        |
        v

calls user()

        |
        v

User object returned

        |
        v

Object placed into test parameter
```

### 5. Write a pytest test using pytest.raises() to verify that a function correctly raises an exception.
Answer

```python
# calculator.py


def divide(a, b):

    # Step 1:
    # Check invalid operation

    if b == 0:

        # Step 2:
        # Raise exception

        raise ValueError("division by zero")


    # Step 3:
    # Normal calculation

    return a / b
```

```python
# test_calculator.py


import pytest


from calculator import divide



def test_divide_exception():


    # Step 1:
    # Tell pytest that an exception is expected

    with pytest.raises(
        ValueError,
        match="division by zero"
    ):

        # Step 2:
        # Code inside this block should raise exception

        divide(10,0)
```
Important point:
Without pytest.raises():
`divide(10,0)`
would fail the test.
With:
`with pytest.raises(ValueError):`
pytest knows that the failure is expected.


### 6. Write a pytest script using pytest.mark.parametrize to test the same function with multiple input values.
Answer
```python
# calculator.py

def square(number):

    # Step 1:
    # Receive a number

    # Step 2:
    # Calculate square

    result = number * number

    # Step 3:
    # Return result

    return result

```

```python
# test_calculator.py

import pytest

from calculator import square



# Step 1:
# parametrize runs the same test multiple times
# with different input values.

@pytest.mark.parametrize(
    "number, expected",
    [
        (2, 4),
        (3, 9),
        (5, 25),
        (10, 100)
    ]
)
def test_square(number, expected):

    # Step 2:
    # Each row of data becomes one test run

    result = square(number)


    # Step 3:
    # Compare actual result with expected result

    assert result == expected
```

Explanation:
Instead of writing:
```python
def test_square_2():
    assert square(2) == 4


def test_square_3():
    assert square(3) == 9

```
we write one test and provide many input combinations.
Each parameter set is treated as a separate test.

### 7. Create a parameterized test that checks both valid and invalid inputs for a function.
Answer
```python
# validator.py


def check_age(age):

    # Step 1:
    # Validate age

    if age < 18:

        # Step 2:
        # Return invalid message

        return "not allowed"


    # Step 3:
    # Return valid message

    return "allowed"
```

```python

# test_validator.py

import pytest

from validator import check_age



# Step 1:
# Create multiple test cases

@pytest.mark.parametrize(
    "age, expected",
    [
        (10, "not allowed"),
        (17, "not allowed"),
        (18, "allowed"),
        (25, "allowed")
    ]
)
def test_age_check(age, expected):

    # Step 2:
    # Execute function

    result = check_age(age)


    # Step 3:
    # Verify output

    assert result == expected
```
Learning point:
Parameterized testing is useful when:
•	the logic is same 
•	only input changes 
It improves:
•	readability 
•	maintenance 
•	test coverage 

### 8. Arrange a pytest project so that tests are automatically discovered.
Answer
Project structure:

```python

my_project/

│
├── calculator.py
│
├── tests/
│
│   ├── test_calculator.py
│   └── test_validator.py
│
└── README.md
```

`calculator.py`
```python
# Application file


def add(a,b):

    # Step 1:
    # Add two numbers

    return a + b
```

`tests/test_calculator.py`

```python
# Test file

from calculator import add



def test_add():

    # Step 1:
    # Call application function

    result = add(2,3)


    # Step 2:
    # Verify result

    assert result == 5
```
Run: (On Terminal)
> pytest
pytest automatically finds:
```python
test_*.py
*_test.py
```
and functions:
`test_*`

Important naming rule:
Correct:
```python
test_math.py
math_test.py
```
Incorrect:
```python
math_testing.py
mytests.py
```
The incorrect names may not be discovered automatically.

### 9. Write a pytest fixture using yield to perform setup and teardown operations.
Answer

```python
# test_resource.py

import pytest



class Resource:


    def start(self):

        print("[APP] resource started")


    def stop(self):

        print("[APP] resource stopped")




@pytest.fixture
def resource():


    # Step 1:
    # Setup section

    print("\n[FIXTURE] setup")


    obj = Resource()


    obj.start()



    # Step 2:
    # Send object to test

    yield obj



    # Step 3:
    # Teardown section
    # Runs after test finishes

    print("[FIXTURE] teardown")


    obj.stop()




def test_resource(resource):


    # Step 4:
    # resource contains object returned by yield

    print("[TEST] running")


    assert isinstance(resource, Resource)
```

Execution flow:
```python
Fixture setup
       |
       v
yield object
       |
       v
Test runs
       |
       v
Code after yield
       |
       v
Teardown
```
Important:
The code before yield is setup.
The code after yield is cleanup.

### 10. Write a pytest example that uses a mock object instead of calling a real external service.
Answer

```python
# payment.py

import requests



def get_price(product):


    # Step 1:
    # Real program would contact internet API

    response = requests.get(
        "https://example.com/product"
    )


    # Step 2:
    # Extract price

    return response.json()["price"]
```

Problem:
Testing this directly:
`get_price("book")`
would:
•	need internet 
•	be slow 
•	depend on external server 

Using Mock:

```python
# test_payment.py


from unittest.mock import Mock

import requests

from payment import get_price



def test_price():


    # Step 1:
    # Create fake response object

    fake_response = Mock()



    # Step 2:
    # Decide what fake object returns

    fake_response.json.return_value = {
        "price":100
    }



    # Step 3:
    # Replace real requests.get

    requests.get = Mock(
        return_value=fake_response
    )



    # Step 4:
    # Run application code

    result = get_price("book")



    # Step 5:
    # Verify result

    assert result == 100
```
Concept:
The test does not contact the internet.
Instead:
```python
Real API
   |
   X
   |
Fake object
   |
   v
Test continues
```
Mocking helps create:
•	fast tests 
•	predictable tests 
•	independent tests 






### 11. Create a conftest.py file containing a fixture and use it in a test file without importing it.
Answer
Project structure:
```python
project/

│
├── calculator.py
│
├── conftest.py
│
└── test_calculator.py
```

conftest.py

```python
import pytest


class Calculator:


    def add(self, a, b):

        # Step 1:
        # Add two numbers

        return a + b




@pytest.fixture
def calculator():


    # Step 2:
    # Create object

    print("\n[FIXTURE] creating calculator")


    obj = Calculator()


    # Step 3:
    # Return object to test

    return obj
```

test_calculator.py

```python
def test_add(calculator):


    # Step 1:
    # calculator object is automatically injected

    print("[TEST] add started")


    result = calculator.add(5, 10)


    # Step 2:
    # Verify result

    assert result == 15
```
Important observation:
There is no:
`from conftest import calculator`
pytest automatically searches:

```python
test file
      |
      v
conftest.py
      |
      v
fixture
```
and injects the object.

### 12. Demonstrate the difference between function scope and module scope fixtures.
Answer
```python
# test_scope.py


import pytest



# Step 1:
# Function scope is default scope
# Runs once for every test function


@pytest.fixture(scope="function")
def function_fixture():

    print("\n[FIXTURE] function setup")

    return "object"



# Step 2:
# Module scope runs once per file


@pytest.fixture(scope="module")
def module_fixture():

    print("\n[FIXTURE] module setup")

    return "object"




def test_one(function_fixture, module_fixture):

    print("[TEST] one")



def test_two(function_fixture, module_fixture):

    print("[TEST] two")

```
Output idea:
```python
[FIXTURE] module setup

[FIXTURE] function setup
[TEST] one

[FIXTURE] function setup
[TEST] two
```
Observation:
`module_fixture`
runs once.
`function_fixture`
runs before every test.



Comparison table:
| Scope | Lifetime | Runs |
| --- | --- | --- |
| function | one test | every test |
| class | test class | once per class |
| module | file | once per file |
| session | complete run | once |

### 13. Create a session-scoped fixture to show that an expensive resource is created only once.
Answer

```python
# test_session.py


import pytest



count = 0



class Connection:


    def connect(self):

        print("[APP] connecting")



    def close(self):

        print("[APP] closing")





@pytest.fixture(scope="session")
def connection():


    global count


    # Step 1:
    # This executes only once

    count += 1


    print(
        f"\n[FIXTURE] setup count = {count}"
    )


    obj = Connection()


    obj.connect()



    # Step 2:
    # Provide object to all tests

    yield obj



    # Step 3:
    # Cleanup at end of session

    obj.close()




def test_one(connection):


    print("[TEST] one")


    assert isinstance(connection, Connection)




def test_two(connection):


    print("[TEST] two")


    assert isinstance(connection, Connection)




def test_three(connection):


    print("[TEST] three")


    assert isinstance(connection, Connection)
```
Expected idea:

```python
[FIXTURE] setup count = 1

[TEST] one
[TEST] two
[TEST] three

[APP] closing
```
The same object is shared.

### 14. Demonstrate the shared state problem with a session-scoped fixture.
Answer
```python
# test_shared_state.py


import pytest




class User:

    def __init__(self):

        self.logged_in = False





@pytest.fixture(scope="session")
def user():


    # Step 1:
    # Create one shared object

    print("\n[FIXTURE] creating user")


    return User()




def test_login(user):


    # Step 2:
    # Modify shared object

    user.logged_in = True


    print("[TEST] user logged in")


    assert user.logged_in == True




def test_status(user):


    # Step 3:
    # This test receives same object

    print("[TEST] checking status")


    assert user.logged_in == True
```
Output concept:
```python
Test 1 changes object
          |
          v
Same object goes to Test 2
          |
          v
Changed value remains
```
Problem:
Tests become dependent on each other.
A safer approach:
`scope="function"`
creates a fresh object.
________________________________________
### 15. Test exceptions and floating point values using pytest tools.
Answer
Part A — Testing Exceptions
Application:
```python
# calculator.py


def divide(a,b):


    # Step 1:
    # Check invalid division

    if b == 0:

        raise ValueError(
            "cannot divide by zero"
        )


    # Step 2:
    # Normal calculation

    return a / b
```
Test:
```python
# test_calculator.py


import pytest

from calculator import divide




def test_exception():


    # Step 1:
    # Tell pytest that exception is expected

    with pytest.raises(
        ValueError,
        match="cannot divide"
    ):


        # Step 2:
        # Code which should raise exception

        divide(10,0)
```
Flow:
```python
Run test
   |
   v
Execute code inside with block
   |
   +------------+
   |            |
Exception     No exception
raised        raised
   |             |
   v             v
PASS          FAIL
```
**Part B — Testing floating point values**
Problem:
```python
def calculate_tax(amount):

    return amount * 0.10
```
Test:
```python
import pytest



def test_tax():


    result = calculate_tax(1.10)


    # Step 1:
    # Do not compare floats exactly

    assert result == pytest.approx(0.11)
```
Why?
Computers store floating point numbers approximately.
Example:
```python
Human:
0.10 + 0.20 = 0.30


Computer:
0.30000000000000004
```
pytest.approx() checks whether values are close enough.





### 16. Write a pytest script that tests the return value of a function using assertions.
Answer
calculator.py
```python
# Step 1:
# Application code file


def multiply(a, b):

    # Step 2:
    # Perform calculation

    result = a * b


    # Step 3:
    # Return result

    return result
```
test_calculator.py

```python
# Step 1:
# Import application function

from calculator import multiply



def test_multiply():


    # Step 2:
    # Call the function

    result = multiply(5, 4)


    # Step 3:
    # Verify returned value

    assert result == 20


    # Step 4:
    # Verify type also

    assert type(result) == int
```
Learning point:
A test should verify:
•	what the function returns 
•	whether the returned value is correct 
•	whether the returned data type is correct 
________________________________________
### 17. Create a pytest script to test multiple functions of an application.
Answer
bank.py
```python
# Application file


def deposit(balance, amount):

    # Step 1:
    # Add amount

    return balance + amount




def withdraw(balance, amount):


    # Step 2:
    # Remove amount

    return balance - amount
```
test_bank.py
```python
# Step 1:
# Import functions

from bank import deposit, withdraw



def test_deposit():


    # Step 2:
    # Test deposit

    result = deposit(100,50)


    assert result == 150




def test_withdraw():


    # Step 3:
    # Test withdrawal

    result = withdraw(100,30)


    assert result == 70
```
Concept:
Each test should normally test one behavior.
Good:
```python
test_deposit()
test_withdraw()
```
Avoid:
```python
test_everything()
```
because failures become difficult to identify.

### 18. Use fixtures with a test class to share common setup code.
Answer
```python
# test_user.py


import pytest



class User:


    def __init__(self):

        self.name = "Student"




@pytest.fixture
def user():


    # Step 1:
    # Create common object

    print("\n[FIXTURE] creating user")


    return User()




class TestUser:


    def test_name(self,user):


        # Step 2:
        # Fixture object injected

        assert user.name == "Student"



    def test_type(self,user):


        # Step 3:
        # Same fixture logic used

        assert isinstance(
            user,
            User
        )
```
Important:
Fixtures reduce repeated code.
Without fixture:
`user = User()`
would be repeated in every test.

### 19. Combine parameterized testing and fixtures to test multiple cases.
Answer

```python
# test_login.py


import pytest



class LoginSystem:


    def check(self, username):


        # Step 1:
        # Simple validation

        if username == "admin":

            return True


        return False




@pytest.fixture
def login():


    # Step 2:
    # Create object

    return LoginSystem()




@pytest.mark.parametrize(
    "username, expected",
    [
        ("admin", True),
        ("guest", False),
        ("abc", False)
    ]
)
def test_login(login, username, expected):


    # Step 3:
    # Same fixture object
    # with different inputs


    result = login.check(username)



    # Step 4:
    # Verify result

    assert result == expected
```
Execution idea:

```python
Fixture creates object
          |
          v
Parameter set 1 -> test
Parameter set 2 -> test
Parameter set 3 -> test
```
Advantages:
•	no repeated test code 
•	many cases covered 
•	easy to add new tests 

### 20. Create a complete small pytest project with application code and test code.
Answer
Project structure:
```python
student_project/

│
├── product.py
│
└── tests/
    │
    └── test_product.py
```
product.py
```python
# Application file


class Product:


    def __init__(self,name,price):


        # Step 1:
        # Store product data

        self.name = name
        self.price = price



    def get_price(self):


        # Step 2:
        # Return stored price

        return self.price
```

`tests/test_product.py`

```python
import pytest


from product import Product



@pytest.fixture
def product():


    # Step 1:
    # Create common object

    print("\n[FIXTURE] creating product")


    return Product(
        "Book",
        100
    )




def test_product_name(product):


    # Step 2:
    # Test name

    assert product.name == "Book"




def test_product_price(product):


    # Step 3:
    # Test method result

    result = product.get_price()


    assert result == 100




@pytest.mark.parametrize(
    "value",
    [
        100,
        200,
        300
    ]
)
def test_multiple_prices(value):


    # Step 4:
    # Test multiple values

    p = Product(
        "Item",
        value
    )


    assert p.get_price() == value
```

Final project demonstrates:

| Concept | Used |
| --- | --- |
| Application code separation | product.py |
| Test file | test_product.py |
| Fixture | @pytest.fixture |
| Dependency injection | fixture parameter |
| Assertions | assert |
| Parametrization | pytest.mark.parametrize |
| Class testing | Product |
