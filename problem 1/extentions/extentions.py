name = input("File name: ")

new_name = name.lower().strip()

if ".gif" in new_name:
    print("image/gif")