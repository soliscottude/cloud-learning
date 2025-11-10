# Example: if / elif / else statements

# Ask user for how many hours they studied today
hours = int(input("How many hours did you study today? "))

# Give feedback based on the number
if hours >= 6:
    print("🔥 Amazing dedication! You worked really hard today!")
elif hours >= 3:
    print("💪 Nice! You're keeping up with your goals.")
elif hours > 0:
    print("👍 Good start! Try to do a bit more tomorrow.")
else:
    print("😴 Take some rest today and start fresh tomorrow!")

# End message
print("Keep learning, Scott!")
