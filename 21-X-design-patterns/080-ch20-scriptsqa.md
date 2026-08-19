




**Q1. Write a script implementing a basic Singleton pattern to maintain a single configuration reference. Verify if two instances point to the exact same memory object.**

```python
# Step 1: Define a class using __new__ to enforce a single instance
class AppConfig:
    _instance = None  # Class variable to store the shared source of truth

    def __new__(cls):
        # Part 1 Explanation: __new__ controls object instantiation logic. 
        # If _instance is None, create it once; otherwise, return the existing one.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Step 2: Create two separate objects and assert identity
config1 = AppConfig()
config2 = AppConfig()

# Verify memory equality using the 'is' identity keyword
print(f"Are instances identical? {config1 is config2}")  # Output: True
```
**Pattern Explanation:**
  -  Design Pattern Used: Singleton Pattern (Creational family).
  -  Core Mechanics: The `__new__` magic method intercepts the creation phase of an object before `__init__` is invoked. By checking if cls._instance is already cached, it ensures that no matter how many times a client calls AppConfig(), they always receive a reference to the exact same block of allocated memory. This serves as a centralized "source of truth" to prevent state synchronization conflicts across complex application layers.

**Q2. Implement a Factory Method function named `get_vehicle `that returns an instance of a `Car` or `Bike` object based on an input string parameter.**

```python
# Step 1: Create concrete product classes with a uniform interface
class Car:
    def drive(self): return "Driving a car!"

class Bike:
    def drive(self): return "Riding a bike!"

# Step 2: Implement the Factory Method function
def get_vehicle(vehicle_type):
    # Part 1 Explanation: This function decouples class selection logic from client code.
    if vehicle_type.lower() == "car":
        return Car()
    return Bike()

# Step 3: Call the factory function and invoke behaviors
v1 = get_vehicle("car")
v2 = get_vehicle("bike")
print(v1.drive())  # Output: Driving a car!
print(v2.drive())  # Output: Riding a bike!
```
**Pattern Explanation:**
  -  Design Pattern Used: Factory Method Pattern (Creational family).
  -  Core Mechanics: The client script avoids calling `Car()` or `Bike()` directly. Instead, object lifecycle generation is delegated to `get_vehicle()`. This structural decoupling conforms to clean architectural principles because if a new class like `Truck` is introduced, only the centralized factory logic changes; the calling application code remains untouched.

**Q3. Design an Abstract Factory setup featuring a `DarkButton` and `DarkWindow `under a `DarkThemeFactory`, and a `LightButton` and `LightWindow` under a `LightThemeFactory`. Include a uniform client loader.**

```python
# Step 1: Build product families
class DarkButton:   def render(self): print("Dark Button")
class DarkWindow:   def render(self): print("Dark Window")
class LightButton:  def render(self): print("Light Button")
class LightWindow:  def render(self): print("Light Window")

# Step 2: Construct individual abstract factories matching product groupings
class DarkThemeFactory:
    def create_button(self): return DarkButton()
    def create_window(self): return DarkWindow()

class LightThemeFactory:
    def create_button(self): return LightButton()
    def create_window(self): return LightWindow()

# Step 3: Write client script that consumes the factory abstractly
def render_ui(factory):
    btn = factory.create_button()
    win = factory.create_window()
    btn.render()
    win.render()

# Step 4: Execute with related groupings
render_ui(DarkThemeFactory())
render_ui(LightThemeFactory())
```
**Pattern Explanation:**
  -  Design Pattern Used: Abstract Factory Pattern (Creational family).
  -  Core Mechanics: This pattern defines a suite of related methods (`create_button, create_window`) designed to produce uniform sets of cohesive products. It acts as a factory of factories, preventing accidental cross-contamination (e.g., matching a `DarkButton` with a `LightWindow`), thereby ensuring complete system component consistency.

**Q4. Build a Robot construction script using the Builder Pattern. Support method chaining for adding custom components step-by-step.**

