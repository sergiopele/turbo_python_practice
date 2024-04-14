with open(file="day24/my_file.txt",mode = "r") as file:
        file.write("new text")
        print(file.read())