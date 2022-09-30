def main():
    answer = input("What time is it? ")
    time = convert(answer)
    if time >= 7 and time <= 8:
        print("Time for Lunch")


def convert(time):
    hours, minutes = time.split(":")
    new_minute = float(minutes) / 60
    return float(hours) + new_minute

if __name__ == "__main__":
    main()