```python
# Step 1: Create the target product class with a parts storage list
class Robot:
    def __init__(self):
        self.parts = []

    def add_sensor(self):
        self.parts.append("Lidar Sensor")
        return self  # Part 1 Explanation: Returning 'self' is required to enable method chaining syntax

    def add_gripper(self):
        self.parts.append("Mechanical Gripper")
        return self

# Step 2: Execute step-by-step instantiation using fluent method chaining
my_bot = Robot().add_sensor().add_gripper().add_sensor()
print(f"Robot assembly: {my_bot.parts}")  # Output: ['Lidar Sensor', 'Mechanical Gripper', 'Lidar Sensor']
```
**Pattern Explanation:**

  -  Design Pattern Used: Builder Pattern (Creational family).
  -  Core Mechanics: Instead of forcing a massive, confusing constructor containing multiple arbitrary arguments, the Builder pattern splits object construction piece-by-piece using descriptive incremental step methods. Returning self at the end of each customization action creates a clean fluent interface syntax.

**Q5. Write a Prototype pattern script where a data-heavy configuration object clones itself via a distinct custom `.clone()` routine.**

```python
# Step 1: Create a prototype-capable configuration object
class DataConfig:
    def __init__(self):
        # Simulate costly setup or data fetching
        self.dataset = [10, 20, 30]

    def clone(self):
        # Step 2: Allocate a new instance and explicitly duplicate internal data lists
        new_clone = DataConfig()
        new_clone.dataset = list(self.dataset)  # Perform an independent copy operation
        return new_clone

# Step 3: Generate an initial object and instantiate a clone
base_obj = DataConfig()
cloned_obj = base_obj.clone()

print(f"Data matches: {base_obj.dataset == cloned_obj.dataset}")  # True
print(f"Are distinct objects: {base_obj is not cloned_obj}")     # True
```
**Pattern Explanation:**
  -  Design Pattern Used: Prototype Pattern (Creational family).
  -  Core Mechanics: The Prototype pattern bypasses expensive standard system initialization workflows by allocating a new raw object structure and duplicating the populated operational properties of an existing blueprint instance directly. This optimization ensures that subsequent variations save CPU processing cycles.

**Q6. Construct a manual structural Decorator class named `BoldDecorator` that wraps a base text-generation function to format string outputs.**

```python
# Step 1: Establish a simple string generator source function
def get_text():
    return "Hello World"

# Step 2: Build a wrapper class that implements structural augmentation
class BoldDecorator:
    def __init__(self, target_function):
        self.target = target_function  # Store original function pointer reference

    def render(self):
        # Wrap target output inside new decorative markup boundaries
        return f"<b>{self.target()}</b>"

# Step 3: Wrap manually and inspect output variations
wrapped = BoldDecorator(get_text)
print(wrapped.render())  # Output: <b>Hello World</b>
```
**Pattern Explanation:**
  -  Design Pattern Used: Decorator Pattern (Structural family).
  -  Core Mechanics: This structural design uses aggregation or wrapping to dynamically assign extra behavior to an object or execution handle at runtime without altering its underlying class architecture. The original function remains entirely isolated and simple, respecting the Open/Closed Principle.

**Q7. Convert the previous BoldDecorator script into an automated native Python syntax format using magic dunder methods.**

```python
# Step 1: Create a decorator class supporting call interceptions
class BoldDecoratorSyntax:
    def __init__(self, target_function):
        self.target = target_function

    def __call__(self):
        # Part 1 Explanation: __call__ allows an instance object to execute like a normal function call
        return f"<b>{self.target()}</b>"

# Step 2: Apply the decorator wrapper via native @ notation syntax
@BoldDecoratorSyntax
def get_custom_text():
    return "Python Design Patterns"

# Step 3: Execute transparently
print(get_custom_text())  # Output: <b>Python Design Patterns</b>
```
**Pattern Explanation:**
  -  Design Pattern Used: Pythonic Decorator Pattern (Structural family).
  -  Core Mechanics: By defining the` __call__` dunder method inside the structural wrapper wrapper class, Python automatically substitutes the raw function descriptor with a `BoldDecoratorSyntax` instance block. This approach provides a natural alternative to traditional Gang of Four class boilerplate.

