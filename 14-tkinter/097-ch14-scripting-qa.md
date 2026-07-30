## Scripting Question/ Answers (TKinter)


**1. Create a basic Tkinter application using an OOP class structure that initializes the main window, sets a custom title and geometry, and includes a button that prints a message to the console when clicked.**

This script establishes the foundational Object-Oriented structure for Tkinter applications. By creating a class that inherits from `tk.Tk`, we encapsulate the GUI logic, preventing global variable scope errors. The `__init__` method initializes the root window (the OS container), sets the title (window manager property), and defines the geometry (size and position). The button demonstrates the use of the `command=` parameter for event handling, which is the simplest way to bind a user action (click) to a Python function without dealing with complex event objects.

```python
import tkinter as tk

class BasicOOPApp(tk.Tk):
    """
    A foundational Tkinter application demonstrating OOP structure.
    
    Concepts Covered:
    1. Class Inheritance: Inheriting from tk.Tk to create the main window.
    2. Initialization: Configuring window properties (title, geometry).
    3. Event Handling: Using the 'command' attribute for button clicks.
    4. Architecture: Explaining the Python -> Tkinter -> OS hierarchy.
    """
    def __init__(self):
        # 1. Initialize the base class (tk.Tk)
        # This starts the Tcl interpreter and creates the root window.
        super().__init__()
        
        # 2. Configure the Root Window
        # These methods interact with the OS Window Manager to update
        # the visual appearance and size of the window container.
        self.title("OOP Structure Demo")
        self.geometry("400x300+100+100") # WidthxHeight+X_Offset+Y_Offset

        # 3. Create a Button Widget
        # 'self' is the parent container (the root window).
        # 'command=self.on_click' binds the click event to our method.
        # Note: No parentheses are used with on_click here.
        self.btn_action = tk.Button(self, text="Print Message", 
                                    command=self.on_click)
        self.btn_action.pack(pady=50, expand=True)

    def on_click(self):
        """
        Callback function executed when the button is pressed.
        
        This represents the 'Python Logic' layer. When the user clicks
        the button (OS Event -> Tk Event -> Python), this code runs.
        """
        print("Button clicked! Application logic executed.")

if __name__ == "__main__":
    # Instantiate the application class to start the GUI
    app = BasicOOPApp()
    # Start the Event Loop (The 'Guard')
    app.mainloop()
```

**2. Write a script using `StringVar` to link an Entry widget and a Label widget. Demonstrate that updating the Entry automatically updates the Label in real-time.**

This script explores the "Reactive Data Model" of Tkinter. Standard Python variables are passive, but Tkinter Control Variables (like `StringVar`) act as live conduits. We bind the variable to the Entry using `textvariable=` and to the Label using `textvariable=`. This creates a "pipeline" where the Tcl/Tk engine automatically notifies the Label to repaint whenever the data in the StringVar changes, eliminating the need for manual refresh commands.

```python
import tkinter as tk

class ReactiveDataApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reactive Data Binding")
        self.geometry("400x200")

        # 1. Create a Tkinter Control Variable (The Source of Truth)
        # StringVar manages the string data in the Tcl/Tk engine.
        self.input_data = tk.StringVar(value="Type something...")

        # 2. Create an Input Widget (Entry)
        # We bind the Entry to 'input_data' using 'textvariable'.
        # Anything typed here updates 'input_data' instantly.
        self.entry_input = tk.Entry(self, textvariable=self.input_data, 
                                    font=("Consolas", 12))
        self.entry_input.pack(pady=20, padx=20, fill="x")

        # 3. Create a Display Widget (Label)
        # We bind the Label to the SAME 'input_data' using 'textvariable'.
        # The Label subscribes to changes in 'input_data'.
        self.lbl_display = tk.Label(self, textvariable=self.input_data, 
                                    font=("Arial", 14, "bold"), fg="blue")
        self.lbl_display.pack(pady=20)

        # Explanation for the student
        tk.Label(self, text="The Label mirrors the Entry automatically.", 
                 font=("Arial", 8)).pack(side="bottom", pady=10)

if __name__ == "__main__":
    app = ReactiveDataApp()
    app.mainloop()
```

**3. Implement a variable tracer using `.trace_add("write", callback)` to validate user input in real-time (e.g., ensuring a password is longer than 6 characters).**

This script demonstrates "Live Automation." Instead of waiting for a button press to validate data, we use the `trace_add` method on a `StringVar`. This method acts as a "watch guard," firing a specific callback function every time the variable is written to (modified). The callback accepts `*args` to absorb the three internal arguments that the Tcl/Tk engine passes (name, index, mode), preventing a runtime crash.

