# Written by Vel Moon
# Math 80 Statistics
# Professor Hu, CCSF
# A simple python program to compare students' gpa and age

# 1. 
# Use python's pandas lib to make a dataframe

# 2. 
# # Call the DataFrame "student" with 6 columns: ID, First name, last name, major, GPA and Age
# for 16 different studentsl so there are 16 rows, one row for each student.
# you can make up the students' name and majors
# user random module to create random ID's, each with 5 digits;
# use rand to make GPA's from 0.00 to 4.00, two decimal placees
# rand ages from 18.0 to 22.0, one decimal place

# 3.
# Print out the Dataframe

# 4.
# draw two box plots for GPA and age side by side

#5. 
# Make a comment: what can we conclude about age and GPA from the Box ploots?
# e.g. : the older, the higher the GPA, or vice versa, or.....
import pandas as pd
import random

# Step 2: Generate data for 16 students
num_students = 16

# Generate random 5-digit IDs
ids = [random.randint(10000, 99999) for _ in range(num_students)]

# Generate random first names and last names
first_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah",
               "Ivy", "Jack", "Karen", "Liam", "Mia", "Noah", "Olivia", "Paul"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
              "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas"]

# List of possible majors
majors = ["Engineering", "Mathematics", "Physics", "Chemistry", "Biology", "Economics", "Literature", "Philosophy"]

# Generate random GPAs (from 0.00 to 4.00, two decimal places)
gpas = [round(random.uniform(0.00, 4.00), 2) for _ in range(num_students)]

# Generate random ages (from 18.0 to 22.0, one decimal place)
ages = [round(random.uniform(18.0, 22.0), 1) for _ in range(num_students)]

# Create the DataFrame
student_data = {
    "ID": ids,
    "First name": first_names,
    "Last name": last_names,
    "Major": [random.choice(majors) for _ in range(num_students)],
    "GPA": gpas,
    "Age": ages
}

student_df = pd.DataFrame(student_data)

# Step 3: Print the DataFrame
print(student_df)

# Step 4: Draw two box plots for GPA and Age side by side
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

# Box plot for GPA
plt.subplot(1, 2, 1)
plt.boxplot(student_df["GPA"], patch_artist=True)
plt.title("Box Plot of GPA")
plt.ylabel("GPA")

# Box plot for Age
plt.subplot(1, 2, 2)
plt.boxplot(student_df["Age"], patch_artist=True)
plt.title("Box Plot of Age")
plt.ylabel("Age")

plt.tight_layout()
plt.show()

# Step 5: Conclusion
# What can we conclude about age and GPA from the box plots?
# Comment: The conclusions will vary based on the generated data, but here is a template conclusion.
# Based on the box plots, it appears that there is no clear relationship between age and GPA. 
# The spread of GPAs does not seem to correlate with the spread of ages. Students of various ages have a wide range of GPAs.
