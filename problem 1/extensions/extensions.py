name = input("File name: ")

new_name = name.lower().strip()

if ".gif" in new_name:
    print("image/gif")
elif ".jpg" in new_name:
    print("image/jpg")
elif  ".jpeg" in new_name:
    print("image/jpeg")
elif ".png" in new_name:
    print("image/png")
elif ".pdf" in new_name:
    print("application/pdf")
elif ".txt" in new_name:
    print("text/plain")
elif ".zip" in new_name:
    print("application/zip")
else:
    print("404 not found")