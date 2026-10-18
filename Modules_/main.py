# Method 1
# importing module
import calculations

add = calculations.add(5, 3)
print(add)

subt = calculations.subtract(5, 3)
print(subt)

# Method 2
# Import specific function from module
from calculations import add, subtract

print(add(5, 3))
print(subtract(5, 3))

# Method 3
# Import module with alias
import calculations as calc

print(calc.add(5,3))

# Method 4 
# importing built in modules from Python
import statistics as stats
data = [1, 2, 3, 4, 5]

mean = stats.mean(data)
print("Mean: ", mean)

# Method 5
# Importing specific function from module as alias
from calculations import multiply as product

print(product(5, 3))

# best to avoid this, not a good standard practice to import all/every modules like this. Import specific modules needed.
# from calculations import * 
# * - import everything