```python
import tkinter as tk

class ValidationTracerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Live Validation with Tracing")
        self.geometry("450x250")

        # 1. Define the Control Variable
        self.password_var = tk.StringVar()

        # 2. Set up the Trace
        # "write" mode: Triggers when the variable's value changes.
        # self.validate_password: The callback function.
        # This establishes the link between data change and logic execution.
        self.password_var.trace_add("write", self.validate_password)

        # 3. GUI Setup
        tk.Label(self, text="Enter Password:", font=("Arial", 10)).pack(pady=(20, 5))
        self.ent_pass = tk.Entry(self, textvariable=self.password_var, show="*", 
                                 font=("Consolas", 12))
        self.ent_pass.pack(pady=5)

        # Label to provide feedback
        self.lbl_status = tk.Label(self, text="Status: Waiting", 
                                   font=("Arial", 10, "italic"))
        self.lbl_status.pack(pady=20)

    def validate_password(self, *args):
        """
        Callback executed automatically when password_var changes.
        
        *args is required because trace_add passes 3 arguments from Tcl:
        args[0] = variable name (e.g., 'PY_VAR0')
        args[1] = index (empty for scalars)
        args[2] = operation mode (e.g., 'write')
        """
        current_val = self.password_var.get()

        # Logic: Check length and update UI instantly
        if len(current_val) == 0:
            self.lbl_status.config(text="Status: Waiting", fg="gray")
        elif len(current_val) < 6:
            self.lbl_status.config(text="Status: Too Short!", fg="red")
        else:
            self.lbl_status.config(text="Status: Strong Password", fg="green")

if __name__ == "__main__":
    app = ValidationTracerApp()
    app.mainloop()
```

**4. Create a form layout using the `.grid()` geometry manager. Include Labels and Entry widgets aligned in rows and columns, and use `sticky`, `padx`, and `pady` for spacing.**

The `.grid()` manager is ideal for form-based layouts as it treats the parent container as a spreadsheet. This script demonstrates how to position widgets using row and column indices. The `sticky` parameter aligns widgets within their grid cells (e.g., `tk.W` for West/Left), while `padx` and `pady` add external padding. This provides precise control over alignment that `.pack()` cannot easily achieve.

```python
import tkinter as tk
from tkinter import ttk

class GridFormApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grid Geometry Manager")
        self.geometry("350x250")

        # Using a Frame to act as the container for the grid
        # This keeps the layout logic isolated from the root window.
        form_frame = ttk.Frame(self, padding="20")
        form_frame.pack(expand=True)

        # --- Row 0: Name Field ---
        ttk.Label(form_frame, text="Full Name:").grid(
            row=0, column=0, sticky=tk.W, pady=10) # Sticky='W' aligns West
        ttk.Entry(form_frame, width=20).grid(
            row=0, column=1, sticky=tk.E, pady=10)

        # --- Row 1: Email Field ---
        ttk.Label(form_frame, text="Email:").grid(
            row=1, column=0, sticky=tk.W, pady=10)
        ttk.Entry(form_frame, width=20).grid(
            row=1, column=1, sticky=tk.E, pady=10)

        # --- Row 2: Buttons (Spanning columns) ---
        # 'columnspan' makes the widget stretch across multiple columns.
        submit_btn = ttk.Button(form_frame, text="Submit")
        submit_btn.grid(row=2, column=0, columnspan=2, pady=20)

        # Configure column weights to allow resizing behavior (optional)
        form_frame.columnconfigure(1, weight=1)

if __name__ == "__main__":
    app = GridFormApp()
    app.mainloop()
```

**5. Build a layout using the `.pack()` geometry manager to create a toolbar (top), a main content area (middle), and a status bar (bottom).**

While `.grid()` is for precision, `.pack()` is for flow. This script demonstrates how to stack widgets in specific directions using the `side` parameter (`top`, `bottom`, `left`, `right`). We also use `fill` to make widgets expand to fill available space (e.g., `fill="x"` for horizontal expansion) and `expand=True` to allocate extra space. This is the standard pattern for application shell layouts.

```python
import tkinter as tk
from tkinter import ttk

class PackLayoutApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pack Geometry Manager")
        self.geometry("400x300")

        # 1. TOP TOOLBAR
        # side='top' places it at the top. fill='x' stretches it horizontally.
        toolbar = tk.Frame(self, bg="#333", height=30)
        toolbar.pack(side="top", fill="x")
        
        tk.Button(toolbar, text="File", bg="#555", fg="white").pack(side="left", padx=5)
        tk.Button(toolbar, text="Edit", bg="#555", fg="white").pack(side="left", padx=5)

        # 2. MAIN CONTENT AREA
        # expand=True tells pack to give this frame any extra available space.
        # fill='both' stretches it in both directions.
        content = tk.Frame(self, bg="white")
        content.pack(side="top", fill="both", expand=True)
        
        tk.Label(content, text="Main Workspace", font=("Arial", 16)).pack(expand=True)

        # 3. BOTTOM STATUS BAR
        # side='bottom' anchors it to the bottom.
        statusbar = tk.Label(self, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side="bottom", fill="x")

if __name__ == "__main__":
    app = PackLayoutApp()
    app.mainloop()
```

