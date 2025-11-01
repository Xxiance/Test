while True:
    try:
        layers = int(input("How many layers on the tree? "))
        for i in range(layers):
            print(f"{' '*(layers-i)}{'*'*i}{'*'*(i-1)}")
    except:
        print("error")