**Q8. Write an Adapter pattern script that converts a legacy incompatible `.request_xml()` output method style into a client-expected `.get_json()` format.**

```python
# Step 1: Provide the incompatible legacy provider class
class LegacyXMLProvider:
    def request_xml(self):
        return "<data>Value</data>"

# Step 2: Create a translator Adapter class mapping to target client endpoints
class DataAdapter:
    def __init__(self, legacy_service):
        self.service = legacy_service

    def get_json(self):
        # Intercept legacy payload, transform structure internally, and return
        xml_payload = self.service.request_xml()
        return f'{{"data": "Converted from {xml_payload}"}}'

# Step 3: Execute via client expected workflow interface
legacy = LegacyXMLProvider()
bridge = DataAdapter(legacy)
print(bridge.get_json())  # Output: {"data": "Converted from <data>Value</data>"}
```
**Pattern Explanation:**
  -  Design Pattern Used: `Adapter` Pattern (Structural family).
  -  Core Mechanics: The `Adapter` acts as a translation layer between two incompatible architectural boundaries. It wraps the legacy system instance inside a wrapper object that exposes the method contract expected by modern clients (`get_json`), preventing the need to refactor existing legacy systems.

**Q9. Implement a unified `HomeFacade` architecture containing `TV` and `SoundSystem` subsystems to expose an incredibly simple `.start_movie()` unified action.**

```python
# Step 1: Define complex inner standalone subsystem classes
class TV:
    def turn_on(self): return "TV screen active."

class SoundSystem:
    def set_surround(self): return "Surround sound initialized."

# Step 2: Build a simple, unified Facade management layer
class HomeFacade:
    def __init__(self):
        self.tv = TV()
        self.sound = SoundSystem()

    def start_movie(self):
        # Coordinate multiple operations behind an uncomplicated abstraction gate
        steps = [self.tv.turn_on(), self.sound.set_surround()]
        return " | ".join(steps)

# Step 3: Call via the simplified public interface
theater = HomeFacade()
print(theater.start_movie())  # Output: TV screen active. | Surround sound initialized.
```
**Pattern Explanation:**
  -  Design Pattern Used: Facade Pattern (Structural family).
  -  Core Mechanics: A Facade provides a single, high-level interface that masks complex internal structural dependencies. Instead of requiring client logic to manage multiple lower-level components independently, the Facade consolidates these operations behind a simplified interface.

**Q10. Model an hierarchical filesystem structure with a unified leaf/composite interface using a File and a Folder component via the Composite design pattern.**

```python
# Step 1: Define the Leaf node element
class File:
    def __init__(self, name, size):
        self.name = name
        self.size_value = size

    def get_size(self):
        return self.size_value

# Step 2: Create the Composite node element containing collection objects
class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def get_size(self):
        # Recursively parse through child objects uniformly
        return sum(child.get_size() for child in self.children)

# Step 3: Assemble structural trees and calculate aggregated evaluations
root = Folder("Root")
root.add(File("notes.txt", 500))
sub_folder = Folder("Images")
sub_folder.add(File("pic.png", 1200))
root.add(sub_folder)

print(f"Total structured sizing: {root.get_size()} bytes")  # Output: 1700 bytes
```
**Pattern Explanation:**
  -  Design Pattern Used: Composite Pattern (Structural family).
  -  Core Mechanics: The Composite pattern establishes a uniform method contract (`get_size`) across both primitive items (File) and organizational container objects (Folder). This allows clients to treat individual objects and complex hierarchical groupings interchangeably without writing conditional type-checking branching statements.

**Q11. Implement a lazy-loading proxy pattern class (ImageProxy) that defers actual instantiation of an expensive internal `_RealImage` object until `.display()` is invoked.**

