# Written by Vel Moon
# Math 80 Statistics
# Professor Hu, CCSF
# A simple program to show an example of mean, standard deviation, and a histogram

import random
import statistics
import matplotlib.pyplot as plt

# Create a random population of 1000 integers ranging from 1 to 10,000
population_size = 1000 
population = [random.randint(1, 10000) for _ in range(population_size)] 
print("Population:\n \n", population)
print ("\n")

# Select a random sample of size 100 from the population
sample_size = 100
sample = random.sample(population, sample_size)
print("Sample:\n \n", sample)
print ("\n")


# Calculate sample mean using statistics library
sample_mean = statistics.mean(sample)
print("Sample Mean: ", sample_mean)


# Calculate sample standard deviation using statistics library
sample_standard_deviation = statistics.stdev(sample)
print("Sample Standard Deviation: ", sample_standard_deviation)


# Create histogram for the sample with 8 class intervals
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(sample, bins=8, color='green', edgecolor='black')


# Create custom x-axis labels for each bin range
bin_ranges = [f'{int(bins[i])}-{int(bins[i+1])}' for i in range(len(bins)-1)]
plt.xticks(bins[:-1], bin_ranges, rotation=45)


# The rest is pretty straightforward just read what is in orange and the other comment.
plt.title('Histogram of Sample')
plt.xlabel('Class Intervals')
plt.ylabel('Frequency')

# Show the plot
plt.tight_layout()
plt.show()