**6. Create a GUI that uses `Checkbutton` widgets bound to `BooleanVar` variables. Add a "Submit" button that checks the state of these variables to determine which options were selected.**

This script covers binary state management. `BooleanVar` holds `True` or `False`. We bind the Checkbutton to the variable using the `variable=` parameter (not `textvariable`). This decouples the visual checkbox from the logic; we don't need to query the widget directly, we simply check the value of the `BooleanVar` using `.get()`. This is cleaner and more "Pythonic" than inspecting widget properties.

```python
import tkinter as tk
from tkinter import messagebox

class CheckboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Checkbutton Selection")
        self.geometry("300x250")

        # 1. Initialize BooleanVars
        # These track the on/off state of the checkboxes in the Tcl engine.
        self.var_news = tk.BooleanVar(value=False)
        self.var_updates = tk.BooleanVar(value=True)
        self.var_terms = tk.BooleanVar(value=False)

        # 2. Create Checkbuttons
        # 'variable=' links the checkbox state to the BooleanVar.
        chk1 = tk.Checkbutton(self, text="Subscribe to Newsletter", 
                              variable=self.var_news)
        chk1.pack(pady=5, anchor="w", padx=20)

        chk2 = tk.Checkbutton(self, text="Receive Product Updates", 
                              variable=self.var_updates)
        chk2.pack(pady=5, anchor="w", padx=20)

        chk3 = tk.Checkbutton(self, text="I agree to Terms & Conditions", 
                              variable=self.var_terms)
        chk3.pack(pady=5, anchor="w", padx=20)

        # 3. Submit Button
        tk.Button(self, text="Register", command=self.show_selections).pack(pady=20)

    def show_selections(self):
        """Reads the values from the variables to determine logic."""
        choices = []
        if self.var_news.get(): choices.append("Newsletter")
        if self.var_updates.get(): choices.append("Updates")
        if self.var_terms.get(): choices.append("Terms")

        if not choices:
            msg = "No options selected."
        else:
            msg = f"You selected: {', '.join(choices)}"
            
        messagebox.showinfo("Registration Details", msg)

if __name__ == "__main__":
    app = CheckboxApp()
    app.mainloop()
```

**7. Implement a "Tabbed Interface" using the `Notebook` widget (ttk). Create two tabs, "Home" and "Settings," and place different widgets in each tab.**

The `Notebook` widget is the container for tabbed interfaces. This script demonstrates how to create "pages" (which are essentially `Frame` widgets) and add them to the Notebook using the `.add()` method. Each tab acts as an independent parent container for its own children, allowing you to organize complex UIs into logical screens without creating multiple windows.

```python
import tkinter as tk
from tkinter import ttk

class TabbedInterfaceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notebook Tabs Demo")
        self.geometry("400x300")

        # 1. Create the Notebook Widget (The Tab Manager)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=5, pady=5)

        # 2. Create Frames for each tab
        # These frames serve as the content containers for the tabs.
        self.tab_home = ttk.Frame(self.notebook)
        self.tab_settings = ttk.Frame(self.notebook)

        # 3. Add Frames to Notebook
        # The 'text' parameter defines the label on the tab header.
        self.notebook.add(self.tab_home, text="Home")
        self.notebook.add(self.tab_settings, text="Settings")

        # 4. Add Widgets to Tab 1 (Home)
        lbl_home = tk.Label(self.tab_home, text="Welcome to the Home Tab", 
                            font=("Arial", 14))
        lbl_home.pack(pady=50)

        # 5. Add Widgets to Tab 2 (Settings)
        lbl_set = tk.Label(self.tab_settings, text="Configure your app here", 
                           font=("Arial", 14))
        lbl_set.pack(pady=50)
        
        # Entry in Settings to show independence
        ttk.Entry(self.tab_settings).pack(pady=10)

if __name__ == "__main__":
    app = TabbedInterfaceApp()
    app.mainloop()
```

**8. Write a script that uses a `PanedWindow` to create a resizable split-screen interface (e.g., a left sidebar and a right content area).**

`PanedWindow` allows users to dynamically adjust the layout by dragging a divider handle. This script creates a horizontal `PanedWindow`. We add two frames to it. Unlike `pack` or `grid`, the user determines the size ratio at runtime. This is crucial for applications like file explorers or code editors where the user needs to control screen real estate.

```python
import tkinter as tk
from tkinter import ttk

class PanedWindowApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PanedWindow Split View")
        self.geometry("500x300")

        # 1. Create the PanedWindow
        # orient='horizontal' creates a left/right split.
        # orient='vertical' would create a top/bottom split.
        self.paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True)

        # 2. Create the Content Frames
        # We use tk.Frame here to easily demonstrate background colors,
        # though ttk.Frame works too.
        self.left_frame = tk.Frame(self.paned, bg="#e0e0e0", width=150)
        self.right_frame = tk.Frame(self.paned, bg="#ffffff", width=350)

        # 3. Add frames to the PanedWindow
        # The 'weight' parameter determines how much extra space is given
        # during resizing. 1 implies equal distribution.
        self.paned.add(self.left_frame, weight=1)
        self.paned.add(self.right_frame, weight=3)

        # 4. Add Widgets to the Panes
        tk.Label(self.left_frame, text="Sidebar\n(Drag divider!)", 
                 bg="#e0e0e0").pack(expand=True)
        tk.Label(self.right_frame, text="Main Content Area", 
                 bg="#ffffff").pack(expand=True)

if __name__ == "__main__":
    app = PanedWindowApp()
    app.mainloop()
```