```python
# Step 1: Create the hidden expensive system target resource class
class _RealImage:
    def __init__(self, filename):
        self.filename = filename
        print(f"LOADING high-res file from disk: {filename}")

    def display(self):
        print(f"Displaying original full resolution file: {self.filename}")

# Step 2: Build the protective access control surrogate proxy class
class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_subject = None  # Defer allocation step initially

    def display(self):
        # Instantiated on demand (lazy execution optimization wrapper pattern)
        if self._real_subject is None:
            self._real_subject = _RealImage(self.filename)
        self._real_subject.display()

# Step 3: Instantiate Proxy surrogate and verify deferred loading actions
img = ImageProxy("photo.raw")  # No print message triggered here
print("--- Proxy initialized ---")
img.display()  # Triggers real loading routine and display actions on-demand
```
**Pattern Explanation:**
  -  Design Pattern Used: Proxy Pattern (Structural family).
  -  Core Mechanics: The Proxy pattern acts as a surrogate or placeholder. Because both the `ImageProxy` and `_RealImage` share equivalent logical public operations, the proxy transparently intercepts requests. It defers resource-intensive operations until they are explicitly needed, saving system memory and startup time.

**Q12. Build an architectural event listener tracking routine matching an Observer workflow by linking a `WeatherStation` subject update with registered display units.**

```python
# Step 1: Construct the Subject communication engine component
class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temp = 0

    def attach(self, observer): self._observers.append(observer)
    
    def set_temperature(self, temp):
        self._temp = temp
        self._notify_all()

    def _notify_all(self):
        for obs in self._observers:
            obs.update(self._temp)

# Step 2: Build an independent display observer module component
class PhoneDisplay:
    def update(self, temp):
        print(f"Phone screen updated broadcast metrics: {temp}°C")

# Step 3: Connect dependencies and distribute states dynamically
station = WeatherStation()
phone = PhoneDisplay()
station.attach(phone)
station.set_temperature(32)  # Output: Phone screen updated broadcast metrics: 32°C
```

**Pattern Explanation:**
  -  Design Pattern Used: Observer Pattern (Behavioral family).
  -  Core Mechanics: This pattern implements a loose Publish-Subscribe (Pub-Sub) architecture. The Subject class tracks listener handles (_observers) and automatically pushes state alerts out to them via individual .update() calls. This decouples sender and receiver modules, allowing you to add new independent display listeners without modifying the core data engine.

**Q13. Code a Strategy layout that encapsulates runtime interchangeable mathematical algorithms by writing an adaptive processing system handling Add or Multiply.**

```python
# Step 1: Define concrete mathematical calculation strategies
class StrategyAdd:
    def execute(self, a, b): return a + b

class StrategyMultiply:
    def execute(self, a, b): return a * b

# Step 2: Construct the Context engine controller block
class CalculatorContext:
    def __init__(self, default_strategy):
        self.strategy = default_strategy  # Injectable processing variant

    def calculate(self, x, y):
        # Delegate computation steps abstractly out to the injected strategy handle
        return self.strategy.execute(x, y)

# Step 3: Change strategies flexibly at execution runtime
calc = CalculatorContext(StrategyAdd())
print(calc.calculate(10, 5))  # Output: 15
calc.strategy = StrategyMultiply()  # Swap algorithm behavior dynamically
print(calc.calculate(10, 5))  # Output: 50
```
**Pattern Explanation:**
  -  Design Pattern Used: Strategy Pattern (Behavioral family).
  -  Core Mechanics: The Strategy pattern organizes a family of algorithms into independent, interchangeable classes. By extracting operational variations out of complex conditional blocks (if-elif) and delegating execution to an isolated strategy object, the application context remains lean and easily testable.

**Q14. Implement an undoable transaction command routing pipeline using the descriptive Command Pattern framework mapping action targets against a Light resource receptor.**

