def division(a, b):
    try:
        return a / b

    except ZeroDivisionError as err:
        print("run-time error:", err)