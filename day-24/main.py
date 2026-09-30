with open("day-24/my_file.txt", mode="r") as file:
    content = file.read()
    print(content)

with open("day-24/new.txt", mode="w") as file:
    file.write("yaoo")