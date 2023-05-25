while True:
    try:
        num=int(input("Enter numerator:"))
        deno=int(input("Enter denominator"))
        value=num/deno
        print(value)
        break
    except ValueError:
        print("Numerator and Denominator should be integer")