**9. Create a script that opens a secondary `Toplevel` window when a button is clicked in the main window. Demonstrate passing data from the main window to the `Toplevel` window.**

`Toplevel` creates a new, independent window that runs in the same process but has its own window manager decorations (close, minimize, maximize). This script shows how to launch a popup and customize its title/geometry. It also demonstrates that `Toplevel` accepts the main window as a logical parent, ensuring proper focus behavior, though it is visually independent.

```python
import tkinter as tk
from tkinter import ttk

class ToplevelWindowApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("300x200")

        self.main_data = "Hello from Main Window!"

        ttk.Button(self, text="Open Child Window", 
                   command=self.open_child_window).pack(pady=50, expand=True)

    def open_child_window(self):
        """
        Creates a new Toplevel window.
        
        This does not block the main window (unlike messagebox).
        Both windows remain active and interactive.
        """
        # Create Toplevel instance (passing 'self' as parent)
        child = tk.Toplevel(self)
        child.title("Child Window")
        child.geometry("250x150")

        # Pass data from the main window (self) to the child
        msg_label = ttk.Label(child, text=self.main_data, font=("Arial", 10))
        msg_label.pack(pady=30, expand=True)

        # Button to close just the child window
        ttk.Button(child, text="Close Child", 
                   command=child.destroy).pack(pady=10)

if __name__ == "__main__":
    app = ToplevelWindowApp()
    app.mainloop()
```

**10. Implement a `Canvas` widget that allows the user to draw rectangles by clicking and dragging the mouse. Use hardware event binding (`<Button-1>`, `<B1-Motion>`, `<ButtonRelease-1>`).**

The `Canvas` is a powerful tool for custom graphics. This script demonstrates "Hardware Event Binding." Unlike `command=`, which is abstract, `bind` connects raw physical actions (mouse clicks, movement) to logic. We track the starting coordinates (`x, y`) on mouse down, draw a dynamic rectangle on mouse drag, and finalize it on mouse release.

```python
import tkinter as tk

class CanvasDrawingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Canvas Drawing")
        self.geometry("500x400")

        # Variables to store drawing state
        self.start_x = None
        self.start_y = None
        self.current_rect = None

        # 1. Create Canvas
        # bg='white' gives a distinct drawing area.
        self.canvas = tk.Canvas(self, bg="white", cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # 2. Bind Hardware Mouse Events
        # <Button-1>: Left mouse click pressed
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        # <B1-Motion>: Mouse moved while button 1 is held down
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        # <ButtonRelease-1>: Left mouse button released
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def on_mouse_down(self, event):
        """Record the starting position of the drawing."""
        self.start_x = event.x
        self.start_y = event.y
        # We don't draw yet, just store coordinates.

    def on_mouse_drag(self, event):
        """Draw a temporary rectangle as the mouse moves."""
        # If a rectangle exists, delete it to prevent "trails"
        if self.current_rect:
            self.canvas.delete(self.current_rect)
        
        # Draw new rectangle from start to current mouse position
        # event.x and event.y are provided by the Event object
        self.current_rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, event.x, event.y, 
            outline="blue", width=2
        )

    def on_mouse_up(self, event):
        """Finalize the rectangle (optional cleanup logic)."""
        # In a complex app, we might save the ID of the finalized shape
        # to a list for later manipulation (move/delete).
        self.current_rect = None

if __name__ == "__main__":
    app = CanvasDrawingApp()
    app.mainloop()
```

**11. Create a `Listbox` widget populated with items. Add buttons to Add and Delete items. Ensure the listbox selection updates a label in real-time using the `<<ListboxSelect>>` virtual event.**

This script covers "Virtual Events." Unlike physical mouse clicks, `<<ListboxSelect>>` is a logical event that fires only when the *selection* in the list actually changes. We also demonstrate standard Listbox manipulation methods: `.insert()` to add items and `.delete()` to remove them using the `curselection()` index.