```python
# Step 1: Define the Receiver target entity
class Light:
    def __init__(self): self.state = "OFF"
    def turn_on(self):  self.state = "ON"
    def turn_off(self): self.state = "OFF"

# Step 2: Create a Concrete Command capsule class tracking execution historical loops
class LightOnCommand:
    def __init__(self, receiver_light):
        self.light = receiver_light

    def execute(self): self.light.turn_on()
    def undo(self):    self.light.turn_off()  # Track inverse operations

# Step 3: Wire execution commands through a basic client control controller
bulb = Light()
cmd = LightOnCommand(bulb)

cmd.execute()
print(f"Current bulb status state: {bulb.state}")  # Output: ON
cmd.undo()
print(f"After undo instruction status state: {bulb.state}")  # Output: OFF
```
**Pattern Explanation:**
  -  Design Pattern Used: Command Pattern (Behavioral family).
  -  Core Mechanics: The Command pattern wraps user requests into standalone objects containing all the context needed for execution. By separating the invoker from the receiver, actions can be stored in queues, passed as parameters, or undone by pairing execution triggers with inverse execution actions.

**Q15. Write a custom sequence traversal loop pattern using the traditional Iterator architecture by defining sequential steps inside `CustomIterator` and `CustomCollection`.**

```python
# Step 1: Implement an independent traversal engine management class
class CustomIterator:
    def __init__(self, elements):
        self._items = elements
        self._index = 0

    def __next__(self):
        # Define sequential manual collection element processing constraints
        if self._index >= len(self._items):
            raise StopIteration  # Signal iteration boundary completion sequence
        val = self._items[self._index]
        self._index += 1
        return val

# Step 2: Implement the iterable collection container class
class CustomCollection:
    def __init__(self): self.data = ["A", "B", "C"]
    def __iter__(self): return CustomIterator(self.data)

# Step 3: Run via a loop sequence interface
for token in CustomCollection():
    print(token)  # Prints: A, then B, then C sequential outputs
```
**Pattern Explanation:**
  -  Design Pattern Used: Iterator Pattern (Behavioral family).
  -  Core Mechanics: The Iterator pattern moves data traversal logic out of a collection class and into a dedicated iterator object. This decouples data storage from list navigation, allowing the client to traverse data elements sequentially via standard loops without needing to know how the collection is structured internally.

**Q16. Create a structural text document printing layout that utilizes a generic standard workflow structure according to the Template Method format.**

```python
# Step 1: Establish an abstract or shared master base layout document class
class BaseDocumentRenderer:
    def render_all(self):
        # The rigid Template Method: standardizes structural execution flow
        self.print_header()
        self.print_body()  # Custom variant step handled downstream

    def print_header(self): 
        print("--- Document Standard Header Header ---")

    def print_body(self): 
        raise NotImplementedError("Subclasses must overwrite this specific method step!")

# Step 2: Override structural variance items inside target subclass contexts
class PDFReport(BaseDocumentRenderer):
    def print_body(self): 
        print("PDF binary encryption body processing content content.")

# Step 3: Call template pipeline sequence loop interfaces
PDFReport().render_all()
```
**Pattern Explanation:**
  -  Design Pattern Used: Template Method Pattern (Behavioral family).
  -  Core Mechanics: The parent class establishes an immutable algorithmic skeleton (`render_all`), hardcoding the order of execution. It provides common default steps (`print_header`) while deferring specific structural steps (`print_body`) to subclasses. This eliminates code duplication across variations.

**Q17. Develop an elegant Pythonic native alternative to resource management workflows by configuring a class utilizing Context Manager protocols.**

