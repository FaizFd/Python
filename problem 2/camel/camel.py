camelCase = input("camelCase: ")

print ("snake_case: ", end="")

for upper_case in camelCase:
    if upper_case.isupper():
        print("_" + upper_case.lower(), end="")
    else:
        print(upper_case, end="")

print()