```python
import tkinter as tk
from tkinter import ttk

class ListboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Listbox Interaction")
        self.geometry("400x300")

        # -- Top Frame for Controls --
        control_frame = ttk.Frame(self)
        control_frame.pack(pady=10)

        self.entry_new = ttk.Entry(control_frame, width=20)
        self.entry_new.pack(side=tk.LEFT, padx=5)

        ttk.Button(control_frame, text="Add", command=self.add_item).pack(side=tk.LEFT)
        ttk.Button(control_frame, text="Delete", command=self.delete_item).pack(side=tk.LEFT)

        # -- Listbox --
        self.listbox = tk.Listbox(self, height=10, font=("Consolas", 10))
        self.listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Initial Data
        items = ["Python", "Java", "C++", "JavaScript"]
        for item in items:
            self.listbox.insert(tk.END, item)

        # -- Virtual Event Binding --
        # <<ListboxSelect>> fires when the user highlights a different item.
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # -- Status Label --
        self.lbl_status = ttk.Label(self, text="Selected: None")
        self.lbl_status.pack(pady=10)

    def add_item(self):
        text = self.entry_new.get()
        if text:
            self.listbox.insert(tk.END, text)
            self.entry_new.delete(0, tk.END)

    def delete_item(self):
        # curselection() returns a tuple of indices.
        selection = self.listbox.curselection()
        if selection:
            # Delete the item at the selected index
            self.listbox.delete(selection[0])

    def on_select(self, event):
        """Callback for the virtual selection event."""
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            # Get the text content of the selected item
            value = self.listbox.get(index)
            self.lbl_status.config(text=f"Selected: {value}")
        else:
            self.lbl_status.config(text="Selected: None")

if __name__ == "__main__":
    app = ListboxApp()
    app.mainloop()
```

**12. Build a form using `LabelFrame` to group related controls (e.g., Personal Details and Contact Info) into distinct sections.**

`LabelFrame` is a container widget that adds a labeled border around its children. This is essential for visual hierarchy in complex forms. This script demonstrates how to nest widgets inside different LabelFrames. It also reinforces the concept of parent-child hierarchy: widgets inside the `LabelFrame` take it as their first argument (`parent`), not the root window.

```python
import tkinter as tk
from tkinter import ttk

class LabelframeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LabelFrame Grouping")
        self.geometry("400x350")

        # Container for padding
        main_container = ttk.Frame(self, padding=20)
        main_container.pack(expand=True, fill="both")

        # 1. Group: Personal Details
        # text= sets the title in the border groove.
        group_personal = ttk.LabelFrame(main_container, text="Personal Details", padding=10)
        group_personal.pack(fill="x", pady=5)

        ttk.Label(group_personal, text="First Name:").grid(row=0, column=0, sticky="w")
        ttk.Entry(group_personal).grid(row=0, column=1, sticky="ew", padx=5)

        ttk.Label(group_personal, text="Last Name:").grid(row=1, column=0, sticky="w")
        ttk.Entry(group_personal).grid(row=1, column=1, sticky="ew", padx=5)
        
        # Configure grid weight for the column
        group_personal.columnconfigure(1, weight=1)

        # 2. Group: Contact Info
        group_contact = ttk.LabelFrame(main_container, text="Contact Info", padding=10)
        group_contact.pack(fill="x", pady=5)

        ttk.Label(group_contact, text="Email:").grid(row=0, column=0, sticky="w")
        ttk.Entry(group_contact).grid(row=0, column=1, sticky="ew", padx=5)

        ttk.Label(group_contact, text="Phone:").grid(row=1, column=0, sticky="w")
        ttk.Entry(group_contact).grid(row=1, column=1, sticky="ew", padx=5)
        
        group_contact.columnconfigure(1, weight=1)

        # Submit Button at the bottom (outside groups)
        ttk.Button(main_container, text="Save Profile").pack(pady=20)

if __name__ == "__main__":
    app = LabelframeApp()
    app.mainloop()
```

**13. Create a `Combobox` widget and use the `<<ComboboxSelected>>` virtual event to change the background color of a label based on the user's selection.**

`Combobox` combines an Entry widget with a Listbox. It is a themed widget (`ttk`), so it looks native. This script focuses on "Logical State Change" events. The `<<ComboboxSelected>>` event fires specifically when the user picks an item from the dropdown list, differentiating it from merely typing into the box. We map these selections to visual state changes.

```python
import tkinter as tk
from tkinter import ttk

class ComboboxApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Combobox Selection")
        self.geometry("300x200")

        # 1. Setup Data
        colors = ["Red", "Green", "Blue", "Yellow", "Cyan"]

        # 2. Instruction
        ttk.Label(self, text="Select a color:").pack(pady=10)

        # 3. Create Combobox
        self.combo = ttk.Combobox(self, values=colors, state="readonly")
        # state="readonly" prevents user from typing arbitrary values
        self.combo.pack(pady=5)
        self.combo.current(0) # Set default selection

        # 4. Bind Virtual Event
        # This event fires only when an item from the list is chosen.
        self.combo.bind("<<ComboboxSelected>>", self.change_color)

        # 5. Feedback Label
        self.lbl_feedback = tk.Label(self, text="Color Preview", 
                                     font=("Arial", 16), width=20, height=5)
        self.lbl_feedback.pack(pady=20)
        
        # Initialize color
        self.change_color(None)

    def change_color(self, event):
        """Changes label background based on dropdown selection."""
        selected = self.combo.get()
        
        # Map string selection to hex codes (or use simple names if supported)
        color_map = {
            "Red": "#ffcccc", "Green": "#ccffcc", "Blue": "#ccccff",
            "Yellow": "#ffffcc", "Cyan": "#ccffff"
        }
        
        bg_color = color_map.get(selected, "white")
        self.lbl_feedback.config(text=selected, bg=bg_color)

if __name__ == "__main__":
    app = ComboboxApp()
    app.mainloop()
```

