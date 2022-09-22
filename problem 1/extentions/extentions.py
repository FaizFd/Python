name = input("File name: ")

new_name = x.lower().strip()

match new_name:
      case "".endswith(".jpg"):
          print("image/jpg")