def countdown():
    for i in range(10, 0, -1):
        if i != 1:
            print(i)
        else:
            print(f"{i}...Fight!")


countdown()