**14. Write a script that implements a `Treeview` widget to display tabular data (ID, Name, Role). Add a function to insert a new row into the tree when a button is clicked.**

`Treeview` is the standard widget for displaying multi-column data (tables) and hierarchical structures (trees). This script demonstrates how to define columns using `.configure()` and create headings using `.heading()`. We also implement `.insert()` to add data rows (items) programmatically.

```python
import tkinter as tk
from tkinter import ttk

class TreeviewApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Treeview Table")
        self.geometry("500x300")

        # 1. Setup Treeview
        # columns defines the internal identifiers for data columns.
        # show='headings' hides the #0 icon column, showing only defined columns.
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Role"), show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 2. Define Headings
        self.tree.heading("ID", text="Employee ID")
        self.tree.heading("Name", text="Full Name")
        self.tree.heading("Role", text="Job Title")

        # 3. Configure Columns
        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Name", width=200, anchor="w")
        self.tree.column("Role", width=150, anchor="w")

        # 4. Initial Data
        employees = [
            (101, "Alice Smith", "Developer"),
            (102, "Bob Jones", "Designer"),
            (103, "Charlie Day", "Manager")
        ]
        
        for emp in employees:
            self.tree.insert("", tk.END, values=emp)

        # 5. Add Input Area
        input_frame = ttk.Frame(self)
        input_frame.pack(fill="x", padx=10, pady=10)

        self.ent_id = ttk.Entry(input_frame, width=10)
        self.ent_id.pack(side="left", padx=5)
        self.ent_id.insert(0, "104") # Default ID

        self.ent_name = ttk.Entry(input_frame, width=20)
        self.ent_name.pack(side="left", padx=5)
        self.ent_name.insert(0, "New User")

        self.ent_role = ttk.Entry(input_frame, width=15)
        self.ent_role.pack(side="left", padx=5)
        self.ent_role.insert(0, "Intern")

        ttk.Button(input_frame, text="Add Row", command=self.add_row).pack(side="left", padx=10)

    def add_row(self):
        """Reads inputs and inserts a new row into the Treeview."""
        emp_id = self.ent_id.get()
        name = self.ent_name.get()
        role = self.ent_role.get()
        
        # Insert data into the tree
        # '' is the parent ID (empty means root level)
        self.tree.insert("", tk.END, values=(emp_id, name, role))

if __name__ == "__main__":
    app = TreeviewApp()
    app.mainloop()
```

**15. Demonstrate the difference between Core (`tk`) and Themed (`ttk`) widgets by creating two buttons: one `tk.Button` with a custom background color, and one `ttk.Button` using a style object.**

This script addresses the design insight from the chapter regarding Core vs. Themed widgets. `tk.Button` allows direct configuration (bg, fg) but looks "retro." `ttk.Button` looks native but rejects direct color arguments, requiring a `ttk.Style` object. This teaches the student that modern styling works through a centralized stylesheet rather than individual widget properties.

```python
import tkinter as tk
from tkinter import ttk

class StylingComparisonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Styling: tk vs ttk")
        self.geometry("400x200")

        # --- Core Widget (tk) ---
        # Pros: Easy to change colors directly.
        # Cons: Looks dated/retro on modern OS.
        self.lbl_tk = tk.Label(self, text="Core Widget (tk.Button):", 
                               font=("Arial", 10, "bold"))
        self.lbl_tk.pack(pady=(20, 5))
        
        btn_core = tk.Button(self, text="I am Core", bg="red", fg="white", 
                             font=("Arial", 12, "bold"))
        btn_core.pack(pady=5)

        # --- Themed Widget (ttk) ---
        # Pros: Looks native/modern.
        # Cons: Cannot use bg/fg directly. Must use Style object.
        self.lbl_ttk = tk.Label(self, text="Themed Widget (ttk.Button):", 
                                font=("Arial", 10, "bold"))
        self.lbl_ttk.pack(pady=(20, 5))

        # 1. Create Style Object
        style = ttk.Style()
        
        # 2. Configure a custom style named "Custom.TButton"
        # This maps to the widget class and specific style name.
        style.configure("Custom.TButton", 
                        font=("Arial", 12, "bold"),
                        foreground="white",
                        background="green") # Note: bg might be ignored on some OS (Mac/Windows)

        # 3. Apply style to widget
        btn_theme = ttk.Button(self, text="I am Themed", style="Custom.TButton")
        btn_theme.pack(pady=5)

        ttk.Label(self, text="(Note: ttk styling depends on OS Theme)", 
                  font=("Arial", 8), foreground="gray").pack(side="bottom")

if __name__ == "__main__":
    app = StylingComparisonApp()
    app.mainloop()
```

