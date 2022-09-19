def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    no_dollar_sign = d.replace("$", "")
    
    return no_dollar_sign


def percent_to_float(p):
    no_percent_sign = p.replace("%", "")
    p_to_float = float(no_percent_sign) / 100
    return p_to_float


main()