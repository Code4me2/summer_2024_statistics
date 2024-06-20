# Written by Vel Moon
# Math 80 Statistics
# Professor Hu, CCSF
# A simple program to show examples of the linear correlation coefficient, linear regression
# and scatter plots.


import random
import statistics
import matplotlib.pyplot as plt

# Create a random population of 1000 integers ranging from 1 to 10,000
population_size = 1000 
population = [random.randint(0, 10000.00)for _ in range(population_size)] 
print("Population:\n \n", population)
print ("\n")

# Select two random lists (x and y) of size 50 from the population
sample_size = 50
list_x = random.sample(population, sample_size)
list_y = random.sample(population, sample_size)
print("Sample 1:\n \n", list_x, "\n")
print("Sample 2: \n \n", list_y, "\n")

# Calculate the linear correlation coefficient
liner_correlation_coefficient = round(statistics.correlation(list_x, list_y), 2)
print("Linear Correlation Coefficient:", liner_correlation_coefficient)

# Calculate the linear regression line
slope, intercept = statistics.linear_regression(list_x, list_y)
print("Regression Line: y =", round(slope, 2), "x +", round(intercept, 2), "\n")

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(list_x, list_y, color='blue', edgecolor='black')

# Plot the regression line
x_values = sorted(list_x)
y_values = [slope * x + intercept for x in x_values]
plt.plot(x_values, y_values, color='red')

# Add titles and labels
plt.title('Scatter Plot of Random Samples')
plt.xlabel('X values')
plt.ylabel('Y values')

# Show the plot
plt.tight_layout()
plt.show()