**16. Create a script that tracks mouse movements over a large Label and displays the X and Y coordinates in real-time. Use the `<Motion>` hardware event.**

This script deepens the understanding of Event Objects. The `<Motion>` event fires every time the mouse pixel changes. Tkinter passes an Event Object to the callback, which contains attributes like `.x` and `.y` (coordinates relative to the widget) and `.x_root` and `.y_root` (coordinates relative to the screen). We access these properties to update our display.

```python
import tkinter as tk
from tkinter import ttk

class MouseTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mouse Motion Tracker")
        self.geometry("400x300")

        # Label to display coordinates
        self.coords_var = tk.StringVar(value="Move mouse over area...")
        self.lbl_coords = ttk.Label(self, textvariable=self.coords_var, 
                                    font=("Consolas", 12))
        self.lbl_coords.pack(side="bottom", pady=10)

        # Large interactive area
        self.canvas = tk.Canvas(self, bg="#f0f0f0")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Bind <Motion> event
        # This provides high-frequency updates of mouse position.
        self.canvas.bind("<Motion>", self.track_mouse)

    def track_mouse(self, event):
        """
        Handles the motion event.
        
        event.x: The x-coordinate relative to the top-left of the canvas.
        event.y: The y-coordinate relative to the top-left of the canvas.
        """
        x_pos = event.x
        y_pos = event.y
        
        # Update the label with the coordinates
        self.coords_var.set(f"Coordinates: X={x_pos}, Y={y_pos}")

        # Optional: Draw a small crosshair at the mouse position
        self.canvas.delete("crosshair")
        self.canvas.create_line(x_pos-10, y_pos, x_pos+10, y_pos, 
                                fill="red", tag="crosshair")
        self.canvas.create_line(x_pos, y_pos-10, x_pos, y_pos+10, 
                                fill="red", tag="crosshair")

if __name__ == "__main__":
    app = MouseTrackerApp()
    app.mainloop()
```

**17. Implement a simple Text Editor using the `Text` widget. Add a "Clear" button that deletes all content using the widget's index system (e.g., `1.0` to `end`).**

The `Text` widget is a complex, multi-line text editor. This script introduces the concept of "indices" in Tkinter text widgets. Indices are strings like "1.0" (Line 1, Character 0). We also use tags to style specific portions of text. The "Clear" function demonstrates how to manipulate the text buffer programmatically.

```python
import tkinter as tk
from tkinter import ttk

class TextEditorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Text Editor")
        self.geometry("400x300")

        # 1. Toolbar
        toolbar = ttk.Frame(self)
        toolbar.pack(side="top", fill="x")
        
        ttk.Button(toolbar, text="Clear Text", command=self.clear_text).pack(side="right", padx=5, pady=5)
        ttk.Button(toolbar, text="Insert Sample", command=self.insert_sample).pack(side="right", padx=5, pady=5)

        # 2. Text Widget
        # wrap='word' breaks lines at word boundaries, preventing mid-word cuts.
        self.text_area = tk.Text(self, wrap="word", font=("Consolas", 11), padx=10, pady=10)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # 3. Scrollbar (Manual setup for compatibility)
        scrollbar = ttk.Scrollbar(self.text_area, command=self.text_area.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=scrollbar.set)

    def insert_sample(self):
        """Inserts text at the current cursor position."""
        # 'tk.END' is a special index representing the end of the buffer.
        # 'tk.INSERT' represents the current cursor location.
        self.text_area.insert(tk.INSERT, "Hello World! This is a text editor.\n")
        
        # Configure a tag for color
        self.text_area.tag_config("highlight", foreground="blue")
        self.text_area.insert(tk.INSERT, "This text is blue using tags.\n", "highlight")

    def clear_text(self):
        """
        Deletes content from start to end.
        
        Indices:
        '1.0' -> Line 1, Character 0 (The very beginning).
        'end' -> The end of the text buffer.
        """
        self.text_area.delete("1.0", tk.END)

if __name__ == "__main__":
    app = TextEditorApp()
    app.mainloop()
```

**18. Create a script that uses the `.place()` geometry manager to position a widget at absolute coordinates. Include a button that randomly repositions the widget to demonstrate dynamic layout changes.**

While `pack` and `grid` are preferred for responsive layouts, `place` is useful for overlays or absolute positioning. This script shows how to use `x` and `y` for absolute pixel positioning and `relx` and `rely` for relative (percentage-based) positioning. We dynamically update these coordinates to show how `place()` can be used for animation or custom dragging logic.