```python
# Step 1: Create a Resource monitoring context manager class structure
class DbSessionConnection:
    def __enter__(self):
        print("ACQUIRE database transaction channel connectivity resource.")
        return self  # Return resource target operational hook pointer reference

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("RELEASE automatic resource garbage teardown extraction workflows cleanup.")
        return False  # Do not suppress any inner exceptions raised during block execution

# Step 2: Use the manager seamlessly via the with structural control block
with DbSessionConnection() as session:
    print("Executing operations inside context boundary scopes...")
```
**Pattern Explanation:**
  -  Design Pattern Used: Pythonic Context Manager Pattern (Alternative to Creational/Behavioral resource management).
  -  Core Mechanics: The `__enter__` and `__exit__` magic methods automate the setup and teardown phases of resource lifecycles. This ensures that files, sockets, or database connections are reliably cleaned up even if unexpected errors break execution flow within the block.

**Q18. Write a Python mixin architecture script featuring independent small single-purpose feature additions via structural multi-inheritance parameters.**

```python
# Step 1: Construct small single-purpose feature utility mixin classes
class JSONSerializationMixin:
    def to_json(self):
        # Convert simple internal instance dictionaries into dynamic pseudo-JSON string records
        return f'{{"data_dump": {str(self.__dict__)}}}'

# Step 2: Inherit behavioral properties as plug-and-play components
class EmployeeProfile(JSONSerializationMixin):
    def __init__(self, username):
        self.username = username

# Step 3: Instantiate and execute capabilities inherited through composition mixins
worker = EmployeeProfile("Alex")
print(worker.to_json())  # Output: {"data_dump": {'username': 'Alex'}}
```
**Pattern Explanation:**
  -  Design Pattern Used: Pythonic Mixin Pattern (Structural technique).
  -  Core Mechanics: A Mixin is a specialized parent class designed solely to add distinct, reusable features to child implementations via multiple inheritance. It provides an elegant alternative to heavy, rigid, traditional Gang of Four class hierarchies.

**Q19. Demonstrate Pythonic Duck Typing flexibility by defining classes lacking explicit interface inheritances that execute uniformly when parsed inside a generalized calling routine.**
```python
# Step 1: Build completely standalone code structures that implement overlapping method names
class AudioFile:
    def play(self): print("Playing music sound wave tracks.")

class VideoFile:
    def play(self): print("Rendering interactive movie clip frames.")

# Step 2: Construct an independent consumer function that calls methods abstractly
def broadcast_media(media_object):
    # Part 1 Explanation: If an object walks and quacks like a duck, Python treats it as one.
    media_object.play()  # Execute behavior without restricting incoming types explicitly

# Step 3: Run varying contexts dynamically
broadcast_media(AudioFile())
broadcast_media(VideoFile())
```
**Pattern Explanation:**
  -  Design Pattern Used: Duck Typing Interface Style (Pythonic structural behavior alternative).
  -  Core Mechanics: Python bypasses rigid, formal interface definitions by focusing on an object's actual capabilities over its explicit inheritance tree. If an object implements the required methods (play), it is deemed fully compatible, significantly reducing software structural boilerplate.

**Q20. Implement a native Python `@dataclass` setup acting as an immutable Value Object, and configure its parameters to raise runtime modifications errors.**

```python
from dataclasses import dataclass

# Step 1: Declare a structured value record entity utilizing dataclass wrappers
@dataclass(frozen=True)
class GeoCoordinates:
    # Part 1 Explanation: frozen=True enforces immutability, making the class an explicit Value Object
    latitude: float
    longitude: float

# Step 2: Instantiate and attempt structural read/write alterations
point = GeoCoordinates(23.45, 85.33)
print(f"Stored points metrics parameters: {point.latitude}, {point.longitude}")

# The follow-up step throws an error if un-commented out due to frozen restrictions:
# point.latitude = 25.00  # Raises dataclasses.FrozenInstanceError
```
**Pattern Explanation:**
  -  Design Pattern Used: Pythonic Value Object Pattern via Dataclasses.
  -  Core Mechanics: Storing simple attributes using lightweight `@dataclass(frozen=True)` containers helps implement the clean immutable structural patterns pattern. It treats data structures as read-only values rather than stateful entities, preventing unpredictable side effects and data corruption.
