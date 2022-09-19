# Ask the user for their input
usrinput = input("Whats happening? ")

# replace the white space with ...
usrinput = usrinput.replace(":)", "🙂")
usrinput = usrinput.replace(":(", "🙁")

# Print the output
print(f"{usrinput}")