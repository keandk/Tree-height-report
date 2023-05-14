import random
import os

# Create directory if it doesn't exist
os.makedirs("Numbers", exist_ok=True)

# Number of files
num_files = 10

# Number of random numbers per file
num_numbers = 10**6

# Range of random numbers
num_range = 10**6

for i in range(num_files):
    # Generate a list of unique random numbers
    numbers = random.sample(range(num_range), num_numbers)

    with open(f"Numbers/numbers_{i+1}.txt", "w") as f:
        for num in numbers:
            f.write(f"{num} ")

print("Files have been created.")
