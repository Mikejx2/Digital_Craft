Width = int(input("Width? "))

Height = int(input("Height? "))

for i in range(Width):
    for j in range(Height):
        if i ==() or i ==Width-1 or j ==() or j ==Height-1:
            print("*", end = "")
        else:
            print (" ", end = "")
    print()