# float_demo.py
# Why 1.10 * 0.10 is not exactly 0.11 in Python.
# Run it with:  python float_demo.py

# Step 1 - The calculation used by calculate_tax(1.10)
result = 1.10 * 0.10
print("1.10 * 0.10         =", result)
print("Is it equal to 0.11?", result == 0.11)

# Step 2 - The same effect in a famous example
print("0.1 + 0.2           =", 0.1 + 0.2)
print("Is it equal to 0.3? ", 0.1 + 0.2 == 0.3)

# Step 3 - What is really stored for 0.1 (shown with 25 decimal places)
print("0.1 is stored as    ", format(0.1, ".25f"))

# Step 4 - Way 1 to compare safely: allow a small tolerance
import math
print("math.isclose(result, 0.11):", math.isclose(result, 0.11))

# Step 5 - Way 2 for money: round to 2 decimal places
print("round(result, 2)    =", round(result, 2))

# Step 6 - Way 3 for money: use the decimal module, which stores
#          decimal fractions exactly when created from strings
from decimal import Decimal
exact = Decimal("1.10") * Decimal("0.10")
print("Decimal result      =", exact)
print("Equal to Decimal('0.11')?", exact == Decimal("0.11"))
