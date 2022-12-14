while True:

    fuel = input("Fraction: ")
    try:
        numerator, denominator = fuel.split("/")

        new_numerator = int(numerator)
        new_denominator = int(denominator)

        f = new_numerator / new_denominator

        if f <= 1:
            break

except ValueError