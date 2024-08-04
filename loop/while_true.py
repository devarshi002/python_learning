while True:
    a = int(input("Enter a number here: "))
    b = int(input("Enter a number here: "))

    print(a + b)
    repeat = input("Do you want to stop the program : (yes/no)").strip().lower()

    if repeat in ["yes","y"]:
        break