with open("sample1.txt", 'a') as file:
    for i in range(2, 13):
        for j in range(1, 11):
            print(f"{j} times {i} is {i*j}", file=file)
        print("="*30, file=file)

