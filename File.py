with open('Values.txt', 'r', encoding="utf-8") as file:
    content = file.read()
    print(content[::-1])