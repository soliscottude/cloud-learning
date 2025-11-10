# Example: Variables and user input in Python

# Ask for user's name and study hours
name = input("Enter your name: ")
hours = input("How many hours did you study today? ")

# Print a message using string concatenation
print("Hello, " + name + "! You studied " + hours + " hours today.")

# Better formatting using f-string (recommended)
print(f"Hello, {name}! You studied {hours} hours today.")

# Convert input to integer and do a simple calculation
total = int(hours) + 2
print(f"If you study 2 more hours, your total will be {total} hours!")
