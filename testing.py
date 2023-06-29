import os
import random
import string

# Number of programs to generate
num_programs = 5

# Directory to save the programs
directory = "generated_programs"

# Generate a random string of given length
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Generate a random Python program with given filename
def generate_python_program(filename):
    program = f"import random\n\n"
    program += f"# This is a simple Python program\n\n"
    program += f"def generate_random_number():\n"
    program += f"    return random.randint(1, 10)\n\n"
    program += f"number = generate_random_number()\n"
    program += f"print('Random number:', number)\n"
    
    with open(filename, 'w') as file:
        file.write(program)

# Create a directory to save the programs
os.makedirs(directory, exist_ok=True)
os.chdir(directory)
program_dir = os.getcwd()

# Generate random Python programs
for i in range(num_programs):
    filename = f"program{i+1}.py"
    generate_python_program(filename)
    print(f"Generated program: {filename}")

print("Script completed successfully.")
