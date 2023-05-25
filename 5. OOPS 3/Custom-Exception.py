class ZeroDivisonError(Exception):
    pass
while True:
    try:
        num=int(input("Enter numerator:"))
        deno=int(input("Enter denominator"))
        if deno==0:
            raise ZeroDivisonError('Denominator mustnot be 0')
        value=num/deno
        print(value)
        break
    except ValueError:
        print("Numerator and Denominator should be integer")
    except ZeroDivisionError:
        print("Denominator should not be zero")
    except ZeroDivisonError:
        print("ZeroDivisonError is raised")