```python
import tkinter as tk
import random

class PlaceManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Place Geometry Manager")
        self.geometry("400x300")

        # Create a movable widget
        self.movable_label = tk.Label(self, text="I Float!", bg="orange", 
                                      fg="black", width=10, height=2)
        
        # Initial placement using absolute coordinates (x=50, y=50)
        self.movable_label.place(x=50, y=50)

        # Button to randomize position
        btn_move = tk.Button(self, text="Randomize Position", 
                             command=self.randomize_position)
        btn_move.pack(side="bottom", pady=20)

    def randomize_position(self):
        """
        Moves the label to a new random spot within window bounds.
        
        We must calculate max_x and max_y so the label doesn't go off-screen.
        """
        # Get current window size
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        
        # Get label size
        label_width = self.movable_label.winfo_width()
        label_height = self.movable_label.winfo_height()

        # Calculate safe boundaries
        max_x = window_width - label_width
        max_y = window_height - label_height - 50 # Subtract space for button

        # Generate random coordinates
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)

        # Apply new position
        self.movable_label.place(x=new_x, y=new_y)

if __name__ == "__main__":
    app = PlaceManagerApp()
    app.mainloop()
```

**19. Implement a `Scale` (slider) widget linked to an `IntVar`. Use `.trace_add` to update a Canvas rectangle's size in real-time as the slider moves.**

This script combines Input Widgets (`Scale`), Control Variables (`IntVar`), Tracing, and Canvas manipulation. It creates a reactive graphical system where a numeric input controls a visual property (size). The `Scale` widget updates the `IntVar`, the trace triggers a callback, and the callback modifies the Canvas item using `.coords()`.

```python
import tkinter as tk
from tkinter import ttk

class ScaleCanvasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scale and Canvas Sync")
        self.geometry("400x350")

        # 1. Control Variable for Slider
        self.size_var = tk.IntVar(value=50)

        # 2. Trace the variable
        # When slider moves -> variable changes -> trace fires -> canvas updates.
        self.size_var.trace_add("write", self.update_rectangle)

        # 3. Slider Widget
        self.scale = ttk.Scale(self, from_=10, to=150, variable=self.size_var, 
                               orient="horizontal", length=300)
        self.scale.pack(pady=20)
        
        self.lbl_val = ttk.Label(self, text="Size: 50")
        self.lbl_val.pack()

        # 4. Canvas
        self.canvas = tk.Canvas(self, bg="white", width=300, height=200)
        self.canvas.pack(pady=10)

        # 5. Draw Initial Rectangle
        # create_rectangle(x1, y1, x2, y2)
        # Centered at (150, 100)
        self.rect_id = self.canvas.create_rectangle(
            100, 50, 200, 150, fill="blue", outline="black"
        )

    def update_rectangle(self, *args):
        """Resizes the rectangle based on the slider value."""
        size = self.size_var.get()
        self.lbl_val.config(text=f"Size: {size}")

        # Calculate new coordinates to keep rectangle centered
        center_x, center_y = 150, 100
        half = size // 2
        
        x1 = center_x - half
        y1 = center_y - half
        x2 = center_x + half
        y2 = center_y + half

        # Update canvas item coordinates
        self.canvas.coords(self.rect_id, x1, y1, x2, y2)

if __name__ == "__main__":
    app = ScaleCanvasApp()
    app.mainloop()
```

**20. Create a "Menu Bar" with "File" and "Help" menus. Implement "File -> Exit" functionality and "Help -> About" which opens a `messagebox`.**

This script covers the `Menu` widget, which is standard for desktop applications. It demonstrates how to cascade menus (tearoffs=0 is modern style), add commands, and add separators. It integrates the `messagebox` module for standard dialogs, reinforcing the use of native OS windows for alerts.

```python
import tkinter as tk
from tkinter import messagebox

class MenuBarApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu Bar Demo")
        self.geometry("400x300")

        # 1. Create the Main Menu Bar container
        menubar = tk.Menu(self)
        
        # 2. Configure the window to use this menubar
        self.config(menu=menubar)

        # 3. Create "File" Menu
        # tearoff=0 prevents the menu from being "torn off" into a separate window
        file_menu = tk.Menu(menubar, tearoff=0)
        
        # Add items to File Menu
        file_menu.add_command(label="New", command=self.dummy_action)
        file_menu.add_command(label="Open", command=self.dummy_action)
        file_menu.add_separator() # Adds a visual line
        file_menu.add_command(label="Exit", command=self.quit_app)
        
        # Add File Menu to Menubar
        menubar.add_cascade(label="File", menu=file_menu)

        # 4. Create "Help" Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        
        # Add Help Menu to Menubar
        menubar.add_cascade(label="Help", menu=help_menu)

        # Main Content
        tk.Label(self, text="Check the top menu bar!", 
                 font=("Arial", 14)).pack(expand=True)

    def dummy_action(self):
        print("Menu action triggered.")

    def quit_app(self):
        """Closes the application safely."""
        self.quit()
        self.destroy()

    def show_about(self):
        """Displays a native OS popup message."""
        messagebox.showinfo("About", "Tkinter Menu Demo\nVersion 1.0")

if __name__ == "__main__":
    app = MenuBarApp()
    app.mainloop()
```














