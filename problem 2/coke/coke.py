price_owed = 50

while True:

    print("Amount Due: ", price_owed)
    coin = int(input("Insert coin: " ))
    if coin in [25, 10, 5]:
        price_owed -= coin
    if price_owed <= 0:
        print("Change Owed:",abs(price_owed))
        break