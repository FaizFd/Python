grocery = {}

while True:

    try:
        item = input()

        if item in grocery:
            grocery [item] += 1

        else:
            grocey [item] = 1

     except EOFError:

        for key in grocery:
            print(key)

        break