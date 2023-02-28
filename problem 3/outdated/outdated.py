months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while true:
    date = input("Date: ")
    try:
        if (int(month) >= 1 and int(month) <= 12) and (int(day) >=1 and int(day) <= 31):
            break
    except:
        try:
            old_month, old_day, year = date.split(" ")