with open("students.txt","r") as file:
    data= file.read()
    print(data)
    print(file.closed)
print(file.closed)