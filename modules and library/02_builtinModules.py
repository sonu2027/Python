import math
print(math.sqrt(16)) # Output: 4.0

# Importing Specific Functions:
# You can import specific functions from a module to avoid using the module name.
from math import sqrt
print(sqrt(16))  # Output: 4.0

# Aliasing a Module:
# You can give a module or function an alias using as.
import math as m
print(m.sqrt(16))  # Output: 4.0

import random
print(random.randint(1, 10))  # Random number between 1 and 10

number=[3,2,4,7,0]
print